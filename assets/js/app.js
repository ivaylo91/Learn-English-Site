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
  if (menuBtn && menu) {
    menuBtn.addEventListener("click", function () {
      var open = menu.classList.toggle("hidden") === false;
      menuBtn.setAttribute("aria-expanded", String(open));
    });
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
