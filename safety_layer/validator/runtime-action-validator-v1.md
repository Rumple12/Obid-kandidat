# Runtime Action Validator v1

**Step:** 8; **status:** implemented and one-off verified; **provenance:** `OBID_CREATED`

## Authority and scope

The validator protects the `SHARED_INTERFACE` action boundary. Its sole contract authority is [`shared_interfaces/json-schema/agent-action.schema.json`](../../shared_interfaces/json-schema/agent-action.schema.json), SHA-256 `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b`. The schema originated with Yacoub; implementing a runtime check does not transfer its authorship to Obid.

The executable implementation is the `Parse and validate frozen action schema` Code node (`n8n-nodes-base.code`, type version 2) in [`runtime-safety-v1.json`](../workflows/runtime-safety-v1.json). It is a schema-specific deterministic validator, not a general JSON Schema engine.

The pinned n8n 1.123.37 installation has no ordinary main-connection JSON Schema validator node. Its Structured Output Parser is an AI parser subnode and is not a suitable independently observable post-agent validator. JSON Schema libraries are installed transitively, but the Code-node sandbox does not allow external modules in the verified runtime configuration. A handwritten Code-node validator was therefore the smallest faithful option that did not alter the Step 3 runtime.

## Accepted candidate forms

- A JSON object is validated directly.
- A raw JSON string is parsed exactly once with `JSON.parse` and then validated.
- Failed parsing and non-object JSON terminate at the validator.
- No model retry, repair, defaulting, trimming, normalization, or type coercion occurs.
- In particular, `"false"` is not converted to `false`, and `"fan_on "` is not converted to `"fan_on"`.

Step 7's internal `no_action` envelope contains no shared action. CONFIG-OBID v2 routes it to its internal terminal before this validator.

## Frozen constraints enforced

| Constraint | Runtime enforcement |
| --- | --- |
| Root | Non-null, non-array, plain JSON object |
| Required fields | `action_id`, `target`, `reason`, `requires_approval` |
| Additional properties | Rejected (`additionalProperties: false`) |
| `action_id` | String and exactly `fan_on` or `fan_off` |
| `target` | String and exactly `fan_1` |
| `reason` | String with minimum length 1 |
| `requires_approval` | Boolean |

This is complete instance-validation parity with every constraint in the frozen action schema. It does not claim broader draft support beyond that schema.

## Observable result

The validator retains the received form, parse outcome, parsed value, complete deterministic error list, and one primary code:

```json
{
  "candidate_received": {},
  "candidate_raw_type": "object",
  "parser_status": "parsed",
  "parsed_candidate": {},
  "validation_status": "invalid",
  "schema_valid": false,
  "validation_reason_code": "MISSING_REQUIRED_FIELD",
  "validation_errors": [
    {
      "code": "MISSING_REQUIRED_FIELD",
      "path": "$.reason",
      "message": "reason is required by the frozen action contract"
    }
  ],
  "action": null
}
```

For a valid candidate, `action` is the unchanged four-field shared action. For an invalid candidate, `action` is `null`, `policy_executed` remains `false`, and the workflow terminates at `OBID_RUNTIME_VALIDATOR` without calling the policy node or middleware.

## Stable reason codes

| Code | Meaning |
| --- | --- |
| `MALFORMED_JSON` | Raw string could not be parsed as JSON |
| `NOT_OBJECT` | Parsed/root value was not a plain object |
| `MISSING_REQUIRED_FIELD` | At least one frozen required property was absent |
| `UNEXPECTED_FIELD` | At least one property was outside the frozen contract |
| `UNKNOWN_ACTION` | `action_id` was not `fan_on` or `fan_off` |
| `UNKNOWN_TARGET` | `target` was not `fan_1` |
| `INVALID_REASON` | `reason` was not a non-empty string |
| `INVALID_APPROVAL_FLAG` | `requires_approval` was not Boolean |
| `VALID_ACTION` | Every frozen constraint passed |

All detected errors are retained. The primary code uses this fixed precedence:

```text
MALFORMED_JSON
-> NOT_OBJECT
-> MISSING_REQUIRED_FIELD
-> UNEXPECTED_FIELD
-> UNKNOWN_ACTION
-> UNKNOWN_TARGET
-> INVALID_REASON
-> INVALID_APPROVAL_FLAG
-> VALID_ACTION
```

The precedence is deterministic and does not depend on model interpretation. Runtime observations are recorded in [`step-08-runtime-validation-policy.md`](../evidence/step-08-runtime-validation-policy.md).
