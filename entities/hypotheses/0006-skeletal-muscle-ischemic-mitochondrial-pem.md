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
- cite:Jones2012
- cite:Wong1992
- cite:Brown2015
- cite:Bizjak2024
related:
- question:0011-mitochondrial-basis-of-pem
- question:0010-vascular-microclot-subphenotype
- question:0016-oxidative-stress-upstream-driver-of-bioenergetic
- hypothesis:0001-shared-dysregulated-attractor
- discussion:0004-pem-shared-muscle-lesion-vs-endpoint-contingency
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- proposition:0030-mecfs-exercise-provoked-skeletal-muscle-bioenergetic-abnormality
- proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle
- proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure
- proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury
- proposition:0035-pem-muscle-lesion-is-self-perpetuating
- interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion
- evidence-line:0075-mecfs-muscle-bioenergetics-supports-0030
- evidence-line:0083-appelman-joseph-t056-muscle-localization-supports-h0006-p1
- evidence-line:0084-walitt2024-central-resting-null-weakly-disputes-h0006-p1
- evidence-line:0085-joseph2023-peripheral-extraction-weakly-supports-h0006-p2
- evidence-line:0086-appelman2024-no-occlusion-weakly-disputes-simple-ischemic-p2
- evidence-line:0087-scheibenbogen2024-na-ca-cascade-weakly-supports-h0006-p3
- evidence-line:0088-scheibenbogen2024-aimm-feedback-weakly-supports-h0006-p4
- task:t056
created: '2026-06-20'
updated: '2026-06-26'
review_state:
  last_reviewed: '2026-06-26'
  last_review_note: 'mode-C: prose Related Work cited question:0016 as the P4 ROS
    step but it was absent from frontmatter related; added question:0016 to related
    to match prose and carry the redox-direction dependency into the graph.'
---
# Hypothesis: Skeletal-muscle ischemic-mitochondrial lesion as the primary substrate of post-exertional malaise

## Organizing Conjecture

The primary substrate of post-exertional malaise (PEM) is a lesion in **skeletal muscle** — not the brain or circulating cells. During and after exertion, microvascular hypoperfusion / endothelial dysfunction produces muscle ischemia; the resulting ionic dysregulation (impaired Na⁺/K⁺ handling → intracellular Na⁺ accumulation → reverse-mode Na⁺/Ca²⁺ exchange → Ca²⁺ overload) damages mitochondria, which further impairs perfusion and energy supply, forming a self-perpetuating "acquired ischemic mitochondrial myopathy" (AIMM; Scheibenbogen2024). On this view PEM is the clinical signature of a muscle-localized vicious cycle that is **shared between post-COVID and ME/CFS**, and the delayed, disproportionate, slow-to-recover character of PEM reflects the time-course of ischemia–reperfusion–mitochondrial damage rather than a central/psychological process.

## Proposition Bundle

### Core Propositions

Formalized into the graph as durable propositions (`/science:specify-model`, 2026-06-26):
P1 → `proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle`,
P2 → `proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure`,
P3 → `proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury`,
P4 → `proposition:0035-pem-muscle-lesion-is-self-perpetuating`. All four are core bundle members, so
the hypothesis is a conjunction over localization, ischemic ordering, ionic mediation, and
self-perpetuation. `proposition:0030` remains an auxiliary/local proposition: it supports the ME/CFS
muscle-endpoint cell but is not a truth-condition of the full ischemic-ionic cascade.

- **P1 (localization → `proposition:0032`):** The bioenergetic deficit underlying PEM localizes
  materially to skeletal muscle, rather than being only central, circulating-cell, or deconditioning
  mediated. This leg is the best-supported: Appelman2024 + Joseph2023 + the t056 ME/CFS muscle body
  support it, while Walitt2024 weakly contests the primary-muscle generalization.
- **P2 (ischemic cause → `proposition:0033`):** Microvascular hypoperfusion / endothelial dysfunction is
  causally **upstream** of the muscle bioenergetic failure (an ischemic or extraction mechanism), not
  merely co-occurring. This leg is weak/contested: Joseph2023 supports a peripheral extraction/delivery
  abnormality, while Appelman2024 argues against a simple capillary-occlusion or hypoxia variant.
- **P3 (ionic mediator → `proposition:0034`):** Ionic dysregulation — Na⁺ overload driving reverse-mode
  Na⁺/Ca²⁺ exchange and Ca²⁺ overload — mediates the step from hypoperfusion to mitochondrial damage.
  This is the weakest mechanistic leg and currently rests on the Scheibenbogen/Wirth AIMM synthesis plus
  the cited ²³Na-MRI sodium anchor.
