---
id: "synthesis:0008-project-synthesis-rollup"
kind: "synthesis"
title: "Project synthesis - health-post-acute-infection"
status: "active"
report_kind: "synthesis-rollup"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
synthesized_from:
  - hypothesis: "hypothesis:0001-shared-dysregulated-attractor"
    file: "entities/synthesis/0001-shared-dysregulated-attractor.md"
    sha: "9db009fff6840e2e8101e6c1d480cf0b8eafd17e"
  - hypothesis: "hypothesis:0002-tissue-reservoir-antigen-fragment"
    file: "entities/synthesis/0002-tissue-reservoir-antigen-fragment.md"
    sha: "5f4e7181a3b5868bd301c23312901d4cc46f79f6"
  - hypothesis: "hypothesis:0003-immune-exhaustion-feedback"
    file: "entities/synthesis/0003-immune-exhaustion-feedback.md"
    sha: "22b86e9d1171fe63c87d808ea22abbed311add3b"
  - hypothesis: "hypothesis:0004-acute-severity-threshold"
    file: "entities/synthesis/0004-acute-severity-threshold.md"
    sha: "b3c70dc42457b121a1fb9ef2acb2a99df98bc499"
  - hypothesis: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    file: "entities/synthesis/0005-reproductive-stage-immune-homeostatic-margin.md"
    sha: "24dd96c99dff230c10984feca1eb509aeaeb6fff"
  - hypothesis: "hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem"
    file: "entities/synthesis/0006-skeletal-muscle-ischemic-mitochondrial-pem.md"
    sha: "f160bfee7d9f6d7c7b5fdce10d0651e302724805"
  - hypothesis: "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
    file: "entities/synthesis/0007-autoimmune-sfn-peripheral-dysautonomia-substrate.md"
    sha: "ba2d9d0fd72554df1a201d1173a80910f6c7671d"
  - hypothesis: "hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent"
    file: "entities/synthesis/0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent.md"
    sha: "0d82dbacede1ee127162483be92ef00dd116ebda"
  - hypothesis: "hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
    file: "entities/synthesis/0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune.md"
    sha: "76989919e7b5e016faee96d1413f45a942b7b983"
  - hypothesis: "hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a"
    file: "entities/synthesis/0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a.md"
    sha: "731ba03c8c57119d68943fd34bc3510b062f6c71"
  - hypothesis: "hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only"
    file: "entities/synthesis/0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only.md"
    sha: "3e006256454939928d16138bdaeff0a24cb4c364"
  - hypothesis: "hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune"
    file: "entities/synthesis/0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune.md"
    sha: "8ac7eb9919423da0ff7302f4342234bb75647a43"
  - hypothesis: "hypothesis:0013-ido1-ido2-bistable-tryptophan-metabolic-trap"
    file: "entities/synthesis/0013-ido1-ido2-bistable-tryptophan-metabolic-trap.md"
    sha: "c84ab2ce6658139ddcba37af9bb7b01865457812"
  - hypothesis: "hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation"
    file: "entities/synthesis/0014-nk-failure-clear-senescent-endothelium-sasp-propagation.md"
    sha: "b427b8b89ef8d214a28ecf5367e7d2792cbd1cf5"
  - hypothesis: "hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais"
    file: "entities/synthesis/0015-ebv-reactivation-consequence-not-cause-of-pais.md"
    sha: "cba4083bccd33e2a23db35dff4cc0e176ee3c45a"
  - hypothesis: "hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker"
    file: "entities/synthesis/0016-fibrinaloid-microclots-nonspecific-inflammatory-marker.md"
    sha: "59f1c58b9a22c18079b46cc32a0f457140e56db0"
  - hypothesis: "hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific"
    file: "entities/synthesis/0017-pem-overdiagnosed-via-self-report-nonspecific.md"
    sha: "ed5254e20af61d23b36bc36934446ff4e2bc2a08"
  - hypothesis: "hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver"
    file: "entities/synthesis/0018-circulating-antigen-as-severity-biomarker-not-driver.md"
    sha: "d82cb89d8c30a266dec6a337745a473e76523cb7"
emergent_threads_sha: "351f28346471a0f8befa6146a5b28a739553fe1e"
orphan_question_count: 19
---

## TL;DR

