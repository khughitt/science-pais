---
id: hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
type: hypothesis
title: Skeletal-muscle ischemic-mitochondrial lesion as the primary substrate of post-exertional
  malaise
status: proposed
phase: candidate
source_refs:
- cite:Scheibenbogen2024
- cite:Appelman2024
- cite:Joseph2023
related:
- question:0011-mitochondrial-basis-of-pem
- question:0010-vascular-microclot-subphenotype
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-20'
updated: '2026-06-20'
---
# Hypothesis: Skeletal-muscle ischemic-mitochondrial lesion as the primary substrate of post-exertional malaise

## Organizing Conjecture

The primary substrate of post-exertional malaise (PEM) is a lesion in **skeletal muscle** — not the brain or circulating cells. During and after exertion, microvascular hypoperfusion / endothelial dysfunction produces muscle ischemia; the resulting ionic dysregulation (impaired Na⁺/K⁺ handling → intracellular Na⁺ accumulation → reverse-mode Na⁺/Ca²⁺ exchange → Ca²⁺ overload) damages mitochondria, which further impairs perfusion and energy supply, forming a self-perpetuating "acquired ischemic mitochondrial myopathy" (AIMM; Scheibenbogen2024). On this view PEM is the clinical signature of a muscle-localized vicious cycle that is **shared between post-COVID and ME/CFS**, and the delayed, disproportionate, slow-to-recover character of PEM reflects the time-course of ischemia–reperfusion–mitochondrial damage rather than a central/psychological process.

## Proposition Bundle

### Core Propositions

- **P1 (localization):** The bioenergetic deficit underlying PEM is localized *primarily* to skeletal muscle, rather than the CNS or circulating immune cells. *(subject: PEM bioenergetic deficit — predicate: is localized to — object: skeletal muscle)*
- **P2 (ischemic cause):** Microvascular hypoperfusion / endothelial dysfunction is causally **upstream** of the muscle bioenergetic failure (an ischemic mechanism), not merely co-occurring.
- **P3 (ionic mediator):** Ionic dysregulation — Na⁺ overload driving reverse-mode Na⁺/Ca²⁺ exchange and Ca²⁺ overload — mediates the step from hypoperfusion to mitochondrial damage.
- **P4 (self-perpetuation):** The lesion is self-perpetuating (mitochondrial damage → more ROS and worse perfusion → more damage), which is why PEM is delayed, exertion-triggered, and slow to recover.

### Supporting Or Auxiliary Propositions

- **A1:** The same muscle lesion underlies PEM in post-COVID and in ME/CFS (a shared substrate — a specific instance of `hypothesis:0001`).
- **A2:** Fibrinaloid microclots contribute by occluding capillaries (links `question:0010`) — but see the *Disputing Evidence* tension that muscle amyloid in long COVID was found **extravascular** (Appelman2024), which complicates a pure capillary-occlusion variant.

## Current Uncertainty

This is filed as **candidate** (not active) because the integrated AIMM model is largely **single-group** (Scheibenbogen / Wirth) and assembled from individually-plausible steps rather than one end-to-end validated pathway; the central ²³Na-MRI anchor (elevated intracellular muscle Na⁺) rests on a single cited study; and the authors disclose conflicts of interest (Wirth directs Mitodicure GmbH; Scheibenbogen holds diagnostic patents). The primary-vs-secondary problem is unresolved: muscle may be the *cause* of systemic PEM or simply one prominent downstream site. The strongest *independent* empirical support (Appelman2024, Joseph2023) confirms a provoked peripheral/muscle deficit but does **not** confirm the ionic cascade (P3) specifically.

## Predictions

