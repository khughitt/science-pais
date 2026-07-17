---
id: question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts
kind: question
title: PAIS incidence and mechanism in chronically immunosuppressed hosts
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Vinson2024
- cite:Peluso2022a
- cite:Chavatza2025
origins:
- type: assistant
  ref: explore-ideas-population
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
created: '2026-07-04'
updated: '2026-07-16'
added_by: explore-ideas:claude-opus-4-8:cand-population-immunosuppressed-host-pais
lens_views:
- lens: population
  rationale: 'PAIS mechanisms assume an immune system able to mount, sustain, then
    fail to resolve inflammation. Immunosuppressed hosts are a natural experiment
    dissociating candidate mechanisms: if antigen persistence/activation drive PAIS,
    partial suppression might reduce incidence; if exhaustion/dysregulation drive
    it, baseline dysfunction might amplify risk. The biologic-DMARD population is
    essentially unstudied for post-infectious sequelae.

    '
  origin_ref: explore-ideas-population
---
# PAIS incidence and mechanism in chronically immunosuppressed hosts

## Summary

<!-- What is being asked and why it is important. -->

## Why It Matters

<!-- Bulleted list. Cover at least:
- the decision this question affects
- the risk if the question is left unanswered
-->

## Current Evidence

- **The counterintuitive headline: immunosuppression is associated with *more* PASC, not less.** Vinson et
  al. (2024, N3C) found solid-organ-transplant recipients had higher PASC than propensity-matched
  non-immunosuppressed controls (2.2% vs 1.4%, aOR 1.48), with mycophenolate mofetil independently
  associated (aOR 2.04) [@Vinson2024]. This argues *against* a simple "immune activation is required, so
  suppressing it protects" model.
- **Mechanistic candidates now have primary support on two axes.** (1) *Impaired clearance / antigen
  persistence:* Chavatza et al. (2025) show anti-CD20 (rituximab) → hypogammaglobulinemia → prolonged,
  lower-respiratory-compartmentalized SARS-CoV-2 persistence (BAL+ in ~71%, often NPS-negative)
  [@Chavatza2025] — a clean instance of the impaired-clearance explanation. (2) *Exhaustion baseline:*
  Peluso et al. (2022, AIDS) show people with HIV had ~4× higher PASC odds with a lower memory-CD8 /
  higher PD-1+ CD4 exhaustion signature [@Peluso2022a].
- **Conflicting / unresolved:** these are distinct mechanisms pointing the same direction (more PASC), so
  the SOT paradox is over-determined — comorbidity/reserve depletion, drug-specific antiviral impairment,
  and prolonged antigen burden are all live and not yet disentangled. No study uses immunosuppression
  *intensity* as the primary exposure gradient.
- **Still empty:** anti-TNF, anti-IL-6R, and JAK-inhibitor populations have no long-COVID mechanism data.

## Thoughts

- Best current interpretation: immunosuppression does not protect against PAIS and may worsen it,
  primarily via impaired viral clearance (antigen persistence, h0002) and pre-existing exhaustion (h0003)
  rather than by blocking an activation requirement — which weakens naive "immune-activation-required" models.
- Major remaining uncertainty: whether a *drug-class × severity × antigen-persistence* design can separate
  the three explanations; and whether the effect reverses for agents that specifically block the
  self-sustaining loop (e.g. JAK/anti-IL-6R) vs those that impair clearance (anti-CD20).

## Connections to Project

- Related hypotheses: `hypothesis:0004` (host reserve/severity threshold), `hypothesis:0002` (antigen
  persistence — via impaired clearance), `hypothesis:0003` (exhaustion baseline).
- Required datasets: N3C is gated/below-bar per D-004; open-data routes flagged under t110.
- Required analyses: drug-class-stratified, severity-matched, immunosuppression-intensity-gradient design.
- Priority level: P2.

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais` (stratum A)
- Article notes: `paper:Vinson2024`, `paper:Peluso2022a`, `paper:Chavatza2025`
- Methods/Datasets:

## Notes

- 2026-07-06: Sharper design: solid-organ-transplant recipients on calcineurin-/mTOR-inhibitor immunosuppression as a human test of the immune-activation requirement — severity-matched vs immunocompetent controls with an immunosuppression-intensity gradient (existing SOT PASC studies report 35-49% but lack matched comparators / dose-gradient). (explore-ideas 2026-07-06 · cand-population-transplant-immunosuppression; anchors in meta:explore-2026-07-06)