- The project now spans **18 hypotheses** — a positive mechanistic core (h0001–h0007, h0013, h0014), a deliberately built **deflationary null battery** (h0010–h0012, h0015–h0018), and a methodological meta-hypothesis (h0008). Every mature mechanism now has an explicit contrarian counterpart, and the graph marks the developed claims `evidential_fragility(contested)`.
- The single most load-bearing empirical result this cycle is negative: acute **serum IL-6 does not rank cross-pathogen fatigue risk** (`interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk`), and the Dubbo cohort shows *severity — not cytokine identity* — predicts post-infective fatigue, closing the serum-cytokine proxy route and redirecting the imprinting test to direct monocyte ATAC-seq (`pre-registration:0006`; from h0001, h0004, h0011, h0012).
- The **shared-molecular-signature** claim remains unproven and is now bounded by a demonstrated *identification ceiling*: public-corpus cross-PAIS pathway-rank concordance sits at or below the sampling floor and fails closed (`interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`; from h0001). A purpose-built K≥3 harmonized cohort is the only route through.
- The **strongest objective signals** are domain-local, not global: the male-biased vascular hard-endpoint reversal survives severity restriction (`proposition:0012`; from h0004, h0005), skin-biopsy SFN recurs across triggers but is non-specific against hEDS (from h0007), and long-COVID persistent JAK-STAT/IL-6 activation with CD8 exhaustion is documented beyond 180 days (`proposition:0025`; from h0003).
- The project's positive claims mostly **grade speculative at the conjunctive-bundle level** despite individual supported pillars — antigen persistence is real (`proposition:0022`; from h0002) but pathogen-agnostic reservoir initiation is not; the immune-exhaustion loop's *descriptive* state is evidenced but its *causal* leg is data-gated on the abrocitinib/JAK1 readout (`pre-registration:0004`; from h0003).
- **Multiple decisive tests are data-gated, not idea-gated**: banked-PBMC monocyte ATAC-seq (from h0001, h0004), the harmonized provoked-muscle protocol (`pre-registration:0005`; from h0006), cross-syndrome paired biopsy with primary-dysautonomia controls (`pre-registration:0003`; from h0007), and the JAK1 target-engagement readout (from h0003). Decisions D-004 (gated-EHR) and D-005 (seed-stage computational gate) bound what is executable.
- **19 orphan questions** (up from 1) now sit outside the hypothesis lattice, clustering into two candidate frames the project does not yet own: upstream innate nucleic-acid sensing (cGAS-STING / NLRP3) and a host-immune-baseline vulnerability gate.

## State

The project collectively believes PAIS across triggers shares a **failed-recovery phenotype**, but it has repeatedly declined to promote any single unifying molecular mechanism to supported status. What is genuinely established is narrow and domain-local: antigen fragments persist post-clearance with bioactivity (`proposition:0022`; from h0002); a dissociated, persistent inflammatory/exhaustion state exists in long COVID beyond 180 days (`proposition:0025`; from h0003); the post-acute female excess concentrates in self-report domains while hard endpoints are sex-null or male-reversed (`proposition:0008`, `proposition:0012`; from h0005); and skin-biopsy small-fiber neuropathy recurs across long COVID, ME/CFS, and PTLDS (from h0007). Each of these is a *pillar*, not a *system*: the conjunctive hypotheses that would turn them into mechanisms (pathogen-agnostic reservoir initiation, a causal exhaustion loop, a menopause-specific threshold, an autoimmune SFN substrate) all remain speculative or candidate.

The strongest evidence sits in the sex/vascular and SFN domains; the weakest sits in the dynamical and cross-trigger-convergence claims, which the project cannot adjudicate without dense longitudinal or harmonized-cohort data it does not yet have. What is most contested is the **shared-vs-heterogeneous** axis: h0001's shared attractor now faces four explicit deflationary rivals (h0010 gradient-not-attractor, h0011 severity-fatigue dissociation, h0012 nonspecific sickness-behavior, and the omnibus `question:0017`), and the cross-PAIS rank probe demonstrated current public data *cannot* arbitrate the finite-repertoire null (`interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed`; from h0001). The cycle's most consequential development is methodological: h0008 formalized measurement-channel bias into a *predictive prior* — self-report and selection-enriched claims attenuate under objective re-measurement (6/9 determinate corpus claims artifact-consistent, `interpretation:0015-t055-measurement-channel-audit-of-pais-group-differences`; from h0008) — with a load-bearing bounded exception set (n=3) that keeps it falsifiable.

