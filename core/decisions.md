<!--
core/decisions.md — load-bearing decisions and the reasoning behind them.
Loaded at session start via AGENTS.md.

Length cap: ~150 lines. When the file outgrows that, move older entries
to doc/decisions/ and keep only the still-load-bearing ones here.

This file is APPEND-ONLY for individual decisions. Do not rewrite a
decision when it is later superseded — add a new entry that references and
supersedes the old one, and update the "Status" line on the original.

Each entry follows the format below. Number entries sequentially.
-->

# Decisions

## D-001: Split post-acute infection syndromes out as their own process project

- **Date:** 2026-06-10 · **Status:** active · **Full reasoning:** `doc/decisions/D-001.md`
- **Decision:** PAIS (long COVID, ME/CFS, PTLDS, post-dengue/Q-fever, post-SARS, PICS) are modeled as a dedicated `process` project under `~/d/health/processes/post-acute-infection`, separate from `health-immunity`. Clinical post-infectious-syndrome work lives here; general immune-mechanism / autoimmunity / tolerance → `health-immunity`; frame-changing cross-project conclusions → `health-meta`; disease-label-vs-biology → `pan-disease`; bridging papers are summarized once and shared via `science commons promote`.

## D-002: Adopt pacing as the default activity-management frame; treat incremental GET as contraindicated where PEM is present

- **Date:** 2026-06-20 · **Status:** active · **Full reasoning:** `doc/decisions/D-002.md`
- **Decision:** For PEM-positive PAIS phenotypes, adopt **pacing / energy-management** (symptom-titrated activity within an energy envelope) as the default activity frame, and treat fixed-increment / deconditioning-model **GET** as **contraindicated**; flag any therapy/trial/endpoint relying on incremental GET in a PEM-positive population as methodologically contested. Provoked-exertion diagnostics (2-day CPET, iCPET) remain endorsed under PEM-crash-risk consent. The stance is **PEM-specific** — always stratify PEM-positive vs PEM-absent before applying.

## D-003: Post-infectious trigger is the in-scope rule; PACVS and GWS/fibromyalgia are boundary-monitor / read-across, not primary scope

- **Date:** 2026-06-21
- **Status:** active
- **Decision:** The `hypothesis:0001` shared dysregulated attractor is held as **post-infection-specific for primary scope**. The headline inclusion rule is **trigger-type: a syndrome is in primary scope only if its trigger is an acute infection.** Two adjacent syndrome classes that fail this rule are ruled **boundary-monitor / read-across** — retained as mechanism evidence to stress-test cross-trigger claims, but **not** counted as in-scope PAIS cases: (a) **post-COVID-vaccination syndrome (PACVS)**, and (b) **non-infectious fatigue syndromes — Gulf War Syndrome (GWS) and fibromyalgia (FM)**. Recorded in `specs/scope-boundaries.md` (new "Boundary-Monitor / Read-Across" section). Trigger: a 2026-06 ingest of five papers (Halma2026, Bellavite2026, Lesgards2025 for PACVS; Davis2025 for GWS/FM) that each independently forced the question, three of them explicitly requesting this adjudication.

**Why:**
- **Trigger-type, not mechanism-overlap, is the discriminating criterion.** Three candidate criteria were tested against the boundary cases: *infection-trigger-required* (excludes PACVS, GWS, FM by one rule; matches the project name), *mechanism-overlap* (admits all three but is over-permissive — it would admit essentially any oxidative/mitochondrial/dysautonomic condition and collapse the boundary), and *PEM-presence* (admits GWS/FM, excludes PACVS). Infection-trigger is the only rule that cleanly bounds primary scope; mechanism-overlap is therefore explicitly rejected as an *admission* criterion (it remains the basis for read-across *retention*).
- **PACVS is excluded by the rule AND sits at the lowest evidence tier.** Its entire PACVS-specific empirical base reduces to one uncontrolled n≈17 ELISA case series reused across three author-overlapping (Bellavite/Di Fede/Halma), COI-disclosed or advocacy-funded narrative reviews; every cross-condition equivalence claim is self-flagged as speculation. The shared-spike-effector idea (same antigen via infection vs. vaccine) is a genuine same-antigen/different-route discriminator and worth monitoring, but is untested by controlled comparison. Admitting it as primary would let the volume of three non-independent papers be mistaken for corroboration.
- **GWS/FM are excluded by the rule but carry mainstream-tier evidence and are the best non-infectious stress-test of `hypothesis:0001`.** Davis2025 documents a shared metabolic/mitochondrial/oxidative lesion plus the PEM metabolic signature (two-CPET) across ME/CFS, GWS, and FM despite non-infectious triggers. GWS — a toxic-chemical trigger reaching the same downstream signature — is the single best external probe of the attractor's trigger-agnostic claim, so it earns read-across retention rather than hard exclusion (which would discard that probe). PEM-presence is the secondary criterion that discriminates GWS/FM (retain) from PACVS (hold at arm's length) within the read-across set.

