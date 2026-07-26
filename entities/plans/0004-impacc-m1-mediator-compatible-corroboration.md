---
kind: plan
id: plan:0004-impacc-m1-mediator-compatible-corroboration
title: "Scope (probe): IMPACC open-data mediator-compatible corroboration of h0005 M1 (t038)"
date: 2026-06-21
created: "2026-06-21"
updated: "2026-06-21"
status: active
related:
  - task:t038
  - report:0004-t036-hormone-panel-cohort-feasibility-m1-positive-test
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways
  - proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold
  - proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing
  - discussion:0001-menopause-timing-pais-rival-models
  - paper:Ozonoff2024
  - paper:Talla2023
  - paper:Shahbaz2025
  - paper:Silva2024
---

# Scope (probe): IMPACC open-data mediator-compatible corroboration of h0005 M1 (t038)

## Goal

Fix the bounded, **in-scope (pre-seed-stage)** literature-synthesis task for `task:t038`: judge whether
IMPACC's **already-published** steroid-axis and immune/metabolic mediator findings are *directionally
compatible* with M1's prediction that sex hormones modify post-infectious recovery through immune
mediators (`proposition:0002`). Pin the hard boundary against the deferred (post-seed-stage) fresh
re-analysis, and pre-commit which proposition a result may move.

## Background

`report:0004` ranked IMPACC **Tier 3** — a *mediator-compatible secondary corroboration*, the
cheapest / most-reproducible of three M1-corroboration paths. IMPACC already reports a sex-linked
androgen-metabolite long-COVID signal (DHEA-S, androsterone-sulfate, etc. **lower** in long COVID)
inside deep longitudinal immune multi-omics. M1's mechanism leg (`proposition:0002`) is **single-line
fragile** — two weak lines only (`evidence-line:0006` Averyanova2022, analogical; `evidence-line:0007`
Shahbaz2025, cross-sectional). A genuinely independent third cohort showing the same androgen↔
inflammation direction would bear on P2. But IMPACC has **no quantitative hormone panel (E2/FSH/AMH),
no reproductive/menopausal staging, no pre-infection baseline, and a hospitalized-severity skew**, so
it can **neither confirm the hormone→recovery direction nor resolve the P3 reverse-causation rival**
(`proposition:0003`). This scope exists to keep the realized analysis honest to exactly that ceiling.

## Approach

Literature synthesis only — **no data download, no re-analysis**. Extract from IMPACC's *published*
outputs: (1) the reported direction/magnitude of the androgen-metabolite long-COVID association; (2)
the immune/metabolic mediator features that co-structure with it; (3) the cohort's sex/severity
composition, sampling timeline, and any age/menopause descriptors. Compare each against M1's predicted
direction — low androgen → reduced anti-inflammatory tone → higher inflammatory cytokines → worse
recovery (the `paper:Shahbaz2025` directional grounding). Classify concordant / discordant /
underdetermined, then map onto the proposition graph **at the correct evidence level only**.

## Inputs

- Existing IMPACC paper entities: `paper:Ozonoff2024` (PASC phenotypes / PROs / LCMM) and
  `paper:Talla2023` (inflammatory serum-protein long-COVID subcategory) — extend in place.
- IMPACC long-COVID multi-omics result (PMC12582403; *Nat. Commun.* s41467-023-44090-5) — the
  androgen-metabolite signal and its co-varying mediator set; add as a new entity only if distinct from
  the two above.
- IMPACC design paper (PMC8713959) — cohort composition, hospitalized-severity skew, sampling timeline.
- `report:0004` — the Tier-3 assessment that scoped this path.
- `proposition:0002` / `proposition:0001` / `proposition:0003` + `discussion:0001` §M1 — the predictions
  to test compatibility against.
- `paper:Shahbaz2025`, `paper:Silva2024` — the two existing cross-sectional androgen↔inflammation lines
  this would triangulate.

## Tasks

1. Work the IMPACC literature: `paper:Ozonoff2024` (PASC phenotypes/PROs) and `paper:Talla2023`
   (inflammatory serum-protein subcategory) **already exist** — update/extend those entities as needed,
   and add a **new** paper entity only if PMC12582403 (the androgen-metabolite multi-omics result) is
   distinct from both. Capture the androgen-metabolite **direction**, the co-varying mediator set, and
   the cohort sex/severity/timeline descriptors.
