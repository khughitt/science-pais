---
id: interpretation:0009-t049-sfn-cross-syndrome-ingestion
kind: interpretation
title: 't049 cross-syndrome SFN ingestion: structural lesion documented across triggers
  but non-length-dependent pattern asserted more than measured; primary-dysautonomia
  controls universally absent'
status: active
source_refs: &id001
- paper:Oaklander2022
- paper:Joseph2021
- paper:Adler2024
- paper:Limongelli2026
- paper:Walitt2024
- paper:deSa2026
- paper:Stein2025
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0004-convergent-small-fiber-neuropathy-substrate
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0016-pais-sfn-autoimmune-causation
- proposition:0017-pais-sfn-cross-trigger-convergence
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- proposition:0019-pais-sfn-immunomodulation-modifies-lesion-trajectory
- topic:post-infectious-dysautonomia-and-autoimmunity
- topic:measurement-ascertainment-artifacts-in-pais
- task:t049
created: '2026-06-24'
updated: '2026-06-24'
input: *id001
prior_interpretations: []
relations: []
---

# Interpretation: t049 cross-syndrome SFN ingestion — structural lesion documented across triggers but the non-length-dependent pattern is asserted more than measured; primary-dysautonomia controls universally absent

## Verdict

**Verdict:** [~] Mixed — P1 (structural lesion) and P4 (cross-trigger convergence) are now **documented** across long COVID, ME/CFS, and PTLDS; P2 (non-length-dependent pattern) is **asserted more than measured** (only one clean paired-site fraction, and it is post-*vaccine*); the autoimmune-causation core (`proposition:0016`) is causally anchored for long COVID (deSa2026) but null in the best ME/CFS cohort (Walitt2024); and **no study supplies primary-dysautonomia controls** — h0007's promotion criterion #1 remains unmet by the existing literature.

## Findings Summary

This ingestion coded seven papers (five corpus-resident: Adler2024, Limongelli2026, Walitt2024, deSa2026, Stein2025; two newly ingested: Oaklander2022, Joseph2021) into eleven evidence-lines (`evidence-line:0038`–`0048`) across the six h0007 propositions.

- **P1 — lesion exists (`proposition:0014`): supported across triggers, with one rigorous null.** Long COVID: Oaklander2022 (n=17 prolonged long COVID; paired distal+proximal biopsy; 62.5% [10/16] distal IENFD abnormal; SFN the most common objective abnormality) — `evidence-line:0038`. ME/CFS: Joseph2021 (n=160; **31%** met SFN threshold; the largest ME/CFS skin-biopsy series) — `evidence-line:0039`. PTLDS: Adler2024 (cited series, 10/10 PTLDS abnormal IENFD/SGNFD). Post-vaccine PASC: Limongelli2026 (19/21 biopsied = 90% reduced fiber density). **Counterweight:** Walitt2024 — the NIH PI-ME/CFS cohort (n=17, unanimous expert adjudication) found **no small-fiber-nerve-density difference** vs controls (explicit null, Suppl. S22) — `evidence-line:0040`.
- **P2 — non-length-dependent pattern (`proposition:0015`): thinly documented.** The only clean paired-site NLD *fraction* is Limongelli2026's **33%** on calf+thigh biopsy — but that cohort is post-*vaccine*, not post-infection (`evidence-line:0041`). Oaklander2022's paired-site near-parity (62.5% distal / ~50% proximal abnormal) is *consistent with* widespread/proximal involvement but **no per-patient NLD fraction was reported** (`evidence-line:0042`, weak). Joseph2021 — the largest study — was **distal-only** and cannot assess P2 at all. Adler2024 asserts NLD as a "final common pathway" but does not measure it in PTLDS.
- **P4 — cross-trigger convergence (`proposition:0017`): breadth supported, standardization absent.** SFN is now documented in four trigger contexts (long COVID, ME/CFS, PTLDS, post-vaccine PASC) — `evidence-line:0043` (Joseph, ME/CFS leg), `evidence-line:0044` (Adler, PTLDS leg + explicit cross-syndrome framing), with the long-COVID leg carried by Oaklander2022 (coded at P1/P2). But the protocols are heterogeneous (paired vs distal-only vs narrative review), there is **no head-to-head standardized comparison**, and the ME/CFS leg is internally contested (Joseph 31% positive vs Walitt null).
- **P3 / 0016 — immune-mediated: causal for LC, null for ME/CFS.** deSa2026 is the strong anchor: LC-patient IgG passive-transferred to mice **reduces intraepidermal nerve-fiber volume/count** (causal demonstration that autoantibodies produce SFN), donor-symptom-matched — `evidence-line:0045`. Against it, Walitt2024 found **no uniform autoantibody signal** in PI-ME/CFS — `evidence-line:0046`.
- **0018 — anti-GPCR pathogenicity: barely supported.** Stein2025 (β2-adrenergic-receptor-AB-selected immunoadsorption) gives indirect support via anti-GPCR selection + depletion-associated autonomic improvement (`evidence-line:0048`, weak). But the strongest *causal* autoantibody evidence (deSa2026) targeted **non-GPCR** antigens (MED20/USP5) and **did not recapitulate the cardiovascular-autonomic phenotype** — so anti-GPCR-specific pathogenicity of the autonomic lesion remains essentially unproven.
- **0019 — immunomodulation modifies trajectory: proof-of-concept only.** Stein2025: repeated immunoadsorption in β2-AR-AB-elevated post-COVID ME/CFS, **70% responders**, COMPASS-31 autonomic improvement (orthostatic/secretomotor/GI), sustained to 6 months — `evidence-line:0047`. Uncontrolled.

