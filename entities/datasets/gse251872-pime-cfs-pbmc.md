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
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251872
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

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-infectious ME/CFS PBMC bulk RNA-seq, ≈17 vs 21 [UNVERIFIED], from the NIH intramural deep-phenotyping study with clinically adjudicated post-infectious onset.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none (strong design)

## Access / caveats

Public accession (`GSE251872`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
