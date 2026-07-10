---
id: "synthesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent"
kind: "synthesis"
title: "Synthesis: 0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-07-10"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` is a methodological meta-hypothesis: it asserts that apparent PAIS group differences inflate in self-report and selection-enriched measurement channels and attenuate toward null or reverse under objective, trigger-matched, ascertainment-controlled re-measurement — in a direction predictable enough to serve as a prior. Three core propositions carry the claim: M1 (`proposition:0027-pais-group-differences-attenuate-under-objective-re-measurement`, channel-direction regularity), M2 (`proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring`, ascertainment-and-scoring inflation), and M3 (`proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific`, endpoint/construct instability).

The decisive evidential step is `interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences` (`task:t055`), which coded 11 corpus group-difference claims by channel, ascertainment-control, and behavior under objective re-measurement. Six of 9 determinate claims are artifact-consistent; self-report and mixed-origin claims attenuate 4/4 (`evidence-line:0066-t055-audit-m1-channel-direction-cut-supports`) and weak-ascertainment claims collapse 3/3 (`evidence-line:0067-t055-audit-m2-sfn-harmonization-supports`). Objective-origin claims are mixed (3 survive, 2 artifact-consistent), so there is no clean "objective implies survives" rule. The bounded exception set (n=3) — `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment` (male vascular hard-endpoint reversal), `proposition:0013-immune-domain-partial-hormone-mediated-objective-exception` (testosterone-conditioned female immune activation), `proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn` (long-COVID persistent inflammatory activation, two cohorts, >180 days) — is load-bearing: it keeps the hypothesis falsifiable and tracks the accumulation rate of genuine objective signals as the running meter. Promotion criterion #1 is met; criterion #2 (same-cohort prospective objective re-measurement) remains open, holding status at `candidate`.

## Arc

The investigation opened not from h0008 but from four parallel lines that each produced a methodologically anomalous finding. `task:t013` and `task:t018`, culminating in `interpretation:0003-t018-subphenotype-sex-reproductive-stage`, decomposed the PAIS female excess by subphenotype and found it concentrated in self-report domains; the objective immune signal was testosterone-conditioned (`proposition:0013-immune-domain-partial-hormone-mediated-objective-exception`), organizing the excess along a measurement-channel axis rather than a menopausal one.

Concurrently, `task:t025` established that the ME/CFS whole-body CPET decrement does not transfer to long COVID at that endpoint even where a muscle OXPHOS lesion was independently documented — the M3 anchor (`proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific`), grounded in `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`. The SFN-prevalence arm (`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`) demonstrated that an apparent 0→91% cross-study prevalence range decomposes into modality breadth, trigger, and referral enrichment rather than biology — the M2 anchor (`proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring`). Each instance was embedded in a different host hypothesis (h0001, h0005, h0006, h0007) rather than recognized as a shared regularity.

The 2026-06-24 specify-model pass formalized the structure: M1–M3 were minted as native propositions and `task:t055` executed the systematic audit (`interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences`), converting belief from "pattern noticed" to "rate estimated" — 6/9 determinate claims artifact-consistent, bounded exception set established at n=3, and promotion criterion #1 declared met.

## Research fronts

**Live questions.** `question:0014-which-pais-case-definition-is-most-biologically-coherent` and `question:0015-does-pem-requirement-improve-cross-study-comparability` probe the ascertainment-inflation limb (M2) in case-definition space. `question:0018-objective-vs-subjective-cognition-dissociation-in` is the sharpest prospective M1 test; currently the evidence is retrospective and cross-study only (`proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing` — female cognitive excess absent in objective neuropsychological testing, present in self-report).

**Open design gap.** All bundle tasks are marked done. The remaining belief-shifting route is promotion criterion #2: a same-cohort, trigger-matched objective re-measurement of a self-report-established PAIS difference. `pre-registration:0005-harmonized-provoked-muscle-endpoint` is adjacent but narrower — it adjudicates M3 for PEM endpoint-contingency without testing M1 or M2.

**Evidential fragility.** The gaps_slice flags `proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode` and its host hypotheses (`hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0005-reproductive-stage-immune-homeostatic-margin`, `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`, `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate`) as `evidential_fragility(contested)`. Because M3 currently rests on a single PEM phenotype instance (`evidence-line:0069-t055-audit-m3-pem-endpoint-contingent-supports`), its contested status directly limits M3's generalizability; the prospective same-cohort design (criterion #2) remains the only path capable of resolving this gap.
