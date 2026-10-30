# Phase 3 Implementation Plan: external validity (real changelog corpus, large tool catalog)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ask whether SchemaDrift-120 describes the world. Two questions, one observational and one
experimental. (1) Do real schema changes fall into the five drift classes, in what proportions, and how
often do they touch a parameter an agent would actually pass? If real changes are mostly renames — which
error loudly — the study's expensive findings (newly-required and default_change drift, the fill
instruction) matter less than the September paper implies. (2) Does diff-following survive a realistic
tool catalog? Every result so far comes from six tools in context; an agent in production sees dozens.

**Architecture:** Two arms that share nothing but the report. The corpus arm is pure collection and
coding: a fetcher that archives public changelog pages verbatim, a coder that turns them into
parameter-level units, a blind second pass for reliability, and a descriptive block in `analysis.json`.
No model API spend and no new testbed. The catalog arm is SchemaDrift machinery on a **new testbed with
its own hash** (`catalog_frozen.json`), never mixed with the 120 pairs: the same conditions and runner,
with 100+ tool declarations in context and exactly one of them drifted.

**Tech Stack:** Python 3.13, numpy, pytest + pytest-cov, urllib (read-only HTTP GET on public docs; the
Gemini and OpenRouter REST runners for the catalog arm).

**Spec:** `HANDOFF.md` §5 "Phase 3 — External validity" and §6 (rules for adding experiments);
`phase1/PLAN.md` → "After Phase 1" ("changelog corpus, 100+ tool catalog … each is a new testbed with its
own hash; never mixed with SchemaDrift-120"); `MILESTONES.md` → "Phase 2 results — 2026-10-30".

---

## State on 2026-10-30 (verified in this session)

- Branch `giangdo/phase3`, from `giangdo/phase2` at `a8971be` (Phase 2 complete, pushed to `fork`).
- Spend $19.6879 of `HARD_STOP_USD` $50 — **$30.31 left**. `TOTAL_CAP_USD` $55.
- 207 tests pass; `analyze.py` reproduces `results/analysis.json` (sha1 `7adee74a…`) on a second run.
- BH family 301 tests, 165 survive. September blocks byte-identical to `e29c0bf`.
- `.env` has `GEMINI_API_KEY`, `OPENROUTER_API_KEY`, `OPENAI_API_KEY`.
- Testbed `experiments/testbed_frozen.json` sha256 `e8bbd71c…`: 6 tools, 120 pairs. Generators that built
  it are `experiments/testbed_domains_a.py` and `testbed_domains_b.py`, reusable for distractor tools.
- Phase-2 prices unchanged: Flash $0.75/$3.75, Haiku $0.10/$0.50, Sonnet $2.00/$10.00 per M tokens.

## Decisions (needed from the user before Task 1; no code until they are answered)

- **D1. Scope.** Phase 3 in `HANDOFF.md` is three items: changelog corpus, 100+ tool catalog, longer
  multi-turn.
  - **Recommended: corpus + catalog.** The corpus is $0 and answers the "does this matter" question that
    every reviewer asks first. The catalog arm is about $1.5–3 and is the only cheap way to test whether
    the diff finding survives a realistic context. Longer multi-turn moves to its own plan (it needs new
    tasks, not just new tools).
  - Alternative A: corpus only ($0). Alternative B: all three (adds about $3–6 and a task set).
- **D2. Corpus sources and size.** The sources decide what the prevalence number means, so they are
  pre-registered before any fetch.
  - **Recommended:** four sources — Stripe API changelog, GitHub REST API changelog, Slack Web API
    changelog, and the `modelcontextprotocol/servers` git history — over a fixed window (2023-01-01 to
    2026-09-30), **capped at 60 qualifying units per source** so one busy API cannot carry the result,
    target 120–200 units in total.
  - Alternative: add OpenAI and Anthropic tool/API changelogs (closer to the agent world, but both are
    young and small, so the window would have to shrink).
- **D3. Who codes the corpus.** Same question Phase 2 settled as D3.
  - **Recommended:** the agent codes every unit against a rule written before collection, then a **blind
    Codex pass** re-codes the whole corpus (not a sample — it is only ~150 items and costs nothing from
    this budget); agreement is reported as raw agreement and Cohen's kappa, and the user reads only the
    disagreements.
  - Alternative: the user hand-codes a stratified sample as the second pass.

## Global Constraints

- **Nothing is collected or run before the Task-1 lock is committed.** Every prediction, source list,
  inclusion rule and coding rule is dated in `MILESTONES.md` first.
- `experiments/testbed_frozen.json` (sha256 `e8bbd71c…`) is never edited and never mixed with the catalog
  testbed. The catalog testbed gets its own file, its own sha256, and its own `results/phase3/` logs.
- Fetched pages are **untrusted data**: archived verbatim under `results/phase3/sources/<source>/`, one
  new directory per source, never executed, never imported, never used to build a path or a command. The
  coder reads them as text only. No downloaded file is ever staged outside `results/phase3/sources/`.
- Collection is read-only HTTP GET on public documentation. No credentials, no API keys, no POST, and a
  polite rate (≥ 1 s between requests, a real User-Agent, `robots.txt` respected). No drifted call ever
  goes to a real third-party API — the executor stays the local mock.
- Corpus coding is reproducible: the coder is a script over the archived files, not an ad-hoc read. Re-
  running it on the same archive must produce the same `corpus.jsonl` byte for byte.
- `HARD_STOP_USD = 50.00`; every catalog run passes `--cap`; the Phase-3 projection is ≤ $3.
- Temperature 0; `max_tokens` 700 (OpenRouter), 1024 (Gemini); Flash thinking `MINIMAL`; Claude at the
  provider default (Phase 2 amendment 2). Every OpenRouter call pins one provider, `allow_fallbacks: false`.
- Seeds: September `RNG`, Phase-1 `RNG_P1` and Phase-2 `RNG_P2` are untouched. Phase 3 uses
  `RNG_P3 = default_rng(<lock date as YYYYMMDD>)`. `N_BOOT = 10_000`, `N_PERM = 20_000`.
- **BH.** The corpus is descriptive and joins no family (it is prevalence, not a paired test). Catalog-arm
  tests join the one family: 301 + the count fixed in the Task-1 lock. Phase-1 and Phase-2 verdicts stay
  on their own families (194, 301), as before.
- Commits `<type>: <description>` with no attribution trailer (user setting).
- New modules: functions < 50 lines, files < 400 lines, inputs never mutated, ≥ 80% line coverage.

## Review Focus

1. **The corpus measures the collector, not the world.** A changelog that lists every patch release will
   swamp one that summarises quarterly. Expected: the per-source cap (D2) plus a per-source count in the
   report; prevalence is reported per source *and* pooled, and the pooled figure is called out as
   source-weighted. (Tasks 1, 5)
2. **"Would an agent pass this parameter?" is where bias enters.** Expected: `agent_visible` is decided by
   a rule that does not look at the drift class — required in v1 or v2, **or** present in the source's own
   example request for that endpoint — and the blind second pass re-codes it too. (Tasks 1, 3, 4)
3. **A real change is often two changes.** Renaming a parameter and tightening its enum in one release is
   not one of the five classes. Expected: `compound` is a pre-registered label, not a judgement call, and
   its share is reported (it is also the motivation for the compound-drift plan). (Task 1)
4. **Fetched HTML is attacker-controlled text.** Expected: the archive directory holds only data, the
   coder takes the path as an argument, and nothing in `results/phase3/sources/` is importable. (Task 2)
5. **The catalog arm changes two things at once** — more tools *and* a different testbed — so its numbers
   are not comparable to the 120 pairs. Expected: the catalog testbed contains the six SchemaDrift tools
   unchanged plus distractors, and the arm runs a `catalog_small` control (the same pairs, six tools) so
   the catalog-size effect is a within-testbed paired difference. (Tasks 6, 9)

---

## Budget, streams and order

| Stream | Work | Estimate |
|---|---|---|
| Corpus: fetch + archive | ~4 sources, one window | $0 |
| Corpus: code + blind second pass | 120–200 units, Codex second pass | $0 from this budget |
| Catalog testbed | 100+ declarations, new hash | $0 |
| Catalog arm, Flash | 48 pairs × (A, B_strict, C) × 2 catalog sizes = 288 | ≈ $1.5 |
| Catalog arm, Haiku | same 288 | ≈ $0.3 |
| **Total** | | **≈ $2**, cumulative ≈ $22 of $50 |

Token note: the catalog arm's cost is driven by the declarations in the prompt, not the replies — 100
tools is roughly 8k input tokens per call against ~450 today. The pilot rechecks this before the full run.

```
T0 decisions → T1 pre-registration (the lock) → T2 fetch + archive → T3 coder → T4 blind pass → T5 corpus block
                                              └→ T6 catalog testbed → T7 runner + gates → T8 pilot + run → T9 catalog analysis
T5, T9 → T10 results
```

---

### Task 0: Decisions (needs the user; no code)

- [ ] The user answers D1–D3.
- [ ] If D1 includes the catalog arm, confirm the two families (recommended Flash + Haiku: one Gemini, one
      Anthropic, both already priced and both known to follow diffs, so a drop is about the catalog).
- [ ] Done when: a dated "Phase 3 run log" line in `MILESTONES.md` records the answers.

### Task 1: Pre-registration (the lock; committed before any fetch or model call)

- [ ] `MILESTONES.md` → "Phase 3 pre-registration — LOCKED <date>", written before Task 2 runs.
- [ ] **Corpus frame.** The source list and the exact entry point for each, the window, the unit of
      analysis (one parameter-level change to one endpoint/tool; an entry that changes two parameters is
      two units), the enumeration order, the per-source cap and the stopping rule.
- [ ] **Inclusion.** A unit qualifies when a *request* parameter of an existing endpoint/tool changes its
      name, type, allowed values, requiredness, or default. Excluded: response-only changes, brand-new
      endpoints, pure documentation wording, deprecation notices with no effective change inside the window.
- [ ] **Labels (mutually exclusive, pre-registered):** `rename`, `enum_tighten`, `required`,
      `type_change`, `default_change`, `compound` (two or more of the five on the same parameter in one
      release), `other`.
- [ ] **`agent_visible` rule:** true when the parameter is required before or after the change, or appears
      in the source's own example request for that endpoint. Decided without looking at the label.
- [ ] **Reliability:** second pass by the D3 method over the whole corpus; report raw agreement and
      Cohen's kappa; pre-register the threshold (raw ≥ 0.90) and what happens below it (the coding rule is
      fixed and both passes re-run before any prevalence number is quoted).
