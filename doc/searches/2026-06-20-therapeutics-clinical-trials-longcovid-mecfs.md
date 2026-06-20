# Literature Search: Therapeutics & Clinical-Trial Landscape for Long COVID and ME/CFS

- **Date:** 2026-06-20
- **Task:** t004 — Therapeutics & clinical-trial landscape for long COVID and ME/CFS
- **Layout:** v3 (`doc/searches/`, `entities/papers/`, `entities/topics/`)

## Search Focus

Survey the therapeutic / clinical-trial landscape for PAIS, emphasizing **controlled trials (RCTs)** and their **endpoints**, across the drug classes most active in long COVID and ME/CFS:
antivirals (nirmatrelvir-ritonavir, ensitrelvir, antiviral prevention of long COVID); immunomodulators (IL-6 blockade, JAK inhibitors, low-dose IL-2, leronlimab, sirolimus); anticoagulation/antiplatelet (microclot-targeting, triple anticoagulant therapy); autoantibody-targeting (BC007/rovunaptabin aptamer, immunoadsorption/apheresis, rituximab including the **negative RituxME** trial); low-dose naltrexone (LDN); vagal/neuromodulation and non-invasive brain stimulation; metabolic (metformin / COVID-OUT for PASC prevention); and non-pharmacologic pacing/energy-management with the GET/PACE controversy.

The corpus was previously thin on treatment. This search relates trials to `topic:biomarkers-and-objective-endpoints` — the recurring problem that PAIS trials lack a validated, objective surrogate endpoint, so most rely on subjective PROs (PROMIS, symptom counts), which weakens interpretation of both positive and null results.

## Query Set

| ID | Variant type | Query (OpenAlex `search=` / PubMed term) |
|----|--------------|------------------------------------------|
| Q2 | broad conceptual | long COVID PASC randomized controlled trial intervention treatment (OpenAlex, n=1362) |
| Q3 | mechanism/drug-class — antivirals | nirmatrelvir ritonavir Paxlovid long COVID PASC trial; + PubMed STOP-PASC, ensitrelvir, RECOVER-VITAL |
| Q4 | mechanism/drug-class — immunomodulators | long COVID immunomodulator baricitinib JAK inhibitor IL-2 tocilizumab trial; + leronlimab, sirolimus, low-dose IL-2 |
| Q5 | mechanism/drug-class — anticoagulation | long COVID microclot anticoagulation antiplatelet trial fibrin; + REMAP-CAP antiplatelet |
| Q6 | mechanism/drug-class — autoantibody | long COVID autoantibody BC007 aptamer immunoadsorption apheresis trial; + Fluge/Mella RituxME |
| Q7 | methods/trial-design + negative-results | rituximab ME/CFS RCT (RituxME null); PACE/GET graded exercise CFS RCT controversy; living systematic reviews |
| Q8 | alternative — LDN / metabolic / neuromod / pacing | low-dose naltrexone; metformin COVID-OUT; vagus nerve stimulation; pacing post-exertional malaise |

Coverage queries (one per uncovered class) added for ensitrelvir prevention, leronlimab/CCR5, sirolimus, low-dose IL-2, BC007, immunoadsorption, antiplatelet.

## Sources and Run Metadata

- **OpenAlex** HTTP API (`https://api.openalex.org/works?search=...&filter=from_publication_date:2014-01-01`), 13 broad/class queries + 6 named-trial coverage queries; `per-page` 20–40; selected fields incl. DOI, year, authorships, type, cited_by_count.
- **PubMed E-utilities** (`esearch` relevance-sorted + `esummary`), 18 targeted terms for named landmark trials; metadata (PMID, DOI, journal, first/last author, publication type) captured directly from `esummary`.
- Window: last ~12 years (2014–2026) plus seminal older RCTs (PACE 2011). De-dup by DOI > PMID > normalized title.
- All metadata below taken from API responses. Items where a field could not be confirmed are marked `[UNVERIFIED]`.
- WebSearch not used (no `fallback-web` items).

## Ranked Results

