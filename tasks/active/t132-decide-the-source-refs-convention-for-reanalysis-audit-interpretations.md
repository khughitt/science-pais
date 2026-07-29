---
id: t132
project: ''
title: Decide the source_refs convention for reanalysis/audit interpretations
type: ''
aspects: []
priority: P3
status: proposed
blocked_by: []
related: []
parent: ''
group: ''
artifacts: []
findings: []
created: '2026-07-17'
completed: null
---

Carry-over from curation sweep 2026-07-10 (PD-3 there), re-verified unresolved in the 2026-07-16 sweep - unchanged across both, hence filed as a task rather than carried a third time. Nine artifacts lack source_refs: interpretation:0010-t006-functional-gpcr-autoantibody-ingestion, 0011-t046-antigen-clearance-trials-ingestion, 0012-t047-h0003-ifn-reconciliation, 0013-t050-novak2026-ingestion, 0014-sfn-prevalence-metric-harmonization-reanalysis, 0015-t055-measurement-channel-audit, 0016-t054-abrocitinib-trial-status-snapshot, 0017-t053-h0002-promotion-audit, plus paper:BrandstetterFigueroa2025. The 2026-07-10 sweep judged this a provenance-FIELD-PLACEMENT issue, not missing provenance: these entities do carry provenance, via related:/input: paper edges rather than source_refs. Decide: (a) backfill source_refs from the existing related: paper edges on the 8 interpretations, or (b) ratify related:/input: as the provenance channel for the reanalysis/audit interpretation class and suppress the inventory signal. Note interpretation:0015 is load-bearing for hypothesis:0008 (the t055 measurement-channel audit), so its provenance should be legible whichever way this lands. BrandstetterFigueroa2025 is a paper, not an interpretation - triage it separately; it may be a plain omission.
