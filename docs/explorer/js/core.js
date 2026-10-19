/* Core helpers for the SchemaDrift-120 explorer: DOM builders, formatting,
   labels, routing, global model visibility. All text goes through
   textContent (never innerHTML), because the data holds model-emitted strings. */
window.SDX = (function () {
  "use strict";
  const D = window.SD_DATA;
  if (!D || !D.episodes) {
    document.getElementById("view").textContent = "data.js is missing or empty. Run: python3 viz/build_explorer_data.py";
    throw new Error("SD_DATA missing: build docs/explorer/data.js first");
  }
  const SVG_NS = "http://www.w3.org/2000/svg";
  const PALETTE = { slate: "#155e8c", hot: "#b3006b", shelf: "#c0641a", good: "#1c7a55",
                    ink: "#16130d", muted: "#6d665a", faint: "#a49c8c", rule: "#e7e2d5" };
  const OUTCOME_COLOR = { ERROR_SURFACED: PALETTE.slate, ACCEPTED_CORRECT: PALETTE.good,
                          ACCEPTED_WRONG: PALETTE.hot, null: PALETTE.faint };
  const MIN_P = 1 / 20000; // analyze.py runs 20,000 sign-flip permutations
  const STORE_KEY = "sdx.models";

  /* ---------- DOM ---------- */
  function build(ns, tag, attrs, children) {
    const el = ns ? document.createElementNS(ns, tag) : document.createElement(tag);
    Object.entries(attrs || {}).forEach(([k, v]) => {
      if (v == null || v === false) return;
      if (k.startsWith("on") && typeof v === "function") el.addEventListener(k.slice(2), v);
      else if (k === "style" && typeof v === "object") Object.assign(el.style, v);
      else if (k === "text") el.textContent = v;
      else el.setAttribute(k === "className" ? "class" : k, v === true ? "" : v);
    });
    children.flat(Infinity).forEach((c) => {
      if (c == null || c === false) return;
      el.appendChild(c instanceof Node ? c : document.createTextNode(String(c)));
    });
    return el;
  }
  const h = (tag, attrs, ...children) => build(null, tag, attrs, children);
  const s = (tag, attrs, ...children) => build(SVG_NS, tag, attrs, children);
  function mount(target, ...children) {
    target.replaceChildren(...children.flat(Infinity).filter((c) => c != null && c !== false));
  }

  /* ---------- formatting ---------- */
  const fmt = {
    rate: (v) => (v == null || Number.isNaN(v) ? "—" : v.toFixed(3).replace(/^(-?)0\./, "$1.")),
    pct: (v) => (v == null ? "—" : `${Math.round(v * 100)}%`),
    signed: (v) => (v == null ? "—" : (v > 0 ? "+" : "") + fmt.rate(v)),
    ci: (ci) => (ci ? `[${fmt.rate(ci[0])}, ${fmt.rate(ci[1])}]` : "—"),
    p: (p) => (p == null ? "—" : p < MIN_P ? `< ${MIN_P.toExponential(0)}` : p < 0.001 ? p.toExponential(1) : p.toFixed(3)),
    dz: (v) => (v == null ? "—" : v.toFixed(2)),
    int: (v) => (v == null ? "—" : v.toLocaleString("en-US")),
    value: (v) => (v === undefined ? "∅" : JSON.stringify(v)),
  };

  /* ---------- labels ---------- */
  const L = D.labels;
  const modelLabel = (m) => (L.models[m] || {}).label || m;
  const modelColor = (m) => (L.models[m] || {}).color || PALETTE.muted;
  const condLabel = (c) => (L.conds[c] || {}).label || c;
  const condShort = (c) => (L.conds[c] || {}).short || c;
  const condDesc = (c) => (L.conds[c] || {}).desc || "";
  const classLabel = (c) => (L.classes[c] || {}).label || c;
  const classDesc = (c) => (L.classes[c] || {}).desc || "";
  const outcomeLabel = (o) => L.outcomes[String(o)] || String(o);
  const followLabel = (v) => ((L.follow || {})[v] || {}).label || v;
  const followDesc = (v) => ((L.follow || {})[v] || {}).desc || "";
  const sameLabel = (v) => (L.same_as_B || {})[v] || v;

  /* ---------- model visibility (global) ---------- */
  const listeners = [];
  function loadVisible() {
    try {
      const saved = JSON.parse(localStorage.getItem(STORE_KEY) || "null");
      if (Array.isArray(saved)) {
        const valid = saved.filter((m) => D.meta.models.includes(m));
        if (valid.length) return new Set(valid);
      }
    } catch (err) { console.warn("ignoring saved model selection:", err); }
    return new Set(D.meta.models);
  }
  let visible = loadVisible();
  const models = () => D.meta.models.filter((m) => visible.has(m));
  function toggleModel(m) {
    const next = new Set(visible);
    if (next.has(m) && next.size > 1) next.delete(m); else next.add(m);
    visible = next;
    try { localStorage.setItem(STORE_KEY, JSON.stringify([...visible])); }
    catch (err) { console.warn("cannot persist model selection:", err); }
    listeners.forEach((fn) => fn());
  }
  const onModelsChange = (fn) => listeners.push(fn);
  const isVisible = (m) => visible.has(m);

  /* ---------- colour scales ---------- */
  function mix(a, b, t) {
    const pa = a.match(/\w\w/g).map((x) => parseInt(x, 16));
    const pb = b.match(/\w\w/g).map((x) => parseInt(x, 16));
    const c = pa.map((v, i) => Math.round(v + (pb[i] - v) * Math.max(0, Math.min(1, t))));
    return `rgb(${c.join(",")})`;
  }
  const seqColor = (v) => mix("ffffff", PALETTE.slate.slice(1), v * 0.92);
  const hotColor = (v) => mix("ffffff", PALETTE.hot.slice(1), v * 0.9);
  const divColor = (v) => (v >= 0 ? mix("ffffff", PALETTE.good.slice(1), Math.min(1, v) * 0.9)
                                  : mix("ffffff", PALETTE.hot.slice(1), Math.min(1, -v) * 0.9));
  const inkOn = (t) => (Math.abs(t) > 0.55 ? "#fff" : PALETTE.ink);

  /* ---------- routing ---------- */
  function parseHash() {
    const raw = location.hash.replace(/^#/, "");
    const cut = raw.indexOf("?");
    const path = cut < 0 ? raw : raw.slice(0, cut);
    const safeDecode = (x) => { try { return decodeURIComponent(x); } catch { return x; } };
    const parts = (path || "overview").split("/").filter(Boolean).map(safeDecode);
    let params = {};
    try { params = Object.fromEntries(new URLSearchParams(cut < 0 ? "" : raw.slice(cut + 1))); }
    catch (err) { console.warn("ignoring malformed query:", err); }
    return { view: parts[0] || "overview", parts: parts.slice(1), params };
  }
  function href(view, params, parts) {
    const p = Object.entries(params || {}).filter(([, v]) => v != null && v !== "");
    const q = p.length ? "?" + new URLSearchParams(p).toString() : "";
    return "#" + [view, ...(parts || [])].map(encodeURIComponent).join("/") + q;
  }
  const go = (view, params, parts) => { location.hash = href(view, params, parts); };

  /* ---------- tooltip ---------- */
  const tipEl = h("div", { className: "tip" });
  document.addEventListener("DOMContentLoaded", () => document.body.appendChild(tipEl));
  function tip(el, text) {
    el.addEventListener("mousemove", (e) => {
      tipEl.textContent = text;
      tipEl.style.display = "block";
      tipEl.style.left = `${Math.min(e.clientX + 14, window.innerWidth - 330)}px`;
      tipEl.style.top = `${e.clientY + 14}px`;
    });
    el.addEventListener("mouseleave", () => { tipEl.style.display = "none"; });
    return el;
  }
  const hideTip = () => { tipEl.style.display = "none"; };

  /* ---------- JSON with highlighted keys ---------- */
  function jsonPre(value, highlightKeys) {
    const hl = new Set(highlightKeys || []);
    const lines = JSON.stringify(value, null, 2).split("\n");
    return h("pre", null, lines.map((line, i) => {
      const m = line.match(/^\s*"([^"]+)":/);
      const text = line + (i < lines.length - 1 ? "\n" : "");
      return m && hl.has(m[1]) ? h("span", { className: "hl" }, text) : text;
    }));
  }

  /* ---------- episode index ---------- */
  const E = D.episodes;
  const pairIndex = new Map();
  E.forEach((e, i) => pairIndex.set([e.model, e.task, e.class, e.cond, e.phrasing, e.rep].join("|"), i));
  const findEpisode = (model, task, cls, cond, phrasing = 0, rep = 0) =>
    pairIndex.get([model, task, cls, cond, phrasing, rep].join("|"));
  const tasksById = Object.fromEntries(D.testbed.tasks.map((t) => [t.id, t]));
  /* The baseline (A) runs once per task, logged under one class, and analysis.json
     pairs it with every drift class the model ran for that task. classesOf mirrors that. */
  const pairedClasses = new Map();
  E.forEach((e) => {
    if (e.cond === "A") return;
    const k = `${e.model}|${e.task}`;
    if (!pairedClasses.has(k)) pairedClasses.set(k, new Set());
    pairedClasses.get(k).add(e.class);
  });
  const classesOf = (e) => (e.cond === "A"
    ? D.meta.classes.filter((c) => (pairedClasses.get(`${e.model}|${e.task}`) || new Set([e.class])).has(c))
    : [e.class]);
  const rate = (eps) => (eps.length ? eps.filter((e) => e.success).length / eps.length : null);

  return { D, E, PALETTE, OUTCOME_COLOR, h, s, mount, fmt, modelLabel, modelColor, condLabel,
           condShort, condDesc, classLabel, classDesc, outcomeLabel, followLabel, followDesc, sameLabel, models, toggleModel, onModelsChange,
           isVisible, seqColor, hotColor, divColor, inkOn, parseHash, href, go, tip, hideTip, jsonPre,
           findEpisode, tasksById, classesOf, rate };
})();
