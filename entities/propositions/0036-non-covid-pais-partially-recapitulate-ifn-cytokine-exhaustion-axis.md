---
id: proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis
type: proposition
title: Non-COVID PAIS partially recapitulate the long-COVID IFN/cytokine/exhaustion axis, but not yet the full JAK-STAT/IL-6 dissociation pattern
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: local_proposition
discusses:
- frame: hypothesis:0003-immune-exhaustion-feedback
  role: background
related:
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0003-immune-exhaustion-feedback
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- paper:EatonFitch2024
- paper:Che2025
- paper:Keijmel2016
- paper:Morroy2016
- paper:Patterson2024
- interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map
- task:t060
source_refs:
- paper:EatonFitch2024
created: '2026-06-26'
updated: '2026-06-26'
---
# Proposition: Non-COVID PAIS partially recapitulate the long-COVID IFN/cytokine/exhaustion axis, but not yet the full JAK-STAT/IL-6 dissociation pattern

## Claim

The cross-PAIS half of `question:0006` is partly true: non-COVID PAIS, especially ME/CFS and Q-fever
fatigue syndrome, show recurring IFN/cytokine/exhaustion-axis abnormalities that overlap with the
long-COVID immune-exhaustion state. The recurrence is **partial**, not a demonstrated shared full state:
no non-COVID study yet co-measures sustained IL-6/JAK-STAT/type-II-IFN tone, blunted type-I antiviral
effectors, and exhaustion markers under the same design used for `proposition:0025`.

This is a **local q0006 proposition**, not a new core conjunct of `hypothesis:0003`. It maps the
generalizability question without changing h0003's load-bearing driver-vs-marker roll-up.

## Evidence Summary

`evidence-line:0089` (EatonFitch2024) supports the ME/CFS/long-COVID recurrence claim weakly: the same
NanoString immune-exhaustion panel found overlapping pathway themes across ME/CFS and long COVID,
including chemokine signaling, type I and II IFN, IL signaling, CTLA4, NF-kB, complement, and
Treg/exhausted-CD8 signals. This is the cleanest same-assay LC/ME/CFS support line for the cross-PAIS arm.

Other corpus evidence is consistent but not yet coded as direct support:
- Che2025 shows ME/CFS ex-vivo cytokine hyperreactivity before exercise and reduced HKCA-induced
  cytokines after exercise in females, interpreted as exercise-triggered immune exhaustion/dysregulation.
- Keijmel2016 shows QFS has elevated Coxiella-stimulated IFN-gamma versus seropositive recovered controls,
  with symptom-duration relationships in the IFN-gamma/IL-2 ratio.
- Morroy2016 summarizes QFS cytokine dysregulation involving IL-6, IL-2, and IFN-gamma, but not persistent
  uniform elevation.
- Patterson2024 is a counterweight: long COVID and chronic Lyme disease are distinguishable by plasma
  cytokine hubs (LC: IL-2/IFN-gamma and IL-6/VEGF/IL-10/sCD40L; CLD: TNF-alpha/IL-4), so recurrence of an
  inflammatory axis does not imply identical molecular state.

## Caveats

This proposition should stay below promotion strength. The current evidence map is heterogeneous across
assays (NanoString PBMC, ex-vivo stimulation, plasma cytokines, QFS antigen stimulation), compartments,
case definitions, and timepoints. It supports **pathway-family recurrence**, not the stricter Aid2025
claim that the same patients carry sustained IL-6/JAK-STAT/type-II IFN, blunted type-I antiviral-effector
ISGs, and exhaustion beyond 180 days. It also says nothing about causality; `proposition:0026` remains
data-gated on the JAK1-inhibitor readout.

## Needed Test

The decisive cross-PAIS test is a harmonized LC + ME/CFS + PTLDS/QFS cohort with the same blood
compartment, pathway scoring, and stimulation assays:

- Hallmark IL6-JAK-STAT3, IFN-gamma, IFN-alpha/type-I-effector ISGs, NF-kB/TNF, and complement scores.
- Exhaustion markers on CD8/T/NK cells, preferably single-cell rather than bulk.
- IFN-I stimulation response to distinguish tolerization from baseline deficiency.
- Antigen/persistence covariates where available.
- Time-since-trigger, acute severity, vaccination/variant, sex, age, BMI, and case-definition covariates.
