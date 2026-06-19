---
id: "doc:session-summary-2026-06-19"
title: "Session summary & review handoff — 2026-06-19 (menopause→PAIS depth thread)"
created: "2026-06-19"
updated: "2026-06-19"
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - task:t016
---

# Session Summary & Review Handoff — 2026-06-19

## Objective

Execute the menopause / reproductive-stage → PAIS causal thread end-to-end as the
project's first depth-first push (chosen over breadth in the next-steps analysis),
turning hypothesis `h0005` into a falsifiable, pre-registerable artifact and
exercising the causal-inference + literature tooling.

## What we did (in order) and the artifacts produced

| Step | Action | Primary artifact(s) |
|---|---|---|
| 1 | **t014 — causal DAG** built (13 vars, 31 `causes` edges) | `entities/patches/menopause-pais-causal-dag.md` + 14 concept entities; `doc/inquiries/menopause-pais-causal-dag.md`; diagram `doc/inquiries/assets/*` |
| 2 | **t014 — adversarial critique** (pgmpy back-door analysis) | `doc/inquiries/menopause-pais-causal-dag-critique.md` |
| 3 | **t022 — knowledge graph** materialized (4,286 triples) | `knowledge/graph.trig`, `composite.trig` |
| 4 | **t016 — analysis plan** (design-stage, pre-registerable) | `entities/plans/2026-06-19-menopause-pais-total-effect-analysis-plan.md` |
| 5 | **t002 — case-definition heterogeneity** synthesis | `entities/topics/pais-case-definition-heterogeneity.md`; questions `0014`, `0015` |
| 6 | **t024 — case-definition crosswalk** of all 71 papers | `doc/meta/2026-06-19-case-definition-crosswalk.{md,tsv}` |
| 7 | **t015 — cohort search** (outside the corpus) | `doc/searches/2026-06-19-hormone-menopause-pais-cohorts.{md,json}`; stubs `AlcaldeHerraiz2025`, `Pollack2023` |

**Commits this session (6, all on `main`, `science validate` PASSES at each):**
`8a433df` (graph/tasks) → `d442f27` (t016 plan) → `aff11d5` (t002) → `4240e4e`
(t024) → `8383290` (t015). (Plus the earlier t014/critique commits.)

## Key findings & claims (load-bearing — please scrutinize)

1. **The total effect is NOT identifiable by adjustment** while unmeasured
   confounders U (SES, prior EBV, genetic/HLA, behaviour) are latent. pgmpy
   confirmed: no covariate set recovers it. The design is therefore explicitly
   partial-identification (E-value bounding + U-proxies), not point estimation.

2. **The originally-locked adjustment set was wrong and was corrected.** The draft
   pre-declared adjust `{age + baseline comorbidity}`. pgmpy showed comorbidity is
   **not** a back-door confounder of the *total* effect (it isn't a parent of
   menopause) → over-adjustment / M-bias. **Corrected minimal set: `{age}`** under
   natal-female restriction.

3. **Clinic-attendance is a confirmed collider.** Post-COVID-clinic cohorts
   condition on it by construction (Stewart2024 exemplar) → manufactured
   association. This drives a hard sample-admissibility gate, not a covariate.

4. **Case definitions dominate cross-study variation (t002/t024).** Of 35 primary
   cohort studies, only **9** use a named standard definition (17 author-defined,
   18 incl. the mixed RECOVER+author row; the all-corpus author-defined count is 22);
   **PEM is a *required* criterion in just 3/71 papers** (the TSV codes
   `pem_required` — a study may measure PEM without requiring it); time thresholds
   scatter ≥4wk→≥6mo;
   **20/35 primary studies are high clinic-collider risk** (only 3 low, all
   male/registry). Recommended t016 outcome: **WHO-2021 ≥3mo + RECOVER PASC-index
   PEM weighting**, run under a 3-definition sensitivity axis.

