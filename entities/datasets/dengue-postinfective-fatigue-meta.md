---
id: dataset:dengue-postinfective-fatigue-meta
kind: dataset
title: Post-dengue fatigue — pooled sex-stratified meta-analysis evidence
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
  source_url: https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00620-5/fulltext
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: 'Published pooled meta-analytic effect sizes (reference dataset): fully extractable now from public forest plots and re-poolable — third-party-reproducible at the aggregate grain. Not individual-level microdata (a scientific-strength limit, not an access one).'
accessions: []
ontology_terms:
- post-dengue-fatigue
- dengue
- meta-analysis
- sex-differences
provided_capabilities: []
related:
- task:t013
- question:0007-mechanism-of-female-predominance-in-pais
- paper:Hertanti2025
- paper:Conde2026
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
---

# Post-dengue fatigue — pooled sex-stratified meta-analysis evidence

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: use-now` — literature-derived
pooled effect sizes; **extractable now** from published forest plots. Not a re-analyzable microdata set.

## What it is

Meta-analytic evidence base for post-dengue fatigue, including in-corpus reviews `paper:Hertanti2025`
(40 studies, n≈38,406; female **OR 1.65**, 95% CI 1.27–2.14) [@Hertanti2025] and `paper:Conde2026` (9 studies,
n≈1,470; female **OR 1.69**, 95% CI 1.33–2.14) [@Conde2026], plus the 2024 *eClinicalMedicine* pooled review.

## Why it fits t013

Provides **convergent, independent-pool female-excess estimates for post-acute dengue fatigue** while
acute DHF/severe-dengue risk factors are *not* female-predominant — direct evidence that female excess
**concentrates in persistence**. Post-dengue depression: null/insufficient (a dissociation signal).

## Access / caveats

Pooled, unadjusted ORs; heterogeneous case definitions; Asian-population predominance. Use as a
literature-derived comparator, not a dataset to re-analyze.
