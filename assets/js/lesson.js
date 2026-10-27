(function () {
  "use strict";

  var root = document.querySelector("[data-lesson-player]");
  var dataEl = document.getElementById("exercises-data");
  if (!root || !dataEl) return;

  // Original set from the server; `exercises` is the live queue (missed items are re-queued once).
  var original = JSON.parse(dataEl.textContent);
  var exercises = original.slice();
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
    tag: root.querySelector("[data-tag]"),
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
    el.tag.innerHTML = "";
    if (ex.retry || ex.review) {
      var tag = document.createElement("span");
      tag.className = "badge " + (ex.retry
        ? "bg-red-100 text-red-800 dark:bg-red-500/15 dark:text-red-200"
        : "bg-violet-100 text-violet-800 dark:bg-violet-500/15 dark:text-violet-200");
      tag.innerHTML = '<i class="fa-solid ' + (ex.retry ? "fa-rotate-left" : "fa-clock-rotate-left") + '" aria-hidden="true"></i><span></span>';
      tag.querySelector("span").textContent = ex.retry ? "Опитай пак" : "Преговор: " + ex.review;
      el.tag.appendChild(tag);
    }
    renderPrompt(ex);
    el.area.innerHTML = "";

    // Read the English prompt aloud (not for Bulgarian prompts or audio exercises).
    var canSpeak = !!(window.govori && window.govori.canSpeak);
    el.speakPrompt.hidden = !canSpeak || ex.type === "translate" || ex.type === "dictation" || ex.type === "order" || !!ex.audio;

    if (ex.audio) {
      el.area.appendChild(audioBar(ex.audio, canSpeak));
      if (canSpeak) setTimeout(function () { window.govori.speak(ex.audio); }, 250);
    }

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
    } else if (ex.type === "order") {
      el.area.appendChild(orderBuilder(ex.words || []));
    } else if (ex.type === "speak") {
      el.area.appendChild(speakBuilder(ex));
    } else {
      var long = ex.type === "translate" || ex.type === "dictation";
      var input = document.createElement(long ? "textarea" : "input");
      input.className = "field-input text-lg";
      input.setAttribute("autocomplete", "off");
      input.setAttribute("autocapitalize", "off");
      input.setAttribute("spellcheck", "false");
      input.setAttribute("lang", "en");
      input.setAttribute("aria-label", "Твоят отговор");
      input.placeholder = {
        translate: "Напиши превода на английски",
        dictation: "Напиши каквото чуваш",
      }[ex.type] || "Напиши липсващата дума";
      if (long) input.rows = 2;
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

  // Speaking exercise: say the sentence aloud; the browser's speech recognition transcribes it.
  var Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;

  function normWords(text) {
    return String(text || "").toLowerCase().replace(/[’‘]/g, "'").replace(/[.,!?;:"]/g, "").split(/\s+/).filter(Boolean);
  }

  function speakBuilder(ex) {
    var wrap = document.createElement("div");
    wrap.className = "rounded-2xl bg-indigo-50 p-4 dark:bg-indigo-500/10";
    if (!Recognition) {
      // No speech recognition (e.g. Firefox): practise aloud and self-check.
      wrap.innerHTML =
        '<p class="text-sm font-semibold text-indigo-900 dark:text-indigo-100">Браузърът ти не разпознава реч (опитай с Chrome, Edge или Safari). Кажи изречението на глас и потвърди.</p>' +
        '<button type="button" class="btn btn-secondary btn-sm mt-3" data-self-check><i class="fa-solid fa-check text-indigo-500" aria-hidden="true"></i>Казах го на глас</button>';
      wrap.querySelector("[data-self-check]").addEventListener("click", function () { setCurrent(ex.prompt); });
      return wrap;
    }
    wrap.innerHTML =
      '<div class="flex items-center gap-4">' +
      '<button type="button" class="grid size-16 shrink-0 place-items-center rounded-full bg-indigo-500 text-2xl text-white shadow-[0_4px_0_0_var(--color-indigo-700)] active:translate-y-[3px] active:shadow-[0_1px_0_0_var(--color-indigo-700)] data-[listening]:animate-pulse data-[listening]:bg-red-500" data-mic aria-label="Говори"><i class="fa-solid fa-microphone" aria-hidden="true"></i></button>' +
      '<div class="min-w-0 flex-1"><p class="text-sm font-bold text-indigo-900 dark:text-indigo-100" data-mic-status>Натисни микрофона и кажи изречението.</p>' +
      '<p class="mt-1 text-lg font-semibold" lang="en" data-heard></p></div></div>';
    var mic = wrap.querySelector("[data-mic]");
    var status = wrap.querySelector("[data-mic-status]");
    var heard = wrap.querySelector("[data-heard]");
    var target = normWords(ex.prompt);

    function score(text) {
      var w = normWords(text);
      return w.filter(function (x) { return target.indexOf(x) !== -1; }).length - Math.abs(w.length - target.length) * 0.5;
    }

    mic.addEventListener("click", function () {
      if (!el.next.hidden) return;
      var rec = new Recognition();
      rec.lang = "en-GB";
      rec.interimResults = false;
      rec.maxAlternatives = 3;
      mic.setAttribute("data-listening", "");
      status.textContent = "Слушам...";
      rec.onresult = function (e) {
        // Pick the alternative closest to the target sentence.
        var alts = Array.prototype.slice.call(e.results[0]).map(function (a) { return a.transcript; });
        alts.sort(function (a, b) { return score(b) - score(a); });
        heard.textContent = "„" + alts[0] + "“";
        status.textContent = "Чух:";
        setCurrent(alts[0]);
      };
      rec.onerror = function (e) {
        status.textContent = e.error === "not-allowed"
          ? "Няма достъп до микрофона. Разреши го в настройките на браузъра."
          : "Не чух ясно. Опитай пак.";
      };
      rec.onend = function () { mic.removeAttribute("data-listening"); };
      rec.start();
    });
    return wrap;
  }

  // After checking a spoken answer, colour each target word: green if heard, red if missed.
  function showWordFeedback(ex, heardText) {
    var heardWords = normWords(heardText);
    var line = document.createElement("p");
    line.className = "mt-3 flex flex-wrap gap-1.5 text-lg font-bold";
    line.lang = "en";
    ex.prompt.split(/\s+/).forEach(function (word) {
      var ok = heardWords.indexOf(normWords(word)[0]) !== -1;
      var span = document.createElement("span");
      span.className = "rounded-lg px-2 py-0.5 " + (ok
        ? "bg-emerald-100 text-emerald-800 dark:bg-emerald-500/15 dark:text-emerald-200"
        : "bg-red-100 text-red-800 underline decoration-wavy dark:bg-red-500/15 dark:text-red-200");
      span.textContent = word;
      line.appendChild(span);
    });
    return line;
  }

  // Word-order exercise: tap tiles to build the sentence, tap again to remove.
  function orderBuilder(words) {
    var wrap = document.createElement("div");
    wrap.innerHTML =
      '<div class="flex min-h-16 flex-wrap items-center gap-2 rounded-2xl border-2 border-dashed border-stone-300 p-3 dark:border-stone-700" data-line aria-label="Твоето изречение"></div>' +
      '<div class="mt-4 flex flex-wrap gap-2" data-bank aria-label="Думи"></div>';
    var line = wrap.querySelector("[data-line]");
    var bank = wrap.querySelector("[data-bank]");
    var baseCls = "rounded-xl border-2 border-b-4 px-3.5 py-2 text-base font-bold transition-transform active:translate-y-0.5 ";
    var tileCls = baseCls + "border-stone-200 bg-white disabled:opacity-30 dark:border-stone-700 dark:bg-stone-900";
    var placedCls = baseCls + "border-brand-300 bg-brand-50 text-brand-900 dark:border-brand-500/40 dark:bg-brand-500/10 dark:text-brand-100";

    function update() {
      var picked = Array.prototype.map.call(line.children, function (t) { return t.textContent; });
      setCurrent(picked.length === words.length ? picked.join(" ") : "");
    }

    words.forEach(function (word, i) {
      var tile = document.createElement("button");
      tile.type = "button";
      tile.className = tileCls;
      tile.textContent = word;
      tile.lang = "en";
      tile.addEventListener("click", function () {
        if (!el.next.hidden) return;
        var placed = document.createElement("button");
        placed.type = "button";
        placed.className = placedCls;
        placed.textContent = word;
        placed.lang = "en";
        placed.addEventListener("click", function () {
          if (!el.next.hidden) return;
          placed.remove();
          tile.disabled = false;
          update();
        });
        line.appendChild(placed);
        tile.disabled = true;
        update();
      });
      bank.appendChild(tile);
    });
    return wrap;
  }

  // Big play button plus a slow replay, for exercises with audio.
  function audioBar(text, canSpeak) {
    var bar = document.createElement("div");
    bar.className = "mb-5 flex items-center gap-3 rounded-2xl bg-rose-50 p-3 dark:bg-rose-500/10";
    if (!canSpeak) {
      bar.innerHTML = '<p class="text-sm font-semibold">Браузърът ти не поддържа звук. Текстът е: <strong lang="en"></strong></p>';
      bar.querySelector("strong").textContent = text;
      return bar;
    }
    bar.innerHTML =
      '<button type="button" class="grid size-14 place-items-center rounded-full bg-rose-500 text-xl text-white shadow-[0_4px_0_0_var(--color-rose-700)] active:translate-y-[3px] active:shadow-[0_1px_0_0_var(--color-rose-700)]" data-play aria-label="Чуй отново"><i class="fa-solid fa-volume-high" aria-hidden="true"></i></button>' +
      '<button type="button" class="grid size-11 place-items-center rounded-full bg-white text-rose-600 dark:bg-stone-900 dark:text-rose-300" data-play-slow aria-label="Чуй бавно"><i class="fa-solid fa-person-walking" aria-hidden="true"></i></button>' +
      '<span class="text-sm font-bold text-rose-800 dark:text-rose-200">Натисни, за да чуеш отново</span>';
    bar.querySelector("[data-play]").addEventListener("click", function () { window.govori.speak(text); });
    bar.querySelector("[data-play-slow]").addEventListener("click", function () { window.govori.speak(text, 0.6); });
    return bar;
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
        // Score uses the first attempt; a missed item comes back once at the end.
        if (!ex.retry) answers[ex.id] = current;
        if (!res.correct && !ex.retry) exercises.push(Object.assign({}, ex, { retry: true }));
        if (ex.type === "choice") {
          el.area.querySelectorAll(".option").forEach(function (o) {
            o.classList.remove("is-selected");
            if (String(o.dataset.choice) === String(res.correct_choice)) o.classList.add("is-correct");
            else if (o.dataset.choice === current) o.classList.add("is-wrong");
          });
        } else if (ex.type === "speak") {
          var box = el.area.firstElementChild;
          if (box && Recognition) box.appendChild(showWordFeedback(ex, current));
        } else if (ex.type === "order") {
          var line = el.area.querySelector("[data-line]");
          line.classList.remove("border-dashed");
          line.classList.add(res.correct ? "!border-emerald-500" : "!border-red-500");
        } else {
          var input = el.area.querySelector(".field-input");
          input.readOnly = true;
          input.classList.add(res.correct ? "!border-emerald-600" : "!border-red-600");
        }
        if (res.correct && window.govori && ex.type !== "translate" && ex.type !== "order" && ex.type !== "speak" && !ex.audio) {
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
    exercises = original.slice();
    show("exercise");
    renderExercise();
    screens.exercise.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  root.querySelector('[data-action="start"]').addEventListener("click", start);
  root.querySelector('[data-action="restart"]').addEventListener("click", start);
})();
