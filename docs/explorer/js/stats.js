/* Statistics: every paired test in analysis.json with its BH status, plus the
   robustness batteries, calling style and token accounting. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.stats = (function () {
  "use strict";
  const X = window.SDX, C = window.SDXCharts;
  const { D, h, fmt } = X;
  const A = D.analysis;
  const LEVERS = ["C", "D", "E"];
  const FAMILIES = { drop: "drop (A − B strict)", "C-B": "diff gain (C − B)", "D-B": "full-schema gain (D − B)",
                     "E-B": "retry gain (E − B)", phrasing: "phrasing shift (1 − 0)", interaction: "class × lever interaction" };

  function collectTests() {
    const survivors = new Set(A.bh.survivors);
    const rows = [];
    const push = (model, family, scope, st, label) => rows.push({
      model, family, scope, label, n: st && st.n, mean: st && st.mean, ci: st && st.ci95,
      p: st ? st.p_signflip : null, dz: st && st.dz, bh: survivors.has(label) });
    Object.entries(A.models).forEach(([m, b]) => {
      Object.entries(b.drop).forEach(([cls, st]) => push(m, "drop", cls, st, `${m}:drop:${cls}`));
      LEVERS.forEach((lv) => {
        Object.entries(b.levers[lv].vs_B).forEach(([cls, st]) => push(m, `${lv}-B`, cls, st, `${m}:${lv}-B:${cls}`));
        rows.push({ model: m, family: "interaction", scope: lv, label: `${m}:interaction:${lv}`, p: b.interaction[lv],
                    bh: survivors.has(`${m}:interaction:${lv}`) });
      });
      Object.entries(b.phrasing_battery || {}).forEach(([cond, st]) => push(m, "phrasing", cond, st, `${m}:phrasing:${cond}`));
    });
    return rows;
  }

  function testTable(params) {
    const fam = params.family || "";
    const rows = collectTests().filter((r) => X.isVisible(r.model) && (!fam || r.family === fam) && (params.bh !== "1" || r.bh));
    const scopeLabel = (r) => (r.family === "interaction" ? X.condLabel(r.scope) : r.family === "phrasing" ? X.condLabel(r.scope) : r.scope === "overall" ? "overall" : X.classLabel(r.scope));
    return h("div", null,
      h("div", { className: "controls" },
        h("label", null, "Family", h("select", { onchange: (e) => X.go("stats", { ...params, family: e.target.value }) },
          h("option", { value: "" }, "all"), Object.entries(FAMILIES).map(([k, v]) => h("option", { value: k, selected: k === fam }, v)))),
        h("label", null, "Filter", h("button", { className: "chip" + (params.bh === "1" ? " on" : ""),
          onclick: () => X.go("stats", { ...params, bh: params.bh === "1" ? "" : "1" }) }, "BH survivors only")),
        h("div", { className: "cap" }, `${rows.length} tests shown`)),
      C.sortable({ rows, sortKey: "p", sortDir: 1, columns: [
        { key: "model", label: "model", render: (r) => h("span", { style: { color: X.modelColor(r.model), fontWeight: 600 } }, X.modelLabel(r.model)) },
        { key: "family", label: "test", render: (r) => FAMILIES[r.family] || r.family },
        { key: "scope", label: "scope", get: scopeLabel },
        { key: "n", label: "n", num: true },
        { key: "mean", label: "mean diff", num: true, render: (r) => fmt.signed(r.mean) },
        { key: "ci", label: "95% CI", num: true, get: (r) => (r.ci ? r.ci[0] : null), render: (r) => fmt.ci(r.ci) },
        { key: "p", label: "p", num: true, render: (r) => fmt.p(r.p) },
        { key: "dz", label: "d_z", num: true, render: (r) => fmt.dz(r.dz) },
        { key: "bh", label: "BH", get: (r) => (r.bh ? 1 : 0), render: (r) => (r.bh ? h("span", { className: "ok" }, "survives") : h("span", { className: "mut" }, "—")) },
      ] }),
      h("div", { className: "cap" }, `Benjamini–Hochberg over the full family of ${A.bh.n_tests} tests at α = .05 (effective threshold p ≤ ${A.bh.effective_threshold}); ${A.bh.n_survive} survive. Paired within task-drift pairs; sign-flip permutation p (20,000 permutations); bootstrap CI (10,000 resamples). An empty CI/d_z means the difference was constant.`));
  }

  function robustness(models) {
    const withNoise = models.filter((m) => A.models[m].noise_floor);
    const noise = withNoise.length ? h("table", null,
      h("thead", null, h("tr", null, ["model", "pairs × 5 reps", "success flip rate", "outcome flip rate"].map((t) => h("th", null, t)))),
      h("tbody", null, withNoise.map((m) => { const n = A.models[m].noise_floor;
        return h("tr", null, h("td", null, X.modelLabel(m)), h("td", { className: "n" }, n.n_pairs), h("td", { className: "n" }, fmt.rate(n.success_flip_rate)), h("td", { className: "n" }, fmt.rate(n.outcome_flip_rate))); })))
      : h("p", { className: "empty" }, "No visible model ran the noise battery.");
    return h("div", { className: "card" }, h("h3", { style: { marginTop: 0 } }, "Noise floor (B strict, 5 repeats at temperature 0 / greedy)"), noise,
      h("div", { className: "cap" }, "Share of pairs whose success (or drift outcome) differs across the five repeats. The phrasing battery appears in the test table as \"phrasing shift\"."),
      h("button", { onclick: () => X.go("episodes", { battery: "noise" }) }, "Open noise episodes"), " ",
      h("button", { onclick: () => X.go("episodes", { battery: "phrasing" }) }, "Open phrasing episodes"));
  }

  function argStyle(models) {
    return h("div", { className: "card" }, h("h3", { style: { marginTop: 0 } }, "Calling style: optional-parameter fill rate"),
      h("table", null,
        h("thead", null, h("tr", null, ["model", "optional fill rate (A)", "B strict success, immune classes", "B strict success, exposed classes"].map((t) => h("th", null, t)))),
        h("tbody", null, models.map((m) => { const s = A.models[m].arg_style;
          return h("tr", null, h("td", null, X.modelLabel(m)), h("td", { className: "n" }, fmt.rate(s.optional_fill_rate)),
            h("td", { className: "n" }, fmt.rate(s.b_strict_success_immune_classes)), h("td", { className: "n" }, fmt.rate(s.b_strict_success_exposed_classes))); }))),
      h("div", { className: "cap" }, "A model that always fills optional parameters is mechanically immune to newly-required and default-change drift. Four points; not a trend."));
  }

  function tokenTable(models) {
    const t = A.token_costs;
    const keys = Object.keys(t.measured_prompt_tokens).filter((k) => models.some((m) => k.startsWith(m + ":")));
    return h("div", { className: "card" }, h("h3", { style: { marginTop: 0 } }, "Token accounting"),
      h("p", { className: "cap" }, `Diff artifact ${t.diff_artifact_tokens_mean.toFixed(1)} tokens vs full schema ${t.full_schema_artifact_tokens_mean.toFixed(1)} (ratio ${fmt.pct(t.ratio)}; chars/4 estimates). Measured mean input tokens per metered call, from experiments/cost_log.jsonl (self-hosted Qwen is not metered):`),
      h("table", null, h("thead", null, h("tr", null, ["model", "condition", "mean prompt tokens", "calls"].map((x) => h("th", null, x)))),
        h("tbody", null, keys.map((k) => { const i = k.lastIndexOf(":"); const v = t.measured_prompt_tokens[k];
          return h("tr", null, h("td", null, X.modelLabel(k.slice(0, i))), h("td", null, X.condLabel(k.slice(i + 1))), h("td", { className: "n" }, v.mean.toFixed(1)), h("td", { className: "n" }, v.n)); }))));
  }

  function render(root, route) {
    const models = X.models();
    X.mount(root,
      h("h2", null, "Statistics"),
      h("p", { className: "lede" }, "Every inferential number in results/analysis.json, sortable and filterable. Nothing here is recomputed."),
      testTable(route.params),
      h("div", { className: "grid2" }, robustness(models), argStyle(models)),
      tokenTable(models));
  }

  return { title: "Statistics", render };
})();
