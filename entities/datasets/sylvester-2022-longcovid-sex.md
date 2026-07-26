---
id: dataset:sylvester-2022-longcovid-sex
kind: dataset
title: Sylvester 2022 — sex differences in long COVID (domain-stratified ORs)
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: reference
tier: use-now
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://pubmed.ncbi.nlm.nih.gov/35726132/
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: 'Published meta-analysis (reference dataset): the artifact IS the domain-stratified sex ORs, fully extractable now from the public paper and trivially re-poolable — third-party-reproducible at the meta-analytic (aggregate) grain. No individual-participant data; the aggregate grain is a scientific-strength limit, not an access-reproducibility one.'
accessions: []
ontology_terms:
- long-covid
- sars-cov-2
- meta-analysis
- sex-differences
- neuropsychiatric
provided_capabilities: []
capability_scope: epidemiological
related:
- task:t013
- question:0007-mechanism-of-female-predominance-in-pais
---

# Sylvester 2022 — sex differences in long COVID

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: use-now` — published domain-stratified
sex ORs, **extractable now**. The anchor row of the cross-trigger effect-size table.

## What it is

Review/meta-analysis (Sylvester et al. 2022, *Curr Med Res Opin*; PMID 35726132) reporting **sex
odds ratios by symptom domain** for long COVID [@Sylvester2022].

## Why it fits t013 (directly operationalizes hypothesis b)

Female excess is **domain-specific**: psychiatric/mood **OR 1.58** (1.37–1.82), neurological 1.30,
ENT 2.28, GI 1.60 — while males are higher for endocrine (0.75) and renal (0.74). Overall long-COVID
female OR **1.22** (1.13–1.32). This is the cleanest published **neuropsychiatric-vs-somatic
dissociation** signal for the COVID trigger [@Sylvester2022].

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| no | yes (long COVID) | yes (mood OR 1.58) | yes (by domain) | yes |

## Access / caveats

Heterogeneous primary studies; ORs not always persistence-specific. Pair with a non-COVID trigger
(dengue, Lyme) to make the cross-trigger claim. Complement: gender/neuro long-COVID meta-analyses.
