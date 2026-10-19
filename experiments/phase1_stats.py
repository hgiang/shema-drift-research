#!/usr/bin/env python3
"""Phase-1 statistics: pure functions, no file I/O, every random function takes `rng`.

Implements the locked pre-registration (MILESTONES.md "Phase 1 pre-registration") and the
addendum's analysis pins A1-A9. `tab` maps a condition (or (condition, reasoning)) to
{(task, class): 0|1}; the caller expands class-independent A to every pair.
"""

import itertools

import numpy as np

from harness import ABLATION_CELLS, FORMATS, INSTRS, PLACES

CONTRAST = ("rename", "enum_tighten", "type_change")
INFO = ("required", "default_change")
REPLICATE_C = "C:sys:json:none"
BEST_CELL_CANDIDATES = [c for c in ABLATION_CELLS if c != REPLICATE_C] + ["C_decl"]  # pin A6: 12 cells
SYS_CELLS = [c for c in ABLATION_CELLS if c.startswith("C:sys:")]
NOISE_REPS = 5
FAMILIES = ("openai/gpt-5.6-luna", "modal-qwen2.5-7b", "gemini-3.6-flash", "gemini-3.1-pro-preview")
GEMINI = ("gemini-3.6-flash", "gemini-3.1-pro-preview")
FACTORS = {"place": PLACES, "fmt": FORMATS, "instr": INSTRS}
FACTOR_GRID = list(itertools.product(PLACES, FORMATS, INSTRS))
UNLOCK_RECOVERY = 0.5
P5_MIN_GAIN = 0.30
P6_BAND = 0.10
P9_MAX_FILL, P9_MIN_DROP = 0.90, 0.20


def cell(place, fmt, instr):
    return f"C:{place}:{fmt}:{instr}"


def pairs_in(pairs, classes=None):
    return [p for p in pairs if classes is None or p[1] in classes]


def cell_vector(tab, cond, pairs):
    """0/1 success per pair, in `pairs` order; KeyError names anything missing (no silent drops)."""
    if cond not in tab:
        raise KeyError(f"condition {cond!r} not in table")
    missing = [p for p in pairs if p not in tab[cond]]
    if missing:
        raise KeyError(f"{cond}: {len(missing)} pairs missing, e.g. {missing[:3]}")
    return np.array([tab[cond][p] for p in pairs], dtype=float)


def recovery(a, b, x, rng, n_boot=10_000):
    """(success(X) - success(B)) / (success(A) - success(B)), paired; bootstrap over pairs
    as in analyze.analyze_model. None when there is no drop to recover."""
    a, b, x = (np.asarray(v, dtype=float) for v in (a, b, x))
    denom = (a - b).mean()
    if denom <= 0:
        return {"point": None, "ci95": None}
    idx = rng.integers(0, len(a), size=(n_boot, len(a)))
    num_bs = (x[idx] - b[idx]).mean(axis=1)
    den_bs = (a[idx] - b[idx]).mean(axis=1)
    ok = den_bs > 0
    rf = num_bs[ok] / den_bs[ok]
    return {"point": float((x - b).mean() / denom),
            "ci95": [float(np.percentile(rf, 2.5)), float(np.percentile(rf, 97.5))]}


def _mean_over(tab, pairs, fixed):
    """Per-pair mean success over the ablation cells matching `fixed` (factor -> level)."""
    cells = [cell(p, f, i) for p, f, i in FACTOR_GRID
             if all(dict(zip(FACTORS, (p, f, i)))[k] == v for k, v in fixed.items())]
    return np.mean([cell_vector(tab, c, pairs) for c in cells], axis=0)


def main_effect(tab, pairs, factor, level, ref):
    """Pin A3: per-pair contrast level - ref, each side averaged over the other two factors'
    cells (4 cells per side for place, 6 for format and instruction)."""
    if factor not in FACTORS or level not in FACTORS[factor] or ref not in FACTORS[factor]:
        raise ValueError(f"unknown factor/level: {factor} {level} {ref}")
    return _mean_over(tab, pairs, {factor: level}) - _mean_over(tab, pairs, {factor: ref})


