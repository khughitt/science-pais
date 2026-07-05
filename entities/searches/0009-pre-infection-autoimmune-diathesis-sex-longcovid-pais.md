---
id: search:0009-pre-infection-autoimmune-diathesis-sex-longcovid-pais
kind: search
title: "Literature search: pre-existing autoimmune diathesis as sex-conditioned effect modifier for long COVID / PAIS risk (t078)"
status: active
created: "2026-06-30"
updated: "2026-06-30"
source_refs:
  - cite:Hill2022
  - cite:Srivatsan2025
  - cite:Wolff2023
  - cite:Steiner2020
  - cite:Tsai2019
  - cite:Fedorchenko2023
  - cite:Shah2025
related:
  - task:t078
  - patch-definition:immune-state-shift-causal-landscape
  - question:0005-latent-to-overt-autoimmunity-conversion
  - question:0007-mechanism-of-female-predominance-in-pais
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
---

# Search: pre-existing autoimmune diathesis as a sex-conditioned effect modifier for long COVID / PAIS risk (t078)

## Search Focus

`task:t078` (fast-follow from `patch-definition:immune-state-shift-causal-landscape`, tied to
`question:0005` and `hypothesis:0005`) asks whether **pre-existing autoimmune diathesis
diagnosed BEFORE the index infection** acts as an **effect-modifier** for failed
post-infectious recovery (long COVID / broader PAIS), and whether that modification is
**sex-conditioned**. Scope discipline: the exposure is *prior* autoimmune liability — **not**
post-infection autoantibodies (that is `question:0005` / `hypothesis:0007` territory) and
**not** the reverse "COVID → new-onset autoimmunity" direction (large but out of primary
scope; carried only as contrast). Mandatory confounding concerns: **sex, age, acute
severity, healthcare utilization, baseline comorbidity**.

## Query Set

OpenAlex (broad discovery) was **503-unavailable** this run; discovery ran on PubMed
E-utilities (esearch/esummary) + targeted web search (`fallback-web`).

1. broad: pre-existing autoimmune disease → long COVID risk
2. EHR/cohort: autoimmune prior diagnosis → PASC cohort
3. sex-stratified: long COVID × autoimmune × sex/female cohort
4. contrast: atopy / asthma / allergic disease → long COVID risk
5. PAIS-broadened: autoimmune disease → post-infectious fatigue / ME/CFS

## Sources and Run Metadata

- **PubMed esearch** relevance-sorted: query-1 (autoimmune × long-COVID/PASC × risk/cohort)
  455 hits; query-2 (autoimmune/atopy × long-COVID × sex) 721 hits. Top ~45 summaries
  triaged.
- **Web search** (`fallback-web`) for direction-disambiguation and atopy/ME-CFS foci.
- Dedupe by DOI → PMID → normalized title. Metadata taken from source records only;
  unverified fields marked `[UNVERIFIED]`.
- **Direction audit applied:** each candidate tagged exposure→outcome; reverse-direction
  (COVID→autoimmunity) demoted to Peripheral.

## Ranked Results

**Bold tier = on-target** (pre-existing autoimmune/atopy **→** long COVID / PAIS).

| Rank | Citation (short) | Year | IDs | Tier | Why it matters |
|---|---|---|---|---|---|
| 1 | Hill — N3C/RECOVER PASC risk factors (EHR) | 2023 | PMID 37880596 · DOI 10.1186/s12889-023-16916-w · (preprint medRxiv 2022, PMID 36032983) | **Core now — READ** | Best design fit: large N3C EHR cohort, 1:5 matched, computable PASC phenotype (U09.9 or LC-clinic visit). Published in **BMC Public Health 2023** (not Lancet). Read → `paper:Hill2022`: autoimmune enters only as a pooled Charlson "rheumatologic disease" term (OR 1.27); sex is a covariate, no sex×comorbidity interaction; utilization only a county-level proxy. Substrate for the t078 design, not the estimand. |
| 2 | Srivatsan — PASC burden in rheumatic diseases | 2025 | PMID 39550103 · DOI 10.1016/j.rdc.2024.08.003 | **Core now — READ** | Direct exposure = pre-existing autoimmune rheumatic disease; outcome = PASC burden. Read → `paper:Srivatsan2025`: **pointer-only** narrative review, no pooled estimate, sex×ARD never crossed; key finding — in the one matched cohort it cites (Boekel2023) ARD→PASC attenuates to non-significant after severity adjustment. Hands off four matched primary cohorts: Boekel2023, Sen/COVAD2023, PatelNJ2024, DiIorio2022. |
| 3 | Wolff — allergic diseases as Long-COVID risk (SR of prospective cohorts) | 2023 | PMID 37936547 · DOI 10.1111/cea.14391 | **Core now** | The atopy **contrast** arm: systematic review restricted to *prospective* cohorts; tests whether the liability is autoimmune-specific vs general immune-hyperreactivity. |
| 4 | Steiner — PTPN22/CTLA4 variants in ME/CFS with infectious onset | 2020 | PMID 32328064 · DOI 10.3389/fimmu.2020.00578 | **Core now** | Genetic **autoimmune diathesis × infection-triggered PAIS** — the cleanest test of "prior autoimmune liability predisposes to post-infectious non-recovery"; effect concentrated in infectious-onset subgroup. |
| 5 | Tsai — IBD → incident chronic fatigue syndrome (population cohort) | 2019 | PMID 30795765 · DOI 10.1186/s12967-019-1797-3 | **Core now** | Pre-existing autoimmune (IBD) → later CFS in a matched population-based retrospective cohort — on-target design in the PAIS-broadened arm. |
| 6 | Yadaw — pre-existing autoimmunity → COVID **severity** (N3C) | 2023 | PMID 36778264 · DOI 10.1101/2023.02.02.23285353 | Relevant next | Matched N3C cohort, autoimmune→severity **consistent across sex** (OR≈1.13). Outcome is acute severity (a **mediator/confounder** on the path to PAIS, `hypothesis:0004`), not long COVID — read for the confounding structure. |
| 7 | Fedorchenko — Long COVID in autoimmune rheumatic diseases | 2023 | PMID 36995436 · DOI 10.1007/s00296-023-05319-0 | Relevant next | Narrative synthesis of the exposure arm *(already in corpus)*. |
| 8 | Shah — Sex Differences in Long COVID | 2025 | PMID 39841477 | Relevant next | The sex-conditioning backbone *(already in corpus)*; not autoimmune-conditioned — pair with the autoimmune arm. |
| 9 | Hu — Long COVID in multiple sclerosis (multicenter) | 2025 | PMID 40910585 | Relevant next | Pre-existing autoimmune (MS) → long COVID, but **cross-sectional** — deprioritized on design. |
| 10 | Zaccardelli — RA acute & postacute COVID outcomes | 2023 | PMID 36752280 | Peripheral monitor | Pre-existing RA → postacute outcomes; opinion/synthesis. |
| 11 | Tzang — COVID & new-onset autoimmune diseases, meta-analysis (97M) | 2025 | PMID 41452424 | Peripheral monitor | **Reverse direction** (COVID→autoimmunity); context for `question:0005`, not the t078 exposure. |
| 12 | Heo — long-term autoimmune CTD risk after COVID | 2024 | PMID 39504045 | Peripheral monitor | **Reverse direction**; `question:0005` territory. |
| 13 | Mandel — long COVID incidence proportion 2020–2024 | 2025 | PMID 39907495 · DOI 10.1093/cid/ciaf046 | Peripheral monitor | Denominator / case-definition reference for any t078 rate calc. |

