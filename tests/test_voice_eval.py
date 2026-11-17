import unittest

from experiments.voice_eval.judge_agreement import bootstrap_ci, cohen_kappa, percent_agreement
from experiments.voice_eval.metrics import cer, corpus_wer, edit_distance, normalize, wer
from experiments.voice_eval.run_demo import DEFAULT_DATA, load, summarize


class TestNormalize(unittest.TestCase):
    def test_urdu_yeh_and_kaf_unified(self):
        self.assertEqual(normalize("كيا", "ur"), normalize("کیا", "ur"))

    def test_sindhi_yeh_preserved(self):
        self.assertIn("ي", normalize("چاهيان", "sd"))

    def test_digits_and_punctuation(self):
        self.assertEqual(normalize("نمبر ۴۵۲ ہے۔", "ur"), "نمبر 452 ہے")

    def test_diacritics_removed(self):
        self.assertEqual(normalize("مُحَمَّد", "ur"), "محمد")

    def test_english_case_and_punct(self):
        self.assertEqual(normalize("Where is my Order?", "en"), "where is my order")

    def test_unknown_lang(self):
        with self.assertRaises(ValueError):
            normalize("x", "fr")


class TestErrorRates(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)

    def test_wer_identical(self):
        self.assertEqual(wer("میرا آرڈر", "میرا آرڈر", "ur"), 0.0)

    def test_wer_one_deletion(self):
        self.assertAlmostEqual(wer("a b c d", "a b d", "en"), 0.25)

    def test_cer(self):
        self.assertAlmostEqual(cer("abcd", "abed", "en"), 0.25)

    def test_corpus_wer(self):
        self.assertAlmostEqual(corpus_wer([("a b", "a b"), ("c d", "c")], "en"), 0.25)

    def test_empty_reference(self):
        self.assertEqual(wer("", "", "en"), 0.0)
        self.assertEqual(wer("", "x", "en"), 1.0)


class TestAgreement(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(cohen_kappa(["p", "f"], ["p", "f"]), 1.0)

    def test_known_value(self):
        a = ["p"] * 20 + ["f"] * 5 + ["p"] * 10 + ["f"] * 15
        b = ["p"] * 20 + ["p"] * 5 + ["f"] * 10 + ["f"] * 15
        self.assertAlmostEqual(cohen_kappa(a, b), 0.4)

    def test_percent(self):
        self.assertEqual(percent_agreement([1, 2, 3, 4], [1, 2, 0, 0]), 0.5)

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            cohen_kappa([1], [1, 2])

    def test_bootstrap_bounds(self):
        a = ["p", "f"] * 20
        lo, hi = bootstrap_ci(a, a, percent_agreement, n_resamples=200)
        self.assertEqual((lo, hi), (1.0, 1.0))


class TestDemo(unittest.TestCase):
    def test_sample_runs(self):
        results = summarize(load(DEFAULT_DATA))
        self.assertEqual(set(results), {"ur", "sd", "ur-latn", "en"})
        self.assertEqual(sum(r["n"] for r in results.values()), 12)


class TestDocReferences(unittest.TestCase):
    def test_voice_track_ids_exist_in_catalog(self):
        import json
        import re
        from pathlib import Path
        root = Path(__file__).resolve().parent.parent
        ids = {p["id"] for p in json.loads((root / "papers" / "catalog.json").read_text(encoding="utf-8"))}
        docs = ["research/AI_RESEARCH_AREAS.md", "research/VOICE_AGENTS_STRATEGY.md",
                "knowledge/datasets.md", "papers/READING_GUIDE.md",
                "research/MULTIMODAL_TEMPORAL_STRATEGY.md",
                "knowledge/multimodal_temporal_literature_review.md"]
        for doc in docs:
            refs = set(re.findall(r"`([a-z]+\d{2}[a-z0-9]*)`", (root / doc).read_text(encoding="utf-8")))
            self.assertFalse(refs - ids, f"{doc} references unknown ids: {sorted(refs - ids)}")


if __name__ == "__main__":
    unittest.main()
