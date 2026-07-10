---
id: question:0089-original-antigenic-sin-pais-subtype-prediction
kind: question
title: Does immune imprinting by ancestral-strain SARS-CoV-2 (original antigenic sin)
  predict PAIS subtype or severity in subsequent breakthrough infections?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Crotty2026
related:
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- hypothesis:0020-host-immune-baseline-reserve-gate
created: '2026-07-10'
updated: '2026-07-10'
---

# Does immune imprinting by ancestral-strain SARS-CoV-2 (original antigenic sin) predict PAIS subtype or severity in subsequent breakthrough infections?

## Summary

Crotty2026 establishes that early immune priming — the original stimulus establishing T_H phenotype, B_Mem specificity, and antibody repertoire — shapes subsequent responses to related antigens for decades (pertussis wP/aP imprinting being the clearest human example; influenza immune history shaping flu vaccine responses being another). For SARS-CoV-2, many individuals were primed with ancestral Wuhan-strain antigens (via infection or mRNA vaccination) before Omicron emerged. Original antigenic sin (OAS) / immune imprinting predicts that these individuals' B_Mem and T cell responses will be biased toward ancestral-strain specificities during subsequent variant encounters, potentially affecting antigen clearance quality and, hypothetically, PAIS character. This question asks whether this imprinting effect is detectable in PAIS phenotyping.

## Why It Matters

- If ancestral-strain immune imprinting shapes the quality of recall responses to Omicron or later variants, it could contribute to incomplete antigen clearance in breakthrough infections — feeding `hypothesis:0002` (antigen fragment persistence) and `hypothesis:0003` (exhaustion loop).
- Identifies a biologically grounded basis for PAIS heterogeneity across pandemic waves: Omicron-era vs ancestral-era PAIS may differ not just due to variant pathogenicity but due to the immunological history of the infected host.
- Connects to `hypothesis:0009` (immune set-point shift): if the ancestral-strain imprint constitutes a "set point" that biases recall quality in a specific direction, this is a concrete molecular mechanism for how prior infection history produces durable immune state changes.
- Risk if unanswered: pandemic-wave–level PAIS epidemiology may confound variant effects (Omicron is less intrinsically pathogenic) with host immune-history effects (Omicron-era populations are also ancestral-imprinted), making causal attribution difficult.

## Current Evidence

- Crotty2026 (review): documents ancestral-strain imprinting for SARS-CoV-2 — Omicron exposures in ancestral-primed individuals preferentially recall ancestral-strain B_Mem and antibodies (original antigenic sin), with high cross-neutralization but a bias toward ancestral-strain epitopes rather than Omicron-specific epitopes. Repeated Omicron exposures can partially overcome imprinting (Yisimayi2023, cited).
- Mak2025 (this project corpus): seasonal coronavirus imprinting shapes LC immune profiles — consistent with the hypothesis that early coronavirus exposure history (not just SARS-CoV-2) shapes long-COVID phenotype via OAS mechanisms.
- SARS-CoV-2 B cell evolution studies (Cho2021, Kaku2022, Muecksch2022, cited in Crotty2026): demonstrate that B_Mem generated after ancestral-strain priming undergoes affinity maturation but retains ancestral specificity bias even after Omicron exposures; Omicron-specific B_Mem generated de novo is a distinct population.
- Direct PAIS-stratified evidence by ancestral-strain imprinting status is absent from the literature: no study has systematically compared PAIS incidence or phenotype between ancestral-imprinted and Omicron-first-primed individuals with adequate confounding adjustment.

## Thoughts

- Best current interpretation: ancestral-strain imprinting is real (Crotty2026 references clearly establish the B cell and antibody OAS effect for SARS-CoV-2), but whether it translates into detectable differences in antigen clearance quality *during a breakthrough infection* (vs simply producing cross-reactive antibodies with a different epitope distribution) is unknown. The crucial intermediate step is demonstrating that imprinting-biased recall leaves specific epitopes less well-covered, allowing more viral persistence at mucosal sites.
- Major uncertainty: the imprinting effect on T cells (as opposed to B cells/antibodies) is less well-characterized. CD4+ T cell memory is also imprinted (wP/aP pertussis example), but the CD4 imprinting effect for SARS-CoV-2 variants is not systematically documented. If CD4 T_H1 vs T_H2/T_H17 phenotype shifts occur due to ancestral-strain vs Omicron imprinting, these could shape PAIS immune character.
- Operationalization: a study comparing PAIS occurrence in (a) Omicron-first breakthrough with ancestral-strain-imprinted background vs (b) Omicron-first breakthrough in Omicron-naïve individuals (rare, primarily children born post-2021 or populations with very low historical exposure) — extremely difficult to achieve but would be the cleanest test.

## Connections to Project

- Related hypotheses: `hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune` (OAS as a mechanism of durable immune state change); `hypothesis:0020-host-immune-baseline-reserve-gate` (imprinting history as a component of immune baseline reserve); `hypothesis:0002-tissue-reservoir-antigen-fragment` (imprinting-limited clearance as a potential contributor to antigen persistence).
- Required analyses: PAIS phenotyping stratified by vaccine-infection history order and by serological imprinting markers (ancestral vs Omicron neutralization ratio as an imprinting proxy); pandemic-wave stratified PAIS incidence analysis adjusting for intrinsic variant severity.
- Priority level: low-medium — conceptually well-grounded but very difficult to test cleanly in existing cohorts; useful as a framing hypothesis for interpreting pandemic-wave PAIS heterogeneity.

## Related

- Topic notes: `topic:long-covid-immune-dysregulation`
- Article notes: `paper:Crotty2026` (OAS framework); `paper:Mak2025` (coronavirus imprinting in LC)
- Methods/Datasets: ancestral vs Omicron neutralization ratio as an imprinting index; cohorts with detailed variant-wave infection history and PAIS ascertainment.
