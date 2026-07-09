---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse67311-fibromyalgia-wholeblood
kind: dataset
title: GSE67311 — Fibromyalgia whole-blood transcriptome (non-infectious specificity, WP4b — BUILT)
status: candidate
created: '2026-07-09'
updated: '2026-07-09'
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
  last_reviewed: "2026-07-09"
  verified_by: "agent (t117 WP4b build)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67311
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "BUILT 2026-07-09: series matrix staged (sha256 959735bd…, 15.7 MB) and parsed through the prebuilt microarray chain (parse_series_matrix --exclude-title-regex '_2$' drops 14 technical replicates -> harmonize_microarray.R hugene11sttranscriptcluster.db=8.8.0 / GPL11532 -> collapse_probes.R median). 60 FM / 68 HC, 19,584 genes, expression-scale PASS, DE-eligible (~ group). The 2nd non-infectious column; activates the reverse projection."
accessions:
- GSE67311
ontology_terms:
- fibromyalgia
- non-infectious
- whole-blood
- microarray
- specificity-control
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: non-infectious-fibromyalgia
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE67311 — Fibromyalgia whole-blood transcriptome (non-infectious specificity, WP4b — BUILT)

**BUILT specificity column for `task:t117`** (`status: candidate`, WP4b **2nd non-infectious column**,
staged + parsed 2026-07-09). The column that activates the reverse projection.

## What it is

The reference **fibromyalgia whole-blood** bulk gene-expression set: "Peripheral Blood Gene Expression in
Fibromyalgia Patients…" — deposited as **70 FM vs 70 healthy controls**, PAXgene whole blood, Affymetrix
Human Gene 1.1 ST array (GPL11532). Non-infectious (idiopathic) trigger. **As built:** the series matrix
carries RMA-normalized log2 (embedded), group from the `diagnosis` characteristic; after dropping 14 `_2`
technical-replicate samples the analysed set is **60 FM / 68 HC** (128 samples, 19,584 genes).

## Corpus role (t117 WP4b)

`matrix: specificity` — the **2nd non-infectious column** (with the flagship [[gse221921-fibromyalgia-pbmc]]),
built through the same uniform DE→enrichment. Its value is orthogonal axes: **independent whole-blood** (vs
the flagship's PBMC) **and independent microarray platform** (vs NovaSeq RNA-seq).

## Result (2026-07-09) — a confound, not a clean replication

- **Forward** (project the FM column onto the PAIS subspace): recovery **0.234** (0.965× the trigger-LOO
  ceiling) → `recovered_like_pais_generic_manifold_consistent` — but the PBMC-FM flagship recovers only
  **0.045**. A **~5× same-condition gap that tracks compartment/platform** (WB-microarray vs PBMC-RNAseq).
  Since the strict PAIS corpus is 5 PBMC + 2 whole-blood, the WB-FM's high recovery is plausibly shared
  **blood composition**, not FM biology — a **compartment/platform confound**, not a validation.
- **Reverse** (build U from the 2 FM columns, project PAIS): the two FM cohorts' case-vs-control axes barely
  agree (leave-one-out 0.039), and with only 2 columns the reverse test is **under-resolved** (r_eff=1 <
  PAIS R=2) → verdict `under_resolved_need_more_noninfectious_columns`. A **3rd+ cross-condition,
  compartment-matched** column ([[emexp2069-gulf-war-illness-pbmc]], [[gse182503-iei-pbmc]]) is required.
