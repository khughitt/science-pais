---
id: interpretation:0028-t059-h0002-promotion-vehicle-hunt
type: interpretation
title: "t059 - h0002 promotion vehicle hunt: no admissible non-Borrelia macrophage-reservoir or retained-burden-over-load vehicle found"
status: active
source_refs:
- paper:Goh2022
- paper:Peluso2024
- paper:BrandstetterFigueroa2025
- paper:Morroy2016
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
- proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load
- evidence-line:0072-goh2022-sars2-tissue-cd68-antigen-weakly-supports-0023
- evidence-line:0073-brandstetterfigueroa2025-acute-nag-predicts-lc-disputes-0024
- interpretation:0017-t053-h0002-promotion-audit
- task:t059
created: '2026-06-26'
updated: '2026-06-26'
input:
- paper:Goh2022
- paper:Peluso2024
- paper:BrandstetterFigueroa2025
- paper:Morroy2016
prior_interpretations:
- interpretation:0017-t053-h0002-promotion-audit
relations:
- predicate: "sci:amends"
  target: "interpretation:0017-t053-h0002-promotion-audit"
---
# Interpretation: t059 - h0002 promotion vehicle hunt

## Verdict

**Verdict:** `[?]` no admissible promotion vehicle found. t059 did not identify a literature result that
can lift either remaining h0002 core conjunct to supported:

- `proposition:0023`: no controlled non-Borrelia PAIS tissue-reservoir study showing retained pathogen
  fragments in tissue-resident macrophages plus overlapping host signature.
- `proposition:0024`: no prospective cohort measuring both acute pathogen load and retained
  post-clearance fragment burden in the same subjects with chronic PAIS diagnosis as endpoint.

No new evidence-line is coded from this pass. h0002 stays `speculative`.

## Screened Evidence Classes

**SARS-CoV-2 tissue persistence.** `evidence-line:0072` (Goh2022) remains the closest match: tissue
nucleocapsid/RNA with CD68 co-localization in two long-COVID cases. It is still only weak partial support
for `proposition:0023` because it lacks controlled prevalence, degradation-resistant chemistry, macrophage functional
retention, host-signature overlap, and symptom/burden association. Other tissue-persistence-style
findings can motivate the search but should not be automatically coded to `proposition:0023` unless they localize the
fragment to a tissue-resident macrophage sink or an equivalent phagocyte-retention mechanism.

**Plasma antigen persistence.** Peluso2024 supports persistence (`proposition:0022`), not the macrophage
reservoir generalization (`proposition:0023`) or retained-burden-over-acute-load (`proposition:0024`). Plasma positivity is
compatible with a tissue reservoir but is not localization evidence.

**Acute antigen/load predictors.** `evidence-line:0073` (BrandstetterFigueroa2025) remains model
criticism for `proposition:0024` because acute nucleocapsid antigen predicts 9-month long-COVID symptoms. It does not
refute `proposition:0024`, but it keeps acute burden alive and makes the head-to-head design mandatory.

**Coxiella/QFS antigen-fragment hypothesis.** Morroy2016 records the immunomodulatory-complex idea
involving non-viable Coxiella DNA/antigen and macrophage-clearance impairment, but this is not yet a
controlled tissue-reservoir demonstration with host-signature overlap.

## Admissible Vehicles

For `proposition:0023`, an admissible positive vehicle must include:

- non-Borrelia PAIS cases and matched recovered/healthy controls;
- tissue sampling from a plausible reservoir compartment;
- pathogen fragment/protein/RNA detection with cell-type localization to tissue-resident macrophages or
  a mechanistically equivalent phagocyte sink;
- evidence the retained material is degradation-resistant or otherwise clearance-refractory;
- host-tissue or PBMC signature overlap with the Borrelia pPG^Bb/McClune2025 axis.

For `proposition:0024`, an admissible vehicle must be prospective and same-subject:

- acute pathogen-load measurement during the acute infection;
- retained post-clearance fragment/antigen burden measured later;
- chronic PAIS diagnosis or validated symptom endpoint;
- a model comparing retained burden against acute load, with retained burden out-predicting acute load.

## Implication

t059 narrows h0002's promotion path but does not discharge it. The correct standing statement is:
`proposition:0022` is supported, `proposition:0023` has one weak partial SARS-CoV-2 tissue/macrophage
line, and `proposition:0024` remains unsupported and weakly contested by acute-load prediction.
