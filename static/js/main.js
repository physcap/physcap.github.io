// PhysCaP project page interactions (plain JS, no framework).
(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  // ---------- top bar: solid after the first screen, current section, progress ----------
  const topbar = $("#topbar");
  const hero = $(".hero");
  const progress = $("#progress");
  const navLinks = $$("#section-nav a");
  const label = $("#current-label");
  const sections = navLinks.map((a) => $(a.getAttribute("href"))).filter(Boolean);

  function onScroll() {
    const y = window.scrollY;
    topbar.classList.toggle("is-solid", y > hero.offsetHeight - 70);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (max > 0 ? (100 * y) / max : 0) + "%";
    let current = null;
    for (const s of sections) if (s.getBoundingClientRect().top <= 90) current = s;
    navLinks.forEach((a) => a.classList.toggle("is-current", current && a.getAttribute("href") === "#" + current.id));
    if (label) label.textContent = current ? current.dataset.nav : "";
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  // ---------- clickable framework figure ----------
  const stage = $("#method-stage");
  const panel = $("#module-panel");
  let activeModule = null;
  function setModule(id) {
    activeModule = id;
    $$(".focus", stage).forEach((g) => g.classList.toggle("is-active", g.dataset.focus === id));
    $$(".hotspot", stage).forEach((b) => b.classList.toggle("is-active", b.dataset.module === id));
    $$(".module-tab").forEach((b) => {
      b.classList.toggle("is-active", b.dataset.module === id);
      b.setAttribute("aria-selected", b.dataset.module === id ? "true" : "false");
    });
    $("[data-default]", panel).hidden = !!id;
    $$("[data-module-text]", panel).forEach((d) => (d.hidden = d.dataset.moduleText !== id));
  }
  $$(".hotspot, .module-tab").forEach((b) =>
    b.addEventListener("click", (e) => {
      e.stopPropagation();
      setModule(activeModule === b.dataset.module ? null : b.dataset.module);
    })
  );
  document.addEventListener("click", (e) => {
    if (activeModule && !e.target.closest("#method-stage, .module-tabs, #module-panel")) setModule(null);
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { setModule(null); closeModal(); }
  });

  // ---------- task buttons ----------
  const taskButtons = $$(".task-button");
  function activateTask(id) {
    taskButtons.forEach((b) => {
      const on = b.dataset.task === id;
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-selected", on ? "true" : "false");
    });
    $$(".task-panel").forEach((p) => {
      const on = p.dataset.taskPanel === id;
      p.hidden = !on;
      $$("video", p).forEach((v) => (on ? null : v.pause()));
    });
  }
  taskButtons.forEach((b, i) => {
    b.addEventListener("click", () => activateTask(b.dataset.task));
    b.addEventListener("keydown", (e) => {
      const d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
      if (!d) return;
      const next = taskButtons[(i + d + taskButtons.length) % taskButtons.length];
      next.focus();
      activateTask(next.dataset.task);
    });
  });

  // ---------- method switch inside a task ----------
  $$(".task-panel").forEach((p) => {
    const video = $(".task-video", p);
    const badge = $(".speed-badge", p);
    const desc = $(".method-desc", p);
    $$(".method-select button", p).forEach((b) =>
      b.addEventListener("click", () => {
        $$(".method-select button", p).forEach((x) => x.classList.toggle("is-active", x === b));
        const wasPlaying = video && !video.paused;
        video.poster = "static/videos/" + b.dataset.video + ".jpg";
        video.querySelector("source").src = "static/videos/" + b.dataset.video + ".mp4";
        video.load();
        if (wasPlaying) video.play();
        badge.hidden = !b.dataset.speed;
        badge.textContent = b.dataset.speed;
        desc.textContent = b.title;
      })
    );
    const cur = $("[data-code-current]", p);
    if (cur)
      cur.addEventListener("click", () => {
        const b = $(".method-select button.is-active", p);
        if (b && b.dataset.code) openCode(b.dataset.code, b.dataset.codeTitle);
        else openText("No generated code", "Generated code is not available for this method.");
      });
  });

  // ---------- results tabs ----------
  function openTab(id) {
    $$(".tab").forEach((t) => t.classList.toggle("is-active", t.dataset.tab === id));
    $$(".tab-panel").forEach((p) => (p.hidden = p.dataset.tabPanel !== id));
  }
  $$(".tab").forEach((t) => t.addEventListener("click", () => openTab(t.dataset.tab)));
  $$("[data-open-tab]").forEach((a) => a.addEventListener("click", () => openTab(a.dataset.openTab)));

  // ---------- code / prompt viewer ----------
  const modal = $("#code-modal");
  const modalTitle = $("#code-modal-title");
  const modalBody = $("#code-modal-body");
  function show(title, text, lang) {
    modalTitle.textContent = title;
    modalBody.className = lang ? "language-" + lang : "";
    modalBody.textContent = text;
    modalBody.parentElement.classList.toggle("wrap", lang !== "python");
    if (window.hljs && lang) window.hljs.highlightElement(modalBody);
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }
  function openText(title, text) { show(title, text, null); }
  function openCode(file, title) {
    const lang = file.endsWith(".py") ? "python" : "markdown";
    fetch("static/code/" + file)
      .then((r) => (r.ok ? r.text() : Promise.reject(r.status)))
      .then((t) => show(title, t, lang))
      .catch(() => show(title, "Could not load " + file + ".", null));
  }
  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }
  $$("[data-close]", modal).forEach((b) => b.addEventListener("click", closeModal));
  $$("[data-code]").forEach((b) => {
    if (b.closest(".method-select")) return;
    b.addEventListener("click", () => openCode(b.dataset.code, b.dataset.title));
  });
  $("#code-copy").addEventListener("click", () => copy(modalBody.textContent, $("#code-copy")));

  // ---------- copy buttons ----------
  function copy(text, btn) {
    navigator.clipboard.writeText(text).then(() => {
      const old = btn.innerHTML;
      btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied';
      setTimeout(() => (btn.innerHTML = old), 1500);
    });
  }
  $$("[data-copy]").forEach((b) => b.addEventListener("click", () => copy($(b.dataset.copy).textContent, b)));
})();