**Alternatives considered and rejected:**
- **Admit either class as in-scope** (via mechanism-overlap, or mechanism+PEM for GWS/FM) — rejected: redefines the project away from "post-acute *infection*," and for PACVS would import the weakest, most-contested evidence tier as primary subject matter.
- **Hard-exclude all three** (not even monitored) — rejected: discards the PACVS same-antigen/different-route discriminator and the GWS non-infectious stress-test, both of which bear directly on whether `hypothesis:0001`'s trigger-agnostic claim holds. Read-across retains their probative value at the correct (non-primary) weight.

**Implications:**
- Scope-boundaries carries the read-across set; PACVS/GWS/FM papers are summarized as read-across mechanism evidence, never tallied as PAIS cases or as independent cross-trigger support for `hypothesis:0001`.
- Any cross-trigger convergence claim that leans on GWS/FM must state it is a *non-infectious* read-across, and flag the unresolved metabolite-direction conflicts (sphingomyelin/tryptophan/taurine sign flips across conditions).
- PACVS shared-spike claims are represented as hypothesis-to-test with their evidence tier (single uncontrolled case series) stated inline.

**Revisit if:**
- A controlled **PACVS-vs-PASC** biomarker comparison appears (would reopen PACVS for possible admission), or a powered design resolves the GWS/FM metabolite-direction conflicts and establishes a shared-attractor signature on causal (not cross-sectional) footing.

## D-004: Shelve the autoimmune × sex × PASC vehicle-based estimand as infeasible-under-transparency-standards

- **Date:** 2026-07-01
- **Status:** active
- **Supersedes:** the operative "N3C primary" verdict in `interpretation:0031` (marked SUPERSEDED).
- **Decision:** The `task:t078`/`task:t079` autoimmune-diathesis × sex × PASC effect-modifier estimand is **shelved, not executed.** It requires population-scale, individual-level patient EHR (rare autoimmune-stratum × sex power — the binding BC-4 gate), which is a **categorically access-gated, non-downloadable data class.** N3C (the locked primary vehicle) was found gated **and** non-downloadable *even at the synthetic tier* (enclave-only compute); OpenSAFELY carries the same real-data gating (insider-only execution, only disclosure-controlled aggregates leave) despite a more transparent code model. No admissible vehicle can produce this estimate as **third-party-reproducible** knowledge, so the line is shelved rather than run. The **design work is banked** — the two-estimand contrast (total vs controlled-direct + mediation), DAGs, adjustment sets, negative-control + bracketing design, and especially the **`hypothesis:0008` measurement/ascertainment synthesis** remain valid and reusable.

**Why:**
Durable scientific knowledge in this ecosystem must be independently re-runnable and verifiable by an arbitrary third party (see [[avoid-gated-nondownloadable-datasets]] in agent memory). Gated + non-downloadable data breaks this even in the best case: an OpenSAFELY-style result is reproducible only by credentialed insiders behind a manual output-review gate, producing a "gray-zone" knowledge patch — *someone with access ran it and got a number; everyone else can only trust them.* The problem is the **data class**, not the vehicle choice: population-scale patient EHR is inherently gated, so no vehicle swap rescues the estimand. The multi-BC feasibility investment was not wasted — it produced the transparent design residue and the first two entries for a forthcoming reproducibility inventory.

