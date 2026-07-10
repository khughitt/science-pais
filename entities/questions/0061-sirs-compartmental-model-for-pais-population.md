---
id: question:0061-sirs-compartmental-model-for-pais-population
kind: question
title: Can SIRS-type compartmental models project PAIS population burden from endemic
  pathogen resurgence waves?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Munro2025
related:
- question:0008-formalize-vicious-cycle-attractor-model
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
created: '2026-07-10'
updated: '2026-07-10'
---

# Can SIRS-type compartmental models project PAIS population burden from endemic pathogen resurgence waves?

## Summary

Munro & House (2025) demonstrate that a simple SIRS compartmental model — with infection, hospitalization, recovery, waning immunity, and seasonal oscillation in contact rates — reproduces the qualitative pattern of post-pandemic endemic pathogen resurgences. The model code is publicly available. This raises the question of whether the same modeling framework, extended with a PAIS compartment (or a post-recovery transition rate to chronic illness), can project population-level PAIS burden arising from endemic pathogen resurgence waves, and whether such a model can make informative predictions about timing, magnitude, and eventual return to baseline PAIS incidence.

## Why It Matters

- Provides a principled population-level complement to the within-host dynamical models being considered for `question:0008` (PAIS attractor formalization). Population-level SIRS and within-host attractor models operate at different scales but share mathematical structure (compartments, waning, thresholds).
- If feasible, a SIRS+PAIS model could quantify the public health burden of post-pandemic PAIS as a function of resurgence wave magnitude — a policy-relevant output currently unmeasured.
- Connects the cycles project's epidemiological modeling to the post-acute-infection project's mechanistic framing.

## Current Evidence

- **Supporting:** Munro2025 SIRS model code is available (Python/Jupyter; https://github.com/thomasallanhouse/covid19-incidence/blob/main/debt.ipynb) and reproduces qualitative resurgence dynamics without pathogen-specific calibration.
- **Supporting (methods):** `interpretation:0024` (t011) documents delayed-viral-dynamics ODE/DDE models relevant to within-host PAIS dynamics; the mathematical structure (compartments, stability, oscillation) is shared with population SIRS.
- **Gap:** No published model currently links the SIRS susceptibility cycle to a PAIS output compartment. The necessary PAIS transition rate from acute infection is not empirically established for RSV, GAS, or other endemic pathogens outside COVID-19.
- **Conflicting (structural):** SIRS models with homogeneous mixing are poor representations of age-structured pathogens like RSV (where infant dynamics drive transmission). A PAIS extension would need at minimum two age classes (infant vs. adult) to be ecologically valid.

## Thoughts

- Best current interpretation: The Munro2025 SIRS framework is a useful starting structure, but requires two nontrivial extensions to project PAIS burden: (1) an empirically grounded PAIS-transition rate from acute infection (currently unavailable for most endemic pathogens), and (2) age stratification (infants, children, adults) to capture RSV dynamics accurately.
- The most tractable version would use COVID-19 PAIS incidence estimates as a benchmark rate and ask whether applying the same rate to RSV/GAS resurgence wave case counts yields a meaningful PAIS burden estimate. This is back-of-envelope but bounded.
- A formal extension would require collaboration with mathematical epidemiologists (House is a potential contact — he co-authors Munro2025 and is at Manchester).
- Major uncertainty: PAIS transition rates from non-COVID endemic pathogens are essentially unknown. Without this parameter, the model is non-identifiable.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (population-level analog of attractor dynamics); `hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a` (SIRS return-to-baseline is a population-level version of recovery gradient).
- Required data or analyses: Post-RSV/GAS PAIS incidence rates (literature survey); Munro2025 model code adaptation; `question:0008` formalization as prerequisite for consistent parameterization.
- Priority level: Low (speculative, requires parameter inputs not yet available; useful to track as the immunity debt resurgence literature matures).

## Related

- Topic notes: `paper:Munro2025` — SIRS model source; cycles peer project — seasonal epidemiology context.
- Article notes: Baker et al. 2020 (PNAS); Messacar et al. 2022 (Lancet); Kinyanjui et al. 2015 (PLoS One — RSV herd immunity in low-income settings, co-authored by House).
- Methods/Datasets: Munro2025 model code at https://github.com/thomasallanhouse/covid19-incidence/blob/main/debt.ipynb.
