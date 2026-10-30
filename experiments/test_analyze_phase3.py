#!/usr/bin/env python3
"""Phase-3 wiring of analyze.py: the corpus block must appear without moving anything else.

Run: python3 -m pytest test_analyze_phase3.py -q
"""

import json
import pathlib
import subprocess
import sys
import types

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_phase3 as ap3  # noqa: E402

RESULTS = HERE.parent / "results"
COMMITTED = json.loads((RESULTS / "analysis.json").read_text())


def unit(label, visible=True, source="stripe", rank=0, parameter="p"):
    return {"unit_id": f"{source}:{rank}:{parameter}", "source": source, "draw_rank": rank,
            "entry_url": "https://d.test/x", "scope": "S", "parameter": parameter,
            "label": label, "agent_visible": visible, "agent_visible_disputed": False}


ROWS = ([unit("rename", True, rank=i, parameter=f"p{i}") for i in range(6)]
        + [unit("compound", False, rank=10 + i, parameter=f"q{i}") for i in range(2)]
        + [unit("other", None, rank=20 + i, parameter=f"r{i}") for i in range(2)]
        + [unit("required", True, source="slack", rank=i, parameter=f"s{i}") for i in range(2)])


def ctx():
    rng = np.random.default_rng(1)
    return types.SimpleNamespace(rng=rng, share=lambda flags: {
        "point": float(np.mean(flags)) if len(flags) else None,
        "ci95": [0.0, 1.0] if len(flags) else None, "n": len(flags)})


def write_corpus(tmp_path, rows=ROWS):
    (tmp_path / "corpus.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    (tmp_path / "agreement.json").write_text(json.dumps({"label": {"rate": 0.95}, "passes": True}))
    return tmp_path


def test_no_corpus_means_no_block(tmp_path):
    assert ap3.analyze(tmp_path, ctx()) is None


def test_flags_count_the_four_predicted_quantities():
    f = ap3.flags(ROWS)
    assert sum(f["coverage"]) == 10 and len(f["coverage"]) == 12   # two "other" are not covered
    assert sum(f["costly"]) == 2                                   # the two slack "required"
    assert sum(f["compound"]) == 2
    assert len(f["reach"]) == 10 and sum(f["reach"]) == 8          # the None units drop out


def test_block_reports_pooled_and_per_source(tmp_path):
    block = ap3.analyze(write_corpus(tmp_path), ctx())
    assert block["pooled"]["n_units"] == 12
    assert set(block["by_source"]) == {"stripe", "slack"}
    assert block["by_source"]["slack"]["n_units"] == 2
    assert block["pooled"]["labels"] == {"rename": 6, "compound": 2, "required": 2, "other": 2}
    assert block["pooled"]["agent_visible"] == {"true": 8, "false": 2, "unknown": 2}
    assert "source-weighted" in block["pooled"]["note"]
    assert block["status"] == {}


def test_a_missing_agreement_file_is_a_status_not_a_crash(tmp_path):
    write_corpus(tmp_path)
    (tmp_path / "agreement.json").unlink()
    block = ap3.analyze(tmp_path, ctx())
    assert block["agreement"] is None and block["status"] == {"agreement": "missing"}


def test_predictions_are_p17_to_p20(tmp_path):
    block = ap3.analyze(write_corpus(tmp_path), ctx())
    preds = ap3.predictions(block)
    assert list(preds) == ["P17", "P18", "P19", "P20"]
    assert all(p["holds"] is None for p in preds.values())   # the fake CI [0, 1] decides nothing


def test_an_empty_phase3_dir_leaves_analysis_json_byte_identical(tmp_path):
    out = tmp_path / "analysis.json"
    empty = tmp_path / "nothing"
    empty.mkdir()
    res = subprocess.run([sys.executable, str(HERE / "analyze.py"),
                          "--phase3-dir", str(empty), "--out", str(out)],
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    got = json.loads(out.read_text())
    assert "phase3" not in got
    for key in ("models", "token_costs", "n_records", "phase1", "phase2", "bh",
                "bh_original_family"):
        assert got[key] == COMMITTED[key], key


def test_the_corpus_registers_no_bh_test(tmp_path):
    import analyze
    before = len(analyze.ALL_P)
    ap3.analyze(write_corpus(tmp_path), ctx())
    assert len(analyze.ALL_P) == before
