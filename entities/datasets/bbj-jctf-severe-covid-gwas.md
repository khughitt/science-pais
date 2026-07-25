---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:bbj-jctf-severe-covid-gwas
kind: dataset
title: BioBank Japan / Japan COVID-19 Task Force — severe COVID-19 (age<65) GWAS summary statistics
status: candidate
provided_capabilities:
- data_product: data-product:gwas-summary-statistics
  qualifiers:
    cohort_design: summary-stats
    trigger: sars-cov-2
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: custom
access:
  level: public
  availability: available
  verified: true
  source_url: https://pheweb.jp/pheno/SevereCOVID19_LT65
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- sars-cov-2
- acute-severity
- east-asian-ancestry
- gwas-summary-statistics
related:
- question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# BioBank Japan / Japan COVID-19 Task Force — severe COVID-19 (age<65) GWAS summary statistics

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Japan COVID-19 Task Force / BioBank Japan GWAS summary statistics for
"Severe COVID-19, aged less than 65" — **440 cases / 2,377 controls**, Japanese ancestry. Served via
PheWeb.jp with a direct download route to the NBDC `hum0343` release.

## Why it fits

The only open, non-European COVID GWAS summary-statistic vehicle verified for
`question:0032`. East-Asian ancestry is specifically informative here because the FOXP4 long-COVID
risk allele (rs9367106-C) runs at ~36% in East Asians versus ~1.6% in non-Finnish Europeans, so
power at that locus is concentrated outside EUR.

## Access / caveats

**Public, no login.** PheWeb.jp landing page confirmed 2026-07-17; sumstats download
resolves without credentials.

**Caveats.**
- **The phenotype is acute severity, not PAIS.** This is an ancestry-transferability probe or an MR
  exposure — it is *not* a long-COVID outcome vehicle, and must not be scored as one. Hence no
  `stratification` claim: a single-ancestry study does not stratify ancestry.
- Small (440 cases); ancestry is not stated on the PheWeb page itself (JCTF/BBJ is Japanese).

**Scope (D-006).** Routing this into the Wave-1 MR line would introduce a **non-HGI outcome
vehicle**, which D-006 requires a fresh scope decision for. It is *not* covered by D-005.

## Access verification log

- 2026-07-17 (agent (verify-access)): PheWeb.jp landing page confirmed 2026-07-17: 440 cases / 2,377 controls, sumstats downloadable without login (/download/SevereCOVID19_LT65 -> NBDC hum0343). Ancestry not stated on page (JCTF/BBJ = Japanese). PHENOTYPE IS ACUTE SEVERITY, NOT PAIS -- ancestry-transferability probe only, not a long-COVID outcome vehicle.
