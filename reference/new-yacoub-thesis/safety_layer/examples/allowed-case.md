# Allowed Case

This example documents one valid allowed action for Step 8.

## Input Action

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```

## Why It Is Allowed

This action is allowed because:

- the JSON is well formed
- all required fields are present
- `action_id` is `fan_on`
- `target` is `fan_1`
- `reason` is a non-empty string
- `requires_approval` is boolean
- `requires_approval` is `false`
- the action matches `shared_interfaces/json-schema/agent-action.schema.json`

## Middleware Endpoint After Validation

After validation, this action may reach:

```text
POST /fan/on
```

In the Dockerized n8n workflow this corresponds to:

```text
http://host.docker.internal:8000/fan/on
```

## Runtime Enforcement Note

This case documents the expected safety decision. It does not prove runtime
enforcement unless a later workflow or middleware implementation executes and
logs the validation step.
