/* Dataset: browse the frozen SchemaDrift-120 testbed (tools and tasks), with
   per-item success pulled from the core episodes. */
window.SDXViews = window.SDXViews || {};
window.SDXViews.dataset = (function () {
  "use strict";
  const X = window.SDX, C = window.SDXCharts;
  const { D, h, fmt } = X;
  const T = D.testbed;
  const coreEps = (pred) => X.E.filter((e) => e.battery === "core" && X.isVisible(e.model) && pred(e));
  const condRate = (eps, cond) => X.rate(eps.filter((e) => e.cond === cond));

  function subnav(sub) {
    return h("div", { className: "chipgroup", style: { margin: "6px 0 14px" } },
      [["tools", `Tools (${Object.keys(T.tools).length})`], ["tasks", `Tasks (${T.tasks.length})`]].map(([k, t]) =>
        h("button", { className: "chip" + (sub === k ? " on" : ""), onclick: () => X.go("dataset", {}, [k]) }, t)));
  }

  function paramTable(params, highlight) {
    return h("table", null,
      h("thead", null, h("tr", null, ["parameter", "type", "required", "default", "enum", "description"].map((t) => h("th", null, t)))),
      h("tbody", null, Object.entries(params).map(([name, p]) => h("tr", { style: highlight && highlight.has(name) ? { background: "#fdeaf3" } : null },
        h("td", { className: "n" }, name), h("td", null, p.type), h("td", null, p.required ? "yes" : ""),
        h("td", { className: "n" }, p.required ? "" : fmt.value(p.default)),
        h("td", { className: "n" }, p.enum ? p.enum.join(", ") : ""), h("td", null, p.desc)))));
  }

  /* models x conds success grid for a set of core episodes; click opens the episodes. */
  function successGrid(eps, drill) {
    const models = X.models();
    return C.heatTable({
      corner: "model \\ condition",
      rows: models.map((m) => ({ key: m, label: X.modelLabel(m), swatch: X.modelColor(m) })),
      cols: D.meta.conds.map((c) => ({ key: c, label: X.condLabel(c) })),
      cell: (r, c) => {
        const sel = eps.filter((e) => e.model === r.key && e.cond === c.key);
        return sel.length ? { v: X.rate(sel), n: sel.length, onClick: () => X.go("episodes", { ...drill, model: r.key, cond: c.key, battery: "core" }) } : null;
      },
    });
  }

  function toolsList(sel) {
    const rows = Object.entries(T.tools).map(([name, t]) => {
      const eps = coreEps((e) => X.tasksById[e.task].drift_tool === name);
      return { name, domain: t.domain, params: Object.keys(t.params).length,
               tasks: T.tasks.filter((k) => k.drift_tool === name).length,
               a: condRate(eps, "A"), b: condRate(eps, "B_strict"), c: condRate(eps, "C") };
    });
    return C.sortable({ rows, compact: true, sortKey: "domain", sortDir: 1, onRowClick: (r) => X.go("dataset", {}, ["tools", r.name]),
      rowClass: (r) => (r.name === sel ? "sel" : ""),
      columns: [{ key: "name", label: "tool" }, { key: "domain", label: "domain" }, { key: "params", label: "params", num: true },
        { key: "tasks", label: "tasks", num: true },
        { key: "a", label: "baseline", num: true, render: (r) => fmt.rate(r.a) },
        { key: "b", label: "silent drift", num: true, render: (r) => fmt.rate(r.b) },
        { key: "c", label: "+ diff", num: true, render: (r) => fmt.rate(r.c) }] });
  }

  function toolDetail(name) {
    const t = T.tools[name];
    if (!t) return h("p", { className: "empty" }, "Select a tool.");
    const eps = coreEps((e) => X.tasksById[e.task].drift_tool === name);
    return h("div", null,
      h("div", { className: "eyebrow" }, t.domain), h("h2", { style: { marginTop: 0 } }, name), h("p", { className: "lede" }, t.description),
      h("h3", null, "v1 parameters"), paramTable(t.params),
      h("h3", null, "Drift variants"),
      D.meta.classes.map((cls) => {
        const key = `${name}::${cls}`;
        if (!T.diffs[key]) return null;
        const changed = new Set(T.diffs[key].changes.map((c) => c.param).concat(T.diffs[key].changes.map((c) => c.new).filter((v) => typeof v === "string")));
        const clsEps = eps.filter((e) => X.classesOf(e).includes(cls));
        return h("details", null, h("summary", null, `${X.classLabel(cls)} (${clsEps.length} core episodes)`),
          X.jsonPre(T.diffs[key].changes), h("div", { className: "cap" }, "v2 parameters (changed rows highlighted):"),
          paramTable(T.v2_schemas[key], changed),
          clsEps.length ? successGrid(clsEps, { drift_tool: name, class: cls }) : null);
      }),
      h("h3", null, "Success on tasks that drift this tool"), successGrid(eps, { drift_tool: name }),
      h("h3", null, "Mock result payload"), X.jsonPre(t.result));
  }

  function tasksList(sel) {
    const rows = T.tasks.map((t) => {
      const eps = coreEps((e) => e.task === t.id);
      return { id: t.id, domain: t.domain, steps: t.steps.length, tool: t.drift_tool, classes: t.assigned.map(X.classLabel).join(", "),
               a: condRate(eps, "A"), b: condRate(eps, "B_strict"), c: condRate(eps, "C"), d: condRate(eps, "D") };
    });
    return C.sortable({ rows, compact: true, sortKey: "b", sortDir: 1, onRowClick: (r) => X.go("dataset", {}, ["tasks", r.id]),
      rowClass: (r) => (r.id === sel ? "sel" : ""),
      columns: [{ key: "id", label: "task" }, { key: "domain", label: "domain" }, { key: "steps", label: "steps", num: true },
        { key: "tool", label: "drifted tool" }, { key: "classes", label: "drift classes" },
        { key: "a", label: "baseline", num: true, render: (r) => fmt.rate(r.a) },
        { key: "b", label: "silent", num: true, render: (r) => fmt.rate(r.b) },
        { key: "c", label: "+diff", num: true, render: (r) => fmt.rate(r.c) },
        { key: "d", label: "+v2", num: true, render: (r) => fmt.rate(r.d) }] });
  }

  function changedKeys(a, b) {
    return [...new Set([...Object.keys(a), ...Object.keys(b)])].filter((k) => JSON.stringify(a[k]) !== JSON.stringify(b[k]));
  }

  function taskDetail(id) {
    const t = X.tasksById[id];
    if (!t) return h("p", { className: "empty" }, "Select a task.");
    const di = t.drift_step_index;
    return h("div", null,
      h("div", { className: "eyebrow" }, `${t.domain} · ${t.steps.length}-step · drifts ${t.drift_tool} at step ${di + 1}`),
      h("h2", { style: { marginTop: 0 } }, id),
      h("h3", null, "Phrasings"), t.phrasings.map((p, k) => h("div", { className: "quote" }, `${k}. ${p}`)),
      h("h3", null, "Ground truth under v1"), X.jsonPre(t.gt_v1),
      t.assigned.map((cls) => {
        const gt = t.gt_v2[cls];
        const eps = coreEps((e) => e.task === id && X.classesOf(e).includes(cls));
        return h("div", null, h("h3", null, `Under ${X.classLabel(cls)} drift`),
          h("div", { className: "cap" }, "Ground truth after the change (changed keys highlighted):"),
          X.jsonPre(gt, changedKeys(t.gt_v1[di], gt[di])),
          successGrid(eps, { task: id, class: cls }));
      }),
      h("div", { className: "cap" }, "Baseline is shared by both drift classes of a task. Eligible classes for this task: ", t.eligible.map(X.classLabel).join(", "), "."));
  }

  function render(root, route) {
    const sub = route.parts[0] === "tasks" ? "tasks" : "tools";
    const sel = route.parts[1];
    X.mount(root,
      h("h2", null, "Dataset"),
      h("p", { className: "lede" }, `${T.name}, frozen ${T.frozen_at} (sha256 ${D.meta.testbed_sha256.slice(0, 12)}…): 30 tools across ten domains, 120 tasks with two phrasings each, five single-edit drift classes, ${T.per_class_pairs} task-drift pairs per class. Success columns pool the visible models' core episodes.`),
      subnav(sub),
      h("div", { className: "split even" },
        h("div", { className: "card" }, sub === "tools" ? toolsList(sel) : tasksList(sel)),
        h("div", { className: "card detail" }, sub === "tools" ? toolDetail(sel) : taskDetail(sel))));
  }

  return { title: "Dataset", render };
})();
