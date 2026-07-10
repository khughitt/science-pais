---
id: "synthesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
kind: "synthesis"
title: "Synthesis: 0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` (phase: candidate) proposes
non-length-dependent autoimmune small-fiber neuropathy (SFN) as the shared peripheral structural
substrate of PAIS dysautonomia across PTLDS, long COVID, and ME/CFS.

**P1 (structural lesion, `proposition:0014-pais-small-fiber-structural-lesion-ienfd`)** is
net-supported but not universal. Skin-biopsy SFN is documented across long COVID (67% on
paired-site protocol, `evidence-line:0063-novak2026-largest-paired-biopsy-pais-sfn-supports-p1`),
ME/CFS (31%, `evidence-line:0039-joseph2021-mecfs-distal-biopsy-31pct-sfn-supports-p1`), and PTLDS
(`evidence-line:0044-adler2024-ptlds-leg-cross-syndrome-framing-supports-p4`), against 0% controls.
One adjudicated ME/CFS cohort returned a null, preserved as a genuine counterexample
(`evidence-line:0040-walitt2024-pimecfs-no-small-fiber-density-difference-disputes-p1`). The
apparent 0–91% prevalence scatter is driven by modality breadth, trigger, and referral-enrichment
rather than the scoring cutoff, per `interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`.

**P4 (cross-trigger convergence, `proposition:0017-pais-sfn-cross-trigger-convergence`)** reached
a first single-protocol two-trigger demonstration
(`evidence-line:0064-novak2026-single-protocol-two-trigger-convergence-supports-p4`). Novak2026's
hEDS arm — SFN comparable to PAIS in a non-infectious heritable dysautonomia — surfaces the first
specificity caveat against `question:0004-convergent-small-fiber-neuropathy-substrate`
(`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`).

**P2 (non-length-dependent pattern, `proposition:0015-pais-sfn-non-length-dependent-pattern`)** is
the least-measured leg: no per-subject NLD classification has been reported for infection-triggered
cohorts (`evidence-line:0065-novak2026-proximal-sgnfd-not-lesser-weakly-supports-p2`;
`evidence-line:0071-joseph2021-distal-only-sampling-scope-criticism-disputes-0015`).

**P3 and P18 (autoimmune causation and anti-GPCR route)** are contested. deSa2026 IgG passive
transfer causally demonstrates SFN
(`evidence-line:0045-desa2026-igg-transfer-causes-sfn-supports-immune-mediated`) but via non-GPCR
antigens without autonomic recapitulation. One functional α1-AR correlation survives as weak
positive evidence
(`evidence-line:0049-kharraziha2020-a1ar-activity-orthostatic-severity-supports-0018`) against a
binding-ELISA specificity null
(`evidence-line:0051-hall2022-elisa-nonspecific-disputes-0018`); no study links any anti-GPCR
antibody to the structural lesion
(`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`). Uncontrolled immunoadsorption
provides proof-of-concept for `proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory`
(`evidence-line:0047-stein2025-immunoadsorption-improves-autonomic-supports-0019`). Graph flags
`proposition:0014-pais-small-fiber-structural-lesion-ienfd`,
`proposition:0015-pais-sfn-non-length-dependent-pattern`, and
`proposition:0016-pais-sfn-autoimmune-causation` as `evidential_fragility(contested)`.

## Arc

The hypothesis was framed as the peripheral end-organ account of PAIS dysautonomia, occupying a
level downstream of the system-level attractor and immune-exhaustion frames.

`interpretation:0009-t049-sfn-cross-syndrome-ingestion` (task `t049`) opened the investigation by
coding seven papers into eleven evidence-lines. P1 and P4 emerged as the strongest legs; P2 was
"asserted more than measured" (only post-vaccine Limongelli2026 supplied a paired-site NLD
fraction); P3 was causally anchored for long COVID (deSa2026 passive transfer) but null in the
adjudicated ME/CFS cohort (Walitt2024). Primary-dysautonomia controls were absent from every
ingested study.

`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion` then formally contested
`proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity`: Hall2022 erased binding-ELISA
seroprevalence as evidence; Kharraziha2020's functional α1-AR correlation is the lone surviving
positive signal; the antibody-to-lesion bridge — functional anti-GPCR activity and IENFD measured
in the same subjects — remains entirely untested.

`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat` surfaced and ingested
Novak2026 during the
`pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls` vehicle hunt.
The largest paired-site series reinforced P1 and upgraded P4 to a single-protocol two-trigger
head-to-head, but also revealed hEDS SFN rates comparable to PAIS — shifting the central question
from "does the lesion exist?" to "is its pattern specific against primary dysautonomia?" The study
was ruled inadmissible for `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls` (hEDS is not a clean primary-dysautonomia arm).

`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis` resolved the
QASAT-vs-percentile question raised by
`interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`: modality breadth —
demonstrated within Novak2026 (48→67→91% on identical patients) — is the dominant prevalence
driver, not the cutoff rule. This validated `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls`'s within-subject
NLD-classification design and converted the alarming scatter into a coherent trigger × modality ×
referral table. The hypothesis stands at candidate with both promotion criteria blocked.

## Research fronts

**Open questions.** `question:0004-convergent-small-fiber-neuropathy-substrate` anchors criterion
#1: whether the PAIS SFN pattern is distinguishable from primary dysautonomia — now the harder
contrast following the hEDS specificity signal. `question:0009-functional-autoantibodies-drive-dysautonomia`
anchors criterion #2 and is adjudicated contested after
`interpretation:0010-t006-functional-gpcr-autoantibody-ingestion`; the antibody-to-lesion bridge
is the decisive missing measurement, co-measurable in `pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls`'s G5 serology arm.

**Open tasks and blocked work.** `t049` is complete. The
`pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls` vehicle search
is blocked on a clean G2 arm. The Novak group is identified as the most probable near-term source
(one protocol amendment from admissibility: add an idiopathic-POTS arm and re-score to percentile
cutoffs), per `interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat`.

**Graph fragility.**
`evidence-line:0070-novak2026-standardized-protocol-scope-criticism-disputes-0017` constrains P4:
under the only single-protocol study, cross-trigger convergence is two-trigger-only and non-specific
(hEDS ≥ PAIS), qualifying the standardized-substrate reading of
`proposition:0017-pais-sfn-cross-trigger-convergence`. Both promotion criteria remain open; h0007
stays at candidate.
