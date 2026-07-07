---
id: question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal
kind: question
title: "IFN-I \u2192 tryptophan malabsorption \u2192 platelet serotonin depletion\
  \ \u2192 vagal hypofunction as a causal chain for PAIS cognitive impairment"
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Wong2023
- cite:Trautmann2025
origins:
- type: assistant
  ref: explore-ideas-mechanism
- type: literature
  ref: paper:Wong2023
  date: '2023-10-01'
  independent: true
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- question:0018-objective-vs-subjective-cognition-dissociation-in
- question:0006-jak-stat-il6-driver-vs-marker
created: '2026-07-04'
updated: '2026-07-07'
added_by: explore-ideas:claude-opus-4-8:cand-mechanism-platelet-serotonin-vagus-cognition
lens_views:
- lens: mechanism
  rationale: "The project names tryptophan-kynurenine (IDO1 shunt) as a gut-brain\
    \ mechanism. The peripheral serotonin-biosynthesis/platelet-storage axis is a\
    \ distinct route using the same substrate, with different therapeutic predictions\
    \ (IDO1 inhibition vs. serotonin-augmenting agents / platelet-serotonin stratifier).\
    \ Bears on question:0018 (objective vs subjective cognition). Anchored by Wong\
    \ 2023 (already a project paper), which validated the full chain in PASC models\
    \ \u2014 recorded here as an independent convergent literature origin.\n"
  origin_ref: explore-ideas-mechanism
---
# IFN-I → tryptophan malabsorption → platelet serotonin depletion → vagal hypofunction as a causal chain for PAIS cognitive impairment

## Summary

Does a **peripheral serotonin-depletion chain** — viral persistence / sustained type-I IFN → impaired
intestinal tryptophan absorption → reduced circulating and platelet serotonin (compounded by MAO-mediated
turnover) → reduced **vagal afferent** signaling → hippocampal / cognitive dysfunction — operate as a
causal route for PAIS cognitive impairment? And is it a **therapeutically distinct axis** from the IDO1
kynurenine-shunt route, which competes for the *same* tryptophan substrate but predicts different
interventions (serotonin-augmenting agents / vagal stimulation vs IDO1 inhibition)?

## Why It Matters

- **Decision it affects:** whether serotonin-repletion strategies (tryptophan/5-HTP, SSRIs, vagal
  stimulation) versus kynurenine-pathway modulation are the right node for a serotonin-depletion subtype;
  and whether **platelet / circulating serotonin** is a usable stratifying and early-prediction biomarker.
- **Risk if unanswered:** PAIS cognitive symptoms stay lumped under generic "neuroinflammation," and a
  measurable, tractable peripheral axis (serotonin, tryptophan, HRV as a vagal-tone readout) goes unused
  for stratification and for enriching cognitive-endpoint trials.

## Current Evidence

- **Supporting — direct anchor (mouse-validated, human-associational):** Wong et al. 2023 (Cell)
  [@Wong2023] validated the *full* chain in post-viral models: viral-RNA persistence → sustained type-I
  IFN → reduced intestinal tryptophan absorption → depleted peripheral (incl. platelet) serotonin →
  reduced vagal signaling → hippocampal dysfunction and memory deficits; serotonin repletion, tryptophan
  supplementation, or vagal restoration **reversed** the cognitive deficits in mice, and reduced serotonin
  was observed in long-COVID patient samples. This is the single strongest anchor and supplies the causal
  skeleton of the question.
- **Supporting — convergent framing:** Trautmann2025 [@Trautmann2025] situates tryptophan–kynurenine
  pathway (TKP) disruption (IDO shunt, low plasma tryptophan, low tryptophan/kynurenine ratio) in both
  long COVID and ME/CFS — establishing the shared-substrate competition between the serotonin-biosynthesis
  route (this question) and the kynurenine/quinolinic-acid neurotoxicity route.
- **Conflicting / limiting:** the causal chain is *established in mice*; the human evidence is
  cross-sectional/associational (reduced serotonin in patients) and does **not** demonstrate the
  vagal→cognition leg in humans. Peripheral serotonin does not cross the blood–brain barrier, so the
  cognitive effect is necessarily **indirect** (via vagal afferents, per Wong's model), not a direct CNS
  serotonin deficit. Serotonin-reduction findings are not universally replicated, and SSRI cognitive
  benefit in long COVID is unproven `[UNVERIFIED]` (trial evidence not audited here).

## Thoughts

- **Best current interpretation:** the peripheral serotonin-depletion axis is a genuinely *distinct* route
  from the IDO1/kynurenine route — both draw on tryptophan but predict different interventions — with
  Wong2023 as a strong mechanistic anchor. Its PAIS-cognition relevance is mechanistically coherent and
  mouse-validated, but the human causal legs (especially vagal→cognition) are not yet demonstrated.
- **Major uncertainty:** whether platelet/circulating serotonin actually stratifies the human PAIS
  cognitive phenotype and predicts response to serotonergic or vagal interventions, and how strongly the
  chain is covariate-dependent (severity, timing, prior immunity).

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (a candidate maintenance loop within
  the shared attractor); `hypothesis:0003-immune-exhaustion-feedback` (the persistent type-I IFN input
  that drives the chain).
- Related questions: `question:0018` (objective vs subjective cognition — this axis predicts an *objective*
  serotonin/vagal correlate); `question:0006` (IFN/JAK-STAT driver-vs-marker — shares the upstream IFN node).
- Required datasets: a long-COVID/ME-CFS cohort with paired plasma tryptophan, serotonin (or platelet
  serotonin), and a vagal-tone readout (HRV) plus objective cognition — none in project yet.
- Required analyses: mediation test of the serotonin→vagal→cognition chain in human data; serotonin as a
  stratifier for cognitive-endpoint response.
- Priority level: **P2** — mechanistically anchored and therapeutically actionable, but the decisive human
  data do not yet exist.

## Related

- Topic notes: `topic:mecfs-long-covid-convergence` (cognitive phenotype).
- Article notes: `paper:Wong2023` (direct full-chain anchor), `paper:Trautmann2025` (TKP shared-substrate
  context).
- Methods/Datasets: none yet.
