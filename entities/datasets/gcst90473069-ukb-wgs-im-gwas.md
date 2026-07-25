---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gcst90473069-ukb-wgs-im-gwas
kind: dataset
title: GCST90473069 — Infectious mononucleosis (ICD10 B27) GWAS summary statistics, UK Biobank WGS
status: candidate
provided_capabilities:
- data_product: data-product:gwas-summary-statistics
  qualifiers:
    cohort_design: summary-stats
    stratification: im-history
    trigger: ebv
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST90473069
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- infectious-mononucleosis
- ebv
- gwas-summary-statistics
related:
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GCST90473069 — Infectious mononucleosis (ICD10 B27) GWAS summary statistics, UK Biobank WGS

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

GWAS Catalog study GCST90473069 — "ICD10 B27: Infectious mononucleosis", **3,621
non-Finnish-European cases / 454,819 controls**, from the UK Biobank WGS association scan
(PMID 40770095). Full summary statistics released.

## Why it fits

An **independent, non-Finnish IM instrument**, so the FinnGen-based MR for `question:0051`
can be replicated cross-cohort rather than resting on a single bottlenecked population.

## Access / caveats

**Public summary statistics.** GWAS Catalog REST confirmed 2026-07-17;
`fullPvalueSet: true`, files on the EBI FTP (~3.2 G).

**D-004 note — this clears the bar.** The study is UK-Biobank-*derived*, but D-004 bars
**individual records**, not open summary statistics. Nothing gated is required to re-obtain and
re-analyse this file, so it is third-party-reproducible and is *not* shelved alongside
`dataset:uk-biobank-covid`.

**Caveats.**
- Registry/ICD-coded IM: medically-attended only; the same control-contamination issue as FinnGen
  (asymptomatic seroconverters sit in the control group).
- WGS-scan output — instrument selection/tuning needed before MR use.
- **Same underpowered + likely-uninterpretable verdict as FinnGen (power-screen 2026-07-18):** at
  3,621 cases the exposure GWAS yields a weak, HLA-dominated instrument; against an HGI long-COVID
  outcome it detects only OR ≥ ~1.4–1.6/SD at 80% power, and an HLA-inclusive instrument is not
  credibly exclusion-restriction-valid (shelve unless a strong non-HLA instrument survives clumping).
- **Sample overlap.** This is a **UKB-derived** exposure and the HGI long-COVID outcome **includes
  UKB**, so a two-sample IM→long-COVID MR would carry direct sample overlap that must be handled.
  Retained **only if the IM estimand is later revived with a defensible (non-HLA) instrument** — not
  tied to the atopy line. See `dataset:finngen-r12-im-gwas`.

## Access verification log

- 2026-07-17 (agent (verify-access)): GWAS Catalog REST confirmed 2026-07-17: trait 'ICD10 B27: Infectious mononucleosis', 3,621 NFE cases / 454,819 controls, PMID 40770095, fullPvalueSet=true. UKB-DERIVED but SUMMARY-LEVEL and freely downloadable -- D-004 bars UKB individual records, not open sumstats, so this clears the bar. Independent non-Finnish IM instrument for replicating the FinnGen MR.
