# Output Validation v1

This file describes the minimum parser and validation behavior for Step 8.

Status: **documentation/specification-level validation design only**.

No runtime validation library or production safety framework is implemented in
this step.

## Goal

The validator protects the boundary between workflow-produced action output and
middleware action execution.

Only a validated action may move toward a middleware endpoint.

## Input

The validator receives raw workflow or agent output.

Expected action shape:

```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```

## Minimum Validation Logic

1. Parse the output as JSON.
2. Verify the parsed value is a JSON object.
3. Verify required fields exist:
   - `action_id`
   - `target`
   - `reason`
   - `requires_approval`
4. Verify no unexpected fields are present.
5. Verify `action_id` is one of:
   - `fan_on`
   - `fan_off`
6. Verify `target` is:
   - `fan_1`
7. Verify `reason` is a non-empty string.
8. Verify `requires_approval` is boolean.
9. If `requires_approval` is `false`, pass the allowed action forward.
10. If `requires_approval` is `true`, route the valid action to HITL review.

## Rejection Rules

Reject and block when:

- JSON is malformed
- the parsed value is not an object
- required fields are missing
- unexpected fields exist
- `action_id` is unknown
- `target` is unknown
- `reason` is missing or empty
- `requires_approval` is not boolean
- the action does not match `shared_interfaces/json-schema/agent-action.schema.json`

Rejected output must not reach middleware.

## Minimal Pseudocode

```text
parse raw_output as JSON
if parse fails:
    block malformed_json

if required fields missing:
    block missing_required_field

if unexpected fields exist:
    block unexpected_field

if action_id not in [fan_on, fan_off]:
    block unknown_action

if target != fan_1:
    block unknown_target

if requires_approval is not boolean:
    block invalid_approval_flag

if requires_approval == true:
    route to HITL checkpoint

otherwise:
    pass validated action to middleware routing
```

## Middleware Routing After Validation

Only after validation:

- `fan_on` may route to `POST /fan/on`
- `fan_off` may route to `POST /fan/off`

The validator must never route free-form text, unknown actions, or unknown
targets into middleware.

## Scope Note

This is a minimal validation design for the thesis. It is not broad guardrail
research, model alignment work, or a complete runtime safety framework.
