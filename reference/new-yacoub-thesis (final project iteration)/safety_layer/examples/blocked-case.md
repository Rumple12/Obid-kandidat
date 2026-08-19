# Blocked Case

This example documents one malformed/invalid action for Step 8.

## Input Action

```json
{
  "action_id": "fan_on",
  "target": "fan_1"
}
```

## Why It Is Blocked

This action is blocked because required fields are missing:

- `reason`
- `requires_approval`

It does not match:

```text
shared_interfaces/json-schema/agent-action.schema.json
```

## Expected Decision

Decision:

```text
block
```

The action must not reach middleware.

## Middleware Endpoint

No middleware endpoint may be called.

Specifically, the system must not call:

- `POST /fan/on`
- `POST /fan/off`

## Runtime Enforcement Note

This case documents the expected safety decision. It does not prove runtime
enforcement unless a later workflow or middleware implementation executes and
logs the validation step.
