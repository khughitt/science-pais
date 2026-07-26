---
title: 'Gate-0 coverage triage (2026-07-03)'
status: active
created: '2026-07-03'
see_also:
- doc:2026-07-03-data-catalog-expansion-design
---

# Gate-0 coverage triage

Baseline: `coverage-baseline-2026-07-03.json` (31 targets: 22 no-candidate, 9 missing-capabilities).
Post-Gate-0: `coverage-postgate0-2026-07-03.json` (31 targets: 22 no-candidate unchanged in count,
9 formerly-`missing-capabilities` targets now resolved to `covered-unstaged` ×4, `capability-mismatch`
×3, `covered-pointer` ×1, `covered-runnable` ×1, per Tasks 3-4).

Every `no-candidate` target is triaged below as **reconcilable** (an existing dataset could be
`related:`-wired to it) or **genuine-discovery** (no cataloged dataset reaches it). Classification is
anchored to the *already-annotated* `provided_capabilities` on the 20 datasets (Task 3) and the
capability vocabulary (`doc/plans/2026-07-03-capability-vocabulary.md`), not to speculative prose
near-misses — a wrong "reconcilable" call is worse than an honest "genuine-discovery" per the task
brief. Two corpus-wide facts drove most of the genuine-discovery calls: (1) the `outcome` tokens
`pem`, `autoimmune-dx`, `dysautonomia`, `recovery-status` and the `stratification: severity` token are
defined in the vocabulary but used by **zero** of the 20 annotated datasets; (2) no dataset carries an
assay/outcome token for functional autoantibody titers, redox/oxidative-stress biomarkers, cognition,
vascular/coagulation biomarkers, single-cell profiling, or trial/RCT outcomes — these are simply not
represented in the catalog yet.

`D-004` (2026-07-01, `core/decisions.md`) shelved the `task:t078`/`t079` autoimmune-diathesis × sex ×
PASC EHR estimand as infeasible-under-transparency-standards: N3C and OpenSAFELY are both classified
`trust-based-output`, below the project's `third-party-reproducible` reproducibility bar
(`science.yaml` `reproducibility_policy: below_bar: halt`). Where a no-candidate target's core need is
exactly that shelved estimand (h0009, q0005), this triage treats wiring the same gated vehicles to a
new target as re-opening a decision made two days prior, not as a reconciliation — so those stay
genuine-discovery even though the datasets carry superficially-adjacent capability (e.g. N3C's
OMOP autoimmune-stratum granularity, confirmed in its own `BC-3` note).

## Triage table

