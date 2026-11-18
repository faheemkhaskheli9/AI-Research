# Adversarial review: Small reasoning LM + external domain knowledge

**Review date:** 2026-11-18  
**Status:** literature-grounded critique and preregistration proposal; **no experiments run**  
**Thesis:** Train a compact model for language, general reasoning, evidence use, and tool control; store specialized and changing factual knowledge in external, swappable retrieval modules.

## Executive verdict

**Conditional GO for a controlled research program; NO-GO for claims of a "knowledge-free intelligent LM" or guaranteed lower end-to-end latency.**

The right research question is **how much parametric knowledge can be removed, at a fixed model and training budget, before evidence use and out-of-distribution reasoning deteriorate?** RAG can reduce the need to memorize *some* long-tail, dynamic facts; it does not remove the need for language, concepts, priors, algorithms, and enough background understanding to interpret evidence. A smaller retriever-augmented system can be effective, but retrieval costs, quality, and security must be counted.

## CRITICAL: correction to an earlier cited empirical paper

The original 2026 preprint *Can Small Language Models Use What They Retrieve?* (arXiv:2603.11513v1) reported an 85–100% failure rate even under "oracle" retrieval and large losses of previously known answers. **The author withdrew these headline oracle-based claims in August 2026.** The oracle selected a passage if it contained the answer string, which did not establish that the passage supported the question; evidence quality and distractor load were confounded. Replacing these passages with annotated HotpotQA supporting facts raised exact match by **+39.2/+44.3/+50.0 percentage points** on Qwen2.5 1.5B/3B/7B in the author's corrected re-evaluation. The corrected manuscript was not yet posted at the source's last update. The paper's other original statistics must not be quoted as validated current results. Its original arXiv page still exposes superseded claims.

- Correction: https://github.com/sanchitpandey/rag-utilization-study
- Superseded v1: https://arxiv.org/abs/2603.11513

This illustrates a specific research failure: answer-string containment is **not** an evidence-support oracle. Oracle benchmarks require verified entailment, complete multi-hop support, and passage provenance.

## Major falsification risks

| Risk | Severity | Why the proposal might fail | Required adversarial test |
|---|---|---|---|
| Knowledge and reasoning are entangled | Critical | Concepts, causal regularities, grammar, procedures and knowledge provide the substrate for reasoning. Withholding broad text may degrade both. | Compare full-data, fact-reduced, and entity-anonymized siblings with *same compute and tokens*, on unseen compositional tasks. |
| Knowledge suppression does not shrink weights | Critical | Changing pretraining data does not change parameter count, FLOPs/token, or KV-cache by itself. | Report size/compute reductions only after actual architecture compression or selecting a smaller model. |
| Retrieval is not free | High | Query encoding, ANN search, reranking, prompt prefill, longer context, KV-cache, index maintenance, and retries add latency/cost. | Measure end-to-end p50/p95 latency and money/query, not decode-only tokens/second. |
| Evidence retrieval may be missing or wrong | Critical | Citation-like text can be irrelevant, insufficient, obsolete, contradictory, or malicious. | Oracle-entailment, imperfect retrieval, missing evidence, conflict, and attack slices. |
| More reasoning training may overfit benchmarks | High | Teacher-generated traces and public exam tasks can leak targets, formatting, and solutions into train. | Held-out task families, private templated transformations, deduplication and blind scoring. |
| Model may not use correct evidence | High | Smaller models can confuse conflicting passages or rely on prior beliefs when source is newer. | Evidence swaps, invented entities, contradictory source priority, and abstention tests. |
| Domain plug-ins are not independent | High | Domain-specific inference requires expertise to interpret texts, not just fetch facts. | Cross-domain transfer with entirely unseen plug-ins and matched vocabulary density. |
| Tool access increases attack surface | High | Prompt injection, poisoned docs, cross-domain leakage and unauthorized retrieval may defeat a correct base model. | Typed provenance, access controls, untrusted-document handling, malicious retriever corpus. |
| Replacing weights with a big index moves costs | Medium | Search memory, embedding model and corpus provenance/rights can outweigh model-memory savings. | Account for generator + retriever + index RAM/disk + operations. |
| Small-model apparent parity can be narrow | High | A distilled 4B matching 120B on selected tasks does not establish general reasoning parity. | Unseen instruction families, compositional tasks, code execution, reliability curves. |

## Claims from the previous report that require correction

