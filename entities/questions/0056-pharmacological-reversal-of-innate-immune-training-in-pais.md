---
id: question:0056-pharmacological-reversal-of-innate-immune-training-in-pais
kind: question
title: Can pharmacological reversal of innate-immune training (BET inhibitors, itaconate,
  statins, DNMT inhibitors) resolve persistent PAIS inflammation?
status: active
ontology_terms:
- trained immunity
- epigenetic therapy
- BET bromodomain
- itaconate
- immunometabolism
- PAIS therapeutics
- innate immune memory
datasets: []
source_refs:
- cite:Arts2016
- cite:Netea2016
- cite:Cheong2023
origins:
- type: assistant
  ref: research-topic
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- topic:therapeutics-and-clinical-trials
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-07-07'
updated: '2026-07-07'
added_by: "llm:claude-sonnet-4-6:research-topic"
---

# Can pharmacological reversal of innate-immune training (BET inhibitors, itaconate, statins, DNMT inhibitors) resolve persistent PAIS inflammation?

## Summary

If the persistent inflammatory output in PAIS is maintained by epigenetic imprinting of HSPCs or peripheral monocytes (trained immunity), then agents that reverse or attenuate the trained epigenome — rather than blocking individual cytokines or inhibiting kinases — could resolve the upstream driver. Several pharmacological strategies have been shown to modulate trained immunity in vitro or in animal models: BET bromodomain inhibitors (JQ1, iBET151) block H3K4me3-dependent transcription; itaconate (and its cell-permeable derivative 4-octyl itaconate) is an endogenous immunometabolic brake on training induction; statins block the mevalonate pathway required for trained immunity induction by oxLDL; DNMT inhibitors (azacytidine) may reverse DNA methylation changes that accompany training. This question asks whether any of these approaches can reset the HSPC epigenome and resolve persistent PAIS inflammation — a distinct therapeutic axis from the cytokine blockade (JAK/IL-6) and antiviral strategies currently in trials.

## Why It Matters

- If PAIS is maintained by trained HSPC imprinting, blocking individual cytokines downstream of the imprint (JAK/IL-6 inhibitors, IL-1β blockade) would suppress symptoms only while administered but not reset the upstream driver — predicting rebound on discontinuation. Epigenetic-reprogramming agents, by contrast, could offer durable remission if the imprint is erased.
- Current PAIS therapeutic trials are almost entirely downstream: antivirals (antigen-clearance), JAK inhibitors (IL-6/IFN signaling), anticoagulants (thromboinflammation). An HSPC-epigenome resetting approach has not been tested in PAIS.
- Without this question, the trained-immunity hypothesis remains therapeutically inert even if mechanistically supported.

## Current Evidence

- Supporting the concept: β-glucan-induced trained immunity in murine models is attenuated by BET inhibitors (JQ1) and by exogenous itaconate; statin pretreatment blocks oxLDL-induced trained immunity in monocytes; DNMT inhibition reverses some post-sepsis epigenetic changes in macrophages. These are all mechanistic observations in model systems, not in PAIS patients.
- Supporting the imprint target: Arts2016 identified glutaminolysis/fumarate → KDM5 inhibition → H3K4me3 accumulation as the metabolic-epigenetic bridge; blocking fumarate production (by inhibiting glutaminolysis) could prevent training induction. Itaconate blocks NLRP3 and succinate dehydrogenase, attenuating the metabolic rewiring that sustains training.
- Gap: No clinical trial has used epigenetic-reprogramming agents specifically for PAIS or long COVID. Statins have been tested as COVID-19 prophylaxis and as general anti-inflammatory in other conditions but not as innate-training modulators in established PAIS. 4-Octyl itaconate has not entered PAIS trials.
- Conflicting / cautionary: Systemic epigenetic agents (azacytidine, broadly acting DNMT inhibitors) carry significant toxicity profiles used as oncology agents at therapeutic doses; their risk-benefit in PAIS (a non-lethal condition) would require ultra-low doses or alternative delivery routes. BET inhibitors are anti-proliferative and have cardiac side effects at clinical doses. The PAIS-relevant dose window for epigenetic resetting without systemic toxicity is entirely unknown.
- Conflicting: If trained immunity in PAIS is partly beneficial (residual antiviral protection), suppressing it could increase infection vulnerability. Immune status and whether any beneficial trained-immunity remains must be considered.

## Thoughts

- Best current interpretation: The pharmacological logic is sound, but the approach is pre-clinical. The appropriate sequence is: (1) establish that HSPC imprinting predicts PAIS (question:0055); (2) confirm ex vivo that patient-derived HSPCs show imprinting reversible by candidate agents; (3) design a phase I/IIa safety and target-engagement trial with HSPC chromatin as pharmacodynamic readout alongside symptom endpoints.
- Major remaining uncertainty: whether PAIS-relevant HSPC imprinting is driven by the same metabolic-epigenetic circuits (fumarate/KDM5, BRD4/H3K4me3) that are targeted by these agents in β-glucan and oxLDL models. COVID-specific imprinting (Cheong2023) is mechanistically characterized at the chromatin-accessibility level but not yet at the metabolic-enzyme or BET-bromodomain level.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` — epigenetic resetting as a potential basin-exit intervention; `hypothesis:0003-immune-exhaustion-feedback` — if trained monocytes sustain the inflammatory signal that drives T-cell exhaustion, resetting training could break the loop.
- Required datasets: ex vivo human HSPC or monocyte epigenetic resetting assays using patient-derived cells; a PAIS phase I trial with chromatin readout.
- Required analyses: dose-response reversal of HSPC H3K4me3/ATAC-seq profile by candidate agents in patient-derived cells; correlation of in vitro epigenetic reversal with cytokine production reduction.
- Priority level: P3 — conceptually important but requires prior question:0055 evidence to justify clinical translation.

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais`, `topic:therapeutics-and-clinical-trials`
- Article notes: Arts2016, Netea2016, Cheong2023.
- Methods/Datasets: ex vivo culture of patient-derived HSPCs or monocytes; ATAC-seq / CUT&RUN H3K4me3; cytokine production assays.
