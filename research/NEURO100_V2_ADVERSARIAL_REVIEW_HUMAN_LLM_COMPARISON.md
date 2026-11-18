# Neuro100 v2: Adversarial Review and Human-vs-LLM Comparison

**Date:** 2026-11-18  
**Status:** Research protocol; no Neuro100 model, human-study results, or validated performance improvements are claimed.  
**Review decision:** MAJOR REVISION before architectural novelty or human parity claims.  
**Research target:** 5–30M-parameter LM, 100-token direct text attention, a separate thinking/task controller, separate long-term memory, goal decomposition, and sequential token output.  
**Related material:** [Architecture](BRAIN_INSPIRED_100_TOKEN_CONTEXT_ARCHITECTURE.md) · [Earlier adversarial review](NEURO100_ADVERSARIAL_REVIEW_2026-11-18.md).

## Executive judgment

**Yes, it is feasible to compare Neuro100 with humans and conventional LLMs on the same objective tasks.** The comparisons must separate task competence, memory retention, planning, recovery and efficiency. “Human level” can be asserted only for specific preregistered benchmarks, not as a claim of cognitive equivalence.

The core testable question is whether explicit, separately managed **task-control state** plus **episodic/semantic memory** improves long-horizon task completion over well-matched planning-only and memory-only methods when the LM sees at most 100 raw text tokens at a time.

A human reading one word at a time is an oversimplification: human working memory stores semantic chunks and task representations; a subword LM step is not equivalent to a human thought step. Human expertise and external artifacts (notes, calculations, code files) also carry information. Treat 100 tokens as an engineering bottleneck, not a measured human memory capacity.

## 1. Risk register

| ID | Severity | Adversarial finding | Correction |
| --- | --- | --- | --- |
| C01 | CRITICAL | Thinking and memory remain conflated: the controller hidden vector stores both goal state and old facts. | Distinct interfaces for controller, task workspace, and long-term episodic/semantic storage; instrument all state sizes. |
| C02 | CRITICAL | A nominal 100-position KV cache can conceal older context via cached hidden representations or multilayer receptive fields. | Strict baseline C0 requires suffix-equivalence: different prefixes, same final 100 tokens -> identical logits. |
| C03 | CRITICAL | Modular decomposer, evaluator, error monitoring and coordinator are already known (MAP 2025); episodic/semantic memory also exists. | Stop claiming first/new based on combinations. Define one falsifiable improvement over strongest baselines. |
| C04 | CRITICAL | Subgoals can be internally completed while violating an untracked root-goal requirement. | Require independent root-goal validator, dependency graph, interruption handling and recovery. |
| H05 | HIGH | A 5–30M model may not be competent enough to produce valid free-form plans or perform sophisticated coding. | First test constrained symbolic/structured goals and language competence; disclose failure boundaries. |
| H06 | HIGH | Planning may be equivalent to repeatedly retrieving a large external task description. | Count task graph bytes, retrieval tokens, recurrent bytes, auxiliary model size and compute separately. |
| H07 | HIGH | Erroneous memory writes create feedback loops, stale facts and instruction injection. | Versioned evidence, confidence/source labels, corrections, adversarial notes, calibrated abstention. |
| H08 | HIGH | Planner invoked per token causes extreme overhead. | Trigger planning/retrieval on events, boundaries or uncertainty; report cost per correctly completed task. |
| H09 | HIGH | V2 pseudocode emits the next token but does not feed it back into the rolling window in the same loop. | Explicit exactly-once token consumption and state mutation tests. |
| H10 | HIGH | Claiming “a few thousand floats <4 KiB” is dtype-dependent and usually false. | 2048 bf16 numbers = 4 KiB; 2048 fp32 numbers = 8 KiB, excluding overhead. |
| H11 | HIGH | Decomposition and notes may do all the work while the tiny LM contributes little. | Include deterministic goal tracker + SQLite and same-memory LLM baselines. |
| H12 | HIGH | Human-vs-LM outcomes can be unfair if humans use poor interfaces or different tools. | Run multiple human conditions, matched task information, participant expertise strata and counterbalanced order. |
| H13 | HIGH | Long output length, self-grading or task checklist completion can falsely signal success. | Independently executable objective checks and true final-state success, with human-blind quality ratings where needed. |
| H14 | HIGH | “Learning” could be mere retrieval; self-generated canon easy to game. | Test generalization to withheld/new task structures; isolate retriever effects from weight adaptation. |
| M15 | MEDIUM | A 100-token human display restriction is artificial and not a cognitive working-memory measurement. | Distinguish normal human ecological baseline from artificially restricted-display group. |
| M16 | MEDIUM | The completed Deep Research report states its redesign Markdown was saved, but live repository and Drive checks did not verify it. | Treat claimed redesign commit/file as unverified; cite only verified present artifacts. |

