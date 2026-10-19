#!/usr/bin/env python3
"""Phase-1 wiring of analyze.py. analyze.py runs in a subprocess so its module-level RNG and
ALL_P start fresh, exactly as in a real run. Fake models only; no API calls.

Run: python3 -m pytest test_analyze_phase1.py -q
"""

import json
import pathlib
import shutil
import subprocess
import sys
import zlib

import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_phase1 as ap1  # noqa: E402
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
import phase1_stats as st  # noqa: E402
import select_thinking_cell  # noqa: E402
from test_phase1 import oracle  # noqa: E402

COMMITTED = json.loads((HERE.parent / "results" / "analysis.json").read_text())


def fake_records(model, arm, reasoning, cells=None):
    """Deterministic mix of v2 (succeeds) and v1 (fails under drift) behaviour per job."""
    out = []
    for job in p1.jobs(arm, cells):
        t, cond, cls, ph, rep = job
        seed = zlib.crc32(f"{model}|{t['id']}|{cond}|{cls}|{rep}|{reasoning}".encode())
        call = oracle("v2" if seed % 3 else "v1")(t, cls)
        out.append(p1.run_episode(job, call, model, arm, reasoning, 700))
    return out


def write(path, records):
    with path.open("a") as f:
        f.writelines(json.dumps(r) + "\n" for r in records)


@pytest.fixture(scope="module")
def phase1_dir(tmp_path_factory):
    d = tmp_path_factory.mktemp("phase1")
    for model in (ap1.LUNA, ap1.QWEN):
        write(d / f"runs_{model.replace('/', '_')}.jsonl",
              fake_records(model, "ablation", "default") + fake_records(model, "infoform", "default"))
    write(d / f"runs_{ap1.LUNA.replace('/', '_')}.jsonl", fake_records(ap1.LUNA, "noise", "default"))
    for model, level in ap1.THINKING.items():
        write(d / f"runs_{model}.jsonl", fake_records(model, "infoform", level))
    sel = select_thinking_cell.select(d)
    (d / ap1.SELECTION_FILE).write_text(json.dumps(sel))
    write(d / f"runs_{ap1.LUNA.replace('/', '_')}.jsonl",
          fake_records(ap1.LUNA, "thinking", "high", [st.REPLICATE_C, sel["selected"]]))
    return d


def run_analysis(tmp_path, phase1_dir):
    out = tmp_path / "analysis.json"
    res = subprocess.run([sys.executable, str(HERE / "analyze.py"), "--out", str(out),
                          "--phase1-dir", str(phase1_dir)], capture_output=True, text=True)
    return res, (json.loads(out.read_text()) if out.exists() else None)


