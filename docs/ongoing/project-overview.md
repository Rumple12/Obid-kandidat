# Obid Project Overview

**Status:** Step 1 scope lock

**Repository:** `Rumple12/Obid-kandidat`

**Project type:** Obid bachelor thesis, developed as one collaborative system with two separately defensible thesis contributions

## Project purpose

Obid extends the completed Yacoub-compatible workflow-to-action system with a stronger, measurable agentic decision and reliability layer. The thesis is intentionally limited to one controlled temperature-to-fan scenario and one primary model configuration.

The project must show whether an n8n-based agentic decision layer can produce the expected IoT action consistently and whether runtime validation, deterministic action policy, and actual Human-in-the-Loop (HITL) approval can keep invalid or risky actions from reaching the inherited action interface.

## Contribution boundary

Yacoub supplies the inherited workflow/action-side handoff:

- local n8n and workflow-to-action infrastructure
- Python middleware/action API
- shared sensor-event and action contracts
- deterministic threshold baseline
- minimal Obid-compatible agent baseline
- existing Raspberry Pi/action-side validation and evidence

Obid supplies the new cognitive/reliability contribution:

- stronger single-agent decision design
- system-prompt design and explicit tool use
- controlled ReAct-style behavior
- one bounded-memory configuration
- structured action output
- runtime schema/output validation
- deterministic action-policy enforcement
- actual HITL behavior
- repeated reliability and latency evaluation against the inherited baseline

Detailed ownership and provenance rules are in [collaboration-boundary.md](collaboration-boundary.md). The verified engineering boundary is in [yacoub-handoff.md](yacoub-handoff.md).

## Tier 1.5 minimum passing system

```text
Yacoub-compatible sensor/test event
  -> Obid n8n agentic decision layer
  -> structured action output
  -> runtime schema/output validation
  -> deterministic action policy
  -> Human-in-the-Loop when required
  -> validated shared action interface
  -> Yacoub-compatible middleware/action boundary
  -> observable fan_on / fan_off behavior
  -> repeated evaluation evidence
```

The minimum core is one scenario, one primary model configuration, one main agent workflow, one bounded-memory configuration, the existing compatible contracts, actual runtime validation, one policy path, one actual approval path, and repeated evaluation. A validator agent or two-agent comparison is optional only after the core is stable.

## Research direction

The locked research questions measure:

1. action accuracy and consistency across normal, malformed, and state-dependent cases;
2. prevention of invalid or risky actions by validation, policy, and HITL; and
3. reliability and latency differences between the inherited minimal agent baseline and the extended Obid workflow.

The exact wording and evidence map are in [research-questions.md](research-questions.md).

Step 5 will freeze the evaluation cases. It must cover at least high temperature, low temperature, the decision boundary, malformed or missing input, unsupported/invalid action, a risky/HITL case, and a state-dependent/bounded-memory case if feasible. The preferred initial design target is five repetitions per case per evaluated core configuration, subject to Step 5 finalization. No evaluation runs have occurred in this repository at Step 1.

## Source reconciliation and contradictions

The source-of-truth order for Step 1 resolves scope as follows:

- The professor assignment proposes one or more agents, a single-agent versus multi-agent comparison, different devices and models, scalability, and Raspberry Pi-oriented evaluation. The active Step 1 scope narrows these to one primary model, one main single-agent workflow, one scenario, and no hardware requirement. A validator/two-agent comparison is supplementary only.
- Obid's approved plan assigns the cognitive workflow, system prompt, ReAct-style behavior, window-buffer memory, output validation, and HITL to Obid. This is compatible with the current scope, except that the plan says Obid will create communication schemas. Yacoub has already supplied the frozen shared schemas, so Obid must adopt and preserve them rather than claim them as newly authored.
- The frozen Yacoub baseline deliberately uses stateless/no-memory execution and no ReAct loop. Obid's bounded memory and controlled ReAct-style behavior are therefore upgrades, not inherited capabilities.
- Yacoub documents validation, policy, and HITL behavior but explicitly labels it specification-only. Runtime enforcement and actual approval are not inherited implementation and remain core Obid work.
- The frozen agent evidence identifies a Google Gemini Chat Model, but the committed workflow export does not include the configured model node or exact model/version. Step 6 must resolve this reproducibility gap before baseline comparison.

These points are recorded rather than hidden. They do not authorize any interface change.

## Active controls

- Work proceeds one explicitly requested numbered step at a time.
- `reference/` and the upstream Yacoub repository are read-only.
- No inherited Yacoub artifact may be represented as Obid-authored work.
- Shared contracts cannot change silently.
- Raw failures and negative outcomes must be retained.
- Claims in the report must trace to implementation or evaluation evidence.
- Optional work cannot displace runtime validation, HITL, or core evaluation.

## Step 1 sources

- [Root repository instructions](../../AGENTS.md)
- [Yacoub handoff reference](../../reference/yacoub-handoff.md)
- [Obid approved project plan](<../../reference/ObidProjekt plan(2).pdf>)
- [Professor assignment](<../../reference/Professor reserach assignment Agentic AI N8N.pdf>)
- [Yacoub 14-step process reference](<../../reference/Yacoub's Notion My 14 step plan (tier 1.5).pdf>)
- Frozen Yacoub commit `278318340bfa4e4650a97a2baba73f63bd868ed9`
