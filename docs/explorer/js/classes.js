/* Drift classes (per-class success, drop, lever gains) and the outcome ledger. */
window.SDXViews = window.SDXViews || {};
(function () {
  "use strict";
  const X = window.SDX, C = window.SDXCharts;
  const { D, h, fmt } = X;
  const DRIFT_CONDS = ["B_strict", "B_lenient", "C", "D", "E"];
  const LEVERS = ["C", "D", "E"];
  const OUTCOMES = ["ERROR_SURFACED", "ACCEPTED_CORRECT", "ACCEPTED_WRONG", null];
  const LEDGER_KEY = { ERROR_SURFACED: "error_surfaced", ACCEPTED_CORRECT: "accepted_correct",
                       ACCEPTED_WRONG: "accepted_wrong", null: "no_call" };
  const EXAMPLE_TOOL = "book_flight";

  function condPicker(view, current, extra) {
    return h("div", { className: "chipgroup" }, DRIFT_CONDS.map((c) =>
      h("button", { className: "chip" + (c === current ? " on" : ""), onclick: () => X.go(view, { ...extra, cond: c }) }, X.condLabel(c))));
  }

  function classCards() {
    return h("div", { className: "grid4" }, D.meta.classes.map((cls) => {
      const diff = D.testbed.diffs[`${EXAMPLE_TOOL}::${cls}`];
      return h("div", { className: "card" }, h("h3", { style: { marginTop: 0 } }, X.classLabel(cls)),
        h("div", { className: "cap", style: { marginTop: 0 } }, X.classDesc(cls)),
        diff ? h("details", null, h("summary", null, `Example diff (${EXAMPLE_TOOL})`), X.jsonPre(diff.changes)) : null);
    }));
  }

  function classHeat(models, cond) {
    return C.heatTable({
      corner: "class \\ model",
      rows: D.meta.classes.map((c) => ({ key: c, label: X.classLabel(c) })),
      cols: models.map((m) => ({ key: m, label: X.modelLabel(m) })),
      cell: (r, c) => ({
        v: D.analysis.models[c.key].success_by_class[cond][r.key],
        title: `${X.modelLabel(c.key)} · ${X.classLabel(r.key)} · ${X.condLabel(cond)} — click for episodes`,
        onClick: () => X.go("episodes", { model: c.key, cond, class: r.key, battery: "core" }),
      }),
    });
  }

  function perClassForest(models, pick, domain, ref) {
    const rows = [];
    D.meta.classes.forEach((cls) => {
      rows.push({ label: X.classLabel(cls), mean: null });
      models.forEach((m) => {
        const st = pick(m, cls);
        if (!st) return;
        const sig = D.analysis.bh.survivors.includes(st.label);
        rows.push({ label: X.modelLabel(m), mean: st.mean, lo: st.ci95[0], hi: st.ci95[1], color: X.modelColor(m),
                    hollow: !sig, title: `n=${st.n} · p ${fmt.p(st.p_signflip)} · d_z ${fmt.dz(st.dz)} · ${sig ? "survives" : "does not survive"} BH` });
      });
    });
    return C.forest({ rows, domain, width: 560, ref });
  }

  function renderClasses(root, route) {
    const models = X.models();
    const cond = DRIFT_CONDS.includes(route.params.cond) ? route.params.cond : "B_strict";
    const lever = LEVERS.includes(cond) ? cond : "C";
    const leverStat = (m, cls) => {
      const st = D.analysis.models[m].levers[lever].vs_B[cls];
      return st && { ...st, label: `${m}:${lever}-B:${cls}` };
    };
    const dropStat = (m, cls) => {
      const st = D.analysis.models[m].drop[cls];
      return st && { ...st, label: `${m}:drop:${cls}` };
    };
    X.mount(root,
      h("h2", null, "Drift classes"),
      h("p", { className: "lede" }, "Every drifted schema differs from v1 by exactly one change of one of five classes, so each failure is attributable to its class."),
      classCards(),
      h("h3", null, "Success by class"), condPicker("classes", cond),
      h("div", { className: "card" }, classHeat(models, cond),
        h("div", { className: "cap" }, X.condDesc(cond), " Source: ", h("code", null, "success_by_class"), ".")),
      h("div", { className: "grid2" },
        h("div", { className: "card" }, h("h3", null, "Drop per class (baseline − silent drift)"),
          perClassForest(models, dropStat, [-0.25, 1.05], 0),
          h("div", { className: "cap" }, "Paired difference with bootstrap 95% CI. Hollow dots do not survive Benjamini–Hochberg.")),
        h("div", { className: "card" }, h("h3", null, `Gain from ${X.condLabel(lever)} over silent drift`),
          perClassForest(models, leverStat, [-0.4, 1.05], 0),
          h("div", { className: "cap" }, "Interaction p (does the gain depend on class?): ",
            models.map((m) => `${X.modelLabel(m)} ${fmt.p(D.analysis.models[m].interaction[lever])}`).join(" · "),
            LEVERS.includes(cond) ? "" : ". Pick C, D or E above to switch the lever."))));
  }

  /* ---------- ledger ---------- */
  function ledgerShares(model, cond, cls) {
    const block = D.analysis.models[model].ledger[cond];
    if (block) return { source: "analysis", n: block[cls].n, share: (o) => block[cls][LEDGER_KEY[o]], silent: block[cls].silent_share_of_failures };
    const eps = X.E.filter((e) => e.model === model && e.cond === cond && e.class === cls && e.battery === "core");
    const share = (o) => (eps.length ? eps.filter((e) => e.drift_outcome === o).length / eps.length : 0);
    const fails = eps.filter((e) => !e.success);
    const silent = fails.length ? fails.filter((e) => e.drift_outcome === "ACCEPTED_WRONG").length / fails.length : null;
    return { source: "episodes", n: eps.length, share, silent };
  }

  function renderLedger(root, route) {
    const models = X.models();
    const cond = DRIFT_CONDS.includes(route.params.cond) ? route.params.cond : "B_strict";
    const cards = models.map((m) => {
      const rows = D.meta.classes.map((cls) => {
        const L = ledgerShares(m, cond, cls);
        return { label: X.classLabel(cls), segs: OUTCOMES.map((o) => ({
          key: String(o), v: L.share(o), color: X.OUTCOME_COLOR[o],
          title: `${X.outcomeLabel(o)}: ${fmt.pct(L.share(o))} of ${L.n} — click for episodes`,
          onClick: () => X.go("episodes", { model: m, cond, class: cls, outcome: String(o), battery: "core" }) })) };
      });
      return h("div", { className: "card" }, h("h3", { style: { marginTop: 0, color: X.modelColor(m) } }, X.modelLabel(m)), C.stacked({ rows }));
    });
    const silent = C.heatTable({
      corner: "class \\ model",
      rows: D.meta.classes.map((c) => ({ key: c, label: X.classLabel(c) })),
      cols: models.map((m) => ({ key: m, label: X.modelLabel(m) })),
      cell: (r, c) => { const v = ledgerShares(c.key, cond, r.key).silent; return { v, title: "share of failures that executed without any error" }; },
    });
    const fromEpisodes = models.some((m) => !D.analysis.models[m].ledger[cond]);
    X.mount(root,
      h("h2", null, "Outcome ledger"),
      h("p", { className: "lede" }, "Every drifted call lands in one of three cells: the executor surfaced an error, accepted it with the intended semantics, or accepted it while doing something else. The last cell is the silent failure no retry loop can see."),
      condPicker("ledger", cond),
      C.legend(OUTCOMES.map((o) => ({ label: X.outcomeLabel(o), color: X.OUTCOME_COLOR[o] }))),
      h("div", { className: "grid2" }, cards),
      h("h3", null, "Silent share of failures"), h("div", { className: "card" }, silent),
      h("div", { className: "cap" }, fromEpisodes
        ? "This condition has no ledger block in analysis.json; shares are computed here from the core episodes' drift_outcome."
        : "Source: analysis.json → ledger."));
  }

  window.SDXViews.classes = { title: "Drift classes", render: renderClasses };
  window.SDXViews.ledger = { title: "Ledger", render: renderLedger };
})();
