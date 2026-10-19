/* Episode fields shared by the pivot and the episode browser: how to read,
   enumerate and label each dimension, and how to filter by URL params. */
window.SDXFields = (function () {
  "use strict";
  const X = window.SDX;
  const { D, E } = X;
  const uniq = (get, numeric) => [...new Set(E.map(get))]
    .sort((a, b) => (numeric ? Number(a) - Number(b) : String(a).localeCompare(String(b))));
  const id = (v) => v;

  const FIELDS = {
    model: { label: "Model", get: (e) => e.model, values: D.meta.models, fmt: X.modelLabel },
    cond: { label: "Condition", get: (e) => e.cond, values: D.meta.conds, fmt: X.condLabel },
    class: { label: "Drift class", get: (e) => e.class, all: X.classesOf, values: D.meta.classes, fmt: X.classLabel },
    battery: { label: "Run set", get: (e) => e.battery, values: ["core", "noise", "phrasing"],
               fmt: (v) => ({ core: "main run", noise: "repeats (noise check)", phrasing: "reworded request" })[v] || v },
    domain: { label: "Domain", get: (e) => e.domain, values: uniq((e) => e.domain), fmt: id },
    n_steps: { label: "Steps", get: (e) => String(e.n_steps), values: ["1", "2"],
               fmt: (v) => (v === "1" ? "single-step" : "two-step") },
    phrasing: { label: "Phrasing", get: (e) => String(e.phrasing), values: ["0", "1"], fmt: (v) => `phrasing ${v}` },
    outcome: { label: "Drift outcome", get: (e) => String(e.drift_outcome),
               values: ["ERROR_SURFACED", "ACCEPTED_CORRECT", "ACCEPTED_WRONG", "null"], fmt: X.outcomeLabel },
    follow: { label: "Drifted call", get: (e) => e.follow,
              values: ["V2_CORRECT", "V2_PARTIAL", "V1_FORM", "V1_SAFE", "OTHER_ERROR", "OTHER_WRONG", "NO_DRIFT_CALL", "n/a"],
              fmt: X.followLabel },
    same_as_B: { label: "vs silent drift", get: (e) => e.same_as_B, values: ["1", "0", "n/a"], fmt: X.sameLabel },
    success: { label: "Success", get: (e) => (e.success ? "1" : "0"), values: ["1", "0"],
               fmt: (v) => (v === "1" ? "success" : "failure") },
    drift_tool: { label: "Drifted tool", get: (e) => X.tasksById[e.task].drift_tool,
                  values: uniq((e) => X.tasksById[e.task].drift_tool), fmt: id },
    task: { label: "Task", get: (e) => e.task, values: uniq((e) => e.task), fmt: id },
    calls_made: { label: "Calls made", get: (e) => String(e.calls_made), values: uniq((e) => String(e.calls_made), true), fmt: id },
  };

  /* A field may give an episode several values (class for baseline episodes). */
  const valuesOf = (f, e) => (f.all ? f.all(e) : [f.get(e)]);
  const split = (v) => (v == null || v === "" ? null : new Set(String(v).split(",")));

  /* Indices of episodes matching params (comma lists = OR within a field).
     Without an explicit model filter, only globally visible models are kept. */
  function filterIndices(params) {
    const active = Object.entries(params)
      .filter(([k]) => FIELDS[k])
      .map(([k, v]) => [FIELDS[k], split(v)])
      .filter(([, set]) => set);
    const modelFree = !split(params.model);
    const q = (params.q || "").trim().toLowerCase();
    const out = [];
    E.forEach((e, i) => {
      if (modelFree && !X.isVisible(e.model)) return;
      if (!active.every(([f, set]) => valuesOf(f, e).some((v) => set.has(v)))) return;
      if (q && !matchesText(e, q)) return;
      out.push(i);
    });
    return out;
  }

  function matchesText(e, q) {
    const task = X.tasksById[e.task];
    return e.task.includes(q) || task.drift_tool.includes(q) || (e.error_seen || "").toLowerCase().includes(q) ||
      task.phrasings[e.phrasing].toLowerCase().includes(q);
  }

  /* Toggle one value inside a comma-list param; returns a new params object. */
  function toggleParam(params, key, value) {
    const set = split(params[key]) || new Set();
    if (set.has(value)) set.delete(value); else set.add(value);
    const vals = FIELDS[key] ? FIELDS[key].values.filter((v) => set.has(v)) : [...set];
    return { ...params, [key]: vals.join(",") };
  }

  function chipFilter(key, params, onChange) {
    const f = FIELDS[key], set = split(params[key]);
    return h_label(f.label, f.values.map((v) => X.h("button", {
      className: "chip" + (set && set.has(v) ? " on" : ""), onclick: () => onChange(toggleParam(params, key, v)),
    }, f.fmt(v))));
  }
  const h_label = (text, kids) => X.h("label", null, text, X.h("div", { className: "chipgroup" }, kids));

  return { FIELDS, valuesOf, filterIndices, toggleParam, chipFilter, split };
})();
