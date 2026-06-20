<!-- Task queue. Use /science:tasks to manage. -->
## [t003] Promote PAIS<->immunity bridge papers to commons once v3 entities/papers promotion is supported
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Blocked by tooling gap (fb-2026-06-11-005). Bridge papers: Choutka2022, Komaroff2025, Klein2023, Rojas2022, Sharma2023.

## [t006] [lit-search] Functional autoantibody (GPCR: beta-adrenergic/muscarinic) literature
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Gap: functional-autoantibody mechanism asserted but specific literature not yet ingested. Relates to question (functional-autoantibodies-drive-dysautonomia), topic:post-infectious-dysautonomia-and-autoimmunity.

## [t007] [lit-search] Microbiome / gut-brain axis in post-infectious syndromes
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Gap: only 1 paper (s10020 gut microbiome PASC). Search: gut dysbiosis, microbial metabolites, serotonin/tryptophan, gut-brain signaling in long COVID and ME/CFS.

## [t008] [lit-search] Pre-infection-baseline longitudinal cohorts (RECOVER and similar)
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Methodology gap: most cohorts lack pre-infection baseline/controls, undercutting causal claims. Identify and characterize the strongest longitudinal designs. Relates to specs/scope-boundaries control-design discipline.

## [t009] [lit-search] Pediatric long COVID and MIS-C
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Gap: batch is adult-focused (Choutka2022 excluded pediatric/ MIS-C). Search pediatric PASC phenotype, MIS-C, and how pediatric post-infectious illness compares to adult PAIS.

## [t010] [lit-search] Reinfection and vaccination effects on PAIS risk and recovery
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Gap: prevention/modification angle. Search effect of vaccination and reinfection on long-COVID incidence and symptom trajectory. Relates to question (prevention-vaccination-antiviral-reduces-pais), hypothesis:0004-acute-severity-threshold.

## [t011] Evaluate the 4 quarantined viral-dynamics ODE papers as modeling substrate for the attractor formalism
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Perevaryukha (Biophysics 2021), Wang (Physica D 2007), Xie (Appl Math Model 2010), Wang-Hu-Liao (JMAA 2014) are within-host viral-dynamics models with delayed immune response, held in ~/downloads. Assess fit as the mathematical substrate for question:0008-formalize-vicious-cycle-attractor-model / hypothesis:0001-shared-dysregulated-attractor.

## [t012] Flag the PAIS family to pan-disease as a disease-label-vs-biology test case
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Long COVID / ME-CFS / PTLDS as distinct disease labels possibly sharing post-infectious biology. Coordinate with ~/d/health/comparisons/pan-disease.

## [t013] Compare female excess across acute and post-acute infection outcomes
- priority: P2
- status: proposed
- aspects: []
- related: [question:0007-mechanism-of-female-predominance-in-pais, topic:menopause-sex-hormones-and-pais-risk, topic:shared-failure-mode-across-pais]
- group: cross-pais-comparison
- created: 2026-06-19

Compare long COVID, PTLD, post-dengue fatigue, and other PAIS evidence to test whether female excess is stronger in post-acute persistence than in acute infection severity, and whether depression/neuropsychiatric outcomes dissociate from somatic fatigue.

## [t018] Compare female and reproductive-stage excess across PAIS subphenotypes
- priority: P2
- status: proposed
- aspects: []
- related: [question:0007-mechanism-of-female-predominance-in-pais, question:0013-reproductive-stage-failed-immune-recovery-after-infection, hypothesis:0005-reproductive-stage-immune-homeostatic-margin, task:t013]
- group: causal-disentanglement
- created: 2026-06-19

Split PAIS outcomes into somatic fatigue/PEM, dysautonomia, vascular-thromboinflammatory, cognitive, pain, mood/depression, and recovery-time phenotypes. Test whether female or reproductive-stage excess is concentrated in specific subphenotypes rather than uniform across all post-infectious symptoms.

## [t019] Audit hormone therapy evidence for PAIS causal inference
- priority: P3
- status: proposed
- aspects: []
- related: [question:0013-reproductive-stage-failed-immune-recovery-after-infection, hypothesis:0005-reproductive-stage-immune-homeostatic-margin, topic:menopause-sex-hormones-and-pais-risk]
- group: causal-disentanglement
- created: 2026-06-19

