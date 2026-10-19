#!/usr/bin/env python3
"""Phase 1 job grid, shared by every runner (OpenRouter, Gemini, Modal/Qwen).

Arms (pre-registered in MILESTONES.md, "Phase 1 pre-registration"):
  ablation   12 diff-following cells + C_decl, primary 120 pairs   (luna, Qwen)
  infoform   CD + Dprime, primary 120 pairs                         (all four families)
  noise      C:sys:json:none, 30 stratified tasks x 5 reps           (luna)
  thinking   chosen cells (--cells) at a non-default reasoning level (luna)

Phase 1 logs live in results/phase1/runs_<model>.jsonl, NOT in results/: analyze.py
globs results/runs_*.jsonl and must keep reproducing analysis.json byte for byte
until it is extended for Phase 1. One file per model holds every arm; records are
keyed by (task, cond, class, phrasing, rep, reasoning).
"""

import json
import pathlib
import random

import harness

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "results" / "phase1"
ARMS = ("ablation", "infoform", "noise", "thinking")
REPLICATE_C = "C:sys:json:none"
SEED = 42


def primary_pairs():
    return [(t, t["assigned"][0]) for t in harness.frozen()["tasks"]]


def noise_tasks():
    """Same 30 stratified tasks as the original noise battery."""
    tasks = sorted(harness.frozen()["tasks"], key=lambda x: x["id"])
    return [t for i, t in enumerate(tasks) if i % 4 == 0][:30]


def jobs(arm, cells=None):
    """List of (task, cond, class, phrasing, rep), shuffled with a fixed seed."""
    if arm == "ablation":
        conds = harness.ABLATION_CELLS + ["C_decl"]
        out = [(t, c, cls, 0, 0) for t, cls in primary_pairs() for c in conds]
    elif arm == "infoform":
        out = [(t, c, cls, 0, 0) for t, cls in primary_pairs() for c in ("CD", "Dprime")]
    elif arm == "noise":
        out = [(t, REPLICATE_C, t["assigned"][0], 0, rep) for t in noise_tasks() for rep in range(5)]
    elif arm == "thinking":
        if not cells:
            raise SystemExit("--arm thinking needs --cells (e.g. C:sys:json:none,C:user:json:none)")
        bad = [c for c in cells if not harness.is_phase1(c)]
        if bad:
            raise SystemExit(f"unknown Phase-1 condition(s): {bad}")
        out = [(t, c, cls, 0, 0) for t, cls in primary_pairs() for c in cells]
    else:
        raise SystemExit(f"unknown arm {arm!r}; choose from {ARMS}")
    random.Random(SEED).shuffle(out)
    return out


def out_path(model, pilot=False):
    """Pilot runs (--limit N) go to a separate *.pilot.jsonl so they never count as data."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUT_DIR / f"runs_{model.replace('/', '_')}{'.pilot' if pilot else ''}.jsonl"


def key(task_id, cond, cls, phrasing, rep, reasoning):
    return (task_id, cond, cls, phrasing, rep, reasoning)


def rec_key(r):
    return key(r["task"], r["cond"], r["class"], r["phrasing"], r.get("rep", 0), r.get("reasoning", "default"))


def load_done(path):
    if not path.exists():
        return set()
    return {rec_key(json.loads(l)) for l in path.read_text().splitlines() if l.strip()}


def tag(job, reasoning):
    t, cond, cls, ph, rep = job
    # "p1-" prefix keeps analyze.token_costs() (original study) blind to Phase-1 spend
    return f"p1-{t['id']}-{cond}-{cls}-p{ph}-r{rep}-{reasoning}"


def run_episode(job, call_model, model, arm, reasoning, max_tokens):
    t, cond, cls, ph, rep = job
    rec = harness.run_episode(t, cond, cls, call_model, phrasing_idx=ph)
    rec.update({"rep": rep, "model": model, "arm": arm, "reasoning": reasoning,
                "max_tokens": max_tokens, "phase": "phase1"})
    return rec
