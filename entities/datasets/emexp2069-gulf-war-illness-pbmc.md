---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:emexp2069-gulf-war-illness-pbmc
kind: dataset
title: E-MEXP-2069 — Gulf War Illness PBMC transcriptome (non-infectious specificity, WP4b — BUILT)
status: candidate
created: "2026-07-09"
updated: "2026-07-10"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: '2026-07-10'
  verified_by: agent (t117 WP4b build)
  source_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MEXP-2069
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: 'BUILT 2026-07-10: the 20 BASELINE (before-exercise) CEL files — 9 GWI (GWS-*A) + 11 controls (Con-*A) — staged individually (per-file locked sha256, 271 MB total) + the SDRF, then RMA-normalized and fed the pinned hgu133plus2.db (GPL570) harmonize + median collapse chain -> 20,338 Ensembl genes. RMA computed in PURE R (limma normexp bg + limma quantile + stats::medpolish) because affy/preprocessCore threaded C fails with pthread_create()=22 (EINVAL) on this host''s new glibc/kernel. The 3rd non-infectious column; lifts the reverse projection to full rank (r_eff=2).'
accessions:
- E-MEXP-2069
source_refs:
- https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MEXP-2069
ontology_terms:
- gulf-war-illness
- non-infectious
- pbmc
- microarray
- specificity-control
provided_capabilities:
- data_product: data-product:gene-expression-microarray
  qualifiers:
    cohort_design: case-control
    trigger: non-infectious-gulf-war-illness
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# E-MEXP-2069 — Gulf War Illness PBMC transcriptome (non-infectious specificity, WP4b — BUILT)

**BUILT specificity column for `task:t117`** (`status: candidate`, WP4b **3rd non-infectious column**,
staged + parsed 2026-07-10). The compartment-matched column that lifts the reverse projection to full rank
and disentangles the platform confound.

## What it is

Whistler et al. 2009 "Impaired immune function in Gulf War Illness" (BMC Med Genomics 2:12) — **9 GWI vs
11 Gulf-War-era control veterans**, PBMC, Affymetrix HG-U133 Plus 2.0, at three exercise timepoints (60
raw `.CEL` files); the baseline timepoint is a genuine case-vs-control arm. **Gulf War Illness is a
non-infectious (organophosphate/toxic-chemical) trigger** — a DIFFERENT non-infectious axis than
fibromyalgia, so it tests trigger-generality of any generic-sickness reading.

## Corpus role (t117 WP4b)

`matrix: specificity` — the **3rd non-infectious column** (with the flagship [[gse221921-fibromyalgia-pbmc]]
and [[gse67311-fibromyalgia-wholeblood]]), built through the same uniform DE→enrichment. Its value is being
**PBMC (compartment-matched to the flagship + the identifiable PAIS stratum)** yet an **independent
non-infectious TRIGGER** (organophosphate/chemical vs idiopathic FM) on an **independent microarray platform**
(GPL570 HG-U133 Plus 2.0). Smallest N in the panel (9 vs 11). The whole-genome human GWI blood universe is
effectively one US lab lineage (this + GSE286345/GSE168409, all Klimas/Broderick), so cross-dataset GWI
robustness is limited by design.

## Result (2026-07-10) — resolves the under-resolution; reveals a PLATFORM (not compartment) confound

- **Build:** 20 baseline CELs → pure-R RMA (limma normexp + limma quantile + `medpolish`; affy/preprocessCore
  threaded C is broken on this host, `pthread_create()=22`) → hgu133plus2.db/GPL570 harmonize (79.4% probes
  mapped) → median collapse → **20,338 genes, 9 GWI / 11 HC**. Expression-scale PASS, DE-eligible (~ group).
- **Reverse projection now FULL-RANK:** with the 3rd column, `r_eff = min(R=2, n_noninf−1=2) = 2 = PAIS R`
  (`identifiability_pass=true`), resolving the 2-column under-resolution ([[gse67311-fibromyalgia-wholeblood]]).
  Verdict **`noninfectious_axis_not_reproducible_indeterminate`**: the leave-one-non-infectious-out ceiling is
  LOW (0.053) — even across FM and GWI the non-infectious case-vs-control axis does **not** reproduce, so there
  is no coherent "generic non-infectious manifold" to test PAIS against (PAIS recovers U at 0.072 > ceiling,
  ratio 1.37).
- **Forward recovery disentangles the confound:** GWI (PBMC, microarray) recovers **0.213** — like the
  WB-microarray FM (0.234) and ~5× the PBMC-RNA-seq FM flagship (0.045). Since GWI is **PBMC** (same compartment
  as the flagship), the ~5× gap tracks **PLATFORM (microarray vs RNA-seq), NOT compartment/blood-composition**
  (the earlier 2-column reading) and NOT condition — a tiny-N (9v11) microarray column recovers high while a
  large-N (96v93) RNA-seq column does not. A technical (platform/enrichment-structure) confound on forward
  recovery.
