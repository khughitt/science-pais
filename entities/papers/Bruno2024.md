---
id: paper:Bruno2024
kind: paper
title: "Association between acquiring SARS-CoV-2 during pregnancy and post-acute sequelae
  of SARS-CoV-2 infection: RECOVER electronic health record cohort analysis"
status: active
ontology_terms:
- PASC
- long COVID
- pregnancy
- SARS-CoV-2
- immune tolerance
- thromboembolism
- cardiovascular
- cognitive impairment
- fatigue
- EHR cohort
- RECOVER initiative
dataset_usage: []
source_refs:
- cite:Bruno2024
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0007-mechanism-of-female-predominance-in-pais
created: '2026-07-07'
updated: '2026-07-07'
---
# Association between acquiring SARS-CoV-2 during pregnancy and post-acute sequelae of SARS-CoV-2 infection: RECOVER electronic health record cohort analysis

- **Authors:** Ann M. Bruno, Chengxi Zang, Zhenxing Xu, Fei Wang, Mark G. Weiner, Nick Guthe, Megan Fitzgerald, Rainu Kaushal, Thomas W. Carton, Torri D. Metz; on behalf of the RECOVER EHR Cohort and RECOVER Pregnancy Cohort
- **Year:** 2024
- **Journal:** eClinicalMedicine
- **DOI:** 10.1016/j.eclinm.2024.102654
- **BibTeX key:** Bruno2024
- **Source:** XML full text via Europe PMC (PMC11137338)

## Key Contribution

Bruno et al. report the first large-scale comparison of PASC incidence between individuals who acquired SARS-CoV-2 during pregnancy versus outside of pregnancy, using a computable phenotype applied to 89,312 females aged 18–49 in the RECOVER PCORnet EHR dataset across 19 US health systems.
COVID-19 acquired during pregnancy was associated with a lower overall PASC incidence at 30–180 days post-infection (aHR 0.85, 95% CI 0.80–0.91), but with a dissociated phenotype: elevated risk for vascular/cardiac components (abnormal heartbeat, thromboembolism) and markedly reduced risk for cognitive and fatigue components (malaise/fatigue, cognitive problems).
The authors interpret this dissociation through the lens of pregnancy's immune tolerant state — the same downregulated Th1/inflammatory milieu that worsens acute infection severity may suppress the immunopathological cascade that drives fatigue/cognitive PASC, while leaving vascular/thromboinflammatory risk intact or elevated.

## Methods

**Design:** Retrospective cohort study using the RECOVER Initiative PCORnet EHR dataset.

**Population:** Females aged 18–49 with lab-confirmed (nucleic acid or antigen test) SARS-CoV-2 infection, March 2020–June 2022. Pregnancies identified using a validated ICD-10 hierarchical algorithm requiring delivery >20 weeks' gestation; pregnancies ending <20 weeks were excluded. N = 5,397 pregnant; N = 83,915 non-pregnant (outside of pregnancy).

**Health systems:** 19 US health systems contributing inpatient and outpatient EHR data (~10 million total patients in the PCORnet infrastructure).

**Exposure:** SARS-CoV-2 acquired during a confirmed ongoing pregnancy (gestational age defined as delivery date minus gestational age at delivery). Individuals with pregnancy and non-concurrent SARS-CoV-2 infection were excluded.

**Primary outcome:** PASC at 30–180 days post-infection, using a previously validated computable phenotype (Thaweethai et al., developed in the non-pregnant adult RECOVER cohort). Anemia was excluded from the 25-component phenotype a priori given its high baseline prevalence in pregnant/postpartum individuals; 24 conditions remained.

**Statistical approach:** Stabilized inverse probability of treatment weighting (IPTW) adjusting for age, race/ethnicity, BMI, area deprivation index, tobacco use, Elixhauser comorbidities, COVID-19 vaccination status, acute COVID-19 severity (outpatient vs inpatient/ICU), and pandemic era (as a variant surrogate). Cox proportional hazards models with Bonferroni-corrected p-values. Two sensitivity analyses: (1) phenotype redefined excluding thromboembolism/pulmonary embolism; (2) propensity score matched comparison.

**Pandemic era coverage:** March 2020–June 2022, spanning Alpha, Delta, and early Omicron; variant was not analyzed separately due to insufficient subgroup N.

**Gestational timing:** Median gestational age at infection was 34 weeks (IQR 25–38); sub-analysis by gestational week was not performed (insufficient N).

