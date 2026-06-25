---
id: proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
type: proposition
title: Persistent JAK-STAT/IL-6 activation coupled with T-cell exhaustion is a proximal
  causal driver of long-COVID chronicity (reversible by pathway inhibition), not merely
  a downstream marker
status: active
claim_layer: causal_effect
identification_strength: interventional
proxy_directness: indirect
supports_scope: hypothesis_bundle
measurement_model:
  observed_entity: JAK1 inhibition with pathway-suppression biomarkers, inflammatory-endotype stratification, and symptom response
  latent_construct: proximal causal maintenance of long-COVID chronicity by the JAK-STAT/IL-6/exhaustion loop
  measurement_relation: pharmacologic pathway inhibition is an indirect driver test; causal support requires co-occurring pathway suppression and symptom improvement in the relevant endotype
  known_failure_modes:
  - pathway suppression without symptom benefit implies marker-not-driver or wrong endotype
  - dose, duration, or single-node targeting may be insufficient for a multi-loop chronic state
  - unstratified nulls can dilute a true inflammatory-endotype effect
discusses:
- hypothesis:0003-immune-exhaustion-feedback
related:
- pre-registration:0004-jak1-inhibitor-driver-vs-marker
- hypothesis:0003-immune-exhaustion-feedback
- question:0006-jak-stat-il6-driver-vs-marker
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- topic:long-covid-immune-dysregulation
- topic:therapeutics-and-clinical-trials
- task:t047
- task:t054
source_refs: []
created: '2026-06-24'
updated: '2026-06-25'
---
# Proposition: Persistent JAK-STAT/IL-6 activation coupled with T-cell exhaustion is a proximal causal driver of long-COVID chronicity (reversible by pathway inhibition), not merely a downstream marker

## Claim

The persistent JAK-STAT/IL-6 activation, coupled with T-cell exhaustion, is a **proximal causal driver**
of long-COVID chronicity — its pharmacological inhibition will **reduce symptoms**, not merely suppress a
biomarker — rather than a downstream **marker** of an upstream lesion (antigen persistence, autoimmunity).
Subject = persistent JAK-STAT/IL-6 + exhaustion signaling; predicate = *causally maintains* (is
reversible-by-inhibition); object = post-acute symptom burden. This is the **causal-loop / maintenance-
engine conjunct** of `hypothesis:0003` and the exact content of `question:0006` (driver vs marker).

## Evidence Summary

**No coded evidence — this is an untested `causal_effect` claim, held at `speculative`.** The supporting
material to date is *observational and correlational only*: Aid2025 shows the activation+exhaustion
signature co-varies with symptom counts (fatigue, dyspnoea, brain fog) and frames it as a failed
negative-feedback loop, but cross-sectional multi-omics cannot establish direction (driver vs marker) or
reversibility. The discriminating test is **interventional** and is committed in
`pre-registration:0004-jak1-inhibitor-driver-vs-marker` (data-gated), whose vehicle is the **abrocitinib
(JAK1 inhibitor) RCT, NCT06597396**:
- a **symptom-reduction + pathway-suppression co-endpoint** → upward evidence for the driver reading
  (this proposition gains a supporting line);
- **pathway suppression without symptom benefit** → **marker, not driver** (a disputing line, and a
  falsifier for `hypothesis:0003`'s maintenance-engine framing).

Until that readout, the standing verdict is `[?]` inconclusive-for-coverage — **no `bears_on` update**.

**Registry-status update (t054, 2026-06-25).** NCT06597396/CLEAR-LC has passed primary completion in the
ClinicalTrials.gov record (2026-03-27 actual), but no results are posted (`hasResults: false`) and study
completion remains estimated for 2026-09-30. The registry endpoint list includes FACIT-Fatigue, EQ-5D-5L,
PASC Symptom PRO, safety/labs, and hsCRP; it does **not** by itself establish the IL-6R/JAK-STAT/ISG
target-engagement readout or inflammatory-endotype stratification required by `pre-registration:0004`.
So this proposition remains untested.

## Caveats

`identification_strength: interventional`, `proxy_directness: indirect` — a JAK1 inhibitor is a **proxy
for "the loop is the operative driver"**: a null could mean *marker-not-driver*, but could also mean the
agent/dose/duration/endotype was wrong (e.g. benefit only in the inflammatory endotype, per
`proposition:0025`'s dissociation; a single-agent hitting one node of a multi-loop attractor, per
`hypothesis:0001`; Seo2025's broad single-agent nulls). The pre-registration's decision criteria must
therefore gate on endotype-stratified, co-endpoint design — a flat null in an unstratified trial is weaker
disconfirmation than a null in the inflammatory-signature-positive subgroup. This proposition is the
**untested causal pillar** that keeps `hypothesis:0003` honestly `speculative` even though its descriptive
state-conjunct (`proposition:0025`) is supported.