Separate hormone therapy evidence by acute infection outcome versus post-acute persistence, route, dose, timing, indication, comorbidity, and healthy-user bias. Decide which findings can inform causal PAIS hypotheses and which should remain clinical-screening or symptom-management context only.

## [t021] Promote h0005 prose Proposition Bundle to first-class proposition + evidence-line entities
- priority: P2
- status: proposed
- aspects: []
- related: [hypothesis:0005-reproductive-stage-immune-homeostatic-margin]
- group: causal-disentanglement
- created: 2026-06-19

h0005 currently carries its reasoning as a prose 'Proposition Bundle' (unmigrated style); cycles already uses first-class proposition + evidence-line entities. Promote each bundle item to a neutral, directional proposition with its own support/dispute evidence-lines. Include BOTH causal directions as separate propositions: P-forward (reproductive-stage transition affects post-infectious recovery threshold) and P-reverse (infection/PAIS perturbs the reproductive axis/timing), each evaluated on its own evidence. This is the test bed for the contextual structural-role design (~/d/science/docs/plans/2026-06-19-contextual-structural-roles-design.md) and connects to the t014 DAG (confounder/collider cautions).

### Notes

- 2026-06-19: Design doc revised to v2 (2026-06-19) after review against the June 8 epistemic-edges facet. Framing change for this migration: P-reverse is an ordinary second relational proposition (multi-edge), roled 'rival' on its cito:discusses membership *relative to h0005* — NOT a new causal-edge label. Confounder/collider cautions from t014 are DERIVED from patch topology + query (epistemic-edges §2.1), so do not author them as edge roles. The only thing this migration exercises that is new is membership_role on the bundle edge (core|rival|background).

## [t023] Build v2 of the t014 menopause-PAIS DAG before specification
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-19

Build v2 of the t014 menopause-PAIS causal DAG with the structure the critique flagged as missing.

PREREQUISITE STRUCTURAL FIX (review 2026-06-19): the current graph has a single cardiometabolic-comorbidity node with menopause -> sex-hormones -> comorbidity. Naively adding the recommended comorbidity -> menopause-timing edge to that same node creates a CYCLE. v2 must first SPLIT the node into baseline (pre-infection) comorbidity and menopause-incident comorbidity: baseline-comorbidity -> menopause-timing (makes baseline comorbidity a true confounder -> adjust) while incident comorbidity stays a downstream mediator (menopause/hormones -> incident-comorbidity -> PAIS). Only after the split is acyclic should the new edges be added.

Then add: the baseline-comorbidity -> menopause-timing edge (test both {age} and {age, baseline-comorbidity} adjustment sets), a hospitalization/acute-care ascertainment collider (severe acute -> hospital -> cohort entry), and a calendar-period/variant/vaccination-era node confounding mediator paths. Keep reverse causation (PAIS -> reproductive axis, t021) as a separate acyclic inquiry with exposure fixed at pre-infection stage. Relates: hypothesis:0005, task:t016, task:t021, patch-definition:menopause-pais-causal-dag.

### Notes

