"""Demo: per-language WER/CER and judge-human agreement on a small toy file.

The bundled sample is illustrative only (hand-written examples, not real model output).

Usage:
    python -m experiments.voice_eval.run_demo
    python -m experiments.voice_eval.run_demo --data path/to/file.jsonl
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from .judge_agreement import cohen_kappa, percent_agreement
from .metrics import NORMALIZER_VERSION, corpus_cer, corpus_wer

DEFAULT_DATA = Path(__file__).with_name("sample_data.jsonl")


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def summarize(rows):
    by_lang = defaultdict(list)
    for row in rows:
        by_lang[row["lang"]].append(row)
    results = {}
    for lang, items in sorted(by_lang.items()):
        pairs = [(r["reference"], r["hypothesis"]) for r in items]
        human = [r["human_label"] for r in items]
        judge = [r["judge_label"] for r in items]
        results[lang] = {
            "n": len(items),
            "wer": round(corpus_wer(pairs, lang), 4),
            "cer": round(corpus_cer(pairs, lang), 4),
            "judge_agreement": round(percent_agreement(human, judge), 4),
            "judge_kappa": round(cohen_kappa(human, judge), 4),
        }
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args(argv)
    results = summarize(load(args.data))
    print(json.dumps({"normalizer_version": NORMALIZER_VERSION, "results": results},
                     ensure_ascii=False, indent=2))
    return results


if __name__ == "__main__":
    main()
