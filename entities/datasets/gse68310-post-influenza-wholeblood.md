---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse68310-post-influenza-wholeblood
kind: dataset
title: GSE68310 — Post-influenza whole-blood (FLU09 convalescent)
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE68310
accessions:
- GSE68310
ontology_terms:
- post-influenza
- influenza
- whole-blood
- microarray
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: influenza
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE68310 — Post-influenza whole-blood (FLU09 convalescent)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-influenza convalescent whole-blood microarray. Convalescent sampling window is short (≈3 weeks [UNVERIFIED]), near/under the ≥4-week post-acute floor.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** sampling window ≈3 wk borderline post-acute AND microarray platform — double LOO-drop candidate (platform + window).

## Access / caveats

Public accession (`GSE68310`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
