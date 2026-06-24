---
id: paper:Krupp2003
type: paper
title: "Study and treatment of post Lyme disease (STOP-LD): a randomized double masked clinical trial"
status: active
ontology_terms:
  - post-treatment Lyme disease syndrome
  - randomized controlled trial
  - ceftriaxone
  - fatigue
  - cognitive function
  - antibiotic retreatment
  - post-acute infection syndrome
dataset_usage: []
datasets: []
source_refs:
- cite:Krupp2003
related:
- proposition:0020-antigen-clearance-rescues-established-pais
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- topic:antigen-pathogen-persistence
- interpretation:0011-t046-antigen-clearance-trials-ingestion
created: '2026-06-24'
updated: '2026-06-24'
---
# Study and treatment of post Lyme disease (STOP-LD): a randomized double masked clinical trial

- **Authors:** Lauren B. Krupp, Lauren G. Hyman, Roger Grimson, Patricia K. Coyle, Peter Melville, Sung Ahnn, Raymond Dattwyler, Brian Chandler
- **Year:** 2003
- **Journal:** Neurology, vol. 60, no. 12, pp. 1923–1930
- **DOI:** 10.1212/01.wnl.0000071227.23769.9e
- **BibTeX key:** Krupp2003
- **Source:** LLM knowledge (paywalled; 2003 classic, >20 years old, foundational PTLDS RCT cited in every review of the field; Crossref count 346 [UNVERIFIED: may be undercounted relative to Google Scholar])

## Key Contribution

STOP-LD is one of the earliest double-blind placebo-controlled RCTs of IV antibiotic retreatment for post-treatment Lyme disease syndrome (PTLDS). The trial tested whether a 28-day course of IV ceftriaxone improved outcomes in patients with persistent severe fatigue following adequately treated Lyme disease. The headline result was **mixed**: fatigue severity improved significantly in the ceftriaxone arm (primary co-endpoint: Fatigue Severity Scale, FSS-11), but objective cognitive function did **not** improve (primary co-endpoint: mental-speed test). The authors explicitly concluded that the fatigue benefit did not justify the risks of IV antibiotic therapy, making STOP-LD an important early null-to-equivocal anchor in the PTLDS retreatment literature.

## Methods

| Feature | Detail |
|---|---|
| Design | Randomized, double-blind, placebo-controlled trial |
| Intervention | IV ceftriaxone 2 g/day × 28 days vs IV placebo |
| Population | Adults with confirmed prior treated Lyme disease and persistent severe fatigue (FSS score ≥4.5) [UNVERIFIED: exact entry FSS threshold] |
| Sample size | n = 55 [UNVERIFIED: enrollment figure; range cited in literature is ~55–78 across trial phases; 55 is the most commonly cited intent-to-treat n for the primary analysis] |
| Co-primary outcomes | (1) Fatigue severity: FSS-11 (Fatigue Severity Scale, 11-item subjective self-report); (2) Cognitive function: objective mental-speed computer test (processing-speed composite) |
| Secondary outcomes | [UNVERIFIED: additional neuropsychological and quality-of-life measures] |
| Setting | Academic center; Stony Brook University [UNVERIFIED] |
| Follow-up | Assessed at end of treatment and at later time points [UNVERIFIED: specific windows] |
| Antigen/pathogen marker measured | None — no persistent Borrelia antigen, peptidoglycan, DNA, or other residual-infection biomarker was measured at baseline or follow-up |

## Key Findings

1. **Fatigue (FSS-11) — positive (subjective endpoint):** Fatigue severity improved significantly in the ceftriaxone arm compared with placebo on the FSS-11 [UNVERIFIED: exact effect size, p-value]. This was a self-reported, subjective measure.

2. **Cognitive function (mental-speed test) — null (objective endpoint):** The objective mental-speed computer test showed **no significant difference** between ceftriaxone and placebo. This was the co-primary outcome with equal billing.

3. **Mixed/partial-positive overall verdict:** With one of two co-primary endpoints positive (the subjective one) and the other null (the objective one), the trial is canonically described as having a mixed result — not a clean benefit.

4. **Authors' caution:** The investigators explicitly stated that the fatigue benefit did not justify the risks associated with IV antibiotic therapy (including catheter-related complications, biliary disease, and the broader risks of prolonged IV access), effectively declining to recommend retreatment.

5. **No antigen clearance demonstrated or measured:** The trial did not assess whether ceftriaxone cleared any persistent Borrelia antigen, peptidoglycan fragments, or other residual infection markers. The assumed mechanism (that retreatment would clear residual Borrelia and thereby rescue symptoms) was never verified or refuted — the biological premise was a proxy assumption, not a measured variable.

## Relevance

STOP-LD is one of the PTLDS antibiotic-retreatment nulls that constitute the Borrelia-clearance arm of the evidence base for `proposition:0020` (clearing persistent antigen rescues symptoms in established PAIS). Its analytical role in this project is coded as **disputing (weak, uninterpretable)** `proposition:0020`, in parallel with the long COVID antiviral-retreatment nulls (Geng2024/STOP-PASC, Bhattacharjee2026/PAX-LC, Peluso2026/outSMART-LC).

The critical interpretive constraint — shared across all trials in this lineage — is that STOP-LD **never measured antigen clearance**. Ceftriaxone is a proxy for clearing residual Borrelia/Borrelia fragments, not a demonstration of it. The trial therefore cannot distinguish:
- "No residual antigen existed to clear" (patients lacked the target)
- "Ceftriaxone cleared antigen but symptoms persisted anyway" (antigen was cleared; the mechanism is wrong)
- "Ceftriaxone failed to clear residual Borrelia peptidoglycan" (the fragmented, non-replicating form now characterized by McClune2025 may be ceftriaxone-insensitive, since beta-lactams target cell-wall synthesis in replicating bacteria)

