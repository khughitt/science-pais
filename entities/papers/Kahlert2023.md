---
id: paper:Kahlert2023
kind: paper
title: Post-Acute Sequelae After Severe Acute Respiratory Syndrome Coronavirus 2
  Infection by Viral Variant and Vaccination Status
status: active
ontology_terms:
- long COVID
- PASC
- SARS-CoV-2 variants
- vaccination
- healthcare workers
- Omicron
- wild-type
- negative-binomial regression
- cross-sectional study
dataset_usage: []
source_refs:
- cite:Kahlert2023
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
- question:0003-acute-severity-threshold-for-self-sustaining-pais
- question:0012-prevention-vaccination-antiviral-reduces-pais
created: '2026-07-10'
updated: '2026-07-10'
---

# Post-Acute Sequelae After Severe Acute Respiratory Syndrome Coronavirus 2 Infection by Viral Variant and Vaccination Status

- **Authors:** Christian R. Kahlert, Carol Strahm, Sabine Güsewell, Alexia Cusini, et al. (SURPRISE Study Group)
- **Year:** 2023
- **Journal:** Clinical Infectious Diseases 77(2):194–202
- **DOI:** 10.1093/cid/ciad143
- **PMCID:** PMC10371307
- **BibTeX key:** Kahlert2023
- **Source:** PDF

## Key Contribution

Among 2912 healthcare workers (HCWs) in northeastern Switzerland, viral variant was the dominant
determinant of PASC symptom burden after adjustment for vaccination status and confounders. Wild-type
(aRR 2.81, 95% CI 2.08–3.83) and Alpha/Delta (aRR 1.93, 95% CI 1.10–3.46) infections were
significantly associated with excess PASC symptoms, while Omicron BA.1 (aRR 1.29, 95% CI 0.69–2.43)
and vaccination before Omicron BA.1 infection (aRR 1.27, 95% CI 0.82–1.94) were not. The study
provides a well-controlled within-cohort comparison across variants with serologically confirmed
uninfected controls — a design feature absent from many earlier long-COVID prevalence studies.

## Methods

**Design:** Multicenter cross-sectional analysis (May/June 2022) embedded in the prospective SURPRISE
cohort (9 healthcare networks, north-eastern Switzerland; cohort launch July/August 2020).

**Participants:** 2912 HCWs (median age 44 years; 81.3% female). 1685 (57.9%) had at least one
confirmed SARS-CoV-2 infection; 1227 served as seronegative controls (no positive swab; negative
anti-nucleocapsid [anti-N] antibody at May/June 2022 survey).

**Variant assignment:** Inferred from population-level sequencing data by date of first positive swab
— wild-type (Feb 2020 – Jan 2021), Alpha/Delta merged (Feb 2021 – Dec 2021; Alpha period merged
due to small numbers), Omicron BA.1 (Jan – Jun 2022).

**Outcome:** Sum of 18 self-reported symptoms lasting >7 days and not present before the pandemic
(loss of smell/taste, shortness of breath, chest pain, hair loss, brain fog, tiredness/weakness, skin
rash, muscle/limb pain, joint pain, headache, nausea/anorexia, dizziness, stomachache, diarrhea,
burnout/exhaustion, fever, chills, cough). Main analysis: negative-binomial regression of symptom
count. Additional outcomes: Fatigue Severity Scale (FSS), PHQ-9, GAD-7, self-rated health (SRH),
Post-COVID-19 Functional Status Scale (PCFS), and self-classification as having long COVID.

**Vaccination sub-analyses:** Stratified by unvaccinated, 1–2 doses, and ≥3 doses (booster) before
infection. Delta/Omicron periods only for booster comparisons (boosters unavailable earlier).

**Serological confirmation:** Roche Elecsys anti-S and anti-N assays; anti-N used to identify
controls and exclude seropositive non-swabbed participants.

**Statistical:** Univariable and multivariable negative-binomial regression; STROBE-compliant;
complete-case and multiple-imputation sensitivity analyses; sensitivity analysis restricted to
participants with full longitudinal serology (to exclude undetected prior infection).

## Key Findings

**PASC symptom burden by variant (unadjusted):**
- Wild-type: estimated mean 1.12 symptoms (95% CI 0.88–1.45; P < .001); median 18.3 months since
  infection.
- Alpha/Delta: 0.67 (95% CI 0.51–0.89; P < .001); median 6.5 months since infection.
- Omicron BA.1: 0.52 (95% CI 0.45–0.61; P = .005); median 3.1 months since infection.
- Controls: 0.39 (95% CI 0.34–0.45).

**Multivariable analysis (n = 2452):**
- Wild-type: aRR 2.81 (95% CI 2.08–3.83) — strongly significant.
- Alpha/Delta: aRR 1.93 (95% CI 1.10–3.46) — significant.
- Omicron BA.1: aRR 1.29 (95% CI 0.69–2.43) — non-significant.
- Vaccination before infection: aRR 1.27 (95% CI 0.82–1.94) — non-significant.
- Other covariates independently significant: BMI > 30 (aRR 1.43), any comorbidity (aRR 1.35), any
  medication (aRR 1.49), cumulative COVID-19 patient contact (aRR 1.11 per order-of-magnitude
  increase).

