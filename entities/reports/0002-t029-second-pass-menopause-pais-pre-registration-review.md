---
id: "report:0002-t029-second-pass-menopause-pais-pre-registration-review"
kind: "report"
title: "t029 second-pass review: unreviewed pre-reg surface and second-precedent cross-read"
status: "draft"
source_refs:
  - pre-registration:0001-menopause-pais-total-effect
  - report:0001-bias-audit-menopause-pais-total-effect
  - task:t029
related:
  - task:t028
  - task:t030
  - task:t031
  - task:t032
  - paper:AlcaldeHerraiz2025
  - paper:Silva2024
  - paper:Shahbaz2025
created: "2026-06-20"
updated: "2026-06-21"
---

# t029 second-pass review

## Scope

Second-pass, out-of-author review of the pre-registration surface not covered by the
identification/adjustment-set pass:

- outcome operationalization from t017;
- exposure staging from t020, including surgical and indeterminate strata;
- feasibility and field-basket caveats from t027;
- out-of-corpus second-precedent search for UKB long-COVID feasibility, selection, and
  SHBG/sex-hormone signal.

This report does not re-litigate the ratified Q1-Q4 amendment set. The primary measured
adjustment set remains `{age, smoking}`.

## A. Out-of-author review of un-reviewed pre-reg surface

### Outcome: primary WHO >=90-day questionnaire outcome

**Verdict: primary outcome computable, with item-level G2 confirmation still required.**

The primary Route-A outcome does not rely on the dropped SF-36 functional gate. It is
computable from:

- UKB COVID test linkage field 40100 for PCR-positive index date; and
- the Health and Well-Being questionnaire symptom, duration, and impact item arrays.

The UKB Health and Well-Being questionnaire overview explicitly lists 45 current symptom
items, corresponding duration items, and a duration category of "More than twelve weeks"
for each endorsed symptom. That supports a direct WHO >=90-day symptom persistence
definition. The pre-reg's G2 requirement to confirm the item IDs and WHO-Delphi mapping at
application is appropriate.

**No amendment question on the primary outcome.** It is not silently substituting an SF-36
or HES-coded proxy for the primary definition.

**Amendment question A1: PEM wording is too strong.** t017 and the pre-reg say UKB has no
"PASC-index/PEM instrument" and no "PEM-specific" item. That is only partly true. UKB does
not have the RECOVER PASC index, CPET, or a validated PEM instrument, but the questionnaire
does include a specific "Post-exertional symptom exacerbation" item with duration and
impact fields. The PEM-weighted arm should be described as a **PESE/fatigue-weighted
questionnaire proxy**, sensitivity-only and not RECOVER-equivalent, rather than as lacking
any PEM-specific questionnaire signal.

**Functional gate disposition: acceptable as dropped, but tighten G6.** The SF-36 T<45 gate
is correctly not pre-registered as computable. UKB does have Health and Well-Being
functional-impact items, but no named substitute is locked. If the intended decision is
"drop def-3 for this pre-reg," G6 should say that, rather than leaving "substitute or drop"
as a live post-lock option.

### Exposure: natural, surgical, and indeterminate strata

**Natural-menopause timing is supportable only after explicit surgical/hysterectomy
exclusions.** Field `2724` ("had menopause") plus field `3581` ("age at menopause") can anchor
natural timing only after records with bilateral oophorectomy or hysterectomy-only
menstrual-marker destruction are removed/quarantined. The t020 decision-tree order does
this in principle.

**Amendment question A2: surgical timing is not computable from the t027 basket as written.**
t020 refers to "`2834` + dates" for bilateral oophorectomy before infection, and the
surgical contrast depends on the age-at-surgery gradient. Field `2834` is the bilateral
oophorectomy flag; the age-at-bilateral-oophorectomy field is 3882. t027 does not list
3882. Add `3882` with `[confirm at application]` to any basket that keeps the surgical
exploratory arm or uses surgery timing to exclude pre-infection bilateral oophorectomy.

**Surgical-menopause promotion call:** keep surgical menopause **exploratory /
triangulating only**, not verdict-bearing. The contrast is useful because the pre-vs-post
FMP oophorectomy gradient and HRT attenuation pattern can discriminate a hormone-withdrawal
channel from aging/SES. But surgical indication, oncology treatment, prophylactic genetics,
endometriosis/fibroids/bleeding, and healthcare-access confounding are too large to promote
it above exploratory until benign-indication restriction and HRT stratification are
actually computable and stable.

**Amendment question A3: HRT-active-at-infection is not computable from baseline HRT fields
alone.** Fields `2814`/`3536`/`3546` establish ever-use, start age, and last-use/still-taking
status at baseline assessment, not necessarily use at SARS-CoV-2 infection 10-14 years
later. The HRT-on-at-infection tag and HRT-stratified surgical contrast need either
prescription/GP linkage fields or a downgrade to "baseline HRT status / unknown at
infection."

