---
id: t080
project: ''
title: Acquire N3C Enclave account + open synthetic-tier access (gates plan:0006 WP0)
type: ''
aspects: []
priority: P2
status: deferred
blocked_by: []
related: []
parent: ''
group: ''
artifacts: []
findings: []
created: '2026-07-01'
completed: null
---

plan:0006/BC-2 WP0 needs the N3C open synthetic OMOP data package. Even the synthetic tier requires an N3C Enclave account. On acquisition: set dataset:n3c-recover-longcovid-synthetic local_path + verified:true + verification_method + last_reviewed, and confirm the OMOP CDM version. Blocks any runnable WP0/WP2 code.

### Notes

- 2026-07-01: 2026-07-01: CONCRETE ACCESS CHECKLIST (grounded in current NCATS/CD2H onboarding docs, web-verified 2026-07-01).

PATH DECISION (step 0): Citizen-scientist route is DEFAULT and sufficient. NCATS FAQ confirms citizen scientists (individuals with no institutional affiliation) CAN join N3C and are RESTRICTED to the synthetic dataset — which is exactly and only what plan:0006 targets. This means NO institutional Data Use Agreement / Authorized Official signature is needed (the affiliation blocker that sank the All-of-Us path in t039 does NOT apply here). If Keith already has a home institution with a DUA on file with NCATS, the affiliated route is faster — but the citizen-scientist route needs no institutional dependency, so default to it.

STEPS:
1. Register at the N3C onboarding portal (via ncats.nih.gov/research/research-activities/n3c/data-overview/access) and request an N3C Enclave account. [UNVERIFIED] exact identity/login provider (Login.gov vs eRA Commons) — FAQ does not pin it; resolve at the registration screen or email ncats_n3c@mail.nih.gov.
2. DUA: citizen scientists sign an INDIVIDUAL DUA (the Authorized-Official institutional DUA path is only for affiliated users). [UNVERIFIED] exact citizen-scientist DUA form/mechanism — NCATS FAQ confirms the citizen-scientist tier exists but does not publish the individual-DUA form; confirm with N3C program staff (ncats_n3c@mail.nih.gov). This is the one procedural unknown.
3. Log into the Enclave (an account alone does NOT grant data access).
4. Training: HSR/human-subjects-research training is NOT required for synthetic-only access (web-confirmed). The generic NIH information-security refresher course may still be required before submitting a DUR — budget ~60-90 min.
5. Submit the Data Use Request (DUR): project title, non-confidential/public research statement, project plan, DATA LEVEL = SYNTHETIC, attest to the DUA + N3C Data User Code of Conduct. NO IRB determination letter needed (that is only for the Limited Data Set tier).
6. DAC (Data Access Committee) review: ~15 business days end-to-end per FAQ (10 business days review + 3 for workspace creation).
7. On approval: confirm the synthetic OMOP CDM version; set dataset:n3c-recover-longcovid-synthetic -> verified:true + verification_method + last_reviewed + a stageable pointer, then rerun the plan:0006 data-availability gate.

MAKE-OR-BREAK UNKNOWN (resolve DURING onboarding, blocks the plan:0006 dual-runtime design): N3C synthetic data has historically been ENCLAVE-ONLY compute with NO row-level extraction, identical to the real tier. plan:0006 assumes a LOCAL synthetic slice runnable under duckdb (the ohdsi_shim local leg, review finding F1). If N3C offers NO downloadable synthetic OMOP package (enclave-Spark only), that assumption is FALSE and the dual-runtime shim loses its local substrate -> either (a) develop against a self-generated OMOP-shaped synthetic fixture locally and treat the enclave synthetic tier as the first Spark target, or (b) drop the local-duckdb leg. VERIFY whether a downloadable synthetic package exists before committing WP0 code. This is the decisive t080 deliverable, not just 'get an account'.

Feeds F2 (dataset:n3c-recover-longcovid-synthetic stageability) and gates plan:0006 WP0/WP2. No participant data involved (synthetic).
- 2026-07-01: 2026-07-01: BLOCKED on reproducibility/transparency grounds (user decision, verified 2026-07-01). Keith checked: N3C synthetic data CANNOT be downloaded — it is enclave-only compute, same as the real tier. Combined with the data being access-gated (DUR/DAC), BOTH properties (gated + non-downloadable) break the project's core reproducibility + transparency goals: there is no open substrate to develop or reproduce against, even at the synthetic tier. => The 'open synthetic tier to prototype' premise that made N3C the LOCKED primary vehicle (interpretation:0031, memo headline) is FALSE. Do NOT pursue N3C in future efforts unless N3C changes its access model (e.g. releases a downloadable synthetic package). This blocks plan:0006 (the N3C synthetic prototype pipeline) at its substrate, not just WP0. Reopens the vehicle decision — see t079 note. t081 (Athena, public vocab) is independent and unaffected.
- 2026-07-01: 2026-07-01: Deferred under D-004 (parent line shelved). N3C stays off the table unless it offers a third-party-reproducible access path (downloadable de-id individual-level data or a truly downloadable synthetic tier).
