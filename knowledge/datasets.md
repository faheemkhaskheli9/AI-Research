# Datasets

Check each dataset's license and current version before use.

| Dataset | Languages relevant here | Use | Reference |
|---|---|---|---|
| Common Voice (Mozilla) | Urdu (and growing) | ASR training/eval | `ardila19commonvoice` |
| FLEURS (Google) | Urdu (`ur_pk`), parallel across 102 languages | ASR eval, cross-lingual comparison | `conneau22fleurs` |
| MMS data/models (Meta) | Urdu, Sindhi and 1,000+ languages | ASR/TTS/LID baselines | `pratap23mms` |
| τ-bench | English | Agent reliability design template | `yao24taubench` |

## Gaps (research opportunities)

- No public **Sindhi voice-agent** task benchmark.
- Little public **Urdu–English code-switched** conversational speech with task labels.
- No public **Urdu LLM-judge vs. human agreement** dataset.
- No public **Urdu medical-triage** spoken evaluation set.

## Planned dataset (this repo)

**Name (working):** UrSi-VoiceBench
- Scripted customer-support and health-information tasks
- Urdu, Sindhi, Urdu–English code-switched, Roman Urdu
- Consenting speakers only; no personal data
- Labels: transcript, intent, entities, expected tool call, task success
- License: decide before release (e.g. CC BY 4.0)
