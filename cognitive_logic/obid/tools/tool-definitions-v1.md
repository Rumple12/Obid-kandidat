# CONFIG-OBID tool definitions v1

**Provenance:** `OBID_CREATED` implementations preserving
`YACOUB_INHERITED` threshold and `SHARED_INTERFACE` action semantics.

Exactly two tools are connected to the single Step 7 agent.

## `temperature_threshold_tool`

- n8n node: `@n8n/n8n-nodes-langchain.toolCode`, type version `1.3`.
- Input: an object containing numeric `value` and `unit: "C"`.
- Output: a JSON string describing `threshold_c`, `relation`,
  `desired_action`, and `desired_fan_state`.
- Rule: `value >= 30.0 C` maps to `fan_on`/`on`; otherwise it maps to
  `fan_off`/`off`.
- Controls: deterministic, read-only, exactly one call per valid event. It does
  not call middleware, change memory, validate a shared action, or implement
  policy/HITL.

## `fan_status_tool`

- n8n node: `@n8n/n8n-nodes-langchain.toolWorkflow`, type version `2.2`,
  containing one minimal inline read-only subworkflow. The installed legacy
  HTTP Tool was rejected by the pinned routing engine at runtime, so the
  supported Workflow Tool fallback is required.
- Input: the literal target `fan_1`; it never controls the URL or selects a
  different target.
- Inline path: Execute Workflow Trigger -> ordinary HTTP Request
  `GET http://host.docker.internal:8000/status` -> deterministic normalization.
  The request has no authentication, query, or body.
- Output: `target`, `fan_state`, `simulated`, and `source: yacoub_status`, all
  derived from the inherited `state.fan` and `state.hardware` response values.
- Controls: at most one call, and only when the latest bounded memory contains
  no usable `state_after`. It never calls `/fan/on` or `/fan/off`, approves an
  action, or implements validation/policy.

No recursive tool, generic tool platform, dynamic tool creation, or third tool
is part of CONFIG-OBID. The status subworkflow cannot call the agent or either
fan action endpoint.