| Rank | Citation | Year | Source IDs | Tier | Why it matters |
|------|----------|------|-----------|------|----------------|
| 1 | Geng LN … Singh U. *Nirmatrelvir-Ritonavir and Symptoms in Adults With PASC: The STOP-PASC RCT.* JAMA Intern Med | 2024 | DOI 10.1001/jamainternmed.2024.2007; PMID 38848477 | **Core now** | Phase 2 placebo-controlled RCT of 15-day nirmatrelvir-ritonavir for established PASC; **null** on PROMIS-29 endpoints. Anchors the antigen-persistence treatment hypothesis and the endpoint problem. |
| 2 | Fluge Ø … Mella O. *B-Lymphocyte Depletion (rituximab) in ME/CFS: A Randomized, Double-Blind, Placebo-Controlled Trial (RituxME).* Ann Intern Med | 2019 | DOI 10.7326/M18-1451; PMID 30934066 | **Core now** | The definitive **negative** rituximab RCT in ME/CFS — overturned promising open-label results. Critical null; cautionary tale on uncontrolled-trial enthusiasm. |
| 3 | Bramante CT … COVID-OUT Study Team. *Outpatient treatment of COVID-19 and incidence of post-COVID-19 condition over 10 months (COVID-OUT).* Lancet Infect Dis | 2023 | DOI 10.1016/S1473-3099(23)00299-2; PMID 37302406 | **Core now** | Quadruple-blind phase-3 RCT: outpatient **metformin reduced long-COVID incidence (~41% RRR)**; ivermectin/fluvoxamine null. Strongest RCT evidence for pharmacologic PASC *prevention*. |
| 4 | Stein E … Kim L (Scheibenbogen group). *Efficacy of repeated immunoadsorption in post-COVID ME/CFS with elevated β2-adrenergic receptor autoantibodies.* Lancet Reg Health Eur | 2025 | DOI 10.1016/j.lanepe.2024.101161; PMID 39759581 | **Core now** | Prospective cohort of autoantibody removal in autoantibody-defined post-COVID ME/CFS subgroup — operationalizes the autoimmunity hypothesis with a stratifying biomarker. |
| 5 | Yotsuyanagi H … Mukae H. *Prevention of post-COVID-19 condition by early ensitrelvir (SCORPIO-SR phase 3).* Antiviral Res | 2024 | DOI 10.1016/j.antiviral.2024.105958; PMID 38972603 | **Core now** | Pre-specified PASC-prevention analysis from a phase-3 antiviral RCT; complements Geng2024 (treatment vs prevention; alternative 3CLpro inhibitor). |
| 6 | Zeraatkar D … Busse JW. *Interventions for the management of long covid: living systematic review.* BMJ | 2024 | DOI 10.1136/bmj-2024-081318; PMID 39603702 | **Core now** | Living SR/meta-analysis of long-COVID RCTs — the map of the controlled-trial landscape and certainty grading; orients the whole topic. |
| 7 | Krumholz HM … Iwasaki A. *The PAX LC Trial: Decentralized Phase 2 RCT of Nirmatrelvir-Ritonavir for Long COVID.* Am J Med | 2024 | DOI 10.1016/j.amjmed.2024.04.030 | **Core now** | Second nirmatrelvir RCT in established long COVID (decentralized design); pairs with STOP-PASC for the antiviral-treatment evidence base. |
| 8 | Bonilla H … Geng LN. *Low-dose naltrexone for management of PASC.* Int Immunopharmacol | 2023 | DOI 10.1016/j.intimp.2023.110966; PMID 37804660 | Relevant next | Retrospective LDN cohort in PASC from the Stanford group; sets up the LDN RCT case. |
| 9 | O'Kelly B … Lambert JS. *Safety and efficacy of low-dose naltrexone in a long-COVID cohort; interventional pre-post study.* Brain Behav Immun Health | 2022 | DOI 10.1016/j.bbih.2022.100485; PMID 35814187 | Relevant next | Prospective interventional (uncontrolled) LDN signal in long COVID. |
| 10 | Tamariz L … Palacio A. *Low-dose Naltrexone Improves post-COVID-19 condition Symptoms.* Clin Ther | 2024 | DOI 10.1016/j.clinthera.2023.12.009; PMID 38267326 | Relevant next | Further LDN clinical evidence in post-COVID condition. |
| 11 | Naik H … Nacul L. *LDN for post-COVID fatigue syndrome: protocol for a double-blind RCT (British Columbia).* BMJ Open | 2024 | DOI 10.1136/bmjopen-2024-085272; PMID 38740499 | Relevant next | Registered double-blind LDN RCT protocol — the controlled test LDN needs; tracks endpoint choice. |
| 12 | Gaylis NB … Yang OO. *Reduced CCR5 and immunosuppression in long COVID* (leronlimab program context). Clin Infect Dis | 2022 | DOI 10.1093/cid/ciac226; PMID 35452519 | Relevant next | Mechanistic/clinical basis for CCR5 antagonism (leronlimab) in long COVID. |
| 13 | White PD … Sharpe M (PACE trial). *Comparison of adaptive pacing, CBT, graded exercise therapy, and specialist medical care for CFS.* Lancet | 2011 | DOI 10.1016/S0140-6736(11)60096-2; PMID 21334061 | Relevant next | The seminal — and **contested** — CFS rehabilitation RCT (GET/PACE controversy); essential context for pacing vs GET. |
| 14 | Wilshire CE … Levin B. *Rethinking the treatment of CFS — a reanalysis and evaluation of findings from a recent major trial of GET and CBT.* BMC Psychol | 2018 | DOI 10.1186/s40359-018-0218-3; PMID 29562932 | Relevant next | The principal published reanalysis challenging PACE recovery claims — the negative/contradiction-value counterpoint. |
| 15 | Sanal-Hayes NEM et al. *A scoping review of 'Pacing' for management of ME/CFS.* J Transl Med | 2023 | DOI 10.1186/s12967-023-04587-5; PMID 37838675 | Relevant next | Synthesizes pacing/energy-management evidence for PEM — the leading non-pharmacologic strategy. |
| 16 | Badran BW et al. *Pilot RCT of supervised, at-home, self-administered transcutaneous auricular VNS* (long COVID context). Bioelectron Med | 2022 | DOI 10.1186/s42234-022-00094-y | Relevant next | Sham-controlled neuromodulation pilot relevant to dysautonomia-targeted long-COVID trials. |
| 17 | Pretorius E et al. *Combined triple treatment of fibrin amyloid microclots and platelet pathology in long COVID* (preprint). | 2021 | DOI 10.21203/rs.3.rs-1205453/v1 | Relevant next | The triple-anticoagulant microclot-targeting protocol (uncontrolled) — the hypothesis controlled trials must test. |
| 18 | REMAP-CAP Investigators (Gordon AC et al.). *Effect of Antiplatelet Therapy on Survival and Organ Support-Free Days in Critically Ill COVID-19: RCT.* JAMA | 2022 | DOI 10.1001/jama.2022.2910; PMID 35315874 | Peripheral monitor | Large antiplatelet RCT (acute, not PASC) — methodological reference; antiplatelet effect did not translate to PASC benefit. |
| 19 | Bonilla H … McComsey GA. *Therapeutic trials for long COVID-19: a call to action from the interventions taskforce.* Front Immunol | 2023 | DOI 10.3389/fimmu.2023.1129459 | Peripheral monitor | Field roadmap of candidate interventions and trial-design priorities. |
| 20 | Antar AAR, Cox AL. *Translating insights into therapies for Long COVID.* Sci Transl Med | 2024 | DOI 10.1126/scitranslmed.ado2106 | Peripheral monitor | Mechanism-to-therapy translation review; ties drug classes to candidate endpoints. |
| 21 | Hohberger B … Wallukat G. *Neutralization of autoantibodies targeting GPCRs (BC007) improves capillary impairment and fatigue after COVID.* Front Med | 2021 | DOI 10.3389/fmed.2021.754667; PMID 34869451 | Peripheral monitor | First-in-human BC007/rovunaptabin aptamer case series — the autoantibody-neutralization hypothesis (RCT pending/reported as null in press). |
| 22 | Strayer DR, Mitchell WM. *Phase III RCT of rintatolimod (Ampligen) in CFS — effect of disease duration.* PLoS One | 2020 | DOI 10.1371/journal.pone.0240403 | Peripheral monitor | One of the few completed phase-3 ME/CFS drug RCTs; immunomodulator (TLR3 agonist) precedent. |
| 23 | Tamariz L et al. / others. *Cochrane-style and JAMA Intern Med STOP-PASC secondary analyses* (digital biometrics, PRO trajectories) | 2025 | DOI 10.1001/jamanetworkopen.2025.26901; 10.1093/ofid/ofaf634 | Peripheral monitor | STOP-PASC secondary analyses exploring objective (digital biometric) endpoints — directly relevant to the endpoint problem. |

