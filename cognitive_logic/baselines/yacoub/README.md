# Yacoub handoff baselines

This directory contains Obid's reproducible packaging and verification of two collaborator-provided baselines from `Rumple12/new-yacoub-thesis` at frozen commit `278318340bfa4e4650a97a2baba73f63bd868ed9`. The workflow designs, threshold, prompt, parser/routing design, and no-memory choice remain `YACOUB_INHERITED`. Packaging, compatibility-repair records, sanitized exports, and new Step 6 observations are `OBID_CREATED` verification work.

## Baseline roles

- `deterministic-baseline.json` is `YACOUB_DETERMINISTIC_ANCHOR`: a fixed non-AI reference, not a third Step 10 core configuration.
- `minimal-agent-baseline.json` is `CONFIG-BASELINE`: the inherited minimal agent later compared with `CONFIG-OBID` under the frozen Step 5 protocol.

Both committed exports are portable, inactive, and stripped of instance, owner, project, and credential metadata. The deterministic export can be imported and activated directly. After importing the minimal export, a human must attach a valid private Google credential to `Google Gemini Chat Model`, save, and activate the workflow. Never commit, print, or record the credential identity or value.

The active Step 6 runtime used n8n `1.123.37`, production webhook paths `/webhook/deterministic-baseline` and `/webhook/agent-minimal`, and the actual frozen Yacoub middleware at `host.docker.internal:8000`. Reproduction details and exact source-to-active differences are in [baseline-manifest.md](baseline-manifest.md) and [step-06-baseline-verification.md](evidence/step-06-baseline-verification.md).

These workflows intentionally contain no Obid ReAct behavior, tools, bounded memory, runtime JSON Schema validator, policy engine, or HITL gate. The minimal parser and unrouted fallback are not a safety layer. Step 7 and later features do not belong in this directory's inherited baseline definitions.

