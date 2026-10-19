/* Overview: headline success matrix, condition profile, drop and recovery. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.overview = (function () {
  "use strict";
  const X = window.SDX, C = window.SDXCharts;
  const { D, h, fmt } = X;
  const LEVERS = ["C", "D", "E"];

  function headline(models) {
    return h("div", { className: "card" },
      C.heatTable({
        corner: "model \\ condition",
        rows: models.map((m) => ({ key: m, label: X.modelLabel(m), swatch: X.modelColor(m) })),
        cols: D.meta.conds.map((c) => ({ key: c, label: X.condLabel(c) })),
        cell: (r, c) => ({
          v: D.analysis.models[r.key].success_rate[c.key],
          title: `${X.modelLabel(r.key)} · ${X.condLabel(c.key)} — click for episodes. ${X.condDesc(c.key)}`,
          onClick: () => X.go("episodes", { model: r.key, cond: c.key, battery: "core" }),
        }),
      }),
      h("div", { className: "cap" }, "Task success per condition, from ",
        h("code", null, "analysis.json → models/<model>/success_rate"),
        ". Click any cell to open those episodes. Gemini models are scored on 240 task-drift pairs (Flash, Qwen) or 120 (Pro, luna)."));
  }

  function profile(models) {
    const series = models.map((m) => ({ key: m, label: X.modelLabel(m), color: X.modelColor(m) }));
    return h("div", { className: "card" },
      C.legend(series.map((se) => ({ label: se.label, color: se.color, round: true }))),
      C.dotStrip({
        rows: D.meta.conds.map((c) => ({ key: c, label: X.condLabel(c) })),
        series, value: (r, se) => D.analysis.models[se.key].success_rate[r.key],
        onClick: (r, se) => X.go("episodes", { model: se.key, cond: r.key, battery: "core" }),
      }),
      h("div", { className: "cap" }, "Each dot is one model's success rate under one condition. The two Gemini models jump back up under the diff (C); GPT-5.6-luna and Qwen do not."));
  }

  function dropForest(models) {
    const rows = models.map((m) => {
      const d = D.analysis.models[m].drop.overall;
      return { label: X.modelLabel(m), mean: d.mean, lo: d.ci95[0], hi: d.ci95[1], color: X.modelColor(m),
               title: `n=${d.n} pairs · p ${fmt.p(d.p_signflip)} · d_z ${fmt.dz(d.dz)}` };
    });
    return h("div", { className: "card" }, h("h3", null, "Drop: baseline − silent drift (strict)"),
      C.forest({ rows, domain: [0, 1], width: 520 }),
      h("div", { className: "cap" }, "Paired drop with bootstrap 95% CI (10,000 resamples)."));
  }

  function recoveryForest(models) {
    const rows = [];
    LEVERS.forEach((lv) => {
      rows.push({ label: X.condLabel(lv), mean: null });
      models.forEach((m) => {
        const r = D.analysis.models[m].levers[lv].recovery_fraction.overall;
        const g = D.analysis.models[m].levers[lv].vs_B.overall;
        rows.push({ label: X.modelLabel(m), mean: r.point, lo: r.ci95[0], hi: r.ci95[1], color: X.modelColor(m),
                    title: `${X.condLabel(lv)} vs silent drift: +${fmt.rate(g.mean)} success, p ${fmt.p(g.p_signflip)}; recovers ${fmt.pct(r.point)} of the drop` });
      });
    });
    return h("div", { className: "card" }, h("h3", null, "Recovery fraction per lever"),
      C.forest({ rows, domain: [-0.25, 1.1], width: 520, ref: 1, refLabel: "full recovery" }),
      h("div", { className: "cap" }, "(lever − silent drift) ÷ (baseline − silent drift), with bootstrap CI. 1.0 means the lever restores baseline."));
  }

  function tokens() {
    const t = D.analysis.token_costs;
    return h("div", { className: "stats" },
      [["30", "tools"], ["120", "frozen tasks"], ["5", "drift classes"], [fmt.int(D.meta.n_records), "episodes"],
       [Math.round(t.diff_artifact_tokens_mean), "diff tokens (mean)"],
       [Math.round(t.full_schema_artifact_tokens_mean), "full-schema tokens"],
       [fmt.pct(t.ratio), "diff / full schema"], [D.analysis.bh.n_survive + " / " + D.analysis.bh.n_tests, "tests survive BH"]]
        .map(([v, k]) => h("div", { className: "stat" }, h("span", { className: "v" }, v), h("span", { className: "k" }, k))));
  }

  function render(root) {
    const models = X.models();
    X.mount(root,
      h("h2", null, "Overview"),
      h("p", { className: "lede" }, "SchemaDrift-120 applies one schema change at a time to 30 tools and asks four model families to complete 120 checkable tasks without being told. Explore the headline numbers here, then drill into drift classes, the outcome ledger, raw episodes, the testbed itself, or every statistical test."),
      tokens(),
      h("h3", null, "Success by condition"), headline(models),
      profile(models),
      h("div", { className: "grid2" }, dropForest(models), recoveryForest(models)));
  }

  return { title: "Overview", render };
})();