def effect_by_place(tab, pairs, factor):
    """Pin A2: e_ip = effect of `factor` ("fmt": prose-json, "instr": apply-none) at place p,
    averaged over the third factor. Shape (n_pairs, 3), columns in PLACES order."""
    level, ref = {"fmt": ("prose", "json"), "instr": ("apply", "none")}[factor]
    return np.stack([_mean_over(tab, pairs, {"place": p, factor: level})
                     - _mean_over(tab, pairs, {"place": p, factor: ref}) for p in PLACES], axis=1)


def perm_within_pairs(E, rng, n_perm=20_000):
    """Pin A2: T = variance over places of the column means; the null permutes the three
    place labels within each pair. p = share of permutations with T >= observed."""
    E = np.asarray(E, dtype=float)
    obs = E.mean(axis=0).var()
    if np.allclose(E, E[:, :1]):  # no within-pair variation: every permutation ties
        return 1.0
    hits, chunk = 0, 2000
    for start in range(0, n_perm, chunk):
        k = min(chunk, n_perm - start)
        order = rng.random((k,) + E.shape).argsort(axis=2)
        perm = np.take_along_axis(np.broadcast_to(E, (k,) + E.shape), order, axis=2)
        hits += int((perm.mean(axis=1).var(axis=1) >= obs - 1e-12).sum())
    return hits / n_perm


def fmt_instr_contrast(tab, pairs):
    """Per-pair 2x2 interaction (prose,apply - prose,none) - (json,apply - json,none), averaged
    over place; tested with a sign-flip by the caller."""
    m = {(f, i): _mean_over(tab, pairs, {"fmt": f, "instr": i}) for f in FORMATS for i in INSTRS}
    return (m["prose", "apply"] - m["prose", "none"]) - (m["json", "apply"] - m["json", "none"])


def flip_rate(reps, n_reps=NOISE_REPS):
    """Share of pairs whose repeated identical calls did not all give the same success.
    Only pairs with all n_reps repetitions count (as analyze.analyze_noise); None if none do."""
    full = [v for v in reps.values() if len(v) == n_reps]
    return float(np.mean([len(set(v)) > 1 for v in full])) if full else None


def within_noise(mean, floor):
    return abs(mean) < floor


def unlocks(recovery_point, ci_low, survives_bh, mean, floor):
    """Locked rule: recovery >= 0.5, CI of X - B_strict excludes 0, BH survives, not within noise."""
    return (recovery_point is not None and recovery_point >= UNLOCK_RECOVERY and ci_low > 0
            and bool(survives_bh) and not within_noise(mean, floor))


def select_best_cell(recoveries, success_all, order):
    """Pin A6: highest recovery; ties -> higher success on all pairs -> earlier in `order`.
    Candidates are the 12 non-replicate cells only; cells with no recovery (None) rank last."""
    cands = [c for c in order if c in BEST_CELL_CANDIDATES and c in recoveries]
    score = lambda c: (-np.inf if recoveries[c] is None else recoveries[c], success_all.get(c, -np.inf),
                       -order.index(c))
    return max(cands, key=score)


def _cell_unlocks(c, floor):
    return unlocks(c["recovery"], c["ci_low"], c["bh"], c["mean"], floor)


def _p1(luna):
    """The C re-run counts as a system-prompt cell (conservative: if it unlocks, P1 fails)."""
    present = [c for c in SYS_CELLS if c in luna["cells"]]
    hits = [c for c in present if _cell_unlocks(luna["cells"][c], luna["floor"])]
    holds = False if hits else (True if len(present) == len(SYS_CELLS) else None)
    return {"holds": holds, "basis": f"system-prompt cells that unlock: {hits or 'none'} "
                                     f"of {len(present)}/{len(SYS_CELLS)} present"}


