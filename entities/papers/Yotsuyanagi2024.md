---
id: paper:Yotsuyanagi2024
type: paper
title: 'Prevention of post COVID-19 condition by early treatment with ensitrelvir in
  the phase 3 SCORPIO-SR trial'
status: active
ontology_terms:
  - ensitrelvir
  - 3C-like protease inhibitor
  - post-COVID-19 condition
  - prevention
  - antiviral therapy
  - randomized controlled trial
  - post-acute infection syndrome
  - SCORPIO-SR
dataset_usage: []
datasets: []
source_refs:
- cite:Yotsuyanagi2024
related:
- topic:antigen-pathogen-persistence
- topic:biomarkers-and-objective-endpoints
created: '2026-06-20'
updated: '2026-06-20'
---
# Prevention of post COVID-19 condition by early treatment with ensitrelvir in the phase 3 SCORPIO-SR trial

- **Authors:** Hiroshi Yotsuyanagi, Norio Ohmagari, Yohei Doi, Masaya Yamato, Akimasa Fukushi, Takumi Imamura, Hiroki Sakaguchi, Takuhiro Sonoyama, Takao Sanaki, Genki Ichihashi, Yuko Tsuge, Takeki Uehara, Hiroshi Mukae
- **Year:** 2024
- **Journal:** Antiviral Research
- **DOI:** 10.1016/j.antiviral.2024.105958
- **PMID:** 38972603
- **BibTeX key:** Yotsuyanagi2024
- **Source:** Europe PMC abstract (full text blocked_but_oa; abstract via paper-fetch)
- **Note:** Pre-specified exploratory analysis of post-COVID-19 condition (PCC) prevention, nested in the double-blind phase-3 SCORPIO-SR RCT. Sponsored by Shionogi.

## Key Contribution

This is a pre-specified exploratory analysis of the double-blind phase-3 SCORPIO-SR trial that assessed whether early oral ensitrelvir — a 3C-like protease (3CLpro) inhibitor — reduces the risk of post COVID-19 condition (PCC/PASC). In patients with mild-to-moderate COVID-19 treated within 120 hours of symptom onset, the 125-mg ensitrelvir arm showed nominally lower risk of persistent PCC symptoms at days 85, 169, and 337 compared with placebo, though confidence intervals crossed the null at all time points. This is one of the few randomised controlled data sources for antiviral-based PAIS prevention and complements nirmatrelvir/ritonavir (Geng2024, STOP-PASC) by targeting prevention rather than treatment of established PASC.

## Methods

**Design:** Double-blind, placebo-controlled, three-arm phase-3 RCT (SCORPIO-SR; trial ID jRCT2031210350). The PCC analysis is a pre-specified exploratory endpoint nested within the acute-treatment efficacy trial.

**Population:** Adults with mild-to-moderate COVID-19. Mean age 35.6–36.5 years; 53–58% male. Predominantly younger, ambulatory Japanese patients [UNVERIFIED — Japan-only enrolment inferred from trial registration context].

**Interventions:**
- Ensitrelvir 125 mg once daily (375 mg loading dose on day 1) for 5 days
- Ensitrelvir 250 mg once daily (750 mg loading dose on day 1) for 5 days
- Matching placebo for 5 days
- Randomised 1:1:1 within 120 hours of symptom onset

**Analysed N:** 341 (125 mg), 317 (250 mg), and 333 (placebo)

**PCC endpoint:** Self-administered questionnaire covering 14 acute-phase COVID-19 symptoms (including 4 neurological items). PCC was defined as at least one mild, moderate, or severe symptom with general health not returning to the usual level. Assessed at days 85, 169, and 337.

**Statistical approach:** Risk reduction (percentage) with 95% confidence intervals versus placebo [UNVERIFIED — exact statistical model not specified in abstract; likely logistic or Poisson regression].

## Key Findings

**Primary PCC outcome (any of 14 symptoms):**

| Timepoint | 125-mg risk reduction vs placebo | 250-mg risk reduction vs placebo |
|---|---|---|
| Day 85 | 32.7% (95% CI: −30.6, 66.1) | 10.9% (95% CI: −67.0, 52.8) |
| Day 169 | 21.5% (95% CI: −37.3, 55.6) | 9.5% (95% CI: −56.6, 48.0) |
| Day 337 | 24.6% (95% CI: −43.7, 60.9) | 30.6% (95% CI: −36.2, 65.5) |

All confidence intervals include zero — no endpoint reached formal statistical significance. The 125-mg dose showed consistently larger point estimates than 250 mg across all timepoints, which is an unusual dose-response pattern and warrants caution.

**Neurological symptom subgroup:** Risk reductions were observed specifically for the subset of 4 neurological PCC symptoms, though the magnitude and precision are not quoted in the abstract [INACCESSIBLE — full subgroup table requires full text].

**Effect modification:** More pronounced risk reductions were observed among:
- Patients with high acute-phase symptom scores at baseline (more severe acute illness)
- Patients with baseline BMI ≥ 25 kg/m²

