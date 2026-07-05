---
id: "evidence-line:0017-dengue-meta-sexneutral-acute-female-postacute-fatigue-supports-persistence-concentration"
kind: "evidence-line"
title: "Dengue sex-neutral acute severity but female post-dengue fatigue supports persistence-concentration"
status: "active"
stance: "supports"
target: "proposition:0008-female-excess-concentrates-in-post-acute-persistence"
source: "dataset:dengue-postinfective-fatigue-meta"
strength: "moderate"
independence: "independent"
independence_group: "post-dengue-fatigue-meta"
evidence_role: "proxy_support"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0008-female-excess-concentrates-in-post-acute-persistence"
  - "question:0007-mechanism-of-female-predominance-in-pais"
source_refs:
  - "paper:Hertanti2025"
  - "paper:Conde2026"
  - "dataset:colombo-dengue-study"
created: "2026-06-22"
updated: "2026-06-22"
---

# Evidence Line: Dengue sex-neutral acute severity but female post-dengue fatigue supports persistence-concentration

## What this line shows

Acute dengue severity (severe dengue / DHF) is **not** female-predominant, yet post-dengue fatigue carries a clear female excess: OR ≈ 1.65 (Hertanti2025, 40 studies) and ≈ 1.69 (Conde2026, 9 studies), corroborated within-trigger by the Colombo cohort (Sigera2021, fatigue RR 2.45). The female excess thus **appears in persistence** despite a sex-neutral acute phase — the pattern `proposition:0008` predicts [@Hertanti2025; @Conde2026; @Sigera2021].

## Why it is independent

A distinct trigger (dengue) from the COVID meta (`evidence-line:0016`) and the Q-fever natural experiment (`evidence-line:0018`). **Internal non-independence is collapsed, not double-counted:** Hertanti2025 and Conde2026 share primary studies (per Conde2026), so they are represented here as **one** consolidated line under `independence_group: post-dengue-fatigue-meta`; the Colombo cohort is treated as same-trigger corroboration whose overlap with the meta primaries is unverified, so it does not add an independent dengue line.

## Caveats / scope

`proxy_support`, moderate: the fatigue arms are well-powered (n in the tens of thousands), but the acute-vs-post-acute contrast is again **between-study** (acute severity series vs post-acute fatigue surveys), not a within-cohort phase interaction. Pooled, mostly unadjusted ORs across heterogeneous case definitions. The dengue *depression* arm is uninterpretable (2 studies/169 pts; Colombo excluded baseline mood disorders) and contributes nothing here — this line is about phase location, not domain [@Conde2026; @Sigera2021].