**Alternatives considered and rejected:**
- **Promote OpenSAFELY to primary** — rejected: same real-data gating, still insider-only/trust-based, and it reintroduces the coded-long-COVID differential under-recording problem (`interpretation:0033`/BC-5) that had made it replication-not-primary.
- **Accept gated-execution vehicles** ("open code + gated data + aggregate outputs" is good enough) — rejected: it violates the third-party-reproducibility bar and normalises gray-zone patches into the knowledge base.

**Implications:**
- `task:t079` → deferred (shelved); `plan:0005` stays `not-ready` (it never became viable) with a SHELVED banner; `plan:0006` → archived; `interpretation:0031` → superseded; the `doc:` feasibility memo carries a SHELVED banner. `task:t080`/`t081`/`t082` → deferred.
- N3C and OpenSAFELY are to be recorded as **below-bar / non-third-party-reproducible** in the reproducibility inventory scoped in `~/d/science` — specifically `trust-based-output` (TRE / aggregate-output vehicles: reviewed aggregates *do* leave, so they are **not** `insider-only`). This is the change that would have flagged N3C at *plan* time. (Wording refined 2026-07-01: the formal Five-Safes classifier yields `trust-based-output`, one notch above the informal "insider-only" first written here; both sit below the third-party-reproducible bar, so the shelve conclusion is unchanged.)
- The `hypothesis:0008` synthesis is the durable residue and remains live for other lines.

**Revisit if:**
- A population-scale EHR vehicle offers a genuinely **third-party-reproducible** access path (downloadable de-identified individual-level data, or a truly open/downloadable synthetic tier), **or** the estimand is reformulated so it no longer requires population-scale gated EHR.

## D-005: Authorize only the Wave-1 open GWAS/MR pilot as the first post-seed computational analysis

- **Date:** 2026-07-04
- **Status:** active
- **Extended by:** D-006 (2026-07-04) — clarifies that reportable-grade promotion of this vehicle (`plan:0008`) is in-scope "direct maintenance", and holds FinnGen as a distinct vehicle.
- **Decision:** The project may cross the `specs/scope-boundaries.md` seed-stage boundary for the **specific Wave-1 GWAS/MR pilot** described in `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`: two-sample MR over the three cataloged public GWAS summary-statistic vehicles (`dataset:covid19-hgi-longcovid-gwas`, `dataset:bentham-2015-sle-gwas`, and `dataset:ruth-2020-shbg-testosterone-gwas`), with IVW primary and the pre-committed sensitivity/bridge-assumption checklist in that handoff.
This decision authorizes planning and implementation of that open, third-party-reproducible pilot only.
It does **not** authorize gated-data analysis, patient-level EHR analysis, N3C/OpenSAFELY execution, or a general transition to unrestricted computational pipeline work.

**Why:**
The scope boundary was written to prevent premature large-scale analysis while the project was still establishing its literature and hypothesis frame.
The Wave-1 data-catalog arc now supplies a narrow, auditable, third-party-reproducible vehicle: public summary statistics with resolvable accessions, explicit dataset entities, declared capabilities, and a handoff contract that separates cataloging from execution.
That vehicle clears the transparency objection behind D-004 because arbitrary third parties can retrieve the same public summary-statistic inputs and rerun the intended analysis.
The scientific estimand is also narrower than the shelved autoimmune x sex x PASC EHR line: it is a germline-liability instrumental-variable effect under MR assumptions, not an individual-level diagnosis/treatment/ascertainment-structured effect and not a reconstruction of the D-004 estimand.

**Alternatives considered and rejected:**
- Keep the project fully at seed-stage literature synthesis — rejected because it would treat a fully open, deliberately constrained empirical pilot the same as gated EHR execution, losing a useful reproducible test without reducing a real transparency risk.
- Declare the project generally "past seed stage" for computational work — rejected as too broad.
The current authorization is intentionally vehicle-specific; future computational lines need their own scope decision unless they are direct maintenance of this pilot.
- Reopen the N3C/OpenSAFELY EHR path under the same ruling — rejected.
D-004 still governs gated, non-downloadable EHR vehicles and remains unchanged.