- [ ] **Predictions, numbered from P17** (the exact set is written at lock time; the intended shape):
      P17 coverage — the five classes plus `compound` cover ≥ 70% of qualifying units;
      P18 the costly classes — `required` + `default_change` ≥ 20% of units;
      P19 reach — ≥ 50% of units are `agent_visible`;
      P20 compound — `compound` ≥ 10% (this is what would justify the compound-drift plan);
      P21 catalog (if D1 includes it) — for each family, C success in the 100-tool catalog is within 0.10
      of C success in the 6-tool control on the same pairs, paired, CI inside ±0.10.
- [ ] **BH:** corpus predictions are descriptive and join no family; the catalog arm's tests and their
      labels (`p3:`) are listed with the new family total.
- [ ] Done when: the lock is committed; `git log` shows it before the first file in `results/phase3/`.

### Task 2: Fetch and archive ($0)

- [ ] `phase3/fetch_sources.py`: for each pre-registered source, GET the entry point and the entries in the
      window, write each response verbatim to `results/phase3/sources/<source>/<nnn>-<slug>.html` (or
      `.json`/`.patch`), plus a `manifest.json` per source with URL, fetch time, HTTP status and sha256.
- [ ] Resume-safe (an existing file with a matching sha256 is not re-fetched), rate-limited ≥ 1 s,
      `robots.txt` checked, no credentials.
