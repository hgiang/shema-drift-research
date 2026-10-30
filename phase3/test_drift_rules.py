#!/usr/bin/env python3
"""Tests for the Phase-3 coding rule (MILESTONES.md "Phase 3 pre-registration").

One case per label, plus the cases the lock calls out: an entry that yields two units, an
entry that qualifies under none of the five classes, and a `compound` change.

Run: python3 -m pytest phase3/test_drift_rules.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drift_rules as dr  # noqa: E402


def label_of(span, name=None):
    unit = dr.classify(span, name or (dr.et.identifiers(span) or [""])[0])
    return unit["label"]


def test_one_case_per_class():
    assert label_of("The `source` parameter has been renamed to `payment_source`.") == "rename"
    assert label_of("The `channel` parameter is now required.") == "required"
    assert label_of("The `status` parameter no longer accepts the `pending` value.") == "enum_tighten"
    assert label_of("The `amount` parameter is now a string instead of an integer.") == "type_change"
    assert label_of("The `limit` parameter now defaults to 20.") == "default_change"


def test_more_wordings_per_class():
    for span in ("We renamed `a` to `b`.", "`a` is now called `b`.", "`a` has been renamed."):
        assert label_of(span, "a") == "rename"
    for span in ("`a` is now a required parameter.", "The endpoint now requires `a`.",
                 "You must now pass `a`."):
        assert label_of(span, "a") == "required"
    for span in ("Removed the `old` value from `a`.", "`a` is restricted to two values.",
                 "`pending` is no longer a valid value for `a`."):
        assert label_of(span, "a") == "enum_tighten"
    for span in ("The type of `a` changed from integer to string.",
                 "`a` now accepts an array.", "`a` is now a boolean."):
        assert label_of(span, "a") == "type_change"
    for span in ("The default for `a` is now 10.", "`a` previously defaulted to false.",
                 "The default value of `a` changed."):
        assert label_of(span, "a") == "default_change"


def test_compound_is_two_classes_on_the_same_parameter():
    span = "The `source` parameter has been renamed to `origin` and is now required."
    unit = dr.classify(span, "source")
    assert unit["label"] == "compound"
    assert sorted(unit["classes"]) == ["rename", "required"]


def test_other_is_a_qualifying_change_that_is_none_of_the_five():
    assert label_of("The `legacy_id` parameter has been removed from the request.") == "other"
    assert label_of("The `note` parameter is now optional.") == "other"


def test_non_qualifying_spans_yield_nothing():
    for span in ("The response now includes a `balance` field.",
                 "We added a new `/v2/search` endpoint.",
                 "Improved the docs for `charges`.",
                 "Rate limits for the API have changed."):
        assert dr.qualifies(span) is False


def test_response_only_changes_are_excluded_even_with_a_change_verb():
    assert dr.qualifies("The `total` field in the response is now a string.") is False
    assert dr.qualifies("`total` is now a string in the response body.") is False


def test_new_parameters_are_excluded_but_constraints_on_existing_ones_are_not():
    assert dr.qualifies("Adds a new `tax_id` parameter.") is False
    assert dr.qualifies("Adds support for a new payment method.") is False
    assert dr.qualifies("The existing `tax_id` parameter is now required.") is True


def test_units_of_entry_yields_one_unit_per_parameter():
    text = ("The `source` parameter has been renamed to `origin`.\n"
            "The `limit` parameter now defaults to 20.\n"
            "Unrelated prose about billing.\n")
    units = dr.units_of_entry(text)
    assert [(u["parameter"], u["label"]) for u in units] == [("source", "rename"), ("limit", "default_change")]
    assert all(u["evidence"] and u["rule"] for u in units)


def test_units_are_deduped_per_parameter_and_merge_into_compound():
    text = "The `source` parameter was renamed.\nThe `source` parameter is now required.\n"
    units = dr.units_of_entry(text)
    assert len(units) == 1 and units[0]["label"] == "compound"
    assert units[0]["evidence"].count("`source`") == 2


def test_agent_visible_is_decided_without_the_label():
    required = dr.classify("The `channel` parameter is now required.", "channel")
    assert required["agent_visible"] is True
    example = dr.agent_visible("x", "`x` is now a string.", 'curl "https://a.test?x=1"')
    assert example is True
    assert dr.agent_visible("x", "`x` is now a string.", "no example here") is None


def test_rule_clause_names_the_pattern_that_decided_it():
    unit = dr.classify("The `limit` parameter now defaults to 20.", "limit")
    assert unit["rule"].startswith("default_change:") and "default" in unit["rule"]


def test_labels_are_exactly_the_locked_set():
    assert dr.LABELS == ("rename", "enum_tighten", "required", "type_change",
                         "default_change", "compound", "other")
