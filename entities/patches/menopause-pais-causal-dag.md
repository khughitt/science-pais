---
id: patch-definition:menopause-pais-causal-dag
type: patch-definition
title: Menopausal transition and PAIS risk (t014/t023 causal DAG v2)
status: active
created: "2026-06-19"
updated: "2026-06-21"
project: post-acute-infection
ontology_terms: []
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0007-mechanism-of-female-predominance-in-pais
- topic:menopause-sex-hormones-and-pais-risk
- task:t014
- task:t023
source_refs: []
content_preview: Causal DAG v2 for the total effect of menopausal transition on failed post-infectious recovery, with the comorbidity time-split, a BMI time-split, smoking/parity/autoimmune-POI/frailty confounders, calendar-variant era, and hospitalization + survival selection colliders explicitly modelled.
file_path: entities/patches/menopause-pais-causal-dag.md
focal: hypothesis:0005-reproductive-stage-immune-homeostatic-margin
scope_set:
- scope: local
neighborhood_policy:
  name: local-closure-v1
  version: local-closure-v1
  max_depth: 2
patch_type: inquiry
inquiry:
  profile: causal
  status: sketch
  treatment: concept:menopausal-transition-reproductive-stage
  outcome: concept:pais-outcome
  boundary_roles:
  - ref: concept:menopausal-transition-reproductive-stage
    role: BoundaryIn
  - ref: concept:chronological-age
    role: BoundaryIn
  - ref: concept:sex-assigned-at-birth
    role: BoundaryIn
  - ref: concept:smoking
    role: BoundaryIn
  - ref: concept:baseline-bmi-adiposity
    role: BoundaryIn
  - ref: concept:pregnancy-history
    role: BoundaryIn
  - ref: concept:autoimmune-poi
    role: BoundaryIn
  - ref: concept:biological-frailty
    role: BoundaryIn
  - ref: concept:calendar-variant-vaccination-era
    role: BoundaryIn
  - ref: concept:pais-outcome
    role: BoundaryOut
  flow_edges:
  # chronological age (confounder, dominant)
  - subject: concept:chronological-age
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:chronological-age
    predicate: causes
    object: concept:baseline-cardiometabolic-comorbidity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:incident-cardiometabolic-comorbidity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:chronological-age
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:chronological-age
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:chronological-age
    predicate: causes
    object: concept:survival-selection
  # smoking (NEW: primary measured confounder)
  - subject: concept:smoking
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:smoking
    predicate: causes
    object: concept:baseline-cardiometabolic-comorbidity
  - subject: concept:smoking
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:smoking
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:smoking
    predicate: causes
    object: concept:survival-selection
  # sex assigned at birth (population-restriction given)
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:sex-assigned-at-birth
    predicate: causes
    object: concept:pais-outcome
  # baseline cardiometabolic comorbidity (CONFOUNDER; v2 split)
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:baseline-cardiometabolic-comorbidity
    predicate: causes
    object: concept:incident-cardiometabolic-comorbidity
  # baseline BMI / adiposity (CONFOUNDER; v2 time-split)
  - subject: concept:baseline-bmi-adiposity
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:baseline-bmi-adiposity
    predicate: causes
    object: concept:baseline-cardiometabolic-comorbidity
  - subject: concept:baseline-bmi-adiposity
    predicate: causes
    object: concept:pais-outcome
  # parity / pregnancy history (staging input + candidate confounder)
  - subject: concept:pregnancy-history
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:pregnancy-history
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:pregnancy-history
    predicate: causes
    object: concept:immune-dysregulation
  # autoimmune POI (etiologic-stratum confounder, NEW)
  - subject: concept:autoimmune-poi
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:autoimmune-poi
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:autoimmune-poi
    predicate: causes
    object: concept:immune-dysregulation
  # biological frailty (confounder + selection, NEW)
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:biological-frailty
    predicate: causes
    object: concept:survival-selection
  # calendar / variant / vaccination era (NEW: confounds mediator paths)
  - subject: concept:calendar-variant-vaccination-era
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:calendar-variant-vaccination-era
    predicate: causes
    object: concept:pais-outcome
  # treatment -> mediators
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:hormone-therapy
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:menopause-pais-symptom-overlap
  - subject: concept:menopausal-transition-reproductive-stage
    predicate: causes
    object: concept:incident-visceral-adiposity
  # sex hormones (mediator, first line)
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:incident-cardiometabolic-comorbidity
  - subject: concept:sex-hormone-levels
    predicate: causes
    object: concept:incident-visceral-adiposity
  - subject: concept:hormone-therapy
    predicate: causes
    object: concept:sex-hormone-levels
  - subject: concept:menopause-pais-symptom-overlap
    predicate: causes
    object: concept:hormone-therapy
  # incident visceral adiposity (mediator, NEW)
  - subject: concept:incident-visceral-adiposity
    predicate: causes
    object: concept:immune-dysregulation
  - subject: concept:incident-visceral-adiposity
    predicate: causes
    object: concept:incident-cardiometabolic-comorbidity
  # incident comorbidity (mediator; v2 split)
  - subject: concept:incident-cardiometabolic-comorbidity
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:incident-cardiometabolic-comorbidity
    predicate: causes
    object: concept:pais-outcome
  # immune / thrombo / severity (mediators)
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:acute-infection-severity
  - subject: concept:immune-dysregulation
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:thromboinflammation-and-endothelial-dysfunction
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:pais-outcome
  - subject: concept:thromboinflammation-and-endothelial-dysfunction
    predicate: causes
    object: concept:pais-outcome
  # ascertainment + colliders (do not condition)
  - subject: concept:menopause-pais-symptom-overlap
    predicate: causes
    object: concept:clinic-attendance
  - subject: concept:pais-outcome
    predicate: causes
    object: concept:clinic-attendance
  - subject: concept:acute-infection-severity
    predicate: causes
    object: concept:hospital-ascertainment
  - subject: concept:pais-outcome
    predicate: causes
    object: concept:hospital-ascertainment
  # latent unmeasured confounders (open back-door)
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:menopausal-transition-reproductive-stage
  - subject: concept:unmeasured-shared-confounders
    predicate: causes
    object: concept:pais-outcome
  unknowns:
  - concept:unmeasured-shared-confounders
  assumptions:
  - ref: pop-natal-female
    statement: 'Target population is natal females; menopausal transition is undefined otherwise, so sex assigned at birth is a population-definition given rather than a within-analysis exposure. The broader female-vs-male predominance contrast (q0007) is a separate estimand not addressed by this DAG.'
  - ref: clinic-collider
    statement: 'Clinic attendance is a COLLIDER of menopause-driven symptom overlap and PAIS. Post-infection-clinic samples (Stewart2024-type cohorts) condition on it by construction; conditioning on it opens a spurious menopause-PAIS path and must be avoided. Do-not-condition.'
  - ref: hospital-collider
    statement: 'Hospitalization / acute-care ascertainment is a SECOND selection collider (severe acute illness -> hospital -> cohort entry -> both severity and detected PAIS). A hospitalized or acute-care-ascertained sample conditions on it by construction and manufactures a spurious severity-PAIS association. Do-not-condition; prefer population-based sampling.'
  - ref: survival-selection
    statement: 'Survival selection / left-truncation is a collider on age, smoking, and frailty (alive-and-enrolled at baseline/2020). Cohort membership conditions on it, inducing M3a left-truncation bias; handle via competing-risk / selection modelling and sensitivity, not by adding it as an adjustment covariate.'
  - ref: total-effect-mediators
    statement: 'Under the primary (total-effect) estimand, sex hormone levels, immune dysregulation, thromboinflammation/endothelial dysfunction, acute infection severity, incident cardiometabolic comorbidity, and incident visceral adiposity are MEDIATORS of the menopausal-transition effect and are left UNADJUSTED. A severity-controlled direct effect would additionally condition on acute infection severity (and then must also control calendar-variant era, which confounds the severity -> PAIS path).'
  - ref: comorbidity-time-split
    statement: 'The v1 single cardiometabolic-comorbidity node is SPLIT in v2 into baseline (pre-infection) comorbidity and menopause-incident comorbidity. Baseline comorbidity is a CONFOUNDER (it gains a baseline-comorbidity -> menopause-timing edge: metabolic disease accelerates menopause) and incident comorbidity is a MEDIATOR (menopause -> hormones -> incident comorbidity -> PAIS). The split is what keeps the new confounder edge acyclic; naively adding it to the single node would have created a cycle.'
  - ref: bmi-time-split
    statement: 'BMI/adiposity is time-split in the same way. Baseline BMI is a CONFOUNDER (higher BMI -> later menopause via peripheral estrogen, and -> worse acute/long COVID), while menopause-incident visceral adiposity is a MEDIATOR on the M1 path (menopause -> visceral fat -> inflammation -> PAIS). Adjusting incident adiposity over-adjusts; baseline BMI is carried only as a sensitivity covariate.'
  - ref: smoking-primary-confounder
    statement: 'Smoking is a measured strong common cause (smoking -> earlier menopause, -> worse COVID/long-COVID, -> higher mortality/left-truncation) and is the v2 PRIMARY measured confounder alongside age (set {age, smoking}, per the t029 reviewer ratification Q1). Coding is baseline never/former/current + pack-years/duration; baseline smoking is pre-infection but not always pre-FMP, so it enters as a measured confounder, not a clean pre-menopause exposure.'
  - ref: parity-dual-role
    statement: 'Parity (pregnancy history) has a dual role - a reproductive-stage staging input AND a candidate confounder of the timing -> PAIS edge (parity -> later menopause, and parity -> immune/LC effects). It gains a parity -> menopause-timing edge in v2 but is held in the sensitivity arm, with an explicit guard against drifting the estimand toward a reproductive-life-course exposure.'
  - ref: autoimmune-poi-stratum
    statement: 'Autoimmune POI is a distinct etiologic-stratum confounder (autoimmunity -> early menopause AND -> PAIS predisposition), not a generic autoimmune-diagnosis (20002) adjustment. Drawn explicitly in v2; handled as a stratum/quarantine plus sensitivity, not a primary covariate (t029 Q3).'
  - ref: frailty-confounder-and-selection
    statement: 'Biological frailty / subclinical pre-infection ill-health is BOTH a confounder (frailty -> earlier menopause AND -> higher PAIS susceptibility) and a selection/competing-risk structure (frailty -> survival selection -> cohort entry). It is handled via selection modelling plus sensitivity, not as a primary adjustment covariate (t029 Q3).'
  - ref: era-mediator-confounder
    statement: 'Calendar period / variant / vaccination era is a common cause of acute severity and of who is studied. It is NOT a cause of menopause timing, so it is off the total-effect back-door (it does not enter the primary adjustment set) unless linked to the exposure via shielding behaviour - a structural alternative noted in prose but not drawn. It DOES confound the mediator (acute severity) -> outcome path and so matters for the severity-controlled direct-effect secondary.'
  - ref: primary-measured-set-not-formally-sufficient
    statement: 'KEY v2 IDENTIFICATION FINDING. With U latent the total effect remains NON-IDENTIFIABLE by adjustment (no measured back-door set blocks the U path). Setting U aside and handling sex by population restriction, the formal minimal sufficient measured set in v2 is the full battery {age, smoking, baseline-cardiometabolic-comorbidity, baseline-bmi, parity, autoimmune-POI, frailty} - because every one of those nodes now has an edge into menopause timing and a path to PAIS. The committed PRIMARY measured set {age, smoking} (t029-ratified, pre-registration:0001) is therefore a deliberate measured-SUBSET choice: the remaining five are confounders-by-structure DEMOTED to sensitivity arms by judgement (ambiguous timing/role, measurement quality, second-order strength), NOT because the graph licenses ignoring them. This is documentation of structure and sensitivity scope only; it does not change pre-registration:0001''s committed primary set and triggers no amendment.'
  - ref: ht-confounding-by-indication
    statement: 'Hormone therapy is subject to confounding by indication and healthy-user bias; observational HT-PAIS contrasts are not interpretable as the HT causal effect without a target-trial / new-user design (t019).'
