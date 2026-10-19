#!/usr/bin/env python3
"""Tests for the Phase-1 statistics (synthetic tables with planted effects). No I/O.

Run: python3 -m pytest test_phase1_stats.py -q
"""

import pathlib
import sys

import numpy as np
import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase1_stats as st  # noqa: E402

PAIRS = [(f"t{i:02d}", cls) for i, cls in enumerate(["rename", "enum_tighten", "type_change"] * 24)]


def table(fn, pairs=PAIRS, cells=None):
    cells = cells or harness.ABLATION_CELLS
    return {c: {p: int(fn(c, p)) for p in pairs} for c in cells}


def rng():
    return np.random.default_rng(0)


def test_cells_match_the_harness_grid():
    assert st.cell("user", "prose", "apply") == "C:user:prose:apply"
    assert sorted(st.cell(*f) for f in st.FACTOR_GRID) == sorted(harness.ABLATION_CELLS)


def test_main_effect_recovers_planted_placement():
    tab = table(lambda c, p: c.startswith("C:user:"))
    assert np.allclose(st.main_effect(tab, PAIRS, "place", "user", "sys"), 1.0)
    assert np.allclose(st.main_effect(tab, PAIRS, "place", "tool", "sys"), 0.0)
    assert np.allclose(st.main_effect(tab, PAIRS, "fmt", "prose", "json"), 0.0)
    assert np.allclose(st.main_effect(tab, PAIRS, "instr", "apply", "none"), 0.0)
    half = table(lambda c, p: c == "C:sys:prose:apply")  # one of the 6 prose cells
    assert np.allclose(st.main_effect(half, PAIRS, "fmt", "prose", "json"), 1 / 6)
    with pytest.raises(ValueError):
        st.main_effect(tab, PAIRS, "colour", "red", "blue")


def test_place_interaction_null_and_planted():
    noise = np.random.default_rng(7)
    random_tab = {c: {p: int(noise.random() < 0.5) for p in PAIRS} for c in harness.ABLATION_CELLS}
    E = st.effect_by_place(random_tab, PAIRS, "fmt")
    assert E.shape == (72, 3)
    assert st.perm_within_pairs(E, rng(), n_perm=2000) > 0.2
    planted = table(lambda c, p: c.startswith("C:tool:prose:"))  # format effect only at tool
    E = st.effect_by_place(planted, PAIRS, "fmt")
    assert np.allclose(E[:, st.PLACES.index("tool")], 1.0) and np.allclose(E[:, :2], 0.0)
    assert st.perm_within_pairs(E, rng(), n_perm=2000) < 0.01
    assert st.perm_within_pairs(np.zeros((72, 3)), rng(), n_perm=200) == 1.0


def test_fmt_instr_contrast_planted():
    tab = table(lambda c, p: c.endswith(":prose:apply"))
    assert np.allclose(st.fmt_instr_contrast(tab, PAIRS), 1.0)
    additive = table(lambda c, p: ":prose:" in c)  # format only, no interaction
    assert np.allclose(st.fmt_instr_contrast(additive, PAIRS), 0.0)


def test_recovery_formula():
    g = np.random.default_rng(3)
    a = np.ones(72)
    b = (g.random(72) < 0.3).astype(float)
    x = np.maximum(b, (g.random(72) < 0.6).astype(float))
    r = st.recovery(a, b, x, rng(), n_boot=2000)
    assert r["point"] == pytest.approx((x - b).mean() / (a - b).mean())
    assert r["ci95"][0] <= r["point"] <= r["ci95"][1]
    assert st.recovery(b, b, x, rng(), n_boot=10) == {"point": None, "ci95": None}  # no drop to recover


def test_cell_vector_missing_pair_raises():
    tab = table(lambda c, p: 1)
    assert st.cell_vector(tab, "C:sys:json:none", PAIRS[:3]).tolist() == [1.0, 1.0, 1.0]
    with pytest.raises(KeyError, match="t99"):
        st.cell_vector(tab, "C:sys:json:none", PAIRS[:2] + [("t99", "rename")])
    with pytest.raises(KeyError, match="NOPE"):
        st.cell_vector(tab, "NOPE", PAIRS)


