#!/usr/bin/env python3
"""Tests for Phase-3 inter-coder reliability.

Run: python3 -m pytest phase3/test_agreement.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import agreement as ag  # noqa: E402


def unit(digest, parameter, label, visible=True):
    return {"digest_id": digest, "parameter": parameter, "label": label, "agent_visible": visible}


A = [unit("s:0", "a", "rename"), unit("s:1", "b", "required"), unit("s:2", "c", "other")]
B = [unit("s:0", "a", "rename"), unit("s:1", "b", "required"), unit("s:3", "d", "other")]


def test_unit_set_agreement_is_both_over_either():
    out = ag.unit_sets(A, B)
    assert out["n_both"] == 2 and out["n_only_a"] == 1 and out["n_only_b"] == 1
    assert out["jaccard"] == 0.5
    assert out["agreed"] == [("s:0", "a"), ("s:1", "b")]


def test_label_agreement_is_computed_on_the_agreed_set_only():
    out = ag.label_agreement(A, B)
    assert out["n"] == 2 and out["n_agree"] == 2 and out["rate"] == 1.0
    assert out["disagreements"] == []


def test_a_label_disagreement_is_listed_not_hidden():
    b = [unit("s:0", "a", "type_change"), unit("s:1", "b", "required")]
    out = ag.label_agreement(A, b)
    assert out["n"] == 2 and out["n_agree"] == 1 and out["rate"] == 0.5
    assert out["disagreements"] == [{"digest_id": "s:0", "parameter": "a",
                                     "a": "rename", "b": "type_change"}]


def test_kappa_is_zero_when_agreement_is_only_what_chance_gives():
    # marginals 5/10 and 2/10 give chance agreement 0.5; five hits out of ten is exactly that
    a = [unit(f"s:{i}", "p", "rename" if i < 5 else "other") for i in range(10)]
    b = [unit(f"s:{i}", "p", "rename" if i in (0, 9) else "other") for i in range(10)]
    out = ag.label_agreement(a, b)
    assert out["rate"] == 0.5 and out["kappa"] == 0.0


def test_kappa_is_one_on_perfect_agreement_with_two_labels_used():
    a = [unit(f"s:{i}", "p", "rename" if i < 5 else "other") for i in range(10)]
    out = ag.label_agreement(a, list(a))
    assert out["kappa"] == 1.0 and out["rate"] == 1.0


def test_kappa_is_none_when_one_label_is_used_everywhere():
    a = [unit(f"s:{i}", "p", "other") for i in range(6)]
    assert ag.label_agreement(a, list(a))["kappa"] is None   # chance agreement is 1: undefined


def test_agent_visible_agreement_counts_none_as_its_own_value():
    a = [unit("s:0", "a", "rename", True), unit("s:1", "b", "required", None)]
    b = [unit("s:0", "a", "rename", True), unit("s:1", "b", "required", False)]
    out = ag.visible_agreement(a, b)
    assert out["n"] == 2 and out["n_agree"] == 1 and out["rate"] == 0.5


def test_report_bundles_every_figure_and_the_threshold_verdict():
    out = ag.report(A, B)
    assert set(out) == {"unit_sets", "label", "agent_visible", "threshold", "passes"}
    assert out["threshold"] == ag.THRESHOLD
    assert out["passes"] is True


def test_report_fails_below_the_threshold():
    b = [unit("s:0", "a", "type_change"), unit("s:1", "b", "other"), unit("s:3", "d", "other")]
    out = ag.report(A, b)
    assert out["label"]["rate"] == 0.0 and out["passes"] is False


def test_an_empty_agreed_set_is_pending_not_passing():
    out = ag.report(A, [unit("z:9", "q", "other")])
    assert out["label"]["n"] == 0 and out["passes"] is None


def test_units_are_matched_on_the_parameters_last_segment():
    a = [unit("s:0", "Plan#create.aggregate_usage", "rename"),
         unit("s:0", "Price#create.recurring.aggregate_usage", "rename")]
    b = [unit("s:0", "aggregate_usage", "rename")]
    out = ag.unit_sets(a, b)
    assert out["n_a"] == 1 and out["n_b"] == 1 and out["n_both"] == 1
    assert out["only_a"] == [] and out["only_b"] == []


def test_matching_is_case_insensitive_on_the_segment():
    a = [unit("s:0", "Body.Limit", "required")]
    b = [unit("s:0", "limit", "required")]
    assert ag.unit_sets(a, b)["n_both"] == 1


def test_merging_within_a_coder_keeps_the_first_unit_seen():
    a = [unit("s:0", "a.x", "rename"), unit("s:0", "b.x", "other")]
    out = ag.label_agreement(a, [unit("s:0", "x", "rename")])
    assert out["n"] == 1 and out["n_agree"] == 1


def test_different_parameters_in_one_digest_stay_separate():
    a = [unit("s:0", "limit", "required"), unit("s:0", "offset", "required")]
    assert ag.unit_sets(a, list(a))["n_both"] == 2
