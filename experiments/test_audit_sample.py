#!/usr/bin/env python3
"""Hand-audit sample (Task 13): stratified draw, blind reading copy, answer parsing, agreement.
Fake models only; no API calls.

Run: python3 -m pytest test_audit_sample.py -q
"""

import json
import pathlib
import sys
from collections import Counter

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze  # noqa: E402  (load_runs only)
import analyze_phase1 as ap1  # noqa: E402
import audit_sample as au  # noqa: E402
import drift_labels  # noqa: E402
from test_analyze_phase1 import fake_records  # noqa: E402


@pytest.fixture(scope="module")
def sept():
    return ap1.sept_index(analyze.load_runs())


@pytest.fixture(scope="module")
def p1runs():
    return (fake_records(ap1.LUNA, "ablation", "default") + fake_records(ap1.QWEN, "infoform", "default")
            + fake_records(ap1.LUNA, "noise", "default"))


def strata(items):
    return Counter((it["key"]["model"], it["auto_label"]) for it in items)


def test_draw_is_deterministic(p1runs, sept):
    assert au.draw(p1runs, sept) == au.draw(p1runs, sept)
    assert au.draw(p1runs, sept, seed=1) != au.draw(p1runs, sept)


def test_floor_per_stratum_then_fill(p1runs, sept):
    pop = Counter((r["model"], au.auto_label(r, sept)) for r in ap1._main_records(p1runs))
    floor = sum(min(au.MIN_PER_STRATUM, n) for n in pop.values())
    small = au.draw(p1runs, sept, n=1)
    assert len(small) == floor  # the floor wins over n
    assert all(strata(small)[s] >= min(au.MIN_PER_STRATUM, n) for s, n in pop.items())
    big = au.draw(p1runs, sept, n=floor + 10)
    assert len(big) == floor + 10 and all(strata(big)[s] >= min(2, n) for s, n in pop.items())


def test_only_main_records_and_unique(p1runs, sept):
    items = au.draw(p1runs, sept, n=60)
    keys = [json.dumps(it["key"], sort_keys=True) for it in items]
    assert len(set(keys)) == len(keys)
    assert all(it["key"]["rep"] == 0 for it in items)  # noise reps 1-4 are not in the population
    assert [it["id"] for it in items] == list(range(1, len(items) + 1))


def test_item_contents(p1runs, sept):
    it = au.draw(p1runs, sept)[0]
    assert it["human_label"] is None and it["note"] == ""
    assert it["auto_label"] in drift_labels.LABELS
    assert set(it["expected"]) == {"v1", "v2"} and it["request"] and it["change"]
    assert it["transcript"] is not None and "drift_outcome" in it


def test_reading_copy_is_blind(p1runs, sept):
    items = au.draw(p1runs, sept, n=40)
    md = au.render_md(items)
    sections = md.split("\n## Item ")[1:]
    assert len(sections) == len(items)
    for sec in sections:
        assert not any(label in sec for label in drift_labels.LABELS)
        assert "\nhuman_label:" in sec and "\nnote:" in sec


def fill(md, answers):
    """Write `answers` {id: (label, note)} into the reading copy."""
    out, current = [], None
    for line in md.splitlines():
        if line.startswith("## Item "):
            current = int(line.split()[2])
        if current in answers and line.startswith("human_label:"):
            line = f"human_label: {answers[current][0]}"
        if current in answers and line.startswith("note:"):
            line = f"note: {answers[current][1]}"
        out.append(line)
    return "\n".join(out)


def test_parse_answers(p1runs, sept):
    items = au.draw(p1runs, sept)
    md = fill(au.render_md(items), {1: ("V1_FORM", "old name kept"), 2: ("v2_correct", "")})
    got = au.parse_answers(md)
    assert got[1] == ("V1_FORM", "old name kept") and got[2] == ("V2_CORRECT", "")
    assert got[3] == (None, "")
    with pytest.raises(SystemExit, match="item 1"):
        au.parse_answers(fill(md, {1: ("WRONGISH", "")}))


def test_apply_answers_is_a_new_copy(p1runs, sept):
    items = au.draw(p1runs, sept)
    filled = au.apply_answers(items, {1: ("V1_FORM", "x")})
    assert items[0]["human_label"] is None
    assert filled[0]["human_label"] == "V1_FORM" and filled[0]["note"] == "x"
    with pytest.raises(SystemExit, match="999"):
        au.apply_answers(items, {999: ("V1_FORM", "")})


def test_agreement_uses_the_current_labeler(p1runs, sept):
    items = au.draw(p1runs, sept)
    assert ap1.audit_agreement(p1runs, sept, {"items": items})["complete"] is False
    agreeing = [{**it, "human_label": it["auto_label"]} for it in items]
    a = ap1.audit_agreement(p1runs, sept, {"items": agreeing})
    assert a == {**a, "n_items": len(items), "n_labelled": len(items), "n_agree": len(items),
                 "rate": 1.0, "complete": True, "passes": True, "disagreements": []}
    other = next(lab for lab in drift_labels.LABELS if lab != items[0]["auto_label"])
    one_off = [{**agreeing[0], "human_label": other}] + agreeing[1:]
    a = ap1.audit_agreement(p1runs, sept, {"items": one_off})
    assert a["n_agree"] == len(items) - 1
    assert a["disagreements"] == [{"id": 1, "auto": items[0]["auto_label"], "human": other}]
    stale = [{**agreeing[0], "auto_label": other}] + agreeing[1:]  # file label is ignored
    assert ap1.audit_agreement(p1runs, sept, {"items": stale})["n_agree"] == len(items)


