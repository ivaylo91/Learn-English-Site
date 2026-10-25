(function () {
  "use strict";

  var root = document.querySelector("[data-dialogue]");
  var dataEl = document.getElementById("dialogue-data");
  if (!root || !dataEl) return;

  var lines = JSON.parse(dataEl.textContent);
  var playBtn = root.querySelector("[data-dialogue-play]");
  var transcript = root.querySelector("[data-transcript]");
  var toggleText = root.querySelector("[data-toggle-transcript]");
  var toggleTr = root.querySelector("[data-toggle-translation]");
  var rate = 0.95;
  var playing = false;
  var token = 0; // invalidates callbacks from a stopped run

  // Transcript / translation toggles
  if (toggleText) {
    toggleText.addEventListener("click", function () {
      var show = transcript.hidden;
      transcript.hidden = !show;
      toggleText.setAttribute("aria-expanded", String(show));
      toggleText.querySelector("span").textContent = show ? "Скрий текста" : "Покажи текста";
      if (toggleTr) toggleTr.hidden = !show;
    });
  }
  if (toggleTr) {
    toggleTr.addEventListener("click", function () {
      var show = toggleTr.getAttribute("aria-pressed") !== "true";
      toggleTr.setAttribute("aria-pressed", String(show));
      toggleTr.querySelector("span").textContent = show ? "Скрий превода" : "Покажи превода";
      transcript.querySelectorAll("[data-translation]").forEach(function (el) { el.hidden = !show; });
    });
  }

  // Speed
  root.querySelectorAll("[data-rate]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      rate = parseFloat(btn.getAttribute("data-rate"));
      root.querySelectorAll("[data-rate]").forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
    });
  });

  if (!playBtn) return;
  if (!("speechSynthesis" in window)) {
    playBtn.disabled = true;
    playBtn.title = "Браузърът не поддържа синтез на реч.";
    return;
  }

  // Pick up to two distinct English voices so speakers sound different.
  function englishVoices() {
    var all = window.speechSynthesis.getVoices().filter(function (v) { return /^en[-_]/i.test(v.lang); });
    all.sort(function (a, b) { return (b.lang === "en-GB") - (a.lang === "en-GB"); });
    return all;
  }

  function setActive(index) {
    transcript.querySelectorAll("[data-bubble]").forEach(function (b, i) {
      if (i === index) b.setAttribute("data-active", "");
      else b.removeAttribute("data-active");
    });
  }

  function setPlaying(on) {
    playing = on;
    playBtn.querySelector("[data-icon-play]").hidden = on;
    playBtn.querySelector("[data-icon-stop]").hidden = !on;
    playBtn.setAttribute("aria-label", on ? "Спри диалога" : "Пусни диалога");
    if (!on) setActive(-1);
  }

  function stop() {
    token += 1;
    window.speechSynthesis.cancel();
    setPlaying(false);
  }

  function play() {
    var run = ++token;
    var voices = englishVoices();
    window.speechSynthesis.cancel();
    setPlaying(true);

    function speakLine(i) {
      if (run !== token) return;
      if (i >= lines.length) { setPlaying(false); return; }
      var line = lines[i];
      var u = new SpeechSynthesisUtterance(line.en);
      var voice = voices.length ? voices[line.who % Math.min(voices.length, 2)] : null;
      if (voice) { u.voice = voice; u.lang = voice.lang; } else { u.lang = "en-GB"; }
      // Same voice for both speakers? Shift pitch so they still differ.
      if (voices.length < 2) u.pitch = line.who % 2 ? 0.8 : 1.15;
      u.rate = rate;
      u.onstart = function () { if (run === token) setActive(i); };
      u.onend = function () { setTimeout(function () { speakLine(i + 1); }, 350); };
      u.onerror = function () { if (run === token) setPlaying(false); };
      window.speechSynthesis.speak(u);
    }
    speakLine(0);
  }

  playBtn.addEventListener("click", function () {
    if (playing) stop();
    else play();
  });
  window.addEventListener("pagehide", stop);
})();
