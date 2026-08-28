# Step 6 baseline verification evidence

**Executed:** 2026-08-22  
**Step status:** `VERIFIED`  
**Evidence provenance:** `OBID_CREATED` verification of `YACOUB_INHERITED` baselines  
**Authoritative Yacoub commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`

These are bounded readiness observations, not Step 10 repetitions, RQ3 result rows, or statistical evidence. Each declared high, low, and exact-threshold stimulus was executed exactly once per baseline.

## Environment and collaborator runtime

| Item | Observed value |
|---|---|
| Obid container | `obid-n8n`, running |
| n8n image/version | `n8nio/n8n:1.123.37`; runtime `1.123.37` |
| Image digest | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Yacoub execution checkout | `<temporary-clean-yacoub-checkout>` |
| Checkout state | clean detached checkout at the authoritative commit |
| Middleware startup | `MIDDLEWARE_HOST=0.0.0.0`, `MIDDLEWARE_PORT=8000`, empty `N8N_WEBHOOK_URL`; `python -u -m middleware.api.app` |
| Middleware addressing | host `http://127.0.0.1:8000`; n8n `http://host.docker.internal:8000` |
| Hardware state | inherited simulated fan only; no GPIO or Raspberry Pi work |

Before baseline requests, host and container-side `GET /status` both returned 200 with `hardware: "simulated"`. The frozen middleware checkout remained unmodified.

## Frozen source inventory

| Frozen path | SHA-256 | Role |
|---|---|---|
| `cognitive_logic/workflows/deterministic-baseline.json` | `4a1267ecd4ba254a44cad8c56b675755746ddbdf18f01c40016d4ed313072194` | deterministic executable source |
| `cognitive_logic/workflows/deterministic-baseline.md` | `203242a618dcabe3e2472672d7fce968cea6ac3ec59652076db20a35f9e1447d` | inherited description |
| `cognitive_logic/workflows/evidence/step-06-runtime-verification.md` | `a4b056b1833a0a9e681a5e07a501ef1074bc39c003aee9b48ce7bd0e1ee3d255` | old Yacoub contextual evidence |
| `cognitive_logic/workflows/agent-minimal.json` | `fab5906aec9923f84f7a5e60eaab80276c86057dfcf924269d69457fca88a6ec` | incomplete minimal-agent draft |
| `cognitive_logic/workflows/agent-minimal.md` | `01665de2f7cc54a5b3fd22b2ddb4761e2183993523a491a417171346fe3f01d9` | inherited description |
| `cognitive_logic/prompts/system-prompt-v1.md` | `a5e24dc517d3bb91eb45ebebb6efd79bbc77bcf7197ecd9b3daf76fd1aab92cd` | inherited prompt |
| `cognitive_logic/memory/memory-choice-v1.md` | `9dc513a537350ca61dbf7ae6b815abb6488ec6e659cc7e3c63cd2a3fc5da11a2` | inherited stateless choice |
| `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md` | `4f2b392a5ee16833a9c96cd0882b23f5dadc6079bb4f7ab754e504b0972b0ade` | old Yacoub contextual agent evidence |

Old Yacoub evidence was used only to establish provenance and recovery direction; it is not presented as a new Obid observation.
All frozen file contents and hashes came from the exact Git objects or the clean detached checkout; the dirty/pruned sibling working tree was not used as content authority.

## Active sanitized artifacts

| Active path | SHA-256 | Sanitization/fidelity result |
|---|---|---|
| `cognitive_logic/baselines/yacoub/deterministic-baseline.json` | `b16b445b72e9ad7d575b6127a9f11a0f9c4a9dd408928ffe68a8d3f340b1e855` | seven inherited nodes, parameters, connections, and settings exact; runtime metadata omitted |
| `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json` | `ed8697e07eb83deaecac3879c82b860e2c4b8f597bde1bc355a3c5b863c15585` | verified 12-node reproduction; credential and instance metadata omitted |
| `cognitive_logic/baselines/yacoub/system-prompt-v1.md` | `a5e24dc517d3bb91eb45ebebb6efd79bbc77bcf7197ecd9b3daf76fd1aab92cd` | byte-identical to frozen prompt; inline System message also exact |
| `cognitive_logic/baselines/yacoub/memory-choice-v1.md` | `9dc513a537350ca61dbf7ae6b815abb6488ec6e659cc7e3c63cd2a3fc5da11a2` | byte-identical to frozen no-memory choice |

Both JSON exports are inactive and credential-sanitized for portable storage. This differs from the successfully activated live workflows and is intentional: activation and private credential attachment are local runtime operations.
Each committed JSON file was also imported successfully into a disposable n8n `1.123.37` container with the repository mounted read-only. That portability check created no persistent volume, credential, workflow execution, or evaluation result.

## Deterministic anchor verification

The active workflow was `new-yacoub deterministic baseline`, ID `deterministic-baseline`, at production path `/webhook/deterministic-baseline`. Static comparison found the frozen and active seven-node definitions, connections, and settings exact. There is no AI, prompt, memory, parser, validator, policy, or HITL node.

| Case | Fixed stimulus | n8n execution | Observable action before middleware | Endpoint/result | State after | Verdict |
|---|---:|---:|---|---|---|---|
| `S6-DET-HIGH` | 31.4 C | 6, success | `fan_on`, `fan_1`, `temperature_at_or_above_threshold`, approval `false` | `POST /fan/on` -> 200, `fan_on` | `on` | PASS |
| `S6-DET-LOW` | 25.0 C | 7, success | `fan_off`, `fan_1`, `temperature_below_threshold`, approval `false` | `POST /fan/off` -> 200, `fan_off` | `off` | PASS |
| `S6-DET-THRESHOLD` | 30.0 C | 8, success | `fan_on`, `fan_1`, `temperature_at_or_above_threshold`, approval `false` | `POST /fan/on` -> 200, `fan_on` | `on` | PASS |

