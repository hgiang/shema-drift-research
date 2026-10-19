/* App shell: tabs, global model toggles, hash routing, keyboard shortcuts. */
(function () {
  "use strict";
  const X = window.SDX, V = window.SDXViews;
  const { D, h } = X;
  const ORDER = ["overview", "classes", "ledger", "pivot", "episodes", "dataset", "stats", "audit"];
  const root = document.getElementById("view");
  let currentView = null;

  function renderTabs(active) {
    X.mount(document.getElementById("tabs"), ORDER.map((k) =>
      h("a", { href: X.href(k), className: k === active ? "on" : "" }, V[k].title)));
  }

  function renderModelBar() {
    X.mount(document.getElementById("modelbar"), h("span", { className: "lab" }, "Models"),
      D.meta.models.map((m) => h("button", { className: "chip" + (X.isVisible(m) ? "" : " off"), onclick: () => X.toggleModel(m),
        title: "show / hide this model everywhere" }, h("span", { className: "sw", style: { background: X.modelColor(m) } }), X.modelLabel(m))));
  }

  function renderFooter() {
    X.mount(document.getElementById("foot"),
      `Built from results/analysis.json (sha256 ${D.meta.analysis_sha256.slice(0, 12)}…), ${D.meta.n_records.toLocaleString("en-US")} episodes in results/runs_*.jsonl, `,
      `and experiments/testbed_frozen.json (sha256 ${D.meta.testbed_sha256.slice(0, 12)}…). Regenerate with `, h("code", null, "python3 viz/build_explorer_data.py"), ".");
  }

  function route() {
    const r = X.parseHash();
    const name = V[r.view] ? r.view : "overview";
    X.hideTip();
    renderTabs(name);
    try {
      V[name].render(root, r);
    } catch (err) {
      console.error(err);
      X.mount(root, h("p", { className: "empty" }, `This view failed to render: ${err.message}. See the browser console for details.`));
    }
    setHeaderHeight(); // tabs and model chips are in place now
    if (currentView !== name) window.scrollTo(0, 0);
    currentView = name;
  }

  /* Publish the sticky header's real height as --top-h: it grows when the tabs or
     model chips wrap, and a fixed offset let the episode panel slide under it. */
  function setHeaderHeight() {
    const top = document.querySelector("header.top");
    if (top) document.documentElement.style.setProperty("--top-h", `${Math.ceil(top.getBoundingClientRect().height)}px`);
  }
  function syncHeaderHeight() {
    window.addEventListener("resize", setHeaderHeight);
    if (window.ResizeObserver) new ResizeObserver(setHeaderHeight).observe(document.querySelector("header.top"));
  }

  function start() {
    syncHeaderHeight();
    renderModelBar();
    renderFooter();
    X.onModelsChange(() => { renderModelBar(); route(); });
    window.addEventListener("hashchange", route);
    document.addEventListener("keydown", (e) => {
      if ((e.target instanceof Element && e.target.matches("input, select, textarea")) || e.metaKey || e.ctrlKey || e.altKey) return;
      const v = V[currentView];
      if (v && v.onKey) v.onKey(e);
    });
    route();
  }

  start();
})();
