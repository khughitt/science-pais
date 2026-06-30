---
id: interpretation:0017-t053-h0002-promotion-audit
type: interpretation
title: "t053 - h0002 promotion audit: weak SARS-CoV-2 tissue/macrophage support, acute-load criticism, no promotion"
status: active
source_refs: []
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
- proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load
- evidence-line:0072-goh2022-sars2-tissue-cd68-antigen-weakly-supports-0023
- evidence-line:0073-brandstetterfigueroa2025-acute-nag-predicts-lc-disputes-0024
- paper:Goh2022
- paper:BrandstetterFigueroa2025
- topic:antigen-pathogen-persistence
- task:t053
created: '2026-06-25'
updated: '2026-06-25'
input:
- paper:Goh2022
- paper:BrandstetterFigueroa2025
prior_interpretations:
- interpretation:0011-t046-antigen-clearance-trials-ingestion
relations:
- predicate: "sci:amends"
  target: "interpretation:0011-t046-antigen-clearance-trials-ingestion"
---
# Interpretation: t053 - h0002 promotion audit

## Verdict

**Verdict:** `[~]` mixed/no-promotion. t053 found one weak partial support line for the cross-pathogen
tissue/macrophage-reservoir conjunct (`proposition:0023`) and one weak model-criticism line against the
retained-burden-over-initial-load conjunct (`proposition:0024`). The evidence base is now more honest and
more specific, but it does **not** promote `hypothesis:0002` out of `speculative`.

## What Was Coded

`evidence-line:0072` codes Goh2022 as weak support for `proposition:0023`. The study is a two-patient
long-COVID tissue case report: SARS-CoV-2 nucleocapsid protein and viral RNA were detected in appendix,
skin, and breast tissue 163 and 426 days after symptom onset, and nucleocapsid signal co-localized with
CD68-positive cells [@Goh2022]. This is the closest available non-Borrelia human tissue result for the
tissue/macrophage arm of h0002.

`evidence-line:0073` codes BrandstetterFigueroa2025 as weak model criticism of `proposition:0024`. In a
prospective acute-COVID cohort, detectable acute plasma SARS-CoV-2 nucleocapsid antigen predicted
persistent long-COVID symptoms at 9 months after adjustment (aOR 3.0, 95% CI 1.1-8.0) [@BrandstetterFigueroa2025]. This keeps acute
pathogen burden alive as an independent predictor and disputes the strongest reading that initial load is
not the lever.

## Why h0002 Still Does Not Promote

Goh2022 is partial: it shows tissue antigen/RNA and CD68 co-localization, but not degradation-resistant
fragment chemistry, a tissue-resident macrophage clearance defect, controlled prevalence, host proteome or
metabolic overlap with McClune2025, or symptom/burden association. It therefore lifts `proposition:0023` from absent to
weakly observed in SARS-CoV-2 tissue, but does not establish the cross-pathogen reservoir mechanism.

BrandstetterFigueroa2025 is not a direct refutation of `proposition:0024`, because it does not measure retained
post-clearance fragment burden. Acute N antigen may index acute severity, systemic dissemination, or the
probability of later retention. It does, however, mean `proposition:0024` cannot claim retained burden out-predicts
initial load until the head-to-head prospective design is run.

Net: `proposition:0023` remains speculative with weak support; `proposition:0024` remains speculative and
weakly contested; the conjunctive bundle grade for `hypothesis:0002` remains `speculative`.

## Promotion Path After t053

The clean upward path is now narrower:

- For `proposition:0023`: a controlled non-Borrelia PAIS tissue-reservoir study showing fragment retention
  in tissue-resident macrophages plus overlapping host signature.
- For `proposition:0024`: a prospective cohort measuring retained post-clearance fragment burden and acute
  pathogen load in the same subjects, with chronic-illness diagnosis as the endpoint, and retained burden
  out-predicting acute load.

Until both exist, h0002 should remain a supported-persistence-pillar hypothesis with an unproven
pathogen-agnostic initiator claim.
