# Step 9 report-support note

## Step

Step 9 — Implement actual Human-in-the-Loop behavior

## Status

Step 9 implemented actual runtime human approval and denial, completed bounded one-off HITL readiness, preserved the initial compatibility failure, and applied one bounded runtime compatibility repair. The initial audit returned `PASS WITH MINOR REPAIR`; the optional-validator scope finding was resolved, and final re-audit returned `PASS` with no remaining findings.

Mandatory Step 9 core work is complete. The optional validator agent was deliberately skipped, and Step 10 has not started. These observations are implementation/readiness evidence, not repeated HITL-effectiveness evidence or final RQ2 results.

## Why Step 9 was necessary

Step 8 established:

```text
candidate action
→ parser
→ frozen-schema validation
→ deterministic policy
→ ALLOW / BLOCK / APPROVAL_REQUIRED
```

but intentionally stopped at `OBID_APPROVAL_REQUIRED_PENDING_STEP9`. Step 9 adds the real human boundary:

```text
APPROVAL_REQUIRED
→ actual n8n waiting execution
→ human manually approves or denies

approve
→ release exact held action
→ endpoint

deny
→ release nothing
→ no endpoint
```

This completes the mandatory runtime-reliability chain before repeated evaluation.

## Yacoub HITL handoff

- Repository: `Rumple12/new-yacoub-thesis`
- Frozen commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`
- Inherited specification: `safety_layer/approvals/hitl-v1.md`

Yacoub supplied the specification-level HITL concept: validate before review, approval cannot rescue invalid output, and human rejection prevents middleware execution. It did not implement a runtime Wait node, approval form, persisted waiting execution, actual human interaction, release after approval, or denial runtime behavior. Those mechanics are `OBID_CREATED`.

## Version lineage

| Version | Preserved role |
| --- | --- |
| `CONFIG-OBID` v1 | cognitive layer |
| `CONFIG-OBID` v2 | same cognition + runtime validation + deterministic policy |
| `CONFIG-OBID` v3 | same cognition and safety + actual HITL |

Earlier versions remain preserved rather than overwritten.

## `CONFIG-OBID` v3

- Artifact: `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`
- Name: `CONFIG-OBID - Single Agent v3 HITL`
- ID: `obid-agent-v3-hitl`
- Production webhook: `POST /webhook/obid-agent-v3-hitl`
- Portable export: inactive and sanitized
- SHA-256: `1a09ee5a3199289c39845f9b97a3a3f516f277924d6a8fcb52da52780b0eaf78`

Step 7 cognition remains unchanged: one Agent v3, one Gemini v1 node using `models/gemini-2.5-flash`, generation options `{}`, `maxIterations: 3`, the same prompt, two tools, two-interaction Simple Memory, internal decision envelope, and no-action path. No second agent or model exists.

## Runtime safety v2 HITL

- Artifact: `safety_layer/workflows/runtime-safety-v2-hitl.json`
- Name: `Step 9 - Runtime safety v2 HITL`
- ID: `runtime-safety-v2-hitl`
- SHA-256: `8dbf1826f43cdea34d510ff53e90fed52e45c93d5ed29956cf3a6dbfd6de652d`

Step 8 parsing and frozen-schema validation remain unchanged. The Step 9 policy-context addition occurs only after successful validation.

## Controlled policy context

The exact internal context is:

```json
{
  "policy_case_id": "POLICY-HITL-REQUIRED",
  "approval_required": true,
  "shared_contract_field": false
}
```

This metadata remains internal and is not inserted into the shared action or schema. Only this exact context is recognized. No context preserves Step 8 direct behavior; any unrecognized supplied context fails closed.

## Approval-required transformation

The frozen proposal is:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature requires a policy-controlled fan activation",
  "requires_approval": false
}
```

