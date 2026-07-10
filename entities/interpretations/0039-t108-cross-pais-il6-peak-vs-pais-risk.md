---
id: interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk
kind: interpretation
title: "t108/q0026: cross-PAIS acute serum IL-6 peak does NOT rank post-infectious-fatigue risk — the IL-6-imprinting-depth proxy fails cross-pathogen; severity is the through-line"
status: active
source_refs:
  - cite:Cheong2023
  - cite:Bomans2018
  - cite:Hickie2006
  - cite:Morroy2016
  - cite:Kremers2014
  - cite:Coomes2020
  - cite:Aucott2016
  - cite:Davis2023
  - cite:Masyeni2024
  - cite:McBride2024
  - cite:Hagau2010
related:
  - task:t108
  - question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
  - topic:innate-immune-memory-trained-immunity-in-pais
  - question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
  - hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune
  - interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
created: '2026-07-10'
updated: '2026-07-10'
input: "Desk-research compilation (t108, deliverable for q0026): acute-phase circulating IL-6 peak levels across seven PAIS triggers (bacterial sepsis, dengue, SARS-CoV-2, acute Q fever, acute Lyme/EM, influenza, acute EBV/IM), severity-stratified where available, tabulated against each trigger's documented post-infectious-syndrome incidence, to test the q0026 cross-pathogen corollary that acute IL-6 magnitude proxies IL-6/STAT3→HSPC central-training depth and thus PAIS risk. Literature-grade; no participant data, no new analysis. Anchored to Cheong2023 (the IL-6→HSPC mechanism), Bomans2018 (post-sepsis HSPC parallel / high-IL-6 anchor), Hickie2006 (Dubbo prospective cross-pathogen cohort), and per-trigger IL-6 + incidence sources."
prior_interpretations: []
relations:
  - predicate: "sci:amends"
    target: "interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility"
---

<!-- Mode: DESK RESEARCH / CROSS-TRIGGER COMPARATIVE COMPILATION (t108, deliverable for q0026).
A literature proxy table + its honest reading; NO participant-level data, no new computation, no
controlled test. No evidence-lines or belief updates are minted on any proposition or hypothesis —
this compiles a cheap proxy and reports whether it coheres, not what a controlled test would find. -->

# Interpretation: t108/q0026 — cross-PAIS acute IL-6 peak vs post-infectious-fatigue risk

## Verdict

**Verdict:** [-] **The cross-pathogen IL-6-peak corollary of q0026 is not supported — and is partly refuted.** Acute serum IL-6 peak does **not** rank post-infectious-fatigue risk across PAIS triggers, and the model's specific prediction — that *low-IL-6* pathogens should imprint less and therefore carry *less* PAIS — fails at the low-IL-6 end: acute Q fever (mean IL-6 ~49 pg/mL, ~2× the healthy range), acute Lyme/EM (median ~21–26 pg/mL, with IL-6 *not even among the differentially-regulated acute markers*), and acute EBV/IM (modestly elevated, IFN-γ/IL-10-dominated) each produce a **10–20% post-infectious-fatigue fraction** comparable to the high-IL-6 end. The variable that survives as the cross-trigger ranking axis is **acute illness severity** — a multi-pathway composite of which IL-6 is one severity-correlated marker, not the driver. This does **not** refute the Cheong2023 within-COVID IL-6→HSPC imprinting mechanism (which is real, severity-bounded, and measured at the marrow/progenitor level, not by serum peak); it refutes the *extrapolation* that serum IL-6 magnitude is a usable cross-pathogen proxy for imprinting depth. The `[-]` is a **positive epistemic event**: it redirects q0026 away from a confounded, assay-broken cheap proxy toward the tests that can actually discriminate (within-pathogen severity-stratified designs; direct HSPC epigenomics — `question:0055` / t107).

## Findings Summary

Compiled acute-phase circulating IL-6 across seven triggers against each trigger's PAIS incidence. Rows are ordered by approximate acute serum IL-6 magnitude (high→low); **absolute cross-row comparison is unsafe** (see assay caveat), so the load-bearing reads are the *within-study severity contrasts* and the *IL-6-vs-PAIS-incidence mismatch*, not the raw pg/mL ordering.

