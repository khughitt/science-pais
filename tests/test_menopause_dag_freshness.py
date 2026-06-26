import pathlib
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code" / "menopause_dag" / "check_adjustment_sets_fresh.py"
EXPECTED = ROOT / "code" / "menopause_dag" / "adjustment_sets_v2.txt"


class MenopauseDAGFreshnessTest(unittest.TestCase):
    def test_committed_adjustment_sets_are_fresh(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHECKER), "--expected", str(EXPECTED)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("fresh", result.stdout)

    def test_stale_adjustment_sets_fail_with_diff(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            stale = pathlib.Path(tmpdir) / "adjustment_sets_v2.txt"
            stale.write_text("stale adjustment output\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(CHECKER), "--expected", str(stale)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale", result.stderr)
        self.assertIn("--- expected", result.stderr)
        self.assertIn("+++ derived", result.stderr)


if __name__ == "__main__":
    unittest.main()