## 2. Corrected architecture: distinct thinking, memory and work products

Three distinct stores should exist:

1. **Thinking / task controller:** current root objective, active subgoal, dependency IDs, next operation, precondition verification, progress flags, error and plan revision signals. May include small recurrent state and a goal stack, but **not an unrestricted memory archive**.
2. **Long-term memory:** episodic events, verified semantic facts, optionally validated reusable procedural strategies. Memories have source, timestamp, confidence, supersession/deletion and strict read/write operations. It provides evidence; it does not autonomously decide the objective.
3. **Task workspace:** external drafts, source files, calculations, intermediate artifacts and test logs, separately budgeted from long-term memory. Human professionals rely heavily on these external artifacts.

The small LM is a token/action interpreter connected to a strictly bounded input interface. Suggested loop:

- Observe latest token or tool feedback.
- Retrieve the active subgoal and relevant evidence into the declared <=100-text-token channel, or a separately accounted latent interface.
- Choose one atomic action: DECOMPOSE, READ, WRITE, EXECUTE, VERIFY, REPLAN, or GENERATE.
- Execute and check environment state; update controller/workspace/memory through explicit operations.
- Emit at most the requested next token or action and repeat.

**Crucial contract distinction:**

- **C0:** only most recent 100 token IDs influence output; no other state or past data. Freshly recompute the 100-token suffix when verifying. Histories with identical final 100 tokens must produce identical logits.
- **C1 / Neuro100:** at most 100 direct text-token attention positions, but extra persistent controller/memory may influence generation. Count its bytes, tokens/vectors transferred, retrieval cost and model weights; never call this a 100-token *total-information* system.
- **C2:** expanding disk memories, clearly separated as non-constant-state upper bound.

These distinctions prevent a success on a large external database from being falsely attributed to a tiny context.

## 3. Human-vs-LLM comparison matrix

| Participant / system | Context or display | Notes / controller | Scientific purpose |
| --- | --- | --- | --- |
| H1: human, normal workflow | Normal reading, scrolling and task materials | Normal notes, editor and permitted tools | Ecological human performance reference |
| H2: human, constrained display | Rolling visible 100-token *text* viewport, with no backscroll | No persistent notes beyond final answer | Artificial constraint sensitivity; **not** human WM measurement |
| H3: human, constrained display + notes | Same artificial 100-token viewport | Budgeted note workspace | Measure cognitive-offloading advantage |
| M0: same-size strict local LM | C0 100-token input suffix | No controller or memory | Strict engineering baseline |
| M1: same-size recurrent LM | C1 <=100 direct text tokens | Fixed 4 KiB continuous state | Neural-memory baseline |
| M2: same-size LM, memory-only | C1 <=100 direct text tokens | Fixed-budget episodic notes, no planner | Memory effect |
| M3: same-size LM, planner-only | C1 <=100 direct text tokens | Fixed-budget goal graph, no long-term episode bank | Planning effect |
| M4: **Neuro100** | C1 <=100 direct text tokens | Goal graph + persistent memory, audited total bytes | Joint mechanism |
| M5: larger LM with constrained wrapper | Same 100-token text channel if technically enforceable | Identical note/tool budget | Scale effects |
| M6: frontier LM, native context | Normal vendor context | Normal allowed tools | Practical performance upper reference, NOT matched for parameter/state |
| M7: deterministic planner + structured store | Explicit task state | Exact same artifact/tools/memory budget | Check whether a neural controller is needed |

