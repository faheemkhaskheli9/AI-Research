"""Regression tests for the research frontier inventory."""
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_frontiers import validate_frontiers


class FrontierTests(unittest.TestCase):
    def test_rejects_wrong_number_of_frontiers(self):
        self.assertTrue(validate_frontiers([], set(), Path(".")))

    def test_rejects_missing_review_file(self):
        records = [
            {"id": f"{i:02d}", "slug": f"{i:02d}-topic",
             "review_path": f"research/areas/{i:02d}-topic.md",
             "key_paper_ids": ["a", "b", "c"],
             "experiment_status": "proposed_not_executed"}
            for i in range(1, 13)
        ]
        with tempfile.TemporaryDirectory() as temp:
            errors = validate_frontiers(records, {"a", "b", "c"}, Path(temp))
        self.assertTrue(any("review missing" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
