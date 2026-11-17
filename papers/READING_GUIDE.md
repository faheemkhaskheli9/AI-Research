# How to read and reproduce AI research

The machine-readable [catalog](catalog.json) records individually linked primary sources. Each entry identifies its publication status; **arXiv preprints are not treated as peer-reviewed conference publications**. Citations are pointers to authors' work; this repository does not mirror PDF files, datasets, code licenses, or model weights.

## Reading sequence

**Phase 1 — foundations**
1. ReAct and Reflexion: distinguish action, feedback, and verbal reflection.
2. Generative Agents: understand episodic stores, retrieval, and reflection.
3. AgentBench and SWE-bench: learn how realistic environment tasks are assessed.

**Phase 2 — 2026 research**
4. Modular Memory: learn the ICL/IWL architectural hypothesis.
5. MemoryBench and CL-Bench: compare memory recall with genuine sequential improvement.
6. JitRL: investigate a no-gradient route to test-time adaptation.
7. Memory-Centric Continual Learning: study retention, adaptation, and transfer.
8. Outcome Rewards paper: separate final answer success from reasoning faithfulness.
9. OSWorld 2.0: consider long-horizon action sequences and checkpoints.

**Phase 3 — grounded learning**
10. DreamerV3: model-based reinforcement learning and imagined rollouts.
11. V-JEPA 2: video representation learning and planning.
12. RT-2: transfer into robot actions.

## Standard per-paper note

Use [paper note template](../knowledge/reading_notes/TEMPLATE.md). Extract: problem; train/eval setting; exact baselines; data leakage risks; compute budget; evidence; what was not demonstrated; code/reproducibility; and your falsifiable next experiment.

## Verification procedure

1. Open the original publisher, arXiv, or author-maintained project.
2. Confirm title, authors, year, venue, version, and code link.
3. Prefer publisher material when a publication exists; maintain the preprint link where valuable.
4. Mark source status honestly and save a `reviewed_on` date.
5. A claim about performance belongs to the paper's authors until independently reproduced.

Useful discovery channels: [PMLR](https://proceedings.mlr.press/), [OpenReview](https://openreview.net/), [arXiv](https://arxiv.org/), [NeurIPS](https://neurips.cc/), [Stanford AI Index](https://hai.stanford.edu/ai-index).

## Voice-agent track (Urdu / Sindhi)

See [voice-agent strategy](../research/VOICE_AGENTS_STRATEGY.md).

1. `radford22whisper` → `baevski20wav2vec2` → `babu21xlsr` — speech recognition foundations.
2. `ardila19commonvoice`, `conneau22fleurs` — datasets that include Urdu.
3. `pratap23mms`, `seamless23m4t` — massively multilingual speech.
4. `defossez24moshi` — real-time full-duplex spoken dialogue.
5. `zheng23judge` → `wang23fair` → `liu23geval` — LLM-as-a-Judge and its biases.
6. `yao24taubench` — agent reliability across repeated trials (pass^k).
7. `lewis20rag`, `asai23selfrag`, `liu23lost` — grounding.

Priority reproductions: Whisper WER on FLEURS Urdu; judge–human agreement on a small Urdu set; pass^k on a toy agent.