## Priority Reading Queue

**Core now** (read to decide t078's form): Hill2022 ✅READ → Srivatsan2025 ✅READ → Wolff2023 → Steiner2020 → Tsai2019. *(Top two read 2026-06-30; both confirm the t078 estimand is unreported → t078 promoted to a design-stage analysis plan. Boekel2023 severity-attenuation makes acute severity a candidate mediator, not just a confounder.)*
**Relevant next:** Yadaw2023 (severity-as-confounder), then re-read the corpus pair Shah2025 + Fedorchenko2023 through the effect-modifier lens.
**Peripheral monitor:** Tzang2025, Heo2024 (reverse-direction anchors for q0005), Mandel2025 (denominators).

## Coverage Notes and Gaps

- **The central gap is the t078 estimand itself.** No identified study reports a
  **sex-stratified (or sex-interaction) estimate of pre-existing autoimmune disease × long
  COVID** with matched infected controls and acute-severity + healthcare-utilization
  adjustment. The closest matched sex-aware design (Yadaw2023, N3C) has the **wrong
  outcome** (acute severity), and the closest long-COVID sex study (Shah2025) is **not
  autoimmune-conditioned**. This strongly suggests t078 is a **new-analysis** target
  (N3C / OpenSAFELY / All-of-Us), not an evidence-extraction task.
- **Confound to pre-commit (per h0008):** autoimmune disease and long COVID are both
  female-predominant and both healthcare-contact-intensive → naive association is
  sex- *and* ascertainment-confounded. Any t078 estimate must condition on sex, age,
  utilization, and baseline comorbidity, and prefer population-based over
  clinic-ascertained sampling. **Acute severity is handled separately, not blanket-adjusted:**
  it is a *mediator* on the h0004 path (autoimmune → severe acute → PASC), so the analysis
  reports a **total effect** (severity not conditioned) and a **severity-controlled / direct
  contrast** as two distinct estimands — see `plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan`.
  Conditioning severity into a single adjustment set would block the exposure-driven path.
- **Exposure heterogeneity:** "autoimmune diathesis" spans organ-specific (Hashimoto's,
  IBD, MS), systemic-rheumatic (SLE, RA), and genetic-risk-only (PTPN22/CTLA4) strata,
  which may modify risk differently — do not pool blindly.
- **Deprioritized as requested:** cross-sectional self-report symptom surveys (surfaced but
  not queued) unless used for hypothesis generation.

## Recommended Next Actions

1. `/science:research-papers` on the five Core-now stubs (Hill2022, Srivatsan2025,
   Wolff2023, Steiner2020, Tsai2019) — extract exposure definition, control matching,
   sex handling, severity/utilization adjustment, and case definition.
2. After reading, decide t078's form: **interpretation pass** (if an existing estimate is
   admissible), **dataset-feasibility pass** (N3C / OpenSAFELY / All-of-Us for a
   sex-stratified pre-existing-autoimmune × long-COVID contrast), or a **small
   analysis-plan** — the coverage gap points to feasibility/analysis, not extraction.
3. Fold the "autoimmune-diathesis effect-modifier" reading into `question:0005` and the
   candidate node in `patch-definition:immune-state-shift-causal-landscape`.
