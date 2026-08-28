# Step 7 cognitive verification evidence

**Executed:** 2026-08-22

**Configuration:** `CONFIG-OBID`

**Evidence provenance:** `OBID_CREATED`

**Status:** `STEP 7 READINESS VERIFIED`

**Completion claim:** All bounded Step 7 runtime-readiness observations are now
retained, including the final fresh-session threshold-then-status trace in main
execution 33. This is the step-runner completion state; repository-level closure
still follows the required audit and report-scribe gate.

These are one-off cognitive readiness observations, not Step 10 repetitions,
RQ percentages, latency comparison rows, or production-safety evidence.

## Environment and inherited boundary

| Item | Observed value |
|---|---|
| n8n container | `obid-n8n`, running |
| n8n image/version | `n8nio/n8n:1.123.37`; runtime `1.123.37` |
| Image digest | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| LangChain nodes package | `@n8n/n8n-nodes-langchain` `1.122.27` |
| Model | `models/gemini-2.5-flash`; stored generation options `{}` |
| Workflow | `CONFIG-OBID - Single Agent v1`, ID `obid-agent-v1` |
| Webhook | active production `POST /webhook/obid-agent-v1` |
| Yacoub checkout | `<temporary-clean-yacoub-checkout>` |
| Frozen commit | `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Middleware start | `MIDDLEWARE_HOST=0.0.0.0`, `MIDDLEWARE_PORT=8000`, empty `N8N_WEBHOOK_URL`; `python -u -m middleware.api.app` |
| Addressing | host `127.0.0.1:8000`; n8n `host.docker.internal:8000` |
| Hardware | inherited simulated fan only |

The frozen checkout was clean and unmodified. The private Google credential was
attached through authenticated n8n UI. Only the presence of a reference was
verified; no credential ID, name, secret, account data, session, cookie, token,
or key is recorded here or in the portable export.

## Implemented cognitive controls

- One AI Agent v3, one Gemini v1 node, one model configuration, and one
  two-interaction Simple Memory v1.3.
- Exactly two tools: deterministic `temperature_threshold_tool` and read-only
  `fan_status_tool`.
- Hard `options.maxIterations: 3`; no fallback model, retry loop, recursive
  agent, or dynamic tools.
- `returnIntermediateSteps: false`; evidence uses tool-node inputs/results and
  final model output, not hidden reasoning or message-log internals.
- Minimal malformed-input handling before the agent.
- Internal decision envelope with either one candidate inherited action or
  `action: null`.
- Minimal controlled action routing only; no Step 8 validator/policy and no
  Step 9 HITL.

## Readiness matrix

| Evidence ID | Main execution | Observation | Verdict |
|---|---:|---|---|
| `S7-INPUT-MALFORMED` | 12 | missing `value` stopped at `OBID_INPUT_HANDLING`; no model, memory, tool, action, or endpoint | PASS |
| `S7-HIGH` | 13 | first attempt exposed an incompatible singleton-enum/`const` tool schema before any tool call | FAIL, retained |
| high repair check 1 | 14 | strict tool schema rejected n8n's execution wrapper fields | FAIL, retained |
| high repair check 2 | 15 | threshold tool succeeded; legacy hidden HTTP Tool failed `Invalid URL` | FAIL, retained |
| high Workflow Tool check | 16 | cold memory; threshold then status; `fan_on`; `/fan/on`; state off -> on | PASS |
| `S7-LOW` | 18 | cold memory; threshold then status; `fan_off`; `/fan/off`; state on -> off | PASS |
| `S7-THRESHOLD` | 20 | 30.0 C; threshold and status; inclusive `fan_on`; state off -> on | PASS |
| initial `S7-MEM-A` | 22 | threshold completed; provider minute quota blocked continuation | FAIL, retained |
| `S7-MEM-A` quota retry | 23 | empty memory; threshold then status; `fan_on`; state off -> on | PASS |
| `S7-MEM-B` | 25 | loaded A; threshold only; `no_action`; no endpoint; state remained on | PASS |
| first `S7-MEM-C` | 26 | loaded A+B; daily quota blocked before tools | FAIL, retained |
| `S7-MEM-C` quota retry | 27 | loaded A+B; threshold only; `fan_off`; state on -> off | PASS |
| `S7-MEM-EVICTION-PROBE` | 28 | pre-agent load exposed B+C and omitted A; quota then blocked model/tools | active-window proof PASS; execution FAIL retained |
| `S7-MEM-RESET` attempts | 29, 30, 31 | distinct session loaded empty history each time; daily quota blocked before tools | isolation PASS; status-call PENDING |
| credential-attached `S7-MEM-RESET` continuation | 32 | current attached credential reference was exercised; new synthetic session loaded empty history; first model call returned the same daily free-tier quota rejection; no tool or endpoint ran; fan remained off | isolation PASS; status-call PENDING; execution FAIL retained |
| human-reported Tier-1-backed `S7-MEM-RESET` continuation | 33 | new synthetic session; empty memory; threshold then status; `no_action`; no endpoint; fan remained off | PASS; final reset evidence complete |

Inline status-tool subexecutions for executions 16, 18, 20, 23, and 33 were 17,
19, 21, 24, and 34 respectively. Each ended at `Normalize inherited status`
with a result derived from actual Yacoub `GET /status`.

## Final reset/isolation continuation

Following the human's report that Tier 1 billing was enabled, the single
authorized continuation probe used a new non-private synthetic session and the
already-defined valid 25.0 C low-temperature event. No billing or credential
identity was inspected.

| Item | Execution 33 observation |
|---|---|
| Start / stop | `2026-08-22 14:51:08.331 UTC` / `2026-08-22 14:51:16.380 UTC` |
| Synthetic session | `s7-reset-tier1-20260822-512a1878` |
| Precondition | inherited simulated fan explicitly set to `off`; `/status` confirmed `off` |
| Memory load | both observable pre-save `loadMemoryVariables.chatHistory` results were empty arrays |
| Model calls | 2, both successful |
| Tool counts | `temperature_threshold_tool` x1; `fan_status_tool` x1 |
| Tool order | `temperature_threshold_tool` -> `fan_status_tool` |
| Threshold input/result | `{"value":25,"unit":"C"}` -> `{"threshold_c":30,"relation":"below","desired_action":"fan_off","desired_fan_state":"off"}` |
| Status input/result | `fan_1` -> `{"target":"fan_1","fan_state":"off","simulated":true,"source":"yacoub_status"}` |
| Main endpoint counts | `POST /fan/on`: 0; `POST /fan/off`: 0 |
| Final middleware state | `off`, simulated |
| Termination | success at `Internal no-action terminal`; one agent run; observable agent `iterationCount: 1`; inside `maxIterations: 3` |

The observable raw model output was:

```json
{"decision": "no_action", "action": null, "state_before": "off", "state_after": "off", "reason_code": "desired_state_already_satisfied"}
```

The parser returned the same decision envelope with `parse_status: parsed`, and
the terminal node added `routing_status: internal_no_action` and
`endpoint_reached: null`. No hidden reasoning was requested or retained.

## Successful tool and termination traces

| Main execution | Model calls | Tool order and count | Final output/route | Bound verdict |
|---:|---:|---|---|---|
| 16 | 3 | threshold x1 -> status x1 | clean JSON `emit_action`; `/fan/on` | PASS |
| 18 | 3 | threshold x1 -> status x1 | clean JSON `emit_action`; `/fan/off` | PASS |
| 20 | 2 | threshold x1 + status x1 in one tool round | clean JSON `emit_action`; `/fan/on` | PASS |
| 23 | 3 | threshold x1 -> status x1 | clean JSON `emit_action`; `/fan/on` | PASS |
| 25 | 2 | threshold x1; status x0 | clean JSON `no_action`; no endpoint | PASS |
| 27 | 2 | threshold x1; status x0 | clean JSON `emit_action`; `/fan/off` | PASS |
| 33 | 2 | threshold x1 -> status x1 | clean JSON `no_action`; no endpoint | PASS |

Every successful agent execution used no more than two permitted tool calls,
called neither tool more than once, completed one agent node run, and terminated
inside the configured bound of three tool-containing rounds. No recursive or
unbounded execution occurred. The successful raw outputs contained plain JSON
only; no Markdown, fences, or extra prose were observed. The failed outputs are
not hidden or replaced.

Representative observable tool results were:

```json
{"threshold_c":30,"relation":"at_or_above","desired_action":"fan_on","desired_fan_state":"on"}
```

```json
{"target":"fan_1","fan_state":"off","simulated":true,"source":"yacoub_status"}
```

For warm sequence executions 25 and 27, execution data contains no
`fan_status_tool` run. This is runtime evidence, rather than a model-generated
claim, that remembered state suppressed the cold-start status lookup.

## Memory inclusion, active-window eviction, and isolation

The memory node logged `loadMemoryVariables.chatHistory` for each execution:

| Execution | Active model-visible human timestamps at load | Meaning |
|---:|---|---|
| 23 / A | empty | cold session |
| 25 / B | `13:08:00Z` | A included |
| 27 / C | `13:08:00Z`, `13:09:00Z` | A+B included before C save |
| 28 / eviction probe | `13:09:00Z`, `13:11:00Z` | B+C included; A excluded |
| 29-31 / distinct reset session | empty | no prior-session context inherited |
| 32 / new credential-attached reset session | empty | no prior-session context inherited; provider rejected the first model call |
| 33 / human-reported Tier-1-backed reset session | empty | isolated cold session; threshold and status tools then completed |

This proves a model-visible bound of two completed interactions and active-window
eviction after C. The underlying save log contained six messages after C, so
older backing messages were not physically deleted; this is the installed
BufferWindowMemory behavior documented in the configuration record.

The reset sessions are demonstrably isolated. Executions 29-31 and the first
credential-attached continuation, execution 32, remain retained failures because
Gemini rejected them before the first tool call. The single permitted
continuation after the human-reported Tier 1 change, execution 33, then proved
the missing cold-session behavior: empty memory, threshold x1, status x1, and an
internal no-op with no action endpoint. Reset/isolation is therefore verified
without hiding the prior failures.

## Structured decisions and middleware observations

- High/check execution 16: `fan_on`, `fan_1`, approval `false`, off -> on;
  middleware returned simulated `fan_on` and exposed final state `on`.
- Low execution 18: `fan_off`, `fan_1`, approval `false`, on -> off;
  middleware returned simulated `fan_off` and exposed final state `off`.
- Exact-threshold execution 20 preserved `30.0 C -> fan_on`.
- A execution 23 moved off -> on. B execution 25 returned internal
  `decision: no_action`, `action: null`, and reached no endpoint. C execution 27
  moved on -> off.
- Reset execution 33 began from an isolated empty session with the simulated fan
  off, called threshold then status, returned `decision: no_action` with
  `action: null`, reached no endpoint, and left the fan off.
- No `no_action` action identifier or new shared field was introduced.

These candidates were routed for cognitive/integration readiness only. They were
not validated against the full action JSON Schema at runtime and are not safety
evidence.

## Retained deviations and bounded repairs

1. Execution 13 showed Gemini rejected a singleton enum converted by n8n into a
   `const` tool-schema keyword. The internal tool schema was narrowed to ordinary
   number/string properties; the deterministic tool code still enforces unit
   `C`. No shared schema changed.
2. Execution 14 showed that `additionalProperties: false` rejected n8n's own
   tool execution wrapper fields. That internal restriction was removed; the
   tool still reads only `value` and `unit` and remains deterministic.
3. Execution 15 proved the installed legacy hidden HTTP Tool was not executable
   through the pinned replacement routing path. It was replaced with the
   installed Workflow Tool v2.2 and one three-node inline read-only status
   subworkflow. No service, adapter, or fan action tool was added.
4. Executions 22, 26, 28, and 29-32 retain Gemini quota failures. The A and C
   sequences were resumed only after provider-specified delays, with the failed
   attempts retained. The eviction and reset loads remain valid because memory
   is loaded before the failed model call.
5. After the human reported credential attachment complete, execution 32 used
   the credential reference currently attached to the live workflow. Only
   presence and reference equality were checked; no ID, name, secret, account,
   or owner value was displayed, copied into evidence, or committed. The
   provider still reported the daily free-tier request quota as exhausted, so
   no retry was performed.
6. After the human reported Tier 1 billing enabled, exactly one further probe
   was run. Execution 33 succeeded without any model, prompt, tool, memory,
   iteration, schema, or oracle change. No second success attempt was run.

The model identifier, generation settings, prompt semantics, iteration bound,
memory strategy/window, shared contracts, and inherited threshold were not
changed to make a run pass.

## Privacy, provenance, and future-step boundary

The committed workflow is inactive and contains no credential object, ID/name,
secret, owner/project metadata, account data, session token, cookie, or
encryption key. Synthetic session IDs contain no personal identity. The live
credential remains only in local n8n state and must be reattached after import.

`YACOUB_INHERITED`: threshold/action semantics, middleware, `/status`, fan
routes, and simulated state. `SHARED_INTERFACE`: frozen sensor/action shapes and
endpoint meanings. `OBID_CREATED`: main workflow, prompt, tools, ReAct controls,
memory configuration, input gate, internal envelope, and this evidence.

No baseline artifact, Step 5 oracle/protocol, shared schema, `reference/` file,
or upstream Yacoub file was intentionally modified. No Step 8 validator/policy,
Step 9 HITL, or Step 10 repeated evaluation was started.

## Remaining human action

None for the bounded Step 7 runtime-readiness observation. Execution 33 supplied
the missing reset/status trace, and the probe must not be repeated merely to
obtain another success. The next repository action is the separate read-only
Step 7 audit, not Step 8 implementation.
