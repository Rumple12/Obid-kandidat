# Action Policy v1

This is the minimum Step 8 action policy for the new-yacoub thesis system.

Status: **documentation/specification-level safety boundary only**.

This file does not implement runtime enforcement by itself. It defines the
minimum policy that later workflow or middleware logic must follow before any
workflow-produced action can reach a middleware fan endpoint.

## Scope

This policy is intentionally narrow:

- one scenario
- one target actuator
- two allowed fan actions
- one approval checkpoint
- no broad guardrail framework
- no multi-agent safety architecture
- no direct hardware access

## Required Contract

Every workflow-produced action must match:

```text
shared_interfaces/json-schema/agent-action.schema.json
```

Required fields:

- `action_id`
- `target`
- `reason`
- `requires_approval`

Allowed `action_id` values:

- `fan_on`
- `fan_off`

Allowed `target`:

- `fan_1`

`requires_approval` must be a boolean.

No additional fields are allowed by the shared action schema.

## Direct Hardware Rule

Direct hardware access is never allowed from workflow or agent output.

Allowed execution path:

```text
workflow output
  -> validation / parser
  -> approval checkpoint if required
  -> middleware endpoint
  -> simulated or future hardware-facing action
```

Disallowed execution paths:

- workflow output directly controlling GPIO
- agent output containing shell commands
- agent output inventing hardware instructions
- unknown device or action routed directly to middleware

## Policy Decisions

### Allowed Without Human Approval

An action may proceed to middleware only when all of these are true:

- output parses as JSON
- output matches `agent-action.schema.json`
- `action_id` is `fan_on` or `fan_off`
- `target` is `fan_1`
- `requires_approval` is `false`

Allowed middleware endpoints after validation:

- `fan_on` -> `POST /fan/on`
- `fan_off` -> `POST /fan/off`

### Human Approval Required

A schema-valid action requires the HITL checkpoint when:

- `requires_approval` is `true`
- the action is valid but the reviewer wants manual confirmation before execution

Approval can only release an action that already matches the shared contract and
the allowed action/target sets.

### Blocked

An action must be blocked when:

- JSON is malformed
- required fields are missing
- `requires_approval` is not boolean
- `action_id` is unknown
- `target` is unknown
- the output contains unexpected fields
- the action does not match `agent-action.schema.json`

Blocked actions must not reach middleware.

### Risky Or Unknown Output

Risky or unknown output must require human review or be rejected.

For policy v1, unknown actions and unknown targets are rejected for direct
execution. They may be shown to a human reviewer for evidence and explanation,
but the reviewer must not approve them into middleware unless they are rewritten
as a valid contract action in a later, explicitly documented step.

## Runtime Enforcement Note

This Step 8 artifact defines the minimum safety design. It is not a production
safety framework and it does not claim runtime enforcement unless a later
implementation adds and tests enforcement logic.
