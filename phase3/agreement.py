#!/usr/bin/env python3
"""Inter-coder reliability for the Phase-3 corpus (MILESTONES.md "Phase 3 amendment 1").

Three figures, because the two coders disagree in two different ways:
  * unit-set agreement — did they find the same units at all (both / either)?
  * label agreement — on the units both found, raw agreement and Cohen's kappa;
  * `agent_visible` agreement — the same, on the same set.

Prevalence is computed on the agreed set only, so a disagreement can never be resolved in
the direction a prediction wants. Nothing here looks at a prediction.
"""

import pathlib
import json

THRESHOLD = 0.90  # locked: raw agreement on `label`


def _key(unit):
    return (unit["digest_id"], unit["parameter"])


def _index(units):
    return {_key(u): u for u in units}


def unit_sets(a, b):
    """Which units each coder found, and the overlap the corpus is built from."""
    ia, ib = _index(a), _index(b)
    both = sorted(set(ia) & set(ib))
    either = set(ia) | set(ib)
    return {"n_a": len(ia), "n_b": len(ib), "n_both": len(both),
            "n_only_a": len(set(ia) - set(ib)), "n_only_b": len(set(ib) - set(ia)),
            "jaccard": round(len(both) / len(either), 4) if either else None,
            "agreed": both,
            "only_a": sorted(set(ia) - set(ib)), "only_b": sorted(set(ib) - set(ia))}


def _kappa(pairs):
    """Cohen's kappa. None when one value is used everywhere: chance agreement is 1."""
    n = len(pairs)
    if not n:
        return None
    observed = sum(x == y for x, y in pairs) / n
    values = {v for pair in pairs for v in pair}
    expected = sum((sum(x == v for x, _ in pairs) / n) * (sum(y == v for _, y in pairs) / n)
                   for v in values)
    if expected >= 1.0:
        return None
    return round((observed - expected) / (1 - expected), 4)


def _compare(a, b, field):
    ia, ib = _index(a), _index(b)
    agreed = sorted(set(ia) & set(ib))
    pairs = [(ia[k][field], ib[k][field]) for k in agreed]
    disagreements = [{"digest_id": k[0], "parameter": k[1], "a": x, "b": y}
                     for k, (x, y) in zip(agreed, pairs) if x != y]
    n_agree = len(pairs) - len(disagreements)
    return {"n": len(pairs), "n_agree": n_agree,
            "rate": round(n_agree / len(pairs), 4) if pairs else None,
            "kappa": _kappa(pairs), "disagreements": disagreements}


def label_agreement(a, b):
    return _compare(a, b, "label")


def visible_agreement(a, b):
    return _compare(a, b, "agent_visible")


def report(a, b, threshold=THRESHOLD):
    """Every figure, plus the locked threshold verdict (None while nothing is comparable)."""
    label = label_agreement(a, b)
    passes = None if not label["n"] else label["rate"] >= threshold
    return {"unit_sets": unit_sets(a, b), "label": label,
            "agent_visible": visible_agreement(a, b),
            "threshold": threshold, "passes": passes}


def load(path):
    return [json.loads(line) for line in pathlib.Path(path).read_text().splitlines() if line.strip()]


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    here = pathlib.Path(__file__).resolve().parent.parent / "results" / "phase3"
    ap.add_argument("--a", type=pathlib.Path, default=here / "labels_codex.jsonl")
    ap.add_argument("--b", type=pathlib.Path, default=here / "labels_sonnet.jsonl")
    ap.add_argument("--out", type=pathlib.Path, default=here / "agreement.json")
    args = ap.parse_args(argv)
    out = report(load(args.a), load(args.b))
    args.out.write_text(json.dumps(out, indent=1) + "\n")
    sets, label = out["unit_sets"], out["label"]
    print(f"units: coder A {sets['n_a']}, coder B {sets['n_b']}, both {sets['n_both']}, "
          f"Jaccard {sets['jaccard']}")
    print(f"label: {label['n_agree']}/{label['n']} = {label['rate']} (kappa {label['kappa']}), "
          f"threshold {out['threshold']} -> {out['passes']}")
    print(f"agent_visible: {out['agent_visible']['rate']} -> {args.out}")


if __name__ == "__main__":
    main()
