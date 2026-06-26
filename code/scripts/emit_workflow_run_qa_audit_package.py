# science:code
# status: workflow-owned
# task_ids: [t035, t066]
# science:end

#!/usr/bin/env python3
"""Emit the t035 workflow-run package consumed by `science qa-audit`."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

import yaml


RUN_NAME = "t035-cross-trigger-pathway-overlap-verdict"
WORKFLOW_NAME = "t035-cross-trigger-pathway-overlap"

QA_CHECKPOINTS = [
    ("gse14577_raw", Path("qa/GSE14577_raw.qa_report.md"), "GSE14577 raw acquisition QA"),
    ("gse130353_raw", Path("qa/GSE130353_raw.qa_report.md"), "GSE130353 raw acquisition QA"),
    ("gse14577_clean", Path("qa/GSE14577_clean.qa_report.md"), "GSE14577 clean matrix QA"),
    ("gse130353_clean", Path("qa/GSE130353_clean.qa_report.md"), "GSE130353 clean matrix QA"),
    ("genesets_clean", Path("qa/genesets_clean.qa_report.md"), "MSigDB mapped gene-set universe QA"),
    ("t035_results", Path("qa/t035_results.qa_report.md"), "t035 terminal result-bundle QA"),
]


ENTITY_GROUPS = {
    "task": "tasks",
    "pre-registration": "pre_registrations",
    "plan": "plans",
    "hypothesis": "hypotheses",
    "question": "questions",
    "interpretation": "interpretations",
}


def load_json(path: Path) -> dict[str, Any]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError(f"{path}: JSON root must be an object")
    return obj


def validate_inputs(results: Path) -> dict[str, Any]:
    metadata_path = results / "run_metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(f"missing t035 run metadata: {metadata_path}")
    for _, rel_path, _ in QA_CHECKPOINTS:
        path = results / rel_path
        if not path.exists():
            raise FileNotFoundError(f"missing t035 QA source report: {path}")
    sentinel = results / "qa/t035_results.qa.pass"
    if not sentinel.exists():
        raise FileNotFoundError(f"missing t035 result QA sentinel: {sentinel}")
    return load_json(metadata_path)


def grouped_entities(metadata: dict[str, Any]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {value: [] for value in ENTITY_GROUPS.values()}
    for ref in metadata.get("entities", []) or []:
        if not isinstance(ref, str) or ":" not in ref:
            continue
        prefix = ref.split(":", 1)[0]
        key = ENTITY_GROUPS.get(prefix)
        if key is not None:
            grouped[key].append(ref)
    return {key: values for key, values in grouped.items() if values}


def qa_report_payload(slug: str, title: str, source_report: Path) -> dict[str, Any]:
    return {
        "title": title,
        "source_report": source_report.as_posix(),
        "flags": [],
        "coverage": {
            "ran": 1,
            "executable_denominator": 1,
            "empty": 0,
            "blocked": 0,
        },
        "notes": [
            "Legacy t035 QA checkpoints emit markdown reports and build-fatal sentinels; "
            "this JSON ledger exposes their successful execution to science qa-audit."
        ],
        "checkpoint": slug,
    }


def build_package(*, results: Path) -> dict[str, Any]:
    metadata = validate_inputs(results)
    entities = grouped_entities(metadata)

    resources: list[dict[str, Any]] = [
        {
            "name": "run_metadata",
            "path": "run_metadata.json",
            "mediatype": "application/json",
        },
    ]
    for slug, rel_path, title in QA_CHECKPOINTS:
        resources.append(
            {
                "name": f"qa_report:{slug}",
                "path": f"qa/{slug}.qa_report.json",
                "mediatype": "application/json",
                "source_report": rel_path.as_posix(),
                "title": title,
            }
        )

    descriptor: dict[str, Any] = {
        "name": RUN_NAME,
        "title": "t035 cross-trigger pathway-overlap workflow run",
        "profile": "data-package",
        "status": "complete",
        "workflow": {
            "name": WORKFLOW_NAME,
            "method": "snakemake",
        },
        "description": (
            "Retrospective workflow-run package for the completed t035 Snakemake run. "
            "It exposes the run metadata and QA checkpoint coverage in the resource "
            "shape consumed by science qa-audit."
        ),
        "resources": resources,
    }
    if entities:
        descriptor["entities"] = entities
    verdict = metadata.get("verdict")
    if isinstance(verdict, str):
        descriptor["verdict"] = verdict
    return descriptor


def write_package(*, results: Path, out_dir: Path) -> Path:
    descriptor = build_package(results=results)
    out_dir.mkdir(parents=True, exist_ok=True)
    qa_dir = out_dir / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(results / "run_metadata.json", out_dir / "run_metadata.json")
    for slug, rel_path, title in QA_CHECKPOINTS:
        payload = qa_report_payload(slug, title, rel_path)
        (qa_dir / f"{slug}.qa_report.json").write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    manifest = out_dir / "datapackage.yaml"
    manifest.write_text(yaml.safe_dump(descriptor, sort_keys=False), encoding="utf-8")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=Path("results"))
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("results/workflow-runs") / RUN_NAME,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = write_package(results=args.results, out_dir=args.out_dir)
    print(f"Wrote {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
