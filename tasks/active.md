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

### Notes

- 2026-06-21: 2026-06-21: Opportunistic non-UKB out-of-corpus search done (advancing toward t028). Found TWO independent, author-independent, non-UKB clinical cohorts corroborating a gonadal-steroid -> long-COVID protective association: Silva2024 (Mount Sinai-Yale MY-LC, n~165; testosterone assoc. w/ lower symptom burden across sexes) and Shahbaz2025 (Univ. Alberta LC/ME-CFS, n=140; reduced testosterone in female LC, reduced estradiol in male LC). Both measure GONADAL STEROIDS, not SHBG; both clinical-cohort grade + cross-sectional w/ unresolved reverse causation. DISPOSITION: SHBG *measure* remains SINGLE-SOURCE (Szczerbinski2023 measured SHBG but reported no assoc.; hospitalized-survivor exposure); the broader sex-hormone-protection (M1-confirm-side, mediator-specific) prior is no longer single-source. No change to locked {age,smoking} primary; does not gate t028. Both papers ingested + linked to h0005/q0007/q0013/t036; disposition recorded in report:0002 addendum. OPEN: SHBG-specific upgrade still unmet; at-application confirmation when AMS basket finalized.

## [t036] Acquire hormone-panel triangulation cohorts (All of Us, Lifelines, Generation Scotland) to positively test H0005 (M1)
- priority: P3
- status: proposed
- aspects: []
- related: [hypothesis:0005-reproductive-stage-immune-homeostatic-margin, question:0013-reproductive-stage-failed-immune-recovery-after-infection, discussion:0001-menopause-timing-pais-rival-models]
- group: causal-disentanglement
- created: 2026-06-20

LOAD-BEARING ASYMMETRY from the 2026-06-20 audit: the committed UKB design can REFUTE H0005 (a powered, sensitivity-robust null is a real downward update) but CANNOT CONFIRM it -- M1's unique positive signature is hormone-marker mediation, exactly what UKB lacks (oestradiol floor-censored at 175 pmol/L; FSH/AMH absent). Positive support for the hormone-mediated failed-recovery model must come from triangulation cohorts WITH hormone panels: All of Us, Lifelines, Generation Scotland (and RECOVER/IMPACC for PEM-stratified arms). Scope/sequence: dataset-feasibility search; this is post-seed-stage per specs/scope-boundaries.md. Recorded so the only path to M1's positive test is not lost.

### Notes

- 2026-06-21: 2026-06-21: Dataset-feasibility search done -> report:0004. VERDICT: no off-the-shelf vehicle for the M1 positive test exists. Structural finding: the pre-infection-baseline requirement (R5) and the directly-measured-hormone-panel requirement (R1) are ANTI-CORRELATED across the candidate landscape -- general biobanks (All of Us, Lifelines, GS) have pre-infection baselines but no/opportunistic sex hormones; purpose-built long-COVID cohorts (RECOVER, IMPACC) have deep mediators but enrol POST-infection so cannot break the P3 reverse-causation ambiguity. Tiers: RECOVER-Adult = best primary vehicle but bespoke (AMH already measured + PEM-weighted index + deep immune/endothelial/autonomic mediators; full E2/T/FSH/LH/SHBG assayable from Mayo biobank; BUT no pre-infection baseline + ancillary-study+external-funding gated). All of Us = only candidate that could break reverse causation (uncensored EHR hormones + pre-pandemic enrol/backfill + ~396k-women staging + Fitbit HRV; BUT opportunistic/sparse coverage, no systematic immune panel, no PEM -- feasibility hinges on a Workbench coverage query). IMPACC = secondary corroboration only (deepest longitudinal immune multi-omics + already shows androgen-metabolite long-COVID signal corroborating M1 direction; BUT no hormone panel, no repro data, no pre-infection baseline, hospitalized skew -- but processed data open via ImmPort SDY1760/dbGaP, no new assays). Lifelines + Generation Scotland RULED OUT as M1 vehicles (no sex steroids measured; GS markers ~9-15yr pre-infection = fatal staleness) -- retain only as long-COVID symptom-design refs. RECOMMENDED SEQUENCE (cheapest/most-reproducible first): (a) IMPACC open-data secondary corroboration (direction only, no funding); (b) All of Us Workbench coverage query (resolves the biggest UNKNOWN, decides if AoU is viable); (c) RECOVER ancillary biospecimen study (eventual primary positive test, post-seed-stage, funded). Does NOT change proposition:0002 fragility -- it EXPLAINS it (no accessible cohort jointly satisfies R1+R2+R5). t036 stays open; positive test is post-seed-stage. No dataset entities created (per scope).

## [t037] Realize the UKB analysis's prose data-QA provisions as a wired-in, build-fatal QA checkpoint when implemented
- priority: P2
- status: proposed
- aspects: []
- related: [pre-registration:0001-menopause-pais-total-effect, hypothesis:0005-reproductive-stage-immune-homeostatic-margin]
- blocked-by: [task:t028]
- group: causal-disentanglement
- created: 2026-06-20

AXIS-1 FORWARD GAP from the 2026-06-20 pipeline-QA audit. The pre-registered UKB menopause->PAIS analysis specifies rich data-QA only in PROSE (sampling-frame/natal-female audit; exposure-timing repeat-assessment validation; dual outcome-route A/B triangulation; U-proxy missingness thresholds >50%; the 3x3 misclassification matrix; oestradiol floor-censoring sentinel at 175 pmol/L). Per ~/d/science/docs/conventions/pipeline-qa-checkpoints.md, prose intentions and side-output counts files do NOT discharge axis-1 QA. When t028 builds the analysis table, add a SEPARATE rule that re-reads the built table with STRUCTURAL (build-fatal: one-row-per-participant; natal-female filter integrity; allowed reproductive-stage codes; outcome-route key alignment) vs DISTRIBUTION (age-at-menopause bounds; 175 pmol/L oestradiol sentinel; missingness) checks, config-driven thresholds shared with the cleaning step. This task exists so the prose QA spec survives into code.
