---
id: "synthesis:rollup"
type: "synthesis"
title: "Project synthesis - health-post-acute-infection"
report_kind: "synthesis-rollup"
generated_at: "2026-06-24T03:28:17Z"
source_commit: "eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec"
synthesized_from:
  - hypothesis: "hypothesis:0001-shared-dysregulated-attractor"
    file: "entities/reports/synthesis/0001-shared-dysregulated-attractor.md"
    sha: "310d48b294ad3e299e5f94e85ae4fd06f7beb209"
  - hypothesis: "hypothesis:0002-tissue-reservoir-antigen-fragment"
    file: "entities/reports/synthesis/0002-tissue-reservoir-antigen-fragment.md"
    sha: "36923e665baddab57080fdbe5a4e9493c8bd9912"
  - hypothesis: "hypothesis:0003-immune-exhaustion-feedback"
    file: "entities/reports/synthesis/0003-immune-exhaustion-feedback.md"
    sha: "26323472618c6fd835e582e5a50c9a900fcbd084"
  - hypothesis: "hypothesis:0004-acute-severity-threshold"
    file: "entities/reports/synthesis/0004-acute-severity-threshold.md"
    sha: "29b8473cb82de338ab6fc7e0fed4a4332fb686a2"
  - hypothesis: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    file: "entities/reports/synthesis/0005-reproductive-stage-immune-homeostatic-margin.md"
    sha: "35371ab7cc14bc4959e3a2911b5f4371dab1352e"
  - hypothesis: "hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem"
    file: "entities/reports/synthesis/0006-skeletal-muscle-ischemic-mitochondrial-pem.md"
    sha: "9ea9e0586c7c636af294e59f768485af68f6191c"
emergent_threads_sha: "d289b3edd4f1dcc442cff348c6aafcb380831ade"
orphan_question_count: 2
---

## TL;DR

- The project's organizing conjecture — that PAIS is a **shared dysregulated attractor** reachable from many triggers (`hypothesis:0001-shared-dysregulated-attractor`) — is supported at the symptom and review level but **not yet at the shared-mechanism level**: the one cross-trigger transcriptomic test returned a non-arbitrating null (ρ = −0.563, underpowered), and the deflationary "coincidence-of-repertoire" rival remains genuinely competitive.
- The empirically richest and most contested front is **sex / reproductive-stage** (`hypothesis:0005-reproductive-stage-immune-homeostatic-margin`, `well_supported` but contested, risk 4.50): a robust crude female PAIS excess that, on decomposition, **channels largely through self-report measurement** and **reverses to male-biased in hard vascular/thrombotic endpoints**.
- The **male vascular reversal survives coarse acute-severity adjustment** (`proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment`), making it a live bridge between the severity-threshold (`hypothesis:0004-acute-severity-threshold`) and reproductive-stage (`hypothesis:0005`) accounts — and showing the vascular domain is not gated by hospitalization-level severity.
- A project-wide **measurement-vs-biology** theme recurs: apparent sex effects, case-definition heterogeneity (`question:0014`/`question:0015`), and PEM correlates all raise the worry that signal is ascertainment artifact rather than pathophysiology.
- **PEM has no single shared substrate**: `proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode` shows the ME/CFS whole-body 2-day-CPET decrement does not transfer to long COVID, tensioning both the attractor frame (h0001) and the candidate muscle-lesion frame (`hypothesis:0006`).
- Two mechanistic hypotheses — **antigen-reservoir** (`hypothesis:0002-tissue-reservoir-antigen-fragment`) and **immune-exhaustion feedback** (`hypothesis:0003-immune-exhaustion-feedback`) — remain at initial framing with **zero deposited analytical work**; they are structured conjectures awaiting their first test.
- The single highest-value pending test, the pre-registered **UKB menopause→PAIS total-effect analysis** (`task:t028`), is **data-gated and unrun**; the project's confirmatory empirical engine has not yet turned over.

## State

The project collectively believes that post-acute infection syndromes plausibly share a failed-recovery physiology, but it holds this as an organizing conjecture rather than a demonstrated fact. The strongest *structural* evidence sits in `hypothesis:0004-acute-severity-threshold`: divergent multi-year trajectories (hospitalized PASC elevated through year three vs. near-baseline recovery in non-hospitalized patients) plus cross-pathogen severity-outcome associations (Q-fever ~20% chronic fraction; severe dengue predicting post-dengue fatigue) are more consistent with threshold-crossing than a pure dose-response gradient.

The most *developed* evidence base is the sex/reproductive-stage program (`hypothesis:0005`). Here the project has done real adjudication: a crude female excess that replicates across COVID, dengue, and Q-fever decomposes into a **measurement-channel axis** — self-report domains female-biased, objective/hard endpoints sex-null or reversed (`proposition:0008`, `proposition:0009`, `proposition:0010`). The one surviving objective female-biased signal is a bounded, testosterone-conditioned immune/inflammatory exception (`proposition:0013-immune-domain-partial-hormone-mediated-objective-exception`).

What is contested is whether reproductive-stage *biology* (as opposed to age/immunosenescence or measurement) drives any of this. `proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold` is evenly split (support 3, dispute 3): a within-age-band menopause null leaves the menopausal-status reading unsupported, and `interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test` finds **no admissible direct HRT→PAIS causal estimate** in the corpus. Across the project, no hypothesis yet rests on `has_empirical_data`; belief states reflect literature posture, and the decisive computational tests are either unrun (h0005) or non-existent in public data (h0001, h0006).

## Arc

