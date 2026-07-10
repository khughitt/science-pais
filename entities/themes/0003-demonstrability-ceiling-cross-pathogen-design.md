---
id: theme:0003-demonstrability-ceiling-cross-pathogen-design
kind: theme
title: Demonstrability ceiling and cross-pathogen harmonized design
status: active
theme_kind: methodological
theme_scope: project
related:
- question:0001-shared-molecular-signature-across-triggers
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared
- question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping
- question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize
- question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais
- question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization
- interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
- interpretation:0037-t116-power-bias-floor-shared-axis-sim
- interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed
- hypothesis:0001-shared-dysregulated-attractor
source_refs: []
origins: []
evidence_refs: []
created: '2026-07-10'
updated: '2026-07-10'
---
# Theme: Demonstrability ceiling and cross-pathogen harmonized design

## Definition

A cross-cutting frame for **what can and cannot be demonstrated about shared-vs-trigger-specific PAIS mechanisms with the data actually available**, and for the study designs that would move the ceiling. It groups the project's recurring finding that public, cross-sectional, and single-cohort resources sit *below the identification floor* for the questions asked of them — so the binding constraint is demonstrability (design + data), not idea generation. The theme's positive pole is the set of harmonized, cross-pathogen, and quasi-experimental designs (co-enrollment, target-trial emulation, Mendelian randomization, negative-control-outcome, wearable/EMA, spatial multi-omics) that would raise the ceiling.

## Why It Matters

Several of the project's most consequential results this cycle are *methodological ceilings*, not biology: the cross-PAIS pathway-rank probe fails closed because public off-diagonal concordance sits at or below the sampling floor (`interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`), and the power/bias simulation showed arm-count and feature-resolution — not per-arm N — are the binding levers (`interpretation:0037-t116-power-bias-floor-shared-axis-sim`). Making this frame explicit prevents the recurring error of reading a *non-arbitrating* null as evidence about PAIS, and it centralizes the design question — a K≥3 harmonized co-enrollment cohort (`question:0050`; `interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility`) — that Research-front #1 of the project synthesis depends on.

## Boundaries

Inside: demonstrability limits, identification floors, power/bias structure, and the design vehicles (`question:0027` MR, `question:0028` wearable/EMA, `question:0029` spatial omics, `question:0030` target-trial emulation, `question:0039` negative-control outcomes, `question:0050` co-enrollment) that would raise them. Outside: the *substantive* mechanism claims those designs would test (those stay in their hypotheses), the deflationary-null adjudication itself (`theme:0001`), and the temporal-kinetics frame (`theme:0002`). The reproducibility/access constraints (D-004 gated-EHR, D-005 seed-stage computational gate) bound which vehicles are admissible but are decisions, not members of this theme.

## Current Project Links

- Design/method questions: `question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared`, `question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping`, `question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize`, `question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais`, `question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization`.
- Demonstrability target + vehicle: `question:0001-shared-molecular-signature-across-triggers`, `question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design`.
- Identification-floor evidence: `interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility`, `interpretation:0037-t116-power-bias-floor-shared-axis-sim`, `interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`.
- Primary hypothesis whose demonstrability this governs: `hypothesis:0001-shared-dysregulated-attractor`.

## Guardrails

- A non-arbitrating or fail-closed result is a statement about the *vehicle*, never about PAIS biology — do not let it update belief on any hypothesis.
- Do not treat public-corpus pathway concordance as a substitute for a purpose-built harmonized cohort; the identification floor is demonstrated, not assumed.
- Keep vehicle admissibility (reproducibility class, D-004/D-005) separate from statistical power — a design can be powered yet inadmissible.

## Downstream Work

- Motivates the `specimen-acquisition` task-group work unblocking the harmonized/co-enrollment vehicles.
- Feeds Research-front #1 (the K≥3 harmonized cohort) of the project synthesis rollup.

## Open Questions

- What operational feature-resolution and arm-count jointly clear the identification floor for a real (not simulated) cross-pathogen dataset?
- Which admissible vehicle (co-enrollment vs target-trial emulation vs MR) is the most reproducible-tier-compatible path given D-004/D-005?

## Update Triggers

- A harmonized cross-pathogen dataset becomes available (revisit the floor empirically).
- Any new fail-closed or non-arbitrating computational result (add to the identification-floor evidence set).
- A change to D-004/D-005 that alters which design vehicles are admissible.