2. Build the compatibility comparison: tabulate IMPACC's reported androgen → mediator → outcome
   directions against M1's predicted directions; classify **concordant / discordant / underdetermined**.
   A `concordant` call requires a *single* reported phenotype / module / model in which the steroid-axis
   metabolite and the immune mediator co-vary — two separate LC-association statements do not qualify
   (→ `underdetermined`).
3. Assess independence + confounding: are IMPACC subjects genuinely disjoint from
   Silva2024/Shahbaz2025 (→ its **own** independence group), and does the hospitalized-severity
   HPG-suppression confound collapse its informativeness (androgen-low could be acute-illness-driven,
   not reproductive-stage-driven)?
4. Interpret onto the graph (`/science:interpret-results`, **conceptual mode**): attach a
   supporting/disputing evidence-line to `proposition:0002` **only**; explicitly leave
   `proposition:0001` (forward causal threshold) and `proposition:0003` (reverse rival) unmoved; verify
   `belief.fragile-single-line` behaviour after the update.
5. Record the synthesis as a `report` entity and update `proposition:0002`'s caveat to reflect the
   **realized** (not merely planned) triangulation; close `task:t038` with the verdict.

## Decision criteria

- **Concordant** — requires the published IMPACC result to show the androgen-metabolite signal **and**
  the immune/metabolic mediator signal **co-varying within the *same* phenotype / module / model /
  subject-stratum**, in the direction M1 predicts. Two separate long-COVID-association statements
  ("androgens lower in LC" *and*, independently, "mediators differ in LC") do **not** qualify — that is
  `underdetermined`. A qualifying concordant result adds a *third*, distinct-cohort **supporting**
  evidence-line to `proposition:0002`, with strength **capped at `weak`** (no quantitative hormone
  panel, no reproductive staging, no pre-infection baseline, hospitalized-severity skew — § Background),
  in **its own independence group** only if subjects are disjoint from Silva2024/Shahbaz2025. The cap is
  load-bearing: a `weak` third line **may not be scored above `evidence-line:0007` (Shahbaz
  cross-sectional)**; it may lift P2 off single-line-fragile only by *adding a line*, never by being
  stronger than the lines already present. Does **not** update `proposition:0001` or weaken
  `proposition:0003` — all three cross-sectional lines remain reverse-causation-symmetric. The
  hospitalized-severity confound rides along as a mandatory caveat.
- **Discordant** (opposite direction): a **disputing** line for `proposition:0002`; P2 stays fragile and
  the mechanism leg weakens.
- **Underdetermined** — covers (a) the **decoupled-reporting** case above (androgen and mediator signals
  reported separately, never shown to co-vary in one phenotype/module/model), (b) severity-confounded
  reads, and (c) sparse reporting that blocks a clean direction call: **no belief update**; record as
  navigation-only and close t038 with the negative scoping result. This is an acceptable — even
  expected — outcome and must not be massaged into a positive read.

## Validation

- Confirm IMPACC subjects are disjoint from Silva2024/Shahbaz2025 **before** assigning a new
  independence group; if they share design weakness but not subjects, that is *shared-design*, not
  *shared-source* — flag it, do not silently merge or split groups.
- Hold mediator sign conventions consistent across the comparison (lower androgen vs. higher cytokine).
- After interpret, re-run `science validate` / `science health`; confirm `proposition:0002` did **not**
  over-promote (no belief jump beyond a single added weak line) and that `proposition:0001` /
  `proposition:0003` are untouched.

## Out of scope (deferred, post-seed-stage)

- Any **fresh re-analysis** of released IMPACC multi-omic data (ImmPort SDY1760 / dbGaP phs002686) — a
  computational analysis, deferred per `entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md`.
- Any dataset-entity provisioning or staging for IMPACC.
- The reverse-causation-breaking and primary positive tests — those are `task:t039` (All of Us coverage
  query) and `task:t040` (RECOVER ancillary), **not** t038.

## Notes on plan scope

Probe-mode (1-page, ~1-day) because t038's in-scope portion is a bounded synthesis of already-published
results yielding a single qualitative compatibility verdict and a tightly-bounded graph update; the
heavy computational arm is explicitly deferred. Sizing this larger would re-import the very
re-analysis this scope deliberately excludes.