- 2026-06-19: Candidate confounder/mediator/alternative set to incorporate in DAG v2 (from the 2026-06-19 confounder review; see doc/methods/2026-06-19-confounder-open-questions-and-staged-amendment.md). CONFOUNDERS (common cause of menopause-timing AND LC; may break {age}-minimal-sufficient): smoking (measured; staged for primary set via t029), BMI/adiposity (ambiguous: confounder vs M1-mediator vs collider — adjudicate role + timing), autoimmune POI / autoimmune common cause, biological frailty / subclinical pre-infection ill-health (non-SES), parity (dual role: staging input AND possible confounder). NEW IDENTIFICATION ARM: Mendelian randomization of genetically-instrumented age-at-menopause -> LC (exogenous to SES/smoking/survival; pleiotropy caveat — menopause loci overlap DNA-repair/immune genes). MEDIATORS (direct-effect/mechanism only, do NOT adjust in total effect): visceral-fat/metabolic shift, estrobolome/gut-microbiome, vasomotor-symptoms/sleep -> autonomic-inflammatory (also a symptom-overlap ascertainment confounder — dual role), iron-status reversal (menstrual loss -> post-menopausal repletion). STRUCTURAL ALTERNATIVES: shielding-behaviour -> infection-timing/variant-era confounding; testing-into-denominator selection (distinct from questionnaire-response M3b); HRT healthy-user / no-open-collider check. Q2/Q4 from the reviewer doc flow here after t029.
- 2026-06-19: TERMINOLOGY SWEEP (reviewer t029 finding, 2026-06-19): the DAG critique correctly states NO valid back-door adjustment set exists while U is latent, yet several docs call {age} the 'unique minimal sufficient set'. DAG v2 must restate these as the 'primary measured adjustment set' (now {age, smoking} after amendment Q1), never 'minimal-sufficient'. Files to correct: doc/methods/2026-06-19-ukb-data-field-specification.md:148,150 (t027 heading + body); doc/inquiries/menopause-pais-causal-dag.md:35; entities/patches/menopause-pais-causal-dag.md:171; entities/plans/2026-06-19-menopause-pais-total-effect-analysis-plan.md:90,152. (pre-reg:0001 + confounder doc already corrected.) Q2/Q3 dispositions to encode in v2: BMI = explicit role edge (confounder vs menopause->adiposity mediator; baseline-vs-incident timing split); autoimmune-POI = distinct etiologic stratum (not generic 20002 adjustment); frailty = selection/competing-risk structure not a primary covariate; parity = staging input + candidate confounder edge (guard against drifting to a reproductive-life-course estimand).

## [t025] Compare PEM-positive vs PEM-negative PASC molecular signatures
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-19

Search for or commission a within-cohort (e.g. RECOVER, IMPACC) proteomic/metabolomic comparison of PEM-positive vs PEM-negative PASC. Single most informative test of the PEM-requirement harmonization policy; addresses question:0015. Data-gated like t015/t005.

## [t026] Evaluate PC-COS core-outcome-set adoption for PAIS analyses
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-19

Assess whether t001/t016 should pre-commit to PC-COS core domains (fatigue, breathlessness, cognitive impairment, QoL) as dimensional outcomes alongside the binary PAIS case variable, enabling continuous cross-study comparison. Follows topic:pais-case-definition-heterogeneity (t002).

## [t028] Execute the pre-registered menopause→PAIS total-effect analysis once UKB data is provisioned
- priority: P2
- status: blocked
- aspects: []
- blocked-by: [pre-registration:0001-menopause-pais-total-effect, task:t032]
- created: 2026-06-19

Data-gated: pre-registration:0001-menopause-pais-total-effect is committed but execution is blocked on the Vehicle-Admissibility Gate (G1 access provisioned, G2 field IDs confirmed, G3 power floor met, G4-G6 sampling/timing/outcome). Standing verdict [?] inconclusive-for-coverage; no bears_on update on h0005 until a provisioned UKB vehicle clears all G-gates. Activate on UKB AMS approval. Primary confirmatory = reproductive-timing exposure -> WHO>=90d long-COVID RR (Route A questionnaire), {age}-adjusted, natal-female. Ref entities/pre-registrations/0001-menopause-pais-total-effect.md.

## [t032] G2 corpus-independence gate: SHBG/sex-hormone prior is single-source (AlcaldeHerraiz2025)
- priority: P2
- status: proposed
- aspects: []
- related: [pre-registration:0001-menopause-pais-total-effect, report:0002-t029-second-pass-menopause-pais-pre-registration-review, task:t028]
- created: 2026-06-20

