# Yacoub-Obid Collaboration Boundary

**Boundary status:** Locked in Step 1

**Collaboration model:** One integrated system, two separately defensible bachelor-thesis contributions

## Ownership summary

| Area | Yacoub-owned / inherited | Obid-owned | Shared use |
| --- | --- | --- | --- |
| Workflow/action infrastructure | Existing local n8n setup and workflow-to-action path | Compatible integration only | Runtime used for end-to-end tests |
| Middleware/action API | Python API, mock state, sensor forwarding, fan endpoints | Must not rebuild; may call through compatible boundary | Observable action execution boundary |
| Contracts | Frozen sensor-event and agent-action schemas and examples | Runtime validation and policy enforcement of those contracts | Common interface and evaluation vocabulary |
| Baselines | Deterministic threshold workflow and minimal agent workflow | Verify, preserve, and compare; do not claim authorship | Common comparison configurations |
| Cognitive design | Minimal strict-output, stateless agent handoff | Stronger single-agent design, prompt, explicit tool use, controlled ReAct, bounded memory | Same input/action semantics |
| Safety/HITL | Documentation/specification-level rules only | Runtime validation, deterministic policy, actual HITL | Agreed rule vocabulary and evidence boundary |
| Evaluation | Existing Yacoub local/Pi evidence is inherited context | Repeated Obid reliability and latency evaluation | Same cases for fair baseline comparison |
| Hardware/Pi | Existing Raspberry Pi/action-side validation and evidence | Not an Obid requirement | Reference context only unless explicitly reused with provenance |

Shared does not mean co-authored. A shared component may be Yacoub-authored and merely reused by Obid.

## Architecture boundary

```text
YACOUB-OWNED / INHERITED                           OBID-OWNED

sensor or test event
  -> middleware POST /sensor-event
  -> Yacoub-compatible sensor-event contract  === compatibility seam ===
                                                  -> stronger single-agent decision
                                                  -> explicit tool use / controlled ReAct
                                                  -> bounded memory
                                                  -> structured action output
                                                  -> runtime schema/output validation
                                                  -> deterministic action policy
                                                  -> actual HITL when required
validated Yacoub-compatible action contract    === compatibility seam ===
  -> POST /fan/on or POST /fan/off
  -> simulated fan state / inherited action evidence

COMPARISON ANCHORS: inherited deterministic baseline and minimal agent baseline
```

## Yacoub-owned components

- `infrastructure/docker/` local n8n baseline in the frozen source
- `middleware/` API, sensor normalization/forwarding, and simulated fan actions
- `shared_interfaces/` schemas and examples
- `cognitive_logic/workflows/deterministic-baseline.*`
- `cognitive_logic/workflows/agent-minimal.*`
- the minimal system prompt and stateless memory choice used by that baseline
- frozen workflow runtime screenshots/logs
- evaluation harness/results and Raspberry Pi/action-side evidence already present in Yacoub's thesis repository
- the documented, but not runtime-enforced, Step 8 safety/HITL design

## Obid-owned components

- system-prompt design for the extended workflow
- stronger single-agent decision layer
- explicit tools exposed to and used by the agent
- a controlled and bounded ReAct-style interaction pattern
- one bounded-memory implementation and its state rules
- structured action generation within the inherited action contract
- runtime schema/output validation with observable outcomes
- deterministic action-policy enforcement
- an actual HITL checkpoint with approve/reject behavior
- repeated test execution, reliability analysis, and latency comparison
- Obid-specific evidence, limitations, and thesis argument

## Shared components

The shared integration surface is deliberately small:

- temperature sensor/test-event semantics
- sensor-event schema fields and allowed constants
- action schema fields and allowed values
- action-to-endpoint mapping
- n8n-to-middleware network boundary
- `fan_on` and `fan_off` observable behavior
- common test cases used for baseline comparison
- trace identifiers and evidence conventions later added without changing the contracts, if possible

Any shared artifact retains its original provenance. Reuse, configuration, test execution, and comparison do not transfer authorship.

## Inherited components and Obid upgrades

| Inherited handoff | Current inherited state | Obid upgrade |
| --- | --- | --- |
| Minimal agent decision | One LLM decision, strict prompt, JSON extraction | Stronger controlled single-agent decision behavior |
| Tool/action use | Workflow branches call fixed fan endpoints | Explicit, bounded tool-use semantics and evidence |
| Memory | Stateless/no memory | One bounded-memory configuration |
| Agent behavior | No ReAct loop | Controlled ReAct-style behavior with bounded iterations/actions |
| Structured output | Prompted JSON plus regex/`JSON.parse` extraction | Contract-bound structured output with runtime validation |
| Action safety | Unsupported action becomes unrouted; safety rules are documentation | Deterministic runtime policy gate with reasoned outcomes |
| HITL | Approval design document only | Actual pause, approve/reject, and auditable continuation/blocking |
| Evaluation | Limited inherited runs and Yacoub-specific evidence | Repeated Obid cases answering RQ1-RQ3 |

## Compatibility requirements

Obid must preserve unless an explicit compatibility decision is approved:

1. Sensor-event fields: `sensor_id`, `timestamp`, `type`, `value`, `unit`.
2. Sensor constants: `type` is `temperature`; `unit` is `C`; `value` is numeric.
3. Action fields: `action_id`, `target`, `reason`, `requires_approval` with no extra fields.
4. Allowed actions: `fan_on`, `fan_off`.
5. Allowed target: `fan_1`.
6. Endpoint mapping: `fan_on -> POST /fan/on`; `fan_off -> POST /fan/off`.
7. Middleware service semantics: `/status`, `/sensor-event`, `/fan/on`, and `/fan/off` remain Yacoub-owned.
8. Baseline threshold semantics: `value >= 30.0 C` selects `fan_on`; lower values select `fan_off`.
9. Action execution remains mediated through the middleware boundary; agent output does not directly control GPIO or shell/hardware commands.
10. Baseline comparison uses the same frozen cases and clearly records any unavoidable environment/configuration difference.

Compatibility means preserving interface behavior, not copying Yacoub implementation into Obid folders during Step 1.

## Provenance rules

- Cite the Yacoub repository, frozen commit, and exact artifact path whenever inherited behavior is described.
- Label inherited implementations, screenshots, measurements, and Raspberry Pi evidence as Yacoub-provided.
- Label Obid-created validators, policy gates, HITL nodes, prompts, memory, workflows, and results as Obid-authored only after they exist.
- Separate inherited evidence from newly collected Obid evidence in filenames, tables, and report prose.
- Do not use wording such as “we created” for an inherited contract, API, baseline, or Pi result.
- If Obid makes a compatibility fix, record the original artifact, the changed file, why it was necessary, and whether semantics changed.
- Never rewrite history by replacing a raw failure or unsuccessful approval/action trace.
- Never silently change a shared contract. Record a decision and obtain explicit authorization first.

## Boundary completion test

The collaboration boundary is preserved when the extended Obid workflow can accept a Yacoub-compatible event and, after Obid-owned decision/reliability handling, either:

- call the correct inherited fan endpoint with a valid allowed action;
- pause for and honor a real HITL decision; or
- block the action without either fan endpoint being called.
