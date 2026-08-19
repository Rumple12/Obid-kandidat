# Future Handoff Verification Checklist

**Created:** Step 2

**Status:** Future checks only. No runtime, schema adoption, baseline import, or evaluation check in this file has been executed during Step 2.

## How to use this checklist

- Perform a check only in its assigned numbered step.
- Record exact configuration, command/UI action, observed result, evidence path, and provenance.
- Keep failed and partial checks visible.
- Do not tick an item based on inherited documentation alone.
- Stop for an explicit decision if compatibility requires changing locked semantics.

## Provenance prerequisite before later adoption

- [ ] **`[CHECK-PROV-01]` Before Step 5/6 adoption:** Use `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9` and exact source paths as authority; do not use the dirty/pruned local nested working-tree state as an exact checkout.
- [ ] **`[CHECK-PROV-02]` Before any active copy:** Record origin, frozen path, provenance label, reason for adoption, destination path, and comparison/repair result.

The local nested reference state has been documented in Step 2. Whether it was intentionally pruned cannot be established from repository contents and does not authorize cleaning or modifying `reference/`.

## Step 3 - Obid n8n runtime compatibility

- [ ] **`[CHECK-S3-01]` Exact Obid n8n version:** Record image/package identifier, resolved version, configuration source, and evidence path.
- [ ] **`[CHECK-S3-02]` Frozen-version comparison:** Compare the Obid runtime with Yacoub's pinned `n8nio/n8n:1.123.37` without silently upgrading or changing assumptions.
- [ ] **`[CHECK-S3-03]` Required node availability:** Verify the built-in and LangChain node types needed to import/reproduce the inherited workflows.
- [ ] **`[CHECK-S3-04]` Compatibility decision:** Record any unavoidable version/configuration deviation and whether it preserves interface/baseline semantics.

Step 3 evidence should identify the new runtime as `OBID_CREATED`. Matching a Yacoub version/configuration does not transfer authorship.

## Step 4 - Integration boundary

- [ ] **`[CHECK-S4-01]` Obid webhook path:** Record the exact test/active webhook path and mode used by the Step 4 boundary.
- [ ] **`[CHECK-S4-02]` `N8N_WEBHOOK_URL`:** Verify the configured forwarding destination end to end without exposing secrets.
- [ ] **`[CHECK-S4-03]` Middleware reachability:** Record host/container addressing and prove the collaborator-provided middleware boundary is reachable.
- [ ] **`[CHECK-S4-04]` `GET /status`:** Verify the documented status/state response and retain evidence.
- [ ] **`[CHECK-S4-05]` `POST /sensor-event`:** Verify a locked compatible sensor event is accepted/forwarded as documented.
- [ ] **`[CHECK-S4-06]` `POST /fan/on`:** Verify the simulated `fan_on` behavior and endpoint mapping.
- [ ] **`[CHECK-S4-07]` `POST /fan/off`:** Verify the simulated `fan_off` behavior and endpoint mapping.
- [ ] **`[CHECK-S4-08]` No competing middleware:** Confirm no Obid middleware architecture was introduced. If a substitute was unavoidable and explicitly authorized, label it `TEST_DOUBLE` and document fidelity/limits.

## Step 5 - Shared contracts and evaluation-boundary preparation

- [ ] **`[CHECK-S5-01]` Sensor schema adoption:** Adopt or immutably reference `shared_interfaces/json-schema/sensor-event.schema.json` from the frozen commit with `SHARED_INTERFACE` provenance.
- [ ] **`[CHECK-S5-02]` Sensor schema verification:** Compare exact fields, types, constants, required fields, and additional-properties behavior with the frozen source.
- [ ] **`[CHECK-S5-03]` Action schema adoption:** Adopt or immutably reference `shared_interfaces/json-schema/agent-action.schema.json` from the frozen commit with `SHARED_INTERFACE` provenance.
- [ ] **`[CHECK-S5-04]` Action schema verification:** Compare exact fields, types, allowed actions, target, required fields, and additional-properties behavior with the frozen source.
- [ ] **`[CHECK-S5-05]` No schema drift:** Produce an exact comparison or documented compatibility result; do not silently change either contract.
- [ ] **`[CHECK-S5-06]` Valid risky case:** Define a schema-conforming action with `requires_approval: true` without widening `fan_on`/`fan_off`, `fan_1`, or the schema.

Actual case definitions, datasets, expected outcomes, evidence formats, and repetition rules are Step 5 work and do not exist in Step 2.

## Step 6 - Inherited comparison baselines

- [ ] **`[CHECK-S6-01]` Deterministic reproducibility:** Import/reproduce the inherited deterministic baseline with exact provenance and the locked `value >= 30.0 C` rule.
- [ ] **`[CHECK-S6-02]` Deterministic high/low/boundary behavior:** Verify all three branches/conditions required by the active Step 6 plan and retain new Obid verification evidence.
- [ ] **`[CHECK-S6-03]` Minimal-agent reproducibility:** Import/recreate the minimal compatible agent baseline without adding Obid ReAct, memory, validation, policy, or HITL behavior.
- [ ] **`[CHECK-S6-04]` Connected Google model node:** Recover or create a reproducible baseline export/configuration containing the connected Google model node shown by Yacoub evidence.
- [ ] **`[CHECK-S6-05]` Exact Gemini configuration:** Record exact model name/version, credential-independent node settings, and generation parameters. Do not store credentials.
- [ ] **`[CHECK-S6-06]` Stateless baseline:** Verify no memory node/state mechanism is connected and label the choice `YACOUB_INHERITED`.
- [ ] **`[CHECK-S6-07]` Minimal-agent high/low/boundary behavior:** Reconfirm expected outputs through the shared action/middleware boundary.
- [ ] **`[CHECK-S6-08]` Compatibility repairs:** Record any necessary active-copy repair, original source, reason, semantic impact, and evidence. Never modify the frozen source.

## Locked semantics used by every future check

Sensor event:

- `sensor_id`, `timestamp`, `type`, `value`, `unit`
- `type = temperature`
- `unit = C`

Agent action:

- `action_id`, `target`, `reason`, `requires_approval`
- `fan_on`, `fan_off`
- `fan_1`

Middleware:

- `GET /status`
- `POST /sensor-event`
- `POST /fan/on`
- `POST /fan/off`

Inherited threshold:

- `value >= 30.0 C -> fan_on`
- otherwise `fan_off`
