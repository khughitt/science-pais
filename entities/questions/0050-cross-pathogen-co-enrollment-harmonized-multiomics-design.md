---
id: question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
kind: question
title: Prospective cross-pathogen co-enrollment design with harmonized multi-omic
  protocols to distinguish shared from trigger-specific PAIS mechanisms
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Trautmann2025
- cite:Thomas2026
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0001-shared-molecular-signature-across-triggers
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
required_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    cohort_design: case-control
created: '2026-07-06'
updated: '2026-07-07'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-cross-pathogen-harmonized-design
lens_views:
- lens: methodology
  rationale: Whether PAIS syndromes share pathophysiology or merely phenotype is methodologically
    unanswerable with existing designs, because every syndrome-specific cohort uses
    different biomarker panels, time windows, and inclusion criteria. A co-enrollment
    harmonized design is the only approach that puts comparable molecular data on
    the same analytical footing across triggers. This is a study-design (not analysis)
    proposal serving the project's central question:0001; the MELLOW protocol shows
    harmonized cross-condition omics dense-sampling is technically feasible.
  origin_ref: explore-ideas-methodology
---
# Prospective cross-pathogen co-enrollment design with harmonized multi-omic protocols to distinguish shared from trigger-specific PAIS mechanisms

## Summary

Would a prospective multi-arm study **co-enrolling** patients 4–12 weeks after *serologically confirmed*
acute COVID-19, Lyme disease, influenza, EBV, and Q-fever — using **identical multi-omic sampling
protocols** and matched uninfected controls — be feasible, and would it produce molecular signatures
that finally resolve the shared-versus-trigger-specific mechanism question? This is the concrete design
form of the discriminating experiment the project repeatedly names but does not yet have: the
"harmonized ≥3-trigger multi-omics with full-recovery controls" that `hypothesis:0001` and
`question:0017` both hinge on.

## Why It Matters

- **Decision it affects:** whether such a study is *feasible* and worth prioritizing/funding — the crux
  is logistics and power, not desirability. It is the single experiment most able to adjudicate the
  project's core thesis (shared attractor, `hypothesis:0001`) against the finite-repertoire-coincidence
  and ascertainment-artifact nulls (`question:0017`).
- **Risk if unanswered:** the shared-vs-trigger-specific question stays unresolvable on the public,
  design-heterogeneous, 2-cohort data that has repeatedly returned non-arbitrating nulls (the t035
  pathway-overlap reanalysis, `interpretation:0001-...`). Shared-mechanism therapeutics and cross-trigger
  biomarker transfer cannot be justified until this design exists.

## Current Evidence

- **Supporting:** Trautmann2025 reviews shared and divergent PAIS features and explicitly notes that
  mechanistic comparison is limited by *incompatible study designs* — directly motivating a single
  harmonized protocol. Thomas2026 (the MELLOW dense-sampling multi-omic protocol for ME/CFS and long
  COVID) demonstrates that cross-condition harmonized omics is operationally feasible.
- **Conflicting / limiting:** co-enrolling five serologically-confirmed acute triggers within a common
  4–12 week window is a major recruitment and logistics challenge (incidence, timing, confirmation
  assays differ per pathogen); matched-control and power requirements are demanding; and the strong
  covariate sensitivity of PAIS (severity, age, sex, timing, prior immunity) must be designed in, not
  adjusted for post hoc.

## Thoughts

- **Best current interpretation:** feasibility — not scientific value — is the binding constraint; a
  staged design (start with the 2–3 highest-incidence, most-confirmable triggers) may be the realistic
  path to the ≥3-trigger bar.
- **Major uncertainty:** whether achievable sample sizes and harmonization would actually yield
  signatures that *separate* shared from trigger-specific biology, rather than another underpowered
  non-arbitrating result.
- **Feasibility gate RESOLVED (t103, 2026-07-07 → `interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility`):**
  **CONDITIONAL GO — staged.** The simultaneous 5-trigger single-site build is a **NO-GO** (Lyme is
  endemic/season-locked with early-serology insensitivity; Q-fever is outbreak-gated). The ≥3-trigger bar
  is reachable via a **Tier-1 COVID-19 + influenza + EBV** triad (year-round acute-care + student-health
  accrual), with Lyme (Tier 2, EM-clinical entry) and Q-fever (Tier 3, outbreak-gated) added
  opportunistically. Two design corrections are load-bearing: (a) primary control frame must be
  **full-recovery (infected-recovered) controls** per `hypothesis:0001`, not the "matched uninfected
  controls" written above; (b) confirmation is **per-arm SOPs** under one harmonized *omics* protocol, not
  a single common assay. Achievable N is *plausibly aligned with* the **shared pathway/latent-factor axis**
  (the level h0001 predicts) — but "adequately powered" is **not** yet established; that is the deliverable
  of the pending power/bias-floor simulation. Trigger-specific molecular discovery is wrong-sized at
  achievable N (exploratory-only). Harmonization's core value is
  removing the between-cohort **bias** ceiling that made the t035 public-data route non-arbitrating
  (`interpretation:0001`). Next gate: run the power/bias-floor simulation (interp-0001 "Q-A") before any
  cohort commitment.
