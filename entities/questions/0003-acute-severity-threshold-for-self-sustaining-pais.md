---
id: question:0003-acute-severity-threshold-for-self-sustaining-pais
kind: question
title: Is there a quantifiable acute-phase severity threshold above which homeostatic recovery becomes self-sustaining failure rather than self-resolving, and is it shared across pathogens?
status: active
ontology_terms:
- disease severity
- homeostasis
- recovery trajectory
- dose-response
datasets: []
source_refs:
- cite:Rahmati2025
- cite:Morroy2016
- cite:Cai2024
- cite:Xie2024
related:
- topic:shared-failure-mode-across-pais
required_capabilities: []
created: "2026-06-11"
updated: "2026-06-11"
---

# Is there a quantifiable acute-phase severity threshold above which homeostatic recovery becomes self-sustaining failure rather than self-resolving, and is it shared across pathogens?

## Summary

Across pathogens, acute-illness severity predicts post-acute burden, and several authors propose a *threshold* above which homeostatic recovery flips from self-resolving to self-sustaining failure. This question asks whether that threshold is real and quantifiable, and whether it is shared across triggers — distinguishing a continuous dose-response from a genuine phase transition into a stable dysregulated state.

## Why It Matters

- Decides whether PAIS prevention should target an identifiable severity threshold (e.g. aggressive acute-phase treatment in above-threshold patients) and whether hospitalized and non-hospitalized PAIS are quantitatively or qualitatively different.
- If unanswered, the field cannot distinguish "more severe insult → more residual damage" from "above threshold → locked attractor", which have opposite therapeutic implications (rehabilitate damage vs disrupt the loop).

## Current Evidence

- Supporting: Rahmati2025 finds ICU/ventilation/severity predict 3-year PASC persistence; Cai2024 shows hospitalized vs non-hospitalized COVID-19 follow qualitatively different multi-year trajectories (the latter approaching baseline); Morroy2016 and others report a consistent ~20% chronic fraction; Xie2024/Gandhi2023 show post-acute burden dominance in both COVID-19 and influenza hospitalizations.
- Conflicting / cautionary: much ME/CFS and long COVID follows *mild* acute infection (Oronsky2021 notes the SIRS→CARS→PICS arc may not apply), arguing against a simple severity threshold; ascertainment/"for vs with" bias inflates severity-outcome associations in administrative data (Gandhi2023).

## Thoughts

- Best current interpretation: severity is one axis of risk but not the only one — a host-determined regulatory threshold (sex, genetics, prior immunity) interacts with insult magnitude (Kalimuddin2022's bimodal recovery; Bai2023's ~10% PTLDS).
- Major uncertainty: whether the hospitalized/non-hospitalized divergence is a continuum or a bifurcation, and whether any threshold is pathogen-shared or trigger-specific.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0004-acute-severity-threshold`.
- Required data or analyses: longitudinal multi-cohort modeling of recovery trajectories vs acute severity with change-point/bistability tests; cross-pathogen replication (dengue DHF, Q-fever, influenza).
- Priority level: P1 — central to the attractor framing and to prevention strategy.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`.
- Article notes: Rahmati2025, Cai2024, Morroy2016, Xie2024, Gandhi2023, Kalimuddin2022, Oronsky2021.
- Methods/Datasets: VA cohorts (Cai2024, Xie2024); ORCHESTRA latent-transition data (Gusinow2026).
