---
id: question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais
kind: question
title: Target trial emulation in multi-trigger EHR cohorts for cross-PAIS comparative
  effectiveness
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Preiss2025
- cite:Bajema2023
- cite:Hansford2023
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0012-prevention-vaccination-antiviral-reduces-pais
- question:0002-antigen-clearance-rescues-symptoms
- question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- topic:measurement-ascertainment-artifacts-in-pais
- theme:0003-demonstrability-ceiling-cross-pathogen-design
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-target-trial-emulation-cross-trigger
lens_views:
- lens: methodology
  rationale: "TTE has estimated antiviral effects on long COVID onset at EHR scale;\
    \ applying the same causal scaffold to non-COVID triggers is untested and would\
    \ test cross-trigger generalizability of prevention strategies. A null/attenuated\
    \ antiviral effect in PTLDS/post-sepsis would itself argue against a single shared\
    \ pathway. Serves question:0012 and question:0002. NOTE reproducibility class:\
    \ leading exemplars use gated enclaves (N3C) \u2014 prefer a design targeting\
    \ third-party-reproducible data sources per project policy.\n"
  origin_ref: explore-ideas-methodology
---
# Target trial emulation in multi-trigger EHR cohorts for cross-PAIS comparative effectiveness

## Summary

Target trial emulation (TTE) applies an explicit protocol (eligibility, treatment strategies,
assignment, time-zero, causal contrast, clone-censor-weight or IPTW estimation) to observational
EHR/claims data to estimate acute-phase intervention effects on PAIS incidence. The novel move is to run
the same causal scaffold **beyond COVID-19** — post-Lyme, post-sepsis (PICS), post-dengue — asking
whether interventions that reduce long-COVID incidence (antivirals, anticoagulants, immunomodulators)
also reduce post-acute syndrome incidence in other triggers, and whether effect heterogeneity tracks
pathogen biology or shared host markers.

## Why It Matters

- **Decision it affects:** cross-trigger generalizability of prevention (`question:0012`) and the
  antigen-clearance-rescues-symptoms logic (`question:0002`). A null/attenuated antiviral effect in
  non-COVID triggers would itself argue against a single shared pathway.
- **Risk if unanswered:** prevention evidence stays COVID-only, and the shared-vs-specific question goes
  untested on the one design that can exploit quasi-experimental treatment-practice variation.

## Current Evidence

- **TTE is mature and validated for COVID.** Preiss2025 emulated Paxlovid → long-COVID onset at
  445,738-patient scale (N3C/RECOVER); Bajema2023 provides a clone-censor-weight TTE template for
  post-COVID conditions in the VA. Hansford2023 catalogs the reporting elements needed to harmonize
  emulations for cross-trigger comparison.
- **Gap:** no TTE has been run for a non-COVID PAIS trigger.

## Thoughts

- **Best current interpretation:** the method transfers cleanly in principle, but the binding constraint
  is the **data vehicle, not the estimator**. The leading exemplars run on **gated enclaves** (N3C, VA),
  which sit below the project's third-party-reproducibility bar — and **D-004** explicitly forbids
  executing gated-EHR estimands (the project's own N3C-style estimand, `plan:0006`, is **banked** for
  exactly this reason). An admissible form of `question:0030` requires a *downloadable* multi-trigger
  EHR/claims resource, which does not currently exist.
- **Major remaining uncertainty:** whether any transparent, third-party-reproducible multi-trigger
  EHR/claims source can support a TTE at adequate power; absent one, the question's value is as a *design
  residue* (the harmonized protocol per Hansford2023) rather than an executable analysis.
- **Priority:** P3 — high conceptual value, blocked on admissible data (D-004). Its sibling
  `question:0039` (negative-control outcomes) is the more admissible bias-bounding path.

## Connections to Project

- Related hypotheses: `hypothesis:0008` (measurement/ascertainment — TTE confounding-control is the
  counterpart to h0008's bias claims).
- Related questions / topic / theme: `question:0012`, `question:0002`, `question:0039`;
  `topic:measurement-ascertainment-artifacts-in-pais`; `theme:0003` (named vehicle).
- Related decisions: **D-004** (no gated-EHR estimands) bounds admissibility; `plan:0006` is the banked
  instance.
- Required datasets: downloadable multi-trigger EHR/claims (missing).
- Required analyses: clone-censor-weight / IPTW TTE per trigger; effect-heterogeneity meta-analysis;
  Hansford2023 reporting harmonization.
- Priority level: P3 (data-blocked, D-004).

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`;
  `theme:0003-demonstrability-ceiling-cross-pathogen-design`.
- Article notes: `cite:Preiss2025`, `cite:Bajema2023`, `cite:Hansford2023`.
- Methods/Datasets: `plan:0006` (banked N3C prototype, D-004).

## Notes

- 2026-07-06: Mechanism-proximal extension: beyond comparative effectiveness, emulate target trials of specific mechanism-proximal interventions (prophylactic anticoagulation, immunomodulators, vaccination timing relative to infection) and extend to non-SARS-CoV-2 triggers (post-Lyme, post-dengue, post-flu) where treatment-practice variation is quasi-experimental. (explore-ideas 2026-07-06 · cand-methodology-tte-pais-mechanism; anchors in meta:explore-2026-07-06)