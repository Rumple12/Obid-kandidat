# Step 8 Runtime Safety Configuration Manifest

**Configuration:** `CONFIG-OBID`, Step 8 runtime-safety version; **runtime:** n8n `1.123.37`, container `obid-n8n`; **date verified:** 2026-08-22; **provenance of new artifacts:** `OBID_CREATED`

## Frozen authorities

| Authority | Provenance | Version/hash | Step 8 use |
| --- | --- | --- | --- |
| `shared_interfaces/json-schema/agent-action.schema.json` | `SHARED_INTERFACE`; Yacoub-originated | SHA-256 `55f0cb93e933a0791aab50a2430ed8afa9372b5ca576405e2f4b8d4bb4048d5b` | Exact runtime validation authority; unchanged |
| `cognitive_logic/obid/workflows/obid-agent-v1.json` | `OBID_CREATED`, frozen Step 7 snapshot | SHA-256 `7e26e8c36786d75cf5e3d8a6f3bc496aea389495eac6d2c1df374476b4de4a17` | Cognitive source retained unchanged |
| Frozen Yacoub safety specifications | `YACOUB_INHERITED` / `REFERENCE_ONLY` | Repository `Rumple12/new-yacoub-thesis`, commit `278318340bfa4e4650a97a2baba73f63bd868ed9` | Design provenance only; not runtime evidence |

The inspected Yacoub specification paths were:

- `safety_layer/parsers/output-validation-v1.md`
- `safety_layer/policies/action-policy-v1.md`
- `safety_layer/approvals/hitl-v1.md`
- `safety_layer/examples/allowed-case.md`
- `safety_layer/examples/blocked-case.md`
- `safety_layer/examples/risky-approval-case.md`

## Portable artifacts

| Path | Workflow name | Stable ID | Nodes | SHA-256 | Export state |
| --- | --- | --- | ---: | --- | --- |
| `cognitive_logic/obid/workflows/obid-agent-v2-safety.json` | `CONFIG-OBID - Single Agent v2 Safety` | `obid-agent-v2-safety` | 25 | `c8f725da7c11013fd96740ebdfcb5f738d5e399e10f69e747aa9e2e1aee3dfdf` | Sanitized, `active: false` |
| `safety_layer/workflows/runtime-safety-v1.json` | `Step 8 - Runtime safety v1` | `runtime-safety-v1` | 10 | `d179f0f4b3ef3977ab65456cc172854176e9dc56336a43e87b9bf92fea3ee378` | Sanitized, `active: false` |
| `safety_layer/workflows/step-08-safety-harness.json` | `Step 8 - Safety readiness harness` | `step-08-safety-harness` | 14 | `4417a3e66a6dc0d09b1e9318bfe7f308c2ec6a52f96ffe00ff04a0a5151a9c0c` | Sanitized, `active: false` |

No credential identity, secret, owner data, cookie, or private session token is present in the exports or evidence. The evidence records only two synthetic, non-authentication CONFIG-OBID test session IDs. The live CONFIG-OBID v2 model node uses the already attached private runtime credential; only its presence was verified.

## Runtime node choices

| Function | Node | Type/version |
| --- | --- | --- |
| Reusable safety ingress | `Receive safety candidate` | Execute Workflow Trigger `n8n-nodes-base.executeWorkflowTrigger` v1.1 |
| Parse/schema validation | `Parse and validate frozen action schema` | Code `n8n-nodes-base.code` v2 |
| Validation branch | `Schema is valid?` | If `n8n-nodes-base.if` v2.3 |
| Deterministic policy | `Apply deterministic action policy` | Code `n8n-nodes-base.code` v2 |
| Policy branches | `Policy is ALLOW?`, `Policy requires approval?` | If v2.3 |
| Shared component call | `Execute runtime safety` | Execute Sub-workflow `n8n-nodes-base.executeWorkflow` v1.3, synchronous |
| Action calls | `POST validated/allowed fan on/off` | HTTP Request `n8n-nodes-base.httpRequest` v4.2 |

The safety subworkflow has no middleware endpoint node. Endpoints exist only in callers after an explicit allow branch.

## CONFIG-OBID v2 topology

```text
Step 7 input + single agent + one model + two tools + bounded memory
-> Step 7 final envelope parser
   -> no_action: internal terminal, no safety call, no endpoint
   -> emit_action: candidate at OBID_POST_AGENT_PRE_VALIDATOR
      -> reusable runtime parser/schema validator
      -> deterministic policy
         -> block: blocked terminal
         -> approval_required: hold terminal pending Step 9
         -> allow: deterministic fan_on/fan_off route
```

The nine frozen Step 7 cognitive nodes were compared as complete JSON node objects between v1 and v2 and matched exactly: input preparation, agent, Gemini model, bounded memory, both tools, final envelope parser, no-action branch, and no-action terminal. The v2 change is the downstream reliability boundary only. It retains one agent, one primary model configuration, one bounded-memory configuration, and the same two tools.

## Fault-injection seam

CONFIG-OBID v2 uses production webhook path `/webhook/obid-agent-v2-safety`. The dedicated harness used `/webhook/step-08-safety-harness`, accepted a candidate at `OBID_POST_AGENT_PRE_VALIDATOR`, and invoked stable workflow ID `runtime-safety-v1`, the same component called by CONFIG-OBID v2. It does not alter the sensor schema, modify the agent prompt, or add a bypass route to CONFIG-OBID. The harness was activated only for the bounded readiness observations and was disabled afterward.

## Live state after verification

- `obid-agent-v2-safety`: active.
- `runtime-safety-v1`: inactive as a top-level trigger; callable synchronously by workflow ID.
- `step-08-safety-harness`: inactive after the one-off checks.
- Actual frozen Yacoub middleware remained on the verified host boundary and exposed simulated fan state only.

## Release and step boundaries

Only `schema_valid == true && policy_decision == allow` can release the unchanged valid action. `approval_required` is a hold with no human interaction. No Step 9 HITL mechanism, second agent/model, risk engine, or Step 10 repeated evaluation exists in this configuration.
