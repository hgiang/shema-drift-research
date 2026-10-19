#!/usr/bin/env python3
"""Pin A6: pick luna's thinking cell from the complete ablation, before the thinking arm runs.

Writes results/phase1/thinking_cell_selection.json ({"selected", "recoveries", "success_all",
"rule"}); commit it before `run_openrouter.py --arm thinking --cells C:sys:json:none,<selected>`.
analyze.py re-derives the selection and fails loudly if the file disagrees.

Usage:  python3 select_thinking_cell.py [--phase1-dir ../results/phase1]
"""

import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze  # noqa: E402  (load_runs only)
import analyze_phase1 as ap1  # noqa: E402


def select(phase1_dir):
    p1runs = ap1.load_phase1_runs(phase1_dir)
    if not ap1.complete(p1runs, ap1.LUNA, "ablation"):
        raise SystemExit("luna ablation is incomplete: finish it (and pass the log gate) first")
    tab = ap1.build_tab(ap1.sept_index(analyze.load_runs()), p1runs, ap1.LUNA)
    return ap1.thinking_selection(tab)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase1-dir", type=pathlib.Path, default=analyze.PHASE1)
    args = ap.parse_args(argv)
    sel = select(args.phase1_dir)
    out = args.phase1_dir / ap1.SELECTION_FILE
    out.write_text(json.dumps(sel, indent=1))
    print(f"selected {sel['selected']!r} -> {out}")
    print(f"thinking arm cells: {ap1.st.REPLICATE_C},{sel['selected']}")


if __name__ == "__main__":
    main()
