---
id: "synthesis:0002-tissue-reservoir-antigen-fragment"
kind: "synthesis"
title: "Synthesis: 0002-tissue-reservoir-antigen-fragment"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0002-tissue-reservoir-antigen-fragment"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0002-tissue-reservoir-antigen-fragment` is **proposed** and active, grading **speculative** at the conjunctive-bundle level. The core claim is that degradation-resistant pathogen fragments accumulate in tissue-resident macrophages, chronically engage innate sensing, and seed chronic PAIS — with retained fragment duration, not initial pathogen load, as the key chronicity determinant.

The three core propositions carry unequal support. `proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive` (fragment persistence and bioactivity) is **supported**: `evidence-line:0058` (McClune2025) demonstrates Borrelia peptidoglycan persisting in Kupffer cells post-clearance with proteome and PBMC-metabolic consequences; `evidence-line:0059` (Peluso2024) corroborates SARS-CoV-2 antigen persistence in ~25% of survivors at 14 months (detection only, no mechanistic link). `proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization` (cross-pathogen macrophage-reservoir generalization) is **speculative with one weak partial line**: `evidence-line:0072` (Goh2022) shows nucleocapsid/CD68 co-localization in two long-COVID tissue samples but lacks controlled prevalence, degradation-resistant chemistry, or host-signature overlap. `proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load` (retained fragment burden predicts chronicity over initial load) is **untested and weakly contested**: no prospective burden-vs-load cohort exists, and `evidence-line:0073` (BrandstetterFigueroa2025) shows acute nucleocapsid antigen predicts 9-month long-COVID symptoms (aOR 3.0, 95% CI 1.1–8.0), keeping initial load alive as an independent predictor. The gaps slice flags both `proposition:0020-antigen-clearance-rescues-established-pais` (clearing antigen rescues established PAIS) and `proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load` as evidentially contested. The weakest-link conjunction caps the hypothesis at speculative even though one pillar is now supported.

## Arc

`hypothesis:0002-tissue-reservoir-antigen-fragment` entered the project as a prose-only conjecture (claim_count=0). Task t046 (`interpretation:0011-t046-antigen-clearance-trials-ingestion`) produced the first formalized evidence base: five evidence lines across two proposition types, establishing that established-disease clearance trials — STOP-PASC (`evidence-line:0053`), PAX-LC (`evidence-line:0054`), outSMART-LC (`evidence-line:0055`), and the consolidated PTLDS antibiotic-retreatment arm (`evidence-line:0060`) — are null but **uninterpretable** for want of antigen target-engagement (`evidence-line:0054` proved NMV/r left circulating Spike unchanged), while acute metformin prevention RCTs (`evidence-line:0056`, `evidence-line:0057`) show PAIS incidence can be halved. This treatment-null/prevention-positive pattern grounded the fixed-risk-factor-at-onset reconciliation: antigen acts as a determinant at onset, not a reversible maintenance target once chronic disease is self-sustaining.

Task t053 ran a promotion audit (`interpretation:0017-t053-h0002-promotion-audit`), surfacing `evidence-line:0072` (Goh2022) as the closest available non-Borrelia tissue/macrophage result and `evidence-line:0073` (BrandstetterFigueroa2025) as model criticism against `proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load`; promotion was declined. Task t059 (`interpretation:0028-t059-h0002-promotion-vehicle-hunt`) confirmed with a wider re-screen of plasma antigen and Coxiella literature that no admissible vehicle existed, and specified the exact study designs required to lift each unsupported conjunct. Running in parallel, `interpretation:0023-t007-microbiome-gut-brain-axis` framed gut dysbiosis (`proposition:0031-pais-gut-dysbiosis-scfa-depletion`) as a recurring PAIS loop node and a contextual read-across for h0002's reservoir/barrier interface, but not promoting evidence for the core conjuncts. The current epistemic position is: one supported pillar; the full pathogen-agnostic initiator hypothesis remains unproven.

## Research fronts

The primary live question is `question:0002-antigen-clearance-rescues-symptoms` (inverse confidence 0.8) — the decisive test of whether clearing antigen rescues symptoms in established PAIS. Existing nulls (`evidence-line:0053`, `evidence-line:0055`, `evidence-line:0060`) are uninterpretable because no completed trial demonstrated antigen clearance; an antigen-positive-enriched, clearance-confirmed trial with symptom endpoints remains unrun.

Two conjunct-level promotion gaps define the structural research frontier:
- **`proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization`** requires a controlled non-Borrelia PAIS tissue-reservoir study localizing clearance-refractory fragments to tissue-resident macrophages with host-signature overlap, as specified by `interpretation:0028-t059-h0002-promotion-vehicle-hunt`.
- **`proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load`** requires a prospective same-subject design measuring retained post-clearance fragment burden vs acute pathogen load against PAIS diagnosis; `evidence-line:0073` has already shown acute burden predicts 9-month symptoms, making the head-to-head design mandatory.

Additional unpursued targets include TLR2-blockade ex vivo testing of fragment-induced metabolic suppression and host clearance-gene burden analysis across PAIS cohorts.
