#!/usr/bin/env python3
"""Phase-3 block of analysis.json: the changelog corpus (MILESTONES.md "Phase 3
pre-registration", amendments 1 and 2). Called by analyze.main, never importing analyze.

The corpus is descriptive: prevalence shares are not paired tests and register nothing with
BH. `ctx` supplies only the Phase-3 bootstrap:
  ctx.rng, ctx.share(flags) -> {"point", "ci95", "n"}

Shares are reported pooled **and** per source. The pooled figure is source-weighted and says
so, because three of the four sources ran out of material (amendment 2).
"""

import collections
import json
import pathlib

import phase3_stats as v

CORPUS, AGREEMENT = "corpus.jsonl", "agreement.json"
SUMMARY, DIGESTS = "corpus_summary.json", "digests_summary.json"


def _read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def load_corpus(phase3_dir):
    path = pathlib.Path(phase3_dir) / CORPUS
    return _read_jsonl(path) if path.exists() else []


def _read(phase3_dir, name):
    path = pathlib.Path(phase3_dir) / name
    return json.loads(path.read_text()) if path.exists() else None


def flags(rows):
    """The four 0/1 vectors the predictions are shares of."""
    decided = [r for r in rows if r["agent_visible"] is not None]
    return {"coverage": [r["label"] in v.COVERED for r in rows],
            "costly": [r["label"] in v.COSTLY for r in rows],
            "reach": [bool(r["agent_visible"]) for r in decided],
            "compound": [r["label"] == "compound" for r in rows]}


def shares(rows, ctx):
    return {name: ctx.share(vec) for name, vec in flags(rows).items()}


def counts(rows):
    labels = collections.Counter(r["label"] for r in rows)
    visible = collections.Counter("unknown" if r["agent_visible"] is None
                                  else str(r["agent_visible"]).lower() for r in rows)
    return {"n_units": len(rows),
            "n_entries": len({(r["source"], r["draw_rank"]) for r in rows}),
            "labels": {k: labels.get(k, 0) for k in v.COVERED + ("other",) if labels.get(k)},
            "agent_visible": {k: visible.get(k, 0) for k in ("true", "false", "unknown")}}


def by_source(rows, ctx):
    out = {}
    for source in sorted({r["source"] for r in rows}):
        part = [r for r in rows if r["source"] == source]
        out[source] = {**counts(part), "shares": shares(part, ctx)}
    return out


def analyze(phase3_dir, ctx):
    """The corpus block, or None when no corpus has been built yet."""
    rows = load_corpus(phase3_dir)
    if not rows:
        return None
    agreement = _read(phase3_dir, AGREEMENT)
    return {
        "pooled": {**counts(rows), "shares": shares(rows, ctx),
                   "note": "source-weighted: read beside by_source"},
        "by_source": by_source(rows, ctx),
        "agreement": agreement,
        "coding": {"corpus_summary": _read(phase3_dir, SUMMARY),
                   "digests": _read(phase3_dir, DIGESTS)},
        "status": {} if agreement else {"agreement": "missing"},
    }


def predictions(block):
    """P17-P20 on the pooled corpus (descriptive; nothing here joins the BH family)."""
    return v.verdicts(block["pooled"]["shares"])
