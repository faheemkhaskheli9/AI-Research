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

    def test_accepts_official_proceedings_hosts(self):
        from copy import deepcopy
        exemplar = {
            "id": "legit", "title": "Example", "year": 2026,
            "status": "peer_reviewed", "topics": ["multimodal"],
            "url": "https://aclanthology.org/2026.emnlp-main.767/",
            "summary": "Benchmark", "open_question": "Why?",
            "reviewed_on": "2026-11-18",
        }
        for host in ("aclanthology.org", "openaccess.thecvf.com", "proceedings.colm.cc"):
            with self.subTest(host=host):
                entry = deepcopy(exemplar)
                entry["url"] = "https://" + host + "/some/paper"
                self.assertEqual(validate([entry]), [])

    def test_rejects_lookalike_hosts(self):
        exemplar = {
            "id": "spoof", "title": "Example", "year": 2026,
            "status": "peer_reviewed", "topics": ["multimodal"],
            "url": "https://aclanthology.org.evil.example/paper",
            "summary": "Benchmark", "open_question": "Why?",
            "reviewed_on": "2026-11-18",
        }
        self.assertTrue(any("source URL" in error for error in validate([exemplar])))


if __name__ == "__main__":
    unittest.main()
