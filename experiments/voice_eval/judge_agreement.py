"""Agreement between an LLM judge and human raters, with bootstrap confidence intervals."""

from __future__ import annotations

import random
from collections import Counter
from typing import Callable, List, Sequence, Tuple


def percent_agreement(a: Sequence, b: Sequence) -> float:
    if len(a) != len(b):
        raise ValueError("label lists must have equal length")
    if not a:
        return 0.0
    return sum(x == y for x, y in zip(a, b)) / len(a)


def cohen_kappa(a: Sequence, b: Sequence) -> float:
    """Cohen's kappa for two raters over categorical labels."""
    if len(a) != len(b):
        raise ValueError("label lists must have equal length")
    n = len(a)
    if n == 0:
        return 0.0
    po = percent_agreement(a, b)
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    if pe == 1.0:
        return 1.0 if po == 1.0 else 0.0
    return (po - pe) / (1 - pe)


def bootstrap_ci(a: Sequence, b: Sequence, stat: Callable[[Sequence, Sequence], float],
                 n_resamples: int = 1000, alpha: float = 0.05, seed: int = 0) -> Tuple[float, float]:
    """Percentile bootstrap CI for a paired statistic."""
    rng = random.Random(seed)
    n = len(a)
    if n == 0:
        return (0.0, 0.0)
    values: List[float] = []
    for _ in range(n_resamples):
        idx = [rng.randrange(n) for _ in range(n)]
        values.append(stat([a[i] for i in idx], [b[i] for i in idx]))
    values.sort()
    lo = values[int((alpha / 2) * n_resamples)]
    hi = values[min(n_resamples - 1, int((1 - alpha / 2) * n_resamples))]
    return (lo, hi)