- **P4 (self-perpetuation → `proposition:0035`):** The lesion is self-perpetuating (mitochondrial damage
  → more ROS and worse perfusion/ion handling → more damage), explaining delayed, exertion-triggered,
  slow-to-recover PEM. This remains weak and model-heavy pending longitudinal muscle time-course data.

### Supporting Or Auxiliary Propositions

- **A1 (endpoint-bound):** Post-COVID and ME/CFS PEM share the *same muscle-endpoint lesion* — specifically, a post-exertional muscle-OXPHOS decline of the Appelman2024 type that appears in **both** triggers under a harmonized protocol. This is a tissue-specific instance of `hypothesis:0001`, but it is **constrained by `proposition:0029` (h0008-M3)**: the cross-trigger *whole-body* 2-day-CPET signature does **not** transfer (Keller2014 ME/CFS-positive vs Gattoni2025 long-COVID-null), so A1's sharing claim must be demonstrated at the **muscle endpoint**, not inferred from shared symptoms or assumed across endpoints. `task:t056` found that ME/CFS does have muscle-endpoint bioenergetic abnormalities (`proposition:0030`: Jones2012/Wong1992/Brown2015/Bizjak2024), so the prior "empty ME/CFS muscle cell" is narrowed to a more precise gap: no harmonized ME/CFS Appelman-type post-PEM OXPHOS/SDH biopsy time-course has been published.
- **A2:** Fibrinaloid microclots contribute by occluding capillaries (links `question:0010`) — but see the *Disputing Evidence* tension that muscle amyloid in long COVID was found **extravascular** (Appelman2024), which complicates a pure capillary-occlusion variant.

## Current Uncertainty

This is filed as **candidate** (not active) because the newly formalized bundle exposes an asymmetric
evidence surface. P1/localization is supported but contested; P2/ischemic ordering is weak and contested;
P3/ionic mediation and P4/self-perpetuation are weak, model-heavy legs. The integrated AIMM model is
largely **single-group** (Scheibenbogen / Wirth) and assembled from individually-plausible steps rather
than one end-to-end validated pathway; the central ²³Na-MRI anchor (elevated intracellular muscle Na⁺)
rests on a single cited study; and the authors disclose conflicts of interest (Wirth directs Mitodicure
GmbH; Scheibenbogen holds diagnostic patents). The primary-vs-secondary problem is unresolved: muscle may
be the *cause* of systemic PEM or simply one prominent downstream site. The strongest *independent*
empirical support (Appelman2024, Joseph2023, plus the t056 ME/CFS muscle-bioenergetics body) confirms a
provoked peripheral/muscle deficit, but it does **not** confirm the ischemic upstream step (P2), ionic
cascade (P3), self-maintaining feedback (P4), or same-lesion cross-trigger A1 specifically.

## Predictions

- **Strong / discriminating:** (i) Two-day CPET (Keller2014) day-2 decline is driven by **peripheral O₂ extraction** (muscle), not central/cardiac limitation; (ii) post-exertional muscle biopsy shows mitochondrial damage and ionic-stress markers *escalating in the recovery window*, tracking PEM onset; (iii) interventions reducing Na⁺/Ca²⁺ overload or improving muscle perfusion improve PEM; (iv) CNS metabolic changes (e.g. Baraniuk2025 CSF) are *secondary to* and smaller than the muscle changes.
- **Weaker corollaries:** muscle-MRI perfusion deficits correlate with PEM severity; hand-grip strength inversely tracks intracellular Na⁺.

## Falsifiability

Confidence drops materially if: PEM persists with **normal** muscle perfusion and OXPHOS while the deficit localizes to CNS or circulating cells; provoked muscle biopsies show **no** escalating ionic/mitochondrial damage; perfusion-/ionic-targeted therapy fails while a CNS-targeted therapy succeeds; or the ²³Na-MRI intracellular-Na⁺ elevation fails to replicate independently. Walitt2024's central "effort-preference"/no-basal-mitochondrial-dysfunction findings are a standing competing frame that, if extended to the provoked state, would weaken P1.

## Promotion criteria