Carries the G2 out-of-corpus disposition recorded in report:0002 (t029 second pass) and pre-reg:0001 amendment 2. The out-of-corpus second-precedent search found only Gao et al. (JAMA 2024) as a genuinely author-independent UKB precedent (weakly corroborates questionnaire feasibility + survival-to-2020/healthy-volunteer selection; hospitalization-conditioned so unusable for effective-n; tests no hormones). Wang et al. and the Prieto-Alhambra preprint share the AlcaldeHerraiz author network -> NOT corpus-independent. DISPOSITION: questionnaire feasibility/selection weakly corroborated out-of-corpus; effective-n + SHBG-protection signal remain SINGLE-SOURCE and are labelled as such; SHBG prior downgraded to single-source background (mediator-specific / M1-confirm-side, not load-bearing for the primary {age,smoking} total effect). OPEN/OPPORTUNISTIC: find a non-UKB SHBG-or-sex-hormone x long-COVID precedent (RECOVER, German NAPKON, All of Us, Lifelines) that would UPGRADE the SHBG prior from single-source background; would strengthen, not gate. At application: confirm this disposition stands when the AMS basket is finalized. Blocks t028 (soft: t028 is data-gated regardless).

## [t034] Adjudicate scope boundary: post-vaccination (PACVS) and non-infectious fatigue (GWS/fibromyalgia)
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-20

Decide, in specs/scope-boundaries.md + a core/decisions.md entry, whether the 'shared failure mode' attractor (hypothesis:0001) is post-infection-SPECIFIC or a broader chronic-fatigue final common pathway that admits (a) post-COVID-VACCINATION syndrome (PACVS) and (b) non-infectious fatigue syndromes (Gulf War Syndrome, fibromyalgia). Trigger: this round ingested 5 papers that each independently force the question — Halma2026, Bellavite2026, Lesgards2025 (PACVS, all explicitly request scope adjudication; contested/heterodox evidence tier) and Davis2025 (folds GWS+fibromyalgia into a shared lipid/energy/oxidative failure mode). Deliverable: a scope ruling (in / out / boundary-monitor) for PACVS and for non-infectious fatigue, with the inclusion criterion stated (trigger type? mechanism overlap? PEM presence?), feeding a decisions.md entry. Relates to hypothesis:0001, question:0016, topic:shared-failure-mode-across-pais, topic:post-infectious-dysautonomia-and-autoimmunity.

## [t035] Public-data pathway-level cross-trigger transcriptomic reanalysis (GSE14577 + GSE130353) for q0001
- priority: P3
- status: active
- aspects: []
- created: 2026-06-20

Reproducible alternative to the declined Galbraith2011 private-array reanalysis. Test hypothesis:0001 (shared dysregulated attractor) at PATHWAY/gene-set level across two PUBLIC post-infective-fatigue expression datasets spanning DIFFERENT triggers: GSE14577 (Gow2009 - post-infectious CFS PBMC, Affymetrix U133A/B, n=8 PI-CFS + 7 HC, male-only, Fukuda criteria) and GSE130353 (Raijmakers2019 - QFS/CFS/asymptomatic-seropositive/healthy monocyte RNA-seq). Goal: gene-set/pathway-overlap (e.g. GSEA/ORA on immune, oxidative-stress, mitochondrial, apoptosis modules) to test whether a shared pathway-level signature survives where Galbraith2011's gene-level cross-trigger test was negative. CAVEATS to honour: small n, platform heterogeneity (microarray vs RNA-seq - no naive merge; compare at pathway level, not probe/gene), sex skew (GSE14577 male-only), Gow2009 has no stated FDR + low cross-study concordance (treat as exploratory). This is HYPOTHESIS-GENERATING, not the decisive harmonized >=3-trigger study. NOTE: per specs/scope-boundaries.md the project is in literature-synthesis/seed stage ('Primary computational pipelines... until the project is past seed stage'); this is a future/post-seed computational task, recorded so the public-data opportunity is not lost. Decision context: author-contact for Galbraith arrays declined on reproducibility grounds (2026-06-20). Grounded in question:0001, hypothesis:0001, discussion:0002.

### Notes

