---
id: question:0017-deflationary-alternatives-vs-shared-pathophysiology
kind: question
title: Are deflationary alternatives better supported than a shared post-infectious pathophysiology?
status: active
ontology_terms: []
datasets: []
source_refs: []
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- discussion:0002-cross-pathogen-pais-signature-convergence
- pre-registration:0002-cross-trigger-pathway-overlap
- interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
- search:0005-pre-infection-baseline-longitudinal-cohorts
required_capabilities:
- data_product: data-product:gene-expression
  qualifiers: {}
created: "2026-06-20"
updated: "2026-06-21"
---
# Are deflationary alternatives better supported than a shared post-infectious pathophysiology?

## Summary

The project's positive hypotheses (especially `hypothesis:0001` shared dysregulated attractor and
`hypothesis:0006` skeletal-muscle PEM) each have to outcompete a set of **deflationary alternatives** —
explanations under which the post-infectious phenotype, and the apparent *cross-trigger convergence*,
require no shared post-infectious pathophysiology at all. This question makes that skeptical null
**bundle** a first-class, tracked entity rather than scattered "disputing evidence" bullets, so that
each positive claim is scored against it explicitly. Five deflationary accounts are tracked:

1. **Finite-organ-failure-repertoire coincidence** (rival to `hypothesis:0001`). Distinct triggers
   converge only *symptomatically* — there is a small repertoire of ways the body expresses chronic
   illness — not via a shared molecular/physiological attractor.
2. **Detection / ascertainment artifact.** Cross-pathogen "convergence" is manufactured by
   case-definition heterogeneity and shared symptom checklists; sicker or more-surveilled populations
   generate spurious associations. (Bridges to `question:0014`, `question:0015`.)
3. **Deconditioning / physical inactivity.** Fatigue and exercise intolerance are secondary to
   detraining, not a primary post-infectious lesion.
4. **Psychological / nocebo / illness-perception perpetuation.** Symptoms are perpetuated by
   expectation, attention, and symptom-focused behaviour rather than ongoing biology.
5. **Reverse causation.** Measured "markers" or "exposures" are consequences of established chronic
   illness (or of its behavioural sequelae), not upstream causes.

## Why It Matters

- **Decision it affects:** whether positive cross-syndrome and mechanistic claims are *promoted* or
  held. A shared-mechanism program (shared-mechanism therapeutics, cross-trigger biomarker transfer)
  is only justified if it outcompetes these nulls; conflating symptom overlap with biological
  equivalence is the exact trap the project guide and `discussion:0002` warn against.
- **Risk if left implicit:** a project whose thesis is "shared failure mode" is structurally exposed to
  confirmation bias. Without the deflationary bundle on record *with its counter-evidence*, weak
  convergence reads as support. This is the standing companion to `/science:bias-audit`.
- **Discriminating value:** naming each alternative forces the question "what observation would
  separate shared pathophysiology from *this* deflationary account?" — sharpening study design
  (e.g. the ≥3-trigger harmonized test; PEM-stratified omics; pre-baseline temporal ordering).

## Current Evidence

- **Against deconditioning as primary:** Appelman2024 (skeletal-muscle pathology and exercise-induced
  myopathic change on biopsy after exertion) and invasive/2-day CPET (Joseph2023) show peripheral
  O₂-extraction and bioenergetic deficits not explained by detraining; reproducible post-exertional
  decline argues for a lesion, not disuse. (See `hypothesis:0006`, `question:0011`.)
- **Against pure nocebo/psychogenic:** objective, partly trigger-shared biology — RANTES/CCL5 across
  two viral triggers (Raijmakers2025), functional autoantibodies (`question:0009`), oxidative-stress /
  mitochondrial signatures (Shankar2025; `question:0016`) — is hard to reconcile with a purely
  expectation-driven account. Hold as a possible *subgroup* contributor, not a whole-syndrome
  explanation; do not dismiss outright (covariate-sensitive, contested literature).
- **Supporting finite-repertoire coincidence (the strongest live deflationary account):** head-to-head
  molecular designs *uniformly fail* to demonstrate a shared positive signature (Galbraith2011: zero
  genes consistent across EBV/RRV/Q-fever; Patterson2024 separates long COVID from chronic Lyme;
  Raijmakers2021 only a shared *negative*). No harmonized ≥3-trigger multi-omics with full-recovery
  controls exists. Convergence is currently demonstrable at *pathway/physiology* level, not shared
  analytes — exactly what coincidence-of-repertoire predicts. Counter: the few genuine shared signals
  (RANTES; terminal-NK, Sommen2026; oxidative stress, Shankar2025) are early exceptions.