- **Power/bias gate RESOLVED (t116, 2026-07-07 → `interpretation:0037-t116-power-bias-floor-shared-axis-sim`):**
  the design-power simulation (seeded with the t035 concordance dispersion) upgrades the "worth simulating"
  claim and **relocates the binding constraint away from per-arm N**. Findings: (a) the **mean-concordance
  statistic** (t035's) is *blind* to the `question:0017` finite-repertoire null — it clears the Monte-Carlo
  bar trivially (power 1.0) but adjudicates nothing (power ≈ 0 vs a strength-matched null); (b) any **2-arm**
  design is **structurally non-arbitrating at any N**; (c) the discriminating statistic is **structural** (is
  there one shared axis through all arms?), needs **K ≥ 3**, and per-arm N in the **tens (MELLOW-scale) is
  adequate** — N is not the lever; **arm count and feature-space resolution are**; (d) a **high-resolution
  feature universe (~1000 sets, Reactome/GO-BP-scale)** drops the required arm count from >6 (Hallmark-50) to
  **K=3**. Net for this design: fundable **with conditions** — commit to K≥3, a ~1000-set feature space, a
  structural single-factor confirmatory statistic (retire mean concordance), and full-recovery controls; the
  opportunistic Tier-2/Tier-3 arms (Lyme, Q-fever) become **power margin**, not garnish. A **fifth condition**
  surfaced by the t116 pipeline review (2026-07-07): the confirmatory statistic has **no protection against a
  *correlated* (shared) batch/platform artifact** — a common axis on every arm mimics a shared attractor and
  drives the false-"attractor" rate to ~0.9 at signal strength. So harmonization must control **cross-arm
  correlated bias specifically** (negative-control features, shared-artifact diagnostics, full-recovery-control
  contrasts), not just reduce per-arm bias magnitude. Pivotal remaining unknown: the real cross-PAIS repertoire
  **rank/lumpiness** (Q-C / task:t117), partly estimable from existing single-trigger multi-omics before any
  cohort commitment.
- **Q-C RESOLVED from data + "any N" scoped (t117, 2026-07-09 → `interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`).**
  The uniform cross-PAIS rank probe over the strict WB/PBMC matrix (7 columns across **3 triggers** — 5
  SARS-CoV-2/LC, 1 PI-ME/CFS, 1 Lyme) returns
  off-diagonal concordance **−0.064 (≤ sampling floor 0.033), SD 0.249** — a **diffuse/heterogeneous
  regime with no recoverable low-rank shared axis**, so Stage-3c calibration is fail-closed and no rank is
  placed on the t116 grid. This **confirms the low-power ceiling from real data**: the **public single-trigger
  route cannot settle the R regime and cannot substitute for the cohort** (the ceiling is signal-level at
  fixed trigger diversity, not fixable by adding more public deposits). **Scope correction (Key decision 5):**
  the earlier phrasing "structurally non-arbitrating **at any N**" applies exactly to **2-arm** designs and the
  **mean-concordance** statistic (undefined / blind by construction); the **high-rank finite-repertoire**
  non-arbitration is scoped to **achievable arm counts under this structural-test family (≤6 arms), not
  literally any N**. Net: the go/no-go stays **fundable-with-conditions**, now with real-data backing for the
  "public data cannot substitute for a K≥3 harmonized cohort" clause.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (the thesis under test);
  `question:0017-deflationary-alternatives-vs-shared-pathophysiology` (the null bundle it would score
  against); `question:0001-shared-molecular-signature-across-triggers` (the positive signature it seeks).
- Required datasets: a new prospective co-enrollment cohort; MELLOW/Trautmann anchor feasibility and
  design precedent.
- Required analyses: pre-registered shared-vs-trigger-specific signature test with full-recovery
  controls and a specified power/feasibility model.
- Priority level: P2 — the highest-leverage design question, gated on a feasibility assessment.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:mecfs-long-covid-convergence`.
- Article notes: Trautmann2025 (incompatible designs limit comparison), Thomas2026 (MELLOW harmonized
  multi-omics feasibility).
- Methods/Datasets: contrasts with public 2-cohort GEO pairings shown inadequate by the t035 reanalysis
  (`pre-registration:0002`, `interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating`).
