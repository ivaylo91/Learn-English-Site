(function () {
  "use strict";

  // List / cards tabs
  var tabs = document.querySelectorAll("[data-tab]");
  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      tabs.forEach(function (t) { t.setAttribute("aria-selected", String(t === tab)); });
      document.querySelectorAll("[data-panel]").forEach(function (p) {
        p.hidden = p.getAttribute("data-panel") !== tab.getAttribute("data-tab");
      });
    });
  });

  var root = document.querySelector("[data-flashcards]");
  var dataEl = document.getElementById("cards-data");
  if (!root || !dataEl) return;

  var cards = JSON.parse(dataEl.textContent);
  if (!cards.length) return;

  var card = root.querySelector("[data-fc-card]");
  var front = root.querySelector("[data-fc-front]");
  var frontSub = root.querySelector("[data-fc-front-sub]");
  var back = root.querySelector("[data-fc-back]");
  var backSub = root.querySelector("[data-fc-back-sub]");
  var counter = root.querySelector("[data-fc-counter]");
  var reverse = root.querySelector("[data-fc-reverse]");
  var index = 0;

  function render() {
    var c = cards[index];
    var bgFirst = reverse.checked;
    card.classList.remove("is-flipped");
    // Wait for the flip back before swapping text so the answer is not revealed.
    setTimeout(function () {
      front.textContent = bgFirst ? c.bg : c.en;
      front.lang = bgFirst ? "bg" : "en";
      frontSub.textContent = bgFirst ? "" : c.ipa || "";
      back.textContent = bgFirst ? c.en : c.bg;
      back.lang = bgFirst ? "en" : "bg";
      backSub.textContent = c.exEn ? c.exEn + (c.exBg ? " (" + c.exBg + ")" : "") : "";
    }, card.dataset.ready ? 150 : 0);
    card.dataset.ready = "1";
    counter.textContent = index + 1 + " / " + cards.length;
  }

  function go(delta) {
    index = (index + delta + cards.length) % cards.length;
    render();
  }

  card.addEventListener("click", function () {
    var flipped = card.classList.toggle("is-flipped");
    // Speak English when it becomes visible.
    if (window.govori && flipped === reverse.checked) window.govori.speak(cards[index].en);
  });
  root.querySelector("[data-fc-next]").addEventListener("click", function () { go(1); });
  root.querySelector("[data-fc-prev]").addEventListener("click", function () { go(-1); });
  root.querySelector("[data-fc-speak]").addEventListener("click", function () {
    if (window.govori) window.govori.speak(cards[index].en);
  });
  root.querySelector("[data-fc-shuffle]").addEventListener("click", function () {
    for (var i = cards.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = cards[i]; cards[i] = cards[j]; cards[j] = t;
    }
    index = 0;
    render();
  });
  reverse.addEventListener("change", render);

  document.addEventListener("keydown", function (e) {
    if (root.hidden || e.target.matches("input, textarea")) return;
    if (e.key === "ArrowRight") go(1);
    else if (e.key === "ArrowLeft") go(-1);
    else if (e.key === " " && document.activeElement !== card) { e.preventDefault(); card.click(); }
  });

  render();
})();