**Implications:**
- `task:t088` is resolved for the Wave-1 MR vehicle.
- `task:t089` may move to the `/science:plan-pipeline` handoff for this pilot.
- Pipeline planning must preserve the handoff's constraints: public retrievable inputs, recorded hashes/datapackages for staged files, ancestry/case-definition/sample-overlap/HLA sensitivity checks, and interpretation only as germline-liability IV evidence.
- Any additional computational analysis line beyond this Wave-1 vehicle requires a separate scope decision unless a future decision explicitly broadens this ruling.

**Revisit if:**
- A planned step needs non-public, credentialed, enclave-only, or non-downloadable data; the MR estimand is expanded toward the D-004-shelved EHR estimand; or the pilot design drops below the project's third-party-reproducible bar.

## D-006: Wave-1 MR reportable-grade promotion (plan:0008) is direct maintenance of the D-005 pilot; FinnGen held as a distinct vehicle

- **Date:** 2026-07-04
- **Status:** active
- **Extends:** D-005 (does not supersede). Discharges `plan:0008` WP0 (the authorisation scope gate).
- **Decision:** The reportable-grade Wave-1 MR design (`plan:0008`) is **direct maintenance of the D-005-authorised pilot vehicle**, not a new computational line, and needs no separate scope authorisation for its primary path. Classifying each input `plan:0008` adds beyond the three D-005 vehicles:
  - **(a) EUR-matched long-COVID outcome — in-scope (same vehicle).** Sourcing a European-ancestry long-COVID **outcome** from the **Long COVID HGI** distribution — the DF4 freeze via LocusZoom (`my.locuszoom.org/gwas/793752/`, "Long COVID HGI – DF4 N1", GRCh38, publicly downloadable without registration), the `covid19hg.org/results` portal, or a GWAS Catalog EUR stratum — is the **same measured-phenotype vehicle** as the D-005-authorised `dataset:covid19-hgi-longcovid-gwas`, in a different freeze/channel. Whether a genuinely EUR-specific stratum exists within that vehicle is a **WP1 factual question**, not presumed here; if none does, `plan:0008` KD1's demotion-to-mechanics-only applies.
  - **(b) LD-score + HapMap3 references — in-scope (infrastructure).** The `eur_w_ld_chr` EUR LD-score reference and the HapMap3 SNP list that the MRlap overlap correction requires are **analysis infrastructure**, the same class as the LD reference panel (`dataset:1000g-eur-ld-panel`) the D-005 pilot already used for clumping — not measured-phenotype vehicles.
  - **(c) FinnGen long-COVID — held (distinct vehicle).** FinnGen (`plan:0008` KD1 rung 3) is a **distinct measured-phenotype vehicle**, not the HGI vehicle. It may **not** be used until (i) a separate decision broadens scope to it **and** (ii) its results-access path is confirmed to clear the third-party-reproducible bar (the `finngen.fi` form/email-mediated access is unverified against that bar). Because (a)/(b) are expected to satisfy the EUR-outcome need, FinnGen stays a contingency and is **not** authorised here.

**Why:**
D-005 already contemplates "direct maintenance of this pilot" as not needing a fresh scope decision, and names the HGI long-COVID GWAS as an authorised vehicle. Promoting the pilot to reportable grade reuses that same vehicle (a different HGI freeze is the same public data source) plus LD-reference infrastructure of the kind the pilot already used. The only genuinely new vehicle — FinnGen — is the only element that would need fresh authorisation, and it is held rather than used. Every authorised input remains public and third-party-retrievable, so the D-004 transparency bar is intact.

