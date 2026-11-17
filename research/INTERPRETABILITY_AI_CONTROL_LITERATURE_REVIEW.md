# Interpretability, AI Control, and Trustworthy Autonomy

**Scoping literature review and preregistration draft | 2026-11-18**

**Research problem:** detect and prevent mismatches between an autonomous agent's assigned goal, intermediate decisions, tool requests, external effects, and reported outcome. Internal activations and written chain of thought (CoT) are useful but incomplete evidence about an agent's objectives.

> **Evidence status:** This is a primary-source-linked *initial scoping synthesis*, NOT the completed systematic review, a successful replication, or a claim of new results. A separate Deep Research literature review was launched on 2026-11-18 and was still in progress when this file was prepared. Integrate its findings only after citation, venue, and quantitative-claim verification.

## 1. Scope, terminology, and threat model

**Question:** Can a monitor identify a materially unauthorized action *before execution* and preserve useful task completion, even when the acting agent is unreliable or intentionally adversarial?

- **Objective:** a specified set of allowed outcomes, forbidden actions, budgets, and authority boundaries. Natural-language instructions alone are often ambiguous; record a structured policy and its provenance.
- **Objective–behavior divergence:** an observable action or proposed action inconsistent with the authorized policy, whether due to misunderstanding, shortcuts, corruption, reward hacking, or intentional subversion. Divergence **does not by itself prove deceptive intent**.
- **Monitorability:** how much relevant safety-relevant behavior can be detected from a chosen observation channel under a specified distribution and attack model.
- **CoT faithfulness:** whether stated reasoning accurately reflects causal factors influencing an answer or action. Legible prose is not evidence of faithfulness.
- **White-box signal:** activations, attention or representation probes, and interventions available when model access permits.
- **Black-box signal:** tool inputs/outputs, event logs, actual filesystem/network effects, user intent, and final report.
- **Controller:** the mechanism that blocks, rate-limits, audits, escalates, or rolls back an action. Detection and successful control are different outcomes.
- **Attacker:** untrusted model, prompt-injected tool result, compromised memory entry, or external adversary; threats should be evaluated separately.

**Trust boundaries:** user/developer instruction vs. retrieved pages and documents; model-proposed arguments vs. trusted tool executor; self-reported work vs. audited state changes; train/validation data vs. held-out deployments. Assume a local sandbox for all adversarial experiments; no production secrets or destructive integrations.

## 2. Rapid literature map (primary sources)

