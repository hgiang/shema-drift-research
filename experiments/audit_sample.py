#!/usr/bin/env python3
"""Task 13: hand audit of the drift-call labels (drift_labels.classify) on Phase-1 episodes.

draw:  stratified sample of the main records (rep 0, base reasoning, unrouted; the records the
       mechanism block labels), strata = model x automatic label, at least MIN_PER_STRATUM per
       non-empty stratum (all of a smaller one), then filled at random to N. The floor wins when
       the strata need more than N. Items are shuffled so strata do not cluster.
       Writes results/phase1/audit_labels_sample.json (the record, with the automatic labels)
       and audit_labels_sample.md (the reading copy: no automatic labels, so the reading is blind).
score: reads the human_label / note lines the reader filled in the .md, copies them into the
       .json, and prints the agreement. analyze.py reports the same agreement in
       phase1.mechanism.audit_agreement, recomputing the automatic labels with the current labeler.

Phase 2 (`--phase 2`, MILESTONES.md "Phase 2 pre-registration"): the population is
analyze_phase2.main_records (the mechanism block's records), B_strict is the same model's
Phase-2 record, seed 20261020; files go to results/phase2/.

Usage:  python3 audit_sample.py draw  [--phase1-dir ../results/phase1]
        python3 audit_sample.py score [--phase1-dir ../results/phase1]
        python3 audit_sample.py draw --phase 2 [--phase2-dir ../results/phase2]
"""

import argparse
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze  # noqa: E402  (load_runs, PHASE1)
import analyze_phase1 as ap1  # noqa: E402
import analyze_phase2 as ap2  # noqa: E402
import drift_labels  # noqa: E402
import harness  # noqa: E402

SEED = 20261019
SEED_P2 = 20261020
SEEDS = {1: SEED, 2: SEED_P2}
B_SOURCE = {1: "September B_strict", 2: "B_strict in this run"}
N = 24
MIN_PER_STRATUM = 2
SAMPLE_FILE = ap1.AUDIT_FILE
READING_FILE = "audit_labels_sample.md"
auto_label = ap1.auto_label
item_key = ap1.audit_key

PLACE = {"sys": "the system prompt", "user": "the user message",
         "tool": "a get_api_changelog result already in the transcript"}
SHOWN = {"C_decl": "old (v1) declaration, with the change written into the parameter's description",
         "CD": "new (v2) declaration, plus the JSON change log in the system prompt",
         "Dprime": "new (v2) declaration; the parameter's description also states the old contract",
         "B_strict": "old (v1) declaration, no change log",
         "B_lenient": "old (v1) declaration, no change log; the executor drops unknown parameters and coerces types",
         "C": "old (v1) declaration; JSON change log in the system prompt",
         "D": "new (v2) declaration, no change log",
         "E": "old (v1) declaration, no change log; a rejected call's error is shown and one retry allowed",
         "B_fill": "old (v1) declaration, no change log; the system prompt asks to pass every parameter explicitly"}

GUIDE = """# Hand audit of the drift-call labels

Read each item and write the label you would give the model's call at the drifted step.
Judge from the arguments the model actually sent (listed under "What the model did").
The automatic label is not shown here; it is in audit_labels_sample.json.

| label | when |
|---|---|
| V2_CORRECT | the call follows the new API on the drifted parameter and is accepted as correct |
| V2_PARTIAL | the model moved off the old form but got the new one wrong (e.g. a string in the old unit, a wrong new enum value) |
| V1_FORM | the call uses the old contract on the drifted parameter: old name, old enum value, old type, or leaves out the newly required / default-changed parameter |
| V1_SAFE | accepted as correct, but the same pair also succeeded with no change log (B_strict): the model fills that parameter anyway, so the success says nothing about reading the change (required / default_change only) |
| OTHER_ERROR | the executor rejected the call over a parameter that is not the drifted one |
| OTHER_WRONG | accepted but wrong for a reason other than the drifted parameter's form (another argument is wrong, or a renamed parameter was left out under both names) |
| NO_DRIFT_CALL | the model never called the drifted tool |

Fill in the two lines at the end of each item (the label is case-insensitive; leave the line
empty to skip an item), then run `python3 experiments/audit_sample.py score`:

    human_label: V1_FORM
    note: kept the old name `tags`
"""


