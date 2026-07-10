---
id: "paper:Azhir2026"
kind: "paper"
title: "The age paradox in post-infectious sequelae: physiological reserve outweighs chronological age in Long COVID susceptibility"
status: "active"
paper_kind: ""
ontology_terms:
- biology:post-acute-sequelae
- biology:immune-aging
- biology:comorbidity
dataset_usage: []
source_refs:
- cite:Azhir2026
related:
- hypothesis:0020-host-immune-baseline-reserve-gate
- hypothesis:0004-acute-severity-threshold
- hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
created: "2026-07-10"
updated: "2026-07-10"
---

# The age paradox in post-infectious sequelae: physiological reserve outweighs chronological age in Long COVID susceptibility

<!--
- **Authors:** Alaleh Azhir, Jingya Cheng, Jiazi Tian, Ingrid V. Bassett, Chirag J. Patel, Jeffrey G. Klann, Shawn N. Murphy, Hossein Estiri
- **Year:** 2026
- **Journal:** medRxiv preprint (not peer-reviewed)
- **DOI/URL:** https://doi.org/10.64898/2026.02.24.26346989
- **BibTeX key:** Azhir2026
- **Source:** PDF
- **Preprint:** yes — posted February 26, 2026 (medRxiv / openRxiv); not yet peer-reviewed
-->

## Key Contribution

Using a validated 133,792-patient EHR cohort (Mass General Brigham Precision PASC Research Cohort, P2RC), this preprint demonstrates that the apparent association between older chronological age and PASC risk is substantially, and perhaps entirely, mediated by accumulated comorbidity burden. After adjustment for comorbidity, each decade of age is associated with a 6% *lower* odds of PASC (OR 0.94; 95% CI 0.93–0.95), and causal mediation analysis reveals that comorbidities account for 145% of the crude age effect — a proportion exceeding 100%, indicating inconsistent mediation in which age's direct protective effect is masked by its indirect harm through chronic disease accumulation. This protective direct effect of age disappears entirely after age 65 (ADE: +0.0020, p=0.14), where chronological age regains prognostic relevance as accumulated reserve mechanisms become exhausted. The paper reframes PASC risk stratification: physiological reserve (operationalized by Charlson Comorbidity Index), not birth year, is the primary determinant of PASC susceptibility in adults younger than 65.

## Methods

**Study design:** Retrospective cohort using electronic health records.

**Cohort:** Precision PASC Research Cohort (P2RC), Mass General Brigham — 133,792 COVID-19 patients comprising 171,050 infection episodes from 12 hospitals and 20 community health centers in Massachusetts. COVID-19 infections from March 6, 2020 to May 8, 2024; follow-up through May 2025. Of these, 24,833 developed PASC within 12 months of infection; 108,959 did not.

**PASC ascertainment:** Validated computational phenotyping algorithm (Azhir et al. 2024, Med); PASC defined per NASEM/WHO as an infection-associated chronic condition unexplained by other conditions, persisting >2 months post-infection. The algorithm uses an exclusion-based approach — a new condition (e.g., dyspnoea) is attributed to PASC only if no prior diagnosis existed in the EHR from 2017 onward. Outcome can recur across re-infections.

**Primary analysis:** Generalised estimating equations (GEE) logistic regression with exchangeable working correlation structure and cluster-robust variance. Predictors: age (per 10-year increment), sex, race, ethnicity, time (year-quarter), Charlson Comorbidity Index (modeled as restricted cubic splines for non-linearity), disease severity (3 levels: non-hospitalised, hospitalised, ICU/ventilation), vaccination status. Age–CCI correlation assessed with Pearson r.

**Causal mediation:** Counterfactual framework; two separate analyses with (1) CCI and (2) acute COVID-19 severity as mediators. Partitioned total effect into ACME (indirect) and ADE (direct). Pre-specified age-stratified analyses: <65 vs ≥65 years.

**Specification Curve Analysis:** 768 specifications across combinations of covariate sets, subgroups (sex, race, three age bands), and model configurations. Visualized as specification curves.

**Statistics:** R 4.3.0; geepack, specr, lm4, forestplot packages. Code: https://github.com/clai-group/PASC_Risk_study

**Ethics:** MGB IRB protocol #2020P001063; waiver of consent for data-only retrospective study.

## Key Findings

**Cohort characteristics:** Mean age 57.5 years (SD 17.2); 63.3% female; 75.3% White, 8.6% Black, 5.3% Hispanic; 91.5% non-hospitalised; 6.4% hospitalised; 2.1% ICU/ventilation; 66.1% vaccinated. PASC cases had mean age 60.5, mean CCI 2.87 vs 2.06 in non-PASC. Age and CCI strongly correlated (r = 0.698, 95% CI 0.695–0.701, P < 0.001).

