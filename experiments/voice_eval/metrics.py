"""Language-aware text normalization and WER/CER for Urdu, Sindhi, Roman Urdu and English."""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable, Sequence, Tuple

NORMALIZER_VERSION = "1.0"

# Arabic diacritics (harakat), superscript alef, and tatweel.
_DIACRITICS = re.compile(r"[ً-ٰٟـ]")
# Punctuation: ASCII plus Arabic/Urdu comma, semicolon, question mark, full stop.
_PUNCT = re.compile(r"[!-/:-@\[-`{-~،؛؟۔٪-٭‘-‟]")
_SPACES = re.compile(r"\s+")

# Extended Arabic-Indic (U+06F0..) and Arabic-Indic (U+0660..) digits -> ASCII.
_DIGITS = {**{chr(0x06F0 + i): str(i) for i in range(10)},
           **{chr(0x0660 + i): str(i) for i in range(10)}}

# Urdu-only letter unification. Not applied to Sindhi, where U+064A is the standard yeh.
_URDU_LETTERS = {
    "ي": "ی",  # Arabic yeh -> Farsi/Urdu yeh
    "ى": "ی",  # alef maksura -> Urdu yeh
    "ك": "ک",  # Arabic kaf -> keheh
}

SUPPORTED_LANGS = {"ur", "sd", "ur-latn", "en"}


def normalize(text: str, lang: str) -> str:
    """Normalize text for scoring. `lang` is one of SUPPORTED_LANGS."""
    if lang not in SUPPORTED_LANGS:
        raise ValueError(f"unsupported lang {lang!r}; expected one of {sorted(SUPPORTED_LANGS)}")
    text = unicodedata.normalize("NFKC", text)
    text = _DIACRITICS.sub("", text)
    text = "".join(_DIGITS.get(ch, ch) for ch in text)
    if lang == "ur":
        text = "".join(_URDU_LETTERS.get(ch, ch) for ch in text)
    text = text.lower()
    text = _PUNCT.sub(" ", text)
    return _SPACES.sub(" ", text).strip()


def edit_distance(ref: Sequence, hyp: Sequence) -> int:
    """Levenshtein distance between two sequences."""
    prev = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        cur = [i] + [0] * len(hyp)
        for j, h in enumerate(hyp, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (r != h))
        prev = cur
    return prev[-1]


def _rate(errors: int, total: int) -> float:
    if total == 0:
        return 0.0 if errors == 0 else 1.0
    return errors / total


def wer(ref: str, hyp: str, lang: str) -> float:
    r, h = normalize(ref, lang).split(), normalize(hyp, lang).split()
    return _rate(edit_distance(r, h), len(r))


def cer(ref: str, hyp: str, lang: str) -> float:
    r = normalize(ref, lang).replace(" ", "")
    h = normalize(hyp, lang).replace(" ", "")
    return _rate(edit_distance(r, h), len(r))


def corpus_wer(pairs: Iterable[Tuple[str, str]], lang: str) -> float:
    """Corpus-level WER: total word errors / total reference words."""
    errors = total = 0
    for ref, hyp in pairs:
        r, h = normalize(ref, lang).split(), normalize(hyp, lang).split()
        errors += edit_distance(r, h)
        total += len(r)
    return _rate(errors, total)


def corpus_cer(pairs: Iterable[Tuple[str, str]], lang: str) -> float:
    errors = total = 0
    for ref, hyp in pairs:
        r = normalize(ref, lang).replace(" ", "")
        h = normalize(hyp, lang).replace(" ", "")
        errors += edit_distance(r, h)
        total += len(r)
    return _rate(errors, total)
