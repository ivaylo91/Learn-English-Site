(function () {
  "use strict";

  var root = document.querySelector("[data-review]");
  var dataEl = document.getElementById("review-data");
  if (!root || !dataEl) return;

  var cards = JSON.parse(dataEl.textContent);
  // URL template ends with /0/; swap in each card's id.
  var answerUrl = root.dataset.answerUrl.replace(/0\/$/, "");
  var el = {
    stage: root.querySelector("[data-stage]"),
    done: root.querySelector("[data-done]"),
    card: root.querySelector("[data-card]"),
    front: root.querySelector("[data-front]"),
    ipa: root.querySelector("[data-ipa]"),
    back: root.querySelector("[data-back]"),
    example: root.querySelector("[data-example]"),
    topic: root.querySelector("[data-topic]"),
    reveal: root.querySelector("[data-reveal]"),
    answers: root.querySelector("[data-answers]"),
    progress: root.querySelector("[data-progress]"),
    counter: root.querySelector("[data-counter]"),
    summary: root.querySelector("[data-summary]"),
  };
  var index = 0;
  var knew = 0;
  var xp = 0;
  var busy = false;

  function speak(text) {
    if (window.govori) window.govori.speak(text);
  }

  function show() {
    var c = cards[index];
    el.card.classList.remove("is-flipped");
    el.answers.hidden = true;
    el.reveal.hidden = false;
    el.counter.textContent = index + 1 + " / " + cards.length;
    el.progress.style.width = (index / cards.length) * 100 + "%";
    setTimeout(function () {
      el.topic.textContent = c.topic + ", кутия " + c.box;
      el.front.textContent = c.en;
      el.ipa.textContent = c.ipa || "";
      el.back.textContent = c.bg;
      el.example.textContent = c.exEn ? c.exEn + (c.exBg ? " (" + c.exBg + ")" : "") : "";
    }, index ? 150 : 0);
    speak(c.en);
  }

  function reveal() {
    el.card.classList.add("is-flipped");
    el.reveal.hidden = true;
    el.answers.hidden = false;
    el.answers.querySelector('[data-knew="1"]').focus();
  }

  function answer(value) {
    if (busy) return;
    busy = true;
    var c = cards[index];
    window.govori
      .postJSON(answerUrl + c.id + "/", { knew: value })
      .then(function (res) {
        if (value) knew += 1;
        xp += res.xp;
        index += 1;
        if (index < cards.length) show();
        else finish();
      })
      .catch(function () {
        window.govori.toast("Няма връзка. Опитай пак.", "fa-triangle-exclamation");
      })
      .finally(function () { busy = false; });
  }

  function finish() {
    el.progress.style.width = "100%";
    el.stage.hidden = true;
    el.done.hidden = false;
    el.summary.textContent =
      "Знаеше " + knew + " от " + cards.length + " думи" + (xp ? ", +" + xp + " XP." : ".") +
      (knew < cards.length ? " Думите, които не се сети, ще се върнат утре." : "");
  }

  el.card.addEventListener("click", function () {
    if (el.card.classList.contains("is-flipped")) el.card.classList.remove("is-flipped");
    else reveal();
  });
  el.reveal.addEventListener("click", reveal);
  el.answers.querySelectorAll("[data-knew]").forEach(function (b) {
    b.addEventListener("click", function () { answer(b.getAttribute("data-knew") === "1"); });
  });
  document.addEventListener("keydown", function (e) {
    if (!el.done.hidden) return;
    if (e.key === " " || e.key === "Enter") {
      if (el.answers.hidden) { e.preventDefault(); reveal(); }
    } else if (!el.answers.hidden && (e.key === "1" || e.key === "ArrowLeft")) answer(false);
    else if (!el.answers.hidden && (e.key === "2" || e.key === "ArrowRight")) answer(true);
  });

  show();
})();