**Primary adjusted associations (comorbidity-adjusted):**
- Age per decade: OR 0.94 (0.93, 0.95), p<0.001 — protective
- Male vs female: OR 0.81 (0.79, 0.84), p<0.001 — 19% lower odds for males
- Black vs White: OR 1.06 (1.01, 1.12), p=0.013 — modestly elevated
- Asian vs White: OR 0.91 (0.85, 0.98), p=0.014
- Vaccination vs unvaccinated: OR 0.94 (0.91, 0.98), p=0.002 — 6% protection
- Hospitalised vs non-hospitalised: OR 1.35 (1.29, 1.42), p<0.001
- ICU/ventilation vs non-hospitalised: OR 1.93 (1.80, 2.07), p<0.001
- Hispanic ethnicity: OR 0.94 (0.88, 1.01), p=0.083 — non-significant

**Comorbidity dose-response (non-linear):** CCI 0 = reference; CCI 5 → OR 2.73; CCI 10 → OR 3.46. The relationship shows a steep initial increase at lower CCI values, attenuating at high burden (consistent with survivorship bias or saturation of comorbidity-PASC pathways).

**Causal mediation — comorbidity mediator:**
- ACME (indirect, via CCI): +0.0137/decade (95% CI 0.0127, 0.0145), p<0.001
- ADE (direct effect of age, adjusting for CCI): -0.0042 (95% CI -0.0055, -0.0032), p<0.001
- Total effect: +0.0094/decade — positive because comorbidity harm dominates
- Proportion mediated by CCI: 145% — inconsistent mediation, comorbidity masks age's protective effect

**Causal mediation — severity mediator:**
- ACME (indirect, via severity): -0.0011/decade (95% CI -0.0012, -0.0010), p<0.001 — negative (age reduces severity → reduces PASC)
- ADE (direct effect of age, adjusting for severity): -0.0079 (95% CI -0.0101, -0.0059), p<0.001
- Total effect: -0.0090/decade — protective when age's severity-reducing role is removed from confounding
- Proportion mediated via severity: 12%

**Age-stratified mediation:**
- Adults <65 years: robust direct protective effect preserved (ADE: -0.0042, p<0.001); comorbidity-mediated suppression = 152%; inconsistent mediation pattern
- Adults ≥65 years: direct protective effect disappears entirely (ADE: +0.0020, p=0.14); full mediation through comorbidity (81%) and severity (26%); both indirect pathways indicate increased PASC risk, eliminating age-related resilience

**Specification Curve Analysis:** 768 specifications assessed; among 384 including comorbidity adjustment, 132 (34.4%) showed statistically significant protective effects of age; only 24 (6.25%) showed significant positive associations. Exception: Black males <45 years consistently showed positive age estimates irrespective of comorbidities.

**Reinfection escalation (from Discussion, citing Bowe2022):** Hazard ratio for at least one PASC sequela rises from ~1.35 after first infection to 2.11 after second and 3.00 after three or more infections — raising the possibility of progressive immunological scarring with each PASC episode.

## Relevance

This paper provides the largest and most methodologically rigorous evidence to date for `hypothesis:0020` (host-immune-baseline-reserve-gate): it operationalizes physiological reserve as Charlson Comorbidity Index, demonstrates that reserve (CCI burden) — not chronological age — is the primary gate for PASC incidence in adults <65, and provides a causal decomposition of the age-PASC relationship into reserve-mediated and direct-protective components. Key connections:

- **`hypothesis:0020` (host-immune-baseline-reserve-gate):** Directly supports P1 (reduced pre-infection reserve raises PASC risk independent of acute severity), P3 (measurable reserve axis — CCI — rank-orders PASC risk), and offers an operational pre-infection reserve proxy. The paper's finding that severity mediates only 12% (vs 145% for comorbidity) supports that reserve operates largely independent of acute insult magnitude.
- **`hypothesis:0004` (acute-severity-threshold):** Complicates the acute-severity framing — severity accounts for only 12% of age's total effect on PASC, while comorbidity (reserve) accounts for 145%. This does not falsify h0004 (severity still elevates PASC risk, OR 1.35–1.93), but it establishes that the severity term is subordinate to the reserve term in explaining population-level age-PASC risk. The age-65 threshold where direct protective mechanisms fail is a new empirical anchor for where the reserve-dominated regime transitions to a severity-reserve compound regime.
- **`hypothesis:0011` (severity does not predict chronic fatigue):** The mediation result (severity mediating only 12% of age-PASC) is consistent with severity being a minor driver; however, this paper uses aggregate PASC diagnosis, not phenotype-resolved fatigue/organ-damage endpoints — so it cannot directly test h0011's phenotype-specific claim.
- **`hypothesis:0008` (measurement and ascertainment bias):** The paper acknowledges residual confounding from healthcare access and SES; the validated EHR phenotyping algorithm and specification curve robustness provide some protection but do not eliminate ascertainment concerns. The Black male under-45 exception in SCA may reflect an ascertainment or population-stratification artifact.
- **`question:0033` (frailty as PASC boundary condition):** The CCI is an aggregate comorbidity metric that likely includes frailty-adjacent conditions; this paper's result is consistent with q0033's framing, though it does not test frailty as a distinct construct (cf. Hammel2023 noted in h0004 which also failed to separate reserve from severity).

