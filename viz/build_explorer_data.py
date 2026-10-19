#!/usr/bin/env python3
"""Bundle the testbed, every logged episode, analysis.json, and the audit into
docs/explorer/data.js for the static SchemaDrift-120 explorer.

Reads only; every number shown by the explorer comes from results/ (curated
views read analysis.json verbatim, the pivot recomputes rates from the same
deduplicated episodes analyze.py uses). Output is deterministic.

    python3 viz/build_explorer_data.py            # -> docs/explorer/data.js
"""

import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXPERIMENTS = ROOT / "experiments"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
OUT = ROOT / "docs" / "explorer" / "data.js"
BUNDLE_PREFIX = "window.SD_DATA = "

sys.path.insert(0, str(EXPERIMENTS))
sys.path.insert(0, str(FIGURES))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "phase1"))
import analyze  # noqa: E402  (load_runs: the same dedupe analysis.json uses)
import harness  # noqa: E402
import episode_semantics as sem  # noqa: E402
from style import FAMILY_COLOR, FAMILY_LABEL  # noqa: E402  (house palette)
import step1_diag_diff_following as follow  # noqa: E402  (Phase 1 step 1 classifier)

COND_LABELS = {  # id: (label, short label, description)
    "A": ("v1 baseline", "A · baseline", "Agent sees v1, executor enforces v1."),
    "B_strict": ("silent drift · strict", "B · strict", "Agent sees v1, executor enforces v2 and rejects any violation."),
    "B_lenient": ("silent drift · lenient", "B · lenient", "Agent sees v1, executor enforces v2 but drops unknown fields and coerces types."),
    "C": ("+ structured diff", "C · diff", "Agent sees v1 plus a machine-readable change log in the system prompt; strict v2 executor."),
    "D": ("+ full v2 schema", "D · v2 schema", "Agent sees the v2 schema; strict v2 executor."),
    "E": ("+ raw-error retry", "E · retry", "Agent sees v1; strict v2 executor; the raw error is fed back with one retry per step."),
}
CLASS_LABELS = {
    "rename": ("renamed parameter", "A parameter is renamed; the old name is unknown to v2."),
    "enum_tighten": ("tightened enum", "An enum value is retired and replaced."),
    "required": ("newly required", "An optional parameter becomes required."),
    "type_change": ("type change", "An integer becomes a formatted string in different units."),
    "default_change": ("default change", "A documented default value flips."),
}
OUTCOME_LABELS = {
    "ERROR_SURFACED": "error surfaced",
    "ACCEPTED_CORRECT": "accepted, correct",
    "ACCEPTED_WRONG": "accepted, wrong semantics",
    None: "no drifted call",
}
COND_ORDER = list(COND_LABELS)
FOLLOW_LABELS = {  # Phase 1 step 1: what the model did at the drifted step
    "V2_CORRECT": ("applied v2", "Accepted with correct semantics. For newly-required and default-change this is counted only when the same pair failed under silent drift."),
    "V2_PARTIAL": ("partly applied", "Moved off the v1 form on the drifted parameter but got it wrong (e.g. string type, old unit)."),
    "V1_FORM": ("v1 call", "Used the v1 contract on the drifted parameter: old name, old enum value, int type, or omitted the newly-required / default-changed parameter."),
    "V1_SAFE": ("safe anyway", "Correct, but the same pair also succeeded under silent drift: the model fills the parameter explicitly regardless, so this says nothing about reading the change."),
    "OTHER_ERROR": ("other error", "Executor error on a parameter that did not drift."),
    "OTHER_WRONG": ("other wrong", "Drifted parameter right, another argument wrong."),
    "NO_DRIFT_CALL": ("no drifted call", "The drifted step was never reached."),
    "n/a": ("n/a (baseline)", "Baseline episodes have no drift."),
}
SAME_LABELS = {"1": "same call as silent drift", "0": "different from silent drift",
               "n/a": "n/a (A or B · strict)"}


def view_key(task_id, cls, cond):
    return f"{task_id}|{cls}|{cond}"


def battery_of(record):
    if record.get("rep", 0):
        return "noise"
    if record["phrasing"]:
        return "phrasing"
    return "core"


def _read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read {path.relative_to(ROOT)}: {exc}") from exc


class _Interner:
    """Deduplicate prompt fragments so 1,500 views share a few hundred strings."""

    def __init__(self):
        self.items, self._index = [], {}

    def add(self, value):
        key = json.dumps(value, sort_keys=True)
        if key not in self._index:
            self._index[key] = len(self.items)
            self.items.append(value)
        return self._index[key]


def build_testbed(frozen):
    tools = frozen["tools_v1"]
    tasks = [{**t, "domain": tools[t["drift_tool"]]["domain"]} for t in frozen["tasks"]]
    return {"name": frozen["name"], "frozen_at": frozen["frozen_at"],
            "classes": frozen["classes"], "per_class_pairs": frozen["per_class_pairs"],
            "tools": tools, "tasks": tasks, "diffs": frozen["diffs"],
            "v2_schemas": frozen["v2_schemas"]}