Promote candidate → active when: (1) an **independent** group (not Scheibenbogen/Wirth) replicates *either* elevated intracellular muscle Na⁺ *or* post-exertional escalation of muscle mitochondrial damage in a PEM-positive cohort with matched controls; **and** (2) peripheral (not central) O₂ extraction is shown to limit day-2 CPET in ≥2 independent cohorts; **and** (3, the cross-trigger sharing test — added 2026-06-24 per `discussion:0004`, narrowed 2026-06-25 by `interpretation:0019`) the post-exertional muscle-OXPHOS lesion is confirmed in **ME/CFS** at the muscle endpoint, set beside the long-COVID lesion (Appelman2024) — ideally within one harmonized multi-endpoint protocol, but at minimum a comparable independent ME/CFS post-exertion biopsy result. Jones2012/Wong1992/Brown2015/Bizjak2024 partially satisfy the weaker proposition "ME/CFS has muscle bioenergetic abnormalities" (`proposition:0030`) but **do not** satisfy criterion #3 because their endpoints are 31P-MRS pH/ATP kinetics, in-vitro contraction signaling, or resting biopsy morphology rather than Appelman-type post-PEM OXPHOS/SDH kinetics.

## Supporting Evidence

- **Scheibenbogen2024** (literature/model; `evidence-line:0087`, `evidence-line:0088`): the AIMM
  synthesis; ²³Na-MRI intracellular-Na⁺ anchor; staged PCS→ME/CFS transition model. Supports the P3/P4
  mechanism weakly, not as independent end-to-end validation.
- **Appelman2024** (empirical, strongest independent support; `evidence-line:0083`): long-COVID muscle
  OXPHOS reduced at baseline and *worse* after PEM, with a selective post-exertional fall in
  succinate-dehydrogenase (Complex II) activity — direct evidence of a provoked muscle bioenergetic
  lesion. Also contributes a mechanism constraint (`evidence-line:0086`) because amyloid was
  extravascular and no simple occlusion/hypoxia signal was found.
- **Joseph2023** (empirical/synthesis; `evidence-line:0085`): invasive CPET shows impaired *peripheral*
  O₂ extraction (preload failure + extraction defect) in both ME/CFS and PASC — consistent with the
  ischemic/peripheral locus (P2, P1), but not a direct causal test.
- **t056 ME/CFS muscle-bioenergetics body** (`proposition:0030`, `evidence-line:0075`): Jones2012 repeated-exercise 31P-MRS shows excess intramuscular acidosis and delayed pH recovery; Wong1992 shows lower ATP at exhaustion during 31P-NMR exercise; Brown2015 shows impaired contraction-stimulated AMPK/glucose uptake in CFS-derived muscle cells; Bizjak2024 shows direct muscle mitochondrial abnormalities in CFS/post-COVID. This supports muscle localization but not Appelman-equivalent cross-trigger sharing.
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

## Notes

- 2026-06-20: Deflationary rivals now tracked as question:0017 — deconditioning/inactivity and nocebo/illness-perception accounts. Both are constrained (not eliminated) by Appelman2024 muscle pathology and invasive/2-day CPET; hold nocebo as a possible subgroup contributor, not a whole-syndrome explanation.
- 2026-06-24: A1 endpoint-bound and promotion criterion #3 added per `discussion:0004` (head-to-head vs h0008-M3 / `proposition:0029`). The Organizing Conjecture's "shared between post-COVID and ME/CFS" is the frame's aspiration; A1 now carries the **precise, testable** form — sharing must be shown at the **muscle endpoint** (post-exertional OXPHOS, Appelman2024-type), because the *whole-body* 2-day-CPET signature demonstrably does not transfer across triggers (Keller2014 vs Gattoni2025). The decisive ME/CFS muscle-endpoint datum does not yet exist; `task:t056` is the interim literature probe, a harmonized multi-endpoint cross-trigger study the decisive (data-gated) test.
- 2026-06-25: `task:t056` completed (`interpretation:0019`). The "no ME/CFS muscle datum" premise is retired. ME/CFS has muscle-endpoint bioenergetic abnormalities, now coded as `proposition:0030`, but the Appelman-equivalent cross-trigger biopsy time-course remains absent. A1 is therefore strengthened at localization and still unproven at same-lesion equivalence.
- 2026-06-26: `science:specify-model` formalized h0006's four core legs as `proposition:0032`–`0035`
  and coded six evidence-lines (`0083`–`0088`). The graph now reflects the honest asymmetry: the muscle
  localization pillar is supported but contested; the ischemic upstream leg is weak/contested; the ionic
  and self-perpetuation legs remain weak mechanistic inferences. `proposition:0030` stays auxiliary/local
  rather than over-crediting the full h0006 bundle.
