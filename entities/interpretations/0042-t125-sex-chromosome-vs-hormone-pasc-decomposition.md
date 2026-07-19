---
id: interpretation:0042-t125-sex-chromosome-vs-hormone-pasc-decomposition
kind: interpretation
title: t125 — female PASC bias does not decompose into hormone vs X-chromosome-dosage axes in Chaulagain2026; the review tilts PASC-specific weight toward the chromosome axis and confirms the h0005 hormone-leg fragility
status: active
source_refs:
- cite:Chaulagain2026
related:
- paper:Chaulagain2026
- question:0080-sex-chromosome-vs-hormone-decomposition-pais
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0020-host-immune-baseline-reserve-gate
- proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways
- proposition:0044-female-pasc-bias-x-chromosome-dosage-rival
- evidence-line:0094-chaulagain2026-x-dosage-supports-genetic-sex-rival
- plan:0009-wave1-mr-hormone-pilot
- question:0007-mechanism-of-female-predominance-in-pais
created: '2026-07-19'
updated: '2026-07-19'
input: entities/papers/Chaulagain2026.md (user-supplied fulltext PDF, intaken seed batch 2026-07-10); entities/questions/0080; entities/propositions/0044; entities/hypotheses/0005
prior_interpretations: []
relations: []
---

# Interpretation: t125 — female PASC bias vs. the hormone/chromosome decomposition

## Verdict

**Verdict:** [~] Not decomposable from this review — Chaulagain2026 juxtaposes the two contributors but does not *isolate* them; it reports **limited direct evidence for gonadal steroids in PASC outcomes** (an evidence *gap*, not positive evidence that X-dosage explains the female excess), which confirms (does not rescue or refute) the pre-existing single-line fragility of h0005's hormone-mechanism leg (`proposition:0002`) and makes the X-dosage rival (`proposition:0044`) a **salient weak rival**, not a rival raised to parity. The genetically-predicted **hormone-liability limb has in fact already been probed** — `plan:0009` ran the D-005-authorized Ruth SHBG/testosterone → HGI long-COVID MR (six strata) and returned an honest **null/uninformative** result under ancestry (KD1) and mixed-sex-outcome (KD3) ceilings — but that MR estimates a hormone-liability effect, it does **not** decompose the female excess into chromosome vs hormone shares. A true decomposition still requires karyotype-and-hormone-resolved designs no admissible PAIS vehicle yet supplies.

## Findings Summary

t125 asked whether the female PASC bias can be split into a **gonadal-steroid-timing** component (the ER/AR/PR hormone axis that `hypothesis:0005` centers on) and a **sex-chromosome-dosage** component (X-linked immune-gene dosage, XCI escape of TLR7/KDM6A, XIST). Reading the already-intaken `paper:Chaulagain2026` (Nature Immunology 2026; 27:660–673) against q0080 and the pre-existing rival `proposition:0044`:

1. **The review does not perform the decomposition.** It is a narrative review that frames the two axes as "orthogonal" and maps sex-differential outcomes pathogen-by-pathogen; it is not a design that measures genetic sex and hormone state in the same subjects, so it cannot attribute the female PASC excess to either axis. (`literature_evidence`; the raw female-PASC association it summarizes is `proxy_directness: indirect`.) The "orthogonal" framing is itself only approximate — the axes **interact** (see the estimand note below): chromosome complement shapes gonadal development, and gonadal steroids transcriptionally regulate X-linked immune genes — the review's own pDC example has **estrogen inducing X-linked TLR7**.

