# Obid Scope Lock

**Scope version:** Step 1

**Status:** Locked unless changed by an explicit later decision

**Primary contribution:** Agentic decision-making and reliability on top of the frozen Yacoub-compatible workflow-to-action system

## Scope statement

Obid will implement and evaluate one stronger single-agent n8n decision layer for one controlled temperature-to-fan IoT scenario. The work begins at the compatible sensor/test-event boundary and ends at the existing Yacoub middleware/action boundary. Obid does not rebuild the inherited middleware, contracts, deterministic baseline, minimal agent baseline, or Raspberry Pi/action-side evidence.

## In scope

- agentic decision design
- one primary LLM/model configuration
- system-prompt design
- explicit tool use
- controlled ReAct-style behavior
- one bounded-memory configuration
- structured action output
- runtime schema/output validation
- deterministic action-policy enforcement
- one actual HITL path
- repeated reliability evaluation
- latency comparison with the inherited minimal agent baseline
- compatibility integration with Yacoub's sensor-event, action, and middleware boundaries
- preservation of raw outputs, failures, blocked actions, approval decisions, and timing evidence

## Tier 1.5 minimum core

- one controlled IoT scenario: temperature event to simulated `fan_on`/`fan_off`
- one primary model configuration
- one main Obid agent workflow
- one bounded-memory configuration
- the frozen Yacoub-compatible sensor-event and action contracts
- actual runtime output/schema validation
- one deterministic action-policy path
- one real approve/reject HITL interaction path
- repeated runs over frozen test cases
- comparison with the inherited minimal agent baseline under the same cases

## Out of scope by default

- broad autonomous multi-agent architecture
- validator-agent or two-agent architecture as a core requirement
- multiple IoT devices
- multiple model benchmarking
- real GPIO as a requirement
- full physical hardware development
- Raspberry Pi deployment as an Obid requirement
- MCP
- n8n core modification
- Prometheus/Grafana
- production deployment
- large-scale scalability benchmarking
- production-grade AI safety claims
- broad model-alignment or guardrail research
- long-term memory, vector-store memory, or a comparison of memory strategies
- rebuilding or redesigning Yacoub's middleware/action API
- changing shared contracts without an explicit, documented compatibility decision

## Optional work gate

Only after the Step 9 core is stable and evidenced may the project consider:

- one minimal validator-agent/two-agent comparison.

An architecture illustration remains normal documentation work and is not an implementation extension.

Optional work is omitted if it threatens validation, HITL, repeated evaluation, evidence quality, or writing time. The core research questions do not depend on optional work.

## Ownership and authorship limits

The following are inherited and cannot be claimed as Obid-authored: workflow-to-action infrastructure, middleware/action API, shared interfaces/contracts, deterministic baseline, minimal compatible agent baseline, and Raspberry Pi/action-side evidence.

Obid may configure, integrate, test, and compare inherited artifacts as part of its methodology. Any necessary compatibility repair must be logged with its exact reason and must not be described as original Obid architecture.

## Success boundary

The Obid thesis passes at Tier 1.5 when the core pipeline runs end to end, invalid or risky actions are demonstrably stopped or approved at runtime, and repeated evidence answers RQ1-RQ3 without relying on the optional validator-agent/two-agent comparison or adding multiple-device or multiple-model work.

## Change control

Any proposed scope expansion requires:

1. an explicit user/supervisor decision;
2. a new entry in `docs/decisions.md`;
3. impact analysis for the research questions and evidence plan; and
4. confirmation that the Yacoub interface and provenance boundaries remain intact.