| target | class | note (dataset to wire / modality needed) | wave |
|---|---|---|---|
| hypothesis:0002-tissue-reservoir-antigen-fragment | genuine-discovery | Needs a tissue-resident-macrophage pathogen-fragment persistence assay in ≥1 non-Borrelia PAIS (tissue/plasma antigen quantification, e.g. TLR2/ELISA-type). Task 2 already confirmed zero reconcilable prose citations here (`recover-adult`'s "RECOVER" prose hits were the plain-English word, not the cohort; recover-adult has no muscle/tissue-antigen assay regardless) — reused, not re-litigated. | 2 |
| hypothesis:0003-immune-exhaustion-feedback | genuine-discovery | Needs single-cell profiling that localizes the persistent IL-6/JAK-STAT signal + exhaustion markers (PD-1/TOX/TIM-3) within individuals, or JAK1-inhibitor RCT outcome data with symptom+pathway co-endpoints. Task 2 confirmed zero reconcilable prose citations. `impacc-immunophenotyping-covid` has bulk-RNA+Olink (annotated) and CyTOF (body-mentioned but never annotated as a capability) but is acute-hospitalized-only, not the >180-day chronic-exhaustion window this hypothesis needs. | 2 |
| hypothesis:0004-acute-severity-threshold | genuine-discovery | Needs an acute-severity-*stratified* longitudinal cohort (`stratification: severity`) — that token is unused by all 20 annotated datasets, including the 3 EHR candidates (`all-of-us-covid`, `n3c-recover-longcovid`, `uk-biobank-covid`) that plausibly record hospitalization tier. Task 4's own concern #1 flagged this exact check as unresolved; `n3c-recover-longcovid`'s BC-6 note confirms severity *is* dateable there in principle, but N3C's real-data tier is the exact vehicle D-004 shelved as below the reproducibility bar — treating that as a ready reconciliation here would quietly re-import the same gating problem. Left genuine-discovery per the brief's ambiguous-case tie-break. | 1 |
| hypothesis:0005-reproductive-stage-immune-homeostatic-margin | **reconcilable** — `dataset:uk-biobank-covid` (secondary: `dataset:my-lc-iwasaki-klein`) | Both datasets already carry the *existing* tokens `outcome: sex-hormone-level` + `stratification: sex` (uk-biobank: pre-infection SHBG panel, prospective-longitudinal; my-lc: testosterone directly predicts symptom burden, case-control) — no new vocabulary or capability authoring needed, only a `related:` edge. Both are already wired to h0005's own stated "primary framing question," `question:0013-reproductive-stage-failed-immune-recovery-after-infection` — h0005 itself was simply never `related:`-linked. Task 2 only grepped the 3 explicitly-flagged hypothesis bodies (h0002/h0003/h0006) for prose citations; no task in this wave did general `related:`-edge repair across *all* no-candidate targets against already-annotated capabilities, which is why this fell through. (The design doc separately plans a Wave-1 causal-MR/sex-hormone-GWAS angle for h0005 — that is additive to, not a substitute for, this descriptive wiring.) | n/a — wireable now, not wave-gated |
| hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem | genuine-discovery | Needs an independent provoked muscle-biopsy time-course (pre / immediately-post / 24-48h post-exertion) measuring mitochondrial function *and* intracellular Na+/Ca2+, paired with peripheral-vs-central CPET decomposition. Task 2 confirmed the flagship "RECOVER → h0006" design example does not survive a literal read: all 4 "recover(y)" hits in the body are the plain English word, and recover-adult has no muscle-tissue/mitochondrial assay regardless — reused, not re-litigated. | 2 |
| hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate | genuine-discovery | needs open SFN/autonomic dataset; t050-gated | 2 |
| hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune | genuine-discovery | Needs a prospective post-infectious cohort with baseline autoantibody-breadth profiling *and* ≥3-5yr autoimmune-disease-incidence follow-up, sex/ascertainment-matched (`outcome: autoimmune-dx` is defined but used by zero datasets). `n3c-recover-longcovid`'s OMOP autoimmune-stratum granularity (BC-3: SLE/RA/Crohn's/UC as curated OHDSI cohorts) would partially cover the incidence side, but has no autoantibody-profiling arm at all, and the entire real-data N3C/OpenSAFELY route for exactly this shape of autoimmune×EHR estimand was explicitly shelved under D-004 (2026-07-01, two days before this triage) as infeasible-under-transparency-standards — wiring it here would quietly reopen a closed decision. | 1 |
| question:0002-antigen-clearance-rescues-symptoms | genuine-discovery | Needs an RCT of antigen-clearing agents stratified by baseline antigen positivity, with symptom+biomarker co-endpoints and *tissue* (not plasma-only) antigen quantification. Peluso2024/BrandstetterFigueroa2025 antigen-persistence findings cited in h0002 are literature (`cite:` refs), not ingested dataset entities. | 2 |
| question:0004-convergent-small-fiber-neuropathy-substrate | genuine-discovery | Same substrate gap as hypothesis:0007 — needs a harmonized multi-trigger skin-biopsy SFN/IENFD + QSART/tilt-table protocol with primary-dysautonomia controls (t050-gated; no admissible vehicle currently identified). | 2 |
| question:0005-latent-to-overt-autoimmunity-conversion | genuine-discovery | Needs a multi-year prospective autoantibody-typed cohort with autoimmune-disease-incidence endpoints, stratified by anti-cytokine specificity and pre-existing autoimmunity (`outcome: autoimmune-dx` unused corpus-wide). Same D-004 gating concern as hypothesis:0009 applies to any EHR-diagnosis-only substitute (e.g. N3C) — coded diagnosis alone cannot supply the early-autoantibody-breadth stratifier this question's core claim needs. | 2 |
| question:0006-jak-stat-il6-driver-vs-marker | genuine-discovery | Same substrate gap as hypothesis:0003 — needs JAK1-inhibitor RCT results (symptom+pathway co-endpoints) or single-cell profiling localizing the IL-6/JAK-STAT source; no dataset in the corpus carries a trial-outcome or single-cell/CyTOF capability token. | 2 |
| question:0008-formalize-vicious-cycle-attractor-model | genuine-discovery | Needs one cohort co-measuring antigen/immune, autonomic/vascular, and mitochondrial/metabolic axes simultaneously and longitudinally in the same subjects, for DAG construction / bistability-hysteresis fitting. `impacc-immunophenotyping-covid` comes closest (longitudinal immunophenotype+transcriptomics+PRO, annotated) but is missing the vascular/autonomic/mitochondrial axes, and its own entity already records it as "not an admissible substitute" for the adjacent question:0015 on comparable multi-axis-coverage grounds. | 2 |
| question:0009-functional-autoantibodies-drive-dysautonomia | genuine-discovery | Needs standardized *functional* (receptor-activation, not binding-ELISA) GPCR-autoantibody assays in trigger-matched POTS/dysautonomia cohorts with recovered+healthy controls, ideally with passive-transfer/depletion arms. No dataset or vocabulary token for functional-autoantibody assay exists in the corpus. | 2 |
| question:0010-vascular-microclot-subphenotype | genuine-discovery | Needs a harmonized vascular/coagulation biomarker panel (complement TCC ratios, vWF/ADAMTS13, D-dimer, RHI, platelet/microclot assays) for unsupervised subphenotype clustering, linkable to anticoagulant/complement-modulator trial outcomes. No vascular-biomarker modality or outcome token exists in the vocabulary. | 2 |
| question:0011-mitochondrial-basis-of-pem | genuine-discovery | Needs paired pre/post standardized two-day CPET with multi-omics (metabolomics/proteomics/immune stimulation) across ≥2 triggers with matched recovered controls. `outcome: pem` is defined in the vocabulary but used by zero of the 20 annotated datasets. | 2 |
| question:0012-prevention-vaccination-antiviral-reduces-pais | genuine-discovery | Needs a prospective cohort or RCT of early antiviral/vaccination status with PAIS-incidence endpoints suitable for confounder-adjusted target-trial-emulation, ideally cross-pathogen. `opensafely-longcovid`'s body notes "vaccination records are linked" — a real near-miss — but no vaccination-status token exists anywhere in the capability vocabulary, and OpenSAFELY's real-data tier sits below the reproducibility bar (`trust-based-output`, the same D-004 class) — a documented fact, not yet a confirmed reconciliation. | 1 |
| question:0016-oxidative-stress-upstream-driver-of-bioenergetic | genuine-discovery | Needs an in-vivo redox target-engagement biomarker, ideally paired with provoked-exertion redox kinetics and an antioxidant/metformin RCT with pre/post readouts. No oxidative-stress/redox modality or assay token exists in the corpus. | 2 |
| question:0018-objective-vs-subjective-cognition-dissociation-in | genuine-discovery | Needs a dataset pairing objective neurocognitive-task scores with subjective (CFQ-type) cognitive-complaint measures in the same subjects, sex-stratified, for mediation analysis against fatigue. No cognition-outcome token exists anywhere in the vocabulary (the `outcome` list has `fatigue`/`pem`/`autoimmune-dx`/`dysautonomia`/`recovery-status`/`sex-hormone-level` — no cognition value). | 2 |
| question:0019-male-biased-vascular-signal-pasc-persistence | genuine-discovery | male vascular/VTE — needs open VTE/vascular-by-sex cohort | 1/2 |
| question:0020-male-vte-excess-post-acute-persistence | genuine-discovery | Same open-vascular-by-sex-cohort gap as question:0019 — needs sex-stratified longitudinal VTE incidence beyond 30 days in ambulatory COVID-19 cohorts, or sex-stratified microclot/endothelial-biomarker follow-up at 3/6/12 months. No vascular/VTE outcome token exists in the vocabulary. | 1/2 |
| question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover | genuine-discovery | Same gap family as question:0019/0020 — needs a sex-stratified COVID-vs-uninfected (or test-negative) comparison of post-acute vascular hard endpoints, ideally an ambulatory cohort over the 31-180-day window. | 1/2 |
| question:0022-immune-state-displacement-mediator-vs-co-traveler | genuine-discovery | Needs an immunomodulation trial with demonstrated target engagement and symptom+pathway co-readout, or a longitudinal multi-axis cohort permitting formal mediation with parallel vascular/metabolic/neural lesions measured alongside immune state. No trial-outcome or multi-axis-mediation substrate exists in the corpus; listed under the design doc's Wave-1 causal-identification bucket, but no current wave concretely supplies trial/RCT data — flagged as a residual gap in the wave plan itself, not just the catalog. | 1 |

