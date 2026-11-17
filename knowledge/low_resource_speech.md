# Low-Resource Speech: Urdu and Sindhi

## Script pitfalls

Urdu and Sindhi use Perso-Arabic scripts. The same visible letter can have different Unicode code points, which silently inflates WER.

| Issue | Urdu | Sindhi |
|---|---|---|
| Yeh | Standard is `ی` (U+06CC); Arabic `ي` (U+064A) often appears in model output | Standard is `ي` (U+064A) — **do not** map it to U+06CC |
| Kaf | Standard is `ک` (U+06A9); Arabic `ك` (U+0643) often appears | Uses `ڪ` (U+06AA) and `ک` (U+06A9) as different letters |
| Diacritics (zer, zabar, pesh) | Usually omitted in writing; strip before scoring | Same |
| Full stop | `۔` (U+06D4) | `.` and `۔` both seen |
| Digits | `۰–۹` (U+06F0–U+06F9) and ASCII digits both used | Same |

**Rule:** normalization must be **language-aware**. A normalizer built for Urdu can corrupt Sindhi text.

## Spelling variants

Many Urdu words have accepted variants, for example `چاہیے` / `چاہئے`. Decide whether to:
- count them as errors (strict), or
- map them through a variant dictionary (lenient) — and report which one you used.

## Code-switching

- **Script-mixed:** Urdu script with English words in Latin (`میرا order`).
- **Transliterated:** English words written in Urdu script (`آرڈر`).
- **Roman Urdu:** everything in Latin script (`mera order cancel kar dein`). No standard spelling, so CER is often fairer than WER.

Report results separately for monolingual and code-switched utterances.

## Practical checklist

- [ ] Normalize Unicode (NFKC) and language-specific characters
- [ ] Strip diacritics and tatweel (`ـ`)
- [ ] Map digits to one system
- [ ] Remove punctuation consistently
- [ ] Report both WER and CER
- [ ] Split results by code-switching type