def test_pairs_in():
    assert len(st.pairs_in(PAIRS, st.CONTRAST)) == 72
    assert st.pairs_in(PAIRS, ("rename",)) == [p for p in PAIRS if p[1] == "rename"]
    assert st.pairs_in(PAIRS) == PAIRS


def test_flip_rate():
    assert st.flip_rate({("a", "x"): [1] * 5, ("b", "x"): [1, 0, 1, 1, 1]}) == 0.5
    assert st.within_noise(0.05, 0.1) and not st.within_noise(-0.2, 0.1)


def test_select_best_cell_tiebreak_excludes_replicate():
    order = ["C:sys:json:none", "C:sys:json:apply", "C:user:json:none", "C_decl"]
    rec = {"C:sys:json:none": 0.9, "C:sys:json:apply": 0.2, "C:user:json:none": 0.4, "C_decl": 0.4}
    succ = {"C:sys:json:none": 1.0, "C:sys:json:apply": 0.5, "C:user:json:none": 0.6, "C_decl": 0.6}
    assert st.select_best_cell(rec, succ, order) == "C:user:json:none"  # tie on both -> earlier
    assert st.select_best_cell(rec, {**succ, "C_decl": 0.7}, order) == "C_decl"
    assert st.select_best_cell({**rec, "C_decl": None, "C:user:json:none": None}, succ, order) == "C:sys:json:apply"


def test_unlocks_needs_all_four():
    ok = dict(recovery_point=0.6, ci_low=0.05, survives_bh=True, mean=0.3, floor=0.1)
    assert st.unlocks(**ok)
    for field, bad in (("recovery_point", 0.49), ("ci_low", 0.0), ("survives_bh", False), ("mean", 0.05)):
        assert not st.unlocks(**{**ok, field: bad}), field
    assert not st.unlocks(**{**ok, "recovery_point": None})


def luna_stats(main=None, sys_unlock=False, thinking=None):
    cell_ok = {"recovery": 0.1, "ci_low": -0.05, "bh": False, "mean": 0.02}
    cells = {c: dict(cell_ok) for c in harness.ABLATION_CELLS + ["C_decl"]}
    if sys_unlock:
        cells["C:sys:prose:apply"] = {"recovery": 0.7, "ci_low": 0.1, "bh": True, "mean": 0.4}
    return {"cells": cells, "floor": 0.1,
            "main": main or {"user-sys": 0.3, "tool-sys": 0.1, "prose-json": 0.05, "apply-none": 0.0},
            "thinking": thinking}


def ci(lo, hi, mean=None):
    return {"mean": (lo + hi) / 2 if mean is None else mean, "ci95": [lo, hi]}


def full_stats(**luna_kw):
    fam = {"Dprime-D_required": ci(0.3, 0.5, 0.4), "Dprime-C": ci(-0.08, 0.09), "CD-C": ci(-0.05, 0.1),
           "CD-D": ci(0.0, 0.2)}
    return {"luna": luna_stats(**luna_kw), "qwen": {"p3": ci(0.02, 0.2)},
            "families": {f: dict(fam) for f in st.FAMILIES}, "route": None}


def test_verdicts_cover_p1_to_p9():
    v = st.verdicts(full_stats(thinking={"C:sys:json:none": {"recovery": 0.2}, "C:user:json:none": {"recovery": 0.4}}))
    assert set(v) == {f"P{i}" for i in range(1, 10)}
    assert all(set(x) == {"holds", "basis"} for x in v.values())
    assert v["P1"]["holds"] and v["P2"]["holds"] and v["P3"]["holds"] and v["P4"]["holds"]
    assert v["P5"]["holds"] and v["P6"]["holds"] and v["P7"]["holds"]
    assert v["P8"]["holds"] is None and v["P9"]["holds"] is None  # route arm not run
    assert st.verdicts(full_stats(sys_unlock=True))["P1"]["holds"] is False
    assert st.verdicts(full_stats())["P4"]["holds"] is None  # thinking arm not run
    hot = {"C:sys:json:none": {"recovery": 0.2}, "C_decl": {"recovery": 0.55}}
    assert st.verdicts(full_stats(thinking=hot))["P4"]["holds"] is False


