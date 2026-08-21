# Step 5 shared-contract freeze

**Freeze date:** 2026-08-21

**Authoritative repository:** `Rumple12/new-yacoub-thesis`

**Authoritative commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`

**Status:** Exact active copies adopted and verified with no drift

## Adoption and integrity record

| Contract | Frozen source path | Active Obid path | Source SHA-256 | Destination SHA-256 | Verdict | Provenance |
| --- | --- | --- | --- | --- | --- | --- |
| Sensor event | `shared_interfaces/json-schema/sensor-event.schema.json` | `shared_interfaces/json-schema/sensor-event.schema.json` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` | `416cec7d396912672171e1fbfdce828820017c9218e2c418de3f784e329ee007` | Exact byte copy; no drift | `SHARED_INTERFACE`; source design/authorship remains `YACOUB_INHERITED` |
| Agent action | `shared_interfaces/json-schema/agent-action.schema.json` | `shared_interfaces/json-schema/agent-action.schema.json` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | Exact byte copy; no drift | `SHARED_INTERFACE`; source design/authorship remains `YACOUB_INHERITED` |

The source bytes were read from the frozen Git objects rather than from a dirty or line-ending-converted working tree. Both source blobs and active copies use LF line endings and a final newline. Adoption makes the files active collaboration interfaces; it does not transfer authorship to Obid.

## Sensor-event constraints

Schema metadata:

- JSON Schema dialect: `https://json-schema.org/draft/2020-12/schema`
- schema identifier: `https://new-yacoub-thesis.local/shared_interfaces/json-schema/sensor-event.schema.json`
- root type: `object`
- required fields, in frozen order: `sensor_id`, `timestamp`, `type`, `value`, `unit`
- `additionalProperties`: `false`

| Property | Required | Frozen type | Const/enum | Format or other constraint |
| --- | --- | --- | --- | --- |
| `sensor_id` | Yes | `string` | None | `minLength: 1` |
| `timestamp` | Yes | `string` | None | `format: date-time` |
| `type` | Yes | `string` | `const: temperature` | None |
| `value` | Yes | `number` | None | No minimum, maximum, or other numeric bound |
| `unit` | Yes | `string` | `const: C` | None |

## Agent-action constraints

Schema metadata:

- JSON Schema dialect: `https://json-schema.org/draft/2020-12/schema`
- schema identifier: `https://new-yacoub-thesis.local/shared_interfaces/json-schema/agent-action.schema.json`
- root type: `object`
- required fields, in frozen order: `action_id`, `target`, `reason`, `requires_approval`
- `additionalProperties`: `false`

| Property | Required | Frozen type | Const/enum | Format or other constraint |
| --- | --- | --- | --- | --- |
| `action_id` | Yes | `string` | `enum: fan_on, fan_off` | None |
| `target` | Yes | `string` | `enum: fan_1` | None |
| `reason` | Yes | `string` | None | `minLength: 1`; exact wording is not constrained |
| `requires_approval` | Yes | `boolean` | Both Boolean values are valid | None |

The action schema has no risk field, no `no_action` action, and no alternative target. A valid action with `requires_approval: true` remains schema-conforming.

## Preserved semantics outside the schemas

The following inherited collaboration semantics are preserved but are not JSON Schema constraints:

```text
value >= 30.0 C -> fan_on
otherwise       -> fan_off

fan_on  -> POST /fan/on
fan_off -> POST /fan/off
```

Internal Obid policy, validation, memory, HITL, and evaluation metadata must adapt around these contracts. They may not add fields or action IDs to the shared schemas. Any future contract version or semantic change requires explicit architectural approval and a documented decision; none is authorized by this freeze.