5. **The imported corpus has ZERO admissible cohort for t016 (t024), and the
   admissible vehicle lives outside it (t015): UK Biobank.** It is the only
   population-based, low-collider, pre-infection-baseline (2006–2010),
   female-inclusive, menopause-staged resource. **Decisive caveat:** baseline
   oestradiol is censored by a 175 pmol/L assay floor → the treatment node must be
   **questionnaire reproductive stage** (± testosterone/SHBG), which *confirms* the
   DAG's choice and routes exposure error to t020. Triangulate with All of Us /
   Lifelines / Generation Scotland. No prior study has run this causal analysis
   with a pre-infection baseline in UKB/Lifelines.

**Net trajectory:** t016 moved from `not-ready` (no cohort) → vehicle resolved
(UKB), case-definition resolved (t002), with only two schema gates left (t017
U-proxy schema, t020 staging misclassification) before `/science:pre-register`.

## Decisions / corrections made this session

- Adjustment set corrected to `{age}` (see finding 2).
- Outcome case definition set to WHO≥3mo + PASC-index with 3-arm sensitivity.
- Treatment operationalized as questionnaire reproductive stage (not serum estradiol).
- Tasks: closed **t002, t014, t015, t022, t024**; created **t023, t024, t025,
  t026, t027**; marked **t016** in_progress; sharpened **t015** then closed it.

## Review targets — where to look hardest

These are the spots most worth an independent check:

1. **The pgmpy identifiability result was run OUT-OF-BAND.** `science inquiry
   export-pgmpy` emitted an empty edge list (tooling bug `fb-2026-06-19-001`:
   causal edges land in the per-inquiry named graph, not `graph/causal`), so the
   back-door analysis was run by hand on the authored edge list. **Re-derive the
   adjustment set independently from `entities/patches/menopause-pais-causal-dag.md`
   to confirm `{age}` (and the non-identifiability) — this is the linchpin claim.**

2. **The DAG edge set itself is uncurated** (`unknown`/`none` on the two-axis
   evidence model). The critique already flags missing edges (comorbidity→menopause
   timing, hospitalization collider, calendar/variant) deferred to DAG v2 (t023).
   Check whether any *missing* edge would change the `{age}`-only conclusion (the
   comorbidity→menopause-timing edge specifically would reintroduce comorbidity as
   a confounder — this is the known fragility).

3. **t024 crosswalk was extracted by 6 parallel subagents** reading the entity
   summaries (not the source PDFs). The per-paper codings (case definition, PEM,
   collider risk, admissibility) are judgment calls from secondary summaries —
   spot-check a few rows in `doc/meta/2026-06-19-case-definition-crosswalk.tsv`
   against the actual paper entities. One known fix: batch B4 initially dropped the
   `t001_admissible` column for ~5 rows; I reconstructed those from its summary.

4. **t015 cohort-capability fields are web-sourced and some are `[UNVERIFIED]`**
   (e.g. All of Us per-analyte hormone-lab N; MGB menopause field; NAPKON female
   fraction). The UK Biobank oestradiol-floor claim (175 pmol/L) and field IDs
   should be confirmed against the UKB Showcase before t027 builds the data spec.
   Citations were verified during search but the two new paper notes
   (`AlcaldeHerraiz2025`, `Pollack2023`) are **UNREAD stubs** — not yet read.

5. **Citation/DOI integrity:** new refs added to `papers/references.bib`
   (AlcaldeHerraiz2025, Pollack2023, Ballering2022, Lott2022, TinTin2021). Author
   lists are partial (`others`) — verify before any external use.

6. **Validator gap (non-blocking):** `entities/meta/0001-next-steps-2026-06-19.md`
   is `type: meta`, which the graph build warns is an unregistered kind in this
   project's profile. Pre-existing; flagged, not fixed.

## Open / next

- **t027** (P1) — draft the UKB data-field specification (field IDs enumerated in
  the task) → then t017, t020 → `/science:pre-register`.
- Breadth gaps still open: **t005** (PEM/mitochondrial), **t004** (therapeutics),
  **t001** (now partially unblocked: definition-stratified within long-COVID only).
- **t025** (PEM+ vs PEM−) confirmed un-serveable by the current corpus.