**`hypothesis:0001-shared-dysregulated-attractor` (the umbrella).** Opened as a convergence-of-triggers conjecture grounded in narrative ME/CFS–long-COVID parallels. Its first empirical probe (`interpretation:0001`, the t035 cross-trigger pathway reanalysis) halted at a pre-registered non-arbitrating null, and the PEM-stratified work (`interpretation:0004`, `interpretation:0007`) established that the decisive within-cohort molecular contrast does not exist in accessible data. Position: organizing frame intact, shared mechanism unproven.

**`hypothesis:0004-acute-severity-threshold`.** Opened from cross-pathogen severity associations and the VA-cohort trajectory split. Its one investigative move (`interpretation:0005-t042`) tested whether the male vascular signal is severity-confounded and found it survives both low- and high-severity strata, minting `proposition:0012` and bounding the threshold frame: the vascular domain expresses below the hospitalization threshold. The formal change-point test (`question:0003`) is still open.

**`hypothesis:0005-reproductive-stage-immune-homeostatic-margin`.** The most worked arc, with the project's richest `sci:amends` chain: t013 cross-trigger effect sizes (`interpretation:0002`) → t018 six-domain decomposition (`interpretation:0003`) → t041 objective-domain search (`interpretation:0006`) + t042 vascular adjustment (`interpretation:0005`) + t019 HRT audit (`interpretation:0008`). It moved from a plausible female-predominance framing to a measurement-channeled, bounded-hormone-exception, contested-core position with its confirmatory test still data-gated.

**`hypothesis:0002-tissue-reservoir-antigen-fragment` and `hypothesis:0003-immune-exhaustion-feedback`.** Both seeded 2026-06-11 and still at initial framing. h0002 assembles a pathogen-agnostic persistence mechanism (McClune2025 Borrelia peptidoglycan backbone; Peluso2024, Morroy2016 analogical support) behind one open question (`question:0002`). h0003 proposes an antigen→innate-inflammation→CD8 exhaustion→failed-resolution loop (Aid2025, Ryan2022) behind `question:0006-jak-stat-il6-driver-vs-marker`. Neither has a single interpretation, task, or graph proposition deposited.

These five active hypotheses relate as a **layered explanation stack**: a shared end-state (h0001) reached above a severity threshold (h0004), maintained by an immune-exhaustion engine (h0003) possibly fueled by an antigen reservoir (h0002), with reproductive-stage/sex (h0005) as a cross-cutting risk modifier whose strongest objective trace runs *opposite* the expected direction in the vascular domain.

## Research fronts

Ranked across active hypotheses by uncertainty density, recent activity, and task priority:

1. **UKB menopause→PAIS total-effect test** — `task:t028` (P2, BLOCKED on data provisioning); the contested core (`proposition:0001`) cannot move without it. *from 0005-reproductive-stage-immune-homeostatic-margin*
2. **Endogenous-hormone mediator vehicles** — `task:t039` (All of Us hormone coverage) and `task:t040` (RECOVER ancillary biospecimen panel) are the live paths to break reverse-causation ambiguity. *from 0005*
3. **Cross-pathogen change-point / bistability modeling** — `question:0003`, the unrun formal test that would most efficiently move the severity-threshold frame in either direction. *from 0004-acute-severity-threshold*
4. **Harmonized ≥3-trigger multi-omics with recovery controls** — `question:0001`, the only design that can arbitrate shared-mechanism vs. deflationary rival (`question:0017`). *from 0001-shared-dysregulated-attractor*
5. **JAK-STAT/IL-6 driver-vs-marker** — `question:0006`; a JAK-inhibitor RCT co-endpoint would be the most efficient evidence, but no task pursues it yet. *from 0003-immune-exhaustion-feedback*
6. **HRT evidence-gap closure** — `task:t045` (Neuhouser2024 WHI triage) and `task:t043` (Boneva2015 ME/CFS early-menopause direction). *from 0005*
7. **Antigen-clearance-rescues-symptoms** — `question:0002`; human tissue evidence is indirect and no clearance trial is coded. *from 0002-tissue-reservoir-antigen-fragment*

## Candidate frames

`hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` (candidate) proposes that PEM's primary substrate is an acquired ischemic mitochondrial myopathy in skeletal muscle — microvascular hypoperfusion → ionic dysregulation → mitochondrial damage in a self-perpetuating cycle. Its strongest independent anchor is Appelman2024 (baseline-impaired long-COVID muscle OXPHOS worsening after provoked PEM, with a selective post-exertional Complex II fall), reaching the hypothesis through `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`; Joseph2023 invasive-CPET adds peripheral-O₂-extraction support. But the ionic-cascade core and self-perpetuation claim rest on a single (COI-disclosed) group and an unreplicated ²³Na-MRI anchor, and `proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode` shows the whole-body CPET decrement does not transfer across triggers — so the muscle frame is plausible for long COVID but cannot be assumed to generalize. Promotion requires independent replication of elevated intracellular muscle Na⁺ (or post-exertional escalation of muscle mitochondrial damage) in a PEM-positive cohort with controls, plus two-cohort confirmation that peripheral O₂ extraction limits day-2 CPET.

## Knowledge Gaps (rollup)

No knowledge gaps detected this run.

## Emergent threads

Beyond the per-hypothesis arcs, three questions show genuine cross-hypothesis reach — most importantly `question:0019-male-biased-vascular-signal-pasc-persistence`, the live bridge between the severity-threshold (h0004) and reproductive-stage (h0005) frames documented in `interpretation:0005`. Two questions are research orphans with no resolving hypothesis (orphan_question_count: **2**): `question:0004-convergent-small-fiber-neuropathy-substrate` (a possible peripheral-autonomic-neuropathy substrate, addressed by no current hypothesis) and `question:0005-latent-to-overt-autoimmunity-conversion` (long-horizon autoimmune conversion). See `entities/reports/synthesis/_emergent-threads.md` for the full treatment, including two tentatively inferred candidate hypotheses.