| Trigger | Acute serum/plasma IL-6 (representative) | Assay | PAIS syndrome — incidence | What predicted PAIS *where tested* |
|---|---|---|---|---|
| **Bacterial sepsis / septic shock** | shock median **~1,300–2,100** (IQR tails >10,000–35,000); non-shock sepsis ~90; control ~24 | ELISA | PICS / post-sepsis syndrome **~35–70%** (3–12 mo) — but **organ-injury/ICU-driven, mechanistically distinct** from fatigue-type PAIS (the [@Bomans2018] HSPC-training parallel) | ICU/organ injury (not a fatigue-PAIS analogue) |
| **Dengue** | DHF **~230**, DF **~130** by ELISA [@Masyeni2024]; **but DSS ~10** by Roche ECLIA in a separate cohort [@McBride2024] | ELISA vs ECLIA (different studies) | post-dengue fatigue **~18–32%** (2 mo–1 yr) | severity; direct IL-6→fatigue link **[UNVERIFIED]** |
| **SARS-CoV-2 (COVID-19)** | severe/ICU pooled **~57**; mild **~17**; 2.9× severe-vs-non-severe (meta) | mixed [@Coomes2020] | long COVID **~50–70% hosp / ~10–30% non-hosp**; **~90% of cases arise from mild** acute infection | severity; IL-6 adjusted OR ≈ 2.0 (hospitalized only; no clean mild-stratum test) |
| **Acute Q fever** | mean **~49** (range 3–226); ~2× healthy | HS multiplex [@Kremers2014] | post-Q-fever fatigue syndrome (QFS) **~20%** [@Morroy2016] | **no acute-cytokine predictor found**; only genetic (IFN-γ/IL-10 SNPs) |
| **Acute Lyme (erythema migrans)** | median **~21–26**; **IL-6 not among top differential acute markers** (IP-10, CXCL9, ferritin, CRP, SAA led) | Luminex [@Aucott2016] | PTLDS **~10–20%** (14.5% in the EM cohort itself) | **acute mediators did NOT predict**; *post-treatment* CCL19 did (12.6× risk) [@Aucott2016] |
| **Severe influenza (ICU)** | severe **~18** serum (nonsurvivors ~65) [@Hagau2010]; mild/outpatient **~2–4** | Luminex / ELISA | "long flu": substantial post-acute burden, **lower-magnitude than COVID**, pulmonary-weighted | severity |
| **Acute EBV / infectious mononucleosis** | elevated but modest; **IFN-γ/IL-10/CD8-dominated** (clean pg/mL not tabulated in accessible primary text) **[UNVERIFIED numeric]** | ELISA | post-IM fatigue / ME-CFS onset **~11–12% at 6 mo** [@Hickie2006] | **acute illness SEVERITY** (not any cytokine) [@Hickie2006] |

Four structural findings drive the verdict:

1. **Assay + study + timing heterogeneity makes absolute cross-pathogen pg/mL ranking unusable.** ELISA, Roche electrochemiluminescence (ECLIA), and Luminex/multiplex report IL-6 on different scales — cross-validation studies put ELISA-vs-ECLIA discrepancies in the **~10–100×** range — and platform is unstated in most primary studies; on top of that, cohorts differ in draw-timing relative to symptom onset and in case mix. The dengue rows illustrate the size of the problem: severe dengue reads **~230 pg/mL** by ELISA in one cohort [@Masyeni2024] but dengue *shock* reads **~10 pg/mL** by ECLIA in another [@McBride2024] — a *cross-study, cross-platform* comparison, so it does not isolate assay from cohort/timing, but it shows the non-biological spread swamps any tidy cross-pathogen ordering. **Caveat:** this is not a same-sample split-platform demonstration (none was located); the claim is bounded to "absolute cross-pathogen pg/mL ranking is unusable," not "assay alone exceeds severity." Only *within-study* severity contrasts are trustworthy.

2. **Within every pathogen with stratified data (COVID, dengue, influenza — and sepsis), IL-6 scales with acute severity.** IL-6 is a robust *severity marker*. PAIS risk *also* scales with severity. So a raw IL-6↔PAIS association is **severity-confounded by construction** — exactly the covariate-sensitivity `interpretation:0036` and the project's own conventions flag. IL-6 and PAIS are both downstream of severity; co-movement does not make IL-6 the causal ranking variable.

3. **The corollary fails at the low-IL-6 end.** The IL-6-imprinting model's discriminating prediction is that *low-IL-6* triggers imprint less → less PAIS. Observed: Q fever (~49, ~2× control), Lyme (~21–26, IL-6 a minor player), and EBV/IM (modest, IFN-γ-dominated) each still produce **~12–20% post-infectious fatigue**. Low serum IL-6 does **not** buy correspondingly low PAIS — the prediction's own tail is where it breaks.

4. **The decisive natural experiment points away from IL-6-specificity.** The Dubbo Infection Outcomes Study [@Hickie2006] prospectively followed EBV, Q-fever, and Ross River virus — three pathogens with markedly different cytokine profiles — under one protocol, and found a **~identical post-infective-fatigue incidence (~11–12% at 6 mo) across all three**, with the predictor being **acute illness severity, not any specific cytokine**. A same-protocol, within-study, prospective cross-pathogen comparison is the strongest evidence available here, and it favors a **severity/host-response route** over an IL-6-magnitude-specific one. Convergently, the two triggers where acute cytokines were directly tested as PAIS predictors returned nulls for the acute cytokine and positives for something else: Lyme (acute mediators null; post-treatment CCL19 positive [@Aucott2016]) and Q fever (no acute-IL-6 predictor; only genotype). Only COVID shows a weak *severity-adjusted* IL-6 signal (Giannitrapani OR≈2.0), and only in hospitalized patients.

