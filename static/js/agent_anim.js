// Agent structure animation: one Identify Empty Can episode through Planner -> Prioritizer -> Coding Agent.
// Each step has a fixed final state (render). Moving forward one step also plays a short motion (play).
(function () {
  "use strict";
  const root = document.getElementById("agent-anim");
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const $$ = (s) => Array.from(root.querySelectorAll(s));
  const stage = $("#aa-stage");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const CAN = { green: "green can", red: "red can", blue: "blue can", black: "black can" };
  const fn = (name) => `<span class="f">${name}</span>`;
  const str = (s) => `<span class="s">"${s}"</span>`;
  const MEASURE = (can) => [
    `<span class="c"># measure the top-ranked candidate</span>`,
    `mass = ${fn("get_mass")}(${str(CAN[can])})`,
    `${fn("print")}(<span class="s">f"Mass: {mass} kg"</span>)`,
  ];
  const FINAL = [
    `<span class="c"># enough evidence: complete the task</span>`,
    `can_pos, can_quat = <span class="f p">get_object_pose</span>(${str("red can")})`,
    `tray_pos, tray_quat = <span class="f p">get_object_pose</span>(${str("wooden tray")})`,
    `<span class="f b">open_gripper</span>()`,
    `<span class="f b">goto_pose</span>(can_pos, can_quat, z_approach=0.1)`,
    `<span class="f b">close_gripper</span>()`,
    `<span class="f b">goto_pose</span>(tray_pos, tray_quat)`,
    `<span class="f b">open_gripper</span>()`,
  ];

  // Final state of each step.
  const STEPS = [
    { label: "Task", active: ["task"],
      caption: "The agent receives a task in natural language and an image of the scene. Which can is empty cannot be seen in the image." },
    { label: "Planner", active: ["planner"], cands: true,
      planner: "Which can is empty? That depends on <b>mass</b>, which is missing.<br>Let&rsquo;s weigh the cans and find out.",
      caption: "The <b>Planner</b> identifies the missing physical information (mass) and proposes candidate interactions: measure the mass of each can." },
    { label: "Prioritizer", active: ["prioritizer"], cands: true, rank: "sorted",
      prior: "Maybe weigh the opened cans first.",
      caption: "The <b>Prioritizer</b> scores each candidate with a short reason and reorders the list. The two opened cans (with straws) go first; the sealed cans get low scores." },
    { label: "Measure", active: ["coding"], cands: true, rank: "sorted", sent: ["green"], cur: "green",
      code: MEASURE("green"), result: "208 g",
      caption: "The <b>Coding Agent</b> writes code that calls the PhysX module <code>get_mass</code> on the top-ranked can. The robot lifts it: 208 g." },
    { label: "Update", active: ["belief", "planner"], cands: true, rank: "sorted", sent: ["green"], cur: "green",
      code: MEASURE("green"), result: "208 g", belief: ["green"],
      planner: "Green can: 208 g, not empty.<br>Not enough evidence yet, so keep exploring.",
      caption: "The measurement updates the <b>system belief</b>. The Planner checks it: the green can is full, so exploration continues." },
    { label: "Measure", active: ["coding"], cands: true, rank: "sorted", sent: ["green", "red"], cur: "red",
      code: MEASURE("red"), result: "15 g", belief: ["green"],
      planner: "Green can: 208 g, not empty.<br>Not enough evidence yet, so keep exploring.",
      caption: "The next candidate in the Prioritizer&rsquo;s order, the red can, is sent to the Coding Agent: 15 g." },
    { label: "Stop", active: ["belief", "planner"], cands: true, rank: "sorted", sent: ["green", "red"], cur: "red",
      code: MEASURE("red"), result: "15 g", belief: ["green", "red"],
      planner: "Red can: 15 g, below 0.1 kg, so it is the empty can.<br><b>Enough evidence: stop exploring.</b>",
      caption: "The Planner acts as a stopping criterion: the red can is empty, so it ends exploration. The two sealed cans are never measured." },
    { label: "Code policy", active: ["coding", "result"], cands: true, rank: "sorted", sent: ["green", "red"],
      code: FINAL, belief: ["green", "red"], done: true,
      planner: "Red can: 15 g, below 0.1 kg, so it is the empty can.<br><b>Enough evidence: stop exploring.</b>",
      caption: "Grounded by the measurements, the Coding Agent writes the final code policy: pick up the red can and place it on the wooden tray. Two objects interacted with instead of four." },
  ];
  const BELIEF = { green: "green can: 0.208 kg &rarr; not empty", red: "red can: 0.015 kg &rarr; <b>empty</b>" };

  let step = 0, playing = true, timer = null, runId = 0, visible = false;
  const ABORT = Symbol("abort");
  const sleep = (ms, id) => new Promise((res, rej) => setTimeout(() => (id === runId ? res() : rej(ABORT)), reduce ? 0 : ms));

  // ---------- helpers ----------
  const panel = (n) => $(`[data-panel="${n}"]`);
  function rel(el) {
    const a = stage.getBoundingClientRect(), r = el.getBoundingClientRect();
    return { x: r.left - a.left, y: r.top - a.top, w: r.width, h: r.height };
  }

  // ---------- static rendering of a step ----------
  function setCode(lines) {
    $("#aa-code").innerHTML = (lines || []).map((l) => `<span class="ln">${l}</span>`).join("");
  }
  function sortRank(sorted) {
    const ol = $("#aa-rank");
    const items = $$("#aa-rank li");
    const order = sorted ? items.slice().sort((a, b) => b.dataset.score - a.dataset.score)
      : ["blue", "black", "green", "red"].map((c) => items.find((li) => li.dataset.can === c));
    order.forEach((li) => ol.appendChild(li));
  }
  function render(i) {
    const s = STEPS[i];
    $$(".aa-panel").forEach((p) => {
      p.classList.toggle("is-active", s.active.includes(p.dataset.panel));
      p.classList.toggle("is-seen", STEPS.slice(0, i + 1).some((t) => t.active.includes(p.dataset.panel)));
    });
    $("#aa-cands").classList.toggle("is-on", !!s.cands);
    const rank = $("#aa-rank");
    rank.classList.toggle("is-on", !!s.rank);
    rank.classList.toggle("is-scored", s.rank === "sorted");
    sortRank(s.rank === "sorted");
    $$("#aa-rank li").forEach((li) => {
      li.classList.toggle("is-low", s.rank === "sorted" && li.dataset.score < 5);
      li.classList.toggle("is-sent", (s.sent || []).includes(li.dataset.can));
      li.classList.toggle("is-current", li.dataset.can === s.cur);
    });
    $("#aa-planner-say").innerHTML = s.planner || "";
    $("#aa-planner-say").classList.toggle("is-on", !!s.planner);
    $("#aa-prior-say").innerHTML = s.prior || (s.rank ? "Maybe weigh the opened cans first." : "");
    $("#aa-prior-say").classList.toggle("is-on", !!s.rank);
    setCode(s.code);
    $("#aa-result").innerHTML = s.result ? `<i class="fa-solid fa-weight-hanging"></i> ${s.result}` : "";
    $("#aa-result").classList.toggle("is-on", !!s.result);
    const b = s.belief || [];
    $("#aa-belief").innerHTML = b.length ? b.map((c) => `<li><img src="static/images/can_${c}.png" alt="">${BELIEF[c]}</li>`).join("")
      : `<li class="aa-empty">no measurements yet</li>`;
    $('[data-panel="result"]').classList.toggle("is-done", !!s.done);
    $("#aa-caption").innerHTML = `<b class="aa-stepno">Step ${i + 1}/${STEPS.length}</b> ${s.caption}`;
    $$("#aa-steps button").forEach((btn, k) => {
      btn.classList.toggle("is-current", k === i);
      btn.classList.toggle("is-past", k < i);
    });
  }

  // ---------- motion ----------
  function fly(fromEl, toEl, html, ms = 650) {
    if (reduce || !fromEl || !toEl) return Promise.resolve();
    const a = rel(fromEl), b = rel(toEl);
    const d = document.createElement("div");
    d.className = "aa-fly";
    d.innerHTML = html;
    d.style.left = a.x + a.w / 2 + "px";
    d.style.top = a.y + a.h / 2 + "px";
    stage.appendChild(d);
    d.getBoundingClientRect();
    d.style.transition = `transform ${ms}ms cubic-bezier(.5,0,.2,1), opacity 200ms ${ms - 150}ms`;
    d.style.transform = `translate(-50%,-50%) translate(${b.x + b.w / 2 - (a.x + a.w / 2)}px, ${b.y + b.h / 2 - (a.y + a.h / 2)}px)`;
    d.style.opacity = "0.98";
    return new Promise((res) => setTimeout(() => { d.remove(); res(); }, ms + 60));
  }
  const canImg = (c) => `<img src="static/images/can_${c}.png" alt="">`;
  async function typeCode(lines, id) {
    setCode([]);
    const code = $("#aa-code");
    for (const l of lines) {
      code.insertAdjacentHTML("beforeend", `<span class="ln is-new">${l}</span>`);
      await sleep(260, id);
    }
  }

  const PLAY = {
    1: async (id) => {
      render(0);
      panelOn("planner");
      await fly($("#aa-task-say"), panel("planner"), `<div class="aa-say aa-user"><i class="fa-solid fa-user"></i><span>Find the empty can.</span></div>`);
      await sleep(150, id);
      render(1);
      $$("#aa-cands img").forEach((im, k) => { im.classList.add("pop"); im.style.animationDelay = k * 120 + "ms"; });
    },
    2: async (id) => {
      render(1);
      panelOn("prioritizer");
      const imgs = $$("#aa-cands img");
      await Promise.all(imgs.map((im, k) => sleep(k * 90, id).then(() => fly(im, $("#aa-rank"), canImg(im.dataset.can), 600))));
      // rows appear in the Planner's order, then get scores, then are reordered
      const rank = $("#aa-rank");
      sortRank(false);
      rank.classList.add("is-on");
      $("#aa-prior-say").classList.remove("is-on");
      await sleep(700, id);
      rank.classList.add("is-scored");
      await sleep(900, id);
      const items = $$("#aa-rank li");
      const before = new Map(items.map((li) => [li, li.getBoundingClientRect().top]));
      sortRank(true);
      items.forEach((li) => {
        const dy = before.get(li) - li.getBoundingClientRect().top;
        li.style.transition = "none";
        li.style.transform = `translateY(${dy}px)`;
        li.getBoundingClientRect();
        li.style.transition = "transform 600ms cubic-bezier(.4,0,.2,1), opacity 300ms";
        li.style.transform = "";
      });
      await sleep(650, id);
      render(2);
    },
    3: async (id) => { await sendAndMeasure("green", 2, 3, id); },
    4: async (id) => { await update("green", 3, 4, id); },
    5: async (id) => { await sendAndMeasure("red", 4, 5, id); },
    6: async (id) => { await update("red", 5, 6, id); },
    7: async (id) => {
      render(6);
      panelOn("coding");
      $("#aa-result").classList.remove("is-on");
      await typeCode(FINAL, id);
      await fly(panel("coding"), panel("result"), `<div class="aa-say aa-robot"><i class="fa-solid fa-robot"></i><span>Execute</span></div>`);
      render(7);
    },
  };
  function panelOn(name) {
    $$(".aa-panel").forEach((p) => p.classList.toggle("is-active", p.dataset.panel === name));
  }
  async function sendAndMeasure(can, from, to, id) {
    render(from);
    panelOn("coding");
    const li = $(`#aa-rank li[data-can="${can}"]`);
    $$("#aa-rank li").forEach((x) => x.classList.toggle("is-current", x === li));
    li.classList.add("is-sent");
    await fly(li.querySelector("img"), panel("coding"), canImg(can));
    $("#aa-result").classList.remove("is-on");
    await typeCode(STEPS[to].code, id);
    await sleep(400, id);
    render(to);
    $("#aa-result").classList.add("pop");
  }
  async function update(can, from, to, id) {
    render(from);
    panelOn("belief");
    await fly($("#aa-result"), panel("belief"), `<div class="aa-result is-on">${STEPS[from].result}</div>`);
    const s = STEPS[to];
    $("#aa-belief").innerHTML = s.belief.map((c) => `<li${c === can ? ' class="pop"' : ""}><img src="static/images/can_${c}.png" alt="">${BELIEF[c]}</li>`).join("");
    await sleep(500, id);
    panelOn("planner");
    await fly(panel("belief"), panel("planner"), `<div class="aa-chip">${BELIEF[can]}</div>`);
    render(to);
    $("#aa-planner-say").classList.add("pop");
  }

  // ---------- playback ----------
  const DWELL = [2600, 3200, 3000, 2600, 3600, 2600, 3600, 6000];
  async function go(i, animate) {
    clearTimeout(timer);
    const id = ++runId;
    step = (i + STEPS.length) % STEPS.length;
    try {
      if (animate && PLAY[step] && !reduce) await PLAY[step](id);
      else render(step);
    } catch (e) {
      if (e !== ABORT) throw e;
      return;
    }
    if (id === runId) schedule();
  }
  function schedule() {
    clearTimeout(timer);
    if (playing && visible) timer = setTimeout(() => go(step + 1, step + 1 < STEPS.length), DWELL[step]);
  }
  function setPlaying(p) {
    playing = p;
    $(".aa-play i").className = p ? "fa-solid fa-pause" : "fa-solid fa-play";
    if (p) schedule(); else clearTimeout(timer);
  }

  const stepsBox = $("#aa-steps");
  STEPS.forEach((s, k) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = s.label;
    b.addEventListener("click", () => { setPlaying(false); go(k, false); });
    stepsBox.appendChild(b);
  });
  root.addEventListener("click", (e) => {
    const b = e.target.closest("[data-aa]");
    if (!b) return;
    const a = b.dataset.aa;
    if (a === "play") setPlaying(!playing);
    if (a === "next") { setPlaying(false); go(step + 1, step + 1 < STEPS.length); }
    if (a === "prev") { setPlaying(false); go(step - 1, false); }
    if (a === "replay") { go(0, false); setPlaying(true); }
  });

  new IntersectionObserver((es) => {
    visible = es[0].isIntersecting;
    if (visible) schedule(); else clearTimeout(timer);
  }, { threshold: 0.35 }).observe(root);
  render(0);
})();
