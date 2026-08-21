# Future Handoff Verification Checklist

**Created:** Step 2

**Status:** Step 3 runtime compatibility, Step 4 integration boundary, and Step 5 contract/evaluation freeze are completed and evidenced. Step 6 checks remain future and unticked. When this checklist was created during Step 2, no later runtime work had yet been executed.

## How to use this checklist

- Perform a check only in its assigned numbered step.
- Record exact configuration, command/UI action, observed result, evidence path, and provenance.
- Keep failed and partial checks visible.
- Do not tick an item based on inherited documentation alone.
- Stop for an explicit decision if compatibility requires changing locked semantics.

## Provenance prerequisite before later adoption

- [x] **`[CHECK-PROV-01]` Before Step 5/6 adoption:** Step 5 used the exact Git objects from `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9`; the dirty/pruned local working tree was not content authority. Evidence: `shared_interfaces/contract-freeze.md`.
- [x] **`[CHECK-PROV-02]` Before any active copy:** Origin, frozen path, `YACOUB_INHERITED`/`SHARED_INTERFACE` provenance, adoption reason, destination, source/destination SHA-256, and no-drift result are recorded in `shared_interfaces/contract-freeze.md` and `docs/collaboration/shared-interface-provenance.md`.

The local nested reference state has been documented in Step 2. Whether it was intentionally pruned cannot be established from repository contents and does not authorize cleaning or modifying `reference/`.

## Step 3 - Obid n8n runtime compatibility

- [x] **`[CHECK-S3-01]` Exact Obid n8n version:** `n8nio/n8n:1.123.37`, image ID/digest `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885`, and runtime-reported version `1.123.37` were verified. Evidence: `infrastructure/docker/evidence/step-03-runtime-verification.md`.
- [x] **`[CHECK-S3-02]` Frozen-version comparison:** The actual Obid runtime exactly matches Yacoub's pinned `n8nio/n8n:1.123.37`; no silent upgrade or port deviation occurred. Evidence: `infrastructure/docker/runtime-manifest.md` and the Step 3 runtime evidence.
- [x] **`[CHECK-S3-03]` Required node availability:** All built-in node types in the frozen deterministic/minimal-agent exports, `@n8n/n8n-nodes-langchain.chainLlm`, and the Google Gemini Chat Model capability were verified from installed runtime packages without importing a workflow or configuring credentials. Evidence: the capability matrix in the Step 3 runtime evidence.
- [x] **`[CHECK-S3-04]` Compatibility decision:** `VERIFIED` compatible for the Step 4/6 prerequisites. Obid-specific names and required secret injection preserve the frozen single-service, SQLite, port, version, node, timezone, and Docker-to-host assumptions. Owner/application initialization survived a non-destructive restart; no shared-interface behavior has been claimed.

Step 3 evidence should identify the new runtime as `OBID_CREATED`. Matching a Yacoub version/configuration does not transfer authorship.

## Step 4 - Integration boundary

- [x] **`[CHECK-S4-01]` Obid webhook path:** Verified active production paths `obid-yacoub-compat`, `obid-yacoub-compat-fan-on`, and `obid-yacoub-compat-fan-off` under host `/webhook/`; `/webhook-test/` was not used. Evidence: `integration/yacoub_compat/evidence/step-04-integration-verification.md`.
- [x] **`[CHECK-S4-02]` `N8N_WEBHOOK_URL`:** Actual Yacoub middleware forwarded end to end through `http://127.0.0.1:5678/webhook/obid-yacoub-compat`, returning nested forwarding status `sent` and n8n status 200.
- [x] **`[CHECK-S4-03]` Middleware reachability:** The exact frozen middleware ran on host bind `0.0.0.0:8000`; host tests used `127.0.0.1:8000`, and `obid-n8n` reached it through `host.docker.internal:8000`.
- [x] **`[CHECK-S4-04]` `GET /status`:** Host and container-side requests returned 200 with the inherited status/message/state shape and simulated hardware state.
- [x] **`[CHECK-S4-05]` `POST /sensor-event`:** One compatible five-field temperature event returned 202, forwarded successfully, and appeared with matching values in successful n8n execution 1.
- [x] **`[CHECK-S4-06]` `POST /fan/on`:** The Obid n8n HTTP Request node called actual Yacoub `/fan/on`; execution 2 succeeded, response reported simulated `fan_on`, and `/status` showed `on`.
- [x] **`[CHECK-S4-07]` `POST /fan/off`:** The Obid n8n HTTP Request node called actual Yacoub `/fan/off`; execution 3 succeeded, response reported simulated `fan_off`, and final `/status` showed `off`.
- [x] **`[CHECK-S4-08]` No competing middleware:** Actual frozen Yacoub middleware was used from a clean detached temporary checkout. No middleware copy, adapter, stub, or `TEST_DOUBLE` was created in Obid.

