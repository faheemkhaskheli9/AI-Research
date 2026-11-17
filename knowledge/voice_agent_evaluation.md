# Evaluation Methodology

## Rules

1. **Fix the test set before running models.** Never tune on it.
2. **Normalize text the same way for every system** (see [low_resource_speech.md](low_resource_speech.md)). Report the normalizer version.
3. **Report uncertainty.** Use bootstrap confidence intervals for every metric on sets under ~10k items.
4. **Measure reliability, not just capability.** Run each agent task several times; report pass^k alongside average success.
5. **Validate judges against humans.** Before trusting an LLM judge in a new language, measure its agreement (Cohen's κ) with at least two human raters.
6. **Check judge biases:** swap answer order (position bias), vary length (verbosity bias), hide model names (self-preference).
7. **Break results down** by language, code-switching, speaker accent, and entity type (names, numbers, dates).
8. **Log everything:** model version, date, prompt, temperature, seed.

## Voice-agent metrics

| Level | Metric | Tool in this repo |
|---|---|---|
| Speech | WER, CER | `experiments/voice_eval/metrics.py` |
| Entities | Entity error rate (numbers, names, dates) | planned |
| Task | Task success, pass^k | planned |
| Judge | Judge–human κ, percent agreement | `experiments/voice_eval/judge_agreement.py` |
| Latency | Time to first audio, end-to-end turn latency | planned |
| Safety | Harmful-advice rate, escalation correctness | planned |

## Medical / high-stakes evaluation

- Use scripted scenarios only; never real patient data without approval.
- Score "unsafe answer" separately from "wrong answer". A refusal plus referral can be correct.
- Have a domain expert review the rubric.
