# Bounded window memory v1

**Configuration:** `OBID_CREATED`

- Node: `@n8n/n8n-nodes-langchain.memoryBufferWindow` (`Simple Memory`).
- Type version: `1.3`.
- `contextWindowLength`: `2` completed interactions.
- `sessionIdType`: `customKey`.
- Session expression: `={{ $json.session_id }}`.
- Runtime metadata source: the synthetic `X-Obid-Session-Id` HTTP header,
  mapped by deterministic input preparation. The shared sensor body is
  unchanged.

One completed interaction is one agent input/final-output pair. Tool calls
inside that execution do not consume separate window entries. The installed
node keys buffers as `<workflow-id>__<session-id>` and exposes the last
`k * 2` human/AI messages when loading memory, so this configuration provides
the latest two completed interactions to the model.

The implementation is process-local: it persists across executions within the
same n8n process, is lost on process restart, and removes inactive session
buffers after one hour when cleanup next runs. A new synthetic session ID gives
logical isolation but does not delete the older session.

The underlying history retains older messages; "eviction" here means exclusion
from the active model-visible two-interaction window, not physical deletion.
Runtime proof therefore uses the Simple Memory node's logged
`loadMemoryVariables.chatHistory`: after A, B, and C, a same-session probe must
load B+C and omit A. A distinct-session probe must load an empty history.

n8n automatically stores the final input/output and observable tool-use summary
for each agent interaction. It does not store a hidden scratchpad. CONFIG-OBID
does not add credentials, account identity, chain-of-thought, vector memory,
long-term retrieval, or a second memory strategy.