def _p2(luna):
    m, floor = luna["main"], luna["floor"]
    place = max(m["user-sys"], m["tool-sys"])
    holds = place > m["prose-json"] and place > m["apply-none"] and not within_noise(place, floor)
    return {"holds": holds, "basis": f"max placement {place:+.3f} vs prose-json {m['prose-json']:+.3f}, "
                                     f"apply-none {m['apply-none']:+.3f}, noise floor {floor:.3f} (pin A4)"}


def _p3(qwen):
    p3 = qwen.get("p3") if qwen else None
    if not p3:
        return {"holds": None, "basis": "Qwen type_change labels not available"}
    return {"holds": p3["mean"] > 0 and p3["ci95"][0] > 0,
            "basis": f"prose - JSON V2_CORRECT share {p3['mean']:+.3f}, CI {p3['ci95']} (pin A7)"}


def _p4(luna):
    th = luna.get("thinking")
    if not th:
        return {"holds": None, "basis": "thinking arm not run"}
    pts = {c: v["recovery"] for c, v in th.items()}
    if any(v is not None and v >= UNLOCK_RECOVERY for v in pts.values()):
        holds = False
    else:
        holds = None if any(v is None for v in pts.values()) else True
    return {"holds": holds, "basis": f"recovery at high effort {pts}; holds when every cell < {UNLOCK_RECOVERY}"}


def _families(stats, key, names=FAMILIES):
    fam = stats.get("families") or {}
    return {f: fam[f][key] for f in names if f in fam and key in fam[f]}


def _p5(stats):
    got = _families(stats, "Dprime-D_required")
    fails = [f for f, v in got.items() if v["mean"] < P5_MIN_GAIN]
    if fails or len(got) < len(FAMILIES):
        holds = False if fails else None
    else:
        holds = True
    return {"holds": holds, "basis": f"D' - D on required, means {({f: round(v['mean'], 3) for f, v in got.items()})}; "
                                     f"needs >= {P5_MIN_GAIN} in all {len(FAMILIES)} families"}


def _p6(stats):
    got = _families(stats, "Dprime-C", GEMINI)
    inside = {f: -P6_BAND <= v["ci95"][0] and v["ci95"][1] <= P6_BAND for f, v in got.items()}
    if not all(inside.values()):
        holds = False
    else:
        holds = True if len(got) == len(GEMINI) else None
    return {"holds": holds, "basis": f"D' - C CI inside [-{P6_BAND}, {P6_BAND}]: {inside}"}


def _p7(stats):
    below = [f for key in ("CD-C", "CD-D") for f, v in _families(stats, key).items() if v["ci95"][1] < 0]
    complete = all(len(_families(stats, k)) == len(FAMILIES) for k in ("CD-C", "CD-D"))
    holds = False if below else (True if complete else None)
    return {"holds": holds, "basis": f"families with a C+D CI wholly below 0: {sorted(set(below)) or 'none'} (pin A7)"}


def _p8_p9(route, luna_floor):
    if not route:
        none = {"holds": None, "basis": "route arm not run (amendment 1)"}
        return none, dict(none)
    p8 = {"holds": _cell_unlocks(route["C"], luna_floor), "basis": f"route C {route['C']}, noise floor {luna_floor}"}
    drop = route["bstrict_change"]["mean"]
    p9 = {"holds": route["fill_rate_A"] < P9_MAX_FILL and drop <= -P9_MIN_DROP,
          "basis": f"fill rate A {route['fill_rate_A']:.3f} (< {P9_MAX_FILL}), "
                   f"B_strict change on required+default {drop:+.3f} (<= -{P9_MIN_DROP})"}
    return p8, p9


def verdicts(stats):
    """P1-P9 judged by code: {"holds": True | False | None (arm not run), "basis": str}."""
    luna = stats["luna"]
    p8, p9 = _p8_p9(stats.get("route"), luna["floor"])
    return {"P1": _p1(luna), "P2": _p2(luna), "P3": _p3(stats.get("qwen")), "P4": _p4(luna),
            "P5": _p5(stats), "P6": _p6(stats), "P7": _p7(stats), "P8": p8, "P9": p9}
