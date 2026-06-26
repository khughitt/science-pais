# science:code
# status: exploratory
# task_ids: [t035, t065, t069]
# science:end

#!/usr/bin/env python3
"""Emit datapackage descriptors for t035 reusable clean-base substrates."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True, slots=True)
class ResourceSpec:
    path: str
    title: str
    mediatype: str
    profile: str | None = None
    schema: dict[str, object] | None = None


@dataclass(frozen=True, slots=True)
class PackageSpec:
    key: str
    name: str
    title: str
    description: str
    directory: str
    group: str
    related_entities: tuple[str, ...]
    resources: tuple[ResourceSpec, ...]


def _resource(
    path: str,
    title: str,
    mediatype: str,
    *,
    profile: str | None = None,
    schema: dict[str, object] | None = None,
) -> ResourceSpec:
    return ResourceSpec(path=path, title=title, mediatype=mediatype, profile=profile, schema=schema)


GENESET_MEMBERS_SCHEMA: dict[str, object] = {
    "fields": [
        {"name": "set_key", "type": "string"},
        {"name": "name", "type": "string"},
        {"name": "member_ids", "type": "string"},
        {"name": "db", "type": "string"},
        {"name": "theme", "type": "string"},
        {"name": "size", "type": "integer"},
    ],
    "primaryKey": "set_key",
}


CLEAN_BASE_PACKAGES: dict[str, PackageSpec] = {
    "gse14577": PackageSpec(
        key="gse14577",
        name="gse14577-pi-cfs-prepared-gene-matrix",
        title="GSE14577 prepared PI-CFS gene-expression clean base",
        description=(
            "Reusable t035 clean-base substrate for the GSE14577 PI-CFS PBMC "
            "microarray cohort: patient-level Ensembl gene matrix, sample "
            "metadata, cohort audit, and clean-base QA sentinel."
        ),
        directory="GSE14577",
        group="gse14577",
        related_entities=(
            "task:t035",
            "task:t065",
            "task:t069",
            "pre-registration:0002-cross-trigger-pathway-overlap",
            "plan:0003-cross-trigger-pathway-overlap-pipeline",
            "question:0001-shared-molecular-signature-across-triggers",
        ),
        resources=(
            _resource("expr.gene.tsv.gz", "Patient-level Ensembl gene expression matrix", "application/gzip"),
            _resource("sample_metadata.tsv", "Patient/chip sample metadata", "text/tab-separated-values"),
            _resource("cohort_audit.json", "Preparation cohort audit", "application/json"),
            _resource("clean.qa.pass", "Clean-base QA sentinel", "text/plain"),
        ),
    ),
    "gse130353": PackageSpec(
        key="gse130353",
        name="gse130353-qfs-cfs-prepared-gene-matrix",
        title="GSE130353 prepared QFS/CFS monocyte gene-expression clean base",
        description=(
            "Reusable t035 clean-base substrate for the GSE130353 QFS/CFS "
            "monocyte RNA-seq cohort: filtered Ensembl log_mu gene matrix, "
            "sample sheet, cohort audit, and clean-base QA sentinel."
        ),
        directory="GSE130353",
        group="gse130353",
        related_entities=(
            "task:t035",
            "task:t065",
            "pre-registration:0002-cross-trigger-pathway-overlap",
            "plan:0003-cross-trigger-pathway-overlap-pipeline",
            "question:0001-shared-molecular-signature-across-triggers",
            "dataset:gse130353-qfs-cfs-monocytes",
        ),
        resources=(
            _resource("expr.gene.tsv.gz", "Filtered Ensembl log_mu gene expression matrix", "application/gzip"),
            _resource("sample_sheet.tsv", "Authoritative subject-status sample sheet", "text/tab-separated-values"),
            _resource("cohort_audit.json", "Near-zero filter and cohort audit", "application/json"),
            _resource("nearzero.qa.pass", "Near-zero bimodality QA sentinel", "text/plain"),
            _resource("clean.qa.pass", "Clean-base QA sentinel", "text/plain"),
        ),
    ),
    "genesets": PackageSpec(
        key="genesets",
        name="msigdb-2024-1-hs-mapped-pais-gene-set-universe",
        title="MSigDB 2024.1.Hs mapped PAIS gene-set universe",
        description=(
            "Pinned t035 gene-set clean base: MSigDB 2024.1.Hs Hallmark, "
            "Reactome, and GO:BP collections mapped to Ensembl, size-filtered, "
            "and assigned to the locked PAIS theme map."
        ),
        directory="genesets",
        group="genesets",
        related_entities=(
            "task:t035",
            "task:t065",
            "pre-registration:0002-cross-trigger-pathway-overlap",
            "plan:0003-cross-trigger-pathway-overlap-pipeline",
            "question:0001-shared-molecular-signature-across-triggers",
        ),
        resources=(
            _resource("hallmark.rds", "Mapped Hallmark gene sets", "application/octet-stream"),
            _resource("reactome.rds", "Mapped Reactome gene sets", "application/octet-stream"),
            _resource("gobp.rds", "Mapped GO:BP gene sets", "application/octet-stream"),
            _resource(
                "members.tsv",
                "Normalized bio.geneset member table",
                "text/tab-separated-values",
                profile="tabular-data-resource",
                schema=GENESET_MEMBERS_SCHEMA,
            ),
            _resource("theme_map.tsv", "Locked per-set PAIS theme assignments", "text/tab-separated-values"),
            _resource("theme_spec.json", "Serialized locked theme-map configuration", "application/json"),
            _resource("msigdb_release_hash.txt", "Pinned MSigDB release hash", "text/plain"),
            _resource("clean.qa.pass", "Gene-set clean-base QA sentinel", "text/plain"),
        ),
    ),
}


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resource_for(resource: ResourceSpec, *, package_dir: Path, group: str) -> dict[str, object]:
    abs_path = package_dir / resource.path
    if not abs_path.exists():
        raise FileNotFoundError(f"missing clean-base resource: {abs_path}")
    descriptor = {
        "name": resource.path.replace(".", "-").replace("_", "-").lower(),
        "path": resource.path,
        "title": resource.title,
        "bytes": abs_path.stat().st_size,
        "hash": "sha256:" + sha256_path(abs_path),
        "mediatype": resource.mediatype,
        "group": group,
    }
    if resource.profile is not None:
        descriptor["profile"] = resource.profile
    if resource.schema is not None:
        descriptor["schema"] = resource.schema
    return descriptor


def build_datapackage(spec: PackageSpec, *, processed: Path) -> dict[str, object]:
    package_dir = processed / spec.directory
    resources = [resource_for(resource, package_dir=package_dir, group=spec.group) for resource in spec.resources]
    return {
        "name": spec.name,
        "title": spec.title,
        "description": spec.description,
        "profile": "data-package",
        "sources": [
            {
                "title": "input acquisition datapackage",
                "path": "data/processed/datapackage.json",
            },
            {
                "title": "pre-registration:0002-cross-trigger-pathway-overlap",
                "path": "entities/pre-registrations/0002-cross-trigger-pathway-overlap.md",
            },
            {
                "title": "plan:0003-cross-trigger-pathway-overlap-pipeline",
                "path": "entities/plans/0003-cross-trigger-pathway-overlap-pipeline.md",
            },
        ],
        "resources": resources,
        "pais": {
            "entities": list(spec.related_entities),
            "clean_base": True,
        },
    }


def write_datapackage(spec: PackageSpec, *, processed: Path) -> Path:
    descriptor = build_datapackage(spec, processed=processed)
    out = processed / spec.directory / "datapackage.json"
    out.write_text(
        json.dumps(descriptor, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return out


def write_all_datapackages(*, processed: Path, keys: Iterable[str] | None = None) -> list[Path]:
    selected = CLEAN_BASE_PACKAGES.keys() if keys is None else keys
    return [write_datapackage(CLEAN_BASE_PACKAGES[key], processed=processed) for key in selected]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--processed", required=True, type=Path)
    parser.add_argument("--package", choices=sorted(CLEAN_BASE_PACKAGES), action="append")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    written = write_all_datapackages(processed=args.processed, keys=args.package)
    for path in written:
        print(f"[emit_clean_base_datapackages] wrote {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
