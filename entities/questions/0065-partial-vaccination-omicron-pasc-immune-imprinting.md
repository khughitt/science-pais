---
id: question:0065-partial-vaccination-omicron-pasc-immune-imprinting
kind: question
title: Does partial vaccination before Omicron infection paradoxically increase PASC
  risk via immune imprinting, and can this be separated from confounding?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Kahlert2023
related:
- question:0012-prevention-vaccination-antiviral-reduces-pais
- hypothesis:0004-acute-severity-threshold
created: '2026-07-10'
updated: '2026-07-10'
---

# Does partial vaccination before Omicron infection paradoxically increase PASC risk via immune imprinting, and can this be separated from confounding?

## Summary

Kahlert2023 (SURPRISE Swiss HCW cohort) found that after Omicron BA.1 infection, individuals with
1–2 prior vaccine doses had significantly higher unadjusted PASC symptom scores (0.71) than
unvaccinated individuals (0.36; P = .028), while boosted individuals (≥3 doses) were intermediate
(0.49; P = .30 vs unvaccinated). This counterintuitive pattern — partial vaccination associated with
worse, not better, PASC outcomes — could reflect: (a) immune imprinting (original antigenic sin),
where prior WT-spike vaccine responses are recalled preferentially during Omicron infection, impairing
class-switching toward Omicron-specific responses and potentially prolonging antigen exposure;
(b) confounding (partially vaccinated HCWs may systematically differ from unvaccinated HCWs in age,
health-seeking behavior, number of exposures, or propensity to seek care for symptoms); or (c) a
chance/small-sample finding (groups were small). This question asks whether a genuine immune-imprinting
mechanism underlies the paradoxical finding and how it can be disentangled from confounding.

## Why It Matters

- If confirmed as a true biological effect, it would suggest that partial mRNA vaccination specifically
  against WT spike creates an imprinting state that impairs Omicron-specific immune resolution and
  elevates PASC risk — with direct implications for the vaccine schedule debate and for mechanism
  framing of PASC under Omicron.
- If confounded, the finding underscores the limits of simple vaccination-status stratification in
  HCW cohorts and cautions against interpreting unadjusted vaccine-PASC contrasts. Ignoring this
  ambiguity risks either falsely implicating vaccination or missing a genuine biological effect.

## Current Evidence

- **Supporting a paradoxical/imprinting effect:**
  - Kahlert2023: 1–2 dose group had statistically significantly higher unadjusted PASC symptoms than
    unvaccinated after Omicron BA.1 (P = .028); boosted group was intermediate and non-significant.
  - The immune imprinting literature for antibody responses shows that WT-primed individuals
    preferentially boost WT-strain antibodies even after Omicron infection, potentially at the cost of
    Omicron-specific breadth. Whether this translates to impaired PASC resolution is speculative.
- **Supporting a confounding explanation:**
  - Kahlert2023 multivariable model: vaccination before infection was aRR 1.27 (CI 0.82–1.94) —
    non-significant after adjustment for confounders.
  - The SURPRISE cohort recruited from 9 hospital networks; partially vaccinated HCWs in 2022 were an
    atypical group (vaccine hesitancy partially, delays partially, or newly eligible) that may differ
    systematically from never-vaccinated HCWs.
  - Nehme 2023 (same Omicron period, Swiss general outpatients) found a protective effect of
    vaccination for PASC after Omicron — contradicting the paradoxical direction here.
- **Conflicting:**
  - Carazo2025 (Quebec HCW cohort) found strong hybrid-immunity protection against long COVID,
    including in Omicron era; their definition treated partly vaccinated differently.
  - The boosted group in Kahlert2023 also showed no statistically significant protection, but trended
    toward a lower score than 1–2 dose, consistent with either dose-response recovery or dose-response
    imprinting partial correction.

## Thoughts

- Best current interpretation: the paradoxical finding is most likely confounded — partially vaccinated
  HCWs in Switzerland in early 2022 were a heterogeneous group that may have included higher-risk or
  more symptom-aware individuals. The multivariable result is non-significant, and direct comparisons
  with Nehme2023 and Carazo2025 suggest protective vaccination effects in similar populations. A
  genuine imprinting mechanism is plausible in antibody studies but has not been demonstrated for PASC
  resolution specifically.
- Major remaining uncertainty: no study has directly tested whether WT-spike-dominated antibody
  imprinting (vs Omicron-specific) correlates with or causally mediates PASC symptom persistence after
  Omicron infection. A within-person design measuring both antibody imprinting depth (WT:Omicron ratio)
  and longitudinal PASC symptoms would be needed.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (partial vaccination may not prevent
  crossing an acute insult threshold for Omicron); `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent`
  (confounding in vaccination-status stratification is exactly the measurement-channel artifact this
  hypothesis covers).
- Related questions: `question:0012-prevention-vaccination-antiviral-reduces-pais` — this is a
  specific counter-evidence case for q0012's pro-vaccination conclusion.
- Required data or analyses: (1) Cohort with vaccine-history detail AND individual Omicron-specific
  antibody profiles post-infection AND longitudinal PASC symptoms; (2) Causal inference or propensity-
  score design to balance partially vaccinated vs unvaccinated HCWs on all confounders; (3) Replication
  across other Omicron-era HCW cohorts.
- Priority level: P3 — mechanistically interesting (immune imprinting × PASC is a novel angle) but
  evidence for the effect is weak and single-study; worth tracking as Omicron-era cohort literature
  matures.

## Related

- Topic notes: `topic:population-boundary-conditions-and-effect-modifiers-in-pais`.
- Article notes: `paper:Kahlert2023` (source); Nehme2023 (contradicting protective finding).
- Methods/Datasets: Omicron-era cohorts with individual variant sequencing, antibody imprinting assays,
  and longitudinal PASC outcome follow-up.
