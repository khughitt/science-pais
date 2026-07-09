---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse286345-gulf-war-illness-pbmc
kind: dataset
title: GSE286345 — Gulf War Illness PBMC RNA-seq (non-infectious specificity, WP4b queued/pending)
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
  verification_method: landing-confirmed
  last_reviewed: "2026-07-09"
  verified_by: "agent (t117 WP4b sweep)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE286345
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample normalized-count CSV (GSE286345_norm_counts_STAR_GWI_FM.csv.gz) + raw reads SRA PRJNA1208952. Staging DEFERRED and admissible_PENDING: the supplementary file is named ..._GWI_FM — RESOLVE whether it co-carries fibromyalgia samples (and disentangle) before building, else the GWI arm is contaminated."
accessions:
- GSE286345
- PRJNA1208952
ontology_terms:
- gulf-war-illness
- non-infectious
- pbmc
- rna-seq
- specificity-control
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: non-infectious-gulf-war-illness
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE286345 — Gulf War Illness PBMC RNA-seq (non-infectious specificity, WP4b queued/pending)

**Candidate dataset for `task:t117`** (`status: candidate`, WP4b **queued replication / admissible_pending**).
Record-verified against the public GEO record on 2026-07-09 (t117 WP4b discovery sweep).

## What it is

The largest human GWI blood RNA-seq set: "Sex-specific transcriptional differences in Gulf War Illness
patients under stressful conditions" (IJMS 2025; Klimas/Broderick group) — **44 GWI vs 40 healthy controls**,
PBMC, Illumina NextSeq 500 + HiSeq 3000, sampled at three exercise timepoints (T0 baseline / T1 exertion /
T2 recovery); the T0 baseline is a clean case-vs-control arm. **Gulf War Illness = non-infectious
(organophosphate/chemical) trigger.**

## Corpus role (t117 WP4b)

`matrix: specificity` — **queued replication** for the flagship [[gse221921-fibromyalgia-pbmc]] and a
larger-N GWI RNA-seq counterpart to the microarray [[emexp2069-gulf-war-illness-pbmc]]. **admissible_PENDING,
two blockers to resolve before building:** (1) the supplementary matrix is named
`GSE286345_norm_counts_STAR_GWI_FM.csv.gz` — **confirm whether it co-carries fibromyalgia samples** and
disentangle the GWI arm; (2) it shares the Klimas/Broderick lab lineage with GSE168409/E-MEXP-2069, so it is
**not an independent replicate** of the GWI signal. Select the T0 baseline arm; carry the multi-platform +
sex axes as covariates.
