---
id: interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
kind: interpretation
title: "t061: no public severity-adjusted PEM molecular matrix is runnable; RECOVER-Adult is the controlled-access route"
status: active
source_refs: &id001
- paper:Maestri2025
- paper:Ozonoff2024
related:
- question:0015-does-pem-requirement-improve-cross-study-comparability
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands
- dataset:recover-adult
- dataset:impacc-immunophenotyping-covid
- paper:Maestri2025
- paper:Ozonoff2024
- task:t061
created: '2026-06-26'
updated: '2026-06-26'
input: *id001
prior_interpretations:
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands
relations:
- predicate: sci:amends
  target: interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands
- predicate: sci:amends
  target: interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
---
<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE. Input is a route audit of the known STOP-PASC,
RECOVER-Adult, and IMPACC surfaces, including live public access checks on 2026-06-26. No participant-
level data were available or analyzed. -->

# Interpretation: t061 - severity-adjusted PEM molecular contrast vehicle triage

## Verdict

**[?] no public runnable vehicle; controlled-access route identified.** The decisive q0015 test remains
uncomputed: no public participant-level matrix currently combines validated PEM measurement,
overall-severity covariates, acute-severity covariates, and molecular endpoints in a form we can analyze
locally. `dataset:recover-adult` is the best route because it is designed around symptom-level RECOVER
phenotyping and controlled-access participant data; it is not a local/public computation. STOP-PASC
remains the nearest published proteome source but is still blocked on individual-level release.
IMPACC/SDY1760 is useful for post-acute phenotype biology but is not an admissible PEM-specific vehicle.

## Route Triage

| Route | Status | Why |
|---|---|---|
| STOP-PASC / `paper:Maestri2025` | **blocked** | The stated GitHub repository (`https://github.com/Khatri-Lab/STOP_PASC_biomarkers`) still returned GitHub 404 on 2026-06-26. The paper's public model is still marginal per-symptom proportional odds, batch-plate-only adjusted, so separate reported coefficients cannot be refit into the severity-adjusted PEM contrast. |
| RECOVER-Adult / `dataset:recover-adult` | **best controlled-access route** | RECOVER's public data page says de-identified participant-level datasets are available through NHLBI BioData Catalyst with registration/permission and dbGaP DAR; the Adult/Pregnancy data dictionary and data-use agreement are public pointers. This is the right access path for a participant-level symptom + severity + molecular model, but not executable without controlled access and confirmation of the needed omics module. |
| IMPACC / `dataset:impacc-immunophenotyping-covid` | **not admissible for q0015** | ImmPort SDY1760 is live and controlled-access, and `paper:Ozonoff2024` shows rich post-acute PRO clusters plus immunophenotyping. But the cohort is hospitalized-only and the available phenotype structure is fatigue/physical/cognitive recovery clusters, not a validated PEM-positive vs PEM-negative instrument with severity-matched arms. It can support adjacent severity/phenotype work, not the decisive PEM-specific molecular contrast. |

## Admissibility Rule for the Future Vehicle

The q0015 vehicle is admissible only if it supplies all of the following in the same participants:

- validated PEM status or severity, preferably DSQ-PEM or RECOVER symptom items that can be mapped to a
  PEM-positive vs PEM-negative contrast;
- a non-PEM overall-severity covariate, such as summed non-PEM symptom burden, PROMIS fatigue plus
  functional limitation, or a latent severity score built without the PEM item;
- acute-severity covariates, including hospitalization/ICU/oxygen, vaccination/prior infection, and time
  since acute infection;
- at least one molecular endpoint measured in the post-acute window, preferably proteomics,
  transcriptomics, metabolomics, or immune profiling;
- enough PEM-negative participants at comparable overall severity to avoid reducing the contrast to
  "severe long COVID vs mild long COVID."

If a candidate lacks the severity covariate, it can only reproduce the Maestri2025 limitation. If it lacks
a validated PEM measure, it can test fatigue/physical recovery endotypes but not q0015.

## Proposed Analysis When Access Exists

The primary model should estimate a PEM effect while conditioning on non-PEM severity:

`molecular_feature ~ PEM + non_PEM_severity + acute_severity + age + sex + BMI + time_since_infection + batch`

For continuous PEM severity, use an ordinal or continuous symptom model with the same non-PEM severity
covariate. Sensitivity analyses should replace `non_PEM_severity` with fatigue-only, functional-limit
burden, and a latent symptom factor excluding PEM. The decision criterion is whether PEM-associated
molecular features remain after severity adjustment and whether those features differ from the generic
severity axis.

## Implications

This amends `interpretation:0007` without changing its belief update. The gap is sharper:
STOP-PASC is not merely "not yet refit"; its public artifact still does not exist. RECOVER is the
preferred next route, but it is a data-access task, not a local analysis task. IMPACC should not be used
as a substitute unless a validated PEM item can be located in its controlled-access instruments.

For `question:0015`, the standing answer remains: PEM requirement is mechanistically plausible and likely
improves within-trigger coherence, but the decisive molecular separation from overall severity remains
unproven. For `proposition:0011`, no new evidence-line is warranted because this is a feasibility verdict,
not a new endpoint result.

## Follow-up

- Open a controlled-access RECOVER-Adult route only if we are ready to pursue a dbGaP/BioData Catalyst
  data-access request and confirm the necessary omics module.
- Keep a lightweight watch on the STOP-PASC repository/data release; if it appears, reopen the Maestri2025
  refit route.
- Do not spend effort forcing IMPACC into q0015 unless controlled metadata reveals a real PEM item; use it
  instead for broader severity/phenotype-cluster questions.
