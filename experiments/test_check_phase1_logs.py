#!/usr/bin/env python3
"""Tests for the Phase-1 log checker (the run gate). No API calls.

Run: python3 -m pytest test_check_phase1_logs.py -q
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_phase1_logs as chk  # noqa: E402
import harness  # noqa: E402
import phase1_grid as p1  # noqa: E402
from test_phase1 import oracle  # noqa: E402


def key_rec(job, reasoning="default"):
    t, cond, cls, ph, rep = job
    return {"task": t["id"], "cond": cond, "class": cls, "phrasing": ph, "rep": rep, "reasoning": reasoning}


def fake_run(jobs, arm="infoform", meta=None):
    out = []
    for job in jobs:
        t, cond, cls, ph, rep = job
        rec = p1.run_episode(job, oracle("v2")(t, cls), "m/x", arm, "default", 700)
        out.append({**rec, "meta": meta or {"provider": "OpenAI", "model": "m/x-2026", "finish_reason": "stop"}})
    return out


def write(path, records, tail=""):
    path.write_text("".join(json.dumps(r) + "\n" for r in records) + tail)
    return path


def test_unparsable_line_reported_with_line_number(tmp_path):
    f = write(tmp_path / "r.jsonl", fake_run(p1.jobs("infoform")[:2]), tail='{"glued": 1}{"x"\n')
    records, bad = chk.read_records(f)
    assert len(records) == 2 and bad == [3]
    ok, report = chk.gate(f, "infoform", "default", pilot=True)
    assert not ok and report["unparsable_lines"] == [3]


def test_complete_fake_run_passes(tmp_path):
    f = write(tmp_path / "r.jsonl", fake_run(p1.jobs("infoform")[:10]))
    ok, report = chk.gate(f, "infoform", "default", pilot=True)
    assert ok, report["failures"]
    assert report["coverage"]["present"] == 10 and report["coverage"]["expected"] == 240
    assert set(report["cells"]) <= {"CD", "Dprime"}
    ok_full, report_full = chk.gate(f, "infoform", "default")
    assert not ok_full and any("coverage" in x for x in report_full["failures"])


def test_two_providers_in_one_cell_fail_gate(tmp_path):
    jobs = [j for j in p1.jobs("infoform") if j[1] == "CD"][:4]
    recs = fake_run(jobs[:2]) + fake_run(jobs[2:], meta={"provider": "Azure", "model": "m/x-2026",
                                                          "finish_reason": "stop"})
    ok, report = chk.gate(write(tmp_path / "r.jsonl", recs), "infoform", "default", pilot=True)
    assert not ok and report["cells"]["CD"]["providers"] == {"Azure": 2, "OpenAI": 2}


def test_length_rate_above_5pct_fails_gate(tmp_path):
    jobs = [j for j in p1.jobs("infoform") if j[1] == "Dprime"][:20]
    recs = fake_run(jobs[:18]) + fake_run(jobs[18:], meta={"provider": "OpenAI", "model": "m/x-2026",
                                                           "finish_reason": "length"})
    ok, report = chk.gate(write(tmp_path / "r.jsonl", recs), "infoform", "default", pilot=True)
    assert report["cells"]["Dprime"]["length_rate"] == 0.1
    assert not ok and any("length" in x for x in report["failures"])
    ok19, _ = chk.gate(write(tmp_path / "s.jsonl", fake_run(jobs[:19]) + recs[19:]), "infoform", "default",
                       pilot=True)
    assert ok19  # 1/20 = 5% is allowed


def test_gemini_max_tokens_counts_as_length(tmp_path):
    recs = fake_run(p1.jobs("infoform")[:1], meta={"model": "g", "finish_reason": "MAX_TOKENS"})
    assert next(iter(chk.cell_report(recs).values()))["length_rate"] == 1.0


def test_two_model_versions_fail_gate(tmp_path):
    jobs = p1.jobs("infoform")[:4]
    recs = fake_run(jobs[:2]) + fake_run(jobs[2:], meta={"provider": "OpenAI", "model": "m/x-2027",
                                                         "finish_reason": "stop"})
    ok, report = chk.gate(write(tmp_path / "r.jsonl", recs), "infoform", "default", pilot=True)
    assert not ok and report["versions"] == {"m/x-2026": 2, "m/x-2027": 2}


def test_duplicate_keys_fail_gate(tmp_path):
    recs = fake_run(p1.jobs("infoform")[:3])
    ok, report = chk.gate(write(tmp_path / "r.jsonl", recs + recs[:1]), "infoform", "default", pilot=True)
    assert not ok and len(report["duplicates"]) == 1


def test_coverage_lists_missing_keys():
    jobs = p1.jobs("ablation")
    cov = chk.coverage([key_rec(j) for j in jobs[1:]], "ablation", "default")
    assert cov["expected"] == 1560 and cov["present"] == 1559
    assert cov["missing"] == [p1.key(jobs[0][0]["id"], *jobs[0][1:], "default")]


def test_noise_rep0_satisfied_by_ablation_record():
    rep0 = [j for j in p1.jobs("noise") if j[4] == 0]
    others = [j for j in p1.jobs("noise") if j[4] != 0]
    ablation_like = [{**key_rec(j), "arm": "ablation"} for j in rep0]
    cov = chk.coverage(ablation_like + [key_rec(j) for j in others], "noise", "default")
    assert cov["present"] == cov["expected"] == 150 and cov["missing"] == []


def test_completeness_flags_missing_fields_and_bad_tool_preamble():
    t, cls = p1.primary_pairs()[0]
    good = {**p1.run_episode((t, "C:tool:json:none", cls, 0, 0), oracle("v2")(t, cls), "m/x", "ablation",
                             "default", 700),
            "meta": {"provider": "OpenAI", "model": "m/x-2026", "finish_reason": "stop"}}
    assert chk.completeness([good]) == []
    broken = {**good, "transcript": good["transcript"][2:]}
    no_usage = {**good, "usage": {"in": 0, "out": 0, "reasoning": 0}}
    no_arm = {k: v for k, v in good.items() if k != "arm"}
    problems = chk.completeness([broken, no_usage, no_arm])
    assert len(problems) == 3
    assert any("preamble" in p for p in problems) and any("usage" in p for p in problems)
    assert any("arm" in p for p in problems)


def test_changelog_recall_rate_counts_real_changelog_calls():
    t, cls = p1.primary_pairs()[0]
    asked = []

    def model(system, user, decls, transcript):
        if not asked:
            asked.append(1)
            return {"name": harness.CHANGELOG_TOOL, "args": {"tool": t["drift_tool"]}, "usage": {"in": 5}}
        return {"final": "DONE", "usage": {"in": 5}}

    recalled = p1.run_episode((t, "C:tool:prose:none", cls, 0, 0), model, "m/x", "ablation", "default", 700)
    plain = p1.run_episode((t, "C:tool:prose:none", cls, 0, 0), oracle("v2")(t, cls), "m/x", "ablation",
                           "default", 700)
    cells = chk.cell_report([recalled, plain])
    assert cells["C:tool:prose:none"]["changelog_recall_rate"] == 0.5
    assert chk.cell_report([plain])["C:tool:prose:none"]["n"] == 1


def test_spend_report_reads_phase1_rows_only(tmp_path):
    log = tmp_path / "cost_log.jsonl"
    rows = [{"ts": "2026-10-20T10:00:00", "phase": "phase1", "model": "m/x", "tag": "p1-a", "est_cost_usd": 0.01},
            {"ts": "2026-10-20T10:02:00", "phase": "phase1", "model": "m/x", "tag": "p1-b", "est_cost_usd": 0.03},
            {"ts": "2026-10-20T10:03:00", "phase": "phase1", "model": "m/x", "tag": "p1-probe-x", "est_cost_usd": 9},
            {"ts": "2026-09-09T10:00:00", "phase": "experiments", "model": "m/x", "tag": "kw", "est_cost_usd": 9}]
    write(log, rows)
    s = chk.spend_report("m/x", 4, log)
    assert s["usd"] == 0.04 and s["usd_per_episode"] == 0.01
    assert s["episodes_per_minute"] == 1.0  # 2 episodes over 2 minutes
    assert chk.spend_report("other", 4, log)["usd"] == 0


def test_cli_exit_code(tmp_path):
    import subprocess
    f = write(tmp_path / "r.jsonl", fake_run(p1.jobs("infoform")[:3]))
    run = lambda *a: subprocess.run([sys.executable, str(HERE / "check_phase1_logs.py"), str(f), *a],
                                    capture_output=True, text=True)
    assert run("--arm", "infoform", "--pilot").returncode == 0
    res = run("--arm", "infoform")
    assert res.returncode == 1 and "FAIL" in res.stdout


def test_pilot_with_no_matching_record_fails(tmp_path):
    f = write(tmp_path / "r.jsonl", fake_run(p1.jobs("infoform")[:3]))
    ok, report = chk.gate(f, "infoform", "LOW", pilot=True)  # runner wrote reasoning "default"
    assert not ok and any("no record matches" in x for x in report["failures"])
    assert report["excluded_other_arms"] == 3


def test_missing_provider_model_or_finish_reason_fails():
    t, cls = p1.primary_pairs()[0]
    rec = fake_run([(t, "CD", cls, 0, 0)])[0]
    assert chk.completeness([rec]) == []
    no_provider = {**rec, "meta": {"model": "m/x-2026", "finish_reason": "stop"}}
    assert any("meta.provider" in x for x in chk.completeness([no_provider]))
    gemini = {**rec, "model": "gemini-3.6-flash", "meta": {"model": "g", "finish_reason": "STOP"}}
    assert chk.completeness([gemini]) == []  # Gemini has no provider field
    assert any("meta.finish_reason" in x for x in chk.completeness([{**gemini, "meta": {"model": "g"}}]))


def test_records_without_a_key_are_reported(tmp_path):
    recs = fake_run(p1.jobs("infoform")[:2])
    broken = {k: v for k, v in recs[0].items() if k != "class"}
    ok, report = chk.gate(write(tmp_path / "r.jsonl", recs + [broken]), "infoform", "default", pilot=True)
    assert not ok and any("without a full key" in x for x in report["failures"])
