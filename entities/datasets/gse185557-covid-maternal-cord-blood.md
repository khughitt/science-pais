---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse185557-covid-maternal-cord-blood
kind: dataset
title: GSE185557 — Maternal-fetal immune responses in pregnant women infected with
  SARS-CoV-2 (maternal + cord blood RNA-seq)
status: candidate
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: sars-cov-2
    cohort_design: cross-sectional
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185557
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- pregnancy
- sars-cov-2
- maternal-immune-milieu
- rna-seq
related:
- question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE185557 — Maternal-fetal immune responses in pregnant women infected with SARS-CoV-2 (maternal + cord blood RNA-seq)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Bulk RNA-seq of **paired maternal peripheral blood and cord blood** from SARS-CoV-2-positive
versus control pregnant women: 38 samples, DNBSEQ-G400. Collected at delivery.

## Why it fits

The closest public deposit to `question:0040` — it is the only located dataset profiling the
*maternal circulating* transcriptome under infection during pregnancy, rather than placental tissue
alone.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; count matrix CSV (1.1 Mb) downloadable.

**Caveats — this is a mechanism prior, not a trajectory vehicle.**
- Explicitly **cross-sectional at delivery**: there is **no post-acute or convalescent maternal
  timepoint**, so it cannot speak to PAIS *trajectory* at all.
- All subjects are pregnant, and the contrast is COVID+ vs COVID− *within* pregnancy — there is **no
  pregnant-vs-non-pregnant contrast**, so pregnancy is not stratified as an effect modifier. Hence
  no `stratification` claim; it does not satisfy `question:0040`.
- n=38, single site.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 38 samples, paired maternal blood (MB) + cord blood (CB), DNBSEQ-G400, count matrix CSV 1.1Mb downloadable. Explicitly CROSS-SECTIONAL at delivery -- no post-acute/convalescent maternal timepoint, so it is a mechanism prior only, not a pregnancy-x-PAIS trajectory vehicle.