---

# Inquiry: Menopausal transition and PAIS risk (t014/t023 causal DAG v2)

## Summary

Causal DAG (sketch, **v2 redraw under t023**) for **task t014**, operationalizing
`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` and
`question:0013-reproductive-stage-failed-immune-recovery-after-infection`.

**Primary estimand (locked, unchanged by v2):** the *total effect* of **menopausal
transition (reproductive stage)** on the **PAIS outcome** (failed post-infectious
recovery). The committed **primary measured adjustment set is `{age, smoking}`**
(t029-ratified; `pre-registration:0001`); **sex assigned at birth** is handled by
population restriction (natal females). Leave **sex hormones, immune dysregulation,
thromboinflammation/endothelial dysfunction, acute infection severity, incident
comorbidity, and incident visceral adiposity** unadjusted as mediators. Never
condition on the colliders **clinic attendance**, **hospitalization/ascertainment**,
or **survival selection**.

> **What v2 changed (t023).** v2 implements the four structural fixes the
> `/science:critique-approach` review and the t029 confounder review staged:
> 1. **Comorbidity time-split** — the single `cardiometabolic comorbidity` node is
>    split into **baseline** (confounder; gains the `baseline → menopause-timing`
>    edge) and **incident** (mediator). The split is what makes the new confounder
>    edge **acyclic** (adding it to the single node would have created a cycle).
> 2. **New confounders drawn explicitly** — `smoking` (primary), `baseline BMI`
>    (with an `incident visceral adiposity` mediator time-split), `parity →
>    menopause`, `autoimmune-POI` (etiologic stratum), and `biological frailty`
>    (confounder + survival-selection).
> 3. **Two new selection colliders** — `hospitalization/ascertainment` and
>    `survival selection` (left-truncation), alongside the existing clinic collider.
> 4. **Calendar/variant/vaccination era** — common cause of acute severity and of
>    who is studied; confounds the mediator→outcome path (matters for the
>    direct-effect secondary), off the total-effect back-door.
>
> **Key identification finding (see the `primary-measured-set-not-formally-sufficient`
> assumption).** With U latent the total effect is still **non-identifiable**. Setting
> U aside, the *formal* minimal sufficient measured set in v2 is the **full battery**
> `{age, smoking, baseline-comorbidity, baseline-BMI, parity, autoimmune-POI,
> frailty}` — `{age, smoking}` alone is **not** sufficient in v2. The committed
> primary `{age, smoking}` is thus a deliberate **measured-subset**; the other five
> are confounders-by-structure **demoted to sensitivity arms by judgement**. This is
> structure/sensitivity documentation only — it does **not** alter
> `pre-registration:0001` and triggers **no** amendment.

