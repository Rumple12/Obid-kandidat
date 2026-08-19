# Obid Thesis Repository Instructions

Repository mode:
Obid bachelor thesis.

Current development model:
Work proceeds through bounded repository tasks and numbered thesis steps.
Execute only the explicitly requested current task or step.

Primary Obid contribution:
Agentic decision-making and reliability extending the
completed Yacoub-compatible workflow-to-action system.

Inherited / Yacoub-owned:
- workflow-to-action infrastructure
- middleware/action API
- existing shared interface/contracts
- deterministic baseline
- minimal Obid-compatible agent baseline
- existing Raspberry Pi/action-side evidence

Obid-owned:
- stronger single-agent decision layer
- explicit tool use
- controlled ReAct-style behavior
- bounded memory
- structured output
- runtime schema/output validation
- action policy enforcement
- real HITL behavior
- repeated reliability evaluation

Repository rules:
- Current development model: ... Work proceeds through bounded repository tasks and numbered thesis steps. ... Execute only the explicitly requested current task or step.
- Never implement future-step functionality.
- Do not silently change shared contracts.
- Do not rebuild Yacoub's middleware architecture.
- Do not claim inherited work as Obid-authored.
- Prefer the smallest implementation that answers the RQs.
- Validator/multi-agent work is optional.
- Never sacrifice validation, HITL, or core evidence for optional features.
- Preserve failures and raw evidence rather than hiding them.
- If instructions conflict, stop and report the conflict.

Reference rule:
Everything under reference/ is read-only source/historical material.
It may contain obsolete or conflicting plans.
Do not modify reference/ and do not treat files there as active
Obid instructions unless the current task explicitly requires them.

Source-of-truth order:
1. Current explicit user/task prompt
2. Root AGENTS.md
3. Active Obid planning documents created during numbered steps
4. reference/ only as supporting context