## Priority Reading Queue

1. **Geng2024** (STOP-PASC) — flagship antiviral PASC RCT, null; read first for endpoint design.
2. **Fluge2019** (RituxME) — the canonical ME/CFS null; pairs with the open-label results it overturned.
3. **Bramante2023** (COVID-OUT) — the one robustly positive prevention RCT (metformin).
4. **Zeraatkar2024** — living SR; the landscape map.
5. **Stein2025** (immunoadsorption) — autoantibody-stratified intervention.
6. **Yotsuyanagi2024** (SCORPIO-SR) — antiviral *prevention*.
7. **Krumholz2024** (PAX-LC) — second nirmatrelvir long-COVID RCT.

## Coverage Notes and Gaps

| Drug class | ≥1 ranked candidate? | Best item(s) |
|------------|----------------------|--------------|
| Antivirals (nirmatrelvir, ensitrelvir, prevention) | Yes | Geng2024, Krumholz2024, Yotsuyanagi2024 |
| Immunomodulators (IL-6, JAK, IL-2, leronlimab, sirolimus) | Partial | Gaylis2022 (CCR5/leronlimab), Strayer2020 (rintatolimod), Antar2024 review. **Gap:** no dedicated baricitinib/JAK, low-dose IL-2, or sirolimus PASC RCT found — these remain early/trial-stage (sirolimus appears in PAX-LC sub-arms). |
| Anticoagulation / antiplatelet / microclot | Yes | Pretorius2021 (triple therapy, uncontrolled), REMAP-CAP antiplatelet (acute). **Gap:** no completed RCT of anticoagulation specifically for *PASC*; RPTH 2024 editorial challenges the microclot-thrombosis hypothesis. |
| Autoantibody-targeting (BC007, immunoadsorption, rituximab) | Yes | Stein2025 (immunoadsorption), Hohberger2021 (BC007 case), Fluge2019 (rituximab null). **Gap:** the BC007/rovunaptabin **RCT** (reuteractTM/Berlin Cures) result not yet indexed with confirmable metadata — only the 2021 case series surfaced; flag for follow-up. |
| Low-dose naltrexone (LDN) | Yes | O'Kelly2022, Bonilla2023b, Tamariz2024 (all observational/pre-post); Naik2024 (RCT protocol). **Gap:** no completed double-blind LDN RCT yet. |
| Vagal / neuromodulation / brain stimulation | Yes | Badran2022 (tVNS pilot RCT). Thin; mostly pilots. |
| Metabolic (metformin) | Yes | Bramante2023 (COVID-OUT) — strong. |
| Non-pharmacologic pacing / GET / PACE controversy | Yes | Sanal-Hayes2023 (pacing review), White2011 (PACE), Wilshire2018 (reanalysis). |

