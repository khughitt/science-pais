---
id: question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping
kind: question
title: Ambulatory within-person wearable + EMA protocol for PEM phenotyping without
  exercise challenge
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Ruijgt2025
- cite:Rekeland2022
- cite:Borhani2025
- cite:Che2025
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0011-mitochondrial-basis-of-pem
- question:0015-does-pem-requirement-improve-cross-study-comparability
- question:0049-two-day-cpet-multiomic-pem-assay-across-pais
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- topic:measurement-ascertainment-artifacts-in-pais
- theme:0003-demonstrability-ceiling-cross-pathogen-design
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-wearable-ema-pem-ambulatory
lens_views:
- lens: methodology
  rationale: "CPET (the gold-standard PEM operationalization the project uses via\
    \ Che2025) demands clinic attendance, risks post-exertional harm, and excludes\
    \ the severely ill. A wearable+EMA design captures the same physiology in the\
    \ natural environment, enabling personalized crash thresholds, continuous symptom-physiology\
    \ coupling, and one-instrument severity grading across triggers \u2014 separating\
    \ whether the PEM phenotype is real from how it is measured (a reproducibility\
    \ bottleneck the project flags). Serves question:0011 and question:0015.\n"
  origin_ref: explore-ideas-methodology
---
# Ambulatory within-person wearable + EMA protocol for PEM phenotyping without exercise challenge

## Summary

An ambulatory, within-person protocol combining continuous multi-modal wearable physiology (HRV,
accelerometry / step cadence, resting HR, skin temperature, SpO₂) with ecological momentary assessment
(EMA) over 14–28 days, proposed as an objective PEM-phenotyping method that does **not** require a
provoked cardiopulmonary exercise challenge. The target readouts are HRV-derived personalized exertion
thresholds and multi-day "crash" signatures that discriminate PAIS from recovered controls and
reproduce across long COVID, ME/CFS and PTLDS. It is attractive because the project's gold-standard PEM
operationalization (2-day CPET, via Che2025) demands clinic attendance, carries post-exertional-harm
risk, and excludes the severely ill.

## Why It Matters

- **Decision it affects:** whether PEM can be measured objectively at scale and used as a trial-ready
  endpoint — bearing on `question:0015` (does a PEM requirement improve cross-study comparability) and
  `question:0011` (mitochondrial basis of PEM).
- **Measurement-channel stakes:** it aims to separate *whether the PEM phenotype is real* from *how it
  is measured*, a reproducibility bottleneck the project repeatedly flags
  (`topic:measurement-ascertainment-artifacts-in-pais`).
- **Risk if unanswered:** PEM stays anchored to a low-throughput, harm-risking, severe-excluding assay,
  and cross-trigger comparability stays hostage to self-report.

## Current Evidence

- **Wearable HRV can distinguish autonomic dysfunction and yields a *candidate* exertion threshold —
  single-cohort preprint, PEM-validity not established.** Ruijgt2025 reports wearable HRV separating
  autonomic dysfunction in long COVID and operationalizes an HRV-derived threshold as a **putative** VT1
  proxy — but the study did not record PEM episodes or symptom questionnaires, and the authors present
  the threshold as a hypothesis requiring controlled study, not a validated PEM marker.
- **Long-horizon wearable feasibility in ME/CFS is established.** Rekeland2022 showed 6-month Fitbit
  activity monitoring is feasible in ME/CFS with step/HR tracking severity — supporting the
  ambulatory-adherence premise.
- **ML can detect persistent post-COVID physiological deviation from wearable streams** (Borhani2025),
  supporting a data-driven crash-signature detector — though on post-COVID physiology generally, not a
  validated PEM label.
- **Gap:** no protocol has validated a within-person composite that reproduces objective PEM across
  LC/ME/CFS/PTLDS without a challenge, and none has established minimal clinically important difference
  / responsiveness for use as a primary endpoint.

## Thoughts

- **Best current interpretation:** autonomic-recovery differences, long-horizon wearable feasibility,
  and ML-based deviation detection are demonstrated; the HRV-derived **PEM-threshold validity is not**
  (Ruijgt2025 is a single-cohort preprint with no PEM validation). The novel, unmet step is integration
  into one cross-trigger, challenge-free instrument benchmarked against an objective-PEM ground truth.
- **Major remaining uncertainty:** a wearable composite risks conflating **deconditioning** with
  **PEM**, and confounds activity with symptom-driven avoidance. Anchoring to an objective-PEM reference
  — the 2-day CPET multi-omic assay (`question:0049`) — is needed to license the "objective PEM" claim;
  otherwise the design imports the very self-report ambiguity it aims to escape (cf.
  `proposition:0011`: objective PEM correlates are trigger/endpoint-specific, not one shared failure mode).
- **Priority:** P2 as the tractable, low-harm complement to `question:0049`; strongest if run paired
  with a CPET-anchored subsample.

## Connections to Project

- Related hypotheses: `hypothesis:0006` (skeletal-muscle ischemic/mitochondrial PEM — the physiology
  the wearable would proxy).
- Related questions / topic / theme: `question:0011`, `question:0015`, `question:0049`;
  `topic:measurement-ascertainment-artifacts-in-pais`; `theme:0003` (named vehicle).
- Required datasets: prospective wearable+EMA cohorts with PAIS phenotyping (none project-held yet).
- Required analyses: within-person threshold estimation; crash-signature detection; cross-trigger
  reproducibility; MCID/responsiveness vs PROMs and vs CPET.
- Priority level: P2.

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`;
  `theme:0003-demonstrability-ceiling-cross-pathogen-design`.
- Article notes: `cite:Ruijgt2025`, `cite:Rekeland2022`, `cite:Borhani2025`; `cite:Che2025` (CPET
  reference standard).
- Methods/Datasets: `question:0049` (2-day CPET multi-omic assay as objective-PEM anchor).

## Notes

- 2026-07-06: Trial-endpoint extension: validate a composite wearable score (continuous HRV, resting HR, skin temperature, activity cadence) as an objective, responsive PRIMARY endpoint for PAIS trials — establishing minimal clinically important difference and responsiveness to benchmark against subjective PROMs, addressing the field's endpoint gap. (explore-ideas 2026-07-06 · cand-methodology-wearable-hrv-trial-endpoint; anchors in meta:explore-2026-07-06)