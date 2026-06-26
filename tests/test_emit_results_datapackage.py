from __future__ import annotations

import gzip
import json
import tempfile
import unittest
from pathlib import Path

from emit_results_datapackage import build_datapackage, expected_result_paths, write_datapackage
from tests.test_qa_results import CONFIG, _populate_bundle


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_gzip(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        fh.write(text)


def _populate_manifest_extras(root: Path) -> tuple[Path, Path]:
    processed, results = _populate_bundle(root)

    for dataset in ("GSE14577", "GSE130353"):
        _write_text(results / "qa" / f"{dataset}_raw.qa_report.md", f"# {dataset} raw QA\n")
        _write_text(results / "qa" / f"{dataset}_clean.qa_report.md", f"# {dataset} clean QA\n")
    _write_text(results / "qa/genesets_clean.qa_report.md", "# genesets QA\n")
    _write_text(results / "qa/t035_results.qa_report.md", "# result QA\n")
    _write_text(results / "qa/t035_results.qa.pass", "PASS t035 result QA\n")

    _write_text(
        results / "run_metadata.json",
        json.dumps(
            {
                "name": "t035-cross-trigger-pathway-overlap-verdict",
                "verdict": "null_nonarbitrating",
                "entities": [
                    "task:t035",
                    "pre-registration:0002-cross-trigger-pathway-overlap",
                    "plan:0003-cross-trigger-pathway-overlap-pipeline",
                ],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )
    _write_text(
        results / "results.md",
        "# Synthetic result\n\nLocked decision 2026-06-21.\n",
    )

    _write_gzip(processed / "GSE14577/expr.gene.tsv.gz", "gene\tS1\nENSG000001\t1\n")
    _write_text(processed / "datapackage.json", "{}\n")
    return processed, results


class ResultsDatapackageTest(unittest.TestCase):
    def test_manifest_records_expected_results_and_excludes_clean_base_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            processed, results = _populate_manifest_extras(root)

            descriptor = build_datapackage(processed=processed, results=results, config=CONFIG)

        paths = {resource["path"] for resource in descriptor["resources"]}
        self.assertIn("results/verdict.json", paths)
        self.assertIn("results/results.md", paths)
        self.assertIn("results/run_metadata.json", paths)
        self.assertIn("results/qa/t035_results.qa.pass", paths)
        self.assertIn("data/processed/de/c1.ranked.tsv", paths)
        self.assertIn("data/processed/fgsea/c1.hallmark.nes.tsv", paths)
        self.assertIn("data/processed/concordance/primary.hallmark.scatter.tsv", paths)
        self.assertIn("data/processed/perm/primary.reactome.nulldist.tsv", paths)
        self.assertIn("data/processed/rollup/db_robustness.tsv", paths)
        self.assertNotIn("data/processed/GSE14577/expr.gene.tsv.gz", paths)
        self.assertNotIn("data/processed/datapackage.json", paths)

        self.assertEqual(descriptor["profile"], "data-package")
        self.assertEqual(descriptor["created"], "2026-06-21")
        self.assertEqual(descriptor["updated"], "2026-06-21")
        self.assertEqual(descriptor["pais"]["verdict"], "null_nonarbitrating")
        self.assertIn("task:t035", descriptor["pais"]["entities"])
        self.assertTrue(all(resource["hash"].startswith("sha256:") for resource in descriptor["resources"]))
        self.assertTrue(all(resource["bytes"] > 0 for resource in descriptor["resources"]))

    def test_missing_expected_result_fails_early(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            processed, results = _populate_manifest_extras(root)
            (processed / "perm/primary.reactome.nulldist.tsv").unlink()

            with self.assertRaisesRegex(FileNotFoundError, "primary.reactome.nulldist.tsv"):
                build_datapackage(processed=processed, results=results, config=CONFIG)

    def test_write_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            processed, results = _populate_manifest_extras(root)
            out = results / "datapackage.json"

            write_datapackage(processed=processed, results=results, config=CONFIG, out=out)
            first = out.read_text(encoding="utf-8")
            write_datapackage(processed=processed, results=results, config=CONFIG, out=out)
            second = out.read_text(encoding="utf-8")

        self.assertEqual(first, second)

    def test_expected_paths_do_not_include_raw_or_clean_base_artifacts(self) -> None:
        paths = {path.as_posix() for path in expected_result_paths(CONFIG)}

        self.assertNotIn("data/processed/datapackage.json", paths)
        self.assertFalse(any(path.startswith("data/processed/GSE14577/") for path in paths))
        self.assertFalse(any(path.startswith("data/processed/GSE130353/") for path in paths))


if __name__ == "__main__":
    unittest.main()