## Evidence Quality

Literature-grade, partially bib-anchored; **not** a controlled test and explicitly not belief-moving. Weighting:

- **Strongest:** Hickie2006 (Dubbo) — prospective, same-protocol, three-pathogen, severity-as-predictor. This is the single result that most directly adjudicates the cross-pathogen question, and it is in-bib and peer-reviewed.
- **Strong / quantitative anchors:** Coomes2020 (COVID IL-6 severe-vs-mild meta, 2.9×), Kremers2014 (acute Q-fever IL-6, n=102, HS multiplex), Morroy2016 (QFS ~20% systematic review), Aucott2016 (acute-mediators-null / CCL19-positive for PTLDS), Davis2023 (long COVID incidence by severity). All in-bib.
- **Mechanism anchors (context, not test):** Cheong2023 (IL-6→HSPC imprinting, severe COVID) and Bomans2018 (post-sepsis HSPC training) frame *why* IL-6 was a candidate proxy — but neither measured a cross-pathogen serum-IL-6/PAIS relationship, so neither supports the corollary; they define the mechanism the corollary was a (failed) shortcut to.
- **Load-bearing for the assay/severity findings (in-bib):** the dengue and influenza IL-6 anchors — Masyeni2024 (DF-vs-DHF ELISA gradient), McBride2024 (dengue-shock ECLIA), Hagau2010 (severe-H1N1 serum IL-6, survivor-vs-nonsurvivor) — carry structural findings #1 (assay/study heterogeneity) and #2 (within-pathogen severity scaling), so they are added to the bib and `source_refs`, not treated as row decoration. Their role is to show IL-6 is a severity marker in *every* pathogen with stratified data and that absolute pg/mL is not cross-comparable; they do **not** bear on the low-IL-6-trigger tail (findings #3–#4), which is where the verdict is actually decided (Q-fever/Lyme/EBV + Dubbo).
- **Weakest / flagged:** per-trigger absolute pg/mL values are drawn from heterogeneous assays and, for EBV/IM, are qualitative only (**[UNVERIFIED numeric]** — primary IM studies report direction/significance, not tabulated means). The "long flu" burden row is cited inline (Al-Aly/Xie VA cohort PMID 38104583) and is **illustrative only** — it bears on neither the assay/severity findings nor the low-IL-6 tail, so it is not promoted to the bib.

**Confirmatory vs exploratory:** exploratory desk compilation. **Dependence:** the four findings are not independent — assay heterogeneity (1), severity confounding (2), and the low-end failure (3) are three views of the same underlying fact (IL-6 is a severity marker, poorly comparable across assays), and Dubbo (4) is the one structurally independent line.

## Data Quality Checks

No empirical dataset was analyzed; the "data-quality" hazards are the compilation's own:

- **Cross-assay non-comparability (dominant):** ELISA/ECLIA/Luminex differ 10–100×; platform unstated in most sources. Any future cross-pathogen cytokine comparison **must** harmonize assay or restrict to within-study severity contrasts — a direct methodological carry-forward of the same platform-confound lesson learned in the t117 flagship.
- **Peak-timing undersampling:** acute IL-6 peaks ~day 7–14 post-onset; single admission draws (common in the mild/outpatient strata) bias those strata low, artificially steepening the severity gradient.
- **Severity-selection in the mechanism anchor:** Cheong2023's imprint is demonstrated only in severe/hospitalized COVID; the corollary silently extrapolates it to mild disease and to non-COVID triggers with no direct support.
- **Sepsis is not a clean fatigue-PAIS analogue:** its high chronic-morbidity fraction is ICU/organ-injury-driven (PICS), so its position as the high-IL-6 anchor overstates the IL-6↔fatigue link if read naively.

No empirical control/count/dimensionality concerns apply (no data).

## Proposition-Level Updates

**None minted.** This is a proxy compilation, not a controlled test; no `proposition:` gains or loses an evidence-line, and no belief moves. The result changes *which experiment to run*, not the belief state — consistent with the discipline of `interpretation:0036`.

## Hypothesis-Level Implications

Qualitative only; no belief updates.