2. **For PASC, the review reports the hormone evidence as thin and offers chromosome-linked observations — but this is an evidence gap, not a demonstrated dominance of the chromosome axis.** It states, per the intaken fulltext, that there is **"limited evidence supporting a role for gonadal steroids in PASC outcomes so far,"** and juxtaposes chromosome-linked findings. Those chromosome-linked findings are **heterogeneous and mostly not PASC-cohort-specific**, so they do not add up to positive evidence that X-dosage carries the female excess:
   - **XIST** — from the primary study Chaulagain cites (Hamlin et al. 2025, Stanford IRIS cohort, n=45 longitudinal; PMC12148066, not yet a project entity): XIST was elevated **during acute infection in females who *subsequently* developed LC**, and "still present but less prominent" at 3 and 12 months. This is an **acute-phase predictor that diminishes**, not a steady-state "upregulation in PASC immune cells."
   - **Biallelic TLR7** — general sex-immunology evidence (pDC/B-cell type-I-IFN, IgG class switch), **not demonstrated in a PASC cohort**.
   - **Y-linked genes** — Hamlin reports **reduced *expression*** of DDX3Y (down-regulated at 12 months in males with LC), UTY, PRKY, USP9Y — **not genomic "loss"** — and the primary study does **not** link this to a cardiovascular phenotype. (My prior draft's "loss of Y-chromosome genes … for the male PASC cardiovascular phenotype" conflated two separate statements and is corrected here.)

   (The "limited gonadal steroids" quote is fulltext-sourced from the user-supplied PDF; the paper is paywalled and this PASC-specific sentence is not independently web-verifiable. The paper's identity and two-axis framing *were* confirmed against the open abstract, which presents the two axes as **joint contributors**, not a comparison establishing that either dominates.)

3. **The one shared observation adjudicates neither axis.** The female 40–55-year PASC/fatigue peak the review reports is *jointly* consistent with a perimenopausal hormone-decline window (hormone axis) and with a fixed X-dosage effect that happens to be read in that age band (chromosome axis). It is therefore not discriminating evidence for either.

4. **Scope guard on the "limited" statement.** "Limited evidence for gonadal steroids" is specific to **PASC outcomes**. Within the *same* review the hormone axis carries substantial evidence in acute IAV severity (estradiol/ERα-agonist rescue), HBV/HCV sex bias, and vaccine immunogenicity/antibody kinetics. The finding is "thin *direct-PASC* hormone evidence," **not** "hormones do not shape immunity."

## Evidence Quality

- **Source class:** single narrative review (secondary source), no systematic search or meta-analysis; effect sizes and replication status of the underlying primary studies are not adjudicated by the review.
- **Underlying mechanism maturity:** the chromosome-axis mechanisms it leans on for PASC (XIST-in-PASC transcriptomics, TLR7 biallelic expression, KDM6A–NK axis) are largely cross-sectional in humans and heavily preclinical/mouse for causal steps; the causal link from these molecular readouts to the PASC *phenotype* is indirect. This matches the `identification_strength: observational`, `proxy_directness: indirect`, `claim_layer: mechanistic_narrative` fields already carried by `proposition:0044`.
- **Dependence:** this is **not** an independent new data line for h0005. It is a re-reading of one review that was already intaken in the seed batch; its epistemic contribution is a *directional weight-shift and a fragility confirmation*, not fresh support or fresh dispute evidence. No new `evidence-line` edges are minted here — the review does not add net support to `proposition:0002` (it reports *absence* of strong direct-PASC hormone evidence), and it is already the `source_ref` of `proposition:0044`.
- **Confirmatory vs exploratory:** exploratory re-reading; no pre-registered test.

## Data Quality Checks

No dataset was analyzed — this is a literature-synthesis rollup, so control-uniqueness / sample-count / dimensionality checks do not apply. One provenance note: the load-bearing PASC-specific quote and the XIST-in-PASC / Y-gene-loss claims originate in the **user-supplied fulltext PDF** captured during the seed-batch intake; the paper is paywalled and these PASC-section sentences could not be re-verified against the open web (only the abstract and two-axis framing were re-confirmed). A minor metadata discrepancy exists — the project bib lists four authors (Chaulagain, Liu, McCombs, Klein) while one indexing source shows three; this does not bear on any claim used here. No data-quality concern otherwise identified.

## Proposition-Level Updates

- **`proposition:0002` (reproductive-stage transition modifies immune-regulatory pathways — the hormone mechanism, `core`/fragile):** No new support. The review's PASC-specific "limited gonadal-steroid evidence" is a **cautionary / fragility-confirming** signal: an independent, mechanistically authoritative review does *not* resolve the single-line fragility flagged in the h0005 bundle, and if anything tilts the *PASC-specific* prior against a hormone-dominant reading. This is **not a refutation** — the hormone axis retains strong evidence outside PASC in the same review, and the review is not a decomposing design. A distinct, germline route has meanwhile *already been tried*: the D-005-authorized hormone-liability MR (`plan:0009`, Ruth SHBG/testosterone → HGI long-COVID) returned a **null/uninformative** result under KD1/KD3 ceilings — weak, non-corroborating and non-reportable-by-construction on the *genetically-predicted-hormone-liability* limb (not a refutation, and it does not touch the reproductive-*stage-transition* content this proposition is actually about). Net: the priority of finding *independent, PASC-direct* corroboration for this leg is reaffirmed (the live cohort/mediator paths remain t038/IMPACC mediator-compatible and t040/RECOVER-ancillary, both already banked; the MR limb is banked pending a matched EUR-only + sex-stratified outcome).

- **`proposition:0044` (female PASC bias may be X-chromosome-dosage/XIST-driven — `rival`):** Remains a **legitimate weak rival, made salient — not raised to parity.** Chaulagain2026 supplies its "limited hormone evidence + XIST/TLR7/Y-gene" content, but as a review it neither isolates genetic sex from hormone timing nor supplies a comparison rubric that would rank the two axes; the supporting `evidence-line:0094` is correctly typed `strength: weak`, `model_criticism`. Its content shows the hormone axis is **underdetermined**, not that the X-dosage axis is established or dominant. `observational`/`indirect`, awaiting a discriminating design. Status unchanged; this interpretation is its rollup, not new belief. *(Both this proposition and `evidence-line:0094` carry "raised to parity" wording from the seed batch; that phrasing is over-stated for the same reason and is flagged for softening — see Limitations.)*

- **`proposition:0001` (reproductive-stage transition shifts the failed-recovery threshold — `core`):** Direction unaffected. The 40–55 female peak is consistent with the threshold-shift account but equally with X-dosage, so it neither raises nor lowers this leg.

## Hypothesis-Level Implications

- **`hypothesis:0005` (reproductive-stage immune homeostatic margin):** Stays `active`; no promotion, no demotion. The consequence of t125 is a **scope observation**: h0005 is framed entirely around the gonadal-steroid/reproductive-stage axis and does **not** represent the sex-chromosome-dosage axis, which the review raises as an alternative contributor to the *female PASC* bias. There is no home hypothesis in the project for the sex-chromosome-dosage axis at present (see the h0020 note). The decomposition gap (q0080) is a **strengthening/promotion blocker for h0005's hormone-mechanism leg** (h0005 is already `active`; the block is on strengthening the fragile hormone leg, not on the hypothesis's activation): until a hormone-measured, genetically-resolved design separates the axes, the female PASC excess cannot be attributed to the hormone axis above and beyond sex/chromosome dosage.

- **`hypothesis:0020` (host immune baseline reserve gate):** A **candidate future home** for the fixed sex-chromosome-dosage component (TLR7 biallelic dose, KDM6A copy number) as a reserve-axis element, distinct from h0005's dynamic hormone modifier — but only that. h0020 is currently `status: draft`, and its P1–P6 bundle contains **no** sex-chromosome-dosage proposition; it names h0005 only as "a worked instance generalized here." Wiring the chromosome-dosage axis into h0020 would require adding an explicit auxiliary proposition; this interpretation does not do so and does not assert h0020 already houses it. No belief change.

## Evidence vs. Open Questions

- **`question:0080` (can sex-biased PAIS be decomposed into X-dosage vs gonadal-steroid components?):** *Partially addressed.* Answer logged: **not from this review.** The two axes are mechanistically distinguishable but **not orthogonal and not cleanly separable by a single mediation split of the total sex effect** — chromosome complement shapes gonadal development, gonadal steroids regulate X-linked immune genes (estrogen→TLR7), and their interaction is plausible. So q0080 should not promise "one decomposition"; the identifiable targets are a **set of conditional estimands**: (a) hormone-state contrasts *within* chromosome strata, (b) chromosome-dosage contrasts *under comparable hormone exposure*, and (c) their interaction — not a total-sex-effect mediation partition. Candidate vehicles: genetic natural experiments (Turner X0 / Klinefelter XXY, gender-diverse cohorts on hormone therapy) with PASC follow-up; longitudinal designs where hormone state varies at fixed karyotype; and hormone-liability MR — but note MR estimates the effect of **genetically-predicted hormone liability** and *cannot* return the *fraction* of the female excess that is hormonal vs chromosomal. The hormone-liability MR has already been run (`plan:0009`, D-005-authorized) and returned a **null/uninformative** result under KD1/KD3 ceilings, so the hormone-liability limb is *probed and non-corroborating*, while the full multi-estimand decomposition still has **no admissible vehicle**. q0080 remains `active` with the estimand structure now made explicit.
- **`question:0007` (mechanism of female predominance in PAIS):** unchanged framing; this interpretation sharpens it into a two-axis, entangled-proxy structure but does not resolve it.

## New Questions Raised

- **XIST: passive readout or active driver? (candidate, not yet minted — Medium):** Does the reported XIST upregulation in female-PASC immune cells reflect a passive epigenetic marker of female sex, or an active driver of immune hyperactivation contributing causally to the female PASC bias? Suggested next evidence: single-cell XIST/XCI-escape mapping in PASC vs recovered, ideally paired with hormone measures. This mirrors follow-up #1 in the `paper:Chaulagain2026` note; deliberately **not** created as a standalone question here to avoid entity proliferation — flagged for a future scope decision if it becomes actionable.
- No new question is minted for the decomposition design itself — `question:0080` already owns it.

## User Questions

None raised during this interpretation.

## Limitations & Residual Uncertainty

- **Single secondary source.** The entire directional weight-shift rests on one narrative review; a different review could weight the axes differently. The "limited hormone evidence in PASC" is the review authors' characterization, not a quantified null.
- **Fulltext provenance.** The PASC-specific load-bearing sentences are from the user-supplied PDF and are paywall-blocked from independent re-verification; only the abstract-level two-axis framing and bibliographic identity were re-confirmed.
- **Entanglement is structural, not incidental.** Because XX sex and female hormone trajectory co-vary across almost the entire lifespan, *no amount of additional observational data* resolves q0080; the limitation is identifiability, not sample size.
- **Authorization/execution status of the hormone MR (correction of an earlier error in this document).** The MR route named in q0080 (`dataset:ruth-2020-shbg-testosterone-gwas` → `dataset:covid19-hgi-longcovid-gwas`, also carried in the h0005 `required_capabilities`) was **explicitly authorized by D-005** (the SHBG/testosterone GWAS is one of the three cataloged Wave-1 vehicles, `core/decisions.md`) and has **already been executed** end-to-end by `plan:0009` across six SHBG+testosterone strata, returning a **null/uninformative** result under the ancestry (KD1) and mixed-sex-outcome (KD3) ceilings (`results/wave1-mr-hormone-pilot/results.md`). It is therefore **not** a "candidate gated behind a fresh D-005 decision" — an earlier draft of this interpretation asserted that and was wrong. Per D-006, a **matched EUR-only + sex-stratified HGI rerun is in-scope maintenance and needs no fresh authorization**; only a *distinct outcome vehicle* (e.g. FinnGen, or any non-HGI outcome) would require a fresh scope decision. The genetic-natural-experiment routes (Klinefelter/Turner, gender-diverse cohorts) remain without an admissible, third-party-reproducible PAIS vehicle.
- **Seed-batch "parity" wording.** `proposition:0044` and `evidence-line:0094` describe the X-dosage rival as "raised to parity" with the hormone account. That over-states a review that offers no ranking rubric and only an *evidence gap* on the hormone side; the accurate reading is a **salient weak rival**. The wording is flagged here; the entities themselves are left as-is pending a dedicated pass to avoid re-litigating seed-batch propositions inside a task rollup.
- **Hamlin primary source not intaken.** The corrected XIST/Y-gene details come from the primary study Chaulagain cites (Hamlin et al. 2025, IRIS cohort, n=45; PMC12148066), read via its open fulltext for this correction but **not yet a project paper entity**; it is referenced here as a verifiable pointer, not a durable `cite:`/`paper:` link.

## Updated Priorities

- **Close t125** as done with this interpretation as the rollup; no reopening.
- **q0080 stays open** with the design bar now explicit; it is the standing blocker for attributing the female PASC bias to the hormone axis and for promoting h0005's hormone-mechanism leg.
- **Reaffirm, do not add work:** the highest-value upward evidence for `proposition:0002` remains a hormone-measured, *genetically-resolved* PASC design — the same requirement already banked under t038 (IMPACC, mediator-compatible) and t040 (RECOVER ancillary, post-seed-stage). t125 does not create new analysis; it sharpens why those designs must resolve *both* axes jointly, not hormones alone.
- **The sex-hormone MR is not pending authorization** — it was the D-005 Wave-1 hormone arm and is already run (`plan:0009`, null under ceilings). Its reportable-grade resumption is **banked D-006 maintenance**, triggered by a matched **EUR-only long-COVID outcome** (lifts KD1) and, for any sex-modification read, a **sex-stratified outcome** (lifts KD3) — not by more compute on the current outcome. Only a *distinct* outcome vehicle (FinnGen/non-HGI) would need a fresh scope decision.
