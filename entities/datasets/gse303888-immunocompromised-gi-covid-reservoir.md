---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse303888-immunocompromised-gi-covid-reservoir
kind: dataset
title: GSE303888 — SARS-CoV-2 GI-epithelium inflammation in immunocompromised cancer patients (GeoMx spatial)
status: candidate
provided_capabilities:
- data_product: data-product:gene-expression-spatial
  qualifiers:
    cohort_design: prospective-longitudinal
    trigger: sars-cov-2
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303888
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- immunosuppression
- sars-cov-2
- antigen-persistence
- spatial-transcriptomics
related:
- question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE303888 — SARS-CoV-2 GI-epithelium inflammation in immunocompromised cancer patients (GeoMx spatial)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

GeoMx spatial transcriptomics of GI biopsies from **3 immunocompromised cancer patients**,
sampled **before and after** SARS-CoV-2 infection (62 samples; NextSeq 2000, GPL30173). Persistent
viral elements and epithelial inflammation were detected to ~49 days post-infection.

## Why it fits

The single most on-target public deposit located for `question:0031`, and it probes the
**antigen/reservoir-persistence** mechanism in a chronically immunosuppressed host. Its
within-patient **pre-infection baseline** is rare and directly answers the standing project caveat
that most PAIS cohorts lack one.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; four CSV supplementary files
(CD45/PanCK filtered segment + normalized matrices, 222 KB–1.6 MB) downloadable, no login.

**Caveats.**
- **n=3, case series, no controls.** Hypothesis-generating only.
- Immunosuppression is **cancer-related**, not transplant or B-cell-depletion — the mechanism may
  not transfer to the populations `question:0031` centres on.
- **~49 days is barely past the acute window**, and no PAIS case definition or symptom phenotype is
  applied — so it cannot supply a PAIS case set.
- All 3 subjects are immunosuppressed with **no immunocompetent comparator**, so it does not
  stratify immunosuppression — hence no `stratification` claim, and it does not satisfy
  `question:0031`'s requirement.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 62 samples, GPL30173, 4 CSV supplementary files (CD45/PanCK filtered segment + normalized matrices, 222KB-1.6MB) downloadable via FTP/HTTP, no login. N=3 patients, GeoMx spatial, within-patient pre-infection baseline; no PAIS case definition applied.
