#!/usr/bin/env python3
"""Phase-2 wiring of analyze.py: fake Phase-2 records on top of the real September and
Phase-1 data, so "those blocks do not move" is checked against the committed analysis.json.
analyze.py runs in a subprocess so its module-level RNGs and ALL_P start fresh.

Run: python3 -m pytest test_analyze_phase2.py -q
"""

import json
import pathlib
import shutil
import subprocess
import sys
import types
import zlib

import numpy as np
import pytest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_phase2 as ap2  # noqa: E402
import phase2_grid as p2  # noqa: E402
import phase2_stats as v  # noqa: E402
from test_phase1 import oracle  # noqa: E402

RESULTS = HERE.parent / "results"
COMMITTED = json.loads((RESULTS / "analysis.json").read_text())
PHASE1_DIR = RESULTS / "phase1"
INPUTS = ("probe_decoding.json", "validator_replay.json")
PIN = {"provider": "fake", "strict": "unset", "endpoint": "openrouter", "quantization": None, "max_tokens": 700}


def stops_on_errors(call):
    """The test oracle reads step 1's result as JSON; after an error (retry conditions) it stops."""
    def wrapped(*args):
        try:
            return call(*args)
        except json.JSONDecodeError:
            return {"final": "giving up"}
    return wrapped


def fake(model, arm, reasoning="default"):
    """Deterministic v1/v2 mix per job; rep 0 of the noise arm is the core record, as in the runs."""
    out = []
    for job in p2.jobs(arm):
        t, cond, cls, ph, rep = job
        if arm == "noise" and rep == 0:
            continue
        seed = zlib.crc32(f"{model}|{t['id']}|{cond}|{cls}|{ph}|{rep}".encode())
        call = stops_on_errors(oracle("v2" if seed % 3 else "v1")(t, cls))
        out.append(p2.run_episode(job, call, model, arm, reasoning, 700, PIN))
    return out


def write(path, records):
    with path.open("a") as f:
        f.writelines(json.dumps(r) + "\n" for r in records)


def file_of(model):
    return f"runs_{model.replace('/', '_')}.jsonl"


@pytest.fixture(scope="module")
def phase2_dir(tmp_path_factory):
    d = tmp_path_factory.mktemp("phase2")
    for m in v.NEW_FAMILIES:
        write(d / file_of(m), [r for arm in ap2.FAMILY_ARMS for r in fake(m, arm)])
    write(d / file_of(v.FLASH), fake(v.FLASH, "fill", "MINIMAL"))
    for name in INPUTS:
        shutil.copy(RESULTS / "phase2" / name, d / name)
    return d


def run_analysis(tmp_path, phase2_dir, out=True):
    target = tmp_path / "analysis.json"
    empty3 = tmp_path / "no_phase3"          # these tests look at Phase 2 alone
    empty3.mkdir(exist_ok=True)
    cmd = [sys.executable, str(HERE / "analyze.py"), "--phase1-dir", str(PHASE1_DIR),
           "--phase2-dir", str(phase2_dir), "--phase3-dir", str(empty3)]
    res = subprocess.run(cmd + (["--out", str(target)] if out else []), capture_output=True, text=True)
    return res, (json.loads(target.read_text()) if out and target.exists() else None)


@pytest.fixture(scope="module")
def full(tmp_path_factory, phase2_dir):
    res, a = run_analysis(tmp_path_factory.mktemp("out"), phase2_dir)
    assert res.returncode == 0, res.stderr
    return a


def test_september_and_phase1_blocks_do_not_move(full):
    for k in ("models", "token_costs", "n_records", "phase1", "bh_original_family"):
        assert full[k] == COMMITTED[k], k


def test_one_bh_family_of_301(full):
    assert full["bh"]["n_tests"] == 301
    p = full["phase2"]
    assert p["status"] == {}
    assert p["family"] == {"n_tests": 301, "expected": 301, "complete": True}
    assert set(p["bh_changes"]) == {"lost", "gained"}
    assert not any(lab.startswith("p2:") for lab in p["bh_changes"]["lost"] + p["bh_changes"]["gained"])


def test_phase2_blocks(full):
    p = full["phase2"]
    assert set(p["models"]) == set(v.NEW_FAMILIES)
    llama = p["models"][v.LLAMA]
    assert llama["n_pairs"] == 120 and set(llama["phrasing_battery"]) == {"A", "B_strict"}
    assert llama["arg_style"]["optional_fill_rate"] is not None
    assert set(p["infoform"]) == set(p["placement"]) == set(v.NEW_FAMILIES)
    assert p["infoform"][v.SONNET]["Dprime-D_required"]["n"] == 24
    assert p["infoform"][v.SONNET]["CD-C"]["n"] == 48
    plc = p["placement"][v.HAIKU]
    assert plc["vs_B"]["n"] == plc["vs_C"]["n"] == 120 and "gain_over_C" in plc
    assert all(p["noise_floor"][m] is not None for m in v.NEW_FAMILIES)
    assert p["noise_floor"][v.FLASH] == COMMITTED["models"][v.FLASH]["noise_floor"]["success_flip_rate"]
    assert p["fill"]["tests"]["info"]["n"] == 48 and p["fill"]["tests"]["contrast"]["n"] == 72
    assert set(p["fill"]["success"]) == {"A_fill", "B_fill", "B_strict"}
    assert p["direct"]["run"] is False and p["probe"]["decision"]["lifts"] is False
    assert p["validator_replay"]["n_calls"] == 5208
    assert p["mechanism"][v.SONNET]["B_strict"] and p["mechanism"]["audit_agreement"] is None
    assert p["instrument"][v.HAIKU]["B_strict@noise"]["n"] == 120
    assert p["instrument"][v.HAIKU]["A@phrasing1"]["n"] == 120


