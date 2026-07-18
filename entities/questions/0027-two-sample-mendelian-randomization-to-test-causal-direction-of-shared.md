---
id: question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared
kind: question
title: Two-sample Mendelian randomization to test causal direction of shared PAIS
  mechanisms across triggers
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Feng2024
- cite:He2023
- cite:Pinero2025
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0001-shared-molecular-signature-across-triggers
- question:0022-immune-state-displacement-mediator-vs-co-traveler
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- theme:0003-demonstrability-ceiling-cross-pathogen-design
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- plan:0009-wave1-mr-hormone-pilot
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-mr-cross-trigger-causal-mechanisms
lens_views:
- lens: methodology
  rationale: 'Candidate mechanisms are largely observational and direction-ambiguous.
    MR uses germline variants as natural randomizations, giving causal inference robust
    to reverse causation and confounding; running instruments cross-trigger additionally
    tests which mechanisms are generic vs trigger-specific. Requires only public GWAS
    summary statistics. Directly serves question:0001 (shared vs trigger-specific)
    and question:0022 (mediator vs co-traveler).

    '
  origin_ref: explore-ideas-methodology
---
# Two-sample Mendelian randomization to test causal direction of shared PAIS mechanisms across triggers

## Summary

Two-sample Mendelian randomization (MR) uses germline genetic variants as instrumental variables to
test whether a proposed PAIS mechanism (autoimmune predisposition, inflammatory-cytokine signalling,
coagulation/fibrinolysis, gut-microbiome composition, mitochondrial-function markers) is *causally
upstream* of post-acute syndrome liability, with inference robust to reverse causation and unmeasured
confounding. The distinctive design move for this project is to run the same mechanism instruments
against **trigger-specific outcome GWAS** (long COVID, and — where they exist — post-Lyme,
post-sepsis), converting each mechanism into a per-trigger causal-support score that separates
*generic* from *trigger-specific* drivers. It requires only public GWAS summary statistics, making it
the most reproducible-tier causal vehicle in the `theme:0003` design set.

## Why It Matters

- **Decision it affects:** which candidate mechanisms deserve scarce experimental/cohort follow-up. A
  germline-liability mechanism with cross-trigger MR support is a stronger prior for the
  shared-attractor thesis (`hypothesis:0001`); and — **conditional on adequate power, valid instruments,
  and a matched-ancestry outcome** — a trigger-specific or null signal would argue against a single
  shared pathway. (An underpowered, ancestry-flagged screen's null does not: absence of a detectable
  effect there is uninformative, not evidence against.)
- **Serves** `question:0001` (shared vs trigger-specific) and `question:0022` (mediator vs
  co-traveller) by supplying a confounding-robust directionality test the observational corpus cannot.
- **Risk if unanswered:** the project keeps ranking mechanisms on association strength alone, unable to
  separate driver from downstream marker — exactly the ambiguity `hypothesis:0001`/`hypothesis:0009`
  turn on.

## Current Evidence

- **Single-trigger / single-mechanism exemplars exist; none is cross-trigger.** Feng2024 ran
  bidirectional two-sample MR between autoimmune diseases and long COVID (single trigger); He2023 ran
  two-sample MR of gut-microbiome taxa → ME/CFS (single syndrome, single mechanism class); Pinero2025
  used TWMR + eQTL + PPI for causal-gene discovery in long COVID. Each demonstrates the instrument→outcome
  step but none runs one instrument set across ≥2 PAIS triggers.
- **The project has already executed the vehicle, twice, and mapped its ceiling.** `plan:0007`
  (autoimmune/SLE → long COVID) and `plan:0009` (SHBG/testosterone → long COVID) were run end-to-end
  (IVW primary; MR-Egger/weighted-median), with `plan:0009` additionally applying MRlap sample-overlap
  correction (`plan:0007` left overlap correction explicitly out of scope). Both returned **no
  reportable signal** and — load-bearing — both are ancestry-flagged / non-primary (KD1) because **no
  matched EUR-only long-COVID outcome GWAS is publicly downloadable** (HGI DF4 deposits only
  multi-ancestry strata; the paper's EUR-only analysis was never deposited). That is a hard
  demonstrability ceiling on the outcome side, not a tunable parameter.

## Thoughts

- **Best current interpretation:** MR is admissible (public sumstats; D-005-authorised for the Wave-1
  pilot) and partially executed, but it is a *screening* instrument, not an adjudicator of the
  project's core claims. It tests **germline liability**, so it cannot identify an *acquired*
  post-infectious set-point shift — `hypothesis:0009`'s acquired-state conversion arrow is explicitly
  **not MR-identifiable** (KD6). Reverse-direction MR functions only as a shared-liability/directionality
  sensitivity, not a test of the acquired mechanism.
- **Major remaining uncertainty / binding constraints:** (1) the outcome vehicle — cross-trigger MR
  needs trigger-specific outcome GWAS, and post-Lyme / post-sepsis / post-dengue PAIS GWAS are
  essentially nonexistent, so "cross-trigger" currently collapses to "long COVID only"; (2)
  binary-exposure liability-scale R² and instrument-R² provenance must be recomputed per exposure (a
  survived power cell is provisional, per the project's power-screen discipline); (3) sample overlap
  with HGI requires MRlap correction; (4) any *new* exposure or a non-HGI outcome vehicle (e.g.
  FinnGen) is a fresh D-005/D-006 scope decision, not in-scope maintenance.
- **Priority:** P2 as a mechanism-screen, but scoped — it prioritises germline-liability mechanisms; it
  does not resolve `hypothesis:0001` vs the deflationary bundle.

## Connections to Project

- Related hypotheses: `hypothesis:0001` (shared attractor — MR screens its candidate drivers),
  `hypothesis:0009` (set-point shift — MR **cannot** identify the acquired arm, KD6).
- Related questions / theme: `question:0001`, `question:0022`; `theme:0003` (this is one of its named
  design vehicles).
- Prior project execution: `plan:0007`, `plan:0009` (Wave-1 MR pilots — the vehicle, its ancestry
  ceiling, and its null).
- Required datasets: public GWAS summary statistics (exposure instruments + trigger-specific outcome
  GWAS); an ancestry-matched downloadable long-COVID/PAIS outcome is the missing input.
- Required analyses: IVW primary + committed sensitivity checklist (MR-Egger, weighted-median, MRlap
  overlap correction, HLA-inclusive / broad-strict sensitivities).
- Priority level: P2 (screening), gated by D-005/D-006 for any new vehicle.

## Related

- Topic notes: `theme:0003-demonstrability-ceiling-cross-pathogen-design`.
- Article notes: `cite:Feng2024`, `cite:He2023`, `cite:Pinero2025`.
- Methods/Datasets: `plan:0007`, `plan:0009`; project MR stack (TwoSampleMR / MRlap / GenomicSEM / LDSC).

## Notes

- 2026-07-06: Run as a systematic screen across the full candidate-mechanism space (EBV-reactivation susceptibility, coagulation/fibrinolysis traits, anti-GPCR-autoantibody propensity, mitochondrial-function markers), assigning per-mechanism causal-genetic-support to prioritize experimental follow-up, and test cross-phenotype generalizability; design around infection-context MR pitfalls (collider bias, immune-locus pleiotropy). (explore-ideas 2026-07-06 · cand-methodology-two-sample-mr-pais-mechanisms; anchors in meta:explore-2026-07-06)