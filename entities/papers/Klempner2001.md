---
id: paper:Klempner2001
type: paper
title: 'Two Controlled Trials of Antibiotic Treatment in Patients with Persistent
  Symptoms and a History of Lyme Disease'
status: active
paper_kind: ""
ontology_terms:
  - post-treatment Lyme disease syndrome
  - PTLDS
  - Borrelia burgdorferi
  - randomized controlled trial
  - antibiotic retreatment
  - ceftriaxone
  - doxycycline
  - health-related quality of life
  - SF-36
  - antigen persistence
  - target engagement
source_refs:
  - cite:Klempner2001
related:
  - hypothesis:0002-tissue-reservoir-antigen-fragment
  - question:0002-antigen-clearance-rescues-symptoms
  - proposition:0020-antigen-clearance-rescues-established-pais
  - topic:antigen-pathogen-persistence
created: '2026-06-24'
updated: '2026-06-24'
---

# Two Controlled Trials of Antibiotic Treatment in Patients with Persistent Symptoms and a History of Lyme Disease

<!--
- **Authors:** Mark S. Klempner, Linden T. Hu, Janine Evans, Christopher H. Schmid, Gary M. Johnson, Richard P. Trevino, DeLona Norton, Lois Levy, Diane Wall, John McCall, Mark Kosinski, Arthur Weinstein
- **Year:** 2001
- **Journal:** New England Journal of Medicine
- **DOI:** 10.1056/NEJM200107123450202
- **BibTeX key:** Klempner2001
- **Source:** LLM knowledge + Europe PMC abstract (status: blocked_but_oa; abstract fully retrieved)
-->

## Key Contribution

The landmark first negative RCT of antibiotic retreatment for what is now called post-treatment Lyme
disease syndrome (PTLDS). Two parallel placebo-controlled trials — one in seropositive patients and one
in seronegative patients — found that 90 days of IV ceftriaxone followed by 60 days of oral doxycycline
produced no improvement in health-related quality of life (SF-36) compared with placebo. Both trials were
stopped early after a planned interim analysis for futility.

## Methods

Two independently powered, parallel double-blind RCTs conducted at US academic sites in patients with
well-documented, previously treated Lyme disease who had persistent musculoskeletal pain, neurocognitive
symptoms, or dysesthesia, often accompanied by fatigue.

- **Cohort 1 (seropositive):** n = 78 patients with IgG seropositivity to *Borrelia burgdorferi* at
  enrollment.
- **Cohort 2 (seronegative):** n = 51 patients who were seronegative.
- **Intervention:** IV ceftriaxone 2 g/day for 30 days, followed by oral doxycycline 200 mg/day for 60
  days (total 90 days antibiotic exposure), vs matching IV and oral placebos.
- **Primary outcome:** Improvement on the physical-component summary (PCS) and mental-component summary
  (MCS) scales of the SF-36 at day 180 (end-of-follow-up), measuring health-related quality of life.
- **Stopping rule:** Planned interim analysis on the first 107 participants; the Data and Safety
  Monitoring Board (DSMB) recommended discontinuation when data indicated it was highly unlikely that a
  significant treatment effect would emerge with the full planned enrollment of 260 patients.

## Key Findings

- **Null primary outcome (both cohorts):** No significant difference in SF-36 PCS or MCS scores between
  antibiotic and placebo arms in intention-to-treat analyses.
- **Seropositive arm (detailed):** Among antibiotic-treated patients, 37% improved, 29% unchanged, 34%
  worsened; among placebo-treated patients, 40% improved, 26% unchanged, 34% worsened — P = 0.96 for
  comparison between arms.
- **Seronegative arm:** Results were similarly null.
- **Severe baseline impairment:** Both cohorts documented severe health-related quality-of-life impairment
  at baseline, validating the clinical significance of the patient population.
- **Early stopping for futility:** Stopped after ~107/260 planned participants; the futility threshold was
  crossed, not a safety signal.
- **No antigen or pathogen biomarker measured:** The trial did not assay for residual *Borrelia*
  peptidoglycan fragments, other degradation-resistant antigen remnants, or any marker of live or dead
  spirochetal persistence before, during, or after treatment.

## Relevance

This trial is the Borrelia-PTLDS parallel to the SARS-CoV-2 long-COVID antigen-clearance nulls (STOP-PASC,
outSMART-LC) already coded in this project. It bears directly on `proposition:0020` (clearing persistent
antigen rescues symptoms in established PAIS) and `question:0002` (does antigen clearance attenuate
post-acute symptoms?).

The trial is coded as **disputing evidence — weak and uninterpretable** for `proposition:0020`, in the
same evidentiary class as `evidence-line:0053`–`0055`. The core analytical reason:

