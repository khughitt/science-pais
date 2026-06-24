---
id: evidence-line:0060-krupp2003-stop-ld-ceftriaxone-mixed-disputes-0020
type: evidence-line
title: "Krupp2003 STOP-LD — 28-day IV ceftriaxone in PTLDS: subjective fatigue improved, objective cognition null, no antigen-clearance assay; weakly disputes antigen-clearance-rescues (Borrelia arm)"
status: active
stance: disputes
target: proposition:0020-antigen-clearance-rescues-established-pais
source: paper:Krupp2003
strength: weak
independence: independent
independence_group: stop-ld-ceftriaxone-ptlds
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: interventional
related:
- proposition:0020-antigen-clearance-rescues-established-pais
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- interpretation:0011-t046-antigen-clearance-trials-ingestion
source_refs:
- paper:Krupp2003
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: Krupp2003 (STOP-LD) — IV ceftriaxone retreatment in established PTLDS

## What this line shows

STOP-LD (n ~55 [UNVERIFIED]) randomized patients with persistent severe fatigue after treated Lyme disease
to IV ceftriaxone 2 g/day × 28 days vs IV placebo. The result was **mixed**: fatigue (FSS-11, subjective
self-report) improved significantly in the ceftriaxone arm, but the co-primary objective cognitive
endpoint (mental-speed computer test) showed **no significant benefit**. The authors explicitly stated the
fatigue benefit did not justify the risks of IV antibiotic therapy. This **weakly disputes**
`proposition:0020` (antigen clearance rescues symptoms in established PAIS) — but is uninterpretable for
the same structural reason as the long COVID antiviral nulls: **no antigen target-engagement was
demonstrated or measured**.

## Why it is independent

`independence: independent` — Stony Brook PTLDS cohort [UNVERIFIED: institution], distinct from Klempner2001
(NEJM, multi-site) and Fallon2008 (Columbia). Also independently distinct from the SARS-CoV-2 retreatment
nulls (0053–0055): different trigger (Borrelia vs SARS-CoV-2), different pathogen class (spirochaete vs
virus), different clearance vehicle (beta-lactam antibiotic vs Mpro inhibitor or neutralizing mAb).
This adds the **cross-pathogen Borrelia arm** to the established-disease-clearance-proxy-null pattern.

## Caveats / scope

**Weak**, and uninterpretable, for the following structural reasons:

1. **No antigen-clearance assay:** The trial measured neither residual Borrelia burden nor Borrelia
   peptidoglycan (pPG^Bb) nor Borrelia DNA before or after treatment. Ceftriaxone is a *proxy* for
   clearing residual Borrelia; whether any Borrelia-derived material was present, reduced, or eliminated
   is unknown. The antecedent of `proposition:0020` (antigen actually cleared) was never established.

2. **Beta-lactam mechanism mismatch with fragment persistence model:** If the biologically active
   residue in PTLDS is non-replicating pPG^Bb (as characterized in McClune2025), ceftriaxone — which
   inhibits cell-wall synthesis in *replicating* bacteria — has no expected clearing mechanism. Even if
   residual fragments were present, this vehicle may have been incapable of removing them, analogous to
   NMV/r failing to clear Spike in Bhattacharjee2026/PAX-LC.

3. **Mixed primary endpoint:** One of two co-primary outcomes (subjective fatigue, FSS-11) was positive;
   the other (objective cognition) was null. A positive on the subjective endpoint and null on the
   objective endpoint is a pattern consistent with partial unblinding (IV ceftriaxone has recognizable
   side effects), expectation effects, or modest placebo response in fatigue — not a clean treatment
   signal.

4. **Authors declined to recommend retreatment:** The investigators themselves concluded the benefit did
   not outweigh IV antibiotic risks — an important calibration cue against over-reading the FSS-11 signal.

5. **Fatigue benefit durability unknown [UNVERIFIED]:** Whether the fatigue improvement persisted after
   the 28-day course ended is unclear from the primary publication; the subsequent PTLDS retreatment
   literature (Klempner2001 — fully null; Fallon2008 — cognitive benefit then relapse) provides no
   durable signal.

Per `discussion:0003`, this null **does not refute antigen persistence** (`hypothesis:0002`) — a drug
that may not have cleared the relevant antigen cannot test whether clearing antigen helps. This line
extends the pattern established in 0053–0055 (SARS-CoV-2 antiviral nulls) to the Borrelia-trigger arm,
filling one of the three flagged gaps in `interpretation:0011`.
