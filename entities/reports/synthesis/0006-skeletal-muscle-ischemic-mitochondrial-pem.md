---
type: synthesis
title: "Synthesis: 0006-skeletal-muscle-ischemic-mitochondrial-pem"
report_kind: hypothesis-synthesis
id: synthesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
hypothesis: hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
generated_at: 2026-06-24T03:28:17Z
source_commit: eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec
provenance_coverage: partial
---

## State

`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` is a **candidate** frame proposing that PEM's
primary substrate is a lesion in skeletal muscle: microvascular hypoperfusion produces ischemia, ionic
dysregulation (Na⁺ overload → reverse-mode Na⁺/Ca²⁺ exchange → Ca²⁺ overload) damages mitochondria, and
the resulting vicious cycle — the "acquired ischemic mitochondrial myopathy" (AIMM) — accounts for PEM's
delayed onset and slow recovery in both post-COVID and ME/CFS.

The strongest independent empirical anchor is the Appelman2024 finding (cited in
`interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`) that long-COVID
muscle OXPHOS is impaired at baseline and worsens after provoked PEM, with a selective post-exertional fall
in Complex II activity — direct evidence of a provoked peripheral muscle bioenergetic lesion. Joseph2023
(cited in the hypothesis body) adds invasive-CPET support for impaired peripheral O₂ extraction in both
ME/CFS and PASC, consistent with propositions P1 (muscle localization) and P2 (ischemic cause).

However, the ionic-cascade core (proposition P3) and the self-perpetuation claim (P4) rest on a
single-group synthesis (Scheibenbogen/Wirth; COI disclosed) and a single ²³Na-MRI anchor, neither
independently replicated. `proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode`
(supported, support=4, dispute=0) adds a further qualification: PEM's objective correlate shifts with
trigger and endpoint — the ME/CFS whole-body 2-day-CPET decrement does not appear in long COVID at
the same endpoint, even when a muscle-level lesion does. This means the muscle hypothesis is plausible
for long COVID but cannot be assumed to generalize as the single unified failure mode across PAIS.
Walitt2024 (cited in the hypothesis body) represents a competing central frame that pressures P1.

## Arc

Arc reconstruction is limited: only one interpretation reaches this hypothesis (via `question:0011`),
and it was primarily framed for `hypothesis:0001`. The arc can be traced but is partly borrowed.

`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` was created 2026-06-20 as a
tissue-specific instantiation of `hypothesis:0001-shared-dysregulated-attractor`, narrowing the
PEM substrate claim to skeletal muscle. It entered as `candidate` because the AIMM model was
recognised from the outset as single-group, assembled from individually plausible steps without
end-to-end validation.

The first substantive interpretive work touching this hypothesis came through `task:t025`, whose
findings are recorded in
`interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`.
That task set out to find within-cohort PEM-stratified molecular contrasts; it found instead that
the decisive design does not yet exist, and that PEM's objective correlate dissociates by trigger
and endpoint. The Appelman2024 muscle result — incorporated into `proposition:0011` via
`interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation` — is
the strongest current empirical anchor for the muscle-localization claim (P1/P2). A subsequent
sweep (`task:t044`, feeding `interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands`)
confirmed that the severity-adjusted PEM-stratified molecular contrast remains uncomputable from
public data, leaving the key gap behind `question:0011-mitochondrial-basis-of-pem` open.

The current epistemic position: muscle-level bioenergetic pathology after provoked PEM in long COVID
is supported by independent data, but the ischemic-ionic cascade (P3), self-perpetuation (P4), and
cross-PAIS generalization (A1) are not independently confirmed. The hypothesis remains candidate
pending replication from outside the originating group.

## Research fronts

**Live questions:**

- `question:0011-mitochondrial-basis-of-pem` — What is the mitochondrial/bioenergetic basis of PEM, and
  is it shared across PAIS? The muscle endpoint is partially anchored (Appelman2024 via
  `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`) but the
  whole-body CPET signal does not transfer to long COVID (Gattoni2025, held at weak/underpowered in
  `proposition:0011`), and the ionic-cascade mechanism is unreplicated.
- `question:0010-vascular-microclot-subphenotype` — The microclot/capillary-occlusion variant of P2/A2
  is complicated by Appelman2024's finding that muscle amyloid is extravascular.
- `question:0017-deflationary-alternatives-vs-shared-pathophysiology` — Deconditioning and
  central/effort-preference accounts (Walitt2024) remain live rivals; Appelman2024 and invasive CPET
  constrain but do not eliminate them.

**Promotion criteria (from hypothesis body):** candidate advances to active when (1) an independent
group replicates elevated intracellular muscle Na⁺ or post-exertional escalation of muscle
mitochondrial damage in a PEM-positive cohort with controls, and (2) peripheral O₂ extraction is
shown to limit day-2 CPET in at least two independent cohorts.

**Discriminating next test:** an independent provoked muscle-biopsy time-course (pre / immediately
post / 24–48 h post standardized exertion) measuring mitochondrial function and ionic markers, paired
with peripheral-vs-central CPET decomposition, in a PEM-positive cohort with matched controls. A
perfusion- or ionic-targeted intervention trial with muscle target-engagement readout would test P2/P3
causally.
