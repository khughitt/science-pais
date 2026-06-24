<!-- Task queue. Use /science:tasks to manage. -->
## [t003] Promote PAIS<->immunity bridge papers to commons once v3 entities/papers promotion is supported
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Blocked by tooling gap (fb-2026-06-11-005). Bridge papers: Choutka2022, Komaroff2025, Klein2023, Rojas2022, Sharma2023.

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

## [t043] Determine whether the ME/CFS early-menopause signal (Boneva2015) is reverse-causation or predisposition
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-22

Boneva2015 reports early menopause (<=45) adj OR 3.20 and ~10y earlier mean age at menopause in ME/CFS — the strongest true reproductive-stage x subphenotype signal found in the t018 sweep (interpretation:0003), but cross-sectional with unresolved direction (illness may advance menopause vs early menopause predisposing). Needs pre-infection menopausal-timing data (same private/deferred within-cohort design flagged in t013). Empirical. Related: interpretation:0003, hypothesis:0005, question:0013, proposition:0003.

## [t045] Ingest and triage Neuhouser2024 (WHI long-COVID risk factors in postmenopausal women) for the HRT-evidence gap
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-23

Surfaced during t019 HRT-evidence audit (interpretation:0008). Neuhouser et al., 'Risk factors for long COVID syndrome in postmenopausal women with previously reported diagnosis of COVID-19', Ann Epidemiol 2024 (WHI; PMC11405002; DOI 10.1016/j.annepidem.2024.xx). n>1,230 COVID-19, 425 long COVID, ML top-20 risk-factor screen. Reported top predictors (weight loss, mobility, RA, heart-valve procedures, sleep) do NOT include HRT. Triage from full text: was menopausal hormone therapy in the candidate feature set (unselected) or never examined? If MHT was examined/reported (even null), add as the first WHI-grade HRT-vs-long-COVID evidence-line on proposition:0006 and correct interpretation:0003's matrix line. Ingest as paper:Neuhouser2024 + references.bib entry.

## [t047] Track JAK-inhibitor RCT NCT06597396 and reconcile the Aid2025 persistent-IFN vs Ryan2022 IFN-I-suppression contradiction (h0003)
- priority: P2
- status: proposed
- aspects: []
- related: [hypothesis:0003-immune-exhaustion-feedback, question:0006-jak-stat-il6-driver-vs-marker, topic:long-covid-immune-dysregulation, topic:therapeutics-and-clinical-trials]
- created: 2026-06-24

h0003 has claim_count=0. Two deposits possible now: (1) Register NCT06597396 (JAK1 inhibitor in long COVID) as the standing driver-vs-marker discriminating test for question:0006 and track its readout; a symptom-reduction + pathway-suppression co-endpoint = upward evidence for the exhaustion-feedback loop as an intervention target, a clean null = marker-not-driver. (2) Reconcile the internal contradiction the synthesis flagged: Aid2025 reports persistent IFN activation beyond 180d while Ryan2022 reports IFN-I SUPPRESSION at ~6 mo. Resolve by timing/compartment/endotype or record as an open tension that, if irreducible, mischaracterizes the loop's inflammatory arm. Mechanism-general - coordinate with health-immunity, promote via commons if warranted.

## [t048] Find a sex-stratified COVID-vs-uninfected ambulatory cohort to estimate the infection-attributable male vascular excess (31-180d) for q0020/q0021
- priority: P2
- status: proposed
- aspects: []
- related: [question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover, question:0020-male-vte-excess-post-acute-persistence, proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment, hypothesis:0004-acute-severity-threshold, topic:thromboinflammation-and-endothelial-dysfunction]
- created: 2026-06-24

Both q0020 and q0021 need the SAME missing design: an ambulatory cohort with a sex-stratified UNINFECTED / test-negative comparator and post-acute (31-180d) vascular hard-endpoint follow-up. DELIVERABLE: (1) lit/dataset scan for such a cohort (candidates: VA Million Veteran / Al-Aly programme with test-negative controls; OpenSAFELY; Clalit/Kopp2024 source; N3C) reporting VTE/MI/CV-death by sex with an uninfected baseline; (2) if found, estimate the male PASC vascular excess as a ratio-of-ratios (COVID M:F vs uninfected M:F) or sex x infection interaction = the infection-attributable increment over male baseline; (3) feed result into proposition:0012 (does the reversal carry a COVID-specific component or dissolve to baseline carryover?) and into how sex x severity should be jointly modeled in the pre-registered work. If no such cohort exists, record the design gap explicitly. Empirical.

## [t050] Discharge q0004 paired-site biopsy + primary-dysautonomia-control study (h0007 promotion criterion #1)
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-24

BLOCKED on vehicle-admissibility gate G1-G4 of pre-registration:0003. Activate when an admissible cross-syndrome study/dataset appears: paired proximal+distal IENFD with site-specific norms (G1), primary-dysautonomia control arm (G2), >=2 PAIS triggers under one protocol (G3), >=40 lesion-positive/side power floor (G4). On arrival, run the two confirmatory legs (P1 lesion-positive rate; P2 headline NLD-fraction delta vs primary-dysautonomia) per the locked decision criteria and interpret-results into h0007 promotion. Standing verdict until then: [?] inconclusive-for-coverage (no bears_on update).

## [t052] Code hypothesis:0002 primary support (McClune2025/Peluso2024) as evidence-lines to lift it from speculative
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-24

After t051 decoupled proposition:0021 (mechanism-agnostic metformin evidence) from h0002's belief, h0002 grades 'speculative' because its genuine primary support — McClune2025 (mouse Borrelia tissue-reservoir + long-COVID molecular overlap) and Peluso2024 (persisting SARS-CoV-2 antigen) — lives in the prose Supporting Evidence section, NOT coded as evidence-lines. The only coded claim bearing on h0002 is the disputed-but-uninterpretable corollary proposition:0020. Mint a core proposition for the tissue-reservoir mechanism and code McClune2025 (moderate; mouse model caveat) + Peluso2024 (weak; antigen detection, no symptom link) as supporting evidence-lines so the graph grades h0002 an honest 'contested'/'supported (contested)' rather than speculative. This is the correct way to promote h0002 — NOT via the metformin prevention trials.