## Step 5 - Shared contracts and evaluation-boundary preparation

- [x] **`[CHECK-S5-01]` Sensor schema adoption:** Adopted the exact frozen `shared_interfaces/json-schema/sensor-event.schema.json` as an active `SHARED_INTERFACE` artifact. Evidence: `shared_interfaces/contract-freeze.md`.
- [x] **`[CHECK-S5-02]` Sensor schema verification:** Verified all five properties, types, constants, required fields, date-time format, numeric rules, and `additionalProperties: false` against the frozen Git blob.
- [x] **`[CHECK-S5-03]` Action schema adoption:** Adopted the exact frozen `shared_interfaces/json-schema/agent-action.schema.json` as an active `SHARED_INTERFACE` artifact. Evidence: `shared_interfaces/contract-freeze.md`.
- [x] **`[CHECK-S5-04]` Action schema verification:** Verified all four properties, types, allowed actions, target, non-empty reason, Boolean approval field, required fields, and `additionalProperties: false` against the frozen Git blob.
- [x] **`[CHECK-S5-05]` No schema drift:** Source and destination SHA-256 hashes match for both schemas; no content or line-ending change occurred.
- [x] **`[CHECK-S5-06]` Valid risky case:** `EVAL-HITL-01A/B` freeze a post-policy schema-valid `fan_on`, `fan_1`, non-empty-reason candidate with `requires_approval: true`; the supplied pre-policy proposal is transformed internally without widening the shared schema.
- [x] **`[CHECK-S5-07]` Threshold and semantic preservation:** The oracle preserves `value >= 30.0 C -> fan_on`, otherwise `fan_off`, target `fan_1`, and the inherited endpoint mapping; these are documented as semantics outside the schemas.
- [x] **`[CHECK-S5-08]` Evaluation-case freeze:** The machine-readable manifest freezes high, low, exact-threshold, malformed, invalid-action, HITL, and bounded-state cases with expected outcomes and ownership.
- [x] **`[CHECK-S5-09]` Malformed ownership/injection point:** `EVAL-MALFORMED-01` enters at Obid-owned `EVAL_DIRECT_PRE_DECISION_INGRESS`, routing to `OBID_EVAL_PRE_AGENT_INGRESS` for `CONFIG-OBID` and an analogous baseline seam; both bypass Yacoub normalization and require no shared action.
- [x] **`[CHECK-S5-10]` Required bounded-memory sequence:** `EVAL-MEMORY-01A/B/C` freezes off -> on, duplicate suppression while on, and on -> off with explicit states and no shared `no_action` value.
- [x] **`[CHECK-S5-11]` Repetition protocol:** Five repetitions are frozen per automated case/applicable configuration; the ordered memory sequence and controlled HITL variants have explicit repetition/reset rules.
- [x] **`[CHECK-S5-12]` RQ3 comparable latency:** High, low, and exact threshold are the common automated latency subset with the same ingress-to-final-automated-terminal timing boundary; human wait is excluded and HITL timing is separated.

Step 5 definitions are frozen in `evaluation/cases/obid-evaluation-cases.json`, `evaluation/evaluation-protocol.md`, and `evaluation/evidence/step-05-contract-and-evaluation-freeze.md`. They are expected-oracle and planning artifacts, not observed results.

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