**Indeterminate and menstrual-marker-destroyed records should not enter the confirmatory
natural-timing exposure via age-band fallback.** Hysterectomy without oophorectomy and
missing/indeterminate FMP can support exploratory projected-stage sensitivity, but they do
not supply age at natural menopause. If the primary confirmatory exposure is age at
menopause / time-since-menopause, these records should be excluded from that primary timing
analysis, not rescued by age-band fallback.

### Feasibility and field-basket caveats

Fields and access caveats that are handled adequately:

- `40100` COVID test records: verified on Showcase.
- Health and Well-Being questionnaire: item-level IDs and WHO mapping correctly gated by
  `[confirm at application]`.
- Category 1307 EBV serology: category exists; exact usable N correctly marked for live
  confirmation.
- GP linkage, vaccination linkage, HLA/PRS: correctly caveated as partial, restricted, or
  confirm-at-application.

Fields/caveats needing correction or explicit confirmation:

- `3882` age at bilateral oophorectomy: missing from t027 basket; required for surgical
  timing and clean pre-infection surgical exclusion.
- HRT active at infection: requires prescription/GP linkage or must be downgraded; baseline
  fields alone are insufficient.
- "IMD" in t017 is named alongside Townsend `189` but no UKB field/derivation is specified.
  Either use Townsend only, or add a field/derivation with `[confirm at application]`.

## B. Out-of-corpus second-precedent cross-read

### Search result

I found UKB long-COVID/PCC studies independent of the **paper** `AlcaldeHerraiz2025` that
partly corroborate the questionnaire feasibility and selection profile, but I did **not**
find an admissible independent UKB precedent that also re-tests the SHBG/sex-hormone signal.

Therefore the corpus-independence finding is **not fully closed**. The null finding is
recorded here: a second precedent exists for UKB Health and Well-Being questionnaire
feasibility and selection, but not for the SHBG/sex-hormone marker story.

### Candidate precedents cross-read

**Wang et al., EBioMedicine 2024, "Refinement of post-COVID condition core symptoms..."**

- Uses UKB Health and Well-Being survey plus linked SARS-CoV-2 surveillance/EHR data.
- Reports 172,303 included participants, 43,395 with PCR-confirmed COVID-19, mean age 68.9,
  57.4% female.
- Corroborates that the UKB questionnaire can support symptom-level PCC phenotyping at
  scale and that UKB PCC analyses are older and response-conditioned.
- Does not test SHBG, testosterone, menopause, HRT, or oestradiol.
- Authorship overlaps the Oxford/Prieto-Alhambra/Xie group and includes Marta
  Alcalde-Herraiz, so this is not a strong author-independent precedent even though it is a
  separate paper.

**Gao et al., JAMA Network Open 2024, "Hospitalization for COVID-19, Other Respiratory
Infections, and Postacute Patient-Reported Symptoms."**

- Uses UKB Health and Well-Being questionnaire symptoms, but the exposure is COVID-19
  hospitalization, not documented community infection.
- Includes 191,710 eligible questionnaire respondents; COVID-hospitalized group n=1,153,
  female n=508 (44.1%) before weighting.
- Useful for selection-profile triangulation: old respondent cohort, hospital-selected
  severe infection, and explicit healthy-UKB limitation.
- Not usable for the pre-reg's effective-n assumption for natal-female, documented-infection,
  WHO >=90-day long COVID because it conditions on hospitalization and reports symptoms
  rather than the pre-reg's case/control infection denominator.
- Does not test SHBG or sex hormones.

**Prieto-Alhambra et al., Research Square 2025 GWAS preprint.**

- Uses UKB Health and Well-Being LC phenotype and reports an LC discovery cohort of 8,469
  participants, 5,768 cases under a >=30-day symptom definition, 4,451 female participants.
- Confirms the same order-of-magnitude questionnaire denominator as AlcaldeHerraiz2025, but
  it is from the same Oxford/Gilead author network and includes Marta Alcalde-Herraiz.
- Does not test SHBG/sex hormones.

### Axis read

**Effective n.** The second-precedent set does not undercut the order-of-magnitude power
assumption for a questionnaire-based UKB analysis. Across separate UKB questionnaire papers,
the infected/respondent base is large, but the exact pre-reg denominator remains definition-
and window-sensitive. AlcaldeHerraiz2025 remains the only source found that directly
provides the relevant 90-day sensitivity and SHBG-linked LC template.

**Selection profile.** The second-precedent set corroborates, rather than contradicts, the
audit's selection warnings: UKB Health and Well-Being analyses are old, healthier-volunteer,
survival-to-2020, and questionnaire-response conditioned. Hospital/EHR phenotypes are more
severe and collider-prone than the questionnaire route.

