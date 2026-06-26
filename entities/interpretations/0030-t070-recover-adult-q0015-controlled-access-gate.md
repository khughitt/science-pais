---
id: interpretation:0030-t070-recover-adult-q0015-controlled-access-gate
type: interpretation
title: "t070 - RECOVER-Adult q0015 controlled-access gate: phenotype release clears, molecular release does not"
status: active
source_refs:
- dataset:recover-adult
related:
- question:0015-does-pem-requirement-improve-cross-study-comparability
- dataset:recover-adult
- interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
- task:t070
created: '2026-06-26'
updated: '2026-06-26'
input:
- dataset:recover-adult
prior_interpretations:
- interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
relations:
- predicate: "sci:amends"
  target: "interpretation:0027-t061-severity-adjusted-pem-vehicle-triage"
---
# Interpretation: t070 - RECOVER-Adult controlled-access q0015 gate

## Verdict

**[?] phenotype vehicle confirmed; molecular vehicle not yet admissible.** RECOVER-Adult is worth keeping
as the best controlled-access path for `question:0015`, but the current public release/access surface does
not yet clear the decisive severity-adjusted PEM molecular contrast. The phenotype side is strong:
participant-level controlled access exists, the current Adult/Pregnancy release is `phs003463.v6.p5`,
RECOVER publishes a public codebook, and the codebook contains repeated PASC Symptoms fields for current
PEM plus DePaul-style bother/frequency/severity follow-ups. Acute-severity and treatment covariates,
EHR linkage, biospecimen inventories, and wearable metadata are also released.

The blocking gate is molecular release. The public dbGaP page exposes phenotype datasets and variables but
shows the Molecular Datasets tab as non-selectable. The March 2026 release notes describe surveys,
laboratory tests, biospecimen inventory, diagnostic-study metadata, EHR data, and raw wearable data; they
do not identify released proteomics, metabolomics, transcriptomics, or immune-profiling matrices joinable
to the PASC symptom rows. Therefore t070 does **not** activate a local analysis plan and does **not**
update `question:0015` or `proposition:0011`.

## Gate Readout

| Gate | Status | Public evidence |
|---|---|---|
| Same-participant controlled access | **clears in principle** | RECOVER's data page states de-identified participant-level datasets are available through NHLBI BioData Catalyst/dbGaP with registration and permission. |
| Current cohort release | **clears** | Current Adult/Pregnancy snapshot: data through 2025-12-05, released 2026-05-13; dbGaP accession `phs003463.v6.p5`. |
| PEM measurement | **clears** | Codebook fields include `ps_malaise_c13`, `ps_malaise_c24`, `ps_malaise_fu`, `ps_malaise_calc`, `ps_malaise_botherdepaul`, `ps_malaise_freqdepaul`, and `ps_malaise_sevdepaul`. The survey text defines PEM as symptoms worse after even minor physical or mental effort. |
| Non-PEM severity covariate | **likely clears** | The PASC Symptoms form has fatigue, soreness, weakness, cognitive, sleep, pain, mood, autonomic, cardiopulmonary, and GI items with DePaul-style frequency/severity follow-ups for many domains. A non-PEM symptom-burden score can be built if controlled data expose these fields consistently. |
| Acute-severity covariates | **clears** | Infection surveys include care setting, hospitalization, emergency care, and acute-treatment items; EHR data are released for a subset. |
| Molecular endpoint | **does not clear** | Public release notes and dbGaP navigation do not expose released omics matrices. Biospecimen inventory is not a molecular endpoint. |
| Joinable same-subject PEM + omics | **unknown / not public** | Requires controlled-access confirmation or a future molecular release/ancillary assay. |

## Consequence

The next RECOVER move should be a **data-access scoping decision**, not a pre-registered analysis:

1. If the goal is q0015 specifically, a DAR should ask whether any released or soon-to-release RECOVER-Adult
   molecular module is joinable to the PASC Symptoms table and includes enough PEM-negative, severity-matched
   participants.
2. If no omics module is available, RECOVER-Adult can still support a phenotype-only or wearable/EHR
   severity analysis, but that would answer a different question.
3. If an omics module later appears, the locked analysis from `interpretation:0027` remains the right
   estimand: molecular feature ~ PEM + non-PEM severity + acute severity + demographics + timing + batch.

## Implications

This strengthens, but does not close, the t061 conclusion. RECOVER-Adult is no longer just a generic
controlled-access suggestion: it has a verified current accession and clear phenotype variables for the
PEM/severity side of q0015. It remains non-runnable for the decisive molecular contrast because omics
availability is not established on the public access surface. No evidence-line is coded because no new
biological result was observed.
