# Safety Outcome v1

**Step:** 8; **provenance:** `OBID_CREATED`

This document defines the stable internal result returned by [`runtime-safety-v1.json`](../workflows/runtime-safety-v1.json). It is runtime metadata, not a shared contract and not a replacement for `agent-action.schema.json`.

## Result sections

| Section | Fields | Purpose |
| --- | --- | --- |
| Trace | `evidence_id`, `injection_point`, `source` | Identifies the bounded run and input seam |
| Candidate | `candidate_received`, `candidate_raw_type`, `parser_status`, `parsed_candidate` | Preserves observable input and parse behavior |
| Validation | `validation_status`, `schema_valid`, `validation_reason_code`, `validation_errors`, `action` | Reports exact frozen-contract validation |
| Policy | `policy_executed`, `policy_decision`, `policy_reason_code`, `released_action`, `held_action` | Reports deterministic release, block, or hold |
| Terminal | `safety_decision`, `terminal_stage`, `endpoint_reached` | Records where processing stopped |

`validation_errors` retains every detected error as an object with stable `code`, JSON-style `path`, and `message`; parse failures may also carry a parser `detail`. No hidden chain-of-thought or model scratchpad is collected.

## Terminal outcomes

| Outcome | Required state | Terminal stage | Endpoint behavior |
| --- | --- | --- | --- |
| Validation block | `schema_valid: false`, `policy_executed: false` | `OBID_RUNTIME_VALIDATOR` | `/fan/on: 0`, `/fan/off: 0` |
| Policy block | `schema_valid: true`, `policy_decision: block` | `OBID_RUNTIME_POLICY` | `/fan/on: 0`, `/fan/off: 0` |
| Approval hold | `schema_valid: true`, `policy_decision: approval_required` | `OBID_APPROVAL_REQUIRED_PENDING_STEP9` | `/fan/on: 0`, `/fan/off: 0` |
| Allow | `schema_valid: true`, `policy_decision: allow` | `OBID_RUNTIME_POLICY_ALLOW` | Exactly the endpoint mapped by the released action |

The caller adds `routing_status`, middleware response, and final `endpoint_reached` only after routing. The reusable safety subworkflow itself never calls middleware.

## Internal no-action

Step 7's envelope may contain `decision: no_action` and `action: null`. CONFIG-OBID v2 terminates this at `internal_no_action` before the safety subworkflow. Absence of a shared action is not a schema error and does not introduce a shared `no_action` action ID.

## Boundary

`approval_required` is a hold outcome only. This version defines no approval request, human decision, release, denial, or timing behavior. Those are explicitly outside Step 8.
