from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from emit_clean_base_datapackages import (
    CLEAN_BASE_PACKAGES,
    build_datapackage,
    write_all_datapackages,
)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _populate_clean_base(root: Path) -> Path:
    processed = root / "data/processed"
    for package in CLEAN_BASE_PACKAGES.values():
        for resource in package.resources:
            _write(processed / package.directory / resource.path, f"{resource.path}\n")
    return processed


class CleanBaseDatapackageTest(unittest.TestCase):
    def test_gse14577_manifest_records_only_local_clean_base_resources(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed = _populate_clean_base(Path(td))

            descriptor = build_datapackage(CLEAN_BASE_PACKAGES["gse14577"], processed=processed)

        paths = {resource["path"] for resource in descriptor["resources"]}
        self.assertEqual(
            paths,
            {
                "expr.gene.tsv.gz",
                "sample_metadata.tsv",
                "cohort_audit.json",
                "clean.qa.pass",
            },
        )
        self.assertEqual(descriptor["profile"], "data-package")
        self.assertEqual(descriptor["name"], "gse14577-pi-cfs-prepared-gene-matrix")
        self.assertTrue(all("/" not in path for path in paths))
        self.assertTrue(all(resource["hash"].startswith("sha256:") for resource in descriptor["resources"]))
        self.assertTrue(all(resource["bytes"] > 0 for resource in descriptor["resources"]))
        self.assertIn("data/processed/datapackage.json", {source["path"] for source in descriptor["sources"]})

    def test_geneset_manifest_records_pinned_mapped_universe(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed = _populate_clean_base(Path(td))

            descriptor = build_datapackage(CLEAN_BASE_PACKAGES["genesets"], processed=processed)

        paths = {resource["path"] for resource in descriptor["resources"]}
        self.assertEqual(
            paths,
            {
                "hallmark.rds",
                "reactome.rds",
                "gobp.rds",
                "members.tsv",
                "theme_map.tsv",
                "theme_spec.json",
                "msigdb_release_hash.txt",
                "clean.qa.pass",
            },
        )
        self.assertEqual(descriptor["name"], "msigdb-2024-1-hs-mapped-pais-gene-set-universe")
        self.assertTrue(all(resource["group"] == "genesets" for resource in descriptor["resources"]))
        resources_by_path = {resource["path"]: resource for resource in descriptor["resources"]}
        self.assertEqual(resources_by_path["members.tsv"]["name"], "members-tsv")
        self.assertEqual(resources_by_path["members.tsv"]["profile"], "tabular-data-resource")
        self.assertEqual(resources_by_path["members.tsv"]["schema"]["fields"][0]["name"], "set_key")
        self.assertEqual(resources_by_path["members.tsv"]["schema"]["primaryKey"], "set_key")

    def test_missing_resource_fails_early(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed = _populate_clean_base(Path(td))
            (processed / "GSE130353/sample_sheet.tsv").unlink()

            with self.assertRaisesRegex(FileNotFoundError, "sample_sheet.tsv"):
                build_datapackage(CLEAN_BASE_PACKAGES["gse130353"], processed=processed)

    def test_write_all_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            processed = _populate_clean_base(Path(td))

            write_all_datapackages(processed=processed)
            first = {
                key: (processed / package.directory / "datapackage.json").read_text(encoding="utf-8")
                for key, package in CLEAN_BASE_PACKAGES.items()
            }
            write_all_datapackages(processed=processed)
            second = {
                key: (processed / package.directory / "datapackage.json").read_text(encoding="utf-8")
                for key, package in CLEAN_BASE_PACKAGES.items()
            }

        self.assertEqual(first, second)
        for payload in second.values():
            json.loads(payload)


if __name__ == "__main__":
    unittest.main()