## Arc

The active hypotheses are best read as a **positive core and its shadow**: for nearly every mechanistic claim (h0001–h0005, h0013, h0014) the project has instantiated a matched deflationary null (h0010–h0012, h0015–h0018), so cross-trigger convergence, severity gating, PEM, EBV reactivation, microclots, and circulating antigen each have a driver reading and an epiphenomenon reading competing over the *same* observables. The framing tension across all active hypotheses is whether PAIS is one shared state realized heterogeneously or a family of trigger-specific processes that merely *look* alike through noisy measurement channels — and the project's own tooling (from h0008; the t117 identification floor from h0001) argues this cannot be settled with existing public data.

**h0001 (shared attractor)** moved from prose-only to a degenerate-realization frame separating the descriptive state-shift from the causal mediation claim; its computational probes returned non-arbitrating and fail-closed, leaving the conjecture intact but molecularly unadvanced (`interpretation:0001`, `interpretation:0038`). **h0002 (tissue reservoir)** gained one supported pillar (fragment persistence, `proposition:0022`) but declined promotion twice for want of a non-Borrelia controlled reservoir vehicle (`interpretation:0017`, `interpretation:0028`). **h0003 (immune-exhaustion feedback)** resolved the Aid2025-vs-Ryan2022 IFN contradiction as a dissociated signature and registered the abrocitinib/JAK1 trial as its causal test, now awaiting a target-engagement-valid readout (`interpretation:0012`, `interpretation:0016`). **h0004 (acute-severity threshold)** established a well-supported male vascular hard-endpoint reversal surviving severity restriction (`proposition:0012`) while its central change-point/bistability test (`question:0003`) stays unexecuted. **h0005 (reproductive-stage margin)** is the most evidence-dense line — a measurement-channeled female excess with one bounded testosterone-conditioned immune exception (`proposition:0013`) — but Shah2025's within-band menopause null disputes a menopause-specific reading and no admissible HRT→PAIS estimate exists.

Among the deflationary actives: **h0010 (gradient-not-attractor)** and **h0011 (severity-fatigue dissociation)** both sharpen h0001/h0004 but are pressured by the Dubbo cohort, which found severity *does* predict post-infective fatigue (`interpretation:0039`; from h0011). **h0012 (nonspecific neuroimmune)** draws suggestive support from the same IL-6-null result yet remains compatible-with rather than a clean rival to h0001. **h0013 (IDO bistable trap)** and **h0014 (NK/senescence clearance failure)** are one-source mechanistic conjectures; h0013 is under directional tension because long-COVID metabolite data show the IFN-type (low-Trp/high-Kyn) pattern opposite to the trap's prediction. **h0015 (EBV epiphenomenon)**, **h0016 (microclots nonspecific)**, **h0017 (PEM over-diagnosed)**, and **h0018 (circulating antigen as biomarker)** are each anchored to real observational dissociations (Peluso2022; Mateu2026/Altmann2023) but await the severity-adjusted or objective-re-measurement tests that would convert them from framing devices into adjudicated nulls.

## Research fronts

Ranked across active hypotheses by uncertainty density, recent activity, and task priority:

1. **The harmonized cross-pathogen cohort (K≥3, ~1000-set resolution).** The binding lever for the entire shared-vs-heterogeneous debate; the t117 identification floor proved public data cannot substitute (from h0001, h0011, h0012; `question:0001`, `question:0050`).
2. **Direct HSPC epigenomic imprinting via banked-PBMC monocyte ATAC-seq.** Serum IL-6 proxy is closed; `pre-registration:0006` is the specified vehicle, gated on specimen access (`task:t121`; from h0001, h0004, h0011).
3. **The JAK1 causal readout (abrocitinib / NCT06597396).** The decisive driver-vs-marker test for the exhaustion loop; primary completion passed with no posted results and unverified target engagement (from h0003; `pre-registration:0004`).
4. **The vascular sex×severity interaction.** Post-acute male CV-mortality excess is established; late ambulatory VTE persistence (31–180 d) and COVID-specific-vs-baseline-carryover attribution remain open (from h0004, h0005; `question:0019`, `question:0021`).
5. **Formal change-point / bistability modeling across pathogens.** The unexecuted core test separating h0004's threshold from h0010's gradient and h0011's phenotype split (from h0004, h0010; `question:0003`, `question:0008`).
6. **The antigen-clearance estimand.** Existing nulls are uninterpretable without demonstrated target engagement; an antigen-positive-enriched, clearance-confirmed trial arbitrates h0002 vs h0018 (from h0002; `question:0002`).
7. **Severity-adjusted / objective re-measurement tests for the deflationary battery** — EBV temporal ordering (from h0015; `question:0054`), matched-inflammatory-control microclot assay (from h0016; `task:t104`), objective PEM concordance (from h0017; `question:0049`).