def main_records(runs, phase=1):
    return ap2.main_records(runs) if phase == 2 else ap1._main_records(runs)


def population(runs, index, phase=1):
    """(record, automatic label) for the phase's main records; `index` holds the B_strict records."""
    recs = sorted(main_records(runs, phase), key=lambda r: json.dumps(item_key(r), sort_keys=True))
    return [(r, auto_label(r, index)) for r in recs]


def _pick(rng, members, k):
    return [members[j] for j in rng.choice(len(members), size=k, replace=False)] if k else []


def draw(runs, index, n=N, seed=None, phase=1):
    rng = np.random.default_rng(SEEDS[phase] if seed is None else seed)
    pop = population(runs, index, phase)
    strata = defaultdict(list)
    for i, (r, label) in enumerate(pop):
        strata[(r["model"], label)].append(i)
    picked = [i for s in sorted(strata) for i in _pick(rng, strata[s], min(MIN_PER_STRATUM, len(strata[s])))]
    taken = set(picked)
    rest = [i for i in range(len(pop)) if i not in taken]
    picked += _pick(rng, rest, min(max(0, n - len(picked)), len(rest)))
    order = rng.permutation(len(picked))
    return [item(k + 1, *pop[picked[j]], index, phase) for k, j in enumerate(order)]


def shown(cond):
    if cond.startswith("C:"):
        _, place, fmt, instr = cond.split(":")
        apply = "; with the 'apply it step by step' line" if instr == "apply" else ""
        return f"old (v1) declaration; change log in {PLACE[place]}, written as {fmt}{apply}"
    return SHOWN.get(cond, cond)


def item(item_id, r, label, index, phase=1):
    task = drift_labels.TASKS[r["task"]]
    didx = task["drift_step_index"]
    b = index.get((r["model"], r["task"], r["class"], "B_strict"))
    return {"id": item_id, "key": item_key(r), "auto_label": label,
            "request": task["phrasings"][r["phrasing"]], "drift_tool": task["drift_tool"],
            "change": drift_labels.drift_change(task, r["class"]), "shown": shown(r["cond"]),
            "expected": {"v1": task["gt_v1"][didx], "v2": task["gt_v2"][r["class"]][didx]},
            "b_strict_success": None if b is None else bool(b["success"]), "b_strict_source": B_SOURCE[phase],
            "transcript": r["transcript"], "final_text": r["final_text"],
            "drift_outcome": r["drift_outcome"], "error_seen": r["error_seen"], "success": r["success"],
            "human_label": None, "note": ""}


def _compact(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False)


def _one_line(text):
    return " / ".join(str(text).split("\n"))


def _steps(transcript):
    lines, n = [], 0
    for t in transcript or []:
        if t["role"] == "assistant_tool_call":
            n += 1
            who = " (pre-filled, not the model)" if t.get("synthetic") else ""
            lines.append(f"{n}. call `{t['name']}`{who}: `{_compact(t['args'])}`")
        elif t["role"] == "tool_result":
            lines.append(f"   - result: {_one_line(t['content'])}")
    return lines or ["(no tool calls)"]


def render_item(it):
    k = it["key"]
    b = {None: "not run", True: "succeeded", False: "failed"}[it["b_strict_success"]]
    error = f", error: {it['error_seen']}" if it["error_seen"] else ""
    return "\n".join([
        f"## Item {it['id']}", "",
        f"- model `{k['model']}` · condition `{k['cond']}` · drift class `{k['class']}` · task `{k['task']}`",
        f"- **User request:** {it['request']}",
        f"- **API change on `{it['drift_tool']}`:** {harness.prose_change(it['change'])}",
        f"- **Shown to the model:** {it['shown']}",
        f"- **Correct call, old API (v1):** `{_compact(it['expected']['v1'])}`",
        f"- **Correct call, new API (v2):** `{_compact(it['expected']['v2'])}`",
        f"- **Same model and pair with no change log ({it.get('b_strict_source', B_SOURCE[1])}):** {b}", "",
        "What the model did:", "", *_steps(it["transcript"]), "",
        f"Final text: {_one_line(it['final_text']) if it['final_text'] is not None else '(none)'}", "",
        f"Executor at the drift step: `{it['drift_outcome']}`{error}; episode "
        f"{'succeeded' if it['success'] else 'failed'}.", "",
        "human_label: ", "note: ", ""])


