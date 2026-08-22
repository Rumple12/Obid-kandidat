# Step 6 baseline manifest

**Status:** `VERIFIED` on 2026-08-22  
**Authoritative source:** `Rumple12/new-yacoub-thesis`  
**Frozen commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`  
**Runtime:** n8n `1.123.37`, image digest `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885`

## `YACOUB_DETERMINISTIC_ANCHOR`

| Item | Frozen/inherited value | Active Obid reproduction |
|---|---|---|
| Provenance | `YACOUB_INHERITED` workflow design | `OBID_CREATED` packaging and verification |
| Source | `cognitive_logic/workflows/deterministic-baseline.json` | `cognitive_logic/baselines/yacoub/deterministic-baseline.json` |
| SHA-256 | `4a1267ecd4ba254a44cad8c56b675755746ddbdf18f01c40016d4ed313072194` | `b16b445b72e9ad7d575b6127a9f11a0f9c4a9dd408928ffe68a8d3f340b1e855` |
| Runtime identity | Frozen ID/path `deterministic-baseline` | ID `deterministic-baseline`; name `new-yacoub deterministic baseline` |
| Webhook | `POST`, `deterministic-baseline` | active production `/webhook/deterministic-baseline` |
| Rule | `body.value >= 30.0` | unchanged |
| Actions | `fan_on` / `fan_off`, target `fan_1`, approval `false` | unchanged |
| Routes | `POST host.docker.internal:8000/fan/on` or `/fan/off` | unchanged |
| AI | none | none |
| Memory | none/not applicable | none/not applicable |
| Readiness | frozen contextual evidence only | 31.4 -> `fan_on`; 25.0 -> `fan_off`; 30.0 -> `fan_on`, each observed once |

The seven inherited nodes, their parameters, connections, and settings are semantically exact. The committed portable export omits n8n instance/version/ownership metadata and is inactive for safe import; the verified live copy was active. These are packaging differences with no decision-semantic impact.

This anchor is not added to the two-configuration Step 5 comparison matrix.

## `CONFIG-BASELINE`

| Item | Frozen/inherited value | Active Obid reproduction |
|---|---|---|
| Provenance | `YACOUB_INHERITED` workflow/prompt/parser/no-memory design | `OBID_CREATED` reconstruction, sanitization, and verification |
| Draft source | `cognitive_logic/workflows/agent-minimal.json` | `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json` |
| SHA-256 | `fab5906aec9923f84f7a5e60eaab80276c86057dfcf924269d69457fca88a6ec` | `ed8697e07eb83deaecac3879c82b860e2c4b8f597bde1bc355a3c5b863c15585` |
| Runtime identity | intended ID/path `agent-minimal` | ID `agent-minimal`; name `new-yacoub minimal agent workflow` |
| Webhook | `POST`, `agent-minimal` | active production `/webhook/agent-minimal` |
| Decision path | one LLM chain, minimal JSON extraction, two action checks, unrouted fallback | unchanged, with the missing model connection restored |
| Model node | historical Google Gemini node | `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`, type version `1` |
| Model | historical node omitted `modelName`; pinned-node default recovered | committed export explicitly records `models/gemini-2.5-flash` |
| Generation settings | stored `options: {}` | `options: {}`; temperature, top-P, top-K, maximum output tokens, and safety settings are not explicitly configured / runtime default |
| Prompt | frozen `cognitive_logic/prompts/system-prompt-v1.md` | exact inline content plus exact adopted file; SHA-256 `a5e24dc517d3bb91eb45ebebb6efd79bbc77bcf7197ecd9b3daf76fd1aab92cd` |
| Memory | stateless/no memory | no memory node, `ai_memory` connection, persistent state, buffer, or vector store; adopted record SHA-256 `9dc513a537350ca61dbf7ae6b815abb6488ec6e659cc7e3c63cd2a3fc5da11a2` |
| Routes | `fan_on` -> `/fan/on`; `fan_off` -> `/fan/off`; unsupported values -> inherited unrouted fallback | unchanged |
| Credential | private runtime prerequisite | attached locally by the human; identity/value not inspected or exported; must be reattached after import |
| Readiness | old Yacoub high/low evidence is contextual only | 31.4 -> `fan_on`; 25.0 -> `fan_off`; 30.0 -> `fan_on`, each observed once |

### Model-configuration recovery

A privacy-scoped read-only inspection of the legitimate stopped historical container `new-yacoub-n8n` found the active 12-node workflow and recovered:

- model node type `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`;
- node type version `1`;
- `ai_languageModel` connection to `Minimal LLM decision`;
- stored parameters `{ "options": {} }`, with no explicit `modelName`.

The historical container and Obid runtime use the same pinned n8n image digest. The installed node definition in that image sets its omitted `modelName` default to `models/gemini-2.5-flash`. The Step 6 live observations used that exact default. The committed sanitized export makes the same value explicit so a later import does not silently depend on an omitted default. No numeric generation parameter is attributed to Yacoub.

### Compatibility repairs

1. Added the connected Google model node and `ai_languageModel` connection proven by the historical active workflow; the frozen draft lacked both.
2. Replaced the draft chain's non-executable prompt-file reminder with the exact frozen prompt bytes in the System message; decision semantics are unchanged.
3. Made the recovered effective default model identifier explicit in the committed sanitized export; the verified live record used the same pinned-node default.
4. Accepted n8n's addition of `conditions.options.version: 2` on the two IF nodes; comparisons, action values, and routing are unchanged.
5. The historical/live reconstruction generated different internal UUIDs and canvas coordinates for the 11 inherited draft nodes. Apart from the separately documented inline-prompt repair and IF-node normalization, node names/types/versions, the user-input expression, preparation fields, parser code, branch comparisons, endpoints, and decision semantics are preserved. The retained `system_prompt_reference` field is a provenance pointer; execution uses the exact inline System message.
6. The portable minimal export explicitly serializes `staticData: null`, which the frozen draft omitted. This adds no workflow state and does not change the stateless choice.
7. Removed credential, owner, project, instance, version, and activation metadata from the committed export. A private credential must be reattached and the workflow activated after import.

The model configuration established here is the expected model-control starting point for future `CONFIG-OBID`, preventing RQ3 from silently becoming a model-comparison experiment. Any material Step 7 change requires an explicit comparability decision. No `CONFIG-OBID` artifact is created here.
