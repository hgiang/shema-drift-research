#!/usr/bin/env python3
"""Tests for the explorer data bundle. The bundle must agree with
analysis.json, reconstruct prompts exactly as the harness built them, and
replay every logged accepted call to the outcome that was logged."""

import collections
import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_explorer_data as bed  # noqa: E402
import episode_semantics as sem  # noqa: E402

sys.path.insert(0, str(bed.EXPERIMENTS))
import harness  # noqa: E402


@pytest.fixture(scope="module")
def payload():
    return bed.build_payload()


def core(episodes, model):
    return [e for e in episodes if e["model"] == model and e["battery"] == "core"]


def test_episode_count_matches_analysis(payload):
    assert len(payload["episodes"]) == payload["analysis"]["n_records"] == 4800


def test_battery_tags(payload):
    counts = collections.Counter((e["model"], e["battery"]) for e in payload["episodes"])
    assert counts[("gemini-3.6-flash", "core")] == 1320
    assert counts[("gemini-3.6-flash", "noise")] == 120   # reps 1-4 x 30 pairs
    assert counts[("gemini-3.6-flash", "phrasing")] == 240
    assert counts[("openai/gpt-5.6-luna", "core")] == 720
    assert ("openai/gpt-5.6-luna", "noise") not in counts


def test_core_success_rates_match_analysis(payload):
    for model, block in payload["analysis"]["models"].items():
        eps = core(payload["episodes"], model)
        for cond, rate in block["success_rate"].items():
            sel = [e["success"] for e in eps if e["cond"] == cond]
            assert sum(sel) / len(sel) == pytest.approx(rate), (model, cond)


def test_every_episode_has_a_view(payload):
    for e in payload["episodes"]:
        assert bed.view_key(e["task"], e["class"], e["cond"]) in payload["views"]


def test_views_reconstruct_harness_prompt_exactly(payload):
    tasks = {t["id"]: t for t in payload["testbed"]["tasks"]}
    for key, view in payload["views"].items():
        task_id, cls, cond = key.split("|")
        setup = harness.build_condition(tasks[task_id], cond, cls)
        assert payload["prompts"]["system"][view["system"]] == setup["system"]
        assert [payload["prompts"]["decls"][i] for i in view["decls"]] == setup["declarations"]
        assert view["profile"] == setup["profile"]
        assert view["retry"] == setup["retry"]


def test_replayed_outcomes_match_logged(payload):
    checked = 0
    for e in payload["episodes"]:
        for step in e["executed"]:
            if step["outcome"] is None:
                assert step["check"] is None
                continue
            assert step["check"]["outcome"] == step["outcome"], (e["model"], e["task"], e["cond"])
            checked += 1
    assert checked > 3000


def test_lenient_rename_shows_dropped_old_name(payload):
    ep = next(e for e in payload["episodes"]
              if e["cond"] == "B_lenient" and e["class"] == "rename"
              and e["executed"] and e["executed"][0]["outcome"] == "ACCEPTED_WRONG")
    fields = ep["executed"][0]["check"]["fields"]
    assert any(f["status"] == "dropped" for f in fields)
    assert any(f["status"] == "wrong" for f in fields)


def test_field_status_vocabulary():
    params = {"a": {"type": "string", "default": "x"},
              "b": {"type": "integer", "default": 0}}
    check = sem.compare_call({"a": "y", "zz": 1}, {"a": "y", "b": 5}, params, "lenient")
    status = {f["param"]: f["status"] for f in check["fields"]}
    assert status == {"a": "ok", "b": "wrong", "zz": "dropped"}
    assert check["outcome"] == "ACCEPTED_WRONG"


def test_task_domain_comes_from_drift_tool(payload):
    tools = payload["testbed"]["tools"]
    for t in payload["testbed"]["tasks"]:
        assert t["domain"] == tools[t["drift_tool"]]["domain"]


def test_labels_cover_every_model_cond_class(payload):
    labels = payload["labels"]
    assert set(payload["analysis"]["models"]) <= set(labels["models"])
    assert {e["cond"] for e in payload["episodes"]} <= set(labels["conds"])
    assert set(payload["testbed"]["classes"]) == set(labels["classes"])


def test_outcome_labels_use_js_null_key(payload):
    # the browser looks labels up with String(null) === "null"
    outcomes = payload["labels"]["outcomes"]
    assert "null" in outcomes and "None" not in outcomes
    assert all(c["short"] for c in payload["labels"]["conds"].values())


def test_payload_is_deterministic():
    a = json.dumps(bed.build_payload(), sort_keys=True)
    b = json.dumps(bed.build_payload(), sort_keys=True)
    assert a == b


def test_follow_fields_match_phase1_report(payload):
    """Explorer labels must agree with phase1/step1_diag_diff_following.json."""
    import step1_diag_diff_following as follow
    report = json.loads(follow.OUT.read_text())
    for model, rep in report.items():
        eps = [e for e in core(payload["episodes"], model) if e["cond"] == "C"]
        for cls, counts in rep["C_drift_call_labels"].items():
            got = collections.Counter(e["follow"] for e in eps if e["class"] == cls)
            assert dict(got) == counts, (model, cls)
            same = sum(e["same_as_B"] == "1" for e in eps if e["class"] == cls)
            assert same == rep["identity"]["C_vs_B_strict"][cls]["identical"], (model, cls)


def test_follow_fields_vocabulary(payload):
    labels = payload["labels"]
    for e in payload["episodes"]:
        assert e["follow"] in labels["follow"]
        assert e["same_as_B"] in labels["same_as_B"]
        if e["cond"] in ("A", "B_strict"):
            assert e["same_as_B"] == "n/a"
        if e["cond"] == "A":
            assert e["follow"] == "n/a"


def test_lenient_rename_old_name_is_v1_form(payload):
    eps = [e for e in payload["episodes"] if e["cond"] == "B_lenient" and e["class"] == "rename"
           and e["drift_outcome"] == "ACCEPTED_WRONG"]
    assert eps and all(e["follow"] in ("V1_FORM", "OTHER_WRONG") for e in eps)


def test_write_bundle_round_trips(tmp_path, payload):
    out = tmp_path / "data.js"
    bed.write_bundle(payload, out)
    text = out.read_text()
    assert text.startswith(bed.BUNDLE_PREFIX)
    parsed = json.loads(text[len(bed.BUNDLE_PREFIX):].rstrip().rstrip(";"))
    assert parsed["meta"]["n_records"] == 4800
