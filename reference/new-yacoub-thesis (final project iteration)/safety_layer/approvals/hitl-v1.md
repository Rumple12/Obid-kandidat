# Human-In-The-Loop Approval v1

This file defines the lightweight Step 8 human approval checkpoint.

Status: **documentation/specification-level approval design only**.

No runtime approval UI or production approval system is implemented in this
step.

## When Approval Is Required

Human review is required when:

- a schema-valid action has `requires_approval: true`
- a valid action should be manually confirmed before execution
- risky or unknown output needs an explicit rejection record

Malformed JSON, missing fields, unknown actions, and unknown targets must not
reach middleware directly.

## What The Reviewer Checks

The reviewer checks:

- output is valid JSON
- required fields are present
- `action_id` is `fan_on` or `fan_off`
- `target` is `fan_1`
- `requires_approval` is boolean
- the action is appropriate for the current temperature event
- no direct hardware instruction or invented device is present

## Reviewer Decisions

Allowed decisions:

- `approve`
- `reject`

## After Approval

Approval may release the action only if it already matches the shared contract:

- valid `action_id`
- valid `target`
- valid required fields
- no unexpected fields

Approved valid actions may continue to middleware routing:

- `fan_on` -> `POST /fan/on`
- `fan_off` -> `POST /fan/off`

Approval does not permit unknown actions or unknown targets to bypass policy.

## After Rejection

Rejected output:

- is not sent to middleware
- is recorded as blocked/rejected evidence
- may be used in Chapter 6 or Chapter 7 discussion

## Unknown Or Risky Output

Unknown actions such as `open_window` or unknown targets such as
`unknown_device` are not allowed to execute in policy v1.

They may be shown to the human reviewer, but the expected minimum-policy
decision is `reject`.

## Scope Note

This HITL design is intentionally lightweight and thesis-scoped. It exists to
show a clear safety boundary, not to implement a broad operational approval
platform.