- 2026-06-20: Prerequisite when started: create formal mixin-dataset-1.0 entities + Frictionless datapackages for GSE14577 and GSE130353 once downloaded (commons-readiness gate). Registry note staged at doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md. Both are commons-promotion candidates after the gate is met.
- 2026-06-20: 2026-06-20: user authorized crossing the seed-stage scope boundary for THIS bounded, public, reproducible reanalysis only (not a general lift of the seed-stage hold). Proceeding plan-first: analysis plan + pre-registration -> data acquisition -> pathway-level pipeline with wired data-QA.
- 2026-06-20: Analysis plan written: entities/plans/2026-06-20-cross-trigger-pathway-overlap-analysis-plan.md (verdict: ready-with-caveats). Data fitness CONFIRMED via plan-analysis: GSE14577 = 7 HC + 8 PI-CFS, male-only, log2 U133A/B PBMC (data in family.soft.gz; series_matrix 404s); GSE130353 = HC/CFS/QFS/QS 10 each, isolated monocytes, MMSEQ gene estimates in per-sample suppl files (NOT counts -> continuous limma). Design: per-dataset limma -> GSEA -> direction-concordant pathway overlap (PI-CFS-vs-HC x QFS-vs-HC) with a pre-committed QS (seropositive-recovered) negative-control veto for fatigue-specificity. Next: light pre-registration of the arbitration rule, then plan-pipeline.
- 2026-06-20: Plan file renamed to entities/plans/0002-cross-trigger-pathway-overlap-analysis-plan.md (id plan:0002-...) to satisfy entity numbering (date-prefix collided on year 2026 with the menopause plan).
- 2026-06-20: Plan revised 2026-06-20 after user code review (6 findings, all accepted). Key changes: (1) PRIMARY overlap test is now NES rank-concordance with a sample-label PERMUTATION null (Fisher-over-correlated-MSigDB-sets was anti-conservative -> demoted to descriptive); (2) specificity now rests on the DIRECT QFS-vs-QS presence contrast (fatigue holding Coxiella exposure constant), with QS-vs-HC reframed as exposure-confounding evidence (the old 'absent-in-QS' veto was weak at n=10); (3) added an acquisition+hash+MMSEQ-scale BLOCKING gate before execution (only metadata files retrieved so far; MMSEQ payloads not downloaded); (4) deferred-CEL choice justified via GSEA rank-invariance; (5) gene-set universe (MSigDB release, 15-500 size filter, keyword->theme map) now a locked pre-reg parameter; (6) ORA demoted to optional diagnostic so an empty list can't trigger 'fragile'.
- 2026-06-20: Pre-registration COMMITTED: entities/pre-registrations/0002-cross-trigger-pathway-overlap.md (pre-registration:0002-cross-trigger-pathway-overlap), data-gated mode. Locks: primary C1 = NES rank-concordance Spearman rho (PI-CFS-vs-HC x QFS-vs-HC, pinned Hallmark) with sample-label PERMUTATION null (B>=2000 or exhaustive); mandatory sensitivities S1 QFS-vs-QS specificity (presence), S2 QS-vs-HC exposure, S3 Reactome+GO-BP DB-robustness (theme must recur >=2 DBs), S4 CFS-vs-HC; gene-set universe pinned (MSigDB 2024.1.Hs, 15-500 size filter, keyword->theme map); 6-label mechanical verdict table; ORA exploratory-only. Standing verdict while gated = [?] inconclusive-for-coverage (no bears_on update). The plan's 4th blocking check (pre-reg lock) is now DISCHARGED; remaining G1 acquisition+hash, G2 MMSEQ scale-parse (Halt-on), G3 gene-id harmonization, G4 contrast/power-floor admissibility are the executable next steps (data is public, a download away -> task stays active, not externally blocked).
- 2026-06-20: Pre-reg tightened after same-day user code review (pre-data, amendment recorded in pre-registration:0002 frontmatter). 5 findings closed: (HIGH) QFS-vs-QS/QS-vs-HC specificity now thresholded (S1/S2 = same-sign-NES + nominal fgsea p<0.05; mechanical fatigue-specific/exposure_sequela/unresolved classes + theme roll-up); (HIGH) added explicit Locked theme map (6 case-insensitive regexes + first-match precedence) and a locked cell-type-marker regex; (MED) intro gate count G1-G3->G1-G4; (MED) task-state wording reconciled (t035 stays active, gate is dischargeable not externally blocked); (LOW) exact permutation label pools stated per contrast. Also added a locked verdict-resolution order (exactly one label; explicit fall-through). Validate PASSED, graph rebuilt, bears_on still scoped to h0001+q0017.
- 2026-06-20: Pre-reg 2nd-pass review closed (pre-data, 2nd amendment recorded in pre-registration:0002): (HIGH) theme-map + marker regexes moved from escaped-pipe Markdown table into fenced YAML with RAW PCRE + 'compile verbatim, case-insensitive' instruction (fixes copy-paste ambiguity); (HIGH) compartment_confounded now set-level: locked 'concordance-carrying set' = primary-concordant AND nominal fgsea p<0.05 in BOTH contrasts, 50%-marker rule runs on that (no gene-level 'leading-edge'); (MED) DB-robustness now requires SAME theme-level NES sign across >=2 DBs (direction-consistent recurrence); (OPEN Q) mixed-theme roll-up made STRICT-DOMINANCE (#fatigue-specific > #exposure_sequela; tie/exposure-majority -> exposure_sequela). Validate PASSED, graph rebuilt, bears_on still h0001+q0017.
- 2026-06-20: G1/G2/G4 CLEARED (data-fitness verified from the data, not metadata). ACQUISITION: GSE130353_RAW.tar (94.9MB, 40 members) downloaded via one-off curl (user ran it; GEO adapter is series-matrix-only) + GSE14577 parsed from local SOFT; all SHA-256s recorded (data/processed/acquisition_manifest.json; top-level hashes in the registry note, now flipped to 'provisioned'). G2 scale verdict=PASS: MMSEQ estimate column = log_mu (natural-log posterior mean, continuous, ~30% neg, 0% integer); 56625 Ensembl(rel68) features; SOFT's 'counts per gene' label is INACCURATE (recommended estimate is log_mu, not the integer unique_hits col) -> continuous limma only, DESeq2/edgeR inadmissible (matches pre-reg lock); sd col = candidate precision weights. G4 admissibility=PASS: groups 10/10/10/10 from authoritative SOFT subject-status (HC/CFS/QFS/QS), 40 distinct donors, 40/40 matched, QFS-vs-QS constructable. GOTCHAS locked in sample_sheet.tsv (keyed on subject_status, NOT filenames): QS samples are coded 'PQ'; CFS titles include CSF/FCS typos. GSE14577: GPL96 22283x15 + GPL97 22645x15, 7HC+8PI-CFS male, log2 confirmed (2.58-14.33). G3 (gene-id harmonization) not yet run but de-risked (both sides -> Ensembl). NEXT: per user, the download must become a Snakemake rule in code/workflows/ for the final impl; g1_acquire.py is the seed. Stopped before any DE/fgsea/concordance per scope.
- 2026-06-20: Pipeline DESIGN plan written: entities/plans/0003-cross-trigger-pathway-overlap-pipeline.md (plan:0003), design mode, Snakemake-specific per user direction. Pure orchestration — does NOT re-decide pre-reg methodology. Architecture: Snakemake under code/workflows/ (R/Bioconductor for limma+fgsea; Python for acquire/QA/harmonize/specificity/rollup/verdict); ONE config.yaml encodes every locked pre-reg param. 8 key decisions (R/Python split; permutation null as 1 heavy R rule w/ internal paired-label loop, NOT 2000-job fanout, NOT gene-shuffle; QA as DAG-gating *.qa.pass sentinels w/ t037 two-severity, qa_report.md never the strict output; config = single param home; Ensembl canonical axis; no cross-dataset merge; pinned msigdbr; deferred-CEL+sd-weighting off-primary). 8 work packages WP0-WP8 (skeleton+config -> acquire(w/ checksum vs locked SHA) -> QA -> G3 harmonize -> preprocess -> limma+fgsea(5 contrasts x 3 DBs) -> concordance+permutation null -> specificity+rollup+db-robustness+compartment -> mechanical verdict). 5 open questions (natural-log log_mu; near-zero filter threshold; U133A∪B overlap combine; annotation/MSigDB version coherence; exhaustive-vs-MC permutation). Validate PASSED, graph rebuilt. NOTE: plan-pipeline command says doc/plans/ but validator enforces type:plan under entities/plans/ -> filed as 0003 (date prefix would collide on year 2026 w/ menopause plan).
- 2026-06-20: Pipeline plan (plan:0003) revised after user code review (5 findings, all accepted): (HIGH) datapackage conflict resolved by SPLITTING two conflated artifacts — a minimal Frictionless datapackage.json (resources+SHA-256+source URL) is now produced by acquisition WP1 and discharges pre-reg G1 literally; the FORMAL mixin-dataset-1.0 commons entity stays deferred to promotion (no pre-reg amendment needed). (HIGH) S3 Reactome/GO-BP DB-sensitivity now in the DAG: the heavy permutation_null rule is parameterized over (concordance-pair x DB) = {primary PI-CFS-vs-HC x QFS-vs-HC, S4 PI-CFS-vs-HC x CFS-vs-HC} x {Hallmark,Reactome,GO-BP} = 6 cells, each its own rho+p_perm (C1=primary×Hallmark; S3=primary×Reactome/GO-BP; S4 rows); db_robustness consumes the per-DB nulls. (MED) verdict-affecting preprocessing now LOCKED in config not picked at runtime (new Key decision 9): near-zero log_mu filter = contrast-blind rule tau=-7.0/min_donors=10 on pooled 40-donor cohort + structural-QA antimode<tau check; U133AunionB combine = mean of platform-collapsed log2. (MED) G3 coverage threshold locked: build-fatal iff mapped Hallmark set EMPTY (matches pre-reg non-empty req), hallmark_coverage_warn=0.90 is distribution-severity only. (LOW) determinism contract (new Key decision 10): L'Ecuyer-CMRG substreams under BiocParallel + stable table ordering + sorted-key/fixed-precision/timestamp-free serialization, so byte-identical verdict.json is engineered not hoped. Registry note updated to reflect the datapackage/formal-entity split. Next: /science:review-pipeline for systematic review.

## [t036] Acquire hormone-panel triangulation cohorts (All of Us, Lifelines, Generation Scotland) to positively test H0005 (M1)
- priority: P3
- status: proposed
- aspects: []
- related: [hypothesis:0005-reproductive-stage-immune-homeostatic-margin, question:0013-reproductive-stage-failed-immune-recovery-after-infection, discussion:0001-menopause-timing-pais-rival-models]
- group: causal-disentanglement
- created: 2026-06-20

LOAD-BEARING ASYMMETRY from the 2026-06-20 audit: the committed UKB design can REFUTE H0005 (a powered, sensitivity-robust null is a real downward update) but CANNOT CONFIRM it -- M1's unique positive signature is hormone-marker mediation, exactly what UKB lacks (oestradiol floor-censored at 175 pmol/L; FSH/AMH absent). Positive support for the hormone-mediated failed-recovery model must come from triangulation cohorts WITH hormone panels: All of Us, Lifelines, Generation Scotland (and RECOVER/IMPACC for PEM-stratified arms). Scope/sequence: dataset-feasibility search; this is post-seed-stage per specs/scope-boundaries.md. Recorded so the only path to M1's positive test is not lost.

## [t037] Realize the UKB analysis's prose data-QA provisions as a wired-in, build-fatal QA checkpoint when implemented
- priority: P2
- status: proposed
- aspects: []
- related: [pre-registration:0001-menopause-pais-total-effect, hypothesis:0005-reproductive-stage-immune-homeostatic-margin]
- blocked-by: [task:t028]
- group: causal-disentanglement
- created: 2026-06-20

AXIS-1 FORWARD GAP from the 2026-06-20 pipeline-QA audit. The pre-registered UKB menopause->PAIS analysis specifies rich data-QA only in PROSE (sampling-frame/natal-female audit; exposure-timing repeat-assessment validation; dual outcome-route A/B triangulation; U-proxy missingness thresholds >50%; the 3x3 misclassification matrix; oestradiol floor-censoring sentinel at 175 pmol/L). Per ~/d/science/docs/conventions/pipeline-qa-checkpoints.md, prose intentions and side-output counts files do NOT discharge axis-1 QA. When t028 builds the analysis table, add a SEPARATE rule that re-reads the built table with STRUCTURAL (build-fatal: one-row-per-participant; natal-female filter integrity; allowed reproductive-stage codes; outcome-route key alignment) vs DISTRIBUTION (age-at-menopause bounds; 175 pmol/L oestradiol sentinel; missingness) checks, config-driven thresholds shared with the cleaning step. This task exists so the prose QA spec survives into code.
