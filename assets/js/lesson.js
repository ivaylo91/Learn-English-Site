(function () {
  "use strict";

  var root = document.querySelector("[data-lesson-player]");
  var dataEl = document.getElementById("exercises-data");
  if (!root || !dataEl) return;

  var exercises = JSON.parse(dataEl.textContent);
  var csrf = root.querySelector("input[name=csrfmiddlewaretoken]").value;
  var checkUrl = root.dataset.checkUrl;
  var completeUrl = root.dataset.completeUrl;

  var screens = {
    start: root.querySelector('[data-screen="start"]'),
    exercise: root.querySelector('[data-screen="exercise"]'),
    result: root.querySelector('[data-screen="result"]'),
  };
  var el = {
    progress: root.querySelector("[data-progress]"),
    counter: root.querySelector("[data-counter]"),
    instruction: root.querySelector("[data-instruction]"),
    prompt: root.querySelector("[data-prompt]"),
    area: root.querySelector("[data-answer-area]"),
    feedback: root.querySelector("[data-feedback]"),
    check: root.querySelector('[data-action="check"]'),
    next: root.querySelector('[data-action="next"]'),
    speakPrompt: root.querySelector('[data-action="speak-prompt"]'),
  };

  var index = 0;
  var answers = {};
  var current = null; // current answer value
  var checking = false;

  function show(name) {
    Object.keys(screens).forEach(function (k) { screens[k].hidden = k !== name; });
  }

  function post(url, body) {
    return fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-CSRFToken": csrf },
      body: JSON.stringify(body),
      credentials: "same-origin",
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    });
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function renderPrompt(ex) {
    var html = escapeHtml(ex.prompt).replace(
      /_{3,}/g,
      '<span class="mx-1 inline-block min-w-16 border-b-2 border-brand-600 align-baseline dark:border-brand-400">&nbsp;</span>'
    );
    el.prompt.innerHTML = html;
  }

  function setCurrent(value) {
    current = value;
    el.check.disabled = value === null || String(value).trim() === "";
  }

  function renderExercise() {
    var ex = exercises[index];
    current = null;
    el.check.disabled = true;
    el.check.hidden = false;
    el.next.hidden = true;
    el.feedback.className = "mt-5 hidden rounded-xl px-4 py-3";
    el.feedback.innerHTML = "";
    el.counter.textContent = index + 1 + " / " + exercises.length;
    el.progress.style.width = (index / exercises.length) * 100 + "%";
    el.instruction.textContent = ex.instruction;
    renderPrompt(ex);
    el.area.innerHTML = "";

    // Read the English prompt aloud (not for Bulgarian translate prompts).
    el.speakPrompt.hidden = !(window.govori && window.govori.canSpeak) || ex.type === "translate";

    if (ex.type === "choice") {
      var list = document.createElement("div");
      list.className = "grid gap-3";
      list.setAttribute("role", "radiogroup");
      ex.choices.forEach(function (c, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "option";
        b.dataset.choice = c.id;
        b.setAttribute("role", "radio");
        b.setAttribute("aria-checked", "false");
        b.innerHTML = '<span class="font-mono text-sm text-stone-500">' + (i + 1) + "</span>" + escapeHtml(c.text);
        b.addEventListener("click", function () {
          if (checking || !el.next.hidden) return;
          list.querySelectorAll(".option").forEach(function (o) {
            o.classList.remove("is-selected");
            o.setAttribute("aria-checked", "false");
          });
          b.classList.add("is-selected");
          b.setAttribute("aria-checked", "true");
          setCurrent(String(c.id));
        });
        list.appendChild(b);
      });
      el.area.appendChild(list);
    } else {
      var input = document.createElement(ex.type === "translate" ? "textarea" : "input");
      input.className = "field-input text-lg";
      input.setAttribute("autocomplete", "off");
      input.setAttribute("autocapitalize", "off");
      input.setAttribute("spellcheck", "false");
      input.setAttribute("lang", "en");
      input.setAttribute("aria-label", "Твоят отговор");
      input.placeholder = ex.type === "translate" ? "Напиши превода на английски" : "Напиши липсващата дума";
      if (ex.type === "translate") input.rows = 2;
      input.addEventListener("input", function () { setCurrent(input.value); });
      input.addEventListener("keydown", function (e) {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          if (!el.next.hidden) el.next.click();
          else if (!el.check.disabled) el.check.click();
        }
      });
      el.area.appendChild(input);
      setTimeout(function () { input.focus(); }, 50);
    }
  }

  function showFeedback(res) {
    var ok = res.correct;
    el.feedback.className =
      "mt-5 rounded-xl px-4 py-3 " +
      (ok
        ? "bg-emerald-50 text-emerald-950 dark:bg-emerald-950/50 dark:text-emerald-100"
        : "bg-red-50 text-red-950 dark:bg-red-950/50 dark:text-red-100");
    var html =
      '<p class="font-semibold"><i class="fa-solid ' + (ok ? "fa-circle-check" : "fa-circle-xmark") +
      ' mr-2" aria-hidden="true"></i>' + (ok ? "Вярно!" : "Не съвсем.") + "</p>";
    if (!ok && res.correct_answer) {
      html += '<p class="mt-1">Правилен отговор: <strong lang="en">' + escapeHtml(res.correct_answer) + "</strong></p>";
    }
    if (res.explanation) html += '<p class="mt-1 text-sm opacity-90">' + escapeHtml(res.explanation) + "</p>";
    el.feedback.innerHTML = html;
  }

  el.check.addEventListener("click", function () {
    if (checking || current === null) return;
    var ex = exercises[index];
    checking = true;
    el.check.disabled = true;
    post(checkUrl, { exercise: ex.id, answer: current })
      .then(function (res) {
        answers[ex.id] = current;
        if (ex.type === "choice") {
          el.area.querySelectorAll(".option").forEach(function (o) {
            o.classList.remove("is-selected");
            if (String(o.dataset.choice) === String(res.correct_choice)) o.classList.add("is-correct");
            else if (o.dataset.choice === current) o.classList.add("is-wrong");
          });
        } else {
          var input = el.area.querySelector(".field-input");
          input.readOnly = true;
          input.classList.add(res.correct ? "!border-emerald-600" : "!border-red-600");
        }
        if (res.correct && window.govori && ex.type !== "translate") {
          // Speak the completed sentence for reinforcement.
          var answerText = ex.type === "choice"
            ? (ex.choices.find(function (c) { return String(c.id) === String(res.correct_choice); }) || {}).text
            : res.correct_answer;
          window.govori.speak(ex.prompt.replace(/_{3,}/g, answerText || ""));
        }
        showFeedback(res);
        el.check.hidden = true;
        el.next.hidden = false;
        el.next.focus();
      })
      .catch(function () {
        el.check.disabled = false;
        el.feedback.className = "mt-5 rounded-xl bg-red-50 px-4 py-3 text-red-950 dark:bg-red-950/50 dark:text-red-100";
        el.feedback.textContent = "Няма връзка със сървъра. Опитай отново.";
      })
      .finally(function () { checking = false; });
  });

  el.next.addEventListener("click", function () {
    index += 1;
    if (index < exercises.length) renderExercise();
    else finish();
  });

  el.speakPrompt.addEventListener("click", function () {
    if (window.govori) window.govori.speak(exercises[index].prompt.replace(/_{3,}/g, "blank"));
  });

  // Keyboard: 1-9 picks a choice
  document.addEventListener("keydown", function (e) {
    if (screens.exercise.hidden || e.target.matches("input, textarea")) return;
    var n = parseInt(e.key, 10);
    if (n >= 1 && n <= 9) {
      var opt = el.area.querySelectorAll(".option")[n - 1];
      if (opt) opt.click();
    } else if (e.key === "Enter") {
      if (!el.next.hidden) { e.preventDefault(); el.next.click(); }
      else if (!el.check.disabled) { e.preventDefault(); el.check.click(); }
    }
  });

  function finish() {
    el.progress.style.width = "100%";
    post(completeUrl, { answers: answers })
      .then(renderResult)
      .catch(function () {
        renderResult(null);
      });
  }

  function renderResult(res) {
    show("result");
    var icon = root.querySelector("[data-result-icon]");
    var title = root.querySelector("[data-result-title]");
    var score = root.querySelector("[data-result-score]");
    var text = root.querySelector("[data-result-text]");
    var stats = root.querySelector("[data-result-stats]");
    stats.innerHTML = "";
    if (!res) {
      icon.className = "mx-auto grid size-16 place-items-center rounded-2xl bg-stone-100 text-3xl text-stone-600 dark:bg-stone-800";
      icon.innerHTML = '<i class="fa-solid fa-wifi" aria-hidden="true"></i>';
      title.textContent = "Резултатът не беше записан";
      score.textContent = "";
      text.textContent = "Провери връзката си и опитай пак.";
      return;
    }
    if (res.passed) {
      icon.className = "mx-auto grid size-16 place-items-center rounded-2xl bg-emerald-100 text-3xl text-emerald-600 dark:bg-emerald-950 dark:text-emerald-400";
      icon.innerHTML = '<i class="fa-solid fa-trophy" aria-hidden="true"></i>';
      title.textContent = res.score === 100 ? "Перфектно!" : "Браво, урокът е завършен!";
    } else {
      icon.className = "mx-auto grid size-16 place-items-center rounded-2xl bg-amber-100 text-3xl text-amber-600 dark:bg-amber-950 dark:text-amber-400";
      icon.innerHTML = '<i class="fa-solid fa-dumbbell" aria-hidden="true"></i>';
      title.textContent = "Още малко упражнение";
    }
    score.textContent = res.score + "%";
    text.textContent = res.correct + " от " + res.total + " верни отговора." + (res.passed ? "" : " Прочети отново теорията и опитай пак.");

    function stat(iconCls, label, cls) {
      var s = document.createElement("span");
      s.className = "badge text-sm " + cls;
      s.innerHTML = '<i class="fa-solid ' + iconCls + '" aria-hidden="true"></i>' + label;
      stats.appendChild(s);
    }
    if (res.saved && res.xp) stat("fa-bolt", "+" + res.xp + " XP", "badge-brand");
    if (res.saved && res.streak) stat("fa-fire", res.streak + (res.streak === 1 ? " ден поред" : " дни поред"), "bg-orange-100 text-orange-800 dark:bg-orange-950 dark:text-orange-200");
  }

  function start() {
    index = 0;
    answers = {};
    show("exercise");
    renderExercise();
    screens.exercise.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  root.querySelector('[data-action="start"]').addEventListener("click", start);
  root.querySelector('[data-action="restart"]').addEventListener("click", start);
})();
