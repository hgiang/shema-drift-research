/* Pivot: cross-tabulate any two episode fields under any filter, recomputed
   live from the raw episodes. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.pivot = (function () {
  "use strict";
  const X = window.SDX, C = window.SDXCharts, F = window.SDXFields;
  const { h, fmt } = X;
  const MAX_CALLS = 4;
  const share = (o) => (eps) => eps.filter((e) => String(e.drift_outcome) === o).length / eps.length;
  const METRICS = {
    success: { label: "success rate", calc: X.rate },
    wrong: { label: "share accepted, wrong", calc: share("ACCEPTED_WRONG"), color: X.hotColor },
    error: { label: "share error surfaced", calc: share("ERROR_SURFACED") },
    correct: { label: "share accepted, correct", calc: share("ACCEPTED_CORRECT") },
    calls: { label: "mean calls made", calc: (eps) => eps.reduce((a, e) => a + e.calls_made, 0) / eps.length,
             scale: (v) => v / MAX_CALLS, show: (v) => v.toFixed(2) },
    count: { label: "episode count", calc: (eps) => eps.length, show: (v) => String(v) },
    rowshare: { label: "share of row", calc: null, show: (v) => fmt.pct(v) }, // needs the row total, see shareOfRow
    same: { label: "share same call as silent drift", calc: (eps) => {
      const k = eps.filter((e) => e.same_as_B !== "n/a");
      return k.length ? k.filter((e) => e.same_as_B === "1").length / k.length : null; } },
  };
  const shareOfRow = (eps, rowAll) => (rowAll && rowAll.length ? eps.length / rowAll.length : null);
  const LUNA = "openai/gpt-5.6-luna", QWEN = "modal-qwen2.5-7b";
  const EXPOSED = "rename,enum_tighten,type_change";
  /* Phase 1 step 1 reading list: each preset is a pivot or an episode filter. */
  const PRESETS = [
    ["Does the diff change the call? (C vs B · strict, by model)", "pivot",
      { rows: "model", cols: "same_as_B", metric: "rowshare", cond: "C", battery: "core" }],
    ["What each model does at the drifted step under C", "pivot",
      { rows: "model", cols: "follow", metric: "rowshare", cond: "C", battery: "core" }],
    ["GPT-5.6-luna under C, by class", "pivot",
      { rows: "class", cols: "follow", metric: "count", cond: "C", model: LUNA, battery: "core" }],
    ["GPT-5.6-luna: C vs D vs silent drift, by class", "pivot",
      { rows: "class", cols: "cond", metric: "success", cond: "B_strict,C,D", model: LUNA, battery: "core" }],
    ["Full v2 schema loses the old default (D, newly required)", "pivot",
      { rows: "model", cols: "outcome", metric: "rowshare", cond: "D", class: "required", battery: "core" }],
    ["luna · C · exposed classes · identical to silent drift", "episodes",
      { model: LUNA, cond: "C", class: EXPOSED, same_as_B: "1", battery: "core" }],
    ["luna · C · calls that did change", "episodes",
      { model: LUNA, cond: "C", same_as_B: "0", battery: "core" }],
    ["Qwen · C · partly applied (type kept old unit)", "episodes",
      { model: QWEN, cond: "C", follow: "V2_PARTIAL", battery: "core" }],
    ["luna · D · newly required failures", "episodes",
      { model: LUNA, cond: "D", class: "required", success: "0", battery: "core" }],
  ];
  const DIM_KEYS = ["class", "cond", "model", "domain", "battery", "n_steps", "phrasing", "outcome", "follow", "same_as_B", "drift_tool", "task", "calls_made"];
  const FILTER_KEYS = ["model", "battery", "cond", "class", "n_steps", "outcome", "follow", "same_as_B", "domain"];
  const DEFAULTS = { rows: "class", cols: "cond", metric: "success", battery: "core" };
  const ALL = "__all__";
  const NO_FILTER = "all"; // explicit "cleared" value, so DEFAULTS do not re-apply

  function group(indices, key) {
    const f = F.FIELDS[key], m = new Map();
    indices.forEach((i) => F.valuesOf(f, X.E[i]).forEach((v) => {
      if (!m.has(v)) m.set(v, []);
      m.get(v).push(X.E[i]);
    }));
    return m;
  }

  function cube(indices, rowKey, colKey) {
    const byRow = group(indices, rowKey);
    const cells = new Map();
    byRow.forEach((eps, rv) => {
      const byCol = new Map([[ALL, eps]]);
      if (colKey) eps.forEach((e) => F.valuesOf(F.FIELDS[colKey], e).forEach((cv) => {
        if (!byCol.has(cv)) byCol.set(cv, []);
        byCol.get(cv).push(e);
      }));
      cells.set(rv, byCol);
    });
    return cells;
  }

  function toCsv(rows, cols, cells, metric) {
    const esc = (v) => `"${String(v).replace(/"/g, '""')}"`;
    const lines = [["row", ...cols.map((c) => c.label)].map(esc).join(",")];
    rows.forEach((r) => lines.push([esc(r.label), ...cols.map((c) => {
      const byCol = cells.get(r.key) || new Map(), eps = byCol.get(c.key);
      if (!eps || !eps.length) return "";
      const v = metric.calc ? metric.calc(eps) : shareOfRow(eps, byCol.get(ALL));
      return v == null ? "" : v;
    })].join(",")));
    return lines.join("\n");
  }

  function download(name, text) {
    const url = URL.createObjectURL(new Blob([text], { type: "text/csv" }));
    const a = h("a", { href: url, download: name });
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function render(root, route) {
    const p = { ...DEFAULTS, ...route.params };
    const rowKey = DIM_KEYS.includes(p.rows) ? p.rows : DEFAULTS.rows;
    const colKey = p.cols === "" || p.cols === "none" ? null : (DIM_KEYS.includes(p.cols) ? p.cols : DEFAULTS.cols);
    const metric = METRICS[p.metric] || METRICS.success;
    const filters = Object.fromEntries(FILTER_KEYS.map((k) => [k, p[k] === NO_FILTER ? "" : p[k]]));
    const update = (patch) => {
      const next = { ...p, ...patch };
      Object.keys(DEFAULTS).filter((k) => FILTER_KEYS.includes(k) && next[k] === "").forEach((k) => { next[k] = NO_FILTER; });
      X.go("pivot", next);
    };

    const indices = F.filterIndices(filters);
    const cells = cube(indices, rowKey, colKey);
    const present = (key, set) => F.FIELDS[key].values.filter((v) => set.has(v));
    const rowVals = present(rowKey, new Set(cells.keys()));
    const colSet = new Set(); cells.forEach((m) => m.forEach((_, k) => colSet.add(k)));
    const rows = rowVals.map((v) => ({ key: v, label: F.FIELDS[rowKey].fmt(v) }));
    const cols = [...(colKey ? present(colKey, colSet).map((v) => ({ key: v, label: F.FIELDS[colKey].fmt(v) })) : []),
                  { key: ALL, label: colKey ? "all" : metric.label }];
    let maxCount = 1; // count shading is relative to the largest non-margin cell
    cells.forEach((m) => m.forEach((eps, k) => { if (k !== ALL || !colKey) maxCount = Math.max(maxCount, eps.length); }));
    const select = (label, value, opts, onchange) => h("label", null, label,
      h("select", { onchange: (e) => onchange(e.target.value) }, opts.map(([v, t]) => h("option", { value: v, selected: v === value }, t))));
    const dims = DIM_KEYS.map((k) => [k, F.FIELDS[k].label]);

    const table = C.heatTable({
      corner: `${F.FIELDS[rowKey].label}${colKey ? " \\ " + F.FIELDS[colKey].label : ""}`,
      rows, cols, scale: metric.color || "seq",
      cell: (r, c) => {
        const byCol = cells.get(r.key) || new Map(), eps = byCol.get(c.key);
        if (!eps || !eps.length) return null;
        const v = metric.calc ? metric.calc(eps) : shareOfRow(eps, byCol.get(ALL));
        if (v == null) return null;
        const shade = metric.scale ? metric.scale(v) : p.metric === "count" ? v / maxCount : v;
        const drill = { ...filters, [rowKey]: r.key };
        if (colKey && c.key !== ALL) drill[colKey] = c.key;
        return { v: shade, n: eps.length, label: metric.show ? metric.show(v) : fmt.rate(v),
                 title: `${r.label}${c.key === ALL ? "" : " · " + c.label}: ${metric.show ? metric.show(v) : fmt.rate(v)} (n=${eps.length}) — click for episodes`,
                 onClick: () => X.go("episodes", drill) };
      },
    });

    X.mount(root,
      h("h2", null, "Pivot"),
      h("p", { className: "lede" }, "Cross-tabulate any two fields of the raw episodes, recomputed live. Baseline episodes count toward every drift class their model ran for that task, as in analysis.json, so a baseline row or column by class shows the paired baseline. Click a cell to read its episodes."),
      h("div", { className: "controls" },
        select("Rows", rowKey, dims, (v) => update({ rows: v })),
        select("Columns", colKey || "none", [["none", "(none)"], ...dims], (v) => update({ cols: v })),
        select("Metric", p.metric in METRICS ? p.metric : "success", Object.entries(METRICS).map(([k, m]) => [k, m.label]), (v) => update({ metric: v })),
        h("button", { onclick: () => download(`schemadrift_pivot_${rowKey}_${colKey || "all"}_${p.metric}.csv`, toCsv(rows, cols, cells, metric)) }, "Download CSV"),
        h("button", { onclick: () => X.go("pivot", {}) }, "Reset")),
      h("details", { className: "presets", open: !Object.keys(route.params).length },
        h("summary", null, "Phase 1 · reading presets (diff following)"),
        h("ol", null, PRESETS.map(([label, view, params]) => h("li", null,
          h("a", { href: X.href(view, params) }, label), h("span", { className: "mut" }, view === "pivot" ? "  pivot" : "  episodes")))),
        h("div", { className: "cap" }, "Drifted call = what the model did on the drifted parameter (labels from phase1/step1_diag_diff_following.py). ",
          "\u201cvs silent drift\u201d compares the drifted-step call with the same pair under B · strict, argument for argument.")),
      h("div", { className: "controls" }, FILTER_KEYS.map((k) => F.chipFilter(k, filters, (next) => update(next)))),
      h("div", { className: "cap" }, `${fmt.int(indices.length)} episodes match · models: ${X.models().map(X.modelLabel).join(", ")} (toggle above)`),
      indices.length ? h("div", { className: "card" }, table) : h("p", { className: "empty" }, "No episodes match these filters."));
  }

  return { title: "Pivot", render };
})();