- **question:0026 — the cheap cross-pathogen route is closed.** q0026's mechanism (IL-6/STAT3→HSPC imprinting) stands untouched *as a within-pathogen, severity-bounded mechanism*; what is refuted is the tempting shortcut that acute **serum IL-6 magnitude ranks it across pathogens**. q0026 remains `active`; its testable edge is now explicitly the direct-epigenomic one, not the serum-cytokine one.
- **topic:innate-immune-memory / question:0055 (imprinting depth predicts persistence) — redirect, not refutation.** The central-training hypothesis should be tested by measuring the **imprint directly** (HSPC/monocyte ATAC-seq or H3K4me3, severity-matched), which is exactly what t107 scopes. Serum IL-6 is too confounded and too assay-noisy to stand in for it.
- **hypothesis:0012 (trigger-nonspecific sickness-behavior) — consistent with / mildly strengthened.** The Dubbo cross-pathogen equal-incidence result is a classic pillar of the trigger-nonspecific view, and the broader "severity not cytokine-identity predicts PAIS" pattern coheres with it. No belief update from a desk proxy, but the compilation lands on the h0012 side of the ledger.
- **hypothesis:0004 (acute-severity threshold) — consistent.** Severity emerging as the surviving cross-trigger ranking axis is congruent with a severity-gated model; again, no controlled update.
- **hypothesis:0011 (severity does NOT predict chronic fatigue, only organ sequelae) — mild tension.** Dubbo found acute severity *did* predict post-infective fatigue, which cuts against h0011's strong form. Noted as tension to be adjudicated by controlled evidence, not by this proxy.

## Evidence vs. Open Questions

- **q0026 — partially addressed.** The cross-pathogen serum-IL-6 corollary is answered (does not hold); the underlying HSPC-imprinting mechanism is not addressed by this route and remains open.
- **q0055 — unchanged standing, sharper route.** Whether imprinting depth predicts persistence is untouched here but is now clearly pointed at direct epigenomics (t107) rather than a cytokine surrogate.
- **question:0001 (shared molecular signature) — small negative texture.** If a single acute cytokine magnitude does not transfer across triggers, a shared *analyte-level* signature is even less likely than a shared *pathway/latent-state* one — echoing the `interpretation:0036` / t035 read that the shared axis, if any, is macro-state-level, not molecule-level.

## New Questions Raised

- **(methodology, P3):** Any future cross-pathogen cytokine comparison must **harmonize assay platform or restrict to within-study severity contrasts** — folded into this interpretation as a design rule, not reserved as a standalone `question:` (it is the same platform-confound lesson as the t117 flagship).
- **(mechanism, P3) — folds into t107/q0055:** does *severity-matched* HSPC imprinting depth differ across triggers, independent of serum IL-6? This is the direct test the serum proxy cannot perform; it is already scoped by t107 (opportunistic archived-PBMC ATAC-seq feasibility). No new task created — this interpretation is the argument for prioritizing t107 over any further serum-cytokine compilation.

## Limitations & Residual Uncertainty

- **A failed proxy is not a failed mechanism.** The compilation weakens *serum-IL-6-as-cross-pathogen-proxy*; it does **not** weaken the Cheong2023 central-training mechanism, which operates at the marrow/progenitor level and is severity-bounded. Serum IL-6 is a crude, timing-sensitive, assay-noisy surrogate for the actual imprinting signal, and its failure is partly a **measurement** failure.
- **Within-pathogen, the IL-6→severity→PAIS chain remains intact** and even plausibly causal (IL-6 could mediate the severity→PAIS link within a trigger); the `[-]` is specifically about the *cross-pathogen magnitude-ranking* prediction, not this within-pathogen chain. The verdict is therefore textured, not monolithic.
- **[UNVERIFIED] numerics:** absolute IL-6 pg/mL are assay-heterogeneous throughout; EBV/IM values are qualitative; direct acute-IL-6→post-dengue-fatigue and →long-flu links were not located (genuine evidence gaps, not just unchecked).
- **Desk-research grade.** No cohort, no reanalysis, no belief update. This licenses reprioritizing q0026's test route; it does not settle the mechanism.

## Updated Priorities

1. **Do not pursue further cross-pathogen serum-cytokine compilations for q0026** — the assay-heterogeneity + severity-confound ceiling is structural and cannot be argued away by adding triggers (directly parallel to the t117 "further public-data pairings are the wrong spend" lesson).
2. **Redirect q0026's empirical edge to the direct imprint:** prioritize **t107** (archived-PBMC HSPC ATAC-seq feasibility) as the route that can actually test imprinting depth, severity-matched, against PAIS persistence (`question:0055`).
3. **Carry the assay-harmonization rule** into any future cross-condition inflammatory-marker comparison (design constraint recorded above).
4. **Note the Dubbo severity-not-cytokine result** on the `hypothesis:0012` / `hypothesis:0011` ledger as literature context for the eventual controlled adjudication (no belief update now).
5. **Record t108 as done** — its deliverable (the cross-trigger frame + its honest reading) is complete; it returned a clean negative that reshapes q0026's test strategy.