The fatigue signal on the FSS-11 is a single subjective endpoint that was not replicated on the objective co-primary, and the authors themselves declined to endorse retreatment. The signal's durability beyond the treatment period is uncertain [UNVERIFIED: whether follow-up data showed persistence of fatigue benefit].

Links to project entities:
- `proposition:0020-antigen-clearance-rescues-established-pais` — this trial provides a weak, uninterpretable disputing line (Borrelia-trigger arm; adds cross-pathogen echo to the long COVID antiviral nulls)
- `hypothesis:0002-tissue-reservoir-antigen-fragment` — the pPG^Bb fragment persistence model (McClune2025) is mechanistically relevant: if the biologically active residue is a non-replicating peptidoglycan fragment rather than viable Borrelia, retreatment with a cell-wall-synthesis-targeting beta-lactam would have no expected clearing effect regardless of whether the fragment drives symptoms
- `interpretation:0011-t046-antigen-clearance-trials-ingestion` — explicitly named STOP-LD as one of the Borrelia retreatment nulls awaiting ingestion; this summary completes that ingestion
- `question:0002-antigen-clearance-rescues-symptoms` — STOP-LD is a broken test of this question for the same structural reason as the long COVID trials: no target-engagement demonstrated

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| IV ceftriaxone retreatment | Proxy for antigen clearance (indirect) | `proxy_directness: indirect`; the assumed mechanism (clearing residual Borrelia) was never verified |
| FSS-11 (Fatigue Severity Scale) | Subjective patient-reported outcome | Analogous to PROMIS fatigue in STOP-PASC; same vulnerability to placebo/expectation effects |
| Objective mental-speed test | Objective cognitive endpoint | Null on this measure; mirrors long COVID trials' pattern of subjective > objective |
| Persistent severe fatigue post-treated Lyme | PTLDS / established PAIS | IDSA-proximate case definition |
| No biomarker of residual infection measured | No target-engagement demonstrated | The project's load-bearing column for cataloguing anti-antigen trials (`discussion:0003`) |

## Limitations

1. **No antigen-clearance measurement (fatal interpretive gap):** Neither residual Borrelia burden, Borrelia peptidoglycan (pPG^Bb), Borrelia DNA, nor any surrogate of ongoing infection was measured. The trial cannot test whether clearing antigen rescues symptoms — it only tests whether giving ceftriaxone to fatigued post-Lyme patients changes outcomes. This is the same structural flaw as in the long COVID antiviral trials.

2. **Mixed primary endpoint result — one subjective positive, one objective null:** The FSS-11 positive does not constitute validated evidence of treatment efficacy when its co-primary (objective cognitive test) is null. Differential improvement on subjective vs. objective measures is a recognized confound in unblinding-susceptible trials.

3. **Partial unblinding risk:** IV ceftriaxone has recognizable side effects (GI, biliary); patients may not have been fully blinded, creating expectation bias on subjective ratings. [UNVERIFIED: extent of unblinding assessed]

4. **Sample size:** n ~55 [UNVERIFIED] limits power to detect modest effects and renders subgroup findings unreliable.

5. **Fatigue benefit not replicated in the objective domain and not clearly durable:** Whether the fatigue improvement persisted after treatment ended is unclear from the published record [UNVERIFIED]. The subsequent larger Klempner2001 trial (NEJM) was null across all outcomes; Fallon2008 showed some cognitive benefit with IV ceftriaxone but then relapse — the field's retreat trials as a whole do not support durable benefit.

6. **Beta-lactam mechanism mismatch with fragment persistence model:** If the biologically active residue is pPG^Bb (non-replicating, cell-wall-derived; McClune2025), ceftriaxone — which works by inhibiting cell-wall synthesis in replicating bacteria — has no expected clearing mechanism. This is a post-hoc mechanistic caveat unavailable to the original authors, but it matters for interpreting the null.

7. **Case definition specificity:** The entry criterion was persistent severe fatigue post-Lyme; it is not clear whether patients had the full PTLDS clinical syndrome or were selected solely on fatigue severity. [UNVERIFIED: full inclusion/exclusion criteria]

## Model / Tool Availability

Not applicable — no computational model, tool, or reusable dataset released.

## Follow-up

- **Ingestion into the evidence graph:** Add a `evidence-line` entry to `proposition:0020` for this trial (Borrelia-clearance arm; stance: disputes; strength: weak; reason: no target engagement, mixed primary endpoint).
- **Cross-pathogen pattern:** STOP-LD + Klempner2001 + Fallon2008 (+ Berende2016/PLEASE) constitute the PTLDS retreatment null cluster — the bacterial-trigger echo of the SARS-CoV-2 antiviral retreatment nulls. Together they generalize the "established-disease clearance proxy null" pattern beyond one pathogen.
- **Read next:** Klempner2001 (NEJM; the larger, fully null PTLDS retreatment trial) and Fallon2008 (IV ceftriaxone → cognitive benefit → relapse pattern) for a complete Borrelia-clearance evidence arm.
- **Mechanistic note:** McClune2025 (pPG^Bb fragment persistence) provides the hypothesis-level account of why beta-lactam retreatment would not clear the biologically active residue — a link worth encoding on the evidence-line for this trial.
