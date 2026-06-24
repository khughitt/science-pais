---
id: paper:Novak2026
type: paper
title: 'Shared autonomic phenotype of long COVID and myalgic encephalomyelitis/chronic
  fatigue syndrome'
status: active
ontology_terms:
- small fiber neuropathy
- long COVID
- myalgic encephalomyelitis/chronic fatigue syndrome
- hypermobile Ehlers-Danlos syndrome
- dysautonomia
- autonomic failure
- cerebral blood flow velocity
- POTS
- epidermal nerve fiber density
- sweat gland nerve fiber density
- QASAT
- skin biopsy
- transcranial Doppler
- post-acute infection syndrome
- cross-trigger convergence
dataset_usage: []
datasets: []
source_refs:
- cite:Novak2026
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0004-convergent-small-fiber-neuropathy-substrate
- topic:post-infectious-dysautonomia-and-autoimmunity
- topic:measurement-ascertainment-artifacts-in-pais
created: '2026-06-24'
updated: '2026-06-24'
---
# Shared autonomic phenotype of long COVID and myalgic encephalomyelitis/chronic fatigue syndrome

- **Authors:** Peter Novak, David M. Systrom, Alexandra Witte, Sadie P. Marciano, Donna Felsenstein, Jeff M. Milunsky, Aubrey Milunsky, Joel Krier, Mark C. Fishman
- **Year:** 2026
- **Journal:** PLOS One
- **DOI:** [10.1371/journal.pone.0341278](https://doi.org/10.1371/journal.pone.0341278)
- **PMCID:** PMC12829881
- **BibTeX key:** Novak2026
- **Tier:** Core — largest single-center comparative autonomic phenotyping study of long COVID and ME/CFS to date
- **Source:** Europe PMC full text (XML, OA CC BY)

## Key Contribution

The largest single-center comparative study of autonomic and peripheral-nerve phenotyping in long COVID (n = 143), ME/CFS (n = 170), hypermobile Ehlers-Danlos syndrome (hEDS, n = 290), and healthy controls (n = 73). Using comprehensive autonomic testing plus paired proximal (thigh) and distal (calf) skin biopsies graded by the age/sex-adjusted QASAT scale, the study demonstrates that long COVID and ME/CFS share near-identical rates of widespread autonomic failure, reduced orthostatic cerebral blood flow velocity (CBFv), and small fiber neuropathy (SFN) — with statistically indistinguishable autonomic profiles across most domains. The inclusion of hEDS as a non-infectious dysautonomia comparator establishes that SFN and autonomic failure are not exclusive to post-infectious triggers: hEDS patients showed comparable or greater SFN rates (63.3% biopsy / 81.1% combined) than either PAIS group, with more pronounced peripheral neurodegeneration by sudomotor metrics. This challenges the assumption that SFN in PAIS is pathophysiologically distinct from SFN in other dysautonomia syndromes.

The paper is an important cross-trigger reference for `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` (P1 structural lesion, P4 cross-trigger convergence) but does not formally classify per-patient length-dependent vs. non-length-dependent SFN, limiting its contribution to P2 (non-length-dependent pattern claim). It was screened as a candidate vehicle for `pre-registration:0003` but is inadmissible (fails G2: hEDS is a contaminated non-infectious comparator arm; no clean primary-dysautonomia-only control group), so it serves as supporting evidence for P1/P4, not a promotion vehicle.

## Methods

**Design:** Retrospective, single-center consecutive-cohort study. Patients with long COVID, ME/CFS, and hEDS who completed autonomic testing at the Brigham and Women's Faulkner Hospital Autonomic Laboratory, Boston, between January 2018 and December 2023. Data accessed May 2023 and January 2025.

**Groups and N:**
- Long COVID: n = 143 (from 166 referred; 23 excluded for incomplete data)
- ME/CFS: n = 170 (from 203 referred; 33 excluded)
- hEDS: n = 290 (from 352 referred; 62 excluded)
- Healthy controls: n = 73 (historical; from a University of Massachusetts autonomic research database)

**Case definitions:**
- *Long COVID:* Confirmed SARS-CoV-2 (PCR or antigen positive) plus persistent/relapsing symptoms (brain fog, fatigue, smell/taste changes, post-exertional malaise, palpitations, dizziness, gastrointestinal symptoms). Cohort spans pre-Delta, Delta, and Omicron eras; variant sub-analyses were not performed due to small pre-Omicron numbers.
- *ME/CFS:* Myalgic Encephalomyelitis International Consensus Criteria (ME-ICC) or National Academy of Medicine (NAM/IOM 2015) criteria. **Crucially, infectious onset was not required** — the ME/CFS cohort is not restricted to post-infectious cases; any ME/CFS meeting those criteria was included.
- *hEDS:* Beighton-Villefranche (pre-2017) or 2017 International Criteria; all diagnoses made by genetic specialists. hEDS patients with concurrent chronic fatigue or ME/CFS diagnosis were excluded.
- *Healthy controls:* Asymptomatic, normal tilt, normal CBFv and respiratory responses.

**Autonomic testing battery (all groups):**
- Valsalva maneuver (sympathetic adrenergic index: end-of-phase-2 BP decline)
- Deep breathing test (parasympathetic cardiovagal index: heart rate variation)
- 10-minute 70° head-up tilt test
- Transcranial Doppler monitoring of middle cerebral artery CBFv (indirect; M1 segment, temporal window, 2 MHz probe stabilized with 3D holder)
- Capnography (end-tidal CO2) during tilt
- Electrochemical skin conductance (ESC) for sudomotor function (proxy for sweat gland nerve fiber loss)

**Skin biopsies:**
- **Paired sites:** proximal thigh (20 cm distal to iliac spine) + calf (10 cm above lateral malleolus)
- 3-mm circular punch; immunoperoxidase staining for axonal marker PGP9.5 (Therapath, New York)
- Outputs: epidermal nerve fiber density (ENFD, fibers/mm) and sweat gland nerve fiber density (SGNFD, % of grid) at each site

**Grading instrument — QASAT (not a strict ≤5th-percentile IENFD cutoff):**
The study uses the Quantitative Scale for Grading of Cardiovascular Autonomic Reflex Tests and Small Fibers from Skin Biopsies (QASAT). QASAT applies age- and sex-adjusted normative values; ENFD or SGNFD scores >0 indicate abnormality regardless of whether values fall below the conventional 5th-percentile IENFD threshold. This is a different and generally more sensitive metric than a strict 5th-percentile IENFD cutoff. **The SFN prevalence figures in this paper are therefore not directly comparable to studies using a strict ≤5th-percentile cutoff** — this is a key methodological caveat when integrating these prevalence estimates with other literature.

**SFN subtypes assessed:** sensory (abnormal ENFD only), autonomic (abnormal SGNFD only), mixed (both abnormal), functional (abnormal ESC), combined morphological+functional (any of ENFD, SGNFD, or ESC abnormal).

**Additional assessments:**
- Invasive cardiopulmonary exercise testing (iCPET, subset only: LC n = 25, ME/CFS n = 66): Fick cardiac output, right atrial pressure, preload failure, deconditioning
- Patient-reported outcomes: Survey of Autonomic Symptoms (SAS), Neuropathy Total Symptom Score-6 (NTSS-6), numerical pain scale, Central Sensitization Inventory (CSI)
- Laboratory panel (subset, ordered at physician discretion): hs-CRP, TNF-α, IL-6, IL-10, IL-1β, leptin, TS-HDS and FGFR3 antibodies, acetylcholine and ganglionic receptor antibodies, VGKC and P/Q calcium channel antibodies, norepinephrine (supine and standing), growth hormone, myoglobin, systemic immune-inflammation index

**Statistics:** Kruskal-Wallis (continuous), chi-squared (categorical), Dunn post-hoc with Benjamini-Hochberg correction; linear mixed-effects models for tilt time-course (adjusted for supine baseline, with age and sex covariates); Fisher's Exact with Holm correction for pairwise categorical comparisons. Missing data sensitivity analysis via complete-case vs. mean/median imputation. Power analysis for primary QASAT outcome: minimum n = 37 per group at 80% power, α = 0.05.

**Funding:** Mona Taliaferro/Bay Shore Recycling; NHLBI (1OT2HL156812-01); FBRI LLC.

## Key Findings

### Demographics

All groups were predominantly younger women. Mean symptom duration differed substantially: long COVID 1.89 years (SD 0.89) vs. ME/CFS 10.22 years (SD 8.68) — a major chronicity confound (see Limitations). hEDS patients were younger (mean 35.7 years) and had higher female representation (94.5%) than the PAIS groups (~72–79% female).

### Autonomic testing (QASAT — abnormal = score > 0)

| Domain | Controls | Long COVID | ME/CFS | hEDS | LC vs ME/CFS p |
|---|---|---|---|---|---|
| Reduced orthostatic CBFv | 0% | 91.6% | 87.6% | 80.0% | 0.274 (ns) |
| Autonomic failure (overall) | 0% | 95.1% | 88.8% | 89.0% | 0.144 (ns) |
| Cardiovagal failure | 0% | 37.1% | 34.1% | 34.8% | 0.999 (ns) |
| Adrenergic failure | 0% | 74.8% | 68.2% | 68.3% | 0.539 (ns) |
| Sudomotor failure | 0% | 77.3% | 72.0% | 56.6% | 0.299 (ns) |
| POTS | 0% | 22.4% | 19.4% | 32.4% | 0.577 (ns) |
| Neurogenic orthostatic hypotension | 0% | 14.7% | 14.7% | 9.7% | 0.999 (ns) |
| HYCH (hypocapnic cerebral hypoperfusion) | 0% | 23.8% | 21.8% | 21.0% | 0.999 (ns) |
| OCHOS | 0% | 25.9% | 31.8% | 17.6% | 0.264 (ns) |

Long COVID showed numerically worse autonomic profiles in most domains and a significantly greater decline in orthostatic end-tidal CO2 (−24% vs. −19% for ME/CFS; p = 0.016), reflecting more prominent hypocapnia. Sudomotor failure was significantly worse in both PAIS groups compared to hEDS (p = 0.003 and p < 0.001).

Maximal orthostatic CBFv decline: long COVID −25.0% (SD 11.1) vs. ME/CFS −22.2% (SD 10.5); both groups exceeded the 19% threshold associated with CNS dysfunction symptoms (p = 0.370 ns for group difference).

### Skin biopsy (QASAT-graded SFN)

**ENFD abnormality (QASAT > 0):**
- Long COVID: 48.3%
- ME/CFS: 33.5%
- hEDS: 53.1%
- Controls: 0%
- LC vs. ME/CFS: p = 0.021 (significant — LC higher)
- ME/CFS vs. hEDS: p < 0.001 (hEDS higher than ME/CFS)
- LC vs. hEDS: p = 0.359 (ns)

**SGNFD abnormality (QASAT > 0):**
- Long COVID: 27.8%
- ME/CFS: 28.8%
- hEDS: 32.2%
- Controls: 0%
- LC vs. ME/CFS: p = 0.999 (ns)
- All pairwise: p = 0.999 (ns across all three patient groups)

**SFN — biopsy-confirmed (abnormal ENFD or SGNFD by QASAT):**
- Long COVID: 67.2%
- ME/CFS: 52.6%
- hEDS: 63.3%
- Controls: 0%
- LC vs. ME/CFS: p = 0.044 (significant)
- ME/CFS vs. hEDS: p = 0.079 (ns trend)
- LC vs. hEDS: p = 0.499 (ns)

**SFN — combined (any of ENFD, SGNFD, or ESC abnormal):**
- Long COVID: 91.4%
- ME/CFS: 82.9%
- hEDS: 81.1%
- Controls: 0%
- LC vs. ME/CFS: p = 0.080 (ns trend)
- LC vs. hEDS: p = 0.020 (significant)

**Mixed SFN (both ENFD and SGNFD abnormal):** LC 11.9% vs. ME/CFS 10.8% vs. hEDS 23.0%; hEDS was significantly higher than both PAIS groups (p = 0.007 vs. ME/CFS; p = 0.019 vs. LC), reflecting more severe/extensive SFN.

**Raw ENFD and SGNFD densities (mean ± SD):**
- ENFD proximal thigh (fibers/mm): Controls 13.44 (3.57), LC 11.86 (4.55), ME/CFS 12.78 (4.61), hEDS 12.07 (4.53) — overall p = 0.033; ME/CFS > LC (p = 0.208 ns pairwise)
- ENFD calf (fibers/mm): Controls 10.15 (2.25), LC 7.94 (3.46), ME/CFS 8.79 (3.55), hEDS 8.20 (4.00) — overall p < 0.001; ME/CFS > LC (p = 0.043)
- SGNFD proximal thigh (% of grid): Controls 57.72 (9.98), LC 55.87 (14.84), ME/CFS 59.27 (17.44), hEDS 52.75 (16.63) — overall p = 0.009; ME/CFS > hEDS (p = 0.049)
- SGNFD calf (% of grid): Controls 49.08 (10.59), LC 49.09 (17.12), ME/CFS 49.00 (17.34), hEDS 45.91 (19.54) — overall p = 0.381 (ns)

**Key observation on proximal vs. distal ENFD and SGNFD:** The raw group-mean density values show SGNFD at the proximal thigh (55–59% of grid across PAIS groups) was notably higher than SGNFD at the calf (45–49%), opposite to the pattern expected in length-dependent dying-back neuropathy where distal should be more depleted. However, **the paper does not perform formal per-patient classification of length-dependent vs. non-length-dependent SFN**; no NLD fraction is reported. Inference about non-length-dependence from group-level raw densities must be made with caution — see Limitations.

### Invasive CPET (iCPET, subset)

Preload failure: 96% (LC) vs. 92.4% (ME/CFS) — p = 0.542 (ns). Deconditioning (peak VO2 < 85% predicted): 64% in both groups. After BMI adjustment, cardiac output was not significantly different. Mitochondrial myopathy pattern (CaO2–CvO2/Hb < 0.8): 20% LC vs. 41.5% ME/CFS — p = 0.096 (ns trend; note very small LC subset n = 25 vs. ME/CFS n = 66).

### Central sensitization

Central sensitization syndrome by CSI ≥ 40: 78.1% LC, 85.4% ME/CFS, 92.4% hEDS. No significant difference between LC and ME/CFS (p = 0.410).

### Laboratory findings

No significant between-group differences between long COVID and ME/CFS in hs-CRP, IL-6, IL-1β, TNF-α, or hormonal markers (cortisol, growth hormone, ACTH). Leptin levels trended higher in LC (p = 0.029 overall) but pairwise comparisons were non-significant. No differences in norepinephrine (supine or standing), TS-HDS, FGFR3 antibodies, acetylcholine receptor antibodies, VGKC, or P/Q calcium channel antibodies. Overall: laboratory tests did not distinguish between conditions.

### hEDS comparison

hEDS patients reported significantly worse autonomic (SAS total 29.7 vs. ~22–23) and neuropathic (NTSS-6 total 11.6 vs. ~9.6) symptoms than both PAIS groups, had worse central sensitization inventory scores, worse pain scores, and were more likely to have mixed SFN (23.0% vs. ~11% in PAIS groups). The sudomotor abnormality rate was significantly lower in hEDS than in either PAIS group. Autonomic failure and POTS were more common in hEDS than ME/CFS (POTS: hEDS 32.4% vs. ME/CFS 19.4%, p = 0.008). The discussion explicitly interprets hEDS as showing "more pronounced peripheral neurodegeneration" than the PAIS groups.

## Relevance

### For `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate`

**P1 (`proposition:0014-pais-small-fiber-structural-lesion-ienfd`):** The study provides the largest biopsy-confirmed SFN prevalence data in both long COVID and ME/CFS to date, using paired proximal + distal biopsies (PGP9.5 immunostaining, Therapath). Biopsy-confirmed SFN: LC 67.2%, ME/CFS 52.6%; combined (including ESC): LC 91.4%, ME/CFS 82.9%. This is strong, large-N corroborating evidence for the structural lesion claim. The referral-center context means these are not population-prevalence estimates, but the absolute n's (LC n = 143, ME/CFS n = 170) substantially exceed prior studies. However, the QASAT grading metric (age/sex-adjusted; score > 0 = abnormal) is more inclusive than a strict ≤5th-percentile IENFD cutoff, which inflates prevalence estimates compared to studies using the conventional cutoff — this must be noted explicitly when citing these numbers.

**P2 (`proposition:0015-pais-sfn-non-length-dependent-pattern`):** The paper provides paired proximal (thigh, 20 cm distal to iliac spine) + distal (calf, 10 cm above lateral malleolus) biopsies with both ENFD and SGNFD, enabling in-principle detection of non-length-dependent patterns. The group-level raw density data suggest SGNFD is higher at the proximal thigh (55.87–59.27% of grid) than at the calf (49.0–49.1% of grid) across PAIS groups — a pattern inconsistent with pure length-dependent dying-back (where distal should be more depleted). ENFD abnormality rates (QASAT) are also higher than SGNFD abnormality rates across groups, further suggesting widespread involvement. **However, the paper does not formally classify individual patients as having length-dependent vs. non-length-dependent SFN, does not report an NLD fraction, and does not explicitly characterize or claim a non-length-dependent pattern.** This is the central methodological gap for P2: the design is *capable* of detecting NLD, and the group-level density data are *suggestive*, but the per-patient NLD claim cannot be derived from this paper as reported. The contribution to P2 is indirect and inference-requiring, not a direct measured claim.

**P4 (`proposition:0017-pais-sfn-cross-trigger-convergence`):** The study demonstrates convergent SFN prevalence across two distinct post-infectious triggers (SARS-CoV-2 for long COVID vs. diverse/unspecified triggers for ME/CFS — noting that the ME/CFS cohort did NOT require documented infectious onset). The fact that hEDS — a non-infectious heritable connective tissue disorder — also shows comparable SFN rates (63.3% biopsy, 81.1% combined) substantially complicates the cross-trigger-PAIS-specific story: the SFN substrate appears to be shared with a broader class of dysautonomia syndromes, not exclusively post-infectious ones. This supports P4 in that it shows SFN convergence, but it weakens any claim that the SFN substrate is specific to post-infectious pathophysiology.

### For `question:0004-convergent-small-fiber-neuropathy-substrate`

This paper is the highest-N study to date directly comparing SFN rates with paired biopsy sites across two PAIS groups (long COVID and ME/CFS) and a non-infectious dysautonomia control (hEDS). The convergence of biopsy-confirmed SFN rates across groups, combined with indistinguishable SGNFD rates and autonomic profiles, provides evidence for a shared substrate — but the hEDS arm complicates the PAIS-specific interpretation.

### For `topic:post-infectious-dysautonomia-and-autoimmunity`

Despite laboratory assessments including acetylcholine receptor, ganglionic AChR, VGKC, and P/Q calcium channel antibodies, no antibody differences were found between long COVID, ME/CFS, or hEDS. TS-HDS and FGFR3 antibodies were measured but not found to be elevated or differentially distributed. This adds null evidence to the autoantibody-mediated SFN hypothesis for the PAIS groups in this referral cohort — though the study acknowledges the inflammatory/autoimmune tests used may lack sensitivity for low-grade pathology.

### For `topic:measurement-ascertainment-artifacts-in-pais`

Two measurement artifacts deserve explicit flagging for this paper:
1. **QASAT vs. ≤5th-percentile IENFD cutoff:** The QASAT grading (age/sex-adjusted, score > 0 = abnormal) is more inclusive than the strict 5th-percentile IENFD threshold used in most prior SFN literature. The SFN prevalence figures (67% / 53% / 63%) are not directly comparable to studies using the conventional cutoff and likely overestimate prevalence relative to that standard.
2. **Referral-center bias:** All patients were referred for autonomic evaluation at a specialized center, highly enriching for dysautonomia and SFN. Prevalence estimates do not represent the general long COVID or ME/CFS population.

### Pre-registration admissibility (`pre-registration:0003`)

Screened as a candidate vehicle; **inadmissible.** The paper fails G2 (clean primary-dysautonomia control arm): hEDS is a contaminated comparator (connective tissue disorder with systemic effects on nerve and autonomic function, not a "primary dysautonomia only" group). The healthy controls are historical and lack matched laboratory data. The paper is supporting evidence for P1/P4, not a promotion vehicle for `hypothesis:0007`.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Biopsy-confirmed SFN in long COVID 67.2% / ME/CFS 52.6% (QASAT) | `proposition:0014` — IENFD structural lesion | Large-N; QASAT metric inflates vs. 5th-percentile cutoff |
| Paired proximal + distal biopsy; SGNFD higher at thigh than calf | `proposition:0015` — non-length-dependent pattern | Suggestive but NLD fraction not formally reported per patient |
| SFN convergence across SARS-CoV-2 (LC) and diverse-trigger (ME/CFS) PAIS | `proposition:0017` — cross-trigger SFN convergence | ME/CFS did NOT require infectious onset — limits cross-trigger claim |
| hEDS shows comparable or higher SFN and more severe peripheral neurodegeneration | `proposition:0017`; hEDS complicates PAIS-specificity | SFN substrate is not exclusive to post-infectious syndromes |
| No autoantibody or inflammatory marker differences between groups | `proposition:0016` — autoimmune causation | Null evidence from limited antibody panel; insufficient sensitivity not ruled out |
| Indistinguishable autonomic failure profiles (LC ~= ME/CFS) | `hypothesis:0007` shared dysautonomia substrate | Strongest evidence domain in this paper |
| QASAT grading metric vs. ≤5th-percentile IENFD | `topic:measurement-ascertainment-artifacts-in-pais` | Prevalence not comparable to conventional-cutoff studies |
| Referral-center cohort, historical controls | `topic:measurement-ascertainment-artifacts-in-pais` | Prevalence not population-representative |
| ME/CFS without required infectious onset | `topic:mecfs-long-covid-convergence` | Dilutes post-infectious specificity of the ME/CFS arm |

## Limitations

1. **Referral-center bias.** All patients were referred to a specialized autonomic laboratory for orthostatic intolerance evaluation, heavily enriching for dysautonomia and SFN. The SFN prevalence figures (67%, 53%, 63%) are not representative of the general long COVID or ME/CFS population. True unselected population prevalence is unknown.

2. **QASAT metric not equivalent to conventional ≤5th-percentile IENFD cutoff.** The QASAT scoring uses age/sex-adjusted normative values; any score > 0 is counted as abnormal. This is more sensitive (and less specific) than the standard 5th-percentile IENFD threshold used in most published SFN literature. SFN prevalence figures in this paper cannot be directly compared to studies using the conventional threshold — they likely overestimate prevalence relative to that reference standard.

3. **Historical healthy controls without laboratory data.** Controls were drawn from a different institution's autonomic database (University of Massachusetts) and lacked matched laboratory evaluations. Group comparisons of laboratory markers between patients and controls were therefore not possible.

4. **Symptom duration confound (ME/CFS >> long COVID).** ME/CFS patients had a mean disease duration of 10.2 years vs. 1.9 years for long COVID. This chronicity difference could plausibly affect both autonomic test results and neuropathological findings. The authors note that greater deconditioning (expected with longer chronicity) was not observed, and autonomic failure was actually somewhat more severe in the shorter-duration long COVID group, suggesting the chronicity effect is not simply confounding in the expected direction — but it remains an acknowledged limitation.

5. **ME/CFS case definition does not require documented infectious onset.** The ME-ICC and NAM criteria used do not mandate a precipitating infection. The ME/CFS arm therefore includes cases without a documented post-infectious trigger, diluting the cross-trigger post-infectious comparison and complicating framing of ME/CFS here as a "post-infectious" comparator.

6. **No formal per-patient NLD vs. length-dependent SFN classification.** Despite paired proximal + distal biopsies enabling NLD detection in principle, the paper does not report per-patient classification of NLD vs. LD SFN, does not cite an NLD fraction, and does not explicitly characterize the observed pattern as non-length-dependent. Group-level density data are suggestive of proximal involvement, but the per-patient NLD claim cannot be supported directly from this paper as reported.

7. **hEDS as comparator is contaminated for testing PAIS-specific SFN.** The stated rationale for including hEDS is as a "non-infectious dysautonomia control." However, hEDS involves connective tissue pathology that directly affects peripheral nerve and autonomic structure, making it a confounded rather than clean comparison group. The finding that hEDS shows comparable or higher SFN than PAIS groups is important for the field, but it does not serve as a validated primary-dysautonomia-only baseline.

8. **Transcranial Doppler CBFv is an indirect flow measure.** CBFv is proportional to blood flow only if middle cerebral artery diameter is constant during tilt — an assumption validated in one imaging study cited by the authors but not independently confirmed in this cohort.

9. **iCPET subset severely undersized for long COVID (n = 25).** The invasive CPET subset for long COVID is too small for reliable cross-group comparisons; the mitochondrial myopathy trend (20% LC vs. 42% ME/CFS, p = 0.096 ns) is underpowered.

10. **Laboratory evaluations ordered at physician discretion.** Missing data rates for laboratory markers were high and varied across tests. Despite sensitivity analysis (complete case, mean imputation, median imputation), physician-ordered-test heterogeneity limits interpretation of null findings.

11. **No longitudinal follow-up.** Cross-sectional design only; no trajectory data. The authors suggest longitudinal observation to determine if long COVID and ME/CFS converge over time.

12. **No immune mechanism data** (e.g., T/B cell immunophenotyping, autoantibody discovery panels beyond the targeted set). The antibody panel measured is limited to clinically ordered neuropathy-associated antibodies; broad autoantibody discovery approaches were not applied.

## Methodological Note for `hypothesis:0007` Evidence Coding

Key questions for evidence integration:

1. **Biopsy methodology — distal only or paired proximal + distal?**
   Paired (proximal thigh + calf). Both ENFD and SGNFD measured at each site using PGP9.5 immunostaining (Therapath).

2. **Grading metric?**
   QASAT (age/sex-adjusted normative reference), NOT a strict ≤5th-percentile IENFD cutoff. Scores > 0 = abnormal. This is more sensitive than the conventional threshold; prevalence numbers are not directly comparable to studies using the standard cutoff.

3. **Non-length-dependent pattern formally reported?**
   No. Group-level raw SGNFD densities suggest proximal > distal abnormality by gradient (thigh SGNFD > calf SGNFD across all patient groups), and ENFD abnormality rates also exceed SGNFD rates at the group level. But no per-patient NLD fraction is reported, and the paper makes no explicit NLD claim.

4. **ME/CFS case definition — infectious onset required?**
   No. ME-ICC or NAM criteria; infectious onset not required for inclusion.

5. **Autoantibody / autoimmune panel?**
   Targeted clinical panel (acetylcholine receptor binding, ganglionic AChR, VGKC, P/Q calcium channel, TS-HDS, FGFR3). All negative / non-differential. Functional GPCR autoantibodies (β-adrenergic, muscarinic M2/M3) were NOT measured.

6. **Primary dysautonomia control arm for `pre-registration:0003` eligibility?**
   Fails G2. hEDS is a contaminated comparator (connective tissue disorder, not primary dysautonomia only). Inadmissible as a promotion vehicle.

## Model / Tool Availability

No computational models, software tools, or public datasets released. Data sharing subject to Mass General Brigham Data Use Agreement (DUA) requirements; contact IRB@mgb.org or RMDUA@mgb.org for access.

## Follow-up

- The QASAT-graded prevalence figures from this paper (LC 67.2% / ME/CFS 52.6% / hEDS 63.3%) should be tabulated in `question:0004-convergent-small-fiber-neuropathy-substrate` alongside the conventional-cutoff estimates from Oaklander2022, Limongelli2026, Joseph2021, and Joseph2023, with a note on metric non-comparability.
- The finding that hEDS has comparable or higher SFN rates than PAIS groups — and more severe peripheral neurodegeneration (sudomotor domain, mixed SFN) — is the most consequential finding for the PAIS-specificity framing of `hypothesis:0007`. This warrants an update to `topic:post-infectious-dysautonomia-and-autoimmunity` to note that the SFN/dysautonomia substrate is not PAIS-exclusive.
- A per-patient NLD classification study remains the key outstanding methodological gap for P2. The paired-site biopsy data in this cohort (n = 143 LC, n = 170 ME/CFS) would theoretically allow such a re-analysis if raw per-patient ENFD and SGNFD data at both sites were released under a DUA — worth a data access request.
- The ME/CFS arm's lack of required infectious onset means that the cross-trigger convergence claim for P4 is weaker than it appears: a ME/CFS-specific sub-analysis restricted to patients with documented post-infectious onset (if available in the raw data) would substantially strengthen the P4 evidence.
- Longitudinal follow-up of this cohort (whether long COVID patients develop ME/CFS-like chronicity signatures, and whether SFN and autonomic metrics converge) is explicitly flagged by the authors as a priority and would be a key empirical test of the shared-attractor / convergence frame in `hypothesis:0001`.
- The null laboratory findings (no elevated inflammatory or autoimmune markers in either PAIS group) should be reconciled with the positive autoantibody signals in Stein2025 and the β2 AR-AB literature; the antibody panels used in this study differ (neuropathy-associated antibodies vs. functional GPCR autoantibodies) and non-overlapping panels likely explain the discrepancy.
