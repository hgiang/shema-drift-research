/* Audit: the hand-verified accepted-with-wrong-semantics sample. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.audit = (function () {
  "use strict";
  const X = window.SDX;
  const { D, h, fmt } = X;

  function card(a) {
    const idx = X.findEpisode(a.model, a.task, a.class, a.cond);
    return h("div", { className: "card" },
      h("div", { style: { display: "flex", justifyContent: "space-between", gap: "10px", alignItems: "baseline" } },
        h("div", null, h("b", { style: { color: X.modelColor(a.model) } }, X.modelLabel(a.model)), ` · ${a.task} · ${X.classLabel(a.class)} · ${X.condLabel(a.cond)}`),
        h("span", { className: "tag " + (a.audit_verdict === "CONFIRMED" ? "ACCEPTED_WRONG" : "null") }, a.audit_verdict)),
      h("div", { className: "quote" }, a.phrasing),
      h("table", null,
        h("thead", null, h("tr", null, ["field", "executed", "intended"].map((t) => h("th", null, t)))),
        h("tbody", null, Object.entries(a.divergent_fields).map(([k, [got, want]]) => h("tr", null,
          h("td", { className: "n" }, k), h("td", { className: "n bad" }, fmt.value(got)), h("td", { className: "n ok" }, fmt.value(want)))))),
      h("p", { className: "cap" }, a.audit_note),
      idx != null ? h("button", { onclick: () => X.go("episodes", { i: idx, model: a.model, task: a.task }) }, "Open episode") : null);
  }

  function render(root) {
    const meta = D.audit.meta;
    const sample = D.audit.sample.filter((a) => X.isVisible(a.model));
    X.mount(root,
      h("h2", null, "Audit of silent failures"),
      h("p", { className: "lede" }, `${meta.confirmed} of ${meta.n} accepted-wrong episodes confirmed by hand (${meta.audited_by}). ${meta.summary}.`),
      h("div", { className: "cap" }, `${sample.length} shown for the visible models.`),
      h("div", { className: "grid2" }, sample.map(card)));
  }

  return { title: "Audit", render };
})();