**Alternatives considered and rejected:**
- Treat `plan:0008` as a wholly new computational line needing full re-authorisation — rejected as over-ceremony; it is the same vehicle promoted, which D-005 already covers as maintenance.
- Pre-authorise FinnGen as a drop-in rung — rejected; distinct vehicle, unverified access path, and unnecessary if the HGI vehicle yields a EUR stratum.
- Rewrite D-005 in place — rejected; `decisions.md` is append-only, so this extends D-005 via a new entry.

**Implications:**
- `plan:0008` WP0 is discharged; WP1 (acquire the HGI EUR distribution) and WP2 (stage `eur_w_ld_chr` + HapMap3) may proceed.
- Any use of FinnGen — or any other non-HGI outcome vehicle — requires a new decision plus a reproducibility-class check first.
- If WP1 finds no EUR-specific HGI stratum, the ancestry hard-stop is not lifted and `plan:0008` KD1 demotes the primary to mechanics/robustness-only.

**Revisit if:**
- No EUR outcome can be sourced from the HGI vehicle and FinnGen (or another vehicle) becomes necessary; or any authorised input's access path drops below the third-party-reproducible bar.

## D-007: Authorize the atopy→long-COVID MR *feasibility packet* only (public sumstats); MR execution gated on a follow-up ratification

- **Date:** 2026-07-18
- **Status:** active
- **Extends:** D-005 (does not supersede). Applies the 2026-07-18 ruling that a **new exposure** against the authorised HGI outcome is a new computational line requiring a fresh D-005 decision (not D-006 maintenance).
- **Decision:** The project may run the **feasibility packet** for an atopy→long-COVID two-sample MR — `dataset:gcst005038-allergic-disease-gwas` (exposure) × `dataset:covid19-hgi-longcovid-gwas` (outcome): (1) instrument construction/clumping, (2) empirical **liability-scale** instrument R², (3) UKB↔HGI **sample-overlap** quantification, (4) binary-exposure **scale** definition — all on public summary statistics. This authorises the feasibility/screening work **only**. MR **execution** (IVW-primary + sensitivity checklist) is **not** authorised here and needs a **follow-up ratification (D-007b)** once the packet clears pre-registered thresholds. The outcome's ancestry status is the **same WP1 question** as `plan:0008` KD1 / D-006(a); if no EUR-specific HGI stratum exists, any eventual estimate inherits the **mechanics/robustness-only demotion** — this is not a reportable-primary MR vehicle on the current outcome file.

**Why:**
The 2026-07-18 power screen left atopy as the only surviving MR candidate among the t110 boundary-strata instruments, but a *provisional* survivor with four undischarged, public-data prerequisites. Those prerequisites are the cheap, transparent work that turns "provisional" into a decidable yes/no; authorising them and only them tests feasibility without pre-committing to an execution whose reportable status is already ancestry-capped. Every input is public and third-party-retrievable (D-004 intact), and the estimand is the same germline-liability IV class D-005 authorised.

**Alternatives considered and rejected:**
- Authorise the full line (feasibility + execution) now — rejected as premature: reportable status is ancestry-capped, and three of four prerequisites (R², overlap, scale) could still sink the line; execution authorisation should follow the evidence.
- Decline/defer all effort until a EUR-matched outcome exists — rejected: the packet is cheap, fully public, and its outputs (instrument strength, overlap, scale) are reusable whenever a matched outcome appears; deferring discards that at no transparency saving.
- Treat it as D-006-style maintenance needing no decision — rejected: it adds a new exposure vehicle, which the recorded ruling classes as a new line.

**Implications:**
- `task:t135` is resolved (scope decision taken): feasibility-only authorised, execution deferred.
- A feasibility-packet task carries the four deliverables; its outputs are the go/no-go inputs for the D-007b execution ratification.
- Scope of estimand: this vehicle speaks only to **broad allergic-disease liability**, not q0034's stronger atopy/MCAS-subgroup question. No gated data, no execution, no new outcome vehicle authorised.

**Revisit if:**
- The packet clears thresholds (→ raise D-007b for execution); or the R²/overlap/scale work shows the line cannot detect the pre-registered floor (OR≳1.2) (→ shelve atopy too); or a EUR-matched HGI outcome becomes available (→ revisit the ancestry cap).
