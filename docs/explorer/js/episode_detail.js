/* Episode detail: what the model saw, what changed, what happened, and how
   each accepted call compares with ground truth. */
window.SDXDetail = (function () {
  "use strict";
  const X = window.SDX;
  const { D, h, fmt } = X;
  const DIFF_MARK = "\n\nNOTE: the API behind tool";

  function header(e, i, nav) {
    return h("div", null,
      h("div", { style: { display: "flex", justifyContent: "space-between", alignItems: "center", gap: "8px" } },
        h("div", { className: "eyebrow" }, `episode #${i}`),
        h("div", { className: "pager", style: { margin: 0 } },
          h("button", { onclick: nav.onPrev, title: "previous (k)" }, "‹ prev"),
          h("button", { onclick: nav.onNext, title: "next (j)" }, "next ›"))),
      h("h2", { style: { marginTop: "2px" } }, `${e.task} · `, h("span", { style: { color: X.modelColor(e.model) } }, X.modelLabel(e.model))),
      h("div", { className: "chipgroup", style: { margin: "6px 0 10px" } },
        h("span", { className: "tag", style: { color: e.success ? X.PALETTE.good : X.PALETTE.hot } }, e.success ? "task success" : "task failure"),
        h("span", { className: "tag " + String(e.drift_outcome) }, X.outcomeLabel(e.drift_outcome)),
        h("span", { className: "tag mut" }, X.condLabel(e.cond)),
        e.cond === "A" ? null : h("span", { className: "tag mut" }, X.classLabel(e.class)),
        e.follow === "n/a" ? null : h("span", { className: "tag fl-" + e.follow, title: X.followDesc(e.follow) }, `drifted call: ${X.followLabel(e.follow)}`)));
  }

  function facts(e, task) {
    const baseline = e.cond === "A";
    const kv = [["condition", X.condDesc(e.cond)],
      ["drift class", baseline ? `none applied (baseline; logged under ${X.classLabel(e.class)})` : `${X.classLabel(e.class)}: ${X.classDesc(e.class)}`],
      [baseline ? "tool that drifts elsewhere" : "drifted tool", `${task.drift_tool} (step ${task.drift_step_index + 1} of ${e.n_steps})`], ["domain", e.domain],
      ["battery", `${e.battery} · phrasing ${e.phrasing} · rep ${e.rep}`], ["calls made", String(e.calls_made)]];
    return h("dl", { className: "kv" }, kv.map(([k, v]) => [h("dt", null, k), h("dd", null, v)]));
  }

  function systemPre(text) {
    const cut = text.indexOf(DIFF_MARK);
    if (cut < 0) return h("pre", null, text);
    return h("pre", null, text.slice(0, cut), h("span", { className: "hl" }, text.slice(cut)));
  }

  function prompt(e, task) {
    const view = D.views[`${e.task}|${e.class}|${e.cond}`];
    const decls = view.decls.map((d) => D.prompts.decls[d]);
    const drifted = e.cond !== "A";
    return h("div", null,
      h("h3", null, "User request"), h("div", { className: "quote" }, task.phrasings[e.phrasing]),
      h("h3", null, "What the model saw"),
      h("details", { open: e.cond === "C" }, h("summary", null, e.cond === "C" ? "System prompt (diff highlighted)" : "System prompt"), systemPre(D.prompts.system[view.system])),
      decls.map((d) => h("details", null,
        h("summary", null, `Tool declaration: ${d.name}`,
          d.name === task.drift_tool && drifted ? (e.cond === "D" ? " (v2 shown)" : " (v1 shown, executor enforces v2)") : ""),
        X.jsonPre(d))),
      h("div", { className: "cap" }, `Executor profile: ${view.profile}${view.retry ? " · raw error fed back, one retry per step" : ""}.`));
  }

  function change(e, task) {
    if (e.cond === "A") return null;
    const diff = D.testbed.diffs[`${task.drift_tool}::${e.class}`];
    return h("div", null, h("h3", null, `Schema change to ${task.drift_tool}`), X.jsonPre(diff.changes));
  }

  /* ---------- Phase 1 step 1: drifted call vs silent drift ---------- */
  function driftKeys(e, task) {
    const ch = D.testbed.diffs[`${task.drift_tool}::${e.class}`].changes[0];
    return e.class === "rename" ? [ch.param, ch.new] : [ch.param];
  }

  function driftCallBox(ep, task, keys, title, onOpen) {
    const call = ep.executed.find((st) => st.tool === task.drift_tool);
    const body = ep.error_seen && !call
      ? [h("div", { className: "cap", style: { marginTop: 0 } }, "rejected; executor said:"), h("pre", { style: { color: X.PALETTE.hot } }, ep.error_seen)]
      : call ? [X.jsonPre(call.args, keys)]
        : [h("p", { className: "empty" }, "no call to the drifted tool")];
    return h("div", { className: "card", style: { padding: "10px 12px", margin: 0 } },
      h("div", { style: { display: "flex", justifyContent: "space-between", gap: "6px", alignItems: "center", marginBottom: "6px" } },
        h("b", { style: { fontFamily: "var(--sans)", fontSize: "13px" } }, title),
        h("span", { className: "tag " + String(ep.drift_outcome) }, X.outcomeLabel(ep.drift_outcome))),
      body,
      onOpen ? h("button", { onclick: onOpen, style: { marginTop: "6px" } }, "open this episode") : null);
  }

  function versusSilent(e, task, params) {
    if (e.cond === "A" || e.cond === "B_strict") return null;
    const j = X.findEpisode(e.model, e.task, e.class, "B_strict", e.phrasing, e.rep);
    if (j == null) return null;
    const b = X.E[j], keys = driftKeys(e, task);
    const same = e.same_as_B === "1";
    return h("div", null,
      h("h3", null, "Drifted call vs silent drift"),
      h("div", { className: "cap", style: { marginTop: 0 } },
        h("span", { className: "tag " + (same ? "ACCEPTED_WRONG" : "ACCEPTED_CORRECT") }, same ? "identical call" : "call changed"), " ",
        same ? `With ${X.condLabel(e.cond)} the model made exactly the call it made with no warning at all.`
             : `${X.condLabel(e.cond)} changed what the model sent on this pair.`,
        " ", X.followLabel(e.follow), ": ", X.followDesc(e.follow)),
      h("div", { className: "split even" },
        driftCallBox(b, task, keys, X.condShort("B_strict"), () => X.go("episodes", { ...params, i: j })),
        driftCallBox(e, task, keys, X.condShort(e.cond), null)),
      h("div", { className: "cap" }, `Highlighted: the drifted parameter (${keys.join(" → ")}). Rejected calls keep only the executor message.`));
  }

  function response(e) {
    if (!e.error_seen) return null;
    return h("div", null, h("h3", null, "Executor error"),
      h("pre", { style: { color: X.PALETTE.hot } }, e.error_seen),
      h("div", { className: "cap" }, "Rejected calls are not logged with their arguments; only the executor's message is kept."));
  }

  function fieldTable(stepRec) {
    const args = stepRec.args || {};
    return h("table", { className: "fields" },
      h("thead", null, h("tr", null, ["parameter", "sent", "effective", "expected", ""].map((t) => h("th", null, t)))),
      h("tbody", null, stepRec.check.fields.map((f) => h("tr", null,
        h("td", { className: "n" }, f.param),
        h("td", { className: "n" }, f.param in args ? fmt.value(args[f.param]) : h("span", { className: "mut" }, "—")),
        h("td", { className: "n" }, fmt.value(f.effective)),
        h("td", { className: "n" }, fmt.value(f.expected)),
        h("td", { className: "st-" + f.status }, f.status)))));
  }

  function calls(e) {
    if (!e.executed.length) return h("div", null, h("h3", null, "Accepted calls"), h("p", { className: "empty" }, "No call was accepted by the executor."));
    return h("div", null, h("h3", null, "Accepted calls vs ground truth"),
      e.executed.map((st, k) => h("div", { className: "card", style: { padding: "10px 12px" } },
        h("div", { style: { display: "flex", gap: "8px", alignItems: "center", marginBottom: "6px", fontFamily: "var(--sans)", fontSize: "13px" } },
          h("b", null, `${k + 1}. ${st.tool}`), h("span", { className: "tag " + String(st.outcome) }, X.outcomeLabel(st.outcome))),
        st.check ? fieldTable(st) : [h("div", { className: "cap" }, "Not scored: not the expected tool at this step."), X.jsonPre(st.args)])),
      h("div", { className: "cap" }, "effective = what the executor actually ran after defaults, dropping unknown fields (lenient) and coercion. ∅ = absent. Compared with harness.semantically_equal."));
  }

  function groundTruth(e, task) {
    const gt = e.cond === "A" ? task.gt_v1 : task.gt_v2[e.class];
    return h("details", null, h("summary", null, `Ground truth for this condition (${gt.length} step${gt.length > 1 ? "s" : ""})`), X.jsonPre(gt));
  }

  function siblings(e, task, params) {
    const models = D.meta.models;
    return h("div", null, h("h3", null, "Same task-drift pair across models and conditions"),
      h("table", { className: "mini" },
        h("thead", null, h("tr", null, h("th", null, ""), D.meta.conds.map((c) => h("th", null, X.condShort(c))))),
        h("tbody", null, models.map((m) => h("tr", null, h("td", { className: "rowhead", style: { textAlign: "left" } }, X.modelLabel(m)),
          D.meta.conds.map((c) => {
            const j = X.findEpisode(m, e.task, e.class, c, e.phrasing, e.rep) ??
              (c === "A" ? X.findEpisode(m, e.task, task.assigned[0], c, e.phrasing, e.rep) : undefined);
            if (j == null) return h("td", { className: "mut" }, "·");
            const s = X.E[j];
            const td = h("td", { className: "cell" + (s === e ? " cur" : ""), style: { background: s.success ? "#dcefe6" : "#f8dceb" },
              onclick: () => X.go("episodes", { ...params, i: j }) }, s.success ? "✓" : "✗");
            return X.tip(td, `${X.modelLabel(m)} · ${X.condLabel(c)} · ${X.outcomeLabel(s.drift_outcome)}`);
          }))))),
      h("div", { className: "cap" }, "The baseline runs once per task (v1 everywhere), so it is shared by both of a task's drift classes. · = not run (Pro and luna ran the primary 120 pairs only)."));
  }

  function render(i, opts) {
    const e = X.E[i], task = X.tasksById[e.task];
    return h("div", null, header(e, i, opts), facts(e, task), prompt(e, task), change(e, task),
      versusSilent(e, task, opts.params), response(e), calls(e), groundTruth(e, task), siblings(e, task, opts.params));
  }

  return { render };
})();