def test_predictions(full):
    preds = full["phase2"]["predictions"]
    assert list(preds) == [f"P{i}" for i in range(10, 17)]
    assert preds["P15"]["holds"] is None
    assert preds["P16"]["holds"] is False  # real replay: pydantic default ~ lenient 0.877


def counting_ctx(labels):
    import analyze
    ctx = types.SimpleNamespace(
        rng=np.random.default_rng(1), prefix="p2:", boot=lambda d: [float(np.min(d)), float(np.max(d))],
        paired=lambda d, label: labels.append(label) or {"n": len(d), "mean": float(np.mean(d)),
                                                        "ci95": [-1.0, 1.0], "p_signflip": 0.5},
        register=lambda label, p: labels.append(label), arg_style=analyze.analyze_arg_style)
    ctx.september = lambda recs, m: analyze.analyze_model(recs, m, ctx)
    ctx.phrasing = lambda recs, m: analyze.analyze_phrasing(recs, m, ctx)
    return ctx


def test_blocks_in_process_register_107_p2_tests(phase2_dir):
    labels = []
    runs = ap2.load_phase2_runs(phase2_dir)
    block = ap2.analyze(runs, counting_ctx(labels), {v.FLASH: {"success_flip_rate": 0.133}}, phase2_dir)
    assert len(labels) == 107 and len(set(labels)) == 107 and all(x.startswith("p2:") for x in labels)
    preds = ap2.predictions(block, survivors=set())
    assert preds["P10"]["holds"] is None  # fake data: A <= B_strict, so recovery is undefined (pending)
    assert preds["P14"]["holds"] is False  # nothing survives BH
    assert ap2.analyze([], counting_ctx([]), {}, phase2_dir) is None


def test_incomplete_arm_adds_no_tests(tmp_path, phase2_dir):
    d = tmp_path / "partial"
    shutil.copytree(phase2_dir, d)
    path = d / file_of(v.LLAMA)
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    path.write_text("".join(json.dumps(r) + "\n" for r in rows if r["cond"] != p2.PLACEMENT_CELL))
    (d / "runs_x.pilot.jsonl").write_text("not json\n")  # pilots are never read
    res, a = run_analysis(tmp_path, d)
    assert res.returncode == 0, res.stderr
    assert a["bh"]["n_tests"] == 301 - 2
    assert a["phase2"]["status"] == {f"{v.LLAMA}:placement": "incomplete"}
    assert a["phase2"]["family"]["complete"] is False
    assert a["phase2"]["predictions"]["P11"]["holds"] is None


def test_partial_family_never_overwrites_the_published_analysis(tmp_path, phase2_dir):
    d = tmp_path / "partial2"
    shutil.copytree(phase2_dir, d)
    (d / file_of(v.FLASH)).unlink()
    before = (RESULTS / "analysis.json").read_bytes()
    res, _ = run_analysis(tmp_path, d, out=False)
    assert res.returncode != 0 and "Phase-2 family" in res.stderr and "not overwriting" in res.stderr
    assert (RESULTS / "analysis.json").read_bytes() == before


def test_unparsable_line_stops_the_analysis(tmp_path, phase2_dir):
    d = tmp_path / "broken"
    shutil.copytree(phase2_dir, d)
    with (d / file_of(v.HAIKU)).open("a") as f:
        f.write('{"half": ')
    res, _ = run_analysis(tmp_path, d)
    assert res.returncode != 0 and "unparsable" in res.stderr


def test_one_job_through_two_endpoints_stops_the_analysis(tmp_path, phase2_dir):
    d = tmp_path / "two_endpoints"
    shutil.copytree(phase2_dir, d)
    rec = json.loads((d / file_of(v.HAIKU)).read_text().splitlines()[0])
    write(d / "runs_zz_other.jsonl", [{**rec, "pin": {**rec["pin"], "endpoint": "openai"}}])
    with pytest.raises(SystemExit, match="endpoints"):
        ap2.load_phase2_runs(d)


def test_direct_records_without_a_lift_stop_the_analysis(phase2_dir):
    probe = json.loads((phase2_dir / "probe_decoding.json").read_text())["summary"]
    rec = {"model": "openai/gpt-5.6-luna", "arm": "direct"}
    with pytest.raises(SystemExit, match="direct"):
        ap2.direct_block(probe, [rec])
    assert ap2.direct_block(None, [])["basis"].startswith("decoding probe missing")
