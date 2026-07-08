---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse270045-longcovid-mecfs-wholeblood
kind: dataset
title: GSE270045 — post-COVID ME/CFS whole-blood transcriptome
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270045
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample count matrix downloadable: GSE270045_LC_counts.tsv.gz (2.4 Mb, TSV, 36 samples). Staging to disk deferred to workflow execution."
accessions:
- GSE270045
ontology_terms:
- long-covid
- post-covid-mecfs
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

# GSE270045 — post-COVID ME/CFS whole-blood transcriptome

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-COVID ME/CFS whole-blood bulk RNA-seq: **19 Long COVID patients with ME/CFS vs 17 controls** (36 GSMs; confirmed). Assay confirmed bulk RNA-seq on Illumina NovaSeq X Plus (GPL34284). Publication PMID 41205594 ("Upregulation of olfactory receptors and neuronal-associated genes … in Long COVID patients"). N (19 vs 17), whole-blood tissue, and bulk RNA-seq all match the discovery-sweep claim.

**Note (t117 WP1, 2026-07-08):** the record describes the 17-subject comparator as **healthy controls (uninfected/naive)**, not infected-recovered — differs from the infected-recovered comparators in GSE224615/GSE228320; relevant to cross-dataset control-type harmonisation. Time-since-infection at sampling is **not stated in record**.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none

## Access / caveats

Verified: per-sample count matrix `GSE270045_LC_counts.tsv.gz` (2.4 Mb, 36 samples) is publicly downloadable → `verified: true`. Clean case-vs-control design (19 LC-ME/CFS vs 17 healthy). Strongest of the four WP1 candidates.
