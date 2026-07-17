---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gcst005038-allergic-disease-gwas
kind: dataset
title: GCST005038 — Shared genetic origin of asthma, hay fever and eczema (Ferreira
  2017) GWAS summary statistics
status: candidate
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    trigger: not-applicable
    cohort_design: summary-stats
    stratification: atopy
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST005038
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- atopy
- allergic-disease
- gwas-summary-statistics
- mendelian-randomization-exposure
related:
- question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GCST005038 — Shared genetic origin of asthma, hay fever and eczema (PMID 29083406) GWAS summary statistics

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

GWAS Catalog study GCST005038 — "Allergic disease (asthma, hay fever or eczema)",
**180,129 European-ancestry cases / 180,709 controls** (PMID 29083406). Full summary statistics
released (`fullPvalueSet: true`).

## Why it fits

The only well-powered **open** atopy exposure instrument located, and therefore the only
third-party-reproducible way into `question:0034` today. Intended as the exposure arm of an
atopy → PAIS MR, paired with `dataset:covid19-hgi-longcovid-gwas` (infected-control long-COVID
outcome) or `dataset:decodeme-gwas-sumstats-osf`.

## Access / caveats

**Public, no DUA.** GWAS Catalog REST confirmed 2026-07-17; full sumstats on the EBI FTP.

**Caveats.**
- The released file **excludes 23andMe samples**, i.e. the best-powered stratum is withheld.
- The phenotype is a **broad any-allergic-disease composite**; it cannot separate atopy from MCAS.
  MCAS specifically has essentially no genetic or omics footprint (see this entity's sibling
  search residue) — hereditary alpha-tryptasemia (TPSAB1 copy number) is **not capturable** from
  standard GWAS arrays or sumstats, so it cannot be recovered through this vehicle.
- **Power is the live risk**, not availability: the long-COVID outcome arm's EUR case count is
  small, so a modest atopy effect may be undetectable. Power should be checked *before* committing.

**Scope (D-005).** Execution is **not authorised** — an atopy → long-COVID MR is a new
computational line over a new exposure vehicle, outside the D-005 Wave-1 pilot.

## Access verification log

- 2026-07-17 (agent (verify-access)): GWAS Catalog REST confirmed 2026-07-17: trait 'Allergic disease (asthma, hay fever or eczema)', 180,129 EUR cases / 180,709 EUR controls, PMID 29083406, fullPvalueSet=true (full sumstats on FTP, no DUA). NOTE: the released file excludes 23andMe samples; broad any-allergic-disease phenotype cannot separate atopy from MCAS.
