---
id: "synthesis:rollup"
type: "synthesis"
title: "Project synthesis - health-post-acute-infection"
report_kind: "synthesis-rollup"
generated_at: "2026-06-24T19:16:12Z"
source_commit: "05a785bf71096ea8cc4d486b93f3f920a481cd74"
synthesized_from:
  - hypothesis: "hypothesis:0001-shared-dysregulated-attractor"
    file: "entities/reports/synthesis/0001-shared-dysregulated-attractor.md"
    sha: "d7a12d7c3e82b35cf4661de31d21edf7741426cd"
  - hypothesis: "hypothesis:0002-tissue-reservoir-antigen-fragment"
    file: "entities/reports/synthesis/0002-tissue-reservoir-antigen-fragment.md"
    sha: "6d4b0c1d5818646954bb6dee1cac76e059bb0374"
  - hypothesis: "hypothesis:0003-immune-exhaustion-feedback"
    file: "entities/reports/synthesis/0003-immune-exhaustion-feedback.md"
    sha: "4a3dbf16875e2814c81a6b4095cc8c71c729cf15"
  - hypothesis: "hypothesis:0004-acute-severity-threshold"
    file: "entities/reports/synthesis/0004-acute-severity-threshold.md"
    sha: "c77089f58dc7c728c56cf543881ca38a003e755d"
  - hypothesis: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    file: "entities/reports/synthesis/0005-reproductive-stage-immune-homeostatic-margin.md"
    sha: "eb360eaf2c5f3707f3a9c74d08fa38df2e161eee"
  - hypothesis: "hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem"
    file: "entities/reports/synthesis/0006-skeletal-muscle-ischemic-mitochondrial-pem.md"
    sha: "a8bcdf3bde1de380f96241b3ee235e2830b1d820"
  - hypothesis: "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
    file: "entities/reports/synthesis/0007-autoimmune-sfn-peripheral-dysautonomia-substrate.md"
    sha: "dac8ce5c489a3a844801142e25791c2d271819d1"
emergent_threads_sha: "fc72f460c21dffd01ace3d98c3448a21dd7ace44"
orphan_question_count: 1
---

# Project synthesis - health-post-acute-infection

## TL;DR

- The project's organizing frame — PAIS as a shared failed-recovery state reachable from many triggers (`hypothesis:0001`) — survives at the **symptom/narrative level but not at the shared-molecule level**: the one empirical cross-trigger probe was a non-arbitrating null and PEM's objective correlate is trigger- and endpoint-specific (`proposition:0011`), so a "single shared bioenergetic lesion" reading is actively disfavored.
- A recurring meta-finding now spans four hypotheses: **apparent PAIS biology is frequently a measurement-channel/ascertainment artifact**. The female excess concentrates in self-report channels; SFN biopsy "prevalence" swings 0→91% by definition/trigger/referral choice (`interpretation:0014`); both attenuate or reverse under objective, trigger-matched measurement.
- The **strongest male-biased signal in the project** — a vascular hard-endpoint reversal (VTE aHR 1.69, CV-mortality HR 1.68) — survives severity adjustment across both ambulatory and hospitalized strata (`proposition:0012`), but its COVID-specific-vs-baseline-carryover fraction is unidentified for want of an uninfected comparator (the t048 cohort hunt).
- **Antigen persistence (`hypothesis:0002`) is real but its causal corollary is untested**: pathogen fragments persist (Borrelia pPGᴮᵇ in liver; SARS-CoV-2 spike to 14 months), but every antigen-clearance trial is an *uninterpretable null* — none demonstrated target engagement — so they do not disconfirm the mechanism.
- **The immune-exhaustion IFN contradiction was resolved** (`interpretation:0012`): persistent type-II inflammatory tone alongside tolerized type-I antiviral effectors is one dissociated signature, not two conflicting ones — and is now a registered, falsifiable prediction awaiting the abrocitinib JAK1 trial (NCT06597396).
- Two **candidate** frames sit at the periphery: the SFN-substrate hypothesis (`hypothesis:0007`, the most-worked thread this quarter — lesion existence now well-evidenced, pattern-*specificity* the open question) and the skeletal-muscle ischemic-PEM frame (`hypothesis:0006`, anchored by one independent muscle-OXPHOS result, ionic core unreplicated).
- **A near-universal structural blocker**: the decisive tests across almost every hypothesis are *data-gated*, not idea-gated — harmonized ≥3-trigger multi-omics (h0001), a target-engagement-demonstrated clearance trial (h0002), the abrocitinib readout (h0003), a sex-stratified uninfected-comparator vascular cohort (h0004/h0005), UKB menopause data (h0005), and an admissible primary-dysautonomia-control biopsy vehicle (h0007) all do not yet exist in accessible form.

## State