def test_verdict_P6_equivalence():
    s = full_stats()
    assert st.verdicts(s)["P6"]["holds"] is True
    s["families"]["gemini-3.1-pro-preview"] = {**s["families"]["gemini-3.1-pro-preview"], "Dprime-C": ci(-0.12, 0.0)}
    assert st.verdicts(s)["P6"]["holds"] is False
    del s["families"]["gemini-3.1-pro-preview"]
    assert st.verdicts(s)["P6"]["holds"] is None  # Pro not run


def test_verdict_P2_within_noise_fails():
    small = {"user-sys": 0.08, "tool-sys": 0.02, "prose-json": 0.01, "apply-none": 0.0}
    assert st.verdicts(full_stats(main=small))["P2"]["holds"] is False
    fmt_wins = {"user-sys": 0.2, "tool-sys": 0.1, "prose-json": 0.25, "apply-none": 0.0}
    assert st.verdicts(full_stats(main=fmt_wins))["P2"]["holds"] is False


def test_verdicts_P3_P5_P7():
    s = full_stats()
    s["qwen"]["p3"] = ci(-0.01, 0.2)
    assert st.verdicts(s)["P3"]["holds"] is False
    s = full_stats()
    s["families"]["openai/gpt-5.6-luna"] = {**s["families"]["openai/gpt-5.6-luna"],
                                            "Dprime-D_required": ci(0.1, 0.4, 0.29)}
    assert st.verdicts(s)["P5"]["holds"] is False
    s = full_stats()
    s["families"]["modal-qwen2.5-7b"] = {**s["families"]["modal-qwen2.5-7b"], "CD-D": ci(-0.3, -0.01)}
    assert st.verdicts(s)["P7"]["holds"] is False
    s = full_stats()
    del s["families"]["gemini-3.1-pro-preview"]
    assert st.verdicts(s)["P5"]["holds"] is None and st.verdicts(s)["P7"]["holds"] is None
    s["families"]["modal-qwen2.5-7b"] = {**s["families"]["modal-qwen2.5-7b"], "CD-C": ci(-0.3, -0.01)}
    assert st.verdicts(s)["P7"]["holds"] is False  # one failing family decides even with one missing


def test_verdicts_P8_P9_when_route_arm_ran():
    s = full_stats()
    s["route"] = {"C": {"recovery": 0.6, "ci_low": 0.1, "bh": True, "mean": 0.3},
                  "fill_rate_A": 0.5, "bstrict_change": {"mean": -0.25}}
    v = st.verdicts(s)
    assert v["P8"]["holds"] is True and v["P9"]["holds"] is True
    s["route"] = {**s["route"], "fill_rate_A": 0.95}
    assert st.verdicts(s)["P9"]["holds"] is False


def test_review_edge_cases():
    # P8 uses luna's noise floor: a route C gain below it does not unlock
    s = full_stats()
    s["route"] = {"C": {"recovery": 0.6, "ci_low": 0.01, "bh": True, "mean": 0.05},
                  "fill_rate_A": 0.5, "bstrict_change": {"mean": -0.25}}
    assert st.verdicts(s)["P8"]["holds"] is False
    # best cell never comes from outside the 12 candidates
    order = list(harness.PHASE1_CONDS)
    rec = {c: 0.1 for c in order}
    rec.update({"CD": 0.9, "Dprime": 0.9, "C:sys:json:none": 0.9, "C:tool:prose:apply": 0.3})
    assert st.select_best_cell(rec, {}, order) == "C:tool:prose:apply"
    # P4 is refuted by one cell >= 0.5 even if another is undefined
    th = {"C:sys:json:none": {"recovery": None}, "C_decl": {"recovery": 0.9}}
    assert st.verdicts(full_stats(thinking=th))["P4"]["holds"] is False
    th = {"C:sys:json:none": {"recovery": None}, "C_decl": {"recovery": 0.1}}
    assert st.verdicts(full_stats(thinking=th))["P4"]["holds"] is None
    # flip rate counts only complete pairs; P1 needs every system-prompt cell
    assert st.flip_rate({("a", "x"): [1, 0], ("b", "x"): [1] * 5}) == 0.0
    assert st.flip_rate({("a", "x"): [1, 0]}) is None
    s = full_stats()
    del s["luna"]["cells"]["C:sys:prose:none"]
    assert st.verdicts(s)["P1"]["holds"] is None