After schema validation and exact context recognition:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature requires a policy-controlled fan activation",
  "requires_approval": true
}
```

Only `requires_approval` changes. `action_id`, `target`, and `reason` remain unchanged; no shared field is added.

## Validation-before-HITL invariant

```text
invalid candidate
→ validator BLOCK
→ no policy-context transformation
→ no HITL request
→ no human gate
→ no endpoint
```

Human review is available only for already-schema-valid actions, so approval cannot make an invalid action valid.

## Actual human mechanism

- Node: `n8n-nodes-base.wait`
- Type version: `1.1`
- Mode: `resume: form`
- Wait duration: indefinite until human interaction

The form displays read-only review information and exactly one controlled field, `human_decision`, with allowed values `approve` and `deny`. The reviewer cannot edit `action_id`, `target`, `reason`, or `requires_approval`; the action shown is the stored held action.

## HITL request identity

Request IDs use `hitl-<execution-id>`, including `hitl-66`, `hitl-71`, and `hitl-73`. These identifiers are synthetic and non-private. No reviewer identity is required or stored.

## Stored-action integrity

Before waiting, the runtime retains the held action and a four-field snapshot. After resume, it compares `action_id`, `target`, `reason`, and `requires_approval` against that stored snapshot. Approval can release only the already-stored held action; the form does not recreate it.

`held_action_unchanged: true` was observed for the completed original child approval and the repaired approval and denial cases. This is deterministic field-level integrity, not cryptographic integrity.

## Pending-state invariant

Before approval or denial, executions 66, 71, and 73 were directly observed in waiting state with a held action, `released_action: null`, endpoint counts `/fan/on: 0` and `/fan/off: 0`, and simulated fan state off. This was runtime evidence rather than inference from node names.

## Original approval attempt — retained failure

The original topology used harness 64, safety 65, and HITL child 66. Before decision, executions 64/66 physically waited; request `hitl-66` held the valid approval-required action, released null, called no endpoint, and left the fan off.

The human manually selected `approve`. Child 66 correctly recorded `human_decision: approve`, `held_action_unchanged: true`, and the unchanged released action with `requires_approval: true`. Human wait was approximately `200,106 ms`.

However, n8n `1.123.37` returned the child's pre-wait input to its synchronous parent instead of the completed post-wait output. The parent could not establish approval authorization and failed closed: `/fan/on: 0`, `/fan/off: 0`, fan off. Verdict: `FAIL-CLOSED`. This failure remains preserved rather than rewritten as success.

## Compatibility repair

Original topology:

```text
parent
→ Execute Sub-workflow
→ child Wait
→ resume child
→ completed child result not propagated correctly to parent
```

Compatible topology:

```text
caller
→ native Wait/form embedded directly
→ same execution resumes after human decision
```

The final gate was embedded directly in the Step 9 readiness harness and `CONFIG-OBID` v3. The repair changed only placement; it did not change schema validation, policy context, transformation, decision values, held-action logic, endpoint authorization, Gemini model, prompt, tools, or memory.

## Retained standalone gate artifact

- Artifact: `safety_layer/hitl/workflows/runtime-hitl-v1.json`
- Name: `Step 9 - Runtime HITL gate v1`
- ID: `runtime-hitl-v1`
- SHA-256: `fd9ce59e033c6074d6688d9eb0037dff7afc3d882a74fea0743901dfa041d902`

This is the retained original standalone-subworkflow compatibility attempt, not the final compatible runtime placement.

## Final HITL readiness harness

- Artifact: `safety_layer/hitl/workflows/step-09-hitl-harness.json`
- Name: `Step 9 - HITL readiness harness`
- ID: `step-09-hitl-harness`
- SHA-256: `090715a02ed15ce0a385788fad8f25abceec7cd473422f63c9114909d850eaac`

The harness operates at frozen `OBID_POLICY_INPUT`, uses the same safety-v2 semantics as `CONFIG-OBID` v3, and embeds a parameter-identical Wait/form gate. It supplied bounded HITL-specific readiness and was inactive/sanitized after verification.

## Approval repair-verification run

`S9-HITL-APPROVE-REPAIR-VERIFY` was a separately human-authorized compatibility check, not a replacement for the original failure or a Step 10 repetition.

Executions 71/72 recorded request `hitl-71`. While pending, execution 71 was physically waiting with a valid held action, null release, endpoints 0/0, and fan off. The human selected `approve`. After resume it recorded:

- `hitl_status: approved` and `human_decision: approve`;
- `held_action_unchanged: true` and no unexpected submitted action fields;
- released action exactly equal to the held action;
- `requires_approval: true` retained;
- `/fan/on` exactly once and `/fan/off` zero; and
- fan off → on.

Verdict: PASS.

## Approval timing

| Segment | Duration |
| --- | ---: |
| Pre-wait automation | `498 ms` |
| Human wait | `104,301 ms` |
| Post-decision automation | `242 ms` |
| Total | `105,041 ms` |

Human wait is retained separately. This single observation is not a general estimate of approval time.

## Denial readiness

`S9-HITL-DENY`, executions 73/74, recorded request `hitl-73`. Before decision, execution 73 physically waited with the held action, null release, endpoints 0/0, and fan off. The human selected `deny`.

After resume it recorded `hitl_status: denied`, `human_decision: deny`, `held_action_unchanged: true`, `released_action: null`, terminal `OBID_HITL_DENIED`, endpoints 0/0, and fan off → off. Verdict: PASS.

## Denial timing

| Segment | Duration |
| --- | ---: |
| Pre-wait automation | `325 ms` |
| Human wait | `43,032 ms` |
| Post-decision automation | `105 ms` |
| Total | `43,462 ms` |

Human wait remains separate from automated processing.

## Timing model

The runtime retains `hitl_flow_started_at`, `approval_requested_at`, `approval_decided_at`, and `hitl_completed_at`.

```text
pre-wait automation
= flow start → wait begins

