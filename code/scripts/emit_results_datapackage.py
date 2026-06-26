# science:code
# status: exploratory
# task_ids: [t035, t064]
# science:end

#!/usr/bin/env python3
"""Emit a deterministic Frictionless-style datapackage for t035 result outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]

TERMINAL_RESULTS = [
    Path("results/verdict.json"),
    Path("results/results.md"),
    Path("results/run_metadata.json"),
]

QA_RESULTS = [
    Path("results/qa/GSE14577_raw.qa_report.md"),
    Path("results/qa/GSE130353_raw.qa_report.md"),
    Path("results/qa/GSE14577_clean.qa_report.md"),
    Path("results/qa/GSE130353_clean.qa_report.md"),
    Path("results/qa/genesets_clean.qa_report.md"),
    Path("results/qa/t035_results.qa_report.md"),
    Path("results/qa/t035_results.qa.pass"),
]


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_yaml(path: Path) -> dict[str, Any]:
    obj = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError(f"config root must be an object: {path}")
    return obj


def sorted_keys(mapping: dict[str, Any], label: str) -> list[str]:
    keys = list(mapping.keys())
    if not keys:
        raise ValueError(f"config {label} must not be empty")
    return keys


def expected_result_paths(config: dict[str, Any]) -> list[Path]:
    contrasts = sorted_keys(config["contrasts"], "contrasts")
    dbs = sorted_keys(config["genesets"]["databases"], "genesets.databases")
    pairs = sorted_keys(config["concordance_pairs"], "concordance_pairs")

    paths: list[Path] = []
    paths.extend(TERMINAL_RESULTS)
    paths.extend(QA_RESULTS)

    for contrast in contrasts:
        paths.append(Path(f"data/processed/de/{contrast}.ranked.tsv"))
        paths.append(Path(f"data/processed/de/{contrast}.diag.json"))

    for contrast in contrasts:
        for db in dbs:
            paths.append(Path(f"data/processed/fgsea/{contrast}.{db}.nes.tsv"))

    for pair in pairs:
        for db in dbs:
            paths.append(Path(f"data/processed/concordance/{pair}.{db}.rho.tsv"))
            paths.append(Path(f"data/processed/concordance/{pair}.{db}.scatter.tsv"))
            paths.append(Path(f"data/processed/perm/{pair}.{db}.perm.tsv"))
            paths.append(Path(f"data/processed/perm/{pair}.{db}.nulldist.tsv"))

    for db in dbs:
        paths.append(Path(f"data/processed/specificity/{db}.classes.tsv"))
        paths.append(Path(f"data/processed/rollup/{db}.themes.tsv"))

    paths.append(Path("data/processed/rollup/db_robustness.tsv"))
    paths.append(Path("data/processed/rollup/compartment.tsv"))
    return paths


def resource_group(path: Path) -> str:
    parts = path.parts
    if parts[:2] == ("results", "qa"):
        return "qa"
    if parts[:1] == ("results",):
        return "terminal"
    if len(parts) >= 3 and parts[:2] == ("data", "processed"):
        return parts[2]
    return "result"


def resource_name(path: Path) -> str:
    return re.sub(r"[^a-z0-9]+", "-", path.as_posix().lower()).strip("-")


def absolute_for(path: Path, *, processed: Path, results: Path) -> Path:
    parts = path.parts
    if parts[:2] == ("data", "processed"):
        return processed / Path(*parts[2:])
    if parts[:1] == ("results",):
        return results / Path(*parts[1:])
    return ROOT / path


def resource_for(path: Path, *, processed: Path, results: Path) -> dict[str, Any]:
    abs_path = absolute_for(path, processed=processed, results=results)
    if not abs_path.exists():
        raise FileNotFoundError(f"missing expected t035 result resource: {path}")
    return {
        "name": resource_name(path),
        "path": path.as_posix(),
        "title": path.as_posix(),
        "bytes": abs_path.stat().st_size,
        "hash": "sha256:" + sha256_path(abs_path),
        "mediatype": mediatype_for(path),
        "group": resource_group(path),
    }


def mediatype_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return "application/json"
    if suffix == ".md":
        return "text/markdown"
    if suffix == ".tsv":
        return "text/tab-separated-values"
    return "text/plain"


def first_provenance_date(*objects: Any) -> str | None:
    text = "\n".join(json.dumps(obj, sort_keys=True) if not isinstance(obj, str) else obj for obj in objects)
    dates = sorted(set(re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", text)))
    return dates[-1] if dates else None


def run_identity(resources: list[dict[str, Any]], metadata: dict[str, Any], verdict: dict[str, Any]) -> str:
    payload = {
        "metadata": metadata,
        "resources": [{"path": r["path"], "hash": r["hash"], "bytes": r["bytes"]} for r in resources],
        "verdict": verdict.get("verdict"),
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_datapackage(*, processed: Path, results: Path, config: dict[str, Any]) -> dict[str, Any]:
    # Paths in the manifest are repo-relative because the workflow pins workdir to ROOT.
    resources = [resource_for(path, processed=processed, results=results) for path in expected_result_paths(config)]
    metadata_path = results / "run_metadata.json"
    verdict_path = results / "verdict.json"
    report_path = results / "results.md"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
    report = report_path.read_text(encoding="utf-8")
    identity = run_identity(resources, metadata, verdict)
    date = first_provenance_date(metadata, verdict, report)

    descriptor: dict[str, Any] = {
        "name": "t035-cross-trigger-pathway-overlap-results",
        "title": "t035 cross-trigger pathway-overlap result bundle",
        "description": (
            "Deterministic manifest for project-specific t035 workflow outputs: "
            "terminal verdict/report metadata, result QA reports, and generated "
            "analysis tables. Raw and clean-base payloads are intentionally excluded."
        ),
        "profile": "data-package",
        "id": f"sha256:{identity}",
        "sources": [
            {
                "title": "pre-registration:0002-cross-trigger-pathway-overlap",
                "path": "entities/pre-registrations/0002-cross-trigger-pathway-overlap.md",
            },
            {
                "title": "plan:0003-cross-trigger-pathway-overlap-pipeline",
                "path": "entities/plans/0003-cross-trigger-pathway-overlap-pipeline.md",
            },
            {
                "title": "input acquisition datapackage",
                "path": "data/processed/datapackage.json",
            },
        ],
        "resources": resources,
        "pais": {
            "entities": metadata.get("entities", []),
            "verdict": metadata.get("verdict", verdict.get("verdict")),
            "run_metadata_hash": "sha256:" + sha256_path(metadata_path),
        },
    }
    if date is not None:
        descriptor["created"] = date
        descriptor["updated"] = date
    return descriptor


def write_datapackage(*, processed: Path, results: Path, config: dict[str, Any], out: Path) -> None:
    descriptor = build_datapackage(processed=processed, results=results, config=config)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(descriptor, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--processed", required=True, type=Path)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    write_datapackage(processed=args.processed, results=args.results, config=config, out=args.out)
    print(f"[emit_results_datapackage] wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
