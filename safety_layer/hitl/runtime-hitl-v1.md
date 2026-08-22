# Runtime HITL Gate v1

**Provenance:** `OBID_CREATED`; informed by Yacoub's
`YACOUB_INHERITED` / `REFERENCE_ONLY` specification
`safety_layer/approvals/hitl-v1.md` at commit
`278318340bfa4e4650a97a2baba73f63bd868ed9`.

## Entry conditions

The gate is reached only when all of these runtime facts are true:

- the candidate passed the frozen action-schema validator;
- `validation_status` is `valid`;
- deterministic policy executed and returned `approval_required`;
- a four-field held action exists and has `requires_approval: true`;
- `released_action` is `null`;
- the policy transformation integrity check passed.

Anything else fails closed before a form exists. In particular, invalid
actions such as `fan_reverse` never enter HITL and cannot be rescued by a
human decision.

## Human interaction

The installed `n8n-nodes-base.wait` node, type version `1.1`, runs with
`resume: form` and no time limit. n8n persists the execution with status
`waiting` and `waitTill: 3000-01-01T00:00:00.000Z` until the form is submitted.

The form description displays only read-only review information:

- request ID;
- action ID, target, reason, and `requires_approval: true`;
- deterministic policy reason;
- recognized policy case.

The only decision field offers the canonical values `approve` and `deny`.
The page implements the radio choice with mutually exclusive checkbox-shaped
controls. The transport additionally supplies n8n's `submittedAt` and
`formMode` metadata. No action field is submitted by the reviewer.

## Stored-action integrity

Immediately before waiting, the workflow deep-copies the valid held action
into `held_action_snapshot`. After resume it retrieves that persisted
pre-Wait node output, not an action from the form. It compares exactly:

- `action_id`;
- `target`;
- `reason`;
- `requires_approval`.

Only an exact `approve` with an unchanged held action authorizes release. The
released action remains `requires_approval: true`; approval is separate
runtime metadata. `deny`, an invalid decision, unexpected submitted fields,
or an integrity failure releases `null`.

## Request identity and single use

The non-private request identifier is `hitl-<execution-id>`. n8n disables a
completed waiting form before resuming that execution, so reopening its URL
does not execute the action again. Execution-specific form URLs are transient
and are never committed.

## Pinned-runtime compatibility repair

The original execution placed this Wait gate in the standalone
`runtime-hitl-v1` subworkflow. The child correctly waited, recorded the human
decision, and produced the approved action, but n8n `1.123.37` resumed the
parent Execute Sub-workflow node with its original pre-wait input instead of
the child's completed output. The parent consequently failed closed.

The final Step 9 implementation embeds the same precondition, request,
Wait/form, finalization, and integrity nodes directly in:

- `safety_layer/hitl/workflows/step-09-hitl-harness.json`;
- `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`.

This is a compatibility placement change only. It does not change the shared
contract, validator, deterministic policy, policy context, decision values,
or endpoint-release invariant.

## Timing

The implementation retains `hitl_flow_started_at`, `approval_requested_at`,
`approval_decided_at`, and `hitl_completed_at`, and derives separate
pre-wait automation, human-wait, post-decision automation, and total elapsed
durations. Human wait is excluded from the later automated RQ3 comparison.
