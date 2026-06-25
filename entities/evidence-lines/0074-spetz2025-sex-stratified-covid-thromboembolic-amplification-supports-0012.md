---
id: evidence-line:0074-spetz2025-sex-stratified-covid-thromboembolic-amplification-supports-0012
type: evidence-line
title: Spetz2025 Swedish total-population cohort shows COVID-added thromboembolic risk is stronger in men than women - supports male vascular reversal beyond pure baseline carryover
status: active
stance: supports
target: proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
source: paper:Spetz2025
strength: moderate
independence: independent
independence_group: spetz2025-scifi-pearl-sex-thromboembolic-covid-interaction
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- question:0020-male-vte-excess-post-acute-persistence
- question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover
- hypothesis:0004-acute-severity-threshold
- topic:thromboinflammation-and-endothelial-dysfunction
- interpretation:0018-t048-vascular-sex-baseline-carryover-audit
- task:t048
source_refs:
- paper:Spetz2025
created: '2026-06-25'
updated: '2026-06-25'
---
# Evidence Line: Spetz2025 sex-stratified COVID thromboembolic amplification

## What this line shows

Spetz2025 provides a Swedish total-population, uninfected-comparator cohort (n=4,095,414 aged 40-75)
with sex-stratified thromboembolic estimates after SARS-CoV-2 infection. In the no-prior-comorbidity
sensitivity table, the thromboembolic outcome (DVT or PE) shows:

| Exposure stratum | Thromboembolic HR |
|---|---:|
| No COVID, men | 1.00 |
| No COVID, women | 0.78 (0.76-0.81) |
| COVID, men | 3.64 (3.43-3.88) |
| COVID, women | 1.81 (1.67-1.97) |

Interpreting these as stratum-specific hazards relative to uninfected men, the implied infection-added
relative risk is approximately 3.64 in men versus 1.81 / 0.78 = 2.32 in women, giving an approximate
male-vs-female ratio-of-ratios of **1.57**. A second sensitivity table excluding recent immigrants gives a
similar pattern: COVID men HR 3.43, uninfected women HR 0.83, COVID women HR 1.86, approximate
ratio-of-ratios **1.53**.

This supports `proposition:0012`'s male hard-vascular endpoint reversal and narrows its leading caveat:
the male signal is unlikely to be **pure** baseline carryover, because the COVID-associated increment in
thromboembolic disease appears larger in men than in women when compared with the uninfected baseline
within the same source population.

## Why it is independent

`independent` under `independence_group: spetz2025-scifi-pearl-sex-thromboembolic-covid-interaction`.
The evidence comes from Swedish nationwide registers and is independent of the UKBB ambulatory VTE cohort
(Xie2022), the hospitalized Kopp2024 cohort, the Abubasheer2025 meta-analysis, and the Ambrosino2021 FMD
case-control study already carrying `proposition:0012`.

## Caveats / scope

`direct_test`, **moderate** for the baseline-carryover question, but not a full t048 discharge. The
reported sex-stratified table is not crossed with the 31-180 day risk window or with the non-hospitalized
severity stratum. Separately, Spetz2025 reports that mild/non-hospitalized COVID-19 has elevated DVT and
PE risk, and that DVT/PE remain elevated in the 91-180 day window overall, but it does not report the
single desired estimand: sex x COVID infection interaction for DVT/PE among non-hospitalized patients in
the 31-180 day window. Therefore this line supports a COVID-added male thromboembolic component while
leaving the exact late ambulatory sex-interaction design gap open.
