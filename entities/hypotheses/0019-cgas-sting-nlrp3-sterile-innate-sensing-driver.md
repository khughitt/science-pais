---
id: hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
kind: hypothesis
title: Upstream cytosolic nucleic-acid sensing (cGAS-STING / NLRP3) as a sterile self-sustaining
  PAIS driver
status: proposed
phase: candidate
source_refs:
- cite:Sun2013
- cite:Domizio2022
- cite:Christ2018
- cite:Saeed2014
origins:
- type: user
  date: '2026-07-10'
- type: assistant
related:
- question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i
- question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
created: '2026-07-10'
updated: '2026-07-10'
added_by: user
---
# Hypothesis: Upstream cytosolic nucleic-acid sensing (cGAS-STING / NLRP3) as a sterile self-sustaining PAIS driver

## Organizing Conjecture

The persistent type-I IFN and IL-1β/IL-18 signatures repeatedly documented in PAIS are sustained by **cytosolic nucleic-acid and inflammasome sensing that operates without ongoing viral replication** — a *sterile* self-amplifying loop, not a response to residual antigen. Two partly-separable innate sensors are proposed as the proximal molecular drivers sitting **upstream** of the downstream outputs the project already tracks (IL-6 / JAK-STAT exhaustion in `hypothesis:0003`; the shared maintenance state in `hypothesis:0001`): (a) cGAS → STING → TBK1 → IRF3 → type-I-IFN, engaged by mitochondrial and dying-cell DNA; and (b) NLRP3 → caspase-1 → IL-1β/IL-18 → gasdermin-D → pyroptotic DAMP release, which re-feeds both sensors. This frame is deliberately *actionable*: it predicts that sensor-selective agents (STING/cGAS antagonists; NLRP3-selective inhibitors such as MCC950 or colchicine) produce effects that are **pharmacologically separable** from JAK/TNF blockade, and that the loop is a candidate **cross-trigger** step because mtDNA release, EBV reactivation, and Borrelia-induced DNA damage all converge on it.

## Proposition Bundle

### Core Propositions

- **P1 (sterile IFN-I driver).** Cytosolic-DNA sensing via cGAS-STING initiates and *sustains* the persistent type-I IFN signature in PAIS independent of active viral replication. (`question:0023`; `mechanistic_narrative`.)
- **P2 (self-amplifying IL-1β loop).** An NLRP3 → caspase-1 → IL-1β/IL-18 → gasdermin-D → DAMP-release chain forms a self-amplifying inflammatory loop that persists without viremia. (`question:0024`; `mechanistic_narrative`.)
- **P3 (pharmacological separability).** Sensor-selective inhibition (STING/cGAS antagonists; NLRP3-selective MCC950/colchicine) yields a clinical effect *separable* from JAK/TNF blockade — the decisive discriminating prediction. (`causal_effect`.)

### Supporting Or Auxiliary Propositions

- **P4 (cross-trigger convergence).** The same sensing hub is engaged across SARS-CoV-2 (mtDNA), EBV reactivation, and Borrelia DNA damage, making it a candidate shared cross-trigger node consistent with `hypothesis:0001`.
- **P5 (DAMP cross-feed).** Gasdermin-D pore–driven DAMP release (mtDNA, HMGB1, ATP) re-engages cGAS-STING and NLRP3, coupling P1 and P2 into one loop and, potentially, feeding myeloid retraining.

## Current Uncertainty

Support is **general-immunology-grounded but PAIS-inferential**. Sun2013 establishes the cGAS sensor and Domizio2022 shows SARS-CoV-2 mtDNA → cGAS-STING → IFN-I immunopathology — but Domizio2022 characterizes *acute/severe* COVID endothelial immunopathology; the extrapolation to *persistent* IFN-I in PAIS (the actual claim) is untested. Christ2018 grounds NLRP3 as a required upstream inducer of durable sterile myeloid reprogramming, but in a Western-diet model, not PAIS. Critically, the appealing "chronic sensor-locus chromatin imprint" sub-idea was **sought and not found** in the primary epigenomic literature (t112, 2026-07) and has been severed from the trained-immunity axis. Whether cGAS-STING/NLRP3 is *upstream seed* or *downstream output* of any myeloid reprogramming in PAIS is unresolved, and no PAIS system has tested the loop directly.

## Predictions

