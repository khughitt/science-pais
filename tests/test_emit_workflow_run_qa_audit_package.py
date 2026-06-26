from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import yaml

from emit_workflow_run_qa_audit_package import build_package, write_package
from science_tool.qa_audit.audit import audit_workflows


QA_REPORTS = {
    "GSE14577_raw.qa_report.md": "# GSE14577 raw\n",
    "GSE130353_raw.qa_report.md": "# GSE130353 raw\n",
    "GSE14577_clean.qa_report.md": "# GSE14577 clean\n",
    "GSE130353_clean.qa_report.md": "# GSE130353 clean\n",
    "genesets_clean.qa_report.md": "# genesets clean\n",
    "t035_results.qa_report.md": "# t035 result QA\n",
}


def _populate_results(root: Path) -> Path:
    results = root / "results"
    (results / "qa").mkdir(parents=True)
    for name, text in QA_REPORTS.items():
        (results / "qa" / name).write_text(text, encoding="utf-8")
    (results / "qa/t035_results.qa.pass").write_text("PASS t035 result QA\n", encoding="utf-8")
    (results / "run_metadata.json").write_text(
        json.dumps(
            {
                "name": "t035-cross-trigger-pathway-overlap-verdict",
                "verdict": "null_nonarbitrating",
                "entities": [
                    "task:t035",
                    "pre-registration:0002-cross-trigger-pathway-overlap",
                    "plan:0003-cross-trigger-pathway-overlap-pipeline",
                    "question:0001-shared-molecular-signature-across-triggers",
                ],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return results


class WorkflowRunQAAuditPackageTest(unittest.TestCase):
    def test_manifest_uses_qa_audit_resource_contract(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            results = _populate_results(root)

            package = build_package(results=results)

        self.assertEqual(package["name"], "t035-cross-trigger-pathway-overlap-verdict")
        self.assertEqual(package["workflow"]["name"], "t035-cross-trigger-pathway-overlap")
        self.assertEqual(package["entities"]["tasks"], ["task:t035"])
        self.assertEqual(
            [resource["name"] for resource in package["resources"] if resource["name"].startswith("qa_report")],
            [
                "qa_report:gse14577_raw",
                "qa_report:gse130353_raw",
                "qa_report:gse14577_clean",
                "qa_report:gse130353_clean",
                "qa_report:genesets_clean",
                "qa_report:t035_results",
            ],
        )
        self.assertTrue(all(not resource["path"].startswith("results/") for resource in package["resources"]))

    def test_written_package_is_read_by_science_qa_audit(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            results = _populate_results(root)
            out_dir = results / "workflow-runs/t035-cross-trigger-pathway-overlap-verdict"
            manifest = out_dir / "datapackage.yaml"
            runs_dir = root / "entities/workflow-runs"
            runs_dir.mkdir(parents=True)

            write_package(results=results, out_dir=out_dir)
            (runs_dir / "t035-cross-trigger-pathway-overlap-verdict.md").write_text(
                "\n".join(
                    [
                        "---",
                        'id: "workflow-run:t035-cross-trigger-pathway-overlap-verdict"',
                        'type: "workflow-run"',
                        'workflow: "t035-cross-trigger-pathway-overlap"',
                        f'manifest_path: "{manifest.relative_to(root).as_posix()}"',
                        "---",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            manifest_obj = yaml.safe_load(manifest.read_text(encoding="utf-8"))
            rows = audit_workflows(runs_dir=runs_dir, repo_root=root)
            qa_json_exists = (out_dir / "qa/gse14577_raw.qa_report.json").exists()

        self.assertTrue(qa_json_exists)
        self.assertEqual(manifest_obj["resources"][0]["name"], "run_metadata")
        self.assertEqual(rows[0]["workflow"], "t035-cross-trigger-pathway-overlap")
        self.assertEqual(rows[0]["engagement"], "NO-FLAGS")
        self.assertEqual(rows[0]["iteration"], "SINGLE-RUN")
        self.assertEqual(rows[0]["breadth"], "6/6")

    def test_missing_source_report_fails_early(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            results = _populate_results(root)
            (results / "qa/GSE14577_raw.qa_report.md").unlink()

            with self.assertRaisesRegex(FileNotFoundError, "GSE14577_raw.qa_report.md"):
                build_package(results=results)


if __name__ == "__main__":
    unittest.main()