- **Supporting ascertainment artifact:** the provenance problem — ~94% of the cross-trigger literature
  fails a case-definition bar (Raijmakers2025), and definitions yield only 61–79% within-cohort
  concordance (`question:0014`) — means apparent convergence may track definition choice, not biology.
- **Reverse causation** is live but partly mitigated in the menopause arm by *pre-infection baseline*
  temporal ordering (UKB reproductive stage fixed 2006–2010; `hypothesis:0005`, `discussion:0001`);
  it remains unaddressed for cross-sectional molecular findings.
- **t008 pre-infection-baseline cohort audit (2026-06-25; `search:0005`) clarifies the design
  hierarchy.** Lifelines (`paper:Ballering2022`) is the benchmark for attributable symptom excess
  because it models pre-infection symptoms and matched uninfected symptom dynamics; UK Biobank
  repeat imaging (`paper:Douaud2022`) is the benchmark for objective pre/post endpoint change.
  UKB/WHI risk-factor papers (`paper:AlcaldeHerraiz2025`, `paper:Neuhouser2024`, `paper:Ng2025`)
  constrain temporal ordering for broad pre-pandemic predictors, while RECOVER remains stronger
  for post-acute phenotype/mechanism discovery than for pre-infection causal ordering. Net:
  reverse causation is no longer a generic complaint; it should be scored by baseline type.
- **t035 cross-trigger pathway-overlap reanalysis (2026-06-21; `interpretation:0001-...`) — NO update
  to the deflationary bundle.** The first empirical probe of the finite-repertoire-coincidence rival
  (PI-CFS × Q-fever-fatigue NES rank-concordance, GSE14577 + GSE130353) returned `null_nonarbitrating`
  (C1 p_perm = 0.949 ≥ α). By the **pre-committed asymmetry** in `pre-registration:0002`, absence of
  detectable concordance here is **not** evidence *for* the coincidence null — it neither strengthens
  nor weakens this bundle; it enters only as *"existing public data cannot adjudicate."* A descriptive
  (non-arbitrating, steps 3–7 unreached) lean was noted — the few mitochondrial/OXPHOS sets surviving
  on Reactome/GO-BP classify as `exposure_sequela` (S2-positive in QS-vs-HC), consistent with the
  Raijmakers2019 exposure-confounding account — but it is **not** recorded as support for ascertainment/
  exposure-artifact, because the confirmatory test never reached the specificity steps. The discriminating
  experiment (harmonized ≥3-trigger multi-omics) still does not exist; this run is the empirical evidence
  that public 2-cohort pairings cannot substitute for it.

## Thoughts

- **Best current interpretation:** the deflationary bundle is not uniformly weak. Nocebo and
  deconditioning are substantially *constrained* by biopsy/physiology evidence; **finite-repertoire
  coincidence and ascertainment artifact remain genuinely competitive** with `hypothesis:0001` and are
  the accounts the project's own evidence most struggles to exclude. The honest present position is
  that cross-trigger convergence is supported at the level of biological *domains/pathways* but not yet
  at shared molecules, which is consistent with *both* a real shared attractor and a
  coincidence-of-repertoire null.
- **Major uncertainty:** the discriminating experiment (harmonized ≥3-trigger multi-omics with
  full-recovery controls, definition held constant) does not exist; until it does, shared-mechanism
  claims should be held at pathway level and explicitly scored against this bundle.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (finite-repertoire rival),
  `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` (deconditioning/nocebo/central rivals).
- Required data or analyses: the ≥3-trigger harmonized test (cf. t035 pathway-overlap step as a
  first, exploratory move); PEM-stratified omics (`question:0015`); definition-held-constant
  re-analysis (`question:0014`). Run as a recurring scoring step inside `/science:bias-audit`.
- Priority level: P2 — a standing skeptical audit that gates promotion of the project's core thesis.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:mecfs-long-covid-convergence`.
- Article notes: Galbraith2011, Raijmakers2025, Raijmakers2021, Patterson2024, Appelman2024,
  Joseph2023, Shankar2025, Sommen2026.
- Methods/Datasets: case-definition crosswalk (`doc/meta/2026-06-19-case-definition-crosswalk.md`);
  cross-trigger GEO sets (`doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md`).