**Vaccination × Omicron BA.1 interaction (unadjusted):**
- Unvaccinated: 0.36 (95% CI 0.22–0.60).
- 1–2 doses before infection: 0.71 (95% CI 0.53–0.95; P = .028 vs unvaccinated).
- ≥3 doses (boosted): 0.49 (95% CI 0.41–0.58; P = .30 vs unvaccinated).
- Counterintuitive pattern: partially vaccinated had significantly higher symptom burden than
  unvaccinated after Omicron BA.1 infection; boosted was intermediate and non-significant.

**Additional outcomes:**
- FSS (fatigue) and PHQ-9 (depression) elevated only for wild-type vs controls; not significantly
  different for Alpha/Delta or Omicron BA.1 vs controls.
- GAD-7 (anxiety) did not differ across groups.
- SRH (self-rated health) slightly lower for wild-type and Alpha/Delta vs controls but not Omicron BA.1.
- Self-reported long COVID prevalence: 17.1% (wild-type), 10.4% (Alpha/Delta), 4.8% (Omicron BA.1),
  0.9% (controls) — all P < .001 vs controls.
- Those self-reporting long COVID averaged 3.2 PASC symptoms vs 0.41 in those without long COVID.

**Symptom profile:**
- Most commonly reported symptoms in infected participants: tiredness/weakness (14.7%), loss of
  smell/taste. In uninfected: tiredness/weakness (9.4%).
- Symptoms consistently associated across all variants in unvaccinated: loss of smell/taste, hair loss.
- Symptoms consistently associated across all variants in vaccinated: loss of smell/taste, brain fog.
- Reinfected participants (excluded from main analysis) had symptom scores similar to wild-type,
  suggesting cumulative viral exposure raises PASC burden.

## Relevance

**hypothesis:0004-acute-severity-threshold:** The variant-era gradient (wild-type > Alpha/Delta >
Omicron) is compatible with the acute-severity-threshold framing: Omicron caused less severe acute
illness and produced the smallest PASC burden, becoming non-significant after adjustment. However,
variant is a compound proxy (intrinsic pathogenicity + immune evasion + population immunity state) and
does not isolate acute severity per se. The 18-month persistence of wild-type PASC excess is a strong
signal that early-pandemic insults crossed a durable threshold. Adds to supporting evidence for h0004
while sharing the mechanism-mixing limitation of all cross-variant observational designs.

**hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent:** The
time-since-infection differential is a critical ascertainment confound: wild-type is measured at 18.3
months, Alpha/Delta at 6.5 months, and Omicron BA.1 at 3.1 months post-infection. Natural resolution
of early PASC over time means the between-variant raw symptom differences include both a true variant
effect and a time-since-infection recovery effect. The study partially addresses this by showing that
after adjusting for acute symptom count, wild-type still exceeded Alpha/Delta and Omicron BA.1
(Supplementary Figure 6), and by confirming similar patterns in unvaccinated participants across
variants. Still, a clean within-person longitudinal design with matched follow-up windows would be
needed to fully separate time from variant. The self-report symptom battery and cross-sectional recall
also create typical ascertainment artifacts. Directly supports h0008's claim that measurement channel
shapes apparent group differences.

**hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a:** The
persistence of elevated PASC burden at 18 months post wild-type infection is relevant evidence.
Wild-type cases still report significantly more symptoms 18 months later, consistent with either a
slow-gradient account (still recovering) or a stable attractor account (trapped). This paper does not
track individuals longitudinally, so it cannot distinguish gradient from plateau. The fact that Omicron
BA.1 is near-baseline at 3 months could reflect rapid resolution (consistent with gradient) or simply
a milder initial perturbation that never crossed any threshold.

**hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only:** This paper
partially contradicts h0011 in that wild-type infection — the highest-severity variant — is the only
group with elevated FSS (fatigue) scores relative to controls, not Omicron BA.1. However, the
interpretation is complicated: (1) the variant comparison confounds severity with time since
infection, (2) FSS compares each variant group to its own-era controls, so the null for Omicron BA.1
vs controls may reflect faster recovery, not absence of fatigue pathogenesis. The finding that
tiredness/weakness was the most common PASC symptom across variants but also common in uninfected
participants underscores h0011's core concern about nonspecific fatigue confounding.

