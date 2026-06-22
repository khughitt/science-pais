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

## [t037] Realize the UKB analysis's prose data-QA provisions as a wired-in, build-fatal QA checkpoint when implemented
- priority: P2
- status: proposed
- aspects: []
- related: [pre-registration:0001-menopause-pais-total-effect, hypothesis:0005-reproductive-stage-immune-homeostatic-margin]
- blocked-by: [task:t028]
- group: causal-disentanglement
- created: 2026-06-20

AXIS-1 FORWARD GAP from the 2026-06-20 pipeline-QA audit. The pre-registered UKB menopause->PAIS analysis specifies rich data-QA only in PROSE (sampling-frame/natal-female audit; exposure-timing repeat-assessment validation; dual outcome-route A/B triangulation; U-proxy missingness thresholds >50%; the 3x3 misclassification matrix; oestradiol floor-censoring sentinel at 175 pmol/L). Per ~/d/science/docs/conventions/pipeline-qa-checkpoints.md, prose intentions and side-output counts files do NOT discharge axis-1 QA. When t028 builds the analysis table, add a SEPARATE rule that re-reads the built table with STRUCTURAL (build-fatal: one-row-per-participant; natal-female filter integrity; allowed reproductive-stage codes; outcome-route key alignment) vs DISTRIBUTION (age-at-menopause bounds; 175 pmol/L oestradiol sentinel; missingness) checks, config-driven thresholds shared with the cleaning step. This task exists so the prose QA spec survives into code.

## [t039] All of Us Researcher Workbench hormone-coverage query (decide if AoU can be the reverse-causation-breaking M1 vehicle)
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-21

Surviving path (b) from report:0004 (t036 feasibility). All of Us is the ONLY candidate that could break the P3 reverse-causation ambiguity (uncensored EHR-lab hormones -- no UKB 175 pmol/L ceiling -- plus pre-pandemic enrolment + EHR backfill + ~396k-women dual-source reproductive staging + Fitbit RMSSD HRV). The single make-or-break UNKNOWN is whether opportunistic EHR hormone labs (oestradiol/FSH/AMH) have ADEQUATE, NON-SELECTIVELY-ORDERED coverage and repeat-measure cadence in long-COVID-affected peri-/post-menopausal women -- answerable ONLY by a Researcher Workbench Data Browser / Cohort Builder query, not from public docs. DELIVERABLE: per-analyte coverage + repeat-measure counts in the target stratum; verdict on whether AoU promotes from Tier 2 to a viable vehicle. GATED on: a signed DURA / institutional Workbench access (no documented unaffiliated-researcher path); analysis is in-cloud with no data export (tension with reproducible-from-public norm -- note in any output). related: report:0004, hypothesis:0005, proposition:0003 (the rival this would help adjudicate).

## [t040] RECOVER-Adult ancillary biospecimen study: assay sex-steroid panel on banked serum for the primary M1 positive test (post-seed-stage)
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-21

Surviving path (c) from report:0004 (t036 feasibility) -- the EVENTUAL PRIMARY positive test of h0005 M1, highest-quality but highest-cost. RECOVER-Adult is the strongest single vehicle: AMH ALREADY measured (Tier 2; the one staging analyte UKB lacks), PEM-weighted validated PASC index (Thaweethai 2023; PEM ~87% of PASC-positive -> best-in-class PEM-stratified outcome), and deep mediators across all three families (Tier-1 D-dimer/troponin/ECG endothelial; Tier-1 active-stand + Tier-3 tilt/catecholamine autonomic; 12-task-force pathobiology immune). The full E2/T/FSH/LH/SHBG panel is ASSAYABLE DE NOVO from banked serum/plasma/PBMC at Mayo. TWO decisive limits: (1) enrolment >=3 mo post-infection -> NO within-person pre-infection hormone baseline, so reverse causation is only PARTIALLY addressable (uninfected-control arm + post-infection trajectory, not a clean pre-exposure anchor); (2) hormone exposure does not yet exist -> requires an ancillary-study proposal (ASOC) with INDEPENDENTLY-SECURED EXTERNAL FUNDING, application-gated, multi-month, not reproducible-from-public. SCOPE: post-seed-stage + funded; this task is recorded so the only path to M1's primary positive test is not lost. OPEN UNKNOWN: whether any RECOVER pathobiology sub-study has ALREADY assayed sex steroids on banked serum (supplemental analyte tables not fully readable in scoping) -- would remove the funded-assay step. related: report:0004, hypothesis:0005, proposition:0002, task:t028.
