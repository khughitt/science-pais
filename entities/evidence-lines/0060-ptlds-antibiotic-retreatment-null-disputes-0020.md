---
id: evidence-line:0060-ptlds-antibiotic-retreatment-null-disputes-0020
type: evidence-line
title: "PTLDS antibiotic-retreatment RCTs (Klempner2001/Krupp2003/Fallon2008/Berende2016) — no durable symptom rescue, no antigen target-engagement; weakly disputes antigen-clearance-rescues (consolidated Borrelia arm)"
status: active
stance: disputes
target: proposition:0020-antigen-clearance-rescues-established-pais
source: paper:Klempner2001
strength: weak
independence: independent
independence_group: ptlds-antibiotic-retreatment
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: interventional
related:
- proposition:0020-antigen-clearance-rescues-established-pais
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0002-antigen-clearance-rescues-symptoms
- interpretation:0011-t046-antigen-clearance-trials-ingestion
- discussion:0003-antigen-persistence-treatable-vs-fixed
source_refs:
- paper:Klempner2001
- paper:Krupp2003
- paper:Fallon2008
- paper:Berende2016
created: '2026-06-24'
updated: '2026-06-24'
---
# Evidence Line: PTLDS antibiotic-retreatment RCTs — the consolidated Borrelia clearance arm

## What this line shows

Four placebo-controlled RCTs of extended or repeat antibiotic therapy in **established** post-treatment
Lyme disease syndrome (PTLDS) collectively show **no durable symptom rescue**, providing the
cross-pathogen Borrelia parallel to the SARS-CoV-2 antiviral nulls (`evidence-line:0053`–`0055`):

- **Klempner2001 (NEJM):** two parallel RCTs (seropositive + seronegative), 90 d IV ceftriaxone → 60 d
  oral doxycycline vs placebo. **Null** on health-related QoL (SF-36); stopped at planned interim analysis
  for futility (~37% vs 40% improved). The foundational double-null.
- **Krupp2003 (STOP-LD):** 28 d IV ceftriaxone vs placebo for persistent severe fatigue. **Mixed** —
  subjective fatigue (FSS-11) improved, but the co-primary objective cognitive endpoint did not; authors
  declined to recommend retreatment given IV-antibiotic risks.
- **Fallon2008 (Lyme encephalopathy):** 10 wk IV ceftriaxone vs placebo. Broad cognitive improvement at
  week 12 (end of treatment) that was **not sustained at week 24** after antibiotics stopped; adverse-event
  rate ~26% (vs 7% placebo), mostly PICC-line events.
- **Berende2016 (PLEASE, NEJM):** largest PTLDS retreatment RCT (~280 randomized). After a shared 2-wk IV
  ceftriaxone induction, 12 wk of oral doxycycline or clarithromycin/hydroxychloroquine vs placebo gave
  **no benefit over placebo** on SF-36 PCS (P≈0.69); all arms improved similarly from baseline.

Together they **weakly dispute** `proposition:0020` (clearing persistent antigen rescues symptoms in
established PAIS) from a spirochaetal trigger — but they are uninterpretable for the **same structural
reason** as the long COVID antiviral nulls: none demonstrated antigen target-engagement.

## Why it is independent

`independence: independent` — relative to the SARS-CoV-2 clearance arm (`evidence-line:0053`–`0055`) this
body is genuinely independent: different trigger (spirochaetal *Borrelia* vs virus), different clearance
modality (β-lactam / tetracycline / macrolide antibiotics vs Mpro inhibitor or neutralizing mAb), different
cohorts and investigators. That cross-pathogen reach is the value this line adds.

**Why these four trials are coded as one line, not four** (`independence_group:
ptlds-antibiotic-retreatment`): internally they are *not* independent refutations — they share the same
intervention class (antibiotics) against the same trigger (Borrelia) and exhibit the same
target-engagement failure. Coding them as four separate disputing lines would falsely inflate the dispute
weight on a proposition whose honest status is "not yet adequately tested." One consolidated weak line
represents the body without over-counting it.

## Caveats / scope

**Weak**, and uninterpretable, for the reasons that make the entire established-disease clearance arm a
broken test of `proposition:0020`:

1. **No antigen target-engagement in any trial.** None measured residual *Borrelia* antigen,
   peptidoglycan (pPG^Bb), or DNA before/after treatment. Antibiotic is a *proxy* for clearing residual
   antigen; whether any pathogen-derived material was present, reduced, or eliminated is unknown — the
   antecedent of `proposition:0020` (antigen actually cleared) was never established.

2. **Mechanism mismatch with the fragment-persistence model — sharper here than for long COVID.** If the
   biologically active residue is *non-replicating* peptidoglycan fragment (McClune2025), antibiotics —
   which kill or inhibit *replicating* spirochaetes — have **no expected mechanism to degrade a retained
   non-viable fragment**. The Borrelia arm is therefore an even cleaner target-engagement failure than the
   LC arm: the vehicle is mechanistically incapable of clearing the hypothesized target, paralleling NMV/r
   failing to move Spike in Bhattacharjee2026/PAX-LC.

3. **No antigen-positive enrichment** (clinical/serologic entry only) and, in Berende2016, a **shared
   ceftriaxone induction** that makes the randomized comparison "more antibiotic vs less," not "antibiotic
   vs none."

4. **The two partial signals do not survive.** Krupp2003's FSS-11 fatigue benefit (subjective, single
   endpoint, possible partial unblinding) and Fallon2008's week-12 cognitive gain (lost by week 24) are
   transient/non-durable and not replicated by the two clean nulls (Klempner2001, Berende2016).

Per `discussion:0003` / `interpretation:0011`, these nulls **do not refute antigen persistence**
(`hypothesis:0002`): a regimen that may not have engaged — indeed cannot mechanistically engage — the
relevant antigen cannot test whether clearing it helps. The pattern is also consistent with the
`proposition:0021` fixed-risk-factor-at-onset reconciliation (antigen shapes onset, becomes non-operative
once the self-sustaining chronic state of `hypothesis:0001` is established, so late retreatment is
ineffective without disconfirming persistence). This line fills the Borrelia clearance arm flagged as
unfilled in `interpretation:0011`; the Coxiella/Q-fever retreatment parallel remains unfilled.
