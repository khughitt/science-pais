---
id: question:0087-vaccine-response-proxy-immune-baseline-reserve
kind: question
title: Can pre-infection vaccine-response magnitude and T helper phenotype serve as
  operational proxies for the immune baseline reserve gate?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Crotty2026
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
- question:0086-hybrid-immunity-type-pais-risk-modifier
created: '2026-07-10'
updated: '2026-07-10'
---

# Can pre-infection vaccine-response magnitude and T helper phenotype serve as operational proxies for the immune baseline reserve gate?

## Summary

`hypothesis:0020` posits a pre-infection "immune homeostatic reserve" that gates PAIS risk, but lacks a validated operational measure. Crotty2026 demonstrates that vaccine-response magnitude and T_H phenotype (B_Mem frequency, T_FH induction, B_PC durability, CD4+ T_H1/T_H2/T_H17 balance) are quantifiable outputs of immune homeostatic competence that vary substantially across individuals and host strata (age, frailty, immunosuppression, prior infection history). This question asks whether these vaccine-response parameters could serve as pre-infection reserve proxies — measurable, biologically grounded variables that index the reserve gate without requiring a direct definition of "homeostatic reserve."

## Why It Matters

- `hypothesis:0020` currently lacks an operational measure of "immune homeostatic reserve," which is the primary bottleneck to testing its core prediction (reserve rank-orders PAIS risk after adjusting for acute severity). A validated proxy would unlock the hypothesis for empirical test.
- Vaccine-response parameters (e.g., antibody durability, B_Mem frequency, T_FH induction after a defined antigen challenge) are measurable in pre-existing biobanks with linked vaccination records — potentially enabling retrospective reserve estimation without a purpose-built study.
- Risk if unanswered: `hypothesis:0020` remains a candidate frame without an empirically testable reserve axis, limiting its promotion from candidate to active status.

## Current Evidence

- Crotty2026 (review): documents that vaccine-response magnitude is shaped by multiple reserve-related variables — aging (declining thymic output → reduced naive T fraction), prior infection history (original antigenic sin for influenza), immunosuppression (blunted B_Mem and B_PC induction), and adjuvant availability (T cell help quality). These dependencies suggest that vaccine response is a downstream readout of immune reserve.
- Stacey2025 (ref'd in Crotty2026): influenza pre-vaccination antibody titers predict post-vaccination response — older titre shapes next response, establishing bidirectional immunity-vaccine relationships. [UNVERIFIED: need to confirm direction and magnitude of this prediction]
- Immune response to a standard antigen challenge (e.g., a booster dose of an established vaccine like tetanus toxoid or COVID booster) as a reserve proxy has been used in frailty/aging research — but systematic validation against PAIS incidence has not been done.
- Conflicting: vaccine response is highly confounded by prior exposure history (for influenza especially), assay differences, vaccine lot/cold-chain variation, and timing. The T_H phenotype (wP/aP imprinting) is fixed by early childhood vaccine type in most populations — reducing variation in adults. A general-purpose reserve proxy would need to disentangle reserve from exposure-history effects.

## Thoughts

- Best current interpretation: vaccine-response parameters are biologically plausible reserve proxies, but their specificity for "immune homeostatic reserve" vs "prior antigen exposure history" is unclear. A study linking pre-infection vaccine response to PAIS incidence, controlling for acute severity and exposure history, would be the cleanest test.
- The most actionable proxy in existing biobanks: COVID booster antibody durability at 6 months (long-lived B_PC indicator), combined with T_FH magnitude (if T cell data available), in cohorts with confirmed subsequent SARS-CoV-2 infections and PAIS ascertainment.
- Major remaining uncertainty: whether any single vaccine-response metric captures enough of the reserve concept to be useful (the reserve is likely multivariate), and whether vaccine-response variance at the individual level is large enough to be informative after adjusting for prior exposure history.

## Connections to Project

- Related hypotheses: `hypothesis:0020-host-immune-baseline-reserve-gate` (primary; this question operationalizes its P3 prediction); `hypothesis:0004-acute-severity-threshold` (confound to control for).
- Required analyses: correlation of pre-infection vaccine-response metrics (antibody t½, B_Mem frequency, T_FH magnitude) with PAIS incidence in a prospective cohort with linked vaccination records and PAIS outcomes. Requires separating reserve from exposure-history confounding.
- Priority level: medium — the most direct path to operationalizing h0020's testable prediction, but requires access to a well-phenotyped pre-infection + post-infection biobank with both vaccine-response and PAIS outcome data.

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais`
- Article notes: `paper:Crotty2026` (framework); `paper:Vinson2024`, `paper:Peluso2022a` (immunosuppressed stratum as an existing grounded case)
- Methods/Datasets: COVID booster antibody decay studies (Israel, UK SIREN); UK Biobank (pre-pandemic immune phenotyping linked to COVID outcomes).