This matches h0005's organizing conjecture: menopause is **not** posited as a direct
cause of PAIS, but as a threshold-shifter acting *through* hormone-driven immune,
endothelial, and autonomic pathways.

## Node role pre-declaration (v2)

| Node | Role w.r.t. menopause → PAIS | Handling |
|---|---|---|
| Chronological age | Confounder (dominant) | **Adjust (primary)** |
| Smoking | Confounder (measured, strong) | **Adjust (primary)** — t029 Q1 |
| Sex assigned at birth | Population-definition given | Restrict population (natal females) |
| Baseline cardiometabolic comorbidity | Confounder (gains `→ menopause` edge) | Sensitivity arm (not primary) |
| Baseline BMI / adiposity | Confounder | Sensitivity arm (not primary) |
| Parity / pregnancy history | Staging input + candidate confounder | Sensitivity arm; guard estimand drift |
| Autoimmune POI | Confounder (etiologic stratum) | Stratum/quarantine + sensitivity |
| Biological frailty | Confounder + selection/competing-risk | Selection model + sensitivity |
| Calendar / variant / vaccination era | Confounder of mediator→outcome path | Adjust only for direct-effect secondary |
| Sex hormone levels | Mediator (first line) | Do not adjust (total effect) |
| Hormone therapy | Mediator + confounded-by-indication | Separate target-trial estimand (t019) |
| Incident cardiometabolic comorbidity | Mediator | Do not adjust (total effect) |
| Incident visceral adiposity | Mediator (M1 path) | Do not adjust (total effect) |
| Immune dysregulation | Mediator | Do not adjust (total effect) |
| Thromboinflammation / endothelial dysfunction | Mediator | Do not adjust (total effect) |
| Acute infection severity | Mediator | Do not adjust; condition only for direct effect |
| Menopause-PAIS symptom overlap | Ascertainment / measurement | Model misclassification; do not treat as biology |
| Clinic attendance | **Collider** | **Do not condition** |
| Hospitalization / ascertainment | **Collider** (selection) | **Do not condition**; prefer population sampling |
| Survival selection / left-truncation | **Collider** (selection) | **Do not condition**; competing-risk modelling |
| Unmeasured shared confounders (U) | Latent confounder (open back-door) | Identifiability threat — non-identifiable as drawn |

