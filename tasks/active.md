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

## [t057] Specify q0016 redox directionality for h0006 self-perpetuation
- priority: P2
- status: proposed
- aspects: []
- related: [question:0016-oxidative-stress-upstream-driver-of-bioenergetic, hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem, proposition:0035-pem-muscle-lesion-is-self-perpetuating]
- group: mechanism-formalization
- created: 2026-06-26

Follow-up from the h0006 specify-model/redox-dependency review. Tighten question:0016 around the discriminating issue for proposition:0035: is ROS/redox stress an upstream feedback driver that helps close the PEM muscle self-perpetuation loop, or a downstream consequence of mitochondrial failure? Deliverable: update q0016 with measurement model, expected temporal ordering, admissible evidence types, and failure modes that would weaken P4/h0006. Keep scope focused on redox directionality in provoked PEM muscle biology, not generic oxidative-stress literature.

## [t058] Pre-register harmonized LC+ME/CFS provoked muscle-endpoint study
- priority: P2
- status: proposed
- aspects: []
- related: [hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem, hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent, question:0011-mitochondrial-basis-of-pem, question:0016-oxidative-stress-upstream-driver-of-bioenergetic, proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific, proposition:0032-pem-bioenergetic-deficit-localizes-to-skeletal-muscle, proposition:0033-microvascular-hypoperfusion-drives-pem-muscle-bioenergetic-failure, proposition:0034-ionic-na-ca-overload-mediates-pem-muscle-mitochondrial-injury, proposition:0035-pem-muscle-lesion-is-self-perpetuating]
- group: causal-disentanglement
- created: 2026-06-26

Design-gated follow-up from t056 and h0006 formalization. Author a pre-registration for the decisive h0006-vs-h0008-M3 adjudicator: long COVID + ME/CFS + recovered/healthy controls under the same exertional provocation, with muscle biopsy pre/immediate/24-48h, OXPHOS/SDH/Complex-II, fiber-type composition, intracellular Na/Ca, ROS/redox markers, perfusion, immune infiltrate, myopathic injury, and central/peripheral CPET decomposition. The key readout is whether the Appelman-style provoked muscle lesion is endpoint-harmonized across triggers, trigger-specific, or measurement-artifact/endpoint-contingent.

## [t059] Hunt h0002 promotion vehicles for non-Borrelia tissue reservoirs and retained-burden prediction
- priority: P2
- status: proposed
- aspects: []
- related: [hypothesis:0002-tissue-reservoir-antigen-fragment, proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization, proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load, interpretation:0017-t053-h0002-promotion-audit]
- group: evidence-ingestion
- created: 2026-06-26

Successor to t053. Search for or design admissible evidence that can lift h0002's two untested core conjuncts rather than over-crediting the persistence pillar. For proposition:0023, require controlled non-Borrelia PAIS tissue-reservoir evidence showing retained pathogen fragments in tissue-resident macrophages plus overlapping host signature. For proposition:0024, require a prospective cohort measuring both acute pathogen load and retained post-clearance fragment burden in the same subjects, with chronic PAIS diagnosis as endpoint and retained burden out-predicting acute load. Output should distinguish found literature from data-gated/commissioned study requirements.

## [t060] Cross-PAIS IFN/JAK-STAT pathway comparison for q0006
- priority: P3
- status: proposed
- aspects: []
- related: [question:0006-jak-stat-il6-driver-vs-marker, hypothesis:0003-immune-exhaustion-feedback, proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn, proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver, interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration]
- group: cross-trigger-generalization
- created: 2026-06-26

Follow-up from t047 distinct from the abrocitinib readout tracked by t054. Determine whether the JAK-STAT/IL-6 and IFN-arm dissociation pattern is LC-specific or recurs across PAIS triggers such as ME/CFS, PTLDS, and Q-fever fatigue. Highest-value design is same-cohort co-measurement of persistent type-II/inflammatory IFN tone, blunted type-I antiviral-effector ISGs, and IFN-I stimulation response; minimum useful output is a comparable cross-PAIS pathway-level evidence map with assay/platform comparability and endotype caveats. Do not use this to discharge t054/pre-registration:0004's interventional driver-vs-marker test.

## [t061] Find or compute severity-adjusted PEM molecular contrast vehicle
- priority: P3
- status: proposed
- aspects: []
- related: [question:0015-does-pem-requirement-improve-cross-study-comparability, proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode, interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation, interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands]
- group: causal-disentanglement
- created: 2026-06-26

Follow-up from t025/t044. The decisive q0015 test remains inaccessible from public STOP-PASC/Maestri2025 data: convert PEM molecular associations into a severity-adjusted PEM-positive vs PEM-negative contrast, or identify an accessible RECOVER/IMPACC-style cohort with validated PEM measurement, overall-severity covariate, acute-severity covariates, and omics/proteomics endpoints. Watch for STOP-PASC individual-level data/repo release; otherwise scope data-access route. Output should say whether a computable vehicle exists, not merely add more unadjusted PEM associations.

## [t068] Add code-to-task back-links for t035 workflow scripts
- priority: P3
- status: proposed
- aspects: []
- related: [pre-registration:0002-cross-trigger-pathway-overlap, plan:0003-cross-trigger-pathway-overlap-pipeline, question:0001-shared-molecular-signature-across-triggers]
- group: workflow-consistency
- created: 2026-06-26

Pipeline-refactor audit finding. t035 workflow files have science:code headers and strong reverse links from the plan, but the code side does not use the sanctioned code-task backlink pattern. Add lightweight comment-block back-links (for example task:t035 / plan:0003 / pre-registration:0002 as appropriate) to code/workflows/*.smk and rule-callable scripts, without changing behavior. This is mechanical consistency work; keep it separate from QA logic changes.

## [t069] Normalize mapped MSigDB clean base for bio.geneset commons promotion
- priority: P3
- status: proposed
- aspects: []
- related: [dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe, task:t065, pre-registration:0002-cross-trigger-pathway-overlap]
- group: workflow-portability
- created: 2026-06-26

Follow-up from t065. The mapped MSigDB 2024.1.Hs clean base is commons-dry-run ready as a base deposit, but not with the bio.geneset mixin because the package currently contains RDS gene-set lists plus theme_map.tsv, not a normalized long member table with set_key/member identifiers. Add a generated members.tsv (or equivalent) with set_key semantics, decide how theme_map relates to it, re-emit the datapackage, and rerun the bio.geneset promotion dry-run. Keep actual commons apply blocked until MSigDB custom-license policy is confirmed.
