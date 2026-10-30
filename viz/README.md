# SchemaDrift-120 Explorer

An interactive, static explorer for the testbed, all 4,800 logged episodes, and
`results/analysis.json`. No server and no dependencies beyond the repo's
`requirements.txt`. It opens straight from disk and can be served by GitHub Pages at
`docs/explorer/`.

```bash
python3 viz/build_explorer_data.py      # -> docs/explorer/data.js (about 5 MB, deterministic)
open docs/explorer/index.html           # or any browser; file:// works
```

Rebuild `data.js` whenever `results/` or the testbed changes. The builder refuses to run
if the deduplicated episode count disagrees with `analysis.json → n_records`.

## Views

| Tab | What it shows | Source |
|---|---|---|
| Overview | Success matrix (model × condition), condition profile, drop and recovery-fraction forests | `analysis.json` |
| Drift classes | Per-class success for any condition, per-class drop and lever gain with CIs, BH status | `analysis.json` |
| Ledger | Error surfaced / accepted correct / accepted wrong per class and model; silent share of failures | `analysis.json` (B); raw episodes (C, D, E) |
| Pivot | Any field × any field, six metrics, chip filters, CSV export | raw episodes |
| Episodes | Filter and page through every episode; detail shows the exact system prompt and tool declarations, the schema change, the executor error, and each accepted call compared field by field with ground truth | raw episodes + `harness.build_condition` |
| Dataset | The 30 tools (v1 parameters, each drift variant, v2 parameters) and the 120 tasks (phrasings, ground truth before and after each drift) with per-item success | `testbed_frozen.json` + raw episodes |
| Statistics | All 112 September paired tests: mean, CI, p, d_z, BH survival (BH over the family in `analysis.json`: 112 in the shipped bundle, 307 once rebuilt with Phases 1-3); noise floor; calling style; token accounting | `analysis.json` |
| Audit | The 24 hand-audited accepted-wrong calls, linked to their episodes | `audit_accepted_wrong_sample.json` |

Every cell and bar can be clicked to open its episodes. The model chips in the header
show or hide a model everywhere (the setting is saved in `localStorage`). URLs hold
the full view state, so you can share a link to a specific filter or episode. In the
episode browser, `j` and `k` step through the list.

## How the numbers stay honest

- Curated views read `analysis.json` verbatim; nothing inferential is recomputed.
- Episodes come from `analyze.load_runs()`, the same deduplication `analyze.py` uses.
  The test suite checks that core-battery success rates recomputed from the bundle
  equal `analysis.json → success_rate` for every model and condition.
- Prompts are rebuilt with `harness.build_condition`, and the tests check that they
  match exactly.
- Field-level comparisons replay each logged accepted call through
  `experiments/executor.py` and compare with `harness.effective_gt` and
  `harness.semantically_equal`. The tests require the replay to reproduce every
  logged step outcome. Rejected calls are not logged with their arguments, so only
  the executor's error message is shown for them.

## Tests

```bash
python3 -m pytest viz/test_explorer_data.py -q     # bundle correctness (13 tests)
node viz/smoke_test_explorer.mjs                   # headless Chrome: every view + interactions
WIDTH=820 FULL=1 node viz/smoke_test_explorer.mjs /tmp/narrow   # narrow layout, full-page shots
```

The smoke test needs Node 22 or later and Google Chrome (set `CHROME=/path/to/chrome` if it
is not in the default macOS location). It fails on any uncaught exception or console
error and writes a screenshot per step.

## Files

| Path | Role |
|---|---|
| `viz/build_explorer_data.py` | Builds `docs/explorer/data.js` |
| `viz/episode_semantics.py` | Replays accepted calls into field-level comparisons |
| `docs/explorer/js/core.js` | DOM builder (text only, no `innerHTML`), formatting, labels, routing |
| `docs/explorer/js/charts.js` | SVG heat tables, dot strips, forest plots, stacked bars, sortable tables |
| `docs/explorer/js/fields.js` | Episode dimensions and URL-param filtering, shared by Pivot and Episodes |
| `docs/explorer/js/<view>.js` | One file per tab; `app.js` wires up tabs, model toggles and the hash router |