def render_md(items):
    return GUIDE + "\n" + "\n".join(render_item(it) for it in items)


def parse_answers(text):
    """{item id: (label or None, note)} from the reading copy."""
    answers, current = {}, None
    for line in text.splitlines():
        m = re.match(r"## Item (\d+)\s*$", line)
        if m:
            current = int(m.group(1))
            answers[current] = (None, "")
        elif current is not None and line.startswith("human_label:"):
            raw = line.split(":", 1)[1].strip().upper()
            if raw and raw not in drift_labels.LABELS:
                raise SystemExit(f"item {current}: unknown label {raw!r}; use one of {drift_labels.LABELS}")
            answers[current] = (raw or None, answers[current][1])
        elif current is not None and line.startswith("note:"):
            answers[current] = (answers[current][0], line.split(":", 1)[1].strip())
    return answers


def apply_answers(items, answers):
    unknown = sorted(set(answers) - {it["id"] for it in items})
    if unknown:
        raise SystemExit(f"answers for items not in the sample: {unknown}")
    return [{**it, "human_label": answers[it["id"]][0], "note": answers[it["id"]][1]} if it["id"] in answers
            else it for it in items]


def write_sample(out_dir, items, runs, index, phase=1):
    paths = (pathlib.Path(out_dir) / SAMPLE_FILE, pathlib.Path(out_dir) / READING_FILE)
    for f in paths:
        if f.exists():
            raise SystemExit(f"{f} exists: the sample is drawn once (delete both files by hand to redraw)")
    pop = Counter(f"{r['model']}|{label}" for r, label in population(runs, index, phase))
    sample = {"seed": SEEDS[phase], "n_target": N, "min_per_stratum": MIN_PER_STRATUM,
              "population": dict(sorted(pop.items())), "items": items}
    paths[0].write_text(json.dumps(sample, indent=1, ensure_ascii=False))
    paths[1].write_text(render_md(items))
    return paths


def score(out_dir, runs, index, phase=1):
    json_path = pathlib.Path(out_dir) / SAMPLE_FILE
    sample = json.loads(json_path.read_text())
    answers = parse_answers((pathlib.Path(out_dir) / READING_FILE).read_text())
    filled = {**sample, "items": apply_answers(sample["items"], answers)}
    json_path.write_text(json.dumps(filled, indent=1, ensure_ascii=False))
    return ap1.audit_agreement_on(main_records(runs, phase), index, filled)


def main(argv=None):  # pragma: no cover - writes the committed sample
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("draw", "score"))
    ap.add_argument("--phase", type=int, choices=(1, 2), default=1)
    ap.add_argument("--phase1-dir", type=pathlib.Path, default=analyze.PHASE1)
    ap.add_argument("--phase2-dir", type=pathlib.Path, default=analyze.PHASE2)
    args = ap.parse_args(argv)
    if args.phase == 2:
        out_dir, runs = args.phase2_dir, ap2.load_phase2_runs(args.phase2_dir)
        index = ap2.b_index(runs)
    else:
        out_dir, runs = args.phase1_dir, ap1.load_phase1_runs(args.phase1_dir)
        index = ap1.sept_index(analyze.load_runs())
    if args.command == "draw":
        items = draw(runs, index, phase=args.phase)
        for f in write_sample(out_dir, items, runs, index, args.phase):
            print(f"wrote {f}")
        print(f"{len(items)} items from {len(population(runs, index, args.phase))} records")
        return
    a = score(out_dir, runs, index, args.phase)
    print(f"labelled {a['n_labelled']}/{a['n_items']}, agree {a['n_agree']}, rate {a['rate']}, passes {a['passes']}")
    for d in a["disagreements"]:
        print(f"  item {d['id']}: auto {d['auto']}, human {d['human']}")


if __name__ == "__main__":
    main()
