---
id: dataset:colombo-dengue-study
type: dataset
title: "Colombo Dengue Study — post-dengue persistent fatigue (Sigera 2021)"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9115379/"
  reproducibility:
    obtainability: named-collaboration
    execution: custodian-run
    extractability: none
    notes: "No deposited/public microdata; the individual-level cohort is held by the original investigators and reproducible only by direct collaboration. Only investigator-published aggregate effect sizes are third-party-available (not third-party-extractable by an independent reproducer). Insider-only."
accessions: []
ontology_terms: [post-dengue-fatigue, dengue, prospective-cohort, sex-differences]
provided_capabilities:
  - modality: epidemiology
    trigger: dengue
    cohort_design: prospective-longitudinal
    outcome: fatigue
    stratification: sex
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
source_refs:
  - cite:Sigera2021
---

# Colombo Dengue Study — post-dengue persistent fatigue

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — **published
sex-stratified ORs usable now**; no public microdata.

## What it is

Prospective dengue cohort (Sri Lanka; Sigera et al. 2021). At 2 months, 51 of 158 dengue patients had fatigue, and fatigue risk was higher in female than male dengue patients (**RR 2.45**, 95% CI 1.24–4.86) [@Sigera2021].

## Why it fits t013

A rare **non-COVID viral trigger** with directly published **sex-stratified persistence/fatigue effect
sizes** — a comparator row in the cross-trigger female-excess table.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (acute dengue) | yes (3-mo fatigue) | weak (psych history excluded) | yes | yes |

## Access / caveats

Baseline depression/anxiety were **exclusion criteria** → weak neuropsychiatric arm. Single site; no
deposited microdata (use published effect sizes).
