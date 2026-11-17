# AI Research Areas — Overview

A beginner-friendly overview of twelve major AI research directions, each with its core question, open problems, and entry papers (IDs refer to [`papers/catalog.json`](../papers/catalog.json)).

| # | Direction | Core question | Competition level |
|---|-----------|---------------|-------------------|
| 1 | Foundations & scaling | How do capability, data, and compute relate? | Very high (big labs) |
| 2 | Architectures | What comes after (or alongside) the transformer? | High |
| 3 | Alignment & post-training | How do we make models follow human intent? | High |
| 4 | Reasoning & planning | How do models solve multi-step problems reliably? | Very high |
| 5 | AI agents & tool use | How do models act in environments over long horizons? | High |
| 6 | Memory & lifelong learning | How do agents learn continuously without forgetting? | Medium |
| 7 | Retrieval & grounding | How do models stay factual and up to date? | Medium |
| 8 | Evaluation & LLM-as-a-Judge | How do we measure what models can actually do? | Medium |
| 9 | Speech & spoken dialogue | How do models listen and talk in real time? | Medium |
| 10 | Multilingual & low-resource AI | How do we serve the world's ~7,000 languages? | **Low** |
| 11 | Efficiency | How do we make models smaller, faster, cheaper? | High |
| 12 | Applied AI (health, science) | How do we deploy AI safely in high-stakes domains? | Medium |

---

## 1. Foundations & scaling
- **Open problems:** data quality vs. quantity; scaling of test-time compute; predicting emergent abilities.
- **Entry papers:** `kaplan20scaling`, `hoffmann22chinchilla`.

## 2. Architectures
- **Open problems:** long-context efficiency; state-space and hybrid models; mixture-of-experts routing.
- **Entry papers:** `vaswani17attention`, `gu23mamba`.

## 3. Alignment & post-training
- **Open problems:** reward hacking; scalable oversight; preference data in non-English languages.
- **Entry papers:** `ouyang22instructgpt`, `rafailov23dpo`, `bai22constitutional`.

## 4. Reasoning & planning
- **Open problems:** faithfulness of reasoning traces; verification; reasoning in low-resource languages.
- **Entry papers:** `wei22cot`, `cobbe21gsm8k`.

## 5. AI agents & tool use
- **Open problems:** reliability across repeated trials; rule following; recovering from tool errors.
- **Entry papers:** `yao22react`, `schick23toolformer`, `yao24taubench`, `jimenez23swebench`.

## 6. Memory & lifelong learning
- **Open problems:** what to store vs. forget; stale-fact updates; memory consolidation; evaluation of memory.
- **Entry papers:** `park23generative`, `packer23memgpt`, `shinn23reflexion`, `wang23voyager`.
- **Code:** [`experiments/continual_memory`](../experiments/continual_memory).

## 7. Retrieval & grounding
- **Open problems:** cross-lingual retrieval; position bias in long context; citation faithfulness.
- **Entry papers:** `lewis20rag`, `asai23selfrag`, `liu23lost`.

## 8. Evaluation & LLM-as-a-Judge
- **Open problems:** judge bias (position, verbosity, self-preference); judge reliability outside English; contamination.
- **Entry papers:** `zheng23judge`, `liu23geval`, `wang23fair`.

## 9. Speech & spoken dialogue
- **Open problems:** full-duplex turn-taking; latency vs. quality; evaluating spoken agents end-to-end.
- **Entry papers:** `radford22whisper`, `defossez24moshi`, `seamless23m4t`.

## 10. Multilingual & low-resource AI
- **Open problems:** code-switching (e.g. Urdu–English, Roman Urdu); script normalization; scarce evaluation data.
- **Entry papers:** `ardila19commonvoice`, `conneau22fleurs`, `pratap23mms`, `babu21xlsr`.

## 11. Efficiency
- **Open problems:** quantization quality loss in low-resource languages; distillation for on-device speech.
- **Entry papers:** `hu21lora`.

## 12. Applied AI (health, science)
- **Open problems:** safe triage; hallucination detection; human oversight in clinical workflows.
- **Entry papers:** see [`knowledge/voice_agent_evaluation.md`](../knowledge/voice_agent_evaluation.md) for safety-oriented evaluation.

---

**Focus tracks in this repo:**
- Memory and lifelong agents (6, 5) — [STRATEGY.md](STRATEGY.md)
- Multilingual voice agents (5, 8, 9, 10) — [VOICE_AGENTS_STRATEGY.md](VOICE_AGENTS_STRATEGY.md)