**Summary:** every no-candidate target in the table above is classified. 1 reconcilable (`hypothesis:0005`, both candidate
datasets already annotated — needs only a `related:` edge, no vocabulary/capability authoring). 21
genuine-discovery. Two (`hypothesis:0009`, `question:0005`) were deliberately kept genuine-discovery
despite superficially-adjacent gated-EHR capability because wiring them would re-open the D-004
shelve decision; two more (`hypothesis:0004`, `question:0012`) were kept genuine-discovery as
ambiguous near-misses per the brief's explicit tie-break instruction, even though a specific dataset
note (N3C's BC-6 severity dateability; OpenSAFELY's linked vaccination records) came close.

## Coverage delta

```
BEFORE Counter({'no-candidate': 22, 'missing-required-capabilities': 9})
AFTER  Counter({'no-candidate': 22, 'covered-unstaged': 4, 'capability-mismatch': 3, 'covered-pointer': 1, 'covered-runnable': 1})
```

The `no-candidate` count is unchanged (22 in both snapshots) because Tasks 3-4 annotated
`provided_capabilities`/`required_capabilities` only on datasets/targets that already had `related:`
edges in the graph — by construction, no-candidate targets have zero such edges, so they were out of
scope for capability annotation. What moved is the *other* 9 targets: all 9 baseline
`missing-required-capabilities` targets now resolve into real coverage states (6 covered across
`covered-unstaged`/`covered-pointer`/`covered-runnable`, 3 legitimate `capability-mismatch` discovery
signals — `question:0003`, `question:0014`, `question:0015`). This triage is what moves the
`no-candidate` count going forward: `hypothesis:0005`'s `related:` edge is Gate-0-actionable now; the
other 21 genuine-discovery gaps feed Wave 1/2 dataset discovery per the table above.