1. **"RAG must be integrated during training" — too strong.** Retrieval can help pretrained models without special training; retrieval-aware training (e.g. RAFT, RETRO, Atlas) can further help. The effect is task- and model-dependent.
2. **"Knowledge removal makes a smaller model" — unproven.** The Knowledge-Less LM work anonymizes named entities to shift reliance toward context and reports gains on some retrieval-grounded tasks, **not a parameter count reduction at equal capability**. Source: https://arxiv.org/abs/2607.12831
3. **"2T tokens for a 7B model is 2–3x Chinchilla" — false.** The rough 20 tokens/parameter reference gives ~140B tokens for 7B; 2T is ~14.3x this ratio. This reference is about training-compute optimality, not deployment-optimal performance. Source: https://papers.neurips.cc/paper_files/paper/2022/file/c1e2faff6f588870935f114ebe04a3e5-Paper-Conference.pdf
4. **"43,000 A100 hours for 7B/2T" — inconsistent with the cited throughput.** PyTorch reports ~3,700 tokens/sec/A100 or ~40B tokens/day across 128 A100s: 2T/40B = 50 days x 128 = **~6,400 A100-days = ~153,600 A100-hours**, before accounting for schedule overhead. Actual cloud price cannot be determined without quoted rates. Source: https://pytorch.org/blog/maximizing-training/
5. **"MoE saves 90% memory with 700M active of 8B total" — false without paging/offload.** Sparse activation reduces *per-token expert compute*, but the deployment must generally retain/load all expert weights. Expert routing, communication and memory can dominate. Do not confuse active parameters with resident parameters.
6. **"10–100 tokens/ms inference" — implausible as a typical single-request small-model metric.** That is 10,000–100,000 tokens/sec. Specify the hardware, model, batch, context, precision, concurrency, and **tokens/sec**. PyTorch provides realistic measured examples: https://pytorch.org/blog/accelerating-generative-ai-2/
7. **"QLoRA means 8-bit adapters" — incorrect.** QLoRA uses low-rank adapters while the frozen base is typically represented in 4-bit (e.g. NF4). Fine-tuning does not necessarily reduce inference model parameter count.
8. **"70–80% generic text and 20% reasoning" — not an established optimum.** It is an ablation candidate, not a literature-supported universal ratio. Data quality, duplication, task-family coverage, and token budget need controlled measurement.
9. **"RAG source text matching is evidence validation" — inadequate.** Entity/string overlap is not enough; verify claim entailment and multi-hop evidence completeness.
10. **"Small model matched 120B on 7/8 benchmarks" — narrow vendor benchmark.** It supports task-specific distillation, not universal reasoning equality or general intelligence. Check held-out quality, test design and contamination before extrapolating. Source: https://www.distillabs.ai/learn/how-we-benchmarked-12-small-language-models/

## Evidence that *does* support exploring the hypothesis

- **RETRO (ICML 2022):** Retrieval-enhanced language models improve next-token prediction and a 7.5B system with a huge external datastore reported performance competitive with much larger models on parts of the Pile. This is not a demonstration that ordinary chat, planning, or general intelligence has been matched. https://proceedings.mlr.press/v162/borgeaud22a.html
- **Atlas (JMLR 2023):** Retrieval integrated with language model training can improve knowledge-intensive few-shot QA; again, the measured tasks are narrower than all-purpose reasoning. https://www.jmlr.org/papers/v24/23-0037.html
- **RAFT (COLM 2024):** Evidence-aware fine-tuning with relevant passages and distractors improves several domain-specific QA settings; it does not establish universal gains. https://proceedings.colm.cc/paper_files/paper/2024/hash/f23750c16a2b5e7e4992db4702a0c366-Abstract-Conference.html
- **KLLM (2026 preprint):** Entity-anonymized pretraining appears promising for grounding and abstention, but needs independent replication and end-to-end size/cost checks. https://arxiv.org/abs/2607.12831
- **LIMO (COLM 2025):** Strong reasoning can be elicited from an already knowledge-rich foundation with selected examples; this is **not** evidence that broad pretraining knowledge is dispensable. https://proceedings.colm.cc/paper_files/paper/2025/hash/bc943cd038a5531d5433b1431c822c01-Abstract-Conference.html
- **Lost in the Middle (TACL 2024):** Evidence placement and long-context utilization are failure modes in context-grounded answering. https://arxiv.org/abs/2307.03172
- **RAGBench (2024):** Evaluate retrieval, relevance, answer faithfulness and context use separately. https://arxiv.org/abs/2407.11005

## Better system concept

`Request -> intent/uncertainty router -> {direct answer | verified retrieve + rerank | deterministic tool} -> small generator -> support checker -> answer / abstain`

Keep **within the model**: language, common concepts, basic world and scientific schemas, reading comprehension, formal reasoning practices, instruction following, multi-step planning, tool calling, epistemic calibration, and security-relevant boundaries.

Keep **outside**: dynamic and long-tail facts, documents, jurisdiction-specific rules, product/API versions, personal records subject to access control, case histories, research papers, and larger computational artifacts. Provide *typed*, versioned, provenance-bearing, swappable stores and deterministic tools for arithmetic/code execution. These are engineering targets, not proven cleanly separable representations.

Use a **two-stage controller**: first decide whether evidence is needed and from which domain; next give the generator as few **verified relevant** passages as possible. Retrieval should be skipped for questions where it cannot improve answer accuracy. Keep a no-retrieval fallback and explicit abstention policy.

## Preregistered hypothesis matrix (proposed, not performed)

