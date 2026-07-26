---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse228320-longcovid-wholeblood-pulmonary
kind: dataset
title: GSE228320 — Long COVID whole-blood (pulmonary-impairment phenotype)
status: candidate
created: "2026-07-07"
updated: "2026-07-07"
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
  last_reviewed: '2026-07-08'
  verified_by: agent (t117 WP1)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228320
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: 'Two per-sample matrices downloadable: GSE228320_Raw_counts.txt.gz (1.7 Mb, raw counts) and GSE228320_Counts_Normalized_postCOVID.txt.gz (6.0 Mb, normalized), 50 samples. Staging to disk deferred to workflow execution.'
accessions:
- GSE228320
source_refs:
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE228320
ontology_terms:
- long-covid
- sars-cov-2
- whole-blood
- rna-seq
provided_capabilities:
- data_product: data-product:gene-expression-bulk-rna
  qualifiers:
    cohort_design: case-control
    trigger: sars-cov-2
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE228320 — Long COVID whole-blood (pulmonary-impairment phenotype)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Whole-blood bulk RNA-seq from **COVID-19 ARDS survivors**, contrasting **severe pulmonary diffusion impairment (DLCO < 60%) vs mild/normal (DLCO ≥ 60%)**: **50 GSMs total** (case-vs-control on lung-function stratum; the ~25/25 split is consistent with "50 samples, cases vs matched controls" but the exact per-arm n is not itemised in the record — approximate). Sampled **3 months after hospital discharge** (confirmed). Assay confirmed bulk RNA-seq on Illumina HiSeq 1500 (GPL18460). Title: "Whole blood transcriptional profiling of pulmonary functional sequelae in ARDS secondary to SARS-CoV-2 infection."

**FLAG — contrast is NOT long-COVID-vs-recovered (t117 WP1, 2026-07-08).** Both arms are severe-COVID (ARDS) survivors; the case axis is **residual lung-function impairment (DLCO)**, a pulmonary-sequelae phenotype, not canonical fatigue-dominant long COVID. This is a severity-selected, organ-specific contrast — reinforces the existing LOO-drop caveat. Comparator is infected-recovered with differential pulmonary outcome.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** pulmonary-impairment-selected phenotype may not represent canonical fatigue-dominant long COVID — LOO-drop candidate.

## Access / caveats

Verified: per-sample matrices (`GSE228320_Raw_counts.txt.gz` + `GSE228320_Counts_Normalized_postCOVID.txt.gz`, 50 samples) are publicly downloadable → `verified: true`. Data access is clean; the **phenotype**, not the access, is the concern — pulmonary-impairment (DLCO) contrast within ARDS survivors makes this a **LOO-drop / demotion candidate** for a fatigue-dominant long-COVID signature analysis.
