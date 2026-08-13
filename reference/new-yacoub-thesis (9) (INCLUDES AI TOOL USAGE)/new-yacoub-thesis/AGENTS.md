# AGENTS.md

## Repository mode

This repository follows the **new-yacoub** thesis plan.

This means:

- the original broader Yacoub/Obid dual-thesis scope is no longer the active implementation target
- **Yacoub's thesis is the primary delivery target**
- only the **minimum Obid-compatible workflow, safety, and contract layers** are implemented
- the repository must stay narrow, measurable, and pass-oriented

---

## Primary objective

Complete Yacoub's thesis in a narrowed but complete form.

The repo must support:

- local self-hosted n8n
- Docker-based runtime baseline
- Python middleware/API bridge
- one sensor/event path
- one actuator/action path
- latency measurement
- RAM/CPU measurement
- thermal measurement or thermal collection path
- evaluation results that can be used in the report

---

## Secondary objective

Implement only the minimum Obid-compatible integration required for:

- workflow integration
- validation/safety
- shared contract definition
- baseline-vs-agent comparison
- future handoff

This minimum layer is limited to:

- one workflow
- one prompt set
- one memory choice
- one JSON contract boundary
- one validation rule
- one human approval checkpoint

Anything beyond that is deferred.

---

## Scope rule

If there is a conflict between:

- a broader historical thesis idea
- a tempting architecture expansion
- a “cool” feature
- and the narrowed implementation plan

the **new-yacoub implementation plan wins**.

---

## Priority order

### Highest priority
1. `docs/plans/implementation-plan.md`
2. `docs/ongoing/yacoub-scope.md`
3. `infrastructure/`
4. `middleware/`
5. `evaluation/`
6. `docs/decisions.md`

### Lower priority, minimum only
7. `shared_interfaces/`
8. `cognitive_logic/`
9. `safety_layer/`

---

## Folder meaning

### High-priority folders
These directly support Yacoub's thesis completion:

- `infrastructure/`
  - Docker
  - local self-hosted n8n
  - runtime assumptions
  - Raspberry Pi deployment notes
  - monitoring hooks

- `middleware/`
  - Python API
  - mock/real sensor path
  - webhook push flow into n8n
  - actuator endpoints like `/fan/on`, `/fan/off`, `/status`

- `evaluation/`
  - datasets
  - metrics
  - results
  - comparison support
  - evidence for the report

- `docs/`
  - planning
  - scope locking
  - decision logging
  - architecture notes
  - report support

### Minimum-integration-only folders
These exist only to make the integrated system valid:

- `shared_interfaces/`
  - sensor/event schemas
  - action schemas
  - example payloads

- `cognitive_logic/`
  - one workflow
  - one prompt set
  - one memory choice

- `safety_layer/`
  - one validation path
  - one approval path
  - one blocked/unsafe case
  - one safe case

---

## Architecture assumptions

These decisions are locked unless explicitly changed in `docs/decisions.md`:

- development starts on a PC using simulated sensor data
- Raspberry Pi deployment is a later Tier 1.5 validation step
- middleware pushes events to n8n using a webhook-based flow
- metrics use lightweight local logging and Docker/runtime statistics
- the LLM/provider is treated as one implementation parameter and is not a model benchmark axis

---

## Anti-scope-creep rules

Do not:

- expand back into the original full Yacoub/Obid thesis scope
- introduce broad multi-agent architecture
- add multiple devices/models
- add multiple memory strategies
- build elaborate ReAct systems
- perform deep n8n core modification unless explicitly required
- introduce MCP in phase 0
- add heavy observability stacks such as Prometheus/Grafana
- optimize for publication-grade breadth over thesis completion

Prefer:

- one complete vertical slice
- one measurable scenario
- one complete baseline
- one minimal agent-enhanced path
- one clean evaluation loop

---

## Working rules for AI agents and tools

When working in this repository:

- protect the narrowed scope
- update planning/specification files before broad implementation when something is unclear
- prefer small, reviewable changes
- keep code and docs aligned
- keep the contract boundary explicit
- never create direct unsafe workflow-to-hardware action paths

Any API or schema change must update:

- `shared_interfaces/json-schema/`
- `shared_interfaces/examples/`
- `docs/architecture/`

Any risky physical action must pass through:

- `safety_layer/`
- then `middleware/`

---

## Antigravity guidance

Antigravity is the main IDE/planning environment.

Antigravity should:

- prioritize Yacoub-complete over Obid-complete
- maintain scope lock
- maintain planning files
- propose next steps in small vertical slices

Antigravity should not:

- redesign the thesis into a broader research platform
- expand into speculative architecture
- treat historical plan files as active implementation orders

---

## Codex guidance

Codex is used as a reviewer/fixer.

Use Codex for:

- audits
- scope checks
- diff reviews
- schema drift checks
- small bounded repairs

Use two thread roles only:

- `audit-review` = inspect, critique, warn
- `repair-fix` = apply one bounded fix

Codex should not silently broaden the architecture.

---

## Definition of success

This repository is on-track when it can support:

- one full end-to-end scenario
- one deterministic baseline
- one minimal agent-enhanced path
- one validation/approval path
- measurable latency/resource behavior
- enough evidence to feed the thesis report

This repository is off-track when it starts acting like:

- a full dual-thesis implementation
- a multi-agent research platform
- a many-device system
- a broad n8n internals project