---
id: synthesis:emergent-threads
type: synthesis
title: "Emergent threads - health-post-acute-infection"
report_kind: emergent-threads
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
orphan_question_count: 1
orphan_interpretation_count: 0
orphan_ids: ["question:0005-latent-to-overt-autoimmunity-conversion"]
---

## Cross-hypothesis questions

Four questions show cross-hypothesis reach at confidence `inverse`, `back-inverse`, or `transitive`
across at least two distinct hypotheses.

**question:0009-functional-autoantibodies-drive-dysautonomia** resolves primarily to
`hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` and carries a back-inverse link to
`hypothesis:0001-shared-dysregulated-attractor`. The cross-cutting nature is significant: functional
GPCR autoantibodies are both a candidate mechanism for the autonomous peripheral-neuropathy substrate
(h0007) and a potential self-sustaining loop within the broader attractor (h0001), making this
question the sharpest current bridge between the structural-lesion frame and the systemic-feedback
frame. The assay-dependent evidence split — functional-assay correlations survive (Kharraziha2020)
while binding-ELISA seropositivity does not discriminate (Hall2022) — means the cross-hypothesis
reach tracks different evidence standards than either hypothesis alone requires.

**question:0011-mitochondrial-basis-of-pem** resolves primarily to
`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` and carries a back-inverse link to
`hypothesis:0001-shared-dysregulated-attractor`. It sits at the seam between a focal muscle-ischemia
account and the shared-attractor account: if the mitochondrial deficit is confined to skeletal muscle
under ischemic microclot load, h0006 is confirmed; if it is systemic (metabolic reprogramming of
immune cells), it feeds into h0001. The two hypotheses make different predictions on whether
mitochondrial dysfunction normalises with microclot clearance or persists independently.

**question:0007-mechanism-of-female-predominance-in-pais** resolves primarily to
`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` with a transitive link to
`hypothesis:0004-acute-severity-threshold`. The male-biased reversal on cardiovascular hard endpoints
(`interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment`,
`proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment`) forces the
severity-threshold account into the same explanatory space as the sex-hormone account, because the
female fatigue excess and the male vascular excess are co-present in the same post-acute window and
require both hypotheses to be explained.

**question:0019-male-biased-vascular-signal-pasc-persistence** resolves primarily to
`hypothesis:0004-acute-severity-threshold` and also reaches
`hypothesis:0005-reproductive-stage-immune-homeostatic-margin`. It bridges these two hypotheses by
asking whether the male post-acute cardiovascular excess (documented in Kopp2024 at 18 months within
a hospitalized-only stratum) reflects a severity carryover or a genuinely sex-differentiated vascular
repair biology — a distinction h0004 and h0005 cannot individually resolve. The companion question
`question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover` adds a further
complication: none of the current evidence lines include an uninfected comparator, so the
infection-attributable fraction of the male vascular signal remains unidentified, conditioning both
hypotheses simultaneously.

---

## Orphan questions

Total: **1**

**question:0005-latent-to-overt-autoimmunity-conversion** asks what fraction of post-infectious
latent autoimmunity converts to overt autoimmune disease over a 5–10 year horizon and which
autoantibody subsets (particularly anti-cytokine/anti-IFN specificities) mark the highest-risk
patients. The resolver assigns no hypothesis because no current hypothesis frames the *longitudinal
progression* from latent to clinical autoimmunity: `hypothesis:0001-shared-dysregulated-attractor`
mentions autoimmunity as one attractor-state input but does not predict conversion rates or risk
stratification; the remaining hypotheses operate on mechanism rather than prognosis. The question's
home topic is `topic:post-infectious-dysautonomia-and-autoimmunity`, where Rojas2022 (83% latent
autoimmunity, only ~3% with overt disease at 7 months) and Sharma2023 (elevated new-onset
autoimmune-disease hazard ratios in large retrospective cohorts) establish the phenomenon without
resolving the conversion trajectory. What would give this question a hypothesis home: a formal
hypothesis that "post-infectious immune-set-point shift in a minority subset results in clinical
autoimmune conversion over years, with anti-cytokine autoantibody breadth as the stratifying
predictor" — extending h0001 into the longitudinal autoimmune-prognosis domain.

---

## Orphan interpretations

Total: **0**

All 14 active interpretations carry at least one direct or transitive `hypothesis:` link via their
`related:` fields. No orphan interpretations exist in this run.

---

## Candidate hypotheses

**Post-infectious immune-set-point shift and long-term autoimmune conversion.** The sole orphan
question (`question:0005`) concerns a longitudinal-prognosis claim that sits between
`hypothesis:0001-shared-dysregulated-attractor` (attractor-state framing) and the autoimmunity
material in `topic:post-infectious-dysautonomia-and-autoimmunity`, but is addressed by neither.
Rojas2022's near-universal latent autoimmunity and the unexplained gap between 83% autoantibody
prevalence and ~3% overt disease at 7 months is precisely the unhoused empirical kernel. A candidate
hypothesis: "In a minority post-infectious subset, latent autoimmunity reflects durable immune
reprogramming rather than a transient mimicry response, with anti-cytokine/anti-IFN autoantibody
breadth predicting clinical conversion over a multi-year horizon." Promoting this to a formal
hypothesis would require a long-term prospective cohort design and would pull in Sharma2023, Rojas2022,
and Ciaffi2023 as founding evidence lines.

**Measurement-ascertainment axis as a standing hypothesis-constraint.** Not a new hypothesis, but
`topic:measurement-ascertainment-artifacts-in-pais` now has sufficient grounded structure — spanning
`hypothesis:0001`, `hypothesis:0005`, `hypothesis:0006`, and `hypothesis:0007` — that it functions
as a cross-hypothesis meta-constraint. The SFN skin-biopsy harmonization case
(`interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`) shows that an apparent 0%–91%
prevalence range across Walitt2024, Novak2026, Oaklander2022, and Joseph2021 is largely decomposable
into modality breadth, trigger (LC vs ME/CFS), and referral enrichment rather than biological
heterogeneity. This pattern recurs across cognition (`proposition:0010`), PEM endpoints
(`proposition:0011`), and dysautonomia sex-skew (`proposition:0009`). Formalising the measurement-
channel axis as an explicit methodological hypothesis — "apparent group or cross-trigger differences
in PAIS phenotypes will preferentially concentrate in self-report or referral-enriched channels and
attenuate or reverse under objective, trigger-matched measurement" — would give it testable content
and prevent downstream over-interpretation of new signals before ascertainment is controlled.