**Strong / discriminating:**
- Sensor-selective inhibition (STING antagonist; NLRP3-selective MCC950/colchicine) improves PAIS endpoints in a manner **not reproduced by, and additive to,** JAK/TNF blockade (P3).
- Persistent IFN-I / ISG activity in PAIS co-localizes with markers of active cytosolic-DNA sensing (cGAMP, phospho-TBK1/IRF3) rather than markers of ongoing viral replication (P1).
- Elevated, persistent IL-1β/IL-18 and gasdermin-D cleavage products track PAIS status and predict response to NLRP3-selective therapy (P2).

**Weaker / corollaries:**
- The sensing signature recurs across SARS-CoV-2, EBV-reactivating, and Borrelia triggers (P4).
- Circulating DAMPs (mtDNA, HMGB1) correlate with both IFN-I and inflammasome readouts (P5).

## Falsifiability

Confidence would be materially reduced if:
- Persistent IFN-I in PAIS tracks residual replication-competent virus or antigen rather than sterile cytosolic-DNA sensing.
- NLRP3-selective inhibition (adequately dosed, target-engagement-confirmed) shows **no** effect separable from JAK/TNF blockade.
- IFN-I and IL-1β activity in established PAIS are *not* elevated/persistent, or are fully explained by an ongoing-antigen model (`hypothesis:0002`).
- The two sensors prove strictly redundant with the IL-6/NF-κB axis (no pharmacological separability at any dose).

## Promotion criteria

Promote from `candidate` to `active` when **either**: (1) a PAIS cohort demonstrates active cGAS-STING or NLRP3 sensing (cGAMP / phospho-TBK1 / cleaved gasdermin-D or IL-18 maturation) that is *persistent* and dissociated from replication markers; **or** (2) a sensor-selective interventional signal (STING antagonist or NLRP3-selective inhibitor) shows a PAIS effect not reproduced by JAK/TNF blockade — i.e. proposition P3 receives at least suggestive interventional support. Absent either, the frame stays a candidate that sharpens `question:0006` (the "what drives IFN-I" gap) without a committed claim.

## Supporting Evidence

- **Sun2013 (literature):** canonical discovery that cytosolic dsDNA drives cGAS → cGAMP → STING → TBK1 → IRF3 → type-I-IFN independent of replication — grounds the sensor for P1.
- **Domizio2022 (literature):** SARS-CoV-2 induces endothelial mtDNA release activating cGAS-STING; STING inhibition (H-151) reduced IFN-I immunopathology *without* affecting viral replication — grounds P1's sterile-driver logic (acute context).
- **Christ2018 (literature):** NLRP3-dependent central myeloid training under a sterile stimulus (`Nlrp3⁻/⁻` abolishes GMP expansion) — grounds NLRP3 as a required upstream inducer of durable reprogramming (P2/P5, analogy).

## Disputing Evidence

- **Trained-immunity locus grounding NOT found (t112, 2026-07):** no primary study reports chromatin accessibility / activating marks at cGAS/STING(TMEM173)/NLRP3/IL-1β loci in trained myeloid cells; Christ2018's ATAC-seq opens *Tet2/Tlr4*, and Saeed2014's signature is metabolic — so the "chronic sensor-locus imprint" mechanism is unsupported.
- No PAIS-specific test of either sensing loop exists; all persistence claims are extrapolated from acute or non-PAIS models.

## Evidence Needed To Shift Belief

- **Most efficient upward:** persistent, replication-dissociated cGAS-STING or NLRP3 activation markers measured directly in an established-PAIS cohort (P1/P2).
- **Most efficient downward:** IFN-I / IL-1β activity in PAIS explained by ongoing antigen (`hypothesis:0002`) or fully collinear with the IL-6/NF-κB axis.
- **Most discriminating next test:** a sensor-selective intervention (NLRP3-selective MCC950/colchicine or a STING antagonist) with target-engagement confirmation and PAIS endpoints, benchmarked against JAK/TNF blockade (P3).

## Related Work

- `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i` and `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1` — the two orphan mechanism questions this hypothesis homes.
- `hypothesis:0003-immune-exhaustion-feedback` — the downstream IL-6/JAK-STAT/exhaustion output for which this names the upstream sterile sensor; `question:0006-jak-stat-il6-driver-vs-marker` is the adjacent driver-vs-marker gap.
- `hypothesis:0001-shared-dysregulated-attractor` — parent frame; this is a candidate cross-trigger maintenance node (P4).
- `topic:innate-immune-memory-trained-immunity-in-pais` — related myeloid-reprogramming topic (the sensor-locus-imprint sub-branch is severed pending primary evidence).
- Papers: Sun2013, Domizio2022, Christ2018, Saeed2014.
