---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse251872-pime-cfs-pbmc
kind: dataset
title: GSE251872 — PI-ME/CFS PBMC transcriptome (NIH intramural)
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: "2026-07-08"
  verified_by: "agent (t117 WP1)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251872
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample count data in GSE251872_RAW.tar (per-sample TXT files, 4.8 MB) plus TXT series matrix; staging to disk deferred to workflow execution."
accessions:
- GSE251872
ontology_terms:
- post-infectious-mecfs
- me-cfs
- pbmc
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: post-infectious-mecfs
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE251872 — PI-ME/CFS PBMC transcriptome (NIH intramural)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Record-verified against the public GEO record on 2026-07-08 (t117 WP1).

## What it is

Post-infectious ME/CFS **PBMC bulk RNA-seq** — confirmed the blood transcriptome, not single-cell and not a non-blood assay. This is the `[PBMC RNA-Seq]` sub-series of the NIH intramural deep-phenotyping study "Deep phenotyping of Post-infectious ME/CFS" (Walitt et al., *Nat Commun* 2024, PMID 38383456), with clinically adjudicated post-infectious onset.

Confirmed design: **27 baseline PBMC samples — 12 PI-ME/CFS vs 15 healthy volunteers** (per the GSM sample listing). Case-vs-control (PI-ME/CFS vs HV) contrast is usable but small (n=12 cases). Two sequencing platforms: GPL21290 (Illumina HiSeq 3000) and GPL24676 (Illumina NovaSeq 6000) — platform/batch is a covariate to model.

**Correction:** the prior "≈17 vs 21" specifics were the overall NIH study enrollment (17 PI-ME/CFS, 21 HV), *not* this GEO deposit. The public PBMC RNA-Seq sub-series contains only 27 samples (12 cases / 15 controls).

Per-sample matrix is downloadable: `GSE251872_RAW.tar` (per-sample TXT count files, 4.8 MB) plus the TXT series matrix.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none (strong design)

## Access / caveats

Public accession (`GSE251872`), per-sample matrix confirmed downloadable via `GSE251872_RAW.tar` + series matrix (t117 WP1, record-checked 2026-07-08). Caveats: small case arm (n=12); two-platform design (HiSeq 3000 + NovaSeq 6000) introduces a batch/platform covariate that must be modelled.
