/* Episode browser: filter all 4,800 logged episodes and open one in detail. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.episodes = (function () {
  "use strict";
  const X = window.SDX, F = window.SDXFields;
  const { h, fmt } = X;
  const PAGE = 50;
  const FILTER_KEYS = ["model", "battery", "cond", "class", "outcome", "follow", "same_as_B", "success", "n_steps", "domain"];
  const PASS_KEYS = ["task", "drift_tool", "phrasing", "calls_made"]; // set by drill-downs, shown as removable chips
  let current = { indices: [], params: {} };

  function row(i, selected, params) {
    const e = X.E[i];
    return h("tr", { className: "click" + (i === selected ? " sel" : ""), onclick: () => X.go("episodes", { ...params, i }) },
      h("td", { className: "n mut" }, i),
      h("td", null, h("span", { className: "sw", style: { background: X.modelColor(e.model), display: "inline-block", width: "8px", height: "8px", borderRadius: "50%", marginRight: "6px" } }), X.modelLabel(e.model)),
      h("td", { className: "n" }, e.task, e.battery === "core" ? "" : h("span", { className: "mut" }, ` ${e.battery}${e.rep ? " r" + e.rep : ""}`)),
      h("td", null, e.cond === "A" ? h("span", { className: "mut" }, "—") : X.classLabel(e.class)),
      h("td", null, X.condShort(e.cond)),
      h("td", { className: "outc" }, h("span", { className: "tag " + String(e.drift_outcome) }, X.outcomeLabel(e.drift_outcome)),
        e.follow === "n/a" ? null
          : h("span", { className: "tag fl-" + e.follow, title: X.followDesc(e.follow) }, X.followLabel(e.follow),
              e.same_as_B === "1" ? " = B" : "")),
      h("td", { className: e.success ? "ok" : "bad", style: { fontWeight: 700 } }, e.success ? "✓" : "✗"));
  }

  function activeChips(params) {
    const keys = PASS_KEYS.filter((k) => params[k]);
    if (!keys.length) return null;
    return h("div", { className: "chipgroup", style: { marginBottom: "10px" } }, keys.map((k) =>
      h("button", { className: "chip on", onclick: () => X.go("episodes", { ...params, [k]: "", page: "" }) },
        `${F.FIELDS[k].label}: ${params[k]} ✕`)));
  }

  function list(params, indices, selected) {
    const pages = Math.max(1, Math.ceil(indices.length / PAGE));
    const page = Math.min(pages, Math.max(1, Number(params.page) || 1));
    const slice = indices.slice((page - 1) * PAGE, page * PAGE);
    const nav = (pg) => X.go("episodes", { ...params, page: pg });
    const pager = h("div", { className: "pager" },
      h("button", { disabled: page <= 1, onclick: () => nav(page - 1) }, "‹"),
      `page ${page} / ${pages} · ${fmt.int(indices.length)} episodes`,
      h("button", { disabled: page >= pages, onclick: () => nav(page + 1) }, "›"));
    const sr = X.rate(indices.map((i) => X.E[i]));
    return h("div", null, pager,
      h("div", { className: "cap", style: { marginTop: 0 } }, `success rate of this selection: ${fmt.rate(sr)}`),
      h("div", { className: "tablewrap" }, h("table", { className: "compact" },
        h("thead", null, h("tr", null, ["#", "model", "task", "class", "cond.", "outcome · drifted call", ""].map((t) => h("th", null, t)))),
        h("tbody", null, slice.map((i) => row(i, selected, params))))),
      slice.length ? pager : h("p", { className: "empty" }, "No episodes match these filters."));
  }

  function step(delta) {
    const { indices, params } = current;
    const pos = indices.indexOf(Number(params.i));
    const next = indices[pos < 0 ? 0 : pos + delta];
    if (next == null) return;
    const page = Math.floor(indices.indexOf(next) / PAGE) + 1;
    X.go("episodes", { ...params, i: next, page });
  }

  function render(root, route) {
    const params = { ...route.params };
    const filterParams = Object.fromEntries([...FILTER_KEYS, ...PASS_KEYS, "q"].map((k) => [k, params[k]]));
    const indices = F.filterIndices(filterParams);
    const selected = params.i != null && X.E[Number(params.i)] ? Number(params.i) : null;
    current = { indices, params };
    const update = (next) => X.go("episodes", { ...next, page: "", i: params.i });
    const search = h("input", { type: "search", placeholder: "task, tool, error text, phrasing…", value: params.q || "",
      onchange: (e) => update({ ...params, q: e.target.value }) });

    X.mount(root,
      h("h2", null, "Episodes"),
      h("p", { className: "lede" }, "Every deduplicated episode in results/runs_*.jsonl. Open one to see the exact prompt and tool declarations the model received (rebuilt with harness.build_condition), the executor's response, and each accepted call compared field by field with ground truth. Use j / k to step through the list."),
      h("div", { className: "controls" }, FILTER_KEYS.map((k) => F.chipFilter(k, params, update)),
        h("label", null, "Search", search),
        h("button", { onclick: () => X.go("episodes", {}) }, "Clear filters")),
      activeChips(params),
      h("div", { className: "split" },
        list(params, indices, selected),
        h("div", { className: "card detail" }, selected != null
          ? window.SDXDetail.render(selected, { onPrev: () => step(-1), onNext: () => step(1), params })
          : h("p", { className: "empty" }, "Select an episode on the left."))));
  }

  function onKey(e) {
    if (e.key === "j") step(1);
    else if (e.key === "k") step(-1);
  }

  return { title: "Episodes", render, onKey };
})();