## Identifiability (v2, pgmpy/networkx-validated 2026-06-21)

- **U latent (real world):** **no valid measured back-door adjustment set** — the
  total effect is **not identifiable** by covariate adjustment (unchanged headline).
- **U set aside, sex by restriction:** the **unique minimal sufficient measured set**
  is the **full battery** `{age, smoking, baseline-comorbidity, baseline-BMI, parity,
  autoimmune-POI, frailty}`. `{age, smoking}` alone is **not** sufficient in v2.
- **Reconciliation:** the committed primary `{age, smoking}` is a deliberate
  measured-subset; the other five are demoted to **sensitivity arms** by judgement.
  Identification still rests on an E-value / bounding argument for U plus the
  sensitivity battery — not on adjustment alone.
- 23 nodes, 59 edges, acyclic. Colliders (clinic, hospital, survival selection) appear
  in **no** recommended set; mediators are correctly excluded from the total-effect set.

## Reverse causation

Kept as a **separate acyclic inquiry** (`t021`, h0005 P-reverse): the infection/PAIS →
reproductive-axis edge would create a cycle if added here, so it is handled by **temporal
ordering** — exposure fixed at **pre-infection reproductive stage** — not a bidirectional edge.

## Notes

- Built via the inquiry patch-definition layout (layout v3); causal edges are authored
  as `flow_edges` with `predicate: causes` and materialized to the
  `inquiry/<slug>` named graph by `science graph build`.
- v2 supersedes the v1 sketch (single comorbidity node). See
  `doc/inquiries/menopause-pais-causal-dag-critique.md` (the adversarial review that
  staged these edges) and `doc/methods/2026-06-19-confounder-open-questions-and-staged-amendment.md`
  (the t029 reviewer rulings Q1–Q4 that fixed each node's primary-vs-sensitivity disposition).
- Next: re-run `/science:critique-approach` on v2 if desired; then `/science:plan-analysis`
  (t016) already encodes the `{age, smoking}` primary set against the measured cohort.
