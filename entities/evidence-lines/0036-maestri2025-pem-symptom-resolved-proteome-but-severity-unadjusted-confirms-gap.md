---
id: "evidence-line:0036-maestri2025-pem-symptom-resolved-proteome-but-severity-unadjusted-confirms-gap"
type: "evidence-line"
title: "Maestri2025 STOP-PASC shows PEM has a symptom-resolved plasma-proteome signature within long COVID, but the per-symptom models are severity-unadjusted, so the decisive q0015 test stays open"
status: "active"
stance: "supports"
target: "proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode"
source: "paper:Maestri2025"
strength: "weak"
independence: "independent"
independence_group: "maestri2025-stop-pasc-cohort"
evidence_role: "proxy_support"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode"
  - "question:0015-does-pem-requirement-improve-cross-study-comparability"
  - "interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "task:t044"
source_refs:
  - "paper:Maestri2025"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Maestri2025 — PEM has a symptom-resolved plasma-proteome signature, but severity-unadjusted

## What this line shows

Maestri2025 (STOP-PASC systems immunology, n = 152 long COVID, Olink Explore HT 5400-plex) is the
first cohort to map plasma proteins onto **post-exertional malaise (PEM) severity** alongside six other
patient-reported outcomes (PROs) on a single platform. PEM carries a **symptom-resolved** proteomic
association profile — **IL1RL1 (ST2 / IL-33 receptor) and IL1R2 negatively associated with PEM** —
that differs from the fatigue/cardiovascular signature (leptin, factor VII, factor XII, all positive)
and the dyspnea signature (CD38, negative). IL1RL1/IL1R2 are soluble decoy IL-1-family receptors, so
the PEM signal is mechanistically distinct from the leptin/coagulation fatigue axis. This is a new
**within-trigger, blood-proteome** datapoint consistent with `proposition:0011`'s core reading — the
objective correlate of PEM is **specific, not a single undifferentiated shared signal** — extending it
from the cross-trigger muscle/whole-body endpoints (Keller2014 / Gattoni2025 / Appelman2024) to the
blood proteome within long COVID [@Maestri2025].

## Why it is independent

A distinct cohort (STOP-PASC RCT participants) and a distinct assay (5400-plex plasma proteomics vs
whole-body CPET and muscle biopsy in the other `proposition:0011` lines); its own
`independence_group: maestri2025-stop-pasc-cohort`. It adds a fourth, orthogonal endpoint (circulating
proteome) to the proposition's endpoint-specificity argument [@Maestri2025].

## Caveats / scope

`proxy_support`, **weak** — deliberately not stronger, because this is a **near-miss on the decisive
`question:0015` test**, not a passing of it:

1. **Severity-unadjusted.** Each protein × symptom association is a **univariate proportional-odds
   logistic regression on the ordinal Likert severity of one symptom, adjusted only for batch plate** —
   no covariate for overall illness/fatigue severity, age, sex, or BMI, and the seven symptoms are
   modeled separately. Because the symptoms are positively intercorrelated (110 proteins track a shared
   trend across ≥ 3 PROs), a protein "associated with PEM" is **not separated from the shared severity
   axis**. The discriminant pattern (different top proteins per symptom) is *consistent with* a
   PEM-specific signal but does **not** establish that it survives severity adjustment — exactly the
   confound q0015 targets [@Maestri2025].
2. **PEM ascertainment is a single self-report Likert item**, not a validated PEM instrument (DSQ-PEM)
   or provocation/CPET.
3. **Cross-sectional**; the authors explicitly disclaim causal direction (immune feature driving PRO vs
   resulting from it).
4. **Treatment-trial population**, possibly unrepresentative of broader long COVID; no
   PEM-negative-matched-for-severity arm.
5. **Not a between-group PEM+ vs PEM− contrast** — it is a continuous-severity association, so it does
   not instantiate the group design `task:t025`/`question:0015` specified.

The decisive severity-adjusted refit would require the **individual-level protein × multi-symptom
matrix**, which is gated ("Olink data available upon publication"; analysis repo not yet created as of
2026-06). This line therefore **supports `proposition:0011` weakly while confirming the `question:0015`
gap remains open** (recorded in `interpretation:0007`).
