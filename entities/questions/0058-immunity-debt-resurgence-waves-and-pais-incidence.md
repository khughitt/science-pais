---
id: question:0058-immunity-debt-resurgence-waves-and-pais-incidence
kind: question
title: Do post-pandemic immunity debt resurgence waves (RSV, GAS) elevate PAIS incidence
  through acute-severity-threshold effects?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Munro2025
related:
- hypothesis:0004-acute-severity-threshold
- paper:Munro2025
created: '2026-07-10'
updated: '2026-07-10'
---

# Do post-pandemic immunity debt resurgence waves (RSV, GAS) elevate PAIS incidence through acute-severity-threshold effects?

## Summary

Non-pharmaceutical interventions (NPIs) during the COVID-19 pandemic suppressed endemic respiratory pathogens, causing population-level immunity debt — an accumulation of susceptible individuals who missed normal infection-acquired immunity cycles (Munro2025). This produced large post-pandemic resurgence waves of RSV, GAS, Mycoplasma pneumoniae, and adenovirus. The question is whether these resurgence waves, by delivering primary or near-primary infections to older children and adults who would normally have been repeatedly exposed, led to measurably higher PAIS incidence for RSV and GAS — mediated through the acute-severity-threshold mechanism (`hypothesis:0004`). In adults, primary RSV and invasive GAS tend to produce more severe acute illness than re-infection, and severe acute illness is the strongest individual-level predictor of PAIS risk.

## Why It Matters

- Determines whether immunity debt is epidemiologically relevant to PAIS burden (not only to acute disease), which would link the cycles/seasonal project directly to the PAIS project.
- If true, post-2021 PAIS registries and surveillance datasets should show a temporal spike in post-RSV and post-GAS fatigue/sequelae coinciding with the resurgence waves — a testable, time-anchored prediction.
- If unmeasured, a potentially large post-RSV/post-GAS PAIS burden is invisible in current PAIS epidemiology, which is dominated by COVID-19 long-COVID cohorts.

## Current Evidence

- **Supporting (indirect):** Munro2025 documents large RSV and invasive GAS resurgence waves post-2021; invasive GAS in particular showed a rate spike insensitive to testing-rate confounding (always tested in severe pediatric disease).
- **Supporting (indirect):** `hypothesis:0004` has multi-pathogen evidence that severe acute illness (e.g. dengue hemorrhagic fever vs. dengue fever) predicts PAIS risk — the same mechanism would apply if primary adult RSV/GAS is more severe than re-exposure.
- **Gap:** No study currently in project directly measures post-RSV or post-GAS PAIS incidence before vs. after the immunity debt resurgence waves. The post-GAS PAIS literature predates the pandemic and does not provide a post-2021 temporal comparison.
- **Conflicting (structural):** RSV PAIS (if it exists as a clinically distinct entity) is poorly characterized compared to post-COVID or post-Lyme disease. Most post-RSV sequelae literature concerns reactive airway disease / asthma induction in infants, not adult fatigue syndromes.

## Thoughts

- Best current interpretation: the immunity debt → PAIS pathway is plausible via h0004, but no direct evidence exists. This is an inference gap, not a contradiction.
- The most informative approach would be a time-series analysis of PAIS-adjacent outcomes (new ME/CFS diagnoses, post-infectious fatigue coded in EHR) from 2021–2024, stratified by pathogen where possible.
- The GAS angle may be more tractable than RSV: invasive GAS is routinely tested and coded; post-streptococcal sequelae (reactive arthritis, glomerulonephritis, neuropsychiatric PANDAS-spectrum) are documented entities that could be searched in administrative data.
- Major uncertainty: whether adult primary RSV truly produces sufficiently severe acute illness to cross h0004's severity threshold for PAIS. RSV is severe in infants; in healthy adults it may not be severe enough even as a primary infection.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (primary link); `hypothesis:0001-shared-dysregulated-attractor` (RSV/GAS as additional PAIS triggers).
- Required data or analyses: Post-2021 EHR or insurance claims data with RSV/GAS coded diagnoses + subsequent PAIS-adjacent outcome codes (fatigue, ME/CFS-adjacent, post-infectious syndrome). Alternatively: ONS-linked UK cohort with pathogen-specific acute illness severity + chronic outcome follow-up.
- Priority level: Low-medium (speculative inferential gap; no tractable dataset in project currently).

## Related

- Topic notes: Immunity debt is covered in `paper:Munro2025`; cycles project holds the seasonal epidemiology frame.
- Article notes: Baker et al. 2020 (PNAS) — original NPI/endemic pathogen prediction; Messacar et al. 2022 (Lancet) — pediatric endemic virus post-pandemic.
- Methods/Datasets: UK ONS infection survey (population-level, surveillance-complete, longitudinal); US insurance claims with ICD coding for RSV/GAS + post-infectious fatigue.