**question:0012-prevention-vaccination-antiviral-reduces-pais:** The paradoxical Omicron BA.1
vaccination finding (1–2 doses: higher symptom score than unvaccinated; boosted: intermediate) adds
conflicting evidence on whether vaccination before Omicron infection reduces PASC. This contradicts
Nehme et al (2023), which found a protective effect of vaccination after Omicron in a general adult
outpatient population. The authors attribute the discrepancy to population differences (HCW vs general)
and definition differences (Nehme treated partly vaccinated as unvaccinated). This paper raises the
possibility that in a high-baseline-immunity HCW population, pre-infection vaccination does not reduce
Omicron PASC and might paradoxically increase it under some definitions — adding a cautionary data
point to q0012 without resolving the mechanism.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Viral variant as primary PASC determinant | Acute antigen/severity burden (proposition:0021) | Variant is a proxy; pathogenicity + immune evasion + host immunity state are all bundled |
| Variant-era symptom gradient (WT > Alpha/Delta > Omicron) | Acute severity threshold (hypothesis:0004) | Supports threshold framing but cannot isolate severity from other variant-era differences |
| Vaccination before Omicron BA.1 not protective (aRR 1.27) | Vaccination reduces PASC (question:0012) | Contradicts many pre-Omicron studies; partially vaccinated paradox unresolved |
| Anti-N seronegative controls | Rigorous uninfected reference group | Key strength distinguishing this study from many prior studies lacking controls |
| Time-since-infection confound (18.3 vs 3.1 months) | Measurement-channel bias (hypothesis:0008) | Within-cohort cross-sectional design cannot match follow-up windows across variant eras |
| Self-reported 18-symptom battery | Self-report ascertainment (hypothesis:0008, 0017) | Nonspecific symptoms common in uninfected controls (9.4% tired/weak) — highlights nonspecificity |
| Wild-type burden persisting at 18 months | Attractor vs gradient (hypothesis:0010) | Compatible with either; within-person longitudinal data needed to distinguish |

## Limitations

1. **Variant assignment is ecological, not individual:** Variant was inferred from population sequencing
   data by date of first positive swab, not from individual-level sequencing. Misclassification is
   likely (especially at transition periods), probably biasing toward null (diluting between-variant
   differences).

2. **Unequal follow-up windows across variant eras:** Wild-type measured 18.3 months post-infection,
   Omicron BA.1 only 3.1 months. Natural PASC resolution over time confounds the between-variant
   comparison, even though sensitivity analyses adjusting for acute symptom count partially mitigate this.

3. **HCW sample limits generalizability:** Predominantly young, healthy, white, female HCWs.
   Omicron BA.1 findings may not apply to elderly, immunocompromised, or highly comorbid populations
   where acute infection is more severe and PASC risk may be higher.

4. **Results not applicable to newer Omicron sub-variants:** Data limited to Omicron BA.1 (Jan–Jun
   2022); subsequent XBB, BQ.1, etc. differ in further immune evasion and could have different PASC
   profiles.

5. **Self-report outcome:** 18-symptom battery with a 7-day duration criterion (less strict than WHO
   12-week definition); burnout/exhaustion is similar to tiredness (sensitivity analysis excluded
   burnout). The large number of symptoms and lower time criterion may overestimate prevalence; missing
   symptoms (e.g., palpitations) may underestimate it.

6. **Control group seronegative definition has caveats:** Anti-N sensitivity wanes over time (~92% at
   18 months). Some truly infected individuals in the control group could have been missed, diluting
   the between-group contrast toward null. Authors use both criteria (swab + anti-N negativity) and
   note sensitivity analysis with longitudinal serology largely confirms main findings.

7. **Paradoxical vaccination finding is not fully explained:** The 1–2 dose group having higher
   unadjusted symptoms than unvaccinated after Omicron BA.1 infection is unexpected and could reflect
   residual confounding (sicker/more cautious HCWs were vaccinated first but not boosted) or immune
   imprinting. The multivariable estimate (aRR 1.27, CI 0.82–1.94) is non-significant but the pattern
   is unexplained and deserves further investigation.

8. **Cross-sectional design precludes trajectory inference:** The study cannot determine whether
   observed PASC at the time of survey represents plateau (chronic attractor) or a point on a slow
   recovery slope (gradient).

## Model / Tool Availability

Not applicable — this is an observational epidemiology study; no model or tool was released.

## Follow-up

- **Papers to read next:**
  - Nehme 2023 (Clin Infect Dis 76:1567–75) — Omicron-specific vaccination × PASC study with
    contrasting protective vaccination finding; direct counterpoint to the paradoxical Omicron
    vaccination result here.
  - Strahm 2022 (Clin Infect Dis 75:e1011–9) — preceding SURPRISE cohort paper on long-COVID in
    HCWs; baseline anchor for this study.
  - Carazo2025 — Quebec HCW cohort showing strong hybrid immunity protection; compare with the
    null vaccination finding here.

- **Questions this raises for the project:**
  - Does partial vaccination before Omicron BA.1 genuinely confer higher PASC risk than no
    vaccination, and if so is immune imprinting (original antigenic sin) a plausible mechanism?
    → Reserve as new question.
  - Can variant-era reductions in PASC incidence be decomposed into reduced intrinsic viral
    pathogenicity, changes in population immunity, and time-since-infection ascertainment artifact?
    → Reserve as new question.