def follow_fields(r, by_key):
    """Phase 1 step 1 fields: the drifted-call label and whether the call is the
    same one the model made under silent drift (B_strict) on the same pair."""
    if r["cond"] == "A":
        return {"follow": "n/a", "same_as_B": "n/a"}
    b = by_key.get((r["model"], r["task"], r["class"], "B_strict", r["phrasing"], r.get("rep", 0)))
    label, _ = follow.classify(r, b)
    if r["cond"] == "B_strict" or b is None:
        same = "n/a"
    else:
        same = "1" if follow.signature(r) == follow.signature(b) else "0"
    return {"follow": label, "same_as_B": same}


def build_episodes(runs, tasks_by_id, tools_v1):
    """Annotate each deduplicated record; return (episodes, views, prompts)."""
    systems, decls, views, setups = _Interner(), _Interner(), {}, {}
    episodes = []
    by_key = {(r["model"], r["task"], r["class"], r["cond"], r["phrasing"], r.get("rep", 0)): r
              for r in runs}
    for r in runs:
        key = view_key(r["task"], r["class"], r["cond"])
        if key not in setups:
            setup = harness.build_condition(tasks_by_id[r["task"]], r["cond"], r["class"])
            setups[key] = setup
            views[key] = {"system": systems.add(setup["system"]),
                          "decls": [decls.add(d) for d in setup["declarations"]],
                          "profile": setup["profile"], "retry": setup["retry"]}
        task = tasks_by_id[r["task"]]
        episodes.append({
            "model": r["model"], "task": r["task"], "cond": r["cond"], "class": r["class"],
            "phrasing": r["phrasing"], "rep": r.get("rep", 0), "battery": battery_of(r),
            "domain": tools_v1[task["drift_tool"]]["domain"], "n_steps": r["n_steps"],
            "success": bool(r["success"]), "drift_outcome": r["drift_outcome"],
            "error_seen": r["error_seen"], "calls_made": r["calls_made"],
            "executed": sem.annotate_executed(r, task, setups[key], tools_v1),
            **follow_fields(r, by_key),
        })
    episodes.sort(key=lambda e: (e["model"], e["battery"], COND_ORDER.index(e["cond"]),
                                 e["class"], e["task"], e["phrasing"], e["rep"]))
    return episodes, dict(sorted(views.items())), {"system": systems.items, "decls": decls.items}


def build_labels(models):
    return {
        "models": {m: {"label": FAMILY_LABEL.get(m, m), "color": FAMILY_COLOR.get(m, "#6d665a")}
                   for m in models},
        "conds": {c: {"label": lab, "short": short, "desc": desc}
                  for c, (lab, short, desc) in COND_LABELS.items()},
        "classes": {c: {"label": lab, "desc": desc} for c, (lab, desc) in CLASS_LABELS.items()},
        "outcomes": {("null" if k is None else k): v for k, v in OUTCOME_LABELS.items()},
        "follow": {k: {"label": lab, "desc": desc} for k, (lab, desc) in FOLLOW_LABELS.items()},
        "same_as_B": SAME_LABELS,
    }


def build_payload():
    frozen = _read_json(EXPERIMENTS / "testbed_frozen.json")
    analysis = _read_json(RESULTS / "analysis.json")
    audit = _read_json(RESULTS / "audit_accepted_wrong_sample.json")
    testbed = build_testbed(frozen)
    tasks_by_id = {t["id"]: t for t in testbed["tasks"]}
    episodes, views, prompts = build_episodes(analyze.load_runs(), tasks_by_id, testbed["tools"])

    if len(episodes) != analysis["n_records"]:
        raise SystemExit(f"{len(episodes)} episodes but analysis.json reports "
                         f"{analysis['n_records']}; re-run experiments/analyze.py first")

    models = list(analysis["models"])
    sha_file = (EXPERIMENTS / "testbed_frozen.sha256").read_text().split()[0]
    return {
        "meta": {"n_records": len(episodes), "models": models, "conds": COND_ORDER,
                 "classes": testbed["classes"], "testbed_sha256": sha_file,
                 "analysis_sha256": hashlib.sha256(
                     (RESULTS / "analysis.json").read_bytes()).hexdigest()},
        "labels": build_labels(models),
        "analysis": analysis,
        "audit": audit,
        "testbed": testbed,
        "prompts": prompts,
        "views": views,
        "episodes": episodes,
    }


def write_bundle(payload, out=OUT):
    out.parent.mkdir(parents=True, exist_ok=True)
    body = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    out.write_text(f"{BUNDLE_PREFIX}{body};\n", encoding="utf-8")


def main():
    payload = build_payload()
    write_bundle(payload)
    size_kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT.relative_to(ROOT)}: {payload['meta']['n_records']} episodes, "
          f"{len(payload['views'])} prompt views, {size_kb:,.0f} KB")


if __name__ == "__main__":
    main()