human wait
= request shown → human decision

post-decision automation
= decision → final terminal/endpoint completion

total HITL elapsed
= flow start → final completion
```

Human wait must remain excluded from the primary automated RQ3 latency comparison.

## Invalid-action regression

Executions 67/68 supplied `fan_reverse` together with HITL context. The validator returned `UNKNOWN_ACTION`; context was not applied, policy was not reached, no HITL request or Wait occurred, endpoints remained 0/0, and fan state stayed off. This bounded observation shows that approval cannot rescue an invalid action.

## Normal direct-allow regression

Executions 69/70 supplied valid `fan_on` without HITL context. Validation passed, policy returned `ALLOW`, HITL was not entered, `/fan/on` executed exactly once, and fan state changed off → on. Step 9 therefore does not force every valid action through human approval.

## No-action path

No separate Step 9 runtime no-action probe was executed. Static comparison showed that `CONFIG-OBID` v3 preserves the Step 7 internal form:

```json
{
  "decision": "no_action",
  "action": null
}
```

The branch bypasses safety/HITL and reaches no endpoint. Its lack of a Step 9 rerun remains a methodological limitation.

## Endpoint-release invariant

### Direct action

```text
schema_valid
AND policy_decision == allow
→ endpoint
```

### HITL action

```text
schema_valid
AND policy_decision == approval_required
AND hitl_status == approved
AND human_decision == approve
AND held_action_unchanged == true
→ endpoint
```

Every other observed outcome reached no endpoint.

## Approval does not alter the shared action

The approved shared action remains:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature requires a policy-controlled fan activation",
  "requires_approval": true
}
```

Human approval is separate runtime metadata and does not reset `requires_approval` to false.

## Denial semantics

Denial retains the held action only as audit/evidence context and releases `null`. No endpoint executes, and there is no retry-until-approval behavior.

## Actual middleware

- Frozen Yacoub commit: `278318340bfa4e4650a97a2baba73f63bd868ed9`
- Runtime authority: actual inherited simulated middleware
- Approval readiness: off → on
- Denial readiness: off → off

No middleware copy, test double, physical hardware, or GPIO deployment was used.

## Privacy and sanitization

All Step 9 workflow exports are inactive and sanitized. No transient Wait/form resume URL, resume token, reviewer identity/email, API key, Gemini credential, account or billing data, cookie, or encryption key is committed. Request IDs are synthetic and non-private.

## Provenance

| Label | Step 9 attribution |
| --- | --- |
| `YACOUB_INHERITED` / `REFERENCE_ONLY` | original HITL specification, middleware, and inherited action/endpoint semantics |
| `SHARED_INTERFACE` | frozen action contract |
| `OBID_CREATED` | controlled policy-context transformation, safety-v2 extension, native Wait/form, pending state, human-decision processing, held-action integrity handling, approve/deny routing, timing instrumentation, `CONFIG-OBID` v3 integration, readiness evidence, and compatibility repair |

Implementing the HITL specification does not transfer authorship of Yacoub's original design.

## `CONFIG-OBID` v3 runtime-coverage limitation

The approval and denial readiness executions 71 and 73 entered through the dedicated `OBID_POLICY_INPUT` harness; they were not full Gemini-driven `CONFIG-OBID` v3 runs. The audit accepted static/executable equivalence because v3 calls the same safety-v2 logic, its embedded HITL gate parameters match the repaired harness, and Step 7 cognition is preserved unchanged. Lack of a full Gemini→HITL v3 readiness execution remains explicit.

## Retained implementation failure

The standalone subworkflow-Wait propagation failure remains engineering evidence:

```text
actual approve
→ post-wait propagation defect
→ caller cannot establish release authorization
→ fail closed
→ zero endpoint
```

It is development/readiness evidence, not final experimental evidence.

## Optional validator-agent decision

`OPTIONAL_VALIDATOR_AGENT: SKIP_FOR_CORE`

Runtime schema validation, deterministic policy, and actual HITL already constitute the core RQ2 runtime-reliability path. A validator agent would add configuration, latency, and attribution complexity; RQ1–RQ3 do not require it, while Step 10 repeated evaluation has higher methodological priority.

This is a deliberate scope decision, not an implementation failure. `CONFIG-OBID` remains a single-agent core configuration. A validator-agent extension may be reconsidered only as a separately scoped future extension that cannot disturb the frozen experiment.

## What Step 9 demonstrates