## Candidate frames

**h0006 (skeletal-muscle ischemic-mitochondrial PEM)** — *partial provenance.* P1/localization (bioenergetic deficit localizes to skeletal muscle) is supported but contested via Appelman2024 plus the newly-ingested ME/CFS muscle body (`interpretation:0019-t056-mecfs-muscle-bioenergetics-ingestion`; from h0006); P2–P4 (microvascular hypoperfusion, Na⁺/Ca²⁺ overload, self-perpetuating AIMM) rest on a single-group, model-heavy account with disclosed COI (Scheibenbogen2024). The decisive gap is endpoint-harmonization: no ME/CFS arm has reproduced the Appelman-type provoked post-exertional OXPHOS/SDH biopsy time-course, which `pre-registration:0005` specifies as the A1-vs-M3 adjudicator (from h0006).

**h0007 (autoimmune small-fiber-neuropathy substrate)** — *high provenance, heavily contested.* The structural lesion (P1) is net-supported across triggers against 0% controls but includes a preserved adjudicated ME/CFS null (Walitt2024), and Novak2026 delivered the first single-protocol two-trigger convergence *while simultaneously* surfacing a specificity caveat — hEDS shows comparable small-fiber loss (from h0007; `interpretation:0013`). The autoimmune/anti-GPCR route (P3/P18) is contested: deSa2026 IgG passive transfer causally produces SFN but via non-GPCR antigens, while Hall2022 erased binding-ELISA seroprevalence as evidence. Both promotion criteria (a clean primary-dysautonomia control arm; an antibody-to-lesion within-subject bridge) remain blocked in `pre-registration:0003` (from h0007).

**h0008 (measurement-channel / ascertainment-bias meta-hypothesis)** — *high provenance.* This is the cycle's structural insight: four separate anomalies embedded in the h0001/h0005/h0006/h0007 lines were recognized as one regularity and formalized into M1–M3, then audited — 6/9 determinate corpus claims artifact-consistent, self-report claims attenuate 4/4, weak-ascertainment claims collapse 3/3 (`interpretation:0015`; from h0008). Promotion criterion #1 is met; criterion #2 (a same-cohort, trigger-matched objective re-measurement of a self-report-established difference) is the open belief-shifting route. Its bounded exception set (`proposition:0012`, `proposition:0013`, `proposition:0025`) is the running meter of genuine objective signal.

**h0009 (immune set-point shift → long-term autoimmune conversion)** — *thin provenance.* Created to give the sole orphan question (`question:0005-latent-to-overt-autoimmunity-conversion`) a formal home; it posits that post-infectious latent autoimmunity is an early marker of a durable set-point shift that, in a susceptible minority, converts to overt autoimmune disease over 5–10 years (from h0009). All three propositions are untested at the conversion step, the sex/ascertainment confound is load-bearing, and `interpretation:0032` established that the genotype-linked latent→overt arm is outside current EHR-codeset reach. No prospective vehicle has been identified.

## Knowledge Gaps (rollup)

No knowledge gaps detected this run.

## Emergent threads

See `entities/synthesis/0009-emergent-threads.md`. Nine questions are genuinely cross-hypothesis (each bridging ≥2 hypotheses at `inverse` confidence — notably `question:0010` at the three-way microclot intersection of h0006/h0014/h0016, and the omnibus `question:0017` spanning the four-hypothesis deflationary cluster). **19 orphan questions** (up from 1 last cycle, driven by the q0023–q0047 expansion batch) sit outside the hypothesis lattice; there are **0 orphan interpretations**. The orphans cluster into two candidate frames the project does not yet own — upstream innate nucleic-acid sensing (cGAS-STING / NLRP3 pyroptosis, `question:0023`, `question:0024`) and a shared host-immune-baseline vulnerability gate (`question:0031`–`question:0034`, `question:0040`) — both flagged in the emergent-threads report as warranting new hypotheses.