- [ ] Tests: manifest round-trip, resume skips, a refusal path when `robots.txt` disallows, and a check
      that nothing outside `results/phase3/sources/` is written.
- [ ] Done when: the archive exists, the manifest hashes verify, and a dated run-log line records the
      source counts.

### Task 3: Coder → `results/phase3/corpus.jsonl` ($0)

- [ ] `phase3/code_changes.py`: reads the archive (path given as an argument), emits one record per unit:
      source, entry id/URL, date, endpoint/tool, parameter, v1→v2 description, `label`, `agent_visible`,
      the quoted evidence span, and the rule clause that decided the label.
- [ ] Deterministic: the same archive gives the same file byte for byte (sorted, stable ids).
- [ ] Tests on fixture pages (hand-written, in `phase3/fixtures/`, not fetched): one unit per label, an
      entry yielding two units, an excluded entry, and a `compound` case.
- [ ] Done when: `corpus.jsonl` is committed with its unit count per source and per label.

### Task 4: Blind second pass and agreement ($0 from this budget)

- [ ] Build a blind copy of the corpus (evidence spans only, no `label`, no `agent_visible`, no rule
      clause) the way `audit_sample.py` builds the Phase-2 reading copy, and verify the committed copy
      carries no labels.
- [ ] Second pass by the D3 method; raw answers archived under `results/phase3/`.
- [ ] `phase3/agreement.py`: raw agreement, Cohen's kappa, per-label confusion, disagreement list.
- [ ] Below the threshold: fix the coding rule, re-run both passes, and say so in the results section.
- [ ] Done when: agreement is committed and the user has read the disagreements.