## Key Findings

**Primary outcome — overall PASC:**

- Pregnancy-group PASC incidence: 25.5% vs non-pregnancy: 33.9%; aHR 0.85 (95% CI 0.80–0.91, p < 0.001).
- Cumulative incidence at 180 days: 30.8 per 100 (pregnant) vs 35.8 per 100 (non-pregnant).
- Robust to sensitivity analyses: excluding VTE from phenotype gave aHR 0.84 (0.79–0.90); propensity-matched gave aHR 0.76 (0.71–0.82).

**Component dissociation — ELEVATED in pregnancy (vascular/cardiac):**

| PASC component | Rate pregnant | Rate non-pregnant | aHR (95% CI) | p-corrected |
|---|---|---|---|---|
| Abnormal heartbeat | 6.16% | 4.40% | **1.67 (1.43–1.94)** | <0.001 |
| Thromboembolism | 0.50% | 0.35% | **1.88 (1.17–3.04)** | 0.003 |
| Abdominal pain | 9.41% | 8.96% | 1.34 (1.16–1.55) | <0.001 |

**Component dissociation — REDUCED in pregnancy (cognitive/fatigue/systemic):**

| PASC component | Rate pregnant | Rate non-pregnant | aHR (95% CI) | p-corrected |
|---|---|---|---|---|
| Malaise and fatigue | 1.41% | 4.68% | **0.35 (0.27–0.47)** | <0.001 |
| Cognitive problems | 0.80% | 2.46% | **0.39 (0.27–0.56)** | <0.001 |
| Acute pharyngitis | 1.46% | 5.06% | 0.36 (0.26–0.48) | <0.001 |
| Hair loss | 0.49% | 1.54% | 0.35 (0.22–0.58) | <0.001 |
| Dyspnea | 4.15% | 8.80% | 0.55 (0.45–0.66) | <0.001 |
| Sleep disorders | 1.00% | 2.47% | 0.53 (0.39–0.74) | <0.001 |
| Encephalopathy | 0.21% | 0.71% | 0.41 (0.20–0.85) | 0.002 |

**Authors' mechanistic interpretation:** The pregnancy immune tolerant state (altered cytokine/complement/T-cell regulation, uterine-placental immune adaptations) may downregulate the robust inflammatory response that drives fatigue, cognitive, and mucosal PASC components, while the prothrombotic physiology of pregnancy independently elevates the thromboinflammatory signal.

## Relevance

This paper is the principal empirical anchor for `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` in a pregnancy context.

It functions as a **natural experiment** within h0005's framework: pregnancy is a physiologically constrained immune state with suppressed Th1/autoimmune tone and elevated prothrombotic physiology, allowing partial dissection of PAIS mechanism classes.

**Why this matters for the h0005 mechanism-dissector role:**
- The *overall protective effect* (aHR 0.85) is consistent with pregnancy's immune tolerant state suppressing immunopathological PASC.
- The *component dissociation* — fatigue/cognitive markedly reduced while cardiac/vascular elevated — is consistent with a model where immune-mediated/inflammatory Th1-class mechanisms drive the fatigue/cognitive component and thromboinflammatory mechanisms drive the vascular/cardiac component, and these two subclasses respond differently to the pregnancy immune environment.
- This supports `proposition:0007-vascular-autonomic-pathways-contribute-to-the-stage-pais-link` within h0005: vascular/autonomic pathways may be at least partly mechanistically distinct from classical adaptive/autoimmune ones.

**Cross-hypothesis links:**
- `hypothesis:0001-shared-dysregulated-attractor`: the dissociation suggests that "PASC" as a unified phenotype may be a mixture of mechanistically distinct pathways that can be selectively modulated — consistent with a heterogeneous attractor state.
- `hypothesis:0003-immune-exhaustion-feedback`: reduced cognitive/fatigue burden in the immune-tolerant pregnant state is directionally consistent with an immunopathological driver.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Pregnancy immune tolerance (cytokine/T-cell/complement alterations) | Immune homeostatic margin / Th1-tone modifier | Natural experiment reducing systemic inflammatory PAIS risk |
| Overall PASC incidence reduction (aHR 0.85) | Acute-phase immune milieu → attractor entry probability | Consistent with immune-mediated attractor entry hypothesis |
| Fatigue/cognitive component reduction | Neuroinflammatory / Th1 PAIS subtype | Selectively suppressed in immune-tolerant state |
| Thromboembolism/cardiac component elevation | Thrombovascular PAIS subtype | Partially or largely pregnancy-physiology-driven; mechanistically distinct |
| Computable PASC phenotype | EHR-derived PASC case definition | 24-component ICD-10-based phenotype; different from symptom-based questionnaires |
| No gestational-week stratification | Missing covariate: immune state changes across trimesters | Cannot determine which immune-stage of pregnancy drives the effect |

