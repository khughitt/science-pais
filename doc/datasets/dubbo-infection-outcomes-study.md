---
id: dataset:dubbo-infection-outcomes-study
type: dataset
title: "Dubbo Infection Outcomes Study (DIOS)"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: track
license: unknown
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1569956/"
accessions: []
ontology_terms: [post-infective-fatigue, ebv, q-fever, ross-river-virus, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - topic:shared-failure-mode-across-pais
---

# Dubbo Infection Outcomes Study (DIOS)

**Candidate dataset for `task:t013`** (female excess: acute vs post-acute). `status: candidate`,
`tier: track` — a catalog entry, not a provisioned dataset: no workflow/`datapackage` exists yet.

## What it is

Prospective community cohort (Dubbo, rural NSW, Australia) that followed individuals with acute
**EBV (glandular fever), Q fever (*Coxiella burnetii*), and Ross River virus** through to recovery or
post-infective fatigue — **three distinct triggers within one harmonized design**. Anchor paper:
Hickie et al. 2006, *BMJ* (PMID 16950834, PMC1569956); later psychosocial/predictor analyses followed.

## Why it fits t013 (highest conceptual match)

- **Cross-trigger, single design** — directly tests whether female excess is trigger-independent.
- Measures **acute severity → post-acute persistence** (CFS caseness ~11% at 6 mo) in the same people.
- Records **sex** as a predictor; outcomes separate **mood disturbance** (psychiatrist-assessed) from
  **somatic fatigue** — enabling the neuropsychiatric-vs-fatigue dissociation test.
- The famous **trigger-independent recovery rate** is itself a key comparator.

## Coverage

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes | yes (6-mo CFS caseness) | yes (mood) | yes | sex recorded (~51% women); per-trigger sex×outcome table not published |

## Access / feasibility

- **No public microdata located.** Use is via published tables or investigator collaboration (UNSW;
  Lloyd / Hickie groups). Outside the `science datasets` adapters.
- **Realistic near-term use:** literature-derived summary statistics (reconstruct sex-stratified
  per-trigger persistence from the papers), not a re-analysis.

## Caveats

Predominantly Caucasian rural-Australian cohort; per-trigger sex-stratified effect sizes must be
reconstructed from publications; microdata not deposited.
