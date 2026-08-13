# Step 08 - Minimum Safety Layer

## What was built

- A minimum Step 8 safety design/specification layer was added under `safety_layer/`.
- The safety layer defines a narrow action policy for the first temperature-to-fan scenario.
- A parser/validation design describes how workflow or agent output should be checked before middleware routing.
- A lightweight human-in-the-loop approval design describes when a reviewer may approve or reject an action.
- Three example cases were documented:
  - allowed valid action
  - blocked malformed action
  - risky or unknown action requiring review and expected rejection

This step documents the intended safety boundary. It does not implement a production-grade safety framework.

## Why it matters for the thesis

Step 8 makes the workflow-to-middleware boundary academically defensible by specifying that workflow-produced actions should not directly trigger middleware endpoints unless they pass validation and, when needed, human approval.

It supports the narrowed thesis scope by providing exactly one minimal validation/approval path for one action family: `fan_on` and `fan_off` targeting `fan_1`. This keeps the Obid-compatible layer small while giving the report concrete safety cases to discuss.

## Evidence produced

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`
- `safety_layer/examples/risky-approval-case.md`
- `docs/architecture/README.md`
- `docs/ongoing/integration-contract.md`
- `shared_interfaces/json-schema/agent-action.schema.json`

The safety design is based on the Step 5 action schema:

- required fields: `action_id`, `target`, `reason`, `requires_approval`
- allowed actions: `fan_on`, `fan_off`
- allowed target: `fan_1`
- no additional fields allowed

## Safety Cases

Allowed case:

- Example file: `safety_layer/examples/allowed-case.md`
- Input action: `fan_on`, target `fan_1`, non-empty reason, `requires_approval: false`
- Expected decision: allow after validation
- Expected middleware endpoint after validation: `POST /fan/on`

Blocked case:

- Example file: `safety_layer/examples/blocked-case.md`
- Input action includes `action_id` and `target` only
- Missing fields: `reason`, `requires_approval`
- Expected decision: block
- Expected middleware endpoint: none

Risky/approval case:

- Example file: `safety_layer/examples/risky-approval-case.md`
- Input action: `open_window`, target `unknown_device`, `requires_approval: true`
- Reason it is risky: unknown action, unknown target, outside the first scenario
- Expected minimum-policy behavior: reject for direct execution; it may be shown to a human reviewer for explanation/evidence
- Expected middleware endpoint: none

## Report chapters it feeds

- Chapter 5 - Implementation: safety policy, validation design, HITL approval design, and documented safety cases.
- Chapter 6 - Results: later allowed/blocked/risky case outcomes once Step 9 runtime evaluation exists.
- Chapter 7 - Discussion: safety limitations, human approval tradeoffs, blocked-case interpretation, and why this is a minimum thesis-scoped safety layer.

## Limitations or assumptions

- Step 8 is a minimum safety design/specification layer.
- The files document intended validation and approval behavior; they do not prove runtime enforcement.
- Middleware runtime enforcement is not claimed here.
- No production-grade safety framework is implemented.
- No runtime approval UI or operational approval system is implemented.
- Unknown actions and unknown targets are not allowed to execute under policy v1.
- Human approval cannot turn an unknown action or unknown target into a middleware call under policy v1.
- The middleware fan endpoints remain simulated at this stage.
- Runtime measurement and evaluation belong to Step 9.
- No latency, RAM, CPU, thermal/resource, or repeated-run safety outcome measurements are produced by this step.

## Screenshots/logs still needed

- Runtime validation logs showing allowed actions passing validation.
- Runtime validation logs showing malformed actions being blocked.
- Runtime approval or rejection logs for risky/unknown output.
- Evidence that blocked and risky cases do not call `/fan/on` or `/fan/off`.
- Step 9 evaluation results for safe vs blocked action behavior.
- Any UI or workflow screenshots if a human approval checkpoint is later implemented in n8n or middleware.
