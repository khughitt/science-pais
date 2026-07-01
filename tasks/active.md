<!-- Task queue. Use /science:tasks to manage. -->
## [t003] Promote PAIS<->immunity bridge papers to commons once v3 entities/papers promotion is supported
- priority: P3
- status: proposed
- aspects: []
- created: 2026-06-11

Blocked by tooling gap (fb-2026-06-11-005). Bridge papers: Choutka2022, Komaroff2025, Klein2023, Rojas2022, Sharma2023.

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

## [t050] Discharge q0004 paired-site biopsy + primary-dysautonomia-control study (h0007 promotion criterion #1)
- priority: P2
- status: proposed
- aspects: []
- created: 2026-06-24

BLOCKED on vehicle-admissibility gate G1-G4 of pre-registration:0003. Activate when an admissible cross-syndrome study/dataset appears: paired proximal+distal IENFD with site-specific norms (G1), primary-dysautonomia control arm (G2), >=2 PAIS triggers under one protocol (G3), >=40 lesion-positive/side power floor (G4). On arrival, run the two confirmatory legs (P1 lesion-positive rate; P2 headline NLD-fraction delta vs primary-dysautonomia) per the locked decision criteria and interpret-results into h0007 promotion. Standing verdict until then: [?] inconclusive-for-coverage (no bears_on update).

VEHICLE HUNT 2026-06-24 (logged in pre-registration:0003 "Screened Vehicles"): no admissible vehicle found; G2 (clean primary-dysautonomia control arm) is the universal blocker. Closest near-miss = Novak et al. 2026 (PLoS One, PMC12829881, DOI 10.1371/journal.pone.0341278), which clears G1 (proximal thigh + distal calf) and G4 (SFN 53-67% by biopsy) and carries two PAIS triggers (long COVID n=143 + ME/CFS n=170) but fails G2 — comparators are healthy + hEDS, and hEDS is excluded by G2's "no SFN-causing comorbidity" clause (hEDS itself 63% SFN = contaminated control). G3 also not cleanly met (ME/CFS arm is ME-ICC/NAM without documented infectious onset); scored by QASAT grading, not the locked <=5th-percentile IENFD cutoff. Ingested as supporting evidence for h0007 P1/P4 (paper:Novak2026) - NOT as a promotion vehicle. Larsen 2025 LC-POTS deep-phenotyping (medRxiv 2025.04.28.25326587) fails G2+G3 (LC-only, healthy controls only). Actionable: the Novak group already runs the exact G1/G4 protocol at scale across two triggers - an admissible vehicle is ~one amendment away (add an idiopathic-POTS/familial-dysautonomia arm, re-score to percentile cutoffs). Note hEDS comparator shows comparable SFN -> previews the pre-reg "reverse/diagnostic surprise" (specificity contrast harder than lesion-existence). Gibbons-type neuropathic-POTS series (PMC3874039; 38-45% reduced IENFD) can pre-constrain the comparator NLD/lesion rate for the G4 power re-derivation. Task stays BLOCKED - no belief update.

## [t054] Track JAK1-inhibitor RCT NCT06597396 (abrocitinib) readout and discharge pre-registration:0004
- priority: P2
- status: blocked
- aspects: []
- related: [interpretation:0016-t054-abrocitinib-trial-status-snapshot]
- blocked-by: [pre-registration:0004-jak1-inhibitor-driver-vs-marker]
- created: 2026-06-24

Standing discriminating test for question:0006 / proposition:0026 / hypothesis:0003 driver-vs-marker, committed in pre-registration:0004 (data-gated). On trial readout: check Vehicle-Admissibility Gate G1-G5 (symptom co-primary; pathway/target-engagement readout; placebo-controlled; endotype stratification/enrichment; adequate power+duration). Then apply the locked decision criteria via interpret-results: symptom+pathway co-suppression -> supporting line on proposition:0026 (upward on h0003); pathway suppression WITHOUT symptom benefit -> disputing line (marker-not-driver, falsifier for h0003 maintenance-engine). An unstratified flat null = weak disconfirmation only (wrong-endotype / multi-loop confound). Until readout: standing verdict [?] inconclusive-for-coverage, no bears_on update.

### Notes

