#!/usr/bin/env python3
"""Tests for the Phase-3 corpus verdicts.

Run: python3 -m pytest test_phase3_stats.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import phase3_stats as v  # noqa: E402


def share(point, low, high, n=100):
    return {"point": point, "ci95": [low, high], "n": n}


def test_a_ci_wholly_above_the_threshold_holds():
    assert v.verdict(share(0.8, 0.72, 0.88), 0.70, "x")["holds"] is True


def test_a_ci_wholly_below_the_threshold_fails():
    assert v.verdict(share(0.5, 0.42, 0.58), 0.70, "x")["holds"] is False


def test_a_straddling_ci_is_undecided():
    assert v.verdict(share(0.72, 0.60, 0.84), 0.70, "x")["holds"] is None


def test_a_ci_touching_the_threshold_from_below_still_holds():
    assert v.verdict(share(0.75, 0.70, 0.9), 0.70, "x")["holds"] is True


def test_an_empty_corpus_cannot_decide():
    assert v.verdict(share(0.0, 0.0, 0.0, n=0), 0.70, "x")["holds"] is None
    assert v.verdict(None, 0.70, "x")["holds"] is None
    assert v.verdict({"point": 0.5, "ci95": None, "n": 10}, 0.70, "x")["holds"] is None


def test_the_basis_quotes_the_numbers_a_reader_needs():
    basis = v.verdict(share(0.8, 0.72, 0.88, n=57), 0.70, "share of units")["basis"]
    assert "0.800" in basis and "0.720" in basis and "n=57" in basis and "0.7" in basis


def test_verdicts_cover_p17_to_p20():
    shares = {"coverage": share(0.9, 0.8, 0.95), "costly": share(0.3, 0.25, 0.4),
              "reach": share(0.6, 0.55, 0.7), "compound": share(0.2, 0.15, 0.3)}
    out = v.verdicts(shares)
    assert list(out) == ["P17", "P18", "P19", "P20"]
    assert [out[k]["holds"] for k in out] == [True, True, True, True]
    assert all(isinstance(o["basis"], str) and o["basis"] for o in out.values())


def test_verdicts_are_pending_when_a_share_is_missing():
    out = v.verdicts({})
    assert all(o["holds"] is None for o in out.values())


def test_the_locked_thresholds_and_label_groups():
    assert (v.P17_MIN, v.P18_MIN, v.P19_MIN, v.P20_MIN) == (0.70, 0.20, 0.50, 0.10)
    assert v.FIVE == ("rename", "enum_tighten", "required", "type_change", "default_change")
    assert v.COVERED == v.FIVE + ("compound",)
    assert v.COSTLY == ("required", "default_change")
