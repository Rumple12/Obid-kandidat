# CONFIG-OBID cognitive system

This directory contains the Step 7 `OBID_CREATED` single-agent cognitive
configuration. It preserves the `YACOUB_INHERITED` temperature threshold,
allowed fan actions, target, middleware routes, and frozen `SHARED_INTERFACE`
contracts.

## Configuration boundary

`CONFIG-OBID - Single Agent v1` contains one Gemini 2.5 Flash model, one AI
Agent, exactly two read-only tools, one two-interaction Simple Memory, a small
pre-agent input gate, an internal decision envelope, and minimal fan routing.
The status tool uses a tiny inline Workflow Tool because the pinned runtime's
legacy hidden HTTP Tool failed through its replacement routing engine.

The active files are:

- `workflows/obid-agent-v1.json`: inactive, credential-sanitized portable
  workflow definition;
- `prompts/system-prompt-v1.md`: exact Obid system prompt;
- `tools/tool-definitions-v1.md`: the two permitted tool contracts;
- `react/react-control-v1.md`: iteration and observation controls;
- `memory/window-buffer-v1.md`: bounded-memory semantics and limitations;
- `structured-output/decision-envelope-v1.md`: internal output shape;
- `configuration-manifest.md`: reproducibility manifest;
- `evidence/step-07-cognitive-verification.md`: actual readiness evidence and
  retained failures.

After import, a human must attach a private Google credential locally and
activate the production webhook `/webhook/obid-agent-v1`. The credential must
never be added to this directory or evidence. Read-only status and controlled
action observations require the actual frozen Yacoub middleware at
`host.docker.internal:8000`.

Step 7 does not implement full runtime action-schema validation, deterministic
safety policy, approval-required transformation, HITL, or repeated evaluation.
Those remain Steps 8, 9, and 10 respectively.
