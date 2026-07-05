---
id: interpretation:0018-t048-vascular-sex-baseline-carryover-audit
kind: interpretation
title: "t048 - vascular male reversal audit: Spetz2025 narrows baseline carryover, exact ambulatory 31-180d sex interaction still unreported"
status: active
source_refs:
- paper:Spetz2025
related:
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- question:0020-male-vte-excess-post-acute-persistence
- question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover
- hypothesis:0004-acute-severity-threshold
- topic:thromboinflammation-and-endothelial-dysfunction
- evidence-line:0074-spetz2025-sex-stratified-covid-thromboembolic-amplification-supports-0012
- paper:Spetz2025
- task:t048
created: '2026-06-25'
updated: '2026-06-25'
input:
- paper:Spetz2025
prior_interpretations:
- interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment
relations:
- predicate: "sci:amends"
  target: "interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment"
---
# Interpretation: t048 - vascular male reversal audit

## Verdict

**Verdict:** `[~]` partial positive / residual design gap. t048 did not find a single perfect vehicle
reporting the full desired estimand - sex x COVID infection interaction for hard vascular outcomes among
ambulatory/non-hospitalized patients in the 31-180 day window. It did find a strong near-vehicle:
Spetz2025, a Swedish total-population SCIFI-PEARL registry cohort with an uninfected comparator, sex-
stratified cardiovascular outcome estimates, hospitalization-defined severity strata, and risk-period
estimates through 730 days [@Spetz2025].

Spetz2025 narrows the leading caveat on `proposition:0012`: the male vascular reversal is unlikely to be
pure baseline carryover. But it does **not** close `question:0020` or `question:0021`, because the
published tables do not cross sex, infection, non-hospitalized severity, and 31-180 day timing in the same
model [@Spetz2025].

## What Spetz2025 Adds

Three separate pieces matter:

1. **Uninfected comparator with sex-stratified thromboembolic estimates.** In the no-prior-comorbidity
   sensitivity table, thromboembolic disease (DVT or PE) is HR 3.64 in COVID-infected men versus HR 1.81
   in COVID-infected women, with uninfected men as reference and uninfected women HR 0.78. The implied
   infection-added male-vs-female ratio-of-ratios is approximately 1.57. A second sensitivity analysis
   excluding recent immigrants gives an approximate ratio-of-ratios of 1.53 [@Spetz2025].
2. **Post-acute persistence overall.** In the 91-180 day window, DVT remains elevated (HR 1.20, 95% CI
   1.04-1.39) and PE remains elevated (HR 1.29, 95% CI 1.10-1.52), compared with uninfected person-time [@Spetz2025].
3. **Non-hospitalized/mild disease is not null overall.** Mild/non-hospitalized COVID-19 carries elevated
   DVT (HR 1.41, 95% CI 1.31-1.52) and PE (HR 1.78, 95% CI 1.64-1.92), compared with uninfected
   person-time.

Together, these are enough to reject the strongest deflationary reading that the male vascular signal is
only the ordinary male baseline vascular excess being carried through infected cohorts. COVID adds
thromboembolic risk in both sexes, and the added relative risk appears larger in men.

## What It Still Does Not Answer

The exact t048 estimator remains unpublished:

`(COVID vs uninfected HR in men) / (COVID vs uninfected HR in women)`, restricted to
non-hospitalized/mild COVID-19 and the 31-180 day post-acute window, preferably for DVT and PE separately [@Spetz2025].

Spetz2025 reports each dimension, but not all dimensions crossed:

- Sex-stratified table: broad thromboembolic outcome over follow-up, not risk-windowed or severity-crossed.
- Risk-period table: DVT/PE separately through 91-180 days, but sex-adjusted rather than sex-stratified.
- Severity table: mild/non-hospitalized DVT/PE risk, but not crossed with sex or 31-180 day timing.

Therefore `question:0021` is **partially addressed**: pure baseline carryover is weakened, but the
infection-attributable male increment is not fully estimated for the target window. `question:0020` is
also **partially addressed**: late VTE persistence exists overall through 91-180 days, but late
ambulatory sex-stratified VTE persistence remains open [@Spetz2025].

## Consequence For The Model

`proposition:0012` should remain `well_supported`, now with a narrower caveat. The vascular hard-endpoint
male reversal has three layers:

- Direction: male-biased hard vascular endpoints are reproducible.
- Severity: the signal is not merely hospitalization/ICU carryover.
- Attribution: Spetz2025 supports a COVID-added male thromboembolic increment beyond pure baseline
  carryover, but the exact ambulatory 31-180 day interaction remains unresolved [@Spetz2025].

For h0004 and future pre-registered analyses, sex and severity should be modeled jointly rather than
treating sex as only a baseline covariate or only a severity proxy. The practical analysis target is now a
formal sex x infection x time-window interaction, with non-hospitalized and hospitalized strata reported
separately.
