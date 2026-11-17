# Research Track: Multilingual Voice Agents

A second focus track alongside [STRATEGY.md](STRATEGY.md) (lifelong learning for agents). Both share the same evaluation discipline.

## Focus

**Reliable multilingual voice agents for low-resource languages (Urdu and Sindhi).**

Big labs optimize for English and other high-resource languages. Urdu (~230M speakers) and Sindhi (~30M speakers) have little public evaluation data for spoken agents, almost none for code-switched speech, and no standard benchmark for end-to-end voice-agent reliability. That gap is the opportunity.

## Why this focus fits

| Existing experience | How it transfers |
|---|---|
| Multilingual customer-support call bots (text, voice notes, real-time calls) | Domain knowledge of real failure modes |
| Real-time medical voice chatbot (OpenAI Realtime) | Voice-agent pipeline + high-stakes domain |
| LLM-as-a-Judge evaluation in production | Core evaluation method |
| RAG, tool calling, agent frameworks | Can build the systems under test |
| Native Urdu, Sindhi, English | Annotation quality, error analysis, data collection |

## Research questions

1. **RQ1 — Benchmark.** How well do current speech and voice-agent systems perform on Urdu, Sindhi, and Urdu–English code-switched tasks?
2. **RQ2 — Judge reliability.** Does LLM-as-a-Judge agree with human raters as well in Urdu/Sindhi as in English?
3. **RQ3 — Error propagation.** How much do ASR errors degrade downstream task success in a voice agent?
4. **RQ4 — Safety.** Can retrieval grounding and uncertainty signals reduce harmful errors in Urdu medical triage?

## Hypotheses (falsifiable)

- **H1:** Judge–human agreement (Cohen's κ) is lower for Urdu than for English on the same tasks.
- **H2:** Script normalization (Arabic vs. Urdu code points) changes reported WER materially; unnormalized results are not comparable.
- **H3:** Code-switched utterances have higher WER than monolingual ones for all tested ASR systems.
- **H4:** Task success correlates more strongly with entity-level errors (names, numbers, dates) than with overall WER.

## Milestones

| Month | Milestone | Output |
|---|---|---|
| 1–2 | Read core papers; reproduce WER on FLEURS/Common Voice Urdu | Reading notes, baseline numbers |
| 3 | Design task schema; collect pilot set (~200 utterances, consented) | Dataset card, annotation guide |
| 4 | Benchmark ASR + realtime voice models | Results table |
| 5 | Judge-vs-human agreement study (RQ2) | Workshop paper draft |
| 6 | Submit to ACL/EMNLP workshop or Interspeech | Submission |
| 7–9 | Scale dataset; add Sindhi; code-switching analysis (RQ3) | Public Hugging Face dataset v1 |
| 10–12 | Medical-triage safety study (RQ4) | Main-conference paper draft |

## Adversarial review (what could go wrong)

- **"Just another dataset."** Mitigation: pair the dataset with a finding (H1/H4), not only numbers.
- **Data consent and privacy.** Mitigation: scripted prompts read by consenting speakers; no real patient data.
- **Model churn.** Mitigation: release the harness, so new models can be re-scored cheaply.
- **Small sample sizes.** Mitigation: report bootstrap confidence intervals; pre-register metrics.
- **Annotator bias (single annotator).** Mitigation: at least two raters per item; report inter-rater agreement.

## Publication venues

- Workshops: ACL/EMNLP/NAACL workshops on low-resource languages, evaluation, and speech.
- Conferences: Interspeech, ICASSP, ACL, EMNLP.
- Datasets/benchmarks track: NeurIPS Datasets & Benchmarks.
