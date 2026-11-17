"""Paper metadata validator regression tests."""
import unittest

from scripts.validate_catalog import validate


class CatalogTests(unittest.TestCase):
    def test_rejects_missing_fields(self):
        self.assertTrue(validate([{"id": "bad"}]))

    def test_rejects_duplicate_and_nonprimary_urls(self):
        paper = {
            "id": "example", "title": "Example", "year": 2025,
            "status": "preprint", "topics": ["agents"],
            "url": "https://example.com/spurious-paper",
            "summary": "Summary", "open_question": "How?",
            "reviewed_on": "2026-11-18",
        }
        errors = validate([paper, paper.copy()])
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("source URL" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
