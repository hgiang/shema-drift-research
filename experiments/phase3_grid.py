#!/usr/bin/env python3
"""Phase 3 job grid: the catalog arm (MILESTONES.md "Phase 3 pre-registration" and
"Phase 3 amendment 4").

One arm, `catalog`, on 40 of the 120 primary pairs (8 per drift class, drawn with the
Phase-3 seed). Each pair runs A, B_strict and C at two catalog sizes:

  small   the task's own 1-2 tool declarations: the study's baseline, unchanged
  full    all 30 frozen tools declared, exactly one of them drifted

The catalog order is drawn once here, so every episode in every family sees the drifted
tool in the same position; it is written into each record so the arm can be rebuilt.

Logs live in results/phase3/runs_<model>.jsonl; pilots go to *.pilot.jsonl and are never
analysed. Resume, keys and pins reuse the Phase-1 helpers.
"""

import random

import harness
import phase1_grid as p1
from phase1_grid import key, load_done, load_pins, pin_id, repair_tail  # noqa: F401  (shared)
from sampling_p3 import SEED_P3, draw_pairs, draw_catalog_order

OUT_DIR = p1.ROOT / "results" / "phase3"
ARMS = ("catalog",)
CONDS = ("A", "B_strict", "C")
CATALOGS = ("small", "full")
PER_CLASS = 8
SEED = 42  # job order, as in Phase 1 and Phase 2

PAIRS = draw_pairs(p1.primary_pairs(), PER_CLASS)
CATALOG_ORDER = draw_catalog_order(sorted(harness.frozen()["tools_v1"]))


def jobs(arm="catalog"):
    """List of (task, cond, class, catalog), shuffled with the usual fixed seed."""
    if arm != "catalog":
        raise SystemExit(f"unknown Phase-3 arm {arm!r}; choose from {ARMS}")
    out = [(t, c, cls, cat) for t, cls in PAIRS for c in CONDS for cat in CATALOGS]
    random.Random(SEED).shuffle(out)
    return out


def rec_key(r):
    """The key a record resumes on: the Phase-1 key plus the catalog size."""
    return (r["task"], r["cond"], r["class"], r.get("catalog", "small"))


def job_key(job):
    t, cond, cls, cat = job
    return (t["id"], cond, cls, cat)


def out_path(model, pilot=False):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = ".pilot" if pilot else ""
    return OUT_DIR / f"runs_{model.replace('/', '_')}{suffix}.jsonl"


def tag(job, reasoning):
    t, cond, cls, cat = job
    return f"p3-{t['id']}-{cond}-{cls}-{cat}-{reasoning}"


def run_episode(job, call_model, model, reasoning, max_tokens, pin):
    t, cond, cls, cat = job
    rec = harness.run_episode(t, cond, cls, call_model, catalog=cat)
    return {**rec, "model": model, "arm": "catalog", "catalog": cat,
            "n_declarations": len(harness.build_condition(t, cond, cls, catalog=cat)["declarations"]),
            "reasoning": reasoning, "max_tokens": max_tokens, "phase": "phase3",
            "catalog_seed": SEED_P3, "pin": pin}
