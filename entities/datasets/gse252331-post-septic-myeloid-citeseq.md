---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse252331-post-septic-myeloid-citeseq
kind: dataset
title: GSE252331 — Post-septic peripheral myeloid compartment, rapid-recovery vs chronic critical illness (CITE-seq)
status: candidate
provided_capabilities:
- data_product: data-product:gene-expression-single-cell
  qualifiers:
    cohort_design: prospective-longitudinal
    trigger: sepsis
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE252331
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- post-sepsis
- chronic-critical-illness
- recovery-trajectory
- cite-seq
related:
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE252331 — Post-septic peripheral myeloid compartment, rapid-recovery vs chronic critical illness (CITE-seq)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

CITE-seq of the post-septic peripheral myeloid compartment: 34 samples (17 GEX + 17 ADT) —
4 early septic (day 4), 10 late (day 14–21, split **rapid-recovery n=5 vs chronic critical illness
n=5**), 12 healthy controls. NovaSeq 6000.

## Why it fits

Carries the contrast `question:0033` structurally needs: **rapid recovery vs chronic critical
illness at matched post-infection timepoints** — a recovery-*trajectory* stratification rather than
a flat case/control split. That is the closest public analogue to "who fails to re-home after an
acute infection".

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; 516.9 Mb archive (TAR) plus SRA Run Selector.

**Caveats.**
- **Frailty is not measured** — it stratifies *trajectory*, not frailty, so it makes no
  `stratification: frailty` claim and does not satisfy `question:0033`.
- Myeloid-only; small per-arm n (5 vs 5).

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 34 samples (17 GEX + 17 ADT), CITE-seq, NovaSeq 6000; 4 early septic (day 4), 10 late (day 14-21, RAP n=5 vs CCI n=5), 12 HC. 516.9Mb TAR + SRA. Carries the recovery-vs-chronic-critical-illness trajectory contrast; frailty unmeasured.