## Limitations

**Design constraints:**
- Retrospective EHR study; outcome ascertainment entirely via ICD-10 codes, which risks misclassification and systematic under-ascertainment — especially for subjective symptoms (fatigue, cognitive problems) that may not generate distinct billing codes.
- PASC computable phenotype was derived in the non-pregnant adult population; its performance characteristics in pregnant/postpartum individuals are unknown.

**Critical ascertainment caveat — the key competing explanation:** Pregnant and postpartum individuals routinely attribute fatigue, cognitive symptoms ("pregnancy brain"), and malaise to normal gestational physiology, pregnancy complications, or early postpartum recovery. These symptoms may generate fewer EHR encounters and ICD-10 codes in the pregnant group relative to the non-pregnant comparator, even if the underlying pathology is equally present. This competing explanation — differential symptom attribution and care-seeking, not a true biological reduction — cannot be distinguished from a true protective biological effect using EHR data alone. This caveat applies most forcefully to exactly the components showing the largest reductions (malaise/fatigue, cognitive problems), and substantially limits the inferential strength for the mechanism-dissector role.

**Missing stratifications:**
- No gestational-week (trimester) stratification. Immune changes across pregnancy are not uniform — first trimester is pro-inflammatory, late second/third trimester is immune-tolerant, and early postpartum involves immune rebound. The median infection at 34 weeks means most infections occurred in the immune-tolerant late-pregnancy window, but variation is large (IQR 25–38 weeks) and not analyzed.
- No postpartum-day stratification. PASC observed in the 30–180 day window for third-trimester infections would occur partly or entirely in the postpartum period (immune rebound phase), further complicating interpretation.
- Insufficient N for sub-analyses by SARS-CoV-2 variant (Alpha/Delta/Omicron), vaccination status, or COVID-19 severity subgroup.

**Population constraints:**
- Excludes pregnancies <20 weeks' gestation and non-live-birth outcomes; findings are not generalizable to early-pregnancy or miscarriage populations.
- EHR-based cohort captures only individuals seeking care; untested/home-tested infections are excluded, potentially biasing toward more symptomatic individuals.
- Residual confounding possible despite IPTW; large baseline differences in comorbidities and vaccination before weighting suggest important pre-existing health differences between groups.

**Interpretation of elevated vascular/cardiac risk:** The increased thromboembolism risk (aHR 1.88) in pregnancy reflects baseline pregnancy physiology (prothrombotic state, venous stasis) more than COVID-specific PASC; the sensitivity analysis excluding VTE barely changes the overall aHR (0.85 → 0.84), confirming the thromboembolism signal is a minor overall driver. Whether the elevated abnormal heartbeat (aHR 1.67) reflects true cardiac PASC or normal pregnancy-related arrhythmia burden (physiologic tachycardia, palpitations) cannot be determined from ICD-10 codes alone.

## Model / Tool Availability

No model, tool, or dataset was released. RECOVER PCORnet EHR data are governed by contributing health system data-sharing agreements; requests can be made through the RECOVER research programme.

## Follow-up

- Prospective confirmation from the RECOVER Pregnancy Cohort (enrolling at time of publication) with symptom-based instruments would help distinguish true biological protection from ascertainment/attribution bias.
- Trimester-stratified analyses with matched gestational and postpartum windows would test whether late-pregnancy immune tolerance drives the effect or whether postpartum immune rebound attenuates it.
- Comparison of ICD-10 code-based PASC ascertainment rates with patient-reported symptom survey data in the same pregnant/postpartum cohort is needed to quantify the differential attribution bias.
- The component dissociation (vascular preserved, fatigue/cognitive reduced) motivates formal mechanistic studies testing whether immune-tolerant states in general (not only pregnancy) selectively modulate fatigue/cognitive versus thrombovascular PASC components.
- Cross-reference with `topic:long-covid-immune-dysregulation` and `topic:menopause-sex-hormones-and-pais-risk` for broader reproductive-immune context.
