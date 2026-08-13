# Step 05 - Shared Contract

## What was built

- A minimal shared contract layer was added under `shared_interfaces/`.
- The input-side sensor event schema defines the first scenario's temperature-event payload.
- The output-side action schema defines the minimal fan action contract for workflow-produced actions.
- Example payloads were added for one valid sensor event, one valid fan-on action, and one negative blocked-action case.
- `docs/ongoing/integration-contract.md` was updated to describe the contract boundary between middleware, shared interfaces, workflow logic, and later safety validation.
- `docs/architecture/README.md` was updated to list the Step 5 contract artifacts.

## Why it matters for the thesis

This step makes the boundary between Yacoub's runtime side and the minimum Obid-compatible workflow/safety side explicit. It supports the thesis by reducing schema drift, making the middleware-to-workflow interface reportable, and preparing a clear place where later validation and approval behavior can be tested.

The contract also keeps the project narrow: it defines one temperature-event path, one fan-action path, and one small set of allowed action and target values.

## Evidence produced

- `shared_interfaces/json-schema/sensor-event.schema.json`
- `shared_interfaces/json-schema/agent-action.schema.json`
- `shared_interfaces/examples/sensor-event.example.json`
- `shared_interfaces/examples/fan-on.example.json`
- `shared_interfaces/examples/blocked-action.example.json`
- `docs/ongoing/integration-contract.md`
- `docs/architecture/README.md`

The contract currently defines:

- sensor event required fields: `sensor_id`, `timestamp`, `type`, `value`, `unit`
- supported sensor type: `temperature`
- supported unit: `C`
- action required fields: `action_id`, `target`, `reason`, `requires_approval`
- initially allowed actions: `fan_on`, `fan_off`
- initially allowed target: `fan_1`

`blocked-action.example.json` is a negative example for later safety testing. It uses `open_window` and `unknown_device`, which are outside the Step 5 allowed action and target sets.

## Report chapters it feeds

- Chapter 4 - Choice of approach: why a schema-based contract boundary is used instead of informal payloads.
- Chapter 5 - Implementation: shared interface files, sensor-event schema, action schema, example payloads, and contract boundary.
- Chapter 7 - Discussion: limitations of contract-only design before runtime enforcement and safety handling.

## Limitations or assumptions

- Step 5 defines schemas and examples only.
- Runtime JSON Schema enforcement is not implemented yet.
- Safety logic is not implemented yet.
- Human approval handling is not implemented yet.
- The Step 4 middleware still uses its minimal inline validation, not the shared JSON schemas.
- `blocked-action.example.json` is not evidence that unsafe output is blocked at runtime; it is a prepared negative example for later Step 8 safety-layer testing.
- Actual enforcement of malformed, risky, or unsupported actions is deferred to Step 8.
- No n8n workflow is claimed to produce or consume these contract payloads yet.
- No latency, resource, or safety outcome measurements are produced by this step.

## Screenshots/logs still needed

- Runtime validation logs once JSON Schema enforcement is connected.
- Safety-layer logs showing the negative blocked-action example being rejected or routed to approval in Step 8.
- n8n workflow evidence showing payloads that follow the shared contract.
- Evaluation records showing allowed and blocked outcomes after enforcement exists.