**Cross-cutting gap (endpoints):** Almost all positive/null results rest on subjective PROs (PROMIS-29, symptom counts, fatigue scales). The STOP-PASC digital-biometrics secondary analysis (2025) and the project's `topic:biomarkers-and-objective-endpoints` highlight the absence of a validated, treatment-responsive objective surrogate — the central methodological weakness of the entire trial landscape and a reason both Geng2024 and Fluge2019 are hard to interpret definitively.

## Recommended Next Actions

1. **Read the 7 Core-now items** and promote a `topic:therapeutics-and-clinical-trials` synthesis tying each drug class to its evidence maturity (RCT vs observational vs hypothesis) and to its endpoint.
2. **Track the BC007/rovunaptabin RCT** (Berlin Cures / reuteractTM) — locate the primary trial report and its (reportedly null) result; the 2021 case series is the only confirmable record so far.
3. **Follow-up search:** dedicated immunomodulator PASC RCTs (baricitinib, low-dose IL-2, sirolimus, tocilizumab) as results mature; RECOVER platform trials (RECOVER-VITAL nirmatrelvir, RECOVER-ENERGIZE pacing/exercise, RECOVER-NEURO).
4. **Link to endpoints topic:** add a note in `topic:biomarkers-and-objective-endpoints` on the PRO-dependence of these trials and the STOP-PASC digital-biometric endpoint exploration.
5. **Pacing vs GET decision note:** consider a `core/decisions.md` entry capturing the project stance that PEM contraindicates incremental GET (post-2021 NICE), distinguishing pacing (energy management) from graded exercise.