def test_agreement_missing_record_fails(p1runs, sept):
    items = au.draw(p1runs, sept)
    gone = {json.dumps(items[0]["key"], sort_keys=True)}
    rest = [r for r in p1runs if json.dumps(au.item_key(r), sort_keys=True) not in gone]
    with pytest.raises(SystemExit, match="item 1"):
        ap1.audit_agreement(rest, sept, {"items": items})


def test_write_refuses_to_overwrite(tmp_path, p1runs, sept):
    items = au.draw(p1runs, sept)
    au.write_sample(tmp_path, items, p1runs, sept)
    sample = json.loads((tmp_path / au.SAMPLE_FILE).read_text())
    assert sample["seed"] == au.SEED and len(sample["items"]) == len(items)
    assert sum(sample["population"].values()) == len(ap1._main_records(p1runs))
    assert (tmp_path / au.READING_FILE).read_text() == au.render_md(items)
    with pytest.raises(SystemExit, match="exists"):
        au.write_sample(tmp_path, items, p1runs, sept)


def test_score_round_trip(tmp_path, p1runs, sept):
    items = au.draw(p1runs, sept)
    au.write_sample(tmp_path, items, p1runs, sept)
    md = tmp_path / au.READING_FILE
    md.write_text(fill(md.read_text(), {it["id"]: (it["auto_label"], "") for it in items}))
    a = au.score(tmp_path, p1runs, sept)
    assert a["complete"] and a["rate"] == 1.0
    sample = json.loads((tmp_path / au.SAMPLE_FILE).read_text())
    assert all(it["human_label"] == it["auto_label"] for it in sample["items"])


def test_analysis_reads_the_audit_file(tmp_path, p1runs, sept):
    assert ap1.audit(p1runs, sept, tmp_path) is None
    au.write_sample(tmp_path, au.draw(p1runs, sept), p1runs, sept)
    assert ap1.audit(p1runs, sept, tmp_path)["n_labelled"] == 0


# ---------------- Phase 2 (MILESTONES.md "Phase 2 pre-registration", label audit) ----------------

import analyze_phase2 as ap2  # noqa: E402
import phase2_stats as v  # noqa: E402
from test_analyze_phase2 import fake as fake_p2  # noqa: E402


@pytest.fixture(scope="module")
def p2runs():
    return (fake_p2(v.SONNET, "core") + fake_p2(v.SONNET, "phrasing") + fake_p2(v.SONNET, "noise")
            + fake_p2(v.SONNET, "placement") + fake_p2(v.FLASH, "fill", "MINIMAL"))


@pytest.fixture(scope="module")
def p2index(p2runs):
    return ap2.b_index(p2runs)


def test_phase2_population_is_the_mechanism_records(p2runs, p2index):
    pop = au.population(p2runs, p2index, phase=2)
    recs = [r for r, _ in pop]
    assert all(r["rep"] == 0 and r["phrasing"] == 0 and r["cond"] not in ("A", "A_fill") for r in recs)
    assert {r["model"] for r in recs} == {v.SONNET, v.FLASH}
    mech = ap2.mechanism(p2runs)
    assert len(pop) == sum(n for m in mech.values() for c in m.values() for cls in c.values() for n in cls.values())
    assert Counter(lab for _, lab in pop) == Counter(
        lab for m in mech.values() for c in m.values() for cls in c.values() for lab, n in cls.items() for _ in range(n))


def test_phase2_draw_uses_its_seed_and_floor(p2runs, p2index):
    items = au.draw(p2runs, p2index, phase=2)
    assert items == au.draw(p2runs, p2index, seed=au.SEED_P2, phase=2)
    pop = Counter((r["model"], lab) for r, lab in au.population(p2runs, p2index, phase=2))
    assert all(strata(items)[s] >= min(au.MIN_PER_STRATUM, n) for s, n in pop.items())


def test_phase2_reading_copy_is_blind_and_names_this_runs_b_strict(p2runs, p2index):
    items = au.draw(p2runs, p2index, n=60, phase=2)
    md = au.render_md(items)
    assert "(September B_strict)" not in md and "(B_strict in this run)" in md
    assert all(it["shown"] != it["key"]["cond"] for it in items)  # every condition is described
    for sec in md.split("\n## Item ")[1:]:
        assert not any(label in sec for label in drift_labels.LABELS)


def test_phase2_score_round_trip_and_analysis(tmp_path, p2runs, p2index):
    items = au.draw(p2runs, p2index, phase=2)
    assert ap2.audit(p2runs, tmp_path) is None
    au.write_sample(tmp_path, items, p2runs, p2index, phase=2)
    sample = json.loads((tmp_path / au.SAMPLE_FILE).read_text())
    assert sample["seed"] == au.SEED_P2 and sum(sample["population"].values()) == len(ap2.main_records(p2runs))
    assert ap2.audit(p2runs, tmp_path)["n_labelled"] == 0
    md = tmp_path / au.READING_FILE
    md.write_text(fill(md.read_text(), {it["id"]: (it["auto_label"], "") for it in items}))
    a = au.score(tmp_path, p2runs, p2index, phase=2)
    assert a["complete"] and a["rate"] == 1.0 and ap2.audit(p2runs, tmp_path)["rate"] == 1.0
