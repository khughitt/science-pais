---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse63085-post-lyme-pbmc
kind: dataset
title: GSE63085 — Post-treatment Lyme PBMC transcriptome
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63085
accessions:
- GSE63085
ontology_terms:
- post-lyme
- ptlds
- lyme-disease
- pbmc
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: lyme-disease
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE63085 — Post-treatment Lyme PBMC transcriptome

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-treatment Lyme PBMC bulk RNA-seq, ≈29 vs 13 [UNVERIFIED]. A post-Lyme timecourse — the cohort is not selected for PTLDS symptoms.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented (Lyme trigger)
- **Conditional/LOO flag:** not PTLDS-symptom-selected — represents post-Lyme, not necessarily symptomatic PTLDS; LOO-drop candidate.

## Access / caveats

Public accession (`GSE63085`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