- **H1: selective externalization** — for the *same target quality* on held-out domain QA, a smaller frozen RAG+tool generator delivers lower end-to-end cost and equal-or-better p95 latency than a larger closed-book model. **Reject** if quality fails or latency/cost is higher.
- **H2: retrieval-aware tuning** — at fixed base model and token budget, evidence-aware fine-tuning improves attribution and missing-evidence abstention versus ordinary instruction tuning. **Reject** without quality/calibration improvements across domains.
- **H3: partial knowledge suppression** — entity anonymization/reduced entity facts improves out-of-domain evidence reliance *without materially harming* novel reasoning or instruction following, under matched tokens and pretraining FLOPs. **Reject** if non-retrieval reasoning declines beyond prespecified margin.
- **H4: router value** — selective retrieval beats retrieve-every-time under the same retriever and generator on paired queries. **Reject** if decision errors erase cost/quality gains.
- **H5: modular transfer** — swapping from software to medical to science repositories without generator updates maintains calibrated evidence-grounded accuracy. **Reject** if domain-specific language comprehension fails.

## Minimum credible experiment

**Models:** Existing strong open-weight **1–2B and 3–4B models**, plus an **approximately 7–8B comparator**. Do not train a 7B foundation model from scratch for this initial experiment. Models must have license review and fixed model IDs/revisions.

**Conditions (paired prompts, same hardware where applicable):**
A. 1–2B closed-book; B. same 1–2B naive RAG; C. same 1–2B reranked oracle-supported RAG; D. same 1–2B evidence-aware fine-tuned + RAG; E. same 1–2B with conditional retrieval and abstention; F. 3–4B RAG equivalent; G. 7–8B closed-book baseline. Later add factual suppression on an *actual matched-pretraining* small model; do **not** compare two already differently-pretrained commercial checkpoints and claim causal effects.

**Data:** At least 3 domains (software, biomedical literature, general science), with a fully held-out fourth domain; include question-only, answer-evidence, multi-hop, conflicting dates, missing passages, paraphrases, adversarial additions, and injected instructions. Version document snapshots and record provenance/licensing. Construct oracle passages using human-validated support spans, not string matches. Keep all teacher traces and contaminated benchmark instances separate from evaluation.

**Metrics:** Answer accuracy/EM and semantic correctness; citation support and faithfulness; evidence recall and reranker NDCG; abstention precision/recall and selective risk; known-vs-unknown retrieval impact; task-family transfer; prompt-injection failure rate; **p50/p95 full-stack latency**, tokens retrieved/prefilled/generated, resident RAM/VRAM, index size and cost/query at specified traffic.

**Statistics:** Multiple random seeds (>=3 if fine-tuning), bootstrap paired 95% CIs, preregistered primary metrics, multiple-testing correction, per-domain failures and unfiltered negative results. Use identical quantization/hardware wherever feasible.

**Hard failure gate (example, adjustable before experiment):** Reject the architecture as a blanket replacement if the small RAG system loses more than 3 percentage points of grounded task accuracy versus comparator, violates a fixed p95 latency SLO, or meaningfully increases prompt-injection failures. Record statistical uncertainty; a result near the gate is inconclusive.

## Practical schedule and budget boundaries

1. **Baseline first:** Use local 6 GB VRAM for quantized 1–2B inference, lightweight retrieval and data-pipeline unit tests; do not promise 7B full fine-tuning on this GPU. Larger quantized inference, offload, or 3–4B QLoRA may depend on context length and real memory measurements.
2. **Evaluate retrieval before fine-tuning:** Establish whether retrieval helps when evidence is genuinely sufficient and what happens with missing/conflicting evidence.
3. **Train only when an observed failure is repairable:** Build balanced, provenance-checked supervised examples with distractors and explicit abstentions. Fine-tune a small student with LoRA/QLoRA, measure after each stage.
4. **Compare both quality and economics:** Query encoder, index, reranker, retrieval, context prefill, decoding, tool execution and retries must all enter the latency bill.
5. **Only if the project clears gates:** Consider a very small from-scratch paired pretraining ablation for knowledge suppression. Running a 7B scratch pretraining experiment should be a separately justified high-budget research project.

## Open issues and novelty

Simple "small LLM + RAG" is established prior art. Publishable novelty might arise from **a causal measurement of the minimum parametric conceptual substrate for cross-domain transfer**, **an evidence-support aware routing policy optimized for p95 latency**, or **quantifying how anonymization affects reasoning under fixed FLOPs and controlled retrieval quality**. A high bar is necessary: new method must beat retrieve-all, no-RAG, teacher distillation, and retrieval-aware fine-tuning baselines, not just a poor naive RAG comparator.

**Bottom line:** The architectural intuition is useful, but "only train intelligence and retrieve all knowledge" is not a scientifically supported partition. Treat it as a falsifiable compression-and-grounding project. Smaller model weights and faster generation must be demonstrated *at system level* rather than inferred from reduced factual memorization.
