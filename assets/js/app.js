(function () {
  "use strict";

  // Theme toggle
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dark = document.documentElement.classList.toggle("dark");
      try { localStorage.setItem("theme", dark ? "dark" : "light"); } catch (e) {}
    });
  });

  // Mobile menu
  var menuBtn = document.querySelector("[data-menu-toggle]");
  var menu = document.getElementById("mobile-menu");
  function setMenu(open) {
    menu.classList.toggle("hidden", !open);
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.setAttribute("aria-label", open ? "Затвори менюто" : "Отвори менюто");
    menuBtn.querySelector("[data-icon-open]").hidden = open;
    menuBtn.querySelector("[data-icon-close]").hidden = !open;
  }
  if (menuBtn && menu) {
    menuBtn.addEventListener("click", function () { setMenu(menu.classList.contains("hidden")); });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menu.classList.contains("hidden")) { setMenu(false); menuBtn.focus(); }
    });
    // Close when the layout switches to the desktop nav.
    window.matchMedia("(min-width: 1024px)").addEventListener("change", function (e) { if (e.matches) setMenu(false); });
  }

  // Close <details> dropdowns on outside click / Escape
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details[data-dropdown][open]").forEach(function (d) {
      if (!d.contains(e.target)) d.removeAttribute("open");
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      document.querySelectorAll("details[data-dropdown][open]").forEach(function (d) { d.removeAttribute("open"); });
    }
  });

  // Text to speech (Web Speech API)
  var voice = null;
  function pickVoice() {
    if (!("speechSynthesis" in window)) return;
    var voices = window.speechSynthesis.getVoices();
    voice =
      voices.find(function (v) { return v.lang === "en-GB"; }) ||
      voices.find(function (v) { return v.lang === "en-US"; }) ||
      voices.find(function (v) { return /^en/i.test(v.lang); }) ||
      null;
  }
  if ("speechSynthesis" in window) {
    pickVoice();
    window.speechSynthesis.addEventListener("voiceschanged", pickVoice);
  }

  function speak(text, rate) {
    if (!("speechSynthesis" in window) || !text) return false;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = voice ? voice.lang : "en-GB";
    if (voice) u.voice = voice;
    u.rate = rate || 0.9;
    window.speechSynthesis.speak(u);
    return true;
  }
  window.govori = { speak: speak, canSpeak: "speechSynthesis" in window };

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-speak]");
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();
    speak(btn.getAttribute("data-speak"), btn.hasAttribute("data-speak-slow") ? 0.6 : undefined);
  });
  if (!("speechSynthesis" in window)) {
    document.querySelectorAll("[data-speak]").forEach(function (b) { b.hidden = true; });
  }

  // Small toast message at the bottom of the screen
  var toastTimer = null;
  function toast(text, icon) {
    var el = document.getElementById("toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "toast";
      el.setAttribute("role", "status");
      el.className = "fixed inset-x-4 bottom-6 z-50 mx-auto flex w-fit max-w-sm items-center gap-2 rounded-2xl bg-stone-900 px-4 py-3 text-sm font-bold text-white shadow-xl transition-[opacity,transform] duration-300 dark:bg-white dark:text-stone-900";
      document.body.appendChild(el);
    }
    el.innerHTML = '<i class="fa-solid ' + (icon || "fa-circle-check") + ' text-amber-400" aria-hidden="true"></i><span></span>';
    el.querySelector("span").textContent = text;
    el.style.opacity = "1";
    el.style.transform = "none";
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      el.style.opacity = "0";
      el.style.transform = "translateY(8px)";
    }, 2200);
  }

  function csrfToken() {
    var input = document.querySelector("input[name=csrfmiddlewaretoken]");
    return input ? input.value : "";
  }

  function postJSON(url, body) {
    return fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-CSRFToken": csrfToken() },
      body: JSON.stringify(body || {}),
      credentials: "same-origin",
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    });
  }
  window.govori.toast = toast;
  window.govori.postJSON = postJSON;

  // Save words for review
  function setSaved(btn, saved) {
    btn.setAttribute("aria-pressed", String(saved));
    btn.querySelector("[data-on]").hidden = !saved;
    btn.querySelector("[data-off]").hidden = saved;
  }
  document.querySelectorAll("[data-save-word]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      postJSON(btn.getAttribute("data-save-word"))
        .then(function (res) {
          setSaved(btn, res.saved);
          toast(res.saved ? "Запазено за преговор" : "Премахнато от преговора", res.saved ? "fa-bookmark" : "fa-trash-can");
        })
        .catch(function () { toast("Нещо се обърка. Опитай пак.", "fa-triangle-exclamation"); });
    });
  });
  var saveAll = document.querySelector("[data-save-all]");
  if (saveAll) {
    saveAll.addEventListener("click", function () {
      postJSON(saveAll.getAttribute("data-save-all"))
        .then(function (res) {
          document.querySelectorAll("[data-save-word]").forEach(function (b) { setSaved(b, true); });
          toast("Всички думи са в преговора (" + res.deck_size + " общо)", "fa-bookmark");
        })
        .catch(function () { toast("Нещо се обърка. Опитай пак.", "fa-triangle-exclamation"); });
    });
  }

  // Category filter chips (level pages): show only lessons of one category, hide empty sections.
  var filterGroup = document.querySelector("[data-filter-group]");
  var filterTarget = document.querySelector("[data-filter-target]");
  if (filterGroup && filterTarget) {
    filterGroup.querySelectorAll("[data-filter]").forEach(function (chip) {
      chip.addEventListener("click", function () {
        var key = chip.getAttribute("data-filter");
        filterGroup.querySelectorAll("[data-filter]").forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
        filterTarget.querySelectorAll("[data-category]").forEach(function (item) {
          item.hidden = !!key && item.getAttribute("data-category") !== key;
        });
        filterTarget.querySelectorAll("[data-filter-section]").forEach(function (section) {
          section.hidden = !section.querySelector("[data-category]:not([hidden])");
        });
      });
    });
  }

  // Show / hide password
  document.querySelectorAll("[data-password-toggle]").forEach(function (btn) {
    var input = document.getElementById(btn.getAttribute("data-password-toggle"));
    if (!input) return;
    btn.addEventListener("click", function () {
      var show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.setAttribute("aria-pressed", String(show));
      btn.setAttribute("aria-label", show ? "Скрий паролата" : "Покажи паролата");
      btn.querySelector("[data-eye]").hidden = show;
      btn.querySelector("[data-eye-off]").hidden = !show;
    });
  });

  // Landing page mini quiz
  var demo = document.querySelector("[data-demo-quiz]");
  if (demo) {
    demo.querySelectorAll("[data-demo-option]").forEach(function (opt) {
      opt.addEventListener("click", function () {
        var right = opt.getAttribute("data-demo-option") === "right";
        demo.querySelectorAll("[data-demo-option]").forEach(function (o) {
          o.classList.remove("is-correct", "is-wrong");
          if (o.getAttribute("data-demo-option") === "right" && right) o.classList.add("is-correct");
        });
        opt.classList.add(right ? "is-correct" : "is-wrong");
        demo.querySelectorAll("[data-demo-feedback]").forEach(function (f) {
          f.classList.toggle("hidden", f.getAttribute("data-demo-feedback") !== (right ? "right" : "wrong"));
        });
        if (right) speak("She is a doctor.");
      });
    });
  }
})();
