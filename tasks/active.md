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

## [t016] Define estimands for reproductive-stage PAIS causal analyses
- priority: P2
- status: in_progress
- aspects: []
- related: [question:0013-reproductive-stage-failed-immune-recovery-after-infection, hypothesis:0005-reproductive-stage-immune-homeostatic-margin, topic:menopause-sex-hormones-and-pais-risk]
- group: causal-disentanglement
- created: 2026-06-19

For each planned PAIS sex/hormone analysis, predeclare whether reproductive stage is treated as confounder, mediator, effect modifier, competing diagnosis, or downstream consequence. Specify target population, exposure window, outcome domain, adjustment set, and variables that should not be adjusted away for each estimand.

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

## [t033] [lit-search] Post-dengue / Q-fever / post-SARS molecular signatures + Galbraith2011 head-to-head deep-read
- priority: P2
- status: proposed
- aspects: []
- related: [discussion:0002-cross-pathogen-pais-signature-convergence, hypothesis:0001-shared-dysregulated-attractor, question:0001-shared-molecular-signature-across-triggers]
- created: 2026-06-20

Closes the decisive head-to-head evidence gap surfaced by t001 (discussion:0002). h0001 (shared-attractor) names post-dengue and post-Q-fever among its triggers, but the 2026-06-20 search found NO usable omics for post-dengue, QFS, or post-SARS(2003) -- only fatigue epidemiology (Conde2026) and a single negative TSPO study (Raijmakers2021). (1) Targeted hunt for proteomic/transcriptomic/metabolomic signatures in post-dengue, QFS, post-SARS, post-Ebola/chikungunya fatigue; if empty, RECORD as a structural evidence gap limiting h0001 testability (not as evidence against). (2) Deep-read Galbraith2011 (Dubbo EBV/Ross-River/Q-fever) -- the closest existing genuine cross-trigger transcriptomic comparison -- and check for reusable GEO data; populate its stub. (3) Read Patterson2024 (strongest disputer; assess ML overfitting) + Walitt2024. Feeds question:0001, hypothesis:0001, discussion:0002.

### Notes

- 2026-06-20: Galbraith2011 deep-read partially addressed (2026-06-20): abstract read and paper:Galbraith2011 stub populated. KEY CORRECTION — the Dubbo head-to-head found NO genes consistent across all three triggers (EBV/RRV/Q-fever) in bulk blood by qPCR, i.e. a head-to-head NEGATIVE at gene level (not the prior 'partial shared/supports' reading). discussion:0002 + q0001 reconciled. RESIDUAL for this task: (a) full text is 403-blocked and NO GEO/ArrayExpress deposit found -> author contact (A. Lloyd, UNSW) + pathway-level/cell-type reanalysis to test whether the gene-level null survives; (b) post-dengue/QFS/post-SARS omics search still outstanding.
