---
id: paper:Fallon2008
kind: paper
title: A randomized, placebo-controlled trial of repeated IV antibiotic therapy for
  Lyme encephalopathy
status: active
paper_kind: ''
ontology_terms:
- post-treatment Lyme disease syndrome
- PTLDS
- Lyme encephalopathy
- antibiotic retreatment
- cognitive impairment
- antigen persistence
- randomized controlled trial
dataset_usage: []
source_refs:
- cite:Fallon2008
related:
- proposition:0020-antigen-clearance-rescues-established-pais
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- discussion:0003-antigen-persistence-treatable-vs-fixed
- interpretation:0011-t046-antigen-clearance-trials-ingestion
created: '2026-06-24'
updated: '2026-06-24'
---

# A randomized, placebo-controlled trial of repeated IV antibiotic therapy for Lyme encephalopathy

<!--
- **Authors:** Fallon BA, Keilp JG, Corbera KM, Petkova E, Britton CB, Dwyer E, Slavov I, Cheng J, Dobkin J, Nelson DR, Sackeim HA
- **Year:** 2008
- **Journal:** Neurology, 70(13):992–1003
- **DOI:** 10.1212/01.WNL.0000284604.61160.2d
- **BibTeX key:** Fallon2008
- **Source:** Abstract (Europe PMC) + LLM knowledge
-->

## Key Contribution

This RCT tested whether 10 weeks of IV ceftriaxone produces lasting cognitive benefit in patients with persistent memory/cognitive impairment after prior standard IV antibiotic therapy for Lyme disease (Lyme encephalopathy, a recognized PTLDS phenotype). The primary finding was a statistically significant but **transient** broad cognitive improvement at week 12 (end of treatment) that was **not sustained at week 24** after antibiotics were discontinued — the cognitive benefit fully relapsed within 12 weeks of stopping treatment. Adverse events from IV access (PICC lines) occurred in 26% of the ceftriaxone group versus 7% of placebo, establishing an unfavorable risk/benefit profile for retreatment.

## Methods

**Design:** Randomized, double-masked, placebo-controlled parallel-group trial.

**Participants:** Patients with well-documented prior Lyme disease (requiring at least 3 weeks of prior IV antibiotic therapy), current positive IgG Western blot, and objectively confirmed memory impairment on neuropsychological testing. Healthy volunteers served as a no-treatment control for practice effects. Screening was extensive: 3,368 patients and 305 volunteers were screened to yield 37 enrolled patients and 20 healthy controls.

**Intervention:** IV ceftriaxone (n = 23) or IV placebo (n = 14) administered for 10 weeks, followed by a no-antibiotic observation period.

**Outcomes:**
- Primary: Neurocognitive performance at week 12 (end of treatment), specifically memory.
- Secondary durability: same battery at week 24 (12 weeks post-treatment).
- Secondary clinical: fatigue, pain, and physical functioning.

**Analysis:** Longitudinal mixed-effects models estimating group-by-time interactions across six cognitive domains.

**Antigen marker:** No measure of residual Borrelia antigen or peptidoglycan fragment was collected at any timepoint. The trial was designed around symptom and cognitive endpoints only; whether the antibiotic course achieved any reduction in pathogen-derived material was not assessed.

## Key Findings

**Cognitive outcomes:**
- At week 12: a significant treatment-by-time interaction favored the ceftriaxone group across all six cognitive domains tested. The effect was generalized (not confined to memory), moderate in magnitude.
- At week 24: the cognitive improvement was **not sustained**; patients regressed after antibiotic discontinuation and the between-group difference was lost. The benefit was fully transient.

**Secondary clinical outcomes:**
- Patients receiving antibiotics who had more severe fatigue, pain, and impaired physical functioning at baseline showed improvement at week 12; **pain and physical functioning improvements were sustained to week 24**, while fatigue was not explicitly noted as sustained. The cognitive signal did not parallel this partial persistence.

**Adverse events:**
- 6 of 23 (26.1%) ceftriaxone patients experienced adverse events attributable to either the study medication or the PICC line.
- 1 of 14 (7.1%) placebo patients experienced such events.
- All adverse events resolved without permanent injury, but the 26% rate represents a clinically meaningful procedural risk for a transient benefit.

**Enrollment challenge:** The 3,368:37 screening-to-enrollment ratio (~91:1) illustrates how stringent the IgG Western blot plus objective memory impairment criteria were for this population.

## Relevance

Fallon2008 is the principal PTLDS retreatment RCT focused on cognitive endpoints and is directly relevant to `proposition:0020` (clearing persistent antigen rescues symptoms in established PAIS). It is coded as **disputing — weak and uninterpretable** evidence on that proposition, for two compounding reasons:

