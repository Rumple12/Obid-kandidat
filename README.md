# Obid Bachelor Thesis

This repository supports Obid's bachelor thesis on an n8n-based agentic decision and reliability layer for a controlled temperature-to-fan IoT scenario.

## Collaboration and scope

Yacoub provides the frozen workflow-to-action infrastructure, middleware/action API, shared contracts, deterministic baseline, minimal compatible agent baseline, and existing Raspberry Pi/action-side evidence. Obid's separately attributable contribution is the stronger single-agent decision layer with explicit tools, controlled ReAct-style behavior, bounded memory, structured output, runtime validation, deterministic policy, actual HITL, and repeated evaluation.

The Tier 1.5 minimum uses one scenario, one primary model configuration, one main Obid workflow, one bounded-memory configuration, the Yacoub-compatible interfaces, one runtime validation/policy path, one actual approval path, and repeated evidence. Optional validator-agent/two-agent work is non-core.

## Current status

Step 1 is closed. Step 2 establishes the repository and Codex-working foundation only. No n8n, Docker, workflow, middleware, schema copy, agent, safety runtime, HITL, dataset, or experimental result is implemented here yet.

## Active repository areas

- `docs/` - canonical plans, collaboration records, working conventions, decisions, and report-support notes
- `cognitive_logic/` - reserved for later inherited baselines and Obid cognitive artifacts
- `safety_layer/` - reserved for later runtime validation, policy, and HITL artifacts
- `shared_interfaces/` - reserved for later provenance-labelled adoption of compatible contracts
- `integration/` - reserved for the Yacoub-compatible integration test boundary and evidence
- `evaluation/` - reserved for the later frozen protocol, raw evidence, and results
- `reference/` - read-only source, history, and collaborator material; never the active implementation area

Each reserved top-level area contains a README stating its ownership and numbered-step boundary.

## Canonical documents

- Process: [`docs/plans/obid-14-step-process.md`](docs/plans/obid-14-step-process.md)
- Implementation strategy: [`docs/plans/implementation-plan.md`](docs/plans/implementation-plan.md)
- Scope: [`docs/ongoing/obid-scope.md`](docs/ongoing/obid-scope.md)
- Collaboration boundary: [`docs/ongoing/collaboration-boundary.md`](docs/ongoing/collaboration-boundary.md)
- Active Yacoub handoff: [`docs/ongoing/yacoub-handoff.md`](docs/ongoing/yacoub-handoff.md)
- Research questions: [`docs/ongoing/research-questions.md`](docs/ongoing/research-questions.md)
- Repository/Codex workflow: [`docs/ongoing/codex-workflow.md`](docs/ongoing/codex-workflow.md)
- Decisions: [`docs/decisions.md`](docs/decisions.md)

Work advances only through an explicitly requested numbered step. Audit `PASS` plus the required report-support evidence is the logical step-completion gate; a commit alone is not.
