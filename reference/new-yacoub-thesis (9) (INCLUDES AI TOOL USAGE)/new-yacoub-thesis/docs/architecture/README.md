# Architecture overview

This folder contains the high-level architecture summary for the **new-yacoub** thesis system.

The thesis is intentionally built around **one small, complete, end-to-end IoT scenario** so that it stays measurable, explainable, and finishable within the available time.

## Core system flow

```text
Sensor event
  -> Middleware
  -> n8n workflow
  -> Validation / Approval
  -> Action execution
  -> Metrics logging
```

## Current intended scenario

```text
Temperature event
  -> Python middleware receives or generates the event
  -> Middleware pushes the event to n8n through webhook flow
  -> n8n evaluates whether fan action is needed
  -> Safety layer validates the output
  -> Approval is required if the action is risky or malformed
  -> Middleware executes /fan/on or /fan/off
  -> Latency and resource metrics are recorded
```

## Main design principle

The system is split into small layers with a clear contract boundary.

This is done to:

- keep the thesis narrow
- reduce scope creep
- make implementation testable
- make the report easier to explain
- prevent workflow logic from directly controlling hardware behavior without checks

## Top-level folder responsibilities

### `infrastructure/`

Contains runtime and deployment-related material.

Purpose:

- local self-hosted n8n baseline
- Docker configuration
- Raspberry Pi deployment assumptions
- monitoring hooks or runtime notes

### `middleware/`

Contains the Python bridge between sensors/actions and n8n.

Purpose:

- receive or generate sensor events
- expose endpoints such as `/status`, `/fan/on`, and `/fan/off`
- push events into n8n through webhook flow
- act as the controlled execution layer for hardware-facing actions

### `cognitive_logic/`

Contains the minimum workflow logic required for integration.

Purpose:

- one workflow
- one prompt set
- one memory choice

In **new-yacoub**, this is minimum integration only. It is not a full cognitive architecture project.

### `safety_layer/`

Contains the minimum safety logic required for the integrated system.

Purpose:

- validate workflow output
- decide whether approval is required
- block malformed or unsafe actions
- preserve one safe case and one blocked case for evaluation

Current Step 8 safety artifacts:

- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`
- `safety_layer/examples/risky-approval-case.md`

### `shared_interfaces/`

This is the **contract boundary** between middleware and workflow/safety logic.

Purpose:

- define sensor-event schemas
- define action schemas
- store example payloads
- prevent schema drift

This is where Yacoub's runtime side and the minimum Obid-compatible layer meet.

Current Step 5 contract artifacts:

- `shared_interfaces/json-schema/sensor-event.schema.json`
- `shared_interfaces/json-schema/agent-action.schema.json`
- `shared_interfaces/examples/sensor-event.example.json`
- `shared_interfaces/examples/fan-on.example.json`
- `shared_interfaces/examples/blocked-action.example.json`

### `evaluation/`

Contains the measurement and result material that will feed the thesis report.

Purpose:

- datasets or fixtures
- metrics output
- result files
- baseline-vs-agent comparison evidence

### `docs/`

Contains planning, scope, decision, and report-support material.

Purpose:

- lock the narrowed scope
- document architecture decisions
- support report writing
- keep AI tools aligned with thesis boundaries

## Contract boundary

The most important architectural boundary in this thesis is:

```text
Middleware <-> Shared Interfaces <-> Workflow / Safety logic
```

### Input side

Middleware creates or receives sensor events and represents them using a shared schema.

Concrete input schema:

- `shared_interfaces/json-schema/sensor-event.schema.json`

### Output side

Workflow logic produces a proposed action using a shared schema.

Concrete output schema:

- `shared_interfaces/json-schema/agent-action.schema.json`

### Safety rule

No risky or malformed action may reach middleware execution without passing validation and, when needed, approval.

Step 8 defines this as a minimum safety design and case documentation layer. It
does not claim production-grade runtime enforcement unless later implementation
and test evidence is added.

## Current communication model

The first implementation uses a push-based communication flow:

- middleware pushes events to n8n through webhook flow
- n8n does not poll middleware in the first version

## Scope note

This architecture is intentionally designed for:

- one complete vertical slice
- one measurable scenario
- one deterministic baseline
- one minimal agent-enhanced path

It is not currently intended to support broad multi-agent expansion, many devices, or deep n8n internals work.
