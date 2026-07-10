---
id: "synthesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
kind: "synthesis"
title: "Synthesis: 0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-07-10"
updated: "2026-07-10"
provenance_coverage: "thin"
---

## State

Hypothesis 0009 is in `phase: candidate`, `status: proposed`. Its central claim is that post-infectious latent autoimmunity — the large gap between near-universal latent autoantibody carriage and the small fraction with overt disease at a 7-month cross-section, which motivates `question:0005-latent-to-overt-autoimmunity-conversion` — is not a transient molecular-mimicry phenomenon but an early marker of a durable immune-set-point shift. The conjecture holds that, in a minority susceptible subset, this displaced immune state progresses to clinically overt autoimmune disease over a 5–10-year horizon.

Three propositions remain untested at the conversion step: (1) that post-infectious latent autoimmunity raises the hazard of incident overt autoimmune disease above the age/sex-matched uninfected baseline; (2) that early anti-cytokine / anti-IFN autoantibody breadth stratifies who converts (a predictive-marker claim); and (3) that conversion reflects durable immune reprogramming, separable from transient mimicry by autoantibody persistence in converters versus decay in non-converters — per the open operands of `question:0005-latent-to-overt-autoimmunity-conversion`.

A load-bearing confound is the sex/ascertainment overlap between autoimmunity and PAIS. `interpretation:0032-t079-bc3-autoimmune-stratum-granularity` reinforces this concern on the exposure side: autoimmune-thyroid strata carry plausibly differential exposure misclassification in both the N3C and OpenSAFELY EHR vehicles. That same interpretation establishes that the genetic-risk-only diathesis arm of `question:0005-latent-to-overt-autoimmunity-conversion` — the latent→overt test most directly relevant to this hypothesis — is not derivable from diagnosis-code tables and requires a genotype-linked data modality.

## Arc

Arc reconstruction is limited: the bundle contains one interpretation (`interpretation:0032-t079-bc3-autoimmune-stratum-granularity`), which concerns reverse-arrow infrastructure work rather than the forward-arrow conversion claim, and no `prior_interpretations` chains exist for this hypothesis.

Hypothesis 0009 was created 2026-07-01 to give `question:0005-latent-to-overt-autoimmunity-conversion` a formal home after it was flagged as the sole orphan question with a drafted but uncreated candidate hypothesis. The complementary reverse-arrow work — pre-existing autoimmune diathesis as a sex-conditioned effect-modifier of PAIS risk — was housed in `task:t078` (now done), clarifying that the forward and reverse arrows are logically distinct and share a sex-confounding trap without entailing each other. `interpretation:0032-t079-bc3-autoimmune-stratum-granularity` subsequently established EHR vocabulary resolvability for disease-specific autoimmune strata across both admissible vehicles and identified the latent→overt genotype-linked arm as outside the reach of current EHR codeset infrastructure. The hypothesis remains a candidate framing: no prospective vehicle has been identified and the core conversion trajectory is untested.

## Research fronts

The primary live question is `question:0005-latent-to-overt-autoimmunity-conversion` (inverse, confidence 0.8): what fraction of post-infectious latent autoantibody carriers convert to overt autoimmune disease, over what horizon, and which early autoantibody repertoire features identify high-risk subsets.

No open tasks are listed in the bundle for this hypothesis; `task:t078` (done) concerns the complementary reverse-arrow framing. Promotion from candidate requires identifying either a prospective post-infectious cohort with baseline autoantibody profiling and ≥3–5-year overt-autoimmune outcomes, or a sex- and ascertainment-adjusted re-analysis of large-cohort new-onset-autoimmune hazard data with an autoantibody linkage (`question:0005-latent-to-overt-autoimmunity-conversion`).

Three methodological blockers remain: (1) no admissible prospective vehicle has been identified; (2) the sex/ascertainment confound requires a matched uninfected comparator with differential-testing controls, a bar not cleared by available retrospective EHR hazard estimates; (3) distinguishing durable reprogramming from transient mimicry requires longitudinal autoantibody kinetics absent from current cross-sectional data.