**SHBG / sex-hormone signal.** No admissible independent UKB long-COVID precedent was found
that tests SHBG, testosterone, menopause status, HRT, or oestradiol against LC/PCC. The
SHBG-protection story remains single-source and should stay labelled as such.

## Closure decision

- **Author-independence finding:** closed for the unreviewed surface by this report, with
  amendment questions A1-A3 recorded rather than silently edited into locked criteria.
- **Corpus-independence finding:** partially addressed but **not closed for SHBG/sex-hormone
  coverage**. The G2 out-of-corpus gate should remain open unless the team accepts a
  non-SHBG second precedent as sufficient for feasibility only. The pre-reg's standing
  `inconclusive-for-coverage` verdict remains appropriate until live field confirmation and
  either an independent SHBG/sex-hormone precedent or a recorded decision to downgrade the
  SHBG prior to single-source background.

## Addendum (2026-06-21, t032): non-UKB out-of-corpus search

Section B above was deliberately **UKB-scoped** (it asked whether an *independent UKB* precedent re-tests the SHBG/sex-hormone signal, and found none). Task **t032** carries the complementary **non-UKB** out-of-corpus action: find any author-independent, non-UK-Biobank cohort linking SHBG or a measured sex hormone to the long-COVID phenotype, which would upgrade the prior off single-source. Result of that search:

**Two independent, non-UKB, author-independent clinical cohorts corroborate a gonadal-steroid → long-COVID association in the protective direction:**

- **`paper:Silva2024`** — Mount Sinai–Yale "MY-LC" cohort (Iwasaki lab), cross-sectional n≈165. Females with LC have **lower testosterone** than control females; **testosterone is associated with lower symptom burden across both sexes** (after accounting for testosterone, sex ceased to predict symptom burden). Measures gonadal steroids, not SHBG.
- **`paper:Shahbaz2025`** — University of Alberta LC/ME-CFS cohort (Shahbaz/Elahi), case-control n=140, CCC ME/CFS, ~12 mo post-infection. **Reduced testosterone in female LC, reduced estradiol in male LC**; testosterone inversely correlated with inflammatory cytokines. Measures gonadal steroids, not SHBG.

**Disposition (updates the Section B "single-source" labelling, does not change any locked criterion):**

1. **SHBG *measure* remains SINGLE-SOURCE.** No independent non-UKB cohort tests SHBG against long COVID with a positive result. (Szczerbiński 2023, Poland, *did* measure SHBG but reported no SHBG–outcome association and used a hospitalized-survivor exposure, not a validated long-COVID case definition — so it does not upgrade the SHBG prior.) The recorded decision to **downgrade the SHBG prior to single-source background** (pre-reg:0001 amendment 2 / t032) therefore **stands**.
2. **The broader sex-hormone-protection mechanism class is no longer single-source.** Silva2024 + Shahbaz2025 are two mutually-independent, non-UKB corroborations of low non-dominant gonadal steroid in long COVID — softening the single-source label **for the gonadal-steroid (M1-confirm-side, mediator-specific) prior**, not for the SHBG measure and not for the primary total effect.
3. **No change to the primary estimand.** Both are clinical-cohort grade, cross-sectional/case-control, with unresolved **reverse causation** (LC may suppress the HPG axis rather than low hormone predisposing to LC). They do **not** establish the pre-infection total-effect causal direction the pre-reg targets, do **not** touch the locked `{age, smoking}` primary adjustment set, and do **not** gate t028 (data-gated regardless). They are M1-confirm-side triangulation material and feed `task:t036` (hormone-panel cohorts for the positive test of `hypothesis:0005`).

## Sources checked

- UKB field 40100, records of COVID-19 test results:
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=40100
- UKB Health and Well-Being questionnaire overview, Resource 2500:
  https://biobank.ndph.ox.ac.uk/ukb/refer.cgi?id=2500
- UKB menopause fields 2724/3581/3591/2834/3882 and HRT fields 2814/3536/3546:
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=2724
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3581
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3591
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3882
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3546
- UKB SHBG/testosterone/oestradiol fields:
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=30830
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=30850
  https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=30800
- UKB Infectious Disease Antigens category 1307:
  https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=51428
- Wang et al. EBioMedicine 2024 UKB PCC abstract:
  https://www.ukbiobank.ac.uk/publications/refinement-of-post-covid-condition-core-symptoms-subtypes-determinants-and-health-impacts-a-cohort-study-integrating-real-world-data-and-patient-reported-outcomes/
- Gao et al. JAMA Network Open 2024:
  https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825348
- Prieto-Alhambra et al. Research Square 2025 preprint:
  https://www.researchsquare.com/article/rs-7676837/v1