### Task 5: Corpus block in `analysis.json` ($0)

- [ ] `experiments/analyze_phase3.py`, wired into `analyze.main` the way `analyze_phase2` is (never
      imported by it), under `RNG_P3`; a `--phase3-dir` flag; an empty dir must leave the file
      byte-identical to the committed `analysis.json`.
- [ ] Block: counts and shares per label, per source and pooled, with bootstrap CIs on the shares;
      `agent_visible` share overall and per label; the agreement figures; P17–P20 verdicts in the
      `{"holds": True|False|None, "basis": str}` shape of `phase2_stats`.
- [ ] Tests: a fixture corpus, the empty-dir invariance, and the verdict functions as pure functions.
- [ ] Done when: `analyze.py` run twice gives the same hash and the Phase-1/Phase-2 blocks do not move.

### Task 6: Catalog testbed (only if D1 includes the catalog arm; $0)

- [ ] `phase3/build_catalog.py`: the six frozen SchemaDrift tools **unchanged**, plus distractor tools from
      the existing domain generators until the catalog holds 100 (and a `catalog_small` view with the six
      only). Writes `phase3/catalog_frozen.json` with its own sha256 recorded in `MILESTONES.md`.
- [ ] Distractors never collide with a frozen tool's name or parameter names; the drifted tool's position
      in the catalog is drawn once from `RNG_P3` and fixed in the file.
- [ ] Tests: hash stability, no name collisions, the six frozen tools byte-identical to `testbed_frozen.json`.

### Task 7: Catalog arm — conditions, runner, gates

- [ ] A `catalog` arm in a `phase3_grid.py` with job keys `(task, cond, class, catalog_size, rep)`;
      conditions A, B_strict, C assembled in `harness.py` only, reading the catalog file.
- [ ] Reuse `run_gemini.py` / `run_openrouter.py` unchanged; records carry the catalog sha256, the catalog
      size and the drifted tool's index.
- [ ] `check_phase1_logs.py --phase 3`: coverage, one provider per file, ≤ 5% truncation per cell, and a
      new check that every episode saw the pre-registered catalog hash.
- [ ] Tests mirror `test_phase2.py`.

### Task 8: Catalog pilot and full run (spends; needs the user's go-ahead)

- [ ] `--limit 5` per family first; gates must PASS with `--pilot`; re-project the cost from pilot usage
      and stop for the user if the projection exceeds $5.
- [ ] Full run, resume-safe, one file per model under `results/phase3/`; every arm gated before analysis.
- [ ] A dated run-log line records episodes, spend, interruptions and any deviation.

### Task 9: Catalog analysis

- [ ] Paired, within-testbed: 100-tool minus 6-tool on the same pairs, per condition and per family; the
      P21 verdict; the tests join the BH family with `p3:` labels.
- [ ] Report the no-call and wrong-tool rates separately — in a 100-tool catalog, "called the wrong tool"
      is a failure mode the 6-tool grid could barely show.

### Task 10: Results and records

- [ ] `analyze.py` twice, identical hash; `models`, `token_costs`, `phase1` and `phase2` unchanged
      against `a8971be`.
- [ ] `MILESTONES.md` "Phase 3 results — <date>": P17–P21 copied from `analysis.json`, prevalence per
      source and pooled, reversals stated plainly, deviations, spend. `HANDOFF.md` progress row and family
      size; `viz/README.md` family size.
- [ ] Full test suite; commit `feat: Phase-3 results`; report to the user in the Phase-1 format.

---

## After Phase 3 (each phase gets its own plan when it starts)

- **Compound drift** (Phase-2 decision D2) and **longer multi-turn** each still need their own testbed and
  their own plan. P20 is the number that says whether the compound plan is worth the money.
- **Phase 4** rebuilds outputs in one order only: `analysis.json` → figures → site → film.
  `figures/build_figures.py` hard-codes the four September models (lines 21, 58, 142); the explorer
  (`docs/explorer/data.js`) is still the September bundle (`n_records` 4800, four models).