Step 9 readiness narrowly demonstrates that a real execution can persist in waiting state; a human can manually approve or deny; no endpoint executes while pending; approval releases the unchanged valid held action; denial releases nothing; invalid output stops before HITL; normal direct action bypasses HITL; the original integration failure failed closed; and human wait can be separated from automated timing.

It does not demonstrate repeated HITL effectiveness, perfect authorization reliability, production safety, completed RQ2, or population-level response timing.

## Methodological limitations

| Limitation | Meaning |
| --- | --- |
| One-off HITL observations | approval and denial are readiness checks, not repeated evidence |
| v3 runtime coverage | no full Gemini-driven `CONFIG-OBID` v3 HITL run occurred |
| Original topology | child-Wait propagation failed and required caller embedding |
| Repair verification | additional approval does not erase the retained failure |
| Human timing | individual controlled durations, not population estimates |
| Native Wait behavior | single-use/replay properties rely on n8n's runtime mechanism |
| Simulated middleware | no physical-hardware evidence |
| Provider reproducibility | prior Gemini/model limitations remain |
| No-action coverage | preserved statically, not rerun in Step 9 |
| Unrecognized context | fail-closed behavior is established mainly through deterministic implementation inspection, not a repeated matrix |
| Optional validator | deliberately not implemented |
| RQ boundary | Step 10 repetition remains necessary before answering the RQs |

## Step 5 preservation

Step 9 did not modify shared schemas, HITL A/B cases, proposal, policy context, approve/deny vocabulary, repetition counts, alternating HITL run order, timing definitions, or RQ mappings. It implements the frozen oracle rather than rewriting it.

## Step 6 preservation

All inherited baseline artifacts remain unchanged.

## Step 7 preservation

The cognitive model, prompt, tools, memory, and v1 snapshot remain unchanged.

## Step 8 preservation

The complete Step 8 snapshot remains unchanged: `CONFIG-OBID` v2, `runtime-safety-v1`, validator, policy, outcomes, harness, and Step 8 evidence. Step 9 introduced new versioned artifacts rather than rewriting Step 8.

## No Step 10 work

Step 9 did not execute five approval or denial repetitions, the alternating frozen HITL A/B schedule, five-round core evaluation, reliability percentages, RQ2 aggregate results, RQ3 latency comparison, or final result tables. All executions remain bounded implementation/readiness evidence.

## Thesis chapters supported

- Chapter 2 — HITL concepts and human-control boundaries;
- Chapter 3 — HITL readiness method and timing separation;
- Chapter 4 — HITL design and deterministic policy-context choice;
- Chapter 5 — actual Wait/form implementation and release logic;
- Chapter 6 — qualitative one-off readiness observations only;
- Chapter 7 — compatibility failure, repair, human-timing, and runtime limitations; and
- Appendix — workflows, form design, request/outcome definitions, and execution references.

## Main Step 9 artifacts

- `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`
- `safety_layer/workflows/runtime-safety-v2-hitl.json`
- `safety_layer/hitl/README.md`
- `safety_layer/hitl/configuration-manifest.md`
- `safety_layer/hitl/runtime-hitl-v1.md`
- `safety_layer/hitl/hitl-outcome-v1.md`
- `safety_layer/hitl/workflows/runtime-hitl-v1.json`
- `safety_layer/hitl/workflows/step-09-hitl-harness.json`
- `safety_layer/hitl/evidence/step-09-hitl-verification.md`

Repository checkpoints:

- Initial workflows: `b21d76d44a1d92ae6f87dba8607eb8845b3e5c70`
- Implementation/evidence: `571e367aedaac05567ae45e60fdaf8c3f041603f`
- Optional-validator documentation repair: `e4438a49200b33c0cf3adb379260d818d3a65377`

The last checkpoint changed only `safety_layer/hitl/configuration-manifest.md`; no runtime artifact, result, workflow hash, policy, HITL behavior, or predecessor artifact changed. The audit exists as Codex/thread review; no separate committed audit artifact is asserted.

## Step 10 dependency

The complete core runtime chain is now:

```text
sensor event
→ CONFIG-OBID cognition
→ candidate / no_action
→ runtime validation
→ deterministic policy

BLOCK
→ stop

ALLOW
→ inherited endpoint

APPROVAL_REQUIRED
→ actual human WAIT

approve
→ unchanged held action
→ endpoint

deny
→ no release
→ stop
```

The mandatory implementation is sufficiently complete for `Step 10 — Repeated reliability evaluation`. Step 10 must use the frozen case manifest, two core configurations, repetition counts, run-order schedule, timing boundaries, HITL approval/denial schedule, and failure-retention rules. No Step 10 implementation was begun in this note.
