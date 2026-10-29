#!/usr/bin/env python3
"""Tests for the Phase-2 verdicts P10-P16 (MILESTONES.md "Phase 2 pre-registration").

Run: python3 -m pytest test_phase2_stats.py -q
"""

import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import phase2_stats as v  # noqa: E402


def claude(rec=0.8, ci_low=0.2, bh=True, mean=0.5, floor=0.1):
    return {"recovery": rec, "ci_low": ci_low, "bh": bh, "mean": mean, "floor": floor}


def test_p10_needs_both_claude_models_to_unlock():
    assert v.p10({v.HAIKU: claude(), v.SONNET: claude()})["holds"] is True
    for bad in (claude(rec=0.4), claude(ci_low=-0.01), claude(bh=False), claude(mean=0.05)):
        assert v.p10({v.HAIKU: claude(), v.SONNET: bad})["holds"] is False
    assert v.p10({v.HAIKU: claude(rec=None), v.SONNET: claude()})["holds"] is None  # no drop: pending
    assert v.p10({v.HAIKU: claude(rec=None), v.SONNET: claude(bh=False)})["holds"] is False
    assert v.p10({v.HAIKU: claude()})["holds"] is None  # Sonnet pending
    assert v.p10({v.HAIKU: claude(), v.SONNET: claude(floor=None)})["holds"] is None  # noise arm pending
    assert v.p10({v.HAIKU: claude(rec=0.1), v.SONNET: claude(floor=None)})["holds"] is False


def llama(c_rec=0.2, gain=0.4, bh=True, mean=0.3, floor=0.1):
    return {"c_recovery": c_rec, "gain": gain, "bh": bh, "mean": mean, "floor": floor}


def test_p11_placement_gain_for_llama():
    assert v.p11(llama())["holds"] is True
    for bad in (llama(c_rec=0.6), llama(gain=0.2), llama(bh=False), llama(mean=0.05)):
        assert v.p11(bad)["holds"] is False
    assert v.p11(llama(c_rec=None, gain=None))["holds"] is None  # A - B_strict <= 0: recovery undefined
    assert v.p11(llama(floor=None))["holds"] is None
    assert v.p11(None)["holds"] is None


def fams(key, **by_family):
    return {f: {key: stat} for f, stat in by_family.items()}


def test_p12_dprime_gain_on_required_in_every_new_family():
    ok = {f: {"Dprime-D_required": {"mean": 0.4}} for f in v.NEW_FAMILIES}
    assert v.p12({"families": ok})["holds"] is True
    low = {**ok, v.LLAMA: {"Dprime-D_required": {"mean": 0.29}}}
    assert v.p12({"families": low})["holds"] is False
    assert v.p12({"families": {v.SONNET: ok[v.SONNET]}})["holds"] is None


def test_p13_cd_never_wholly_below_c_or_d():
    ok = {f: {"CD-C": {"ci95": [-0.1, 0.1]}, "CD-D": {"ci95": [-0.2, 0.0]}} for f in v.NEW_FAMILIES}
    assert v.p13({"families": ok})["holds"] is True
    below = {**ok, v.HAIKU: {"CD-C": {"ci95": [-0.3, -0.01]}, "CD-D": {"ci95": [0.0, 0.1]}}}
    assert v.p13({"families": below})["holds"] is False
    assert v.p13({"families": {v.HAIKU: ok[v.HAIKU]}})["holds"] is None


def fill(mean=0.35, ci=(0.2, 0.5), bh=True, contrast=(-0.05, 0.08), floor=0.133):
    return {"info": {"mean": mean, "ci95": list(ci), "bh": bh}, "contrast": {"ci95": list(contrast)},
            "floor": floor}


def test_p14_fill_instruction_on_flash():
    assert v.p14(fill())["holds"] is True
    for bad in (fill(mean=0.25), fill(ci=(-0.01, 0.6)), fill(bh=False), fill(contrast=(-0.12, 0.05)),
                fill(contrast=(-0.05, 0.11)), fill(floor=0.4)):
        assert v.p14(bad)["holds"] is False
    assert v.p14(None)["holds"] is None


def test_p15_untested_without_the_direct_arm():
    out = v.p15({"run": False, "basis": "no luna direct route lifts"})
    assert out == {"holds": None, "basis": "direct arm not run: no luna direct route lifts"}
    with pytest.raises(ValueError, match="not implemented"):
        v.p15({"run": True})


def replay(pyd=0.96, fast=0.97, js=0.99):
    return {"pydantic_default": {"vs_lenient": pyd}, "fastapi_default": {"vs_lenient": fast},
            "jsonschema_closed": {"vs_strict": js}}


def test_p16_validator_agreement():
    assert v.p16(replay())["holds"] is True
    assert v.p16(replay(pyd=0.877))["holds"] is False
    assert v.p16(replay(js=0.94))["holds"] is False
    assert v.p16(None)["holds"] is None


def test_verdicts_cover_p10_to_p16():
    stats = {"claude": {v.HAIKU: claude(), v.SONNET: claude()}, "llama": llama(),
             "families": {f: {"Dprime-D_required": {"mean": 0.4}, "CD-C": {"ci95": [0.0, 0.1]},
                              "CD-D": {"ci95": [0.0, 0.1]}} for f in v.NEW_FAMILIES},
             "fill": fill(), "direct": {"run": False, "basis": "x"}, "replay": replay()}
    out = v.verdicts(stats)
    assert list(out) == [f"P{i}" for i in range(10, 17)]
    assert [out[k]["holds"] for k in out] == [True, True, True, True, True, None, True]
    assert all(isinstance(o["basis"], str) for o in out.values())
