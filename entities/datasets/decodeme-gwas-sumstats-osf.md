---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:decodeme-gwas-sumstats-osf
kind: dataset
title: DecodeME GWAS summary statistics (OSF) — ME/CFS including infectious- vs non-infectious-onset strata
status: candidate
provided_capabilities:
- data_product: data-product:gwas-summary-statistics
  qualifiers:
    cohort_design: summary-stats
    stratification: infectious-onset
    trigger: post-infectious-mecfs
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
  source_url: https://osf.io/rgqs3/files/osfstorage
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- mecfs
- infectious-onset
- gwas-summary-statistics
- mendelian-randomization-outcome
related:
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# DecodeME GWAS summary statistics (OSF) — ME/CFS including infectious- vs non-infectious-onset strata

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

DecodeME GWAS summary statistics hosted openly on OSF (node `rgqs3`, public). The
`DecodeME Summary Statistics` folder holds REGENIE outputs including the headline scan
(`gwas_1.regenie.gz`, `gwas_2.regenie.gz`), sex-stratified files, and — most relevant here —
**`gwas_1_infectious_onset.regenie.gz` (318 MB)** and **`gwas_1_non_infectious_onset.regenie.gz`
(316 MB)**. DecodeME is the largest ME/CFS genetic study to date (~15,579 cases / 259,909 controls
in the main GWAS).

## Why it fits

Supplies the only released ME/CFS genetic **outcome** split by infectious vs non-infectious
onset. That split is directly load-bearing for `hypothesis:0001` (shared attractor reachable from
many triggers) and gives `question:0051` and `question:0034` an outcome arm for MR that is
independent of long-COVID ascertainment channels.

## Access / caveats

**Public, no DAC.** Verified 2026-07-17 via the OSF API: node `rgqs3` reports
`public: true`, and the summary-statistic files are directly downloadable.

**An important distinction the literature blurs:** DecodeME's **individual-level** data *is*
gated (Data Access Committee, ~3–6 month review). The **summary statistics are not.** Reporting
"DecodeME is gated" without that split would wrongly shelve an obtainable, third-party-reproducible
vehicle under D-004.

**Caveats.**
- The onset strata are **any infectious onset**, *not* glandular-fever-specific. There is no
  GF-only sumstat file, so this cannot by itself isolate the `question:0051` IM-history contrast —
  hence `stratification: infectious-onset`, which deliberately does **not** satisfy q0051's
  `im-history` requirement.
- Onset is self-reported; only ~68% of GF-onset cases were lab-confirmed.
- Case ascertainment is ME/CFS-criteria dependent (see `topic:pais-case-definition-heterogeneity`).

## Access verification log

- 2026-07-17 (agent (verify-access)): OSF API confirmed 2026-07-17: node rgqs3 'DecodeME' public=true; folder 'DecodeME Summary Statistics' contains gwas_1_infectious_onset.regenie.gz (318MB) and gwas_1_non_infectious_onset.regenie.gz (316MB) plus gwas_1/gwas_2/sex-stratified files, all directly downloadable, no DAC. IMPORTANT: individual-level DecodeME data IS DAC-gated (3-6mo review) -- the SUMSTATS are not. Onset strata are 'any infectious onset', NOT glandular-fever-specific.
