# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""datapackage.py — WP6 result-bundle manifest for t117.

Frictionless-style datapackage.json for manifest parity with the rest of results/
(review Dimension 9; mirrors code/workflows/t116-power-bias-floor emit). Lists the
run's terminal + intermediate result resources with sizes + sha256, and cross-
references the deliverable interpretation, the workflow, and the config as sources.
Regenerable; results/* is gitignored.

Fail-early: every declared resource must exist on disk (a missing terminal artifact
is a real pipeline gap, not a manifest to paper over) — a missing path HALTs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def halt(msg: str):
    raise SystemExit(f"[datapackage] HALT: {msg}")


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


# (name, repo-relative path, mediatype, group). Paths are the actual result artifacts;
# `results` is the workflow results root passed on the CLI.
def _resources_meta(res: str):
    return [
        # terminal deliverables
        ("grid-strict", f"{res}/grid/strict.grid.json", "application/json", "terminal"),
        ("grid-sensitivity", f"{res}/grid/sensitivity.grid.json", "application/json", "terminal"),
        ("calibration-verdict", f"{res}/calibration/calibration.pass", "application/json", "terminal"),
        ("specificity-gws-fm", f"{res}/specificity/gws_fm.json", "application/json", "terminal"),
        # supporting result artifacts (the descriptive R + adjudication the grid consumes)
        ("calibration-detail", f"{res}/calibration/calibration.json", "application/json", "support"),
        ("rank-strict", f"{res}/rank/strict.rank.json", "application/json", "support"),
        ("rank-sensitivity", f"{res}/rank/sensitivity.rank.json", "application/json", "support"),
        ("stability-strict", f"{res}/rank/strict.stability.json", "application/json", "support"),
        ("stability-sensitivity", f"{res}/rank/sensitivity.stability.json", "application/json", "support"),
        ("adjudicated-strict", f"{res}/artifact/strict.adjudicated.json", "application/json", "support"),
        ("adjudicated-sensitivity", f"{res}/artifact/sensitivity.adjudicated.json", "application/json", "support"),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, help="workflow results root (config paths.results)")
    ap.add_argument("--config", required=True, help="config path (recorded as a source)")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    resources = []
    for name, rel, mediatype, group in _resources_meta(args.results):
        p = Path(rel)
        if not p.exists():
            halt(f"declared resource missing on disk: {rel} — a terminal/support artifact is not built")
        resources.append({
            "name": name, "path": str(p), "title": str(p),
            "bytes": p.stat().st_size, "hash": _sha256(p),
            "mediatype": mediatype, "group": group,
        })
    pkg_id = "sha256:" + hashlib.sha256(
        "".join(sorted(r["hash"] for r in resources)).encode()).hexdigest()
    pkg = {
        "name": "t117-crosspais-rank-results",
        "title": "t117 cross-PAIS pathway-response rank-estimation result bundle",
        "description": ("Deterministic manifest for the t117 rank-estimation outputs (grid placement "
                        "records, Stage-3c calibration verdict, descriptive rank + stability, "
                        "artifact/compartment adjudication, and the WP4b GWS/FM specificity read-across). "
                        "Grid placement is fail-closed: no R is placed on the t116 grid because Stage-3c "
                        "calibration failed. Regenerable; results/* is gitignored."),
        "profile": "data-package",
        "id": pkg_id,
        "sources": [
            {"title": "interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed",
             "path": "entities/interpretations/0038-t117-crosspais-rank-nonidentified-fail-closed.md"},
            {"title": "plan:0010-crosspais-pathway-response-rank-estimation",
             "path": "entities/plans/0010-crosspais-pathway-response-rank-estimation.md"},
            {"title": "workflow", "path": "code/workflows/t117-crosspais-rank/Snakefile"},
            {"title": "config", "path": args.config},
        ],
        "entities": [
            "task:t117",
            "plan:0010-crosspais-pathway-response-rank-estimation",
            "interpretation:0038-t117-crosspais-rank-nonidentified-fail-closed",
            "interpretation:0037-t116-power-bias-floor-shared-axis-sim",
            "question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design",
            "hypothesis:0001-shared-dysregulated-attractor",
            "dataset:gse221921-fibromyalgia-pbmc",
        ],
        "resources": resources,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(pkg, indent=2))
    print(f"[datapackage] wrote {args.out} ({len(resources)} resources, id={pkg_id[:19]}…)")


if __name__ == "__main__":
    main()