- 2026-06-25: Registry snapshot: ClinicalTrials.gov API v2 record for NCT06597396 reports ACTIVE_NOT_RECRUITING, enrollment 46 actual, primary completion 2026-03-27 actual, study completion 2026-09-30 estimated, last update posted 2026-04-20, and hasResults=false. No admissible readout yet; pre-registration:0004 remains [?] inconclusive-for-coverage. Public endpoints include FACIT-Fatigue/PASC PRO and hsCRP but not a specific IL-6R/JAK-STAT/ISG target-engagement score, so G2 must be checked in the eventual paper/supplement.

## [t079] Vehicle-feasibility pass for autoimmune-diathesis × sex × PASC analysis (t078 / plan:0005)
- priority: P2
- status: in-progress
- aspects: []
- created: 2026-06-30

Blocking checks BC-1..BC-7 from plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan before it can move to ready/pre-register. BC-1 vehicle selection + OpenSAFELY dataset discovery (no dataset entity yet); BC-2 access verification (prototype N3C synthetic tier); BC-3 autoimmune stratum granularity with dated pre-index onset (fix Hill pooled-Charlson gap); BC-4 sex×stratum×PASC cell counts vs power floor; BC-5 lock computable PASC definition; BC-6 acute-severity dateability in acute window (gates E2/E3 mediator role); BC-7 individual-level utilization covariate (replace county proxy). Provisional primary vehicle N3C; population-based replication OpenSAFELY/All-of-Us; RECOVER-Adult phenotype adjunct; UKB baseline triangulation.

### Notes

- 2026-07-01: BC-1 RESOLVED (interpretation:0031, 2026-07-01). Decision: N3C = PRIMARY vehicle; OpenSAFELY = pre-committed population-based REPLICATION (not primary); All-of-Us = diverse triangulation. Rationale: both platforms carry the exposure side well (dated pre-index autoimmune strata, dated SGSS/OMOP infection index, dated acute severity, individual utilisation), so the call turns on OUTCOME + prototyping cost. N3C has the most mature computable PASC phenotype (Hill proved it), rare-stratum x sex scale, and an OPEN SYNTHETIC TIER to prototype on now. OpenSAFELY's coded long-COVID is SEVERELY and DIFFERENTIALLY under-recorded (Walker: 23,273/58M; 26.7% of practices never coded; under-coding correlated with consultation frequency -> autoimmune patients coded more) => coded-only outcome carries outcome-side h0008 bias, disqualifying as primary but leaving its population-based frame valuable for the ascertainment arbiter role (plan rule #4) CONDITIONAL on a non-coded-only PASC phenotype (BC-5). Also: EMIS research backend PAUSED -> OpenSAFELY realistically TPP-only ~24M now; SDC (<=7, round-5) forces rare-cell pooling. Created dataset:opensafely-longcovid; added 3 OpenSAFELY refs (Williamson2020, Andrews2022, WalkerLongCOVID2021). Remaining: BC-2..BC-7. Next = BC-2 (stand up pipeline on N3C open synthetic tier). [UNVERIFIED] Sjogren/vasculitis/myositis/autoimmune-thyroid OpenCodelists URLs; exact coded-vs-survey under-recording ratio.
- 2026-07-01: BC-2 pipeline designed: plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline (design mode). Prototype skeleton on the N3C OPEN SYNTHETIC SLICE only (mixed-access gate PASS for the public slice; Limited/De-identified enclave siblings out of scope pending DUA). OMOP-first with an execution shim so the same code runs local-synthetic (duckdb) and enclave (Foundry/PySpark). 10 work packages WP0-WP9: synthetic standup+access punch-list; versioned concept-set bundle (reusable, shared with enclave + OpenSAFELY BC-5); cohort (Hill 1:5 matching, weighting alt); exposure strata+pooling; covariates (individual utilisation replaces county proxy; vaccination built adjusted AND unadjusted per the plan:0005 caveat); severity as a structurally-separated POST-index mediator (guard test bars it from the E1 set); PASC outcome (U09.9+phenotype); E1/E2/E3 + RERI + multiplicative + site frailty; disclosure-portable outputs (suppress-then-round, clears N3C review + OpenSAFELY SDC); scale/e2e validation. ACCEPTANCE = pipeline runs, strata resolve, estimands compute, outputs disclosure-safe — NOT any coefficient (synthetic data has no signal). Real-tier execution + interpretable estimate remain gated (rest of BC-2). BC-3 (codelist clinical sign-off) and BC-5 (OpenSAFELY phenotype) flagged, not folded in.