- **Target-engagement gap:** Antibiotics act on live spirochetes. They have no established mechanism for
  degrading or clearing residual, non-viable *Borrelia* peptidoglycan (pPG^Bb) — the chemically
  degradation-resistant fragment shown by McClune2025 to persist in macrophages after spirochete
  clearance. A null retreatment trial can only falsify the claim "more antibiotic kills more live
  bacteria, and that kills symptoms." It cannot falsify the claim "residual pPG^Bb, which antibiotics do
  not degrade, persists and drives symptoms."
- **No antigen-positivity enrichment:** The trial did not enrich for patients with detectable residual
  antigen; the treated population's antigen status at baseline was never established.
- **No antigen-clearance assay:** Whether the antibiotic course reduced any measure of residual antigen
  burden was not tested.

The treatment-null result therefore does not constitute a clean disconfirmation of the antigen-persistence
hypothesis for PTLDS, for the same structural reason that Bhattacharjee2026 renders the STOP-PASC null
uninterpretable in long COVID.

This paper completes the PTLDS half of the "Borrelia/Coxiella clearance parallel" flagged as not yet
ingested in `hypothesis:0002-tissue-reservoir-antigen-fragment`.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Persistent symptoms after treated Lyme disease | PTLDS (post-treatment Lyme disease syndrome) | A named PAIS subtype; fits the project's shared-failure-mode frame |
| Prolonged antibiotic retreatment | Antigen-clearance intervention | Proxy only — targets live spirochetes, not degradation-resistant fragments |
| SF-36 PCS/MCS at day 180 | Health-related QoL symptom endpoint | Subjective; the study lacks objective biomarker co-endpoints |
| No residual-antigen assay | Target-engagement gap | The decisive interpretability flaw for `proposition:0020` |
| DSMB-mandated futility stop | Early stopping for futility | Reduces statistical power vs full enrollment; finding is a null |

## Limitations

- **Target-engagement not demonstrated:** No assay for residual *Borrelia* antigen, peptidoglycan, DNA,
  or viable spirochetes was performed. The trial cannot distinguish "antigen-persistence drives symptoms
  but antibiotics do not clear fragments" from "no antigen persists and antigen is irrelevant."
- **Stopped early for futility (underpowered):** Final n = 107 vs planned n = 260. The null is formally
  supported by the futility crossing, but a modest treatment effect cannot be fully excluded at the
  planned sample size.
- **Seropositive/seronegative split not mechanistically informative:** Serostatus is a rough proxy for
  prior pathogen exposure and immune engagement, not a direct measure of residual antigen burden.
- **No antigen-positive enrichment:** Patients were not stratified by any marker of active or residual
  Borrelia burden; any benefit in an antigen-positive subgroup would be diluted in the ITT analysis.
- **Outcome is subjective QoL only:** No objective neurological, immunological, or inflammatory
  co-endpoints were pre-specified, limiting mechanistic interpretation.
- **Seronegative cohort is definitionally ambiguous:** Persistent symptoms without seropositivity raises
  diagnostic uncertainty; this arm may contain misdiagnosed patients.
- **Adverse events not detailed in the abstract:** IV ceftriaxone has known risks (biliary sludge,
  allergic reactions); the risk/benefit calculus for retreatment is unfavorable regardless of the null.
- **2001 sample; pre-PTLDS case-definition consensus:** The case definition predates the 2006 IDSA PTLDS
  working definition and current CCC/ICC-analog frameworks for post-infectious illness. Cohort
  composition may not map cleanly onto modern PTLDS criteria.

## Model / Tool Availability

Not applicable — this is a clinical trial; no models, tools, or datasets are released for reuse.

## Follow-up

- **Fallon2008 (NEJM):** A second seropositive-only PTLDS retreatment RCT (IV ceftriaxone vs placebo)
  with a cognitive primary endpoint; also negative — would extend the disputing-evidence base for
  `proposition:0020` in the PTLDS arm. [UNVERIFIED — not yet summarized in this project]
- **McClune2025:** The direct counterpart demonstrating pPG^Bb persistence and biological activity after
  antibiotic clearance in a mouse model; mechanistically explains why Klempner2001 is an uninterpretable
  null rather than a disconfirmation.
- **`hypothesis:0002-tissue-reservoir-antigen-fragment`:** Update "Disputing Evidence" to add Klempner2001
  as the PTLDS parallel now ingested.
- **`proposition:0020-antigen-clearance-rescues-established-pais`:** Add an evidence line for
  Klempner2001 (PTLDS IV ceftriaxone/doxycycline retreatment, null on SF-36, stopped for futility, no
  antigen target-engagement) as a cross-pathogen replication of the uninterpretable-null pattern.
- Question for the project: is there a Coxiella/Q-fever retreatment RCT analogous to Klempner2001 and
  STOP-PASC? If so, the "PTLDS antibiotic-retreatment / COVID antiviral-retreatment / QFFS null" triad
  would be the strongest available cross-pathogen illustration of the target-engagement problem.
