---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse228320-longcovid-wholeblood-pulmonary
kind: dataset
title: GSE228320 — Long COVID whole-blood (pulmonary-impairment phenotype)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228320
accessions:
- GSE228320
ontology_terms:
- long-covid
- sars-cov-2
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: sars-cov-2
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE228320 — Long COVID whole-blood (pulmonary-impairment phenotype)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID selected for a pulmonary-impairment phenotype, whole-blood bulk RNA-seq, ≈25 vs 25 [UNVERIFIED].

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** pulmonary-impairment-selected phenotype may not represent canonical fatigue-dominant long COVID — LOO-drop candidate.

## Access / caveats

Public accession (`GSE228320`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