The execution records began at `2026-08-22 11:01:59Z`. Each ran in production webhook mode and terminated at the expected middleware HTTP Request node. No repeat was made.

## Minimal-agent reconstruction and model recovery

The frozen draft had 11 nodes and no executable model node/connection. Frozen screenshots and evidence established Google Gemini use but not the exact node configuration. A read-only, workflow-scoped inspection of the legitimate stopped historical `new-yacoub-n8n` runtime recovered the active 12-node workflow. Only workflow node types, non-secret parameters, and connections were queried.

Recovered configuration:

- node: `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`, type version `1`;
- connection: `Google Gemini Chat Model` -> `Minimal LLM decision` via `ai_languageModel`;
- historical stored parameters: `{ "options": {} }`;
- historical `modelName`: absent;
- exact effective model: `models/gemini-2.5-flash`, recovered from the matching pinned node implementation's default;
- temperature, top-P, top-K, maximum output tokens, and safety settings: not explicitly configured / runtime default.

The historical and Obid containers use the same image digest. The installed node definition at n8n `1.123.37` declares `models/gemini-2.5-flash` as the default. The active readiness run used this omitted default; the sanitized committed export pins the same value explicitly. No substitute model or invented numeric setting was selected.

A human attached a private Google credential through authenticated n8n UI. Verification checked only that a reference was present. No credential ID, name, secret, encrypted value, owner data, session, cookie, token, or encryption key was queried, printed, or committed.
Temporary SQLite copies and the raw runtime export used for scoped inspection were removed after safe fields were extracted. The credential remains only in n8n's persistent local runtime state.

The live workflow contained exactly one LLM chain and one connected Google model node. The exact frozen prompt was placed in the chain's System message because the draft's repository-path reminder was not executable runtime configuration; the retained `system_prompt_reference` input field is provenance only. The inherited parser code, action checks, endpoints, and unrouted fallback remained unchanged. The reconstruction generated different internal UUIDs and canvas coordinates for the 11 inherited draft nodes, n8n normalized the two IF nodes by adding `conditions.options.version: 2`, and the portable export explicitly serializes `staticData: null` although the draft omitted that key. None of these metadata/serialization differences changed executable decision semantics or added state. No memory node or `ai_memory` connection existed.

The webhook is the active production `/webhook/agent-minimal`. It maps directly to the Step 5 logical `CORE_CONFIG_WORKFLOW_INGRESS` and `BASELINE_EVAL_PRE_DECISION_INGRESS`: the request is received immediately before preparation and the single baseline decision, so no extra adapter was added.

## Minimal-agent readiness observations

### `S6-AGENT-HIGH` - execution 9

Input was the five-field temperature event with fixed timestamp `2026-08-22T10:10:00Z` and value `31.4` C.

Raw observable model response:

~~~text
```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```
~~~

The inherited parser extracted the object. The `fan_on` branch called `POST /fan/on`; middleware returned 200 with simulated `fan_on`, and state was `on`. Verdict: **PASS**.

### `S6-AGENT-LOW` - execution 10

Input used fixed timestamp `2026-08-22T10:11:00Z` and value `25.0` C.

Raw observable model response:

~~~text
{"action_id": "fan_off", "target": "fan_1", "reason": "temperature_below_threshold", "requires_approval": false}
~~~

The inherited parser extracted the object. The `fan_off` branch called `POST /fan/off`; middleware returned 200 with simulated `fan_off`, and state was `off`. Verdict: **PASS**.

### `S6-AGENT-THRESHOLD` - execution 11

Input used fixed timestamp `2026-08-22T10:12:00Z` and value `30.0` C.

Raw observable model response:

~~~text
```json
{
  "action_id": "fan_on",
  "target": "fan_1",
  "reason": "temperature_at_or_above_threshold",
  "requires_approval": false
}
```
~~~

The inherited parser extracted the object. The inclusive threshold routed to `POST /fan/on`; middleware returned 200 with simulated `fan_on`, and final state was `on`. Verdict: **PASS**.

The three executions began at `2026-08-22 11:36:49Z`, `11:36:52Z`, and `11:36:54Z`, and all completed successfully. Each case was observed once. The high and threshold responses violated the prompt's JSON-only formatting instruction by adding code fences; this inherited baseline behavior was retained and documented, not tuned or rerun.

## Offline contract observation

The three parsed minimal-agent objects each passed an offline `Test-Json` check against the adopted Step 5 `agent-action.schema.json`. This was evidence-only static checking after execution. No validator node, policy, retry, or runtime enforcement was added; runtime validation remains Step 8.

## Failures, limitations, and boundaries

- No infrastructure/import failure occurred.
- No decision or routing failure occurred in the six readiness observations.
- The two fenced model responses are retained as observable format deviations.
- Middleware action responses use inherited `reason: "manual_api_call"`; this is middleware response behavior and does not replace the agent proposal's reason.
- Direct baseline webhooks bypassed `/sensor-event` as authorized, so middleware `last_sensor_event` remained `null`.
- The inherited unrouted fallback is minimal routing only, not JSON Schema validation, policy, HITL, or a production-safety claim.
- No Step 5 malformed, memory-sequence, invalid-action, HITL, five-repetition, run-order, latency-comparison, or aggregate evaluation case was executed.
- No `CONFIG-OBID`, Step 7 prompt/tool/ReAct/memory artifact, Step 8 validator/policy, Step 9 HITL, or Step 10 result was created.

Step 7 may use the established Gemini configuration as its model-control starting point, but any material change must be an explicit comparability decision. Step 7 was not started.
