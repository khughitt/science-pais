---
id: question:0063-geographic-variation-long-covid-true-vs
kind: question
title: Does geographic variation in long COVID prevalence (South America 51% vs North
  America 30%) reflect true etiological heterogeneity or systematic measurement and
  access artifacts?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Hou2025
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0020-host-immune-baseline-reserve-gate
created: '2026-07-10'
updated: '2026-07-10'
---

# Does geographic variation in long COVID prevalence (South America 51% vs North America 30%) reflect true etiological heterogeneity or systematic measurement and access artifacts?

## Summary

Hou et al. 2025 (429-study meta-analysis) finds long COVID "ever" prevalence of 51% (95% CI
35%–66%) in South America vs. 30% (24%–38%) in North America and 39% (31%–48%) in Europe.
The paper notes I² = 100% globally, and Figure 4 lists age structure, healthcare access,
national health index, genetics, vaccine access/uptake, and comorbidity prevalence as
candidate true sources of heterogeneity alongside study-design artifacts (definition,
diagnosis, sampling). The question is whether the geographic gradient has biological signal
or primarily reflects systematic data-quality and access disparities.

## Why It Matters

- If geographic variation is largely measurement-driven, pooling global estimates is
  misleading and region-specific burden estimates require separate modeling from
  region-specific cohorts.
- If variation is partly etiological (genetics, comorbidity burden, healthcare access shaping
  acute-to-chronic transition), it is an important signal for hypothesis:0020
  (host-immune-baseline-reserve-gate) and for identifying high-burden populations.
- Risk if unanswered: public health resource allocation decisions may be miscalibrated if
  the South American 51% is substantially inflated by diagnostic/reporting bias rather than
  true burden.

## Current Evidence

- Hou2025: South America 51% (10 studies), North America 30% (24 studies), Africa estimated
  53% but only 3 studies — unreliable. I² between 99%–100% within each region.
- The paper explicitly notes Africa and Oceania are massively under-represented, limiting
  any inter-regional comparison.
- Between-region heterogeneity in ORs for risk factors is smaller than heterogeneity in
  prevalence estimates (narrower prediction intervals for ORs in Supplementary Tables 7–9),
  suggesting some study-design factors inflate prevalence estimates more than OR estimates.
- No available cross-region harmonized study using a single definition and diagnostic protocol.

## Thoughts

- The most parsimonious interpretation: the geographic gradient is a mixture of (a) true
  differences in comorbidity burden, variant exposure timing, and vaccine uptake, and (b)
  study-design artifacts (survey vs. clinical follow-up, definition breadth).
- South American studies may include more hospitalized cohorts or use broader symptom
  definitions; without individual-study covariate data this cannot be adjudicated.
- A major uncertainty: whether access to testing and follow-up referral (which selects for
  more symptomatic / hospitalized patients in resource-limited settings) inflates apparent
  prevalence in lower-resource regions.

## Connections to Project

- Related hypotheses: `hypothesis:0008` (measurement/ascertainment bias); `hypothesis:0020`
  (host immune baseline and comorbidity gating).
- Required data or analyses: cross-region comparison controlling for hospitalization rate,
  definition breadth, and comorbidity prevalence; or a prospective harmonized multi-site
  cohort with a common protocol.
- Priority level: Medium. Primarily an epidemiological question; answers would inform
  global burden modeling but are not decisive for the mechanistic hypotheses this project
  focuses on.

## Related

- Topic notes: `topic:pais-case-definition-heterogeneity`, `topic:measurement-ascertainment-artifacts-in-pais`
- Article notes: `paper:Hou2025`
- Methods/Datasets: Household Pulse Survey (US-specific benchmark); harmonized multi-site
  studies if available