## Evidence Quality

All seven sources are `literature_evidence`; deSa2026's passive-transfer arm is the only *experimental* (causal) identification, the rest observational. Independence is good — seven distinct cohorts/designs (Oaklander INSPIRE, Joseph iCPET referral, Walitt NIH intramural, Limongelli Genova post-vaccine, Adler narrative review, deSa MY-LC + mouse transfer, Stein Charité immunoadsorption), so convergence on P1 is not single-group. Power is the dominant weakness: Oaklander (n=17) and Walitt (n=17) are both small, so the P1 support *and* its null counterweight are each underpowered. Joseph (n=160) is the one well-powered structural study but is distal-only [@Oaklander2022; @Walitt2024; @Joseph2021]. This is exploratory/observational throughout — no confirmatory powered SFN study with controls exists.

## Data Quality Checks

No data-quality anomalies in the coded sources. Two methodological flags drive the verdict rather than data errors: (1) **biopsy-protocol non-uniformity** — distal-only (Joseph) vs paired distal+proximal (Oaklander, Limongelli) — directly gates whether P2 is even assessable; (2) **selection/ascertainment** — Limongelli biopsied only 30% of its cohort, Stein excluded the severe housebound, Joseph's controls are normal-iCPET referrals (not population controls) [@Limongelli2026; @Stein2025; @Joseph2021]. These are the `topic:measurement-ascertainment-artifacts-in-pais` concerns made concrete.

## Proposition-Level Updates

- `proposition:0014` (P1): **net supported** — three independent supports (Oaklander, Joseph, + Limongelli/Adler) vs one rigorous null (Walitt). Belief should rise to "documented but prevalence is protocol- and cohort-sensitive," not "established universal."
- `proposition:0015` (P2): **weakly supported, under-determined** — one moderate (Limongelli, post-vaccine) + one weak (Oaklander, near-parity) support; the largest study cannot test it. The non-length-dependent claim is the **least-measured** leg and the project should treat it as open.
- `proposition:0016` (P3 core): **split** — causally supported for long COVID (deSa2026), disputed for ME/CFS (Walitt2024). Immune mediation is trigger-specific in the current evidence, not pan-PAIS.
- `proposition:0017` (P4): **supported in breadth, not in standardization** — convergence of the *finding* across ≥3 triggers; convergence of a *standardized substrate* unestablished.
- `proposition:0018` (anti-GPCR pathogenicity): **remains the weakest leg** — one weak indirect support (Stein); the best causal autoantibody data point away from GPCR targets and away from the autonomic axis.
- `proposition:0019` (immunomodulation): **proof-of-concept support** (Stein) — but endpoints are symptomatic/autonomic, **not a measured IENFD/lesion trajectory**, so the structural claim it is meant to underwrite is untouched.

