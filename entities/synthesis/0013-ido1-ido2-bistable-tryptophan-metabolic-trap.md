---
id: "synthesis:0013-ido1-ido2-bistable-tryptophan-metabolic-trap"
kind: "synthesis"
title: "Synthesis: 0013-ido1-ido2-bistable-tryptophan-metabolic-trap"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0013-ido1-ido2-bistable-tryptophan-metabolic-trap"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-07-10"
updated: "2026-07-10"
provenance_coverage: "thin"
---

## State

*Status: proposed, phase: active.* The IDO1–IDO2 bistable-trap hypothesis posits that IDO1 substrate inhibition at elevated tryptophan, combined with IDO2 loss-of-function polymorphisms removing the enzymatic backup pathway, creates a bistable system capable of locking susceptible individuals into a self-sustaining metabolic attractor — high tryptophan, low kynurenine, depleted NAD⁺ precursors — that persists after the triggering infection resolves. Drawing on the hypothesis spec's YAML frontmatter chains (source_refs: cite:Kashi2019, cite:Al-Hakeim2023), the mechanism was formalized as a mathematical-model conjecture for ME/CFS (cite:Kashi2019) and has not been empirically tested in any PAIS cohort.

The central open question is directional. The trap predicts a **high-Trp / low-Kyn** metabolite signature — the *opposite* of the IFN-driven **low-Trp / high-Kyn** pattern tracked by `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal` (inverse confidence 0.8). The cross-sectional long-COVID study cite:Al-Hakeim2023 (source_ref) reports the IFN-type direction — low tryptophan, elevated kynurenine — placing the bistable-trap mechanism under directional tension in PASC specifically. No PAIS dataset stratified by IDO2 genotype exists; no longitudinal study has tested for the hysteresis the bistability hypothesis requires. Overall support is *thin*: one mathematical-model source (cite:Kashi2019, ME/CFS-specific, one-source) and one partially disputing cross-sectional observation (cite:Al-Hakeim2023) that is more consistent with the rival route of `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal`.

## Arc

Arc reconstruction is limited: no interpretations with `prior_interpretations` chains exist for `hypothesis:0013-ido1-ido2-bistable-tryptophan-metabolic-trap` in the bundle; the following is based solely on hypothesis spec provenance fields.

The hypothesis was introduced on 2026-07-06 via the explore-ideas mechanism (hypothesis spec frontmatter: `added_by: explore-ideas:claude-opus-4-8:cand-mechanism-ido-tryptophan-bistable-trap`), seeded from cite:Kashi2019 and cite:Al-Hakeim2023. It was framed as a candidate cell-intrinsic bistable realization of `hypothesis:0001-shared-dysregulated-attractor` — a trigger-nonspecific attractor route with an explicit genetic-susceptibility axis (IDO2 genotype) — and scoped from the outset to contrast with the rival IFN-I gut-malabsorption route of `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal`. No subsequent interpretive work, task execution, or empirical follow-up is recorded. The investigation remains at initial framing: discriminating directional predictions are defined, but no test has been designed or initiated.

## Research fronts

The only live question in the bundle is `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal` (inverse confidence 0.8), the directional rival whose IFN-type low-Trp / high-Kyn prediction is currently more consistent with available long-COVID metabolite data (cite:Al-Hakeim2023 source_ref). Resolving the rivalry requires PAIS metabolomics stratified by IDO2 genotype — a study design not present in the bundle's task list (tasks: none recorded).

Key gaps from the hypothesis spec YAML frontmatter:

- No PAIS cohort has been IDO2-genotype-stratified across any trigger (long COVID, PTLDS, post-Q-fever, post-sepsis).
- No longitudinal Trp/Kyn dataset exists to test for hysteresis or attractor persistence after inputs normalize.
- The bistable-trap model has not been empirically validated even in ME/CFS, the condition for which it was originally proposed (cite:Kashi2019).
- The parent attractor frame, `hypothesis:0001-shared-dysregulated-attractor`, is independently listed as contested in the bundle gaps_slice, meaning the broader frame the hypothesis relies on is itself under pressure.

The most discriminating next test, per the hypothesis spec, is a joint IDO2-genotype × longitudinal-Trp/Kyn design capable of detecting hysteresis and directionally separating the trap from `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal`.