**Absolute risk rates:** Not available from the abstract [INACCESSIBLE].

**Adverse events / safety:** Not reported in the abstract [INACCESSIBLE].

## Relevance

This trial directly addresses `question:0012` — whether early antiviral treatment of acute COVID-19 reduces PAIS incidence. It provides the first randomised evidence from a phase-3 trial for a 3CLpro inhibitor (ensitrelvir) on PCC prevention, complementing observational and retrospective data for nirmatrelvir/ritonavir.

Connection to `hypothesis:0001` (antigen/pathogen persistence as upstream driver of PAIS): If early viral replication suppression during the acute phase lowers PAIS risk, this is consistent with a model in which viral antigen burden or viral-driven immune damage during the acute window causally seeds the post-acute syndrome. The trend toward greater effect in patients with high acute symptom scores further supports the idea that the acute insult magnitude matters.

Comparison with Geng2024 (STOP-PASC): Geng2024 tests nirmatrelvir/ritonavir in patients who already have established PASC (treatment, not prevention). Yotsuyanagi2024 tests ensitrelvir given at the moment of acute infection (prevention). Together they ask: (a) does reducing acute viral burden prevent PAIS, and (b) does late antiviral suppress a viral reservoir sustaining established PAIS? These are distinct mechanistic hypotheses, and a positive on (a) with a null on (b) would favour an "initial hit" model over a persistent-reservoir model.

The neurological-symptom subgroup finding is particularly relevant to dysautonomia and cognitive-symptom hypotheses (brain-fog, SFN), though the data here are exploratory.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Post COVID-19 condition (PCC) | PAIS | PCC is the WHO-defined label for long COVID; maps directly |
| 14-symptom questionnaire endpoint | Patient-reported PCC phenotype | Self-report; no biomarker or objective endpoint used |
| 4 neurological symptoms | Neurological PAIS subphenotype (dysautonomia, cognitive) | Subgroup suggests neurological symptoms may be more responsive to acute antiviral |
| Acute symptom severity (high vs low) | Acute-severity threshold hypothesis | Effect modification by baseline severity is consistent with `hypothesis:0003` |
| 3CLpro inhibition (ensitrelvir) | Antiviral replication suppression | Same mechanistic class as nirmatrelvir; different PK profile |
| 5-day acute treatment within 120 h | Acute-phase intervention window | Window aligns with peak viral replication; tests early-insult causal model |

## Limitations

1. **Exploratory, not confirmatory.** PCC was a pre-specified exploratory endpoint, not a primary endpoint. The trial was powered for acute-phase outcomes; it is underpowered for PCC. All confidence intervals include zero.

2. **Short treatment window, young population.** Mean age ~36; predominantly mild-to-moderate disease. Effect size and generalisability to older, sicker, or immunocompromised patients (who have higher PAIS risk) are unknown.

3. **Self-report endpoint only.** PCC defined by self-administered symptom questionnaire with no biomarker, functional, or objective measurement. Susceptible to recall bias and differential placebo unblinding.

4. **Non-monotonic dose-response.** The 125-mg arm consistently showed larger point-estimate reductions than the 250-mg arm. This may reflect statistical noise in an underpowered subgroup analysis, pharmacokinetic differences, or dose-dependent adverse effects reducing compliance [UNVERIFIED — full-text tables needed to adjudicate].

5. **Single-country RCT.** Inferred enrolment in Japan [UNVERIFIED]; a largely East Asian, younger, predominately male cohort may not generalise to other populations where PAIS disproportionately affects women.

6. **No pre-specified symptom clusters.** The 14-symptom composite outcome pools heterogeneous PCC manifestations; clustering or dimensional analyses that might reveal differential antiviral benefit for fatigue vs cognitive vs autonomic subtypes are not reported in the abstract.

7. **COVID-19 variant era not specified in abstract.** The variant circulating during enrolment affects both acute severity and PCC rates [INACCESSIBLE — requires full text].

8. **No Kaplan-Meier time-to-resolution curves.** Risk reduction at discrete snapshots (days 85/169/337) may miss dynamic patterns or initial benefit that erodes over time.

## Model / Tool Availability

None. This is a clinical RCT report; no computational models, tools, or publicly deposited datasets are described.

## Follow-up

- Read full text for: absolute risk rates, safety data, precise neurological subgroup results, variant era, enrolment geography, and the statistical model specification.
- Compare with Geng2024 (STOP-PASC): prevention (Yotsuyanagi) vs treatment of established PASC (Geng) — together they bound the "acute insult" vs "persistent reservoir" debate.
- Consider updating `question:0012` frontmatter to add `cite:Yotsuyanagi2024` to `source_refs`.
- The non-monotonic dose-response (125 mg > 250 mg) is unexplained and warrants follow-up — could reflect PK differences (e.g. ensitrelvir CNS penetration varies by dose) or random variation in an underpowered subgroup.
- Effect modification by BMI ≥ 25 and high baseline severity aligns with `hypothesis:0003` (acute severity threshold); worth noting in that hypothesis file.