## Hypothesis-Level Implications

h0007 moves from "literature-only, uncoded" to "literature-coded, partially supported." The end-organ-lesion frame (P1) is the strongest leg and now has real cross-trigger footing. But the two claims that make h0007 *distinctive* — the **non-length-dependent** signature (P2, what separates it from metabolic SFN) and **autoimmune causation** (P3, what makes it "autoimmune-SFN") — are exactly the under-supported legs: P2 is barely measured, and P3 is causal only for long COVID. The hypothesis is therefore better described today as "a peripheral small-fiber lesion recurs across PAIS triggers" than as "a *non-length-dependent autoimmune* SFN." Promotion to `active` should not occur on this evidence: criterion #1 (a standardized cross-syndrome study **with primary-dysautonomia controls**) is unmet by every paper ingested.

## Evidence vs. Open Questions

`question:0004` (convergent SFN substrate): **partially addressed** — the substrate is documented across triggers, but the specific question it poses (is it a *distinct, non-length-dependent* substrate vs primary dysautonomia?) is **not answered**, because no study includes primary-dysautonomia controls or a uniform paired-site protocol. `question:0009` (functional autoantibodies drive dysautonomia): **advanced** — deSa2026 (causal IgG→SFN) and Stein2025 (anti-GPCR depletion→autonomic improvement) both push it forward, but neither closes the anti-GPCR-specific autonomic-pathogenicity gap.

## New Questions Raised

1. **(P2, the central gap)** Does a paired proximal+distal skin-biopsy protocol show a genuinely non-length-dependent IENFD pattern in *infection*-triggered PAIS at a higher rate than in length-dependent/metabolic SFN? — high priority; suggested evidence: a single-protocol paired-site study. (Candidate to formalize as a new question if not folded into `question:0004`.)
2. Why does the most rigorously adjudicated ME/CFS cohort (Walitt2024) show **no** SFN while a large referral cohort (Joseph2021) shows 31%? Ascertainment, severity, or protocol? — bears on P1/P4 and `topic:measurement-ascertainment-artifacts-in-pais`.
3. Are the *autonomic* (cardiovascular) small fibers specifically autoantibody-targeted, given deSa2026's transfer reproduced somatic-pain SFN but **not** the cardiovascular-autonomic phenotype? — the unresolved core of 0018.

## Limitations & Residual Uncertainty

The evidence base is small-n and protocol-heterogeneous; the two underpowered cohorts (Oaklander, Walitt) supply both the headline support and its strongest contradiction for P1. No causal autoimmune evidence exists outside long COVID. The one interventional result (Stein2025) is uncontrolled, COI-disclosed, and measures symptoms not the structural lesion. Above all, the **primary-dysautonomia-control gap is universal** — so the claim that distinguishes h0007 from generic post-infectious SFN (a *distinct* non-length-dependent substrate) cannot be adjudicated from anything currently in the corpus.

## Updated Priorities

- Keep h0007 at **candidate**; do not promote on this evidence.
- The highest-value next test is unchanged but now sharper: a **single-protocol paired (proximal+distal) skin-biopsy + autonomic study in infection-triggered PAIS with a primary-dysautonomia control arm** — this is the `/science:pre-register` target for `question:0004` and directly addresses P2 + the universal control gap.
- `task:t006` (functional-autoantibody lit-search) should specifically seek anti-GPCR evidence on the **autonomic** axis to move `proposition:0018`, given deSa2026's non-GPCR/non-autonomic result.
- Flag for `topic:measurement-ascertainment-artifacts-in-pais`: the Joseph-vs-Walitt ME/CFS discordance is a concrete instance of protocol/ascertainment generating opposite SFN conclusions.
