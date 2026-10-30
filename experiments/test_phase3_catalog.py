#!/usr/bin/env python3
"""The catalog manipulation (MILESTONES.md "Phase 3 amendment 4").

The large catalog must be a *view* of the frozen testbed: every declaration byte-identical
to what the small catalog would have served, with the drifted tool in a fixed position.

Run: python3 -m pytest test_phase3_catalog.py -q
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harness  # noqa: E402
import phase3_grid as p3  # noqa: E402

TASK = harness.frozen()["tasks"][0]
CLS = TASK["assigned"][0]


def test_the_small_catalog_is_exactly_what_the_study_has_always_served():
    plain = harness.build_condition(TASK, "C", CLS)
    small = harness.build_condition(TASK, "C", CLS, catalog="small")
    assert small == plain
    assert len(plain["declarations"]) <= 2


def test_the_large_catalog_declares_every_frozen_tool():
    large = harness.build_condition(TASK, "C", CLS, catalog="full")
    names = [d["name"] for d in large["declarations"]]
    assert len(names) == 30 == len(set(names))
    assert set(names) == set(harness.frozen()["tools_v1"])


def test_the_shared_declarations_are_byte_identical_between_catalogs():
    small = harness.build_condition(TASK, "C", CLS, catalog="small")
    large = harness.build_condition(TASK, "C", CLS, catalog="full")
    by_name = {d["name"]: d for d in large["declarations"]}
    for decl in small["declarations"]:
        assert by_name[decl["name"]] == decl


def test_the_catalog_order_is_fixed_and_not_the_task_order():
    first = [d["name"] for d in harness.build_condition(TASK, "A", CLS, catalog="full")["declarations"]]
    other = harness.frozen()["tasks"][7]
    second = [d["name"] for d in harness.build_condition(other, "A", other["assigned"][0],
                                                         catalog="full")["declarations"]]
    assert first == second == p3.CATALOG_ORDER
    assert first != sorted(first)          # drawn from RNG_P3, not alphabetical


def test_the_drifted_tool_still_drifts_in_the_large_catalog():
    large = harness.build_condition(TASK, "B_strict", CLS, catalog="full")
    plain = harness.build_condition(TASK, "B_strict", CLS)
    dt = TASK["drift_tool"]
    assert large["active"][dt] == plain["active"][dt]
    assert large["active"][dt] != harness.frozen()["tools_v1"][dt]["params"]


def test_only_the_drifted_tool_is_v2_among_all_thirty():
    large = harness.build_condition(TASK, "B_strict", CLS, catalog="full")
    v1 = harness.frozen()["tools_v1"]
    drifted = [n for n, p in large["active"].items() if p != v1[n]["params"]]
    assert drifted == [TASK["drift_tool"]]


def test_an_unknown_catalog_is_refused():
    try:
        harness.build_condition(TASK, "A", CLS, catalog="enormous")
    except ValueError as e:
        assert "enormous" in str(e)
    else:
        raise AssertionError("an unknown catalog should not be served")
