/* Reusable chart primitives (hand-drawn SVG and heat tables). */
window.SDXCharts = (function () {
  "use strict";
  const { h, s, fmt, tip, seqColor, divColor, inkOn, PALETTE } = window.SDX;

  /* Natural size, shrinking to fit narrow containers but never upscaling text. */
  const svgAttrs = (width, height) => ({ width, height, viewBox: `0 0 ${width} ${height}`,
                                         style: "max-width:100%;height:auto;display:block" });

  /* Heat table. cell(row, col) -> {v, n, label, title, onClick} or null. */
  function heatTable({ rows, cols, cell, scale = "seq", corner = "" }) {
    const color = typeof scale === "function" ? scale : scale === "div" ? divColor : seqColor;
    return h("table", null,
      h("thead", null, h("tr", null, h("th", null, corner), cols.map((c) => h("th", { style: { textAlign: "center" } }, c.label)))),
      h("tbody", null, rows.map((r) => h("tr", null,
        h("td", { className: "rowhead" }, r.swatch ? h("span", { className: "sw", style: { background: r.swatch, display: "inline-block", width: "9px", height: "9px", borderRadius: "50%", marginRight: "6px" } }) : null, r.label),
        cols.map((c) => {
          const x = cell(r, c);
          if (!x || x.v == null) return h("td", { className: "mut", style: { textAlign: "center" } }, "—");
          const td = h("td", { className: "heat", style: { background: color(x.v), color: inkOn(x.v) }, onclick: x.onClick },
            x.label != null ? x.label : fmt.rate(x.v), x.n != null ? h("small", null, `n=${x.n}`) : null);
          return x.title ? tip(td, x.title) : td;
        }))))
    );
  }

  /* Horizontal strip: one row per category, one dot per series on [0, 1]. */
  function dotStrip({ rows, series, value, width = 720, rowH = 34, onClick }) {
    const left = 190, right = 24, top = 22, w = width - left - right;
    const height = top + rows.length * rowH + 10;
    const x = (v) => left + v * w;
    const ticks = [0, 0.25, 0.5, 0.75, 1];
    const svg = s("svg", svgAttrs(width, height),
      ticks.map((t) => [s("line", { x1: x(t), x2: x(t), y1: top - 6, y2: height - 6, className: "axis" }),
                        s("text", { x: x(t), y: 12, className: "tick", "text-anchor": "middle" }, fmt.rate(t))]),
      rows.map((r, i) => {
        const y = top + i * rowH + rowH / 2;
        return [s("text", { x: left - 12, y: y + 4, className: "lbl", "text-anchor": "end" }, r.label),
                s("line", { x1: left, x2: left + w, y1: y, y2: y, stroke: PALETTE.rule, "stroke-dasharray": "2 3" }),
                series.map((se) => {
                  const v = value(r, se);
                  if (v == null) return null;
                  const dot = s("circle", { cx: x(v), cy: y, r: 7, fill: se.color, "fill-opacity": 0.85,
                    stroke: "#fff", "stroke-width": 1.5, className: "seg", onclick: onClick ? () => onClick(r, se) : null });
                  return tip(dot, `${se.label} · ${r.label}: ${fmt.rate(v)}`);
                })];
      }));
    return svg;
  }

  /* Forest plot: rows [{label, mean, lo, hi, color, strong, title}] */
  function forest({ rows, domain = [-0.2, 1.1], width = 560, rowH = 24, ref = 0, refLabel }) {
    const left = 200, right = 70, top = 22, w = width - left - right;
    const height = top + rows.length * rowH + 8;
    const x = (v) => left + ((Math.max(domain[0], Math.min(domain[1], v)) - domain[0]) / (domain[1] - domain[0])) * w;
    const ticks = [];
    for (let t = Math.ceil(domain[0] * 4) / 4; t <= domain[1] + 1e-9; t += 0.25) ticks.push(+t.toFixed(2));
    return s("svg", svgAttrs(width, height),
      ticks.map((t) => [s("line", { x1: x(t), x2: x(t), y1: top - 4, y2: height - 4, className: "axis" }),
                        s("text", { x: x(t), y: 12, className: "tick", "text-anchor": "middle" }, fmt.rate(t))]),
      s("line", { x1: x(ref), x2: x(ref), y1: top - 4, y2: height - 4, stroke: PALETTE.ink, "stroke-width": 1 }),
      refLabel ? s("text", { x: x(ref) + 4, y: height - 6, className: "tick" }, refLabel) : null,
      rows.map((r, i) => {
        const y = top + i * rowH + rowH / 2;
        if (r.mean == null) return s("text", { x: left - 10, y: y + 4, className: "lbl mut", "text-anchor": "end" }, r.label);
        const g = s("g", null,
          s("text", { x: left - 10, y: y + 4, className: "lbl", "text-anchor": "end", "font-weight": r.strong ? 700 : 400 }, r.label),
          r.lo != null ? s("line", { x1: x(r.lo), x2: x(r.hi), y1: y, y2: y, stroke: r.color, "stroke-width": 2.5, "stroke-linecap": "round" }) : null,
          s("circle", { cx: x(r.mean), cy: y, r: 5, fill: r.hollow ? "#fff" : r.color, stroke: r.color, "stroke-width": 2 }),
          s("text", { x: width - right + 8, y: y + 4, className: "tick" }, fmt.rate(r.mean)));
        return r.title ? tip(g, r.title) : g;
      }));
  }

  /* Stacked horizontal 100% bars: rows [{label, segs:[{key, v, color, title, onClick}]}] */
  function stacked({ rows, width = 560, rowH = 26, left = 150 }) {
    const right = 10, top = 4, w = width - left - right;
    const height = top + rows.length * rowH + 4;
    return s("svg", svgAttrs(width, height),
      rows.map((r, i) => {
        const y = top + i * rowH;
        let acc = 0;
        return [s("text", { x: left - 10, y: y + rowH / 2 + 4, className: "lbl", "text-anchor": "end" }, r.label),
          r.segs.map((sg) => {
            const x0 = left + acc * w, sw = sg.v * w;
            acc += sg.v;
            if (sg.v <= 0) return null;
            const rect = s("rect", { x: x0, y: y + 3, width: Math.max(0, sw - 1), height: rowH - 6, fill: sg.color,
                                     className: "seg", onclick: sg.onClick });
            const label = sw > 34 ? s("text", { x: x0 + sw / 2, y: y + rowH / 2 + 4, "text-anchor": "middle",
                                                fill: "#fff", "font-size": 11, "pointer-events": "none" }, fmt.pct(sg.v)) : null;
            return [sg.title ? tip(rect, sg.title) : rect, label];
          })];
      }));
  }

  const legend = (items) => h("div", { className: "legend" },
    items.map((it) => h("span", null, h("i", { style: { background: it.color, borderRadius: it.round ? "50%" : "2px" } }), it.label)));

  /* Sortable table. columns: [{key, label, num, get(row), render(row)}] */
  function sortable({ columns, rows, onRowClick, sortKey, sortDir = -1, rowClass, compact = false }) {
    let key = sortKey, dir = sortDir;
    const wrap = h("div");
    function draw() {
      const col = columns.find((c) => c.key === key);
      const sorted = col ? [...rows].sort((a, b) => {
        const va = col.get ? col.get(a) : a[col.key], vb = col.get ? col.get(b) : b[col.key];
        if (va == null) return 1; if (vb == null) return -1;
        return (va < vb ? -1 : va > vb ? 1 : 0) * dir;
      }) : rows;
      const head = h("tr", null, columns.map((c) => h("th", { className: "sortable", onclick: () => {
        dir = key === c.key ? -dir : (c.num ? -1 : 1); key = c.key; draw();
      } }, c.label, key === c.key ? (dir > 0 ? " ▲" : " ▼") : "")));
      const body = sorted.map((r) => h("tr", { className: [onRowClick ? "click" : "", rowClass ? rowClass(r) : ""].join(" "),
        onclick: onRowClick ? () => onRowClick(r) : null },
        columns.map((c) => h("td", { className: c.num ? "n" : "" }, c.render ? c.render(r) : (c.get ? c.get(r) : r[c.key])))));
      wrap.replaceChildren(h("table", { className: compact ? "compact" : null }, h("thead", null, head), h("tbody", null, body)));
    }
    draw();
    return wrap;
  }

  return { heatTable, dotStrip, forest, stacked, legend, sortable };
})();