def test_no_phase1_data_is_byte_identical(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    res, _ = run_analysis(tmp_path, empty)
    assert res.returncode == 0, res.stderr
    assert (tmp_path / "analysis.json").read_bytes() == (HERE.parent / "results" / "analysis.json").read_bytes()


def test_phase1_leaves_september_blocks_unchanged(tmp_path, phase1_dir):
    res, a = run_analysis(tmp_path, phase1_dir)
    assert res.returncode == 0, res.stderr
    assert a["models"] == COMMITTED["models"] and a["token_costs"] == COMMITTED["token_costs"]
    assert a["n_records"] == COMMITTED["n_records"]
    assert a["bh_original_family"] == COMMITTED["bh"]
    assert a["bh"]["n_tests"] == 112 + 82  # the locked Phase-1 family
    p = a["phase1"]
    assert p["status"] == {}
    assert set(p["ablation"]) == {ap1.LUNA, ap1.QWEN} and set(p["infoform"]) == set(st.FAMILIES)
    assert p["ablation"][ap1.LUNA]["pairs"] == 72 and p["ablation"][ap1.QWEN]["pairs"] == 120
    assert set(p["predictions"]) == {f"P{i}" for i in range(1, 10)}
    assert p["predictions"]["P8"]["holds"] is None  # route arm not run (amendment 1)
    assert p["noise_floor"][ap1.LUNA] is not None
    assert p["noise_floor"]["gemini-3.1-pro-preview"] == p["noise_floor"]["gemini-3.6-flash"]
    assert p["thinking_selection"]["selected"] in st.BEST_CELL_CANDIDATES
    assert set(p["drift_over_time"][ap1.LUNA]["call_identity"]) == set(analyze_classes())
    assert p["drift_over_time"][ap1.LUNA]["n"] == 120
    assert p["family"] == {"n_tests": 194, "expected": 194, "complete": True}
    luna_cells = p["instrument"][ap1.LUNA]
    assert luna_cells["C:sys:json:none"]["n"] == 120  # base level, rep 0 only
    assert luna_cells["C:sys:json:none@high"]["n"] == 120 and luna_cells["C:sys:json:none@noise"]["n"] == 120
    assert p["mechanism"][ap1.LUNA]["C_decl"]
    assert p["accounting"]["prompt_tokens_per_call"]


def test_incomplete_arm_adds_no_tests(tmp_path, phase1_dir):
    d = tmp_path / "partial"
    shutil.copytree(phase1_dir, d)
    (d / "runs_gemini-3.1-pro-preview.jsonl").unlink()  # Pro never ran
    res, a = run_analysis(tmp_path, d)
    assert res.returncode == 0, res.stderr
    assert a["bh"]["n_tests"] == 194 - 4
    assert a["phase1"]["status"] == {"gemini-3.1-pro-preview:infoform": "incomplete"}
    assert a["phase1"]["predictions"]["P6"]["holds"] in (None, False)


def test_pilot_files_ignored(tmp_path, phase1_dir):
    d = tmp_path / "with_pilot"
    shutil.copytree(phase1_dir, d)
    (d / "runs_openai_gpt-5.6-luna.pilot.jsonl").write_text("not json\n")
    res, a = run_analysis(tmp_path, d)
    assert res.returncode == 0, res.stderr
    assert a["bh"]["n_tests"] == 194


def test_thinking_selection_mismatch_fails(tmp_path, phase1_dir):
    d = tmp_path / "bad_selection"
    shutil.copytree(phase1_dir, d)
    sel = json.loads((d / ap1.SELECTION_FILE).read_text())
    other = next(c for c in st.BEST_CELL_CANDIDATES if c != sel["selected"])
    (d / ap1.SELECTION_FILE).write_text(json.dumps({**sel, "selected": other}))
    res, _ = run_analysis(tmp_path, d)
    assert res.returncode != 0 and "thinking arm ran on the wrong cell" in res.stderr


def test_unparsable_phase1_line_stops_the_analysis(tmp_path, phase1_dir):
    d = tmp_path / "broken"
    shutil.copytree(phase1_dir, d)
    with (d / "runs_gemini-3.6-flash.jsonl").open("a") as f:
        f.write('{"half": ')
    res, _ = run_analysis(tmp_path, d)
    assert res.returncode != 0 and "unparsable" in res.stderr


def test_blocks_in_process(phase1_dir):
    """Same blocks without a subprocess (coverage), with a counting ctx."""
    import types

    import analyze
    import numpy as np
    labels = []
    ctx = types.SimpleNamespace(
        rng=np.random.default_rng(1), boot=lambda d: [float(np.min(d)), float(np.max(d))],
        paired=lambda d, label: labels.append(label) or {"mean": float(np.mean(d)), "ci95": [-1.0, 1.0],
                                                        "p_signflip": 0.5},
        register=lambda label, p: labels.append(label))
    p1runs = ap1.load_phase1_runs(phase1_dir)
    block = ap1.analyze(analyze.load_runs(), p1runs, ctx, {"gemini-3.6-flash": {"success_flip_rate": 0.133},
                                                           ap1.QWEN: {"success_flip_rate": 0.0}}, phase1_dir)
    assert len(labels) == 82 and len(set(labels)) == 82 and all(x.startswith("p1:") for x in labels)
    preds = ap1.predictions(block, survivors=set())
    assert preds["P1"]["holds"] is True  # nothing survives BH, so no system-prompt cell unlocks
    assert ap1.analyze(analyze.load_runs(), [], ctx, {}, phase1_dir) is None
    assert ap1.predictions({**block, "ablation": {}}, set()) == {"pending": "luna ablation and noise arms must be complete"}


def analyze_classes():
    return ["rename", "enum_tighten", "required", "type_change", "default_change"]


def test_missing_selection_file_with_thinking_records_fails(tmp_path, phase1_dir):
    d = tmp_path / "no_selection"
    shutil.copytree(phase1_dir, d)
    (d / ap1.SELECTION_FILE).unlink()
    res, _ = run_analysis(tmp_path, d)
    assert res.returncode != 0 and "must be committed before the thinking arm" in res.stderr


def test_partial_family_never_overwrites_the_published_analysis(tmp_path, phase1_dir):
    import analyze
    d = tmp_path / "partial2"
    shutil.copytree(phase1_dir, d)
    (d / "runs_gemini-3.1-pro-preview.jsonl").unlink()
    before = (HERE.parent / "results" / "analysis.json").read_bytes()
    res = subprocess.run([sys.executable, str(HERE / "analyze.py"), "--phase1-dir", str(d)],
                         capture_output=True, text=True)
    assert res.returncode != 0 and "not overwriting" in res.stderr
    assert (HERE.parent / "results" / "analysis.json").read_bytes() == before
    assert analyze.RESULTS == HERE.parent / "results"