Human pretraining, expertise and perception cannot be matched numerically to LLM parameters. The target is **task behavior**, not matching humans' hidden thoughts. A person restricted to a 100-token viewport may perform worse due to UI friction; report this explicitly and include H1.

## 4. Four benchmark families

**B1 — Planning and replanning:** held-out graph navigation, Tower of Hanoi, dependency-constrained logistics, changed requirements and tool failure. Metrics: verified root goal, valid action %, length vs optimal plan, recovery success.

**B2 — Memory and future intentions:** entity updates, random IDs, superseded facts, deferred instructions (“after X, do Y”) after 200/1K/10K/100K irrelevant tokens. Metrics: exact recall, newest-fact accuracy, intention completion, abstention on unanswerable questions, total memory bytes.

**B3 — Large multi-stage artifact:** small synthetic code repositories with 3–20 linked requirements, regression tests and interruptions. Metrics: hidden tests, correct final files, unmet requirements, regressions, verified repair and time/cost. Use equivalent environments and developer tools for humans and models.

**B4 — Long-form output:** constrained multi-section stories/reports with seeded continuity facts and an independently generated event ledger. Metrics: constraints met, contradictory events per 1K tokens, repeated spans, completeness, blinded human ratings, total compute/storage. No credit merely for printing 100K tokens.

**Pilot proposal:** 10–20 tasks/domain, several independent model seeds and a small, diverse group of consenting humans; then establish test-set size and human sample with a power analysis. Keep training/dev/test generator seeds disjoint. Avoid making pilot results into strong human-parity claims.

## 5. Comparison protocol

- Same task objective, starting materials, legal operations, source access and independent success verifier for all conditions.
- Two resource views: **equal elapsed time** and **equal action/tool-call budget**. Neither alone removes all human-vs-AI asymmetry.
- Human groups should cover appropriate experience levels (or restrict claims to one expertise population); randomize task assignments and counterbalance order/learning effects.
- Record time-to-completion, total root-goal success, failures/recovery, tool calls, memory writes/reads, notes size, tokens generated, inference FLOPs, total model parameters, disk and peak RAM.
- Run each model multiple times with independent decoding seeds; report human participant variance and task uncertainty.
- Lock a primary outcome **before collecting test data**: externally verified root-goal completion over held-out long-horizon tasks.
- Report performance by task depth and difficulty, not a single “human intelligence score.” Use hierarchical logistic analysis or task-stratified bootstrap confidence intervals.
- A METR-style time-horizon analysis is possible: fit success probability against *human reference completion time*, then report where model success crosses 50%. This measures task difficulty, **not how long the AI can think continuously**.
- Report how “expert,” “normal workflow,” “constrained window,” “same tools” and “model configuration” were operationalized. Obtain informed consent and follow applicable ethics requirements for human participants.

## 6. Adversarial test battery

1. **Same suffix, contradictory history:** C0 output logits must be equal; C1 differences only from declared persistent state.
2. **Deceptive subgoal list:** all local subtasks pass but the root constraint fails. Does verifier detect and repair?
3. **Deferred task:** the agent must remember to perform Y after X despite 20 unrelated subtasks.
4. **Stale correction:** memory contains older and newer facts. Only the current sourced fact should win.
5. **Poisoned note:** retrieved memory contains malicious instructions. Controller must treat them as data.
6. **Overcapacity:** 1,000 unpredictable noncompressible facts arrive with 4 KiB state. Score retention utility and calibrated uncertainty, never assume exact unlimited recall.
7. **Overhead:** turn on/off planning and memory triggers. Does quality per second or cost change favorably?
8. **Self-generated facts:** separate independent future probes from claims the model chose for itself.
9. **Novel tasks:** same high-level skill but changed entity names, structures and task generators; score transfer without oracle data.
10. **UI unfairness:** compare human natural workflow against artificial rolling display before drawing human-cognition conclusions.