- **Strong / discriminating:** (i) Two-day CPET (Keller2014) day-2 decline is driven by **peripheral O₂ extraction** (muscle), not central/cardiac limitation; (ii) post-exertional muscle biopsy shows mitochondrial damage and ionic-stress markers *escalating in the recovery window*, tracking PEM onset; (iii) interventions reducing Na⁺/Ca²⁺ overload or improving muscle perfusion improve PEM; (iv) CNS metabolic changes (e.g. Baraniuk2025 CSF) are *secondary to* and smaller than the muscle changes.
- **Weaker corollaries:** muscle-MRI perfusion deficits correlate with PEM severity; hand-grip strength inversely tracks intracellular Na⁺.

## Falsifiability

Confidence drops materially if: PEM persists with **normal** muscle perfusion and OXPHOS while the deficit localizes to CNS or circulating cells; provoked muscle biopsies show **no** escalating ionic/mitochondrial damage; perfusion-/ionic-targeted therapy fails while a CNS-targeted therapy succeeds; or the ²³Na-MRI intracellular-Na⁺ elevation fails to replicate independently. Walitt2024's central "effort-preference"/no-basal-mitochondrial-dysfunction findings are a standing competing frame that, if extended to the provoked state, would weaken P1.

## Promotion criteria

Promote candidate → active when: (1) an **independent** group (not Scheibenbogen/Wirth) replicates *either* elevated intracellular muscle Na⁺ *or* post-exertional escalation of muscle mitochondrial damage in a PEM-positive cohort with matched controls; **and** (2) peripheral (not central) O₂ extraction is shown to limit day-2 CPET in ≥2 independent cohorts. In short: the ischemic-ionic core (P2+P3) needs at least one independent confirmation beyond the originating group.

## Supporting Evidence

- **Scheibenbogen2024** (literature/model): the AIMM synthesis; ²³Na-MRI intracellular-Na⁺ anchor; staged PCS→ME/CFS transition model.
- **Appelman2024** (empirical, strongest independent support): long-COVID muscle OXPHOS reduced at baseline and *worse* after PEM, with a selective post-exertional fall in succinate-dehydrogenase (Complex II) activity — direct evidence of a provoked muscle bioenergetic lesion.
- **Joseph2023** (empirical): invasive CPET shows impaired *peripheral* O₂ extraction (preload failure + extraction defect) in both ME/CFS and PASC — consistent with the ischemic/peripheral locus (P2, P1).
- **Keller2014** (empirical, related): two-day CPET reproducibility loss — the provoked-state objective signature the model predicts.

## Disputing Evidence

- **Appelman2024** also found the muscle amyloid deposits to be **extravascular**, arguing against a simple capillary-occlusion (microclot) variant of P2/A2.
- **Walitt2024** (NIH deep phenotyping): emphasizes central features ("effort preference") and reports **no basal mitochondrial dysfunction** — a competing central framing that pressures P1.
- **Naviaux2016 / Germain2022**: systemic plasma-metabolome signatures (not muscle-specific) show the bioenergetic disturbance is at least partly *systemic*, not exclusively muscular.
- Single-group origin + disclosed COI of the integrated model (above).

## Evidence Needed To Shift Belief

The most discriminating next test is an **independent provoked muscle-biopsy time-course** (pre / immediately-post / 24–48 h post standardized exertion) measuring mitochondrial function *and* ionic markers (intracellular Na⁺/Ca²⁺), paired with peripheral-vs-central CPET decomposition, in a PEM-positive cohort with controls. A perfusion- or ionic-targeted intervention trial (with a muscle target-engagement readout) would test P2/P3 causally.

## Related Work

- Questions: `question:0011-mitochondrial-basis-of-pem` (the deficit this hypothesis proposes a *location and cause* for), `question:0010-vascular-microclot-subphenotype` (the vascular/microclot contribution), `question:0016-oxidative-stress-upstream-driver-of-bioenergetic` (ROS as the self-perpetuation step in P4).
- Hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (this is a tissue-specific instantiation), `hypothesis:0003-immune-exhaustion-feedback`.
- Papers: Scheibenbogen2024, Appelman2024, Joseph2023, Keller2014, Walitt2024, Baraniuk2025, Wang2023 (WASF3 supercomplex lesion), Syed2025.
