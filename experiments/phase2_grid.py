#!/usr/bin/env python3
"""Phase 2 job grid, shared by the runners (OpenRouter / OpenAI direct, Gemini).

Arms (pre-registered in MILESTONES.md, "Phase 2 pre-registration"), primary 120 pairs:
  core       A, B_strict, B_lenient, C, D, E (September's grid)          (new families)
  phrasing   A and B_strict on phrasing 1                                (new families)
  noise      B_strict, 30 stratified tasks x 5 reps                      (new families)
  infoform   CD + Dprime                                                 (new families)
  placement  C:user:prose:apply, Qwen's best Phase-1 cell                (new families)
  fill       A_fill, B_fill and a B_strict re-run                        (Gemini Flash)
  direct     A, B_strict, C:sys:json:none, C:user:prose:apply            (luna, OpenAI direct; contingent)

Rep 0 of the noise arm has the same key as the core B_strict record, so a model that ran
core first gets 120 new noise episodes, not 150 (as in Phase 1, where noise shared rep 0
with the ablation's C re-run).

Logs live in results/phase2/runs_<model>[.<endpoint>].jsonl; one file per model and
endpoint holds every arm. Resume, pins and keys reuse the Phase-1 helpers.
"""

import random
import re

import harness
import phase1_grid as p1
from phase1_grid import key, load_done, load_pins, pin_id, rec_key, repair_tail  # noqa: F401  (shared)

OUT_DIR = p1.ROOT / "results" / "phase2"
ARMS = ("core", "phrasing", "noise", "infoform", "placement", "fill", "direct")
CORE_CONDS = ("A", "B_strict", "B_lenient", "C", "D", "E")
PLACEMENT_CELL = "C:user:prose:apply"
FILL_CONDS = ("A_fill", "B_fill", "B_strict")
DIRECT_CONDS = ("A", "B_strict", p1.REPLICATE_C, PLACEMENT_CELL)
SEED = 42


def _per_pair(conds, phrasing=0):
    return [(t, c, cls, phrasing, 0) for t, cls in p1.primary_pairs() for c in conds]


def jobs(arm):
    """List of (task, cond, class, phrasing, rep), shuffled with a fixed seed."""
    if arm == "core":
        out = _per_pair(CORE_CONDS)
    elif arm == "phrasing":
        out = _per_pair(("A", "B_strict"), phrasing=1)
    elif arm == "noise":
        out = [(t, "B_strict", t["assigned"][0], 0, rep) for t in p1.noise_tasks() for rep in range(5)]
    elif arm == "infoform":
        out = _per_pair(("CD", "Dprime"))
    elif arm == "placement":
        out = _per_pair((PLACEMENT_CELL,))
    elif arm == "fill":
        out = _per_pair(FILL_CONDS)
    elif arm == "direct":
        out = _per_pair(DIRECT_CONDS)
    else:
        raise SystemExit(f"unknown Phase-2 arm {arm!r}; choose from {ARMS}")
    random.Random(SEED).shuffle(out)
    return out


def out_path(model, pilot=False, endpoint=None):
    """runs_<model>.jsonl for OpenRouter and Gemini; runs_<model>.<endpoint>.jsonl otherwise.
    Pilot runs (--limit N) go to *.pilot.jsonl and are never analysed."""
    if endpoint is not None and not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", endpoint):
        raise SystemExit(f"endpoint {endpoint!r}: use lowercase letters, digits, '-' or '_'")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = (f".{endpoint}" if endpoint not in (None, "openrouter") else "") + (".pilot" if pilot else "")
    return OUT_DIR / f"runs_{model.replace('/', '_')}{suffix}.jsonl"


def tag(job, reasoning):
    t, cond, cls, ph, rep = job
    return f"p2-{t['id']}-{cond}-{cls}-p{ph}-r{rep}-{reasoning}"


def run_episode(job, call_model, model, arm, reasoning, max_tokens, pin):
    t, cond, cls, ph, rep = job
    rec = harness.run_episode(t, cond, cls, call_model, phrasing_idx=ph)
    return {**rec, "rep": rep, "model": model, "arm": arm, "reasoning": reasoning,
            "max_tokens": max_tokens, "phase": "phase2", "pin": pin}
