# Obid Decision Log

Decisions are numbered, dated, and active until an explicit later entry supersedes them. A superseding decision must name the earlier entry and explain its evidence and scope impact.

## D-001 - Obid Tier 1.5 scope

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** The minimum passing thesis is one temperature-to-fan scenario, one primary model configuration, one main agent workflow, one bounded-memory configuration, runtime validation, one deterministic action-policy path, one actual HITL path, and repeated evaluation through the Yacoub-compatible interface.
- **Reason/impact:** This is the smallest system that can answer RQ1-RQ3 without broadening into production or platform research.

## D-002 - One collaborative system, two thesis contributions

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Yacoub and Obid contribute to one integrated system, but their implementations, evidence, and report claims must remain separately attributable.
- **Reason/impact:** Integration does not merge authorship. The collaboration boundary must be visible in architecture, methodology, results, and appendices.

## D-003 - Yacoub implementation remains inherited

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** The workflow-to-action infrastructure, middleware/action API, shared interfaces/contracts, deterministic baseline, minimal Obid-compatible agent baseline, and Raspberry Pi/action-side evidence are inherited/Yacoub-owned.
- **Reason/impact:** Obid may verify and compare these artifacts but cannot represent them as Obid-authored work.

## D-004 - Yacoub repository remains frozen

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** The authoritative Yacoub source is `Rumple12/new-yacoub-thesis` at commit `278318340bfa4e4650a97a2baba73f63bd868ed9`. Neither upstream nor `reference/` may be modified by Obid work.
- **Reason/impact:** A fixed source preserves provenance and prevents retrospective interface or evidence drift.

## D-005 - Shared-interface compatibility is mandatory

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Obid must preserve the frozen sensor-event fields/constants, action fields/allowed values, target `fan_1`, and `fan_on`/`fan_off` endpoint mapping.
- **Reason/impact:** The extended layer must remain a compatible cognitive/reliability upgrade, not a middleware redesign.

## D-006 - One primary model

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Core implementation and evaluation use one primary LLM/model configuration. The exact model and settings must be recorded before reportable runs.
- **Reason/impact:** Model-family benchmarking and any additional model configuration are out of scope.

## D-007 - One main agent design

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** The core Obid system uses one stronger single-agent workflow with explicit tools and controlled ReAct-style behavior.
- **Reason/impact:** Broad autonomous multi-agent architecture is unnecessary for RQ1-RQ3 and would add scope risk.

## D-008 - One bounded-memory configuration

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Obid will implement and evaluate one bounded-memory configuration. The inherited comparison baseline remains stateless/no-memory.
- **Reason/impact:** One defined state mechanism supports state-dependent testing without turning the thesis into a memory-strategy comparison.

## D-009 - Runtime validation and actual HITL are core

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Runtime structured-output validation, deterministic action-policy enforcement, and a real approve/reject HITL path are mandatory Tier 1.5 behavior.
- **Reason/impact:** Yacoub's safety/HITL artifacts are specification-only, so documentation alone cannot answer RQ2.

## D-010 - Minimal validator-agent/two-agent comparison is optional

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** One minimal validator-agent/two-agent comparison may be considered only after Step 9 core stability and is not required by any core research question.
- **Reason/impact:** Optional work must not consume validation, HITL, evaluation, evidence, or writing capacity.

## D-011 - Repeated evaluation is required

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Reportable evaluation must repeat frozen cases under identified configurations. Step 5 will finalize the count; the preferred initial target is five repetitions per case per evaluated core configuration.
- **Reason/impact:** Single demonstrations cannot establish consistency or support the planned reliability comparison.

## D-012 - Raw failures must be retained

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Failed, malformed, blocked, rejected, timed-out, missing, and unexpected runs remain in raw evidence with their denominators and error context.
- **Reason/impact:** Removing failures would bias reliability and safety conclusions.

## D-013 - Report claims trace to evidence

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** Every implementation, result, safety, latency, or hardware claim must trace to a versioned artifact or retained runtime/evaluation record.
- **Reason/impact:** Planned behavior and inherited documentation are not evidence that Obid runtime behavior occurred.

## D-014 - No silent contract changes

- **Date:** 2026-08-19
- **Status:** Accepted
- **Decision:** No shared contract or endpoint semantic may change without explicit authorization and a new decision entry describing compatibility and evaluation impact.
- **Reason/impact:** Silent changes would invalidate the collaboration boundary and baseline comparison.