## 7. Scientific novelty and go/no-go gates

**Known precedents challenge a broad novelty claim:**

- Webb, Mondal & Momennejad (2025) introduced the **Modular Agentic Planner**, with decomposer, monitor and evaluator modules, and reported human-comparable results on a *specific* StrategyQA condition, not general human parity.
- Soar and ACT-R have long separated task control/working state from durable knowledge in cognitive-architecture research.
- RWKV, RMT, Mamba and BabyLM 2026 fixed-state models address bounded neural-state history.
- Neuro100's episodic store, memory selection, state updating and consolidation overlap prior memory-agent and brain-inspired RAG research.

**Gates**: (G0) verify 100-token direct attention with C0 suffix-equivalence; (G1) achieve basic next-token and structured task competence; (G2) each added subsystem beats meaningful baselines at comparable resource budgets; (G3) joint planning+memory improves root-goal success over planner-only and memory-only; (G4) recover reliably from delayed commitments and corruptions; (G5) human/model results are collected under transparent task protocols; (G6) only then formulate a narrowly supported publication claim.

**Final recommendation:** Do NOT train the full architecture as an end-to-end monolith yet. Implement a strict baseline, deterministic goal controller and simple memory, followed by quantitative ablations. The paper-worthy question is whether a **separate thinking controller and memory system** yield superior long-horizon task performance under a severe text-context limit—not whether the model literally works like a brain.

## 8. Primary references

1. Webb, Mondal & Momennejad, *A brain-inspired agentic architecture to improve planning with LLMs*, Nature Communications (2025). https://www.nature.com/articles/s41467-025-63804-5
2. Burnett & Richmond, *Meta-analytic investigations of the effect of cognitive offloading on memory-based task performance and interindividual variability*, Memory & Cognition (published June 2025; 2026 volume). https://link.springer.com/article/10.3758/s13421-025-01743-8
3. METR, *Task-completion time horizons* (accessed 2026-11-18). https://metr.org/time-horizons/
4. Kwa et al., *Measuring AI Ability to Complete Long Tasks* (2025). https://arxiv.org/abs/2503.14499
5. Furr, *Four Kilobytes of Memory: A 10M-Parameter Fixed-State Recurrent LM* (BabyLM 2026). https://aclanthology.org/2026.babylm-main.40/
6. Spens & Burgess, *Hippocampo-neocortical interaction as compressive retrieval-augmented generation* (2026). https://www.nature.com/articles/s41467-026-74357-6
7. Khorasani et al., *Hierarchical Reinforcement Learning with Targeted Causal Interventions* (2025). https://proceedings.mlr.press/v267/khorasani25a.html
8. SokoBench, *Evaluating Long-Horizon Planning and Reasoning in LLMs* (2026). https://arxiv.org/abs/2601.20856
9. *Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning* (EMNLP 2026). https://aclanthology.org/2026.emnlp-main.1299/
10. *MemFail: Stress-Testing Failure Modes of LLM Memory Systems* (Findings EMNLP 2026). https://aclanthology.org/2026.findings-emnlp.779/

**Provenance:** Primary papers and METR documentation support related published results; the user/deep-research Neuro100_v2 description supplies the proposed architecture. All predictions and pass thresholds in this document are recommendations, not experimentally demonstrated Neuro100 outcomes. The separate Deep Research claim that NEURO100_Redesign.md was saved was not corroborated by live GitHub/Drive lookup.