The project collectively believes that post-acute infection syndromes share a **convergent clinical and physiological phenotype** whose **mechanistic unity is unproven and, at the level of a single shared molecular lesion, currently disfavored**. The strongest, best-replicated empirical facts are not mechanisms but **structure-of-evidence findings**: (1) the female PAIS excess is real but largely measurement-channeled — female-biased in self-report, sex-null or male-reversed on hard objective endpoints (`hypothesis:0005`); (2) a male vascular hard-endpoint reversal is robust to severity adjustment (`hypothesis:0004`, `proposition:0012`); (3) small-fiber neuropathy is genuinely present across triggers against 0% controls, but its apparent prevalence heterogeneity is an ascertainment artifact, not biology (`hypothesis:0007`, `interpretation:0014`).

What is **contested**: the antigen-reservoir hypothesis (`hypothesis:0002`, 2 support / 4 dispute — but the disputes are uninterpretable nulls on a non-core corollary); the reproductive-stage threshold proposition (`proposition:0001`, 3/3 — Shah2025's within-age-band menopause null pressures a menopause-specific reading while leaving an age/immunosenescence threshold live); and the SFN structural/causal legs (`proposition:0014`/`0016`/`0018`, all flagged `evidential_fragility(contested)`, with the Walitt2024 null and Hall2022 specificity null as the live counter-signals). What is **strongest**: the most evidence-dense hypothesis is `hypothesis:0005` (26 support edges across five interpretations); the most decisively *reframed* this quarter is `hypothesis:0003` (the IFN reconciliation). The thinnest legs everywhere are **causal and longitudinal**: persistence ≠ pathogenicity (h0002), correlation ≠ driver (h0003), lesion existence ≠ pattern specificity (h0007).

## Arc

The five active hypotheses form a rough **systemic-to-peripheral stack** over the same failed-recovery process: h0001 (the whole attractor) → h0002/h0003 (two candidate loop-maintenance engines: antigen persistence and immune exhaustion) → h0004/h0005 (two host-susceptibility modifiers: acute-severity threshold and reproductive-stage margin). They are complementary rather than rival, and the project's work this quarter has been less about adjudicating between them than about **disciplining each one's evidence base against measurement and identification confounds**.

**`hypothesis:0001` (shared attractor)** began as narrative convergence and has been progressively constrained: the t035 cross-trigger pathway-overlap probe returned a non-arbitrating null (underpowered 2-cohort public data), and the t025/t044 PEM work formalized that PEM's objective correlate is trigger- and endpoint-specific (`proposition:0011`) — so the conjecture survives at the symptom level while the "one shared lesion" reading does not. The decisive harmonized ≥3-trigger multi-omics test (`question:0001`) does not exist.

**`hypothesis:0002` (antigen reservoir)** resolved this quarter to an honest split: one supported persistence pillar (`proposition:0022`) and two untested distinctive pillars (cross-pathogen generalization `0023`, burden-predicts-chronicity `0024`). The t046/t051 trial-ingestion work established that the antigen-clearance nulls are *uninterpretable* (no target engagement demonstrated), encoded as a target-engagement admissibility gate on `question:0002` so future nulls are not misfiled as disconfirmations.

**`hypothesis:0003` (immune exhaustion)** had its central internal contradiction dissolved: Aid2025's persistent IFN and Ryan2022's IFN-I suppression index different IFN arms (type-II inflammatory vs type-I antiviral-effector), a dissociated tolerization signature that recoded Ryan2022 from dispute to support (`interpretation:0012`). The causal pillar (`proposition:0026`) is now a locked, data-gated prediction on the abrocitinib trial.

**`hypothesis:0004` (severity threshold)** remains the best cross-pathogen organizing principle for chronicity but its formal change-point test (`question:0003`) is unrun; the live work is the male-vascular-reversal thread, where the signal survives severity bracketing (`interpretation:0005`) and the open question is COVID-specificity vs baseline carryover.

**`hypothesis:0005` (reproductive-stage margin)** is the most evidence-dense and the most thoroughly *deflated-and-rebuilt*: the female excess is largely measurement-channeled (`interpretation:0003`), with one bounded testosterone-conditioned objective immune exception (`proposition:0013`); its decisive menopause→PAIS total-effect test is blocked on UKB data (t028).

## Research fronts

Ranked across the active hypotheses by a blend of decisiveness, recent activity, and task priority:

1. **Sex-stratified uninfected-comparator vascular cohort** (from `hypothesis:0004`, also `hypothesis:0005`) — t048 [P2]. The male vascular reversal is the project's most robust hard-endpoint signal, but its infection-attributable fraction is unidentified. A ratio-of-ratios against an age-stratified uninfected comparator (MVP/Al-Aly test-negative, OpenSAFELY, N3C) would resolve `question:0021`. Highest-leverage runnable-ish front.
2. **Abrocitinib JAK1 trial readout** (from `hypothesis:0003`) — t054 [P2]. The one place a registered, falsifiable causal prediction (`pre-registration:0004`) will be tested by an external event; symptom + pathway co-suppression vs pathway-only suppression cleanly separates driver from marker.
3. **UKB menopause→PAIS total-effect** (from `hypothesis:0005`) — t028 [P2, blocked on data provisioning], paired with t037 [QA wiring]. The decisive test of the contested core threshold proposition; idea-complete, data-blocked.
4. **Harmonized ≥3-trigger multi-omics with full-recovery controls** (from `hypothesis:0001`) — `question:0001`. The decisive shared-mechanism test; no admissible dataset exists, so this is a standing data-acquisition target rather than an analysis.
5. **Target-engagement-demonstrated antigen-clearance trial** (from `hypothesis:0002`) — `question:0002`. An antigen-positive-enriched, clearance-verified, timing-armed trial is the missing experiment; until then the persistence pillar cannot promote.
6. **Formal change-point / bistability modeling** (from `hypothesis:0001`, `hypothesis:0004`) — `question:0008`/`question:0003`, with t011's quarantined viral-dynamics ODE papers as candidate substrate. The attractor and threshold claims remain qualitative.

Knowledge-gap note: the topic-gap computation returned empty this run; per-hypothesis fragility flags (the `evidential_fragility(contested)` markers on h0002, and on `proposition:0014`/`0016`/`0018` under h0007) are the live gap signals and are rendered in those files.

## Candidate frames

**`hypothesis:0006` (skeletal-muscle ischemic-mitochondrial PEM)** — candidate. A tissue-specific instantiation of h0001 proposing an "acquired ischemic mitochondrial myopathy." Its strongest anchor is independent: Appelman2024's long-COVID muscle OXPHOS impairment that worsens after provoked PEM, with a selective post-exertional Complex II fall (via `proposition:0011`). But the ionic-cascade core (P3) and self-perpetuation (P4) are single-group/unreplicated (Scheibenbogen/Wirth, COI disclosed), the whole-body 2-day-CPET decrement does not transfer from ME/CFS to long COVID at the same endpoint, and the central effort-preference rival (Walitt2024) still pressures muscle localization. Promotion needs ≥1 independent replication of post-exertional muscle Na⁺/mitochondrial escalation and a two-cohort demonstration that peripheral O₂ extraction limits day-2 CPET.

**`hypothesis:0007` (non-length-dependent autoimmune SFN substrate)** — candidate; the most actively worked thread this quarter. Across t049 → t006 → t050 → the metric-harmonization re-analysis, the state sharpened decisively: P1 (lesion existence) is now well-evidenced and P4 (cross-trigger convergence) was quality-upgraded to a single-protocol two-trigger demonstration (Novak2026), while P2 (non-length-dependent pattern) remains "asserted more than measured" and P3 (autoimmune causation) is causally anchored only for non-GPCR antigens in a mouse passive-transfer model (deSa2026). The consequential new result is a **specificity caveat**: hEDS, a non-infectious dysautonomia, carries comparable-or-greater SFN, shifting the binding question from "does the lesion exist?" to "is its pattern specific vs primary dysautonomia?" Both promotion criteria are blocked — #1 on the missing primary-dysautonomia-control biopsy vehicle (`pre-registration:0003`, data-gated; the Novak group is "one protocol amendment away"), #2 on the untested functional-antibody-to-lesion bridge (t006). A standing convention emerged: SFN-prevalence claims are uninterpretable without stating trigger + biopsy modality + site protocol + cutoff rule.

## Knowledge Gaps (rollup)

No knowledge gaps detected this run (the `compute_topic_gaps` slice was empty). The live gap signals this pass are the graph fragility flags — `evidential_fragility(contested)` on `hypothesis:0002` and on `proposition:0014`/`0016`/`0018` (h0007) — surfaced in the respective per-hypothesis files.

## Emergent threads

See `entities/reports/synthesis/_emergent-threads.md`. **One orphan question** (`question:0005-latent-to-overt-autoimmunity-conversion`) has no hypothesis home: it concerns the *longitudinal* conversion of post-infectious latent autoimmunity (Rojas2022: 83% latent, ~3% overt at 7 months) to clinical disease, a prognosis question no current mechanism-focused hypothesis frames — the emergent-threads file proposes a candidate "immune-set-point shift" hypothesis to house it. The file also documents four genuinely cross-hypothesis questions (functional autoantibodies `q0009` bridging h0007↔h0001; mitochondrial PEM `q0011` bridging h0006↔h0001; female predominance `q0007` and male-vascular `q0019` jointly conditioning h0004↔h0005), and flags the measurement-ascertainment axis as a candidate standing meta-constraint spanning h0001/h0005/h0006/h0007.