| Work / date | Evidence type | Main contribution relevant to this track | Limitations / question |
| --- | --- | --- | --- |
| [Turpin et al., 2023: Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) | Research preprint | Input biasing features can affect answers without appearing in model-generated CoT. | Selected tasks and perturbations do not characterize every model or every source of unfaithfulness. |
| [Greenblatt et al., 2023 preprint: AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942) | Research preprint | Evaluates safety/control protocols with a powerful untrusted policy, weaker trusted monitoring, and scarce trusted human review. | Threat model and programming-task setup may not transfer to persistent real-world agents. |
| [Heimersheim & Nanda, 2024: How to Use and Interpret Activation Patching](https://arxiv.org/abs/2404.15255) | Methodological preprint | Shows subtleties of causal interpretability interventions and interpretation. | Local causal effects do not by themselves establish agent intentions or reliable safety classification. |
| [AgentDojo, 2024](https://arxiv.org/abs/2406.13352) | Research preprint / benchmark | Dynamic prompt-injection environment for tool-using agents with attacks and defenses. | Successful injection, task failure, and policy violation must be reported separately. |
| [SHADE-Arena, 2025](https://arxiv.org/abs/2506.15740) | Research preprint / benchmark | Evaluates agent sabotage and the ability of monitors to notice suspicious trajectories. | Synthetic/adversarial tasks can overstate or understate natural-world frequency; monitor transfer is unresolved. |
| [Reliable Weak-to-Strong Monitoring of LLM Agents, 2025](https://arxiv.org/abs/2508.19461) | Research preprint | Red-teams monitors using diverse adversary awareness and computer-use scenarios. | Robustness under adaptive attacks and deployment shift remains the key validation challenge. |
| [OpenAI: Open Sourcing Monitorability Evaluations, Apr 23 2026](https://alignment.openai.com/monitorability-evals/) | Organization research report + [released code](https://github.com/openai/monitorability-evals) | Releases datasets/code spanning intervention, process, and outcome-property monitorability; describes g-mean-squared and cross-fit filtering. | Some evaluations remain private; metric choice and sample-selection effects matter. |
| [OpenAI: Investigating the consequences of accidentally grading CoT during RL, May 7 2026](https://alignment.openai.com/accidental-cot-grading/) | Organization research report | Studies training signals that could unintentionally optimize the apparent reasoning trace. | Does not imply every RL training method produces covert monitor evasion. |
| [OpenAI: How we detect frontier model misalignment, Oct 29 2026](https://alignment.openai.com/how-we-detect-frontier-model-misalignment/) | Organization operational report | Describes layered monitoring using reasoning, recent conversation, tool behavior, and escalated review. | Operational data and infrastructure are not fully public; measure real-world base rates, costs and latency. |
| [OpenAI: Training activation classifiers for safety and alignment, Nov 2 2026](https://alignment.openai.com/training-activation-classifiers/) | Organization research report | Streaming activation-based probes can flag policy risks during generation and before tool calls; complements text monitors. | Requires model activation access, supervised categories and ongoing calibration; adaptive robustness is not guaranteed. |
| [OpenAI: Eval-production behavior gaps in agent safety, Nov 3 2026](https://alignment.openai.com/eval-production-behavior-gap/) | Organization research report | Evaluation-objective framing can change agent behavior; some evaluated safety outcomes differ from comparable production settings. | Model, setup and population differences complicate generalization; stated eval awareness is not direct access to beliefs. |
| [Wang et al., OpenAI: What affects CoT monitorability across the model lifecycle?, Nov 10 2026](https://alignment.openai.com/cot-monitorability-model-lifecycle/) | Organization research report | Relates pretraining perplexity and architecture to no-CoT reasoning, and RL/model-generated data to CoT controllability. | **No-CoT capability and controllability are proxies**, not direct measures of deception or proven monitor evasion. |

**Key synthesis:** no single channel is a ground-truth window into internal intentions. Monitoring should be multi-layer, policy-aware, action-grounded, and tested against *adaptive* attacks. Prefer trustable external state and authorization boundaries to post hoc rationales. White-box probes can provide earlier warning but require careful causal and out-of-distribution validation.

## 3. What the November 10, 2026 study does—and does not—show

Source: [OpenAI study](https://alignment.openai.com/cot-monitorability-model-lifecycle/).

1. Across studied models, improving pretraining (lower perplexity) was associated with stronger no-CoT capabilities; some architectural variants had distinct strengths on particular multihop reasoning tasks.
2. CoT controllability increased during RL even without explicitly rewarding CoT contents in the investigated conditions; tool-use supervision had a smaller additional association.
3. Students trained on generated data from more CoT-controllable teachers exhibited greater controllability than matched students trained on less-controllable teachers.
4. **Critical distinction:** CoT controllability is noisy and imperfect; it is **not interchangeable with monitor-evasion success**. Avoid conclusions that all stronger or more controllable models are more deceptive.
5. Research opportunity: directly measure the incremental benefit of CoT, activations, tool traces, and verified side effects under matched adversarial conditions, rather than reporting a single proxy.

## 4. Taxonomy of candidate monitoring methods

| Layer | Inputs | Example mechanism | Failure modes |
| --- | --- | --- | --- |
| L0: hard authorization | User-approved policy, allowlists, signed execution context | Reject unauthorized tool capabilities, parameters or sensitive writes before dispatch | Too coarse policy; policy-parser mistakes; indirect side effects |
| L1: behavioral audit | Tool calls, actual tool results, state diffs, network/file logs | State-machine checks, anomaly detection, policy graph, provenance-aware verifier | Legitimate but unusual workflows; incomplete instrumentation |
| L2: trace monitoring | Visible CoT where available, plans, structured intents, conversation | Trusted reviewer classifies evidence and recommends escalation | Unfaithful, hidden, obfuscated or unavailable reasoning |
| L3: activation monitoring | Residual activations / learned probes | Token- or action-level risk scoring, abstention | Probe confounding, layer dependence, adaptive attacks, no access to closed weights |
| L4: causal investigation | Controlled changes to states, prompts or activations | Counterfactual interventions and activation patching | Correlation confused with causation; interventions alter task difficulty |
| L5: independent oversight | Human/stronger trusted reviewer, sandbox replay | Escalate high-risk actions; rollback audited changes | Cost, latency, reviewer mistakes, collusion and alert fatigue |

**Default:** hard constraints for irreversible actions, with a hybrid L1+L2 monitor; add L3 only for compatible open-weight policies. Evaluate every layer independently and in combination.

## 5. Gaps and adversarial review

1. **Intent ambiguity:** a forbidden state change may reflect a mistake, not subversion. Ground labels in policy violations, and keep intent-related claims separate.
2. **Counterfactual insufficiency:** text-only classifiers may catch harmful phrasing but miss innocuous-looking tool calls with dangerous effects. Record state diffs and replay outcomes.
3. **Eval contamination:** agents might infer the benchmark objective; split by environment and attack family, vary task framing, and run blinded hidden tests.
4. **Monitor gaming:** red-team against the monitor itself with access levels disclosed; hold out attack generators and use sequential adaptive attacks.
5. **Costs versus recall:** detection after execution is too late. Report time to first valid alert relative to the first irreversible action, along with token cost and latency.
6. **Selection bias:** a high AUROC on balanced sabotage examples may be useless at very low deployment base rates. Report alerts per 1,000 legitimate tasks and precision at realistic prevalence.
7. **Opaque model internals:** latent probes are impossible for some hosted APIs. Design a credible black-box baseline and report white-box gains only on comparable scenarios.
8. **Causal claims:** intervening on a feature and changing outputs supports a local mechanism claim, not proof of stable hidden goals.

## 6. Recommended publishable project

**Working title:** *Action-Grounded Early Warning for Objective–Behavior Divergence in Tool-Using AI Agents* (AGEW).

**Hypothesis H1:** Given identical actions and a fixed false-positive budget, a verifier using trusted state changes plus tool-call semantics detects more unauthorized behavior than a transcript-only LLM judge.

**H2:** Combining structured policy checks with a language-model reviewer yields earlier warnings (before dangerous tool execution) than monitoring final reports.

**H3 (optional; open models):** Adding an activation probe improves early detection under held-out attack types relative to equally budgeted action/trace monitoring, but may not generalize across model families.

**H4:** Monitor performance drops under adversarial task framing, indirect prompt injection, and held-out environments; use this as a failure-mode study rather than assuming robustness.

### Experimental design

**Unit of evaluation:** a complete agent episode, with tool-step timestamps and trusted environment state before/after each action.

**Safe sandbox tasks:** synthetic repo repair; simulated cloud IAM config; mock financial read-only workflow; filesystem operations confined to temp directories. No live exfiltration destinations, real credentials, or dangerous deployments.

**Examples:** an authorized refactor that includes a hidden permission change; a prompt-injected search result that induces an unauthorized write; an agent disabling an audit hook while claiming compliance; a benign maintenance task with similar-looking but authorized changes.

**Labels:** authorized outcome; unauthorized *attempt* before execution; unauthorized executed side effect; monitor alert timestamp; independent task completion. Use a deterministic policy oracle for explicit invariants, plus blinded human review for genuinely ambiguous tasks.

**Baselines:** (B0) no monitoring; (B1) keyword/rule monitor; (B2) transcript-only LLM monitor; (B3) tool-call classifier; (B4) execution-state verifier; (B5) proposed hybrid; (B6) optional activation probe/hybrid. Match budgets and the logged information available at each decision point.

**Primary metrics:**
- Recall and precision for unauthorized attempts at a fixed benign false-positive rate (e.g. 1%).
- *Pre-execution recall:* fraction of violations flagged before first prohibited tool effect.
- Safety–utility tradeoff: successful authorized tasks, blocked unsafe actions, unnecessary interventions.
- False alerts per 1,000 benign episodes; AUPRC and AUROC; calibration (ECE/Brier).
- Lead time (number of tool steps and milliseconds before harmful effect); p50/p95 monitor latency; model/API/compute cost.

**Robustness:** leave-one-attack-family-out; leave-one-task-environment-out; unseen base models; prompt injections at different trust boundaries; adaptive attacks with constrained monitor-query budgets; shifted benign-task prevalence.

**Statistics:** paired bootstrap confidence intervals by task family; at least three random seeds for stochastic components; report all attempted runs and exact failure cases. Predeclare the alert threshold on validation only. Separate development, attack tuning and untouched test sets.

**Ablation:** remove structured authorization; remove trusted state diff; remove CoT; remove activation features; remove reviewer; vary observation delay. Ensure no hidden ground-truth label is inadvertently supplied to a monitor.

### Minimal schema for reproducible traces

```json
{
  "episode_id": "episode-0001",
  "policy_id": "signed-policy-v1",
  "tool_step": 3,
  "agent_message": "proposed call or plan (optional)",
  "tool_name": "simulated_repo_write",
  "tool_arguments": {"path": "config/security.yml"},
  "authorized": false,
  "executed": false,
  "state_diff_hash": null,
  "monitor_score": 0.93,
  "monitor_alert_before_execute": true,
  "label_provenance": "deterministic_policy"
}
```

Treat the numeric score as **illustrative**, not an observed result. Never include privileged labels in features seen by the monitor.

## 7. Ninety-day execution plan

| Phase | Work | Exit criterion |
| --- | --- | --- |
| Days 1–15 | Complete full-paper checks and evidence table; freeze threat model and task/label schema | 15+ source-verified studies, rationale and gaps; no fabricated metrics |
| Days 16–30 | Implement deterministic simulator, sandbox and policy oracle; generate benign and adversarial trajectories | Seeded repeatability, isolated tools, tests for policy edge cases |
| Days 31–45 | Build B0–B4 and matched observation budgets | Baseline scripts, logged latency, attack success and false alerts |
| Days 46–60 | Implement hybrid monitor and pre-execution gate | Single primary preregistered H1/H2 experiment |
| Days 61–75 | Blind held-out attacks, shifts and ablations; optional probe extension | Confidence intervals, negative results, zero data leakage |
| Days 76–90 | Replication, documentation, reproducibility package, draft paper | Public code + configs + dataset cards + honest limitations |

**Go/no-go:** If a simple state verifier matches the proposed hybrid at lower latency/cost, publish that negative result and rethink novelty; do not rename engineering integration as a new scientific discovery.

## 8. Reading order and downstream artifacts

1. [AI Control](https://arxiv.org/abs/2312.06942) → explicit untrusted-model threat model.
2. [CoT unfaithfulness](https://arxiv.org/abs/2305.04388) → why explanations cannot be treated as ground truth.
3. [OpenAI monitorability evaluations + code](https://github.com/openai/monitorability-evals) → baseline metric reproduction.
4. [AgentDojo](https://arxiv.org/abs/2406.13352) and [SHADE-Arena](https://arxiv.org/abs/2506.15740) → agent attacks and monitor benchmarks.
5. [Activation classifiers](https://alignment.openai.com/training-activation-classifiers/) → white-box monitoring design.
6. [2026 model-lifecycle analysis](https://alignment.openai.com/cot-monitorability-model-lifecycle/) → direct research motivation.

**Next artifacts (not yet implemented):** structured paper-review table with exact author/venue verification; benchmark adapters; trace-schema validation tests; model/monitor implementations; analysis notebooks; results with confidence intervals. Review outcomes from the ongoing Deep Research run before claiming the literature is exhaustive.