1. **No antigen target-engagement was demonstrated.** The trial contains no measure of whether IV ceftriaxone altered residual Borrelia antigen or peptidoglycan (pPG^Bb) levels. The intervention is therefore a **proxy for antigen clearance**, not a test of it. A positive cognitive signal at week 12 could reflect antibiotic action on residual viable organisms, immunomodulatory effects of ceftriaxone independent of antigen, or PICC-line-mediated effects — none of which require the antigen-clearance mechanism. A null at week 24 likewise cannot distinguish "antigen persisted and drives relapse" from "antibiotic effect wore off."

2. **The cognitive benefit was transient, not durable.** The fact that improvement dissipated after the drug was stopped is consistent with an antigen-dependent mechanism (persistent antigen re-drives pathology once antibiotic pressure is removed), but equally consistent with direct pharmacological suppression of a self-sustaining neuroinflammatory process that re-established after treatment ended. The trial design cannot discriminate these.

Together, these properties place Fallon2008 in the same "uninterpretable-null" category as the long COVID antiviral RCTs (Geng2024, Bhattacharjee2026, Peluso2026) cataloged under `proposition:0020`: the treatment was a proxy for the mechanistic variable of interest, and the proxy was never validated.

The adverse event profile (26% in the treatment arm) is directly relevant to the risk/benefit calculus that would motivate or disfavor Borrelia-specific antigen-clearance trials: even if a future trial were to demonstrate pPG^Bb target-engagement, the IV delivery route imposes a safety cost that would require proportionate and durable benefit to justify.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Lyme encephalopathy with persistent cognitive symptoms | PTLDS / established PAIS | PTLDS is this project's Borrelia-specific PAIS phenotype |
| IV ceftriaxone retreatment | Antigen-clearance intervention (proxy) | Proxy directness: indirect; no antigen assay |
| Transient cognitive improvement at week 12 | Weak/transient signal, non-durable | Matches "disputed — weak" coding in `proposition:0020` |
| Relapse after antibiotic discontinuation | Possible antigen-re-drive OR self-sustaining loop | Ambiguous between `hypothesis:0002` and `hypothesis:0001` |
| No antigen marker measured | Target-engagement failure | Same load-bearing gap as Bhattacharjee2026 for SARS-CoV-2 |
| PICC line adverse events (26%) | Risk/benefit signal for IV antigen-clearance approach | Relevant to trial design for future Borrelia-clearance studies |

## Limitations

- **No antigen or pathogen-load assay.** The single most critical gap: the trial cannot speak to whether ceftriaxone cleared, reduced, or left unchanged any Borrelia-derived material. This renders the cognitive time-course uninterpretable as a test of the antigen-clearance hypothesis.
- **Small sample.** 37 enrolled patients (23 ceftriaxone, 14 placebo), yielding modest power for subgroup analyses; the secondary findings in high-fatigue/pain subgroups require replication.
- **Single antibiotic, single route.** Ceftriaxone targets extracellular forms; residual peptidoglycan fragments in macrophages (the tissue-reservoir mechanism in McClune2025) would not be reached by conventional beta-lactam exposure.
- **No tissue sampling.** Plasma or CSF Borrelia antigen — let alone tissue-macrophage pPG^Bb — was not assayed. The compartment most relevant to the McClune2025 mechanism (liver/Kupffer cells) was invisible to the trial.
- **IgG Western blot as inclusion criterion, not antigen-positivity enrichment.** Seropositivity confirms prior infection but does not select for patients who currently harbor residual antigen; this is the same enrichment failure noted for STOP-PASC and outSMART-LC under `proposition:0020`.
- **Unblinding hazard.** IV PICC line adverse events occurred at a 4× higher rate in the treatment arm; patients and clinicians may have been partially unblinded despite the double-masked design.
- **Case definition:** "Lyme encephalopathy" required IgG Western blot positivity plus objective cognitive impairment; this is a narrower PTLDS subgroup than fatigue-predominant PTLDS and is not directly comparable to post-COVID cognitive impairment in long COVID trials.

## Model / Tool Availability

Not applicable. This is a clinical RCT; no computational model, tool, or public dataset was released.

## Follow-up

- The parallel Klempner2001 PTLDS retreatment RCT (two concurrent trials: seropositive vs seronegative patients) is the companion study that together constitute the foundational PTLDS retreatment null literature; ingesting Klempner2001 alongside Fallon2008 would complete the Borrelia-retreatment evidence base for `proposition:0020`.
- The critical design gap — a retreatment trial that **measures Borrelia antigen (pPG^Bb or equivalent) before and after** and enriches on antigen-positive patients — remains unexecuted. McClune2025's r-mAb2G10 ELISA for pPG^Bb is the assay candidate.
- For the parallel question in long COVID, see `evidence-line:0054` (Bhattacharjee2026/PAX-LC), which is the closest existing analogue: it too administered an antigen-targeting agent and measured antigen levels, confirming non-clearance.