The paper also raises a new possibility — progressive PASC recurrence as immunological scarring — that could be framed as a new question for the project.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Physiological reserve | Pre-infection immune homeostatic reserve (h0020 P1) | Operationalized as CCI; broader project uses "reserve" to include immune baseline |
| Charlson Comorbidity Index | Reserve proxy / pre-infection reserve axis | Paper's empirical choice; project would want biological proxies (inflammatory tone, naïve-T fraction) |
| Age-65 direct-effect threshold | Reserve exhaustion transition point | Mechanistic basis unexplained; immunological, metabolic, or tissue-repair origin speculated |
| Inconsistent mediation (145%) | Reserve-vs-severity gate competition | Comorbidity dominating over acute severity supports reserve as the dominant upstream term |
| Reinfection PASC HR escalation | Immunological scarring / attractor persistence | Adjacent to h0001 (shared dysregulated attractor) — prior PASC may lower threshold for re-entry |
| Vaccination OR 0.94 | Prevention/modification evidence | Consistent with h0004 prevention arm; small effect |
| Female predominance (65.4% PASC vs 62.8% non-PASC) | Sex-linked PASC susceptibility | Aligns with h0005 (reproductive-stage-immune-homeostatic-margin) and autoimmune biology |

## Limitations

- **Single healthcare system:** MGB is a tertiary-referral New England system; generalizability to community, non-White, or LMIC populations is uncertain. The authors note this explicitly.
- **EHR phenotyping:** The P2RC algorithm uses structured clinical data, which lacks depth of clinical narratives, may miss diagnoses coded elsewhere, and can underreport symptoms that patients do not bring to clinical attention. This is partially mitigated by the validated exclusion-based phenotyping approach.
- **Residual confounding:** Socioeconomic status, healthcare access, behavioural variables, and health literacy are unmeasured. These could drive apparent race-group differences and the comorbidity-PASC association.
- **Causal mediation assumptions:** The counterfactual framework requires no unmeasured confounding of the exposure-mediator, mediator-outcome, and exposure-outcome relationships. Violations (particularly socioeconomic confounders affecting both CCI accumulation and PASC ascertainment) could bias the mediated proportions.
- **Charlson Index as reserve proxy:** CCI is a blunt aggregate of specific chronic conditions originally developed for mortality prediction; it is not a direct measure of immunological reserve, biological age, or physiological resilience. The non-linear CCI–PASC relationship and attenuation at high CCI (survivorship bias) are noted but not fully resolved.
- **PASC not phenotyped by domain:** The analysis collapses fatigue, cognitive, autonomic, and organ-damage phenotypes into a single PASC outcome. The age-reserve relationship may differ across phenotypes — not tested here.
- **Observational design:** Cannot distinguish direct age biology from CCI confounding at residual level; cannot adjudicate immunological scarring vs. competing risk explanations for the reinfection HR escalation.
- **Age-65 threshold:** Pre-specified on clinical-policy grounds, not derived from the data; the true biological transition may not fall exactly at this threshold.
- **Preprint:** Not yet peer-reviewed.

## Model / Tool Availability

Analysis code is publicly available at https://github.com/clai-group/PASC_Risk_study (R 4.3.0; geepack, specr, lm4, forestplot packages). Patient-level data from P2RC cannot be shared due to IRB restrictions. No new software model or dataset is released; the P2RC cohort is an MGB internal resource.

## Follow-up

**Papers to read next:**
- Azhir et al. 2024, *Med* (N Y) — the P2RC validation paper (ref [37]); needed to assess phenotyping algorithm specificity and cohort construction
- Hammel2023 (already in project) — frailty→PASC dose-response in VA veterans; compare to this paper's CCI findings and the severity non-adjustment problem identified in h0004
- Papers on biological age clocks and PASC (refs [1–3]: Ho2023, Wu2021, An2022) — if biological age measures outperform CCI as reserve proxy

**Questions this raises:**
- Does the age-65 resilience threshold differ by PASC phenotype (fatigue/cognitive vs. organ-damage)? [new question, see below]
- Does serial PASC episode accumulation deplete physiological reserve in a dose-dependent way (immunological scarring model)? [new question]
- Can CCI or a refined proxy serve as a pre-infection reserve measure for PASC risk prediction across other PAIS (ME/CFS, PTLD, post-dengue)? [links to q0033, q0042]
