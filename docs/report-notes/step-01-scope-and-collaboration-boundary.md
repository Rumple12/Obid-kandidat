# Step 1 report-support note

## Step

Step 1 — Lock Obid scope and the Yacoub–Obid collaboration boundary

## Status

Step 1 passed audit after bounded repair. The completed work is a planning, scope, provenance, and evidence-boundary checkpoint; it does not establish that any planned Obid implementation functionality has been completed.

## What was established

Step 1 locked one collaborative system with two separately attributable bachelor-thesis contributions. The frozen handoff establishes Yacoub's completed workflow-to-action infrastructure and compatible baselines as inherited material. Obid is planned to extend that system with a stronger single-agent decision and reliability layer while preserving a small shared compatibility boundary.

The minimum contribution was fixed at Tier 1.5: one temperature-to-fan scenario, one primary model configuration, one main Obid agent workflow, one bounded-memory configuration, runtime validation, one deterministic policy path, one real approval path, and repeated evaluation against frozen cases. RQ1–RQ3 were locked around action accuracy and consistency, prevention of invalid or risky actions, and reliability/latency differences from the inherited minimal agent baseline. Runtime structured-output validation, policy enforcement, actual HITL, and repeated evaluation are mandatory directions. A validator-agent or two-agent comparison remains optional, supplementary, and non-core.

## Why it matters

This boundary prevents scope creep and authorship/provenance confusion. It fixes the experimental comparison anchors and ensures that Obid extends the inherited Yacoub system instead of duplicating its middleware or baselines. It also makes later implementation claims, runtime traces, and evaluation results traceable to the correct thesis contribution.

## Yacoub-owned / inherited

The following remain Yacoub-owned or inherited:

- prior pinned n8n setup/configuration, workflow/runtime assumptions, and Yacoub runtime evidence;
- workflow-to-action infrastructure;
- middleware/action API, including sensor forwarding, mock state, and fan endpoints;
- shared sensor-event and action contracts;
- deterministic threshold baseline;
- minimal Obid-compatible, stateless agent baseline;
- existing Raspberry Pi/action-side evidence; and
- safety, validation, policy, and HITL designs that are specification-only rather than runtime enforcement.

Obid may configure, verify, integrate, and compare these artifacts, but reuse does not transfer authorship. Inherited implementations or evidence must not be reported as Obid-authored.

## Obid-owned planned contribution

Step 1 locked the following contribution targets for later numbered steps:

- creation/configuration of the Step 3 Obid runtime and compatibility verification against the frozen Yacoub configuration;
- a stronger single-agent decision layer and its system prompt;
- explicit tools and controlled ReAct-style behavior;
- one bounded-memory configuration;
- structured action output;
- runtime schema/output validation;
- deterministic action-policy enforcement;
- actual HITL approve/reject behavior; and
- repeated reliability and latency evaluation.

These are planned Obid-owned targets, not implementations completed during Step 1.

## Shared compatibility boundary

The locked inherited sensor-event semantics are:

- fields: `sensor_id`, `timestamp`, `type`, `value`, `unit`;
- `type = temperature`;
- `unit = C`.

The locked inherited action semantics are:

- fields: `action_id`, `target`, `reason`, `requires_approval`;
- allowed actions: `fan_on`, `fan_off`;
- target: `fan_1`.

The inherited middleware endpoints are:

- `GET /status`;
- `POST /sensor-event`;
- `POST /fan/on`;
- `POST /fan/off`.

The inherited deterministic baseline is:

- `value >= 30.0 C -> fan_on`;
- otherwise `fan_off`.

The action-to-endpoint mapping remains `fan_on -> POST /fan/on` and `fan_off -> POST /fan/off`. Shared contracts and endpoint semantics must not change silently; any change requires explicit authorization and a recorded compatibility decision.

## Research questions

RQ1:

> How accurately and consistently does the extended n8n-based agentic decision layer produce the expected IoT action across defined normal, malformed, and state-dependent test cases?

RQ2:

> How effectively do runtime structured-output validation, action policies, and Human-in-the-Loop approval prevent invalid or risky agent actions from reaching the shared IoT action interface?

RQ3:

> What reliability and latency differences are observed between the inherited minimal agent baseline and the extended Obid agentic workflow under the same defined IoT test cases?

## Evaluation rules locked by Step 1

- Step 5 must define and freeze the evaluation cases before reportable runs.
- At least one state-dependent/bounded-memory case is mandatory and must define an expected transition or other state-dependent outcome.
- Only one bounded-memory configuration is in scope.
- The preferred starting target is five repetitions per case per evaluated core configuration, subject to Step 5 finalization.
- Raw failures, malformed outputs, blocks, rejects, timeouts, missing values, and unexpected outcomes must remain preserved with their denominators and error context.
- Malformed-case injection point, component under test, expected terminal stage, expected outcome, and ownership attribution must be explicit.
- Handling performed by inherited Yacoub middleware is integration/context evidence and must not be counted automatically as Obid agent correctness.
- The inherited minimal-agent versus Obid automated-latency comparison must use a common comparable automated case subset with identical repetition rules.
- Human HITL wait time is excluded from the main automated latency comparison.
- Where instrumentation allows, HITL timing is reported separately as pre-wait automated processing, human wait, post-decision automated processing, and total elapsed time. Unseparated timing components must be reported as limitations rather than guessed.

No evaluation runs occurred in Step 1.

## Evidence / source artifacts

The active Step 1 planning artifacts are:

- `docs/ongoing/collaboration-boundary.md`
- `docs/ongoing/yacoub-handoff.md`
- `docs/ongoing/obid-scope.md`
- `docs/ongoing/research-questions.md`
- `docs/ongoing/project-overview.md`
- `docs/ongoing/report-outline.md`
- `docs/plans/implementation-plan.md`
- `docs/plans/obid-14-step-process.md`
- `docs/decisions.md`

The read-only handoff source is `reference/yacoub-handoff.md`. The authoritative frozen Yacoub source is commit `278318340bfa4e4650a97a2baba73f63bd868ed9`.

Repository checkpoints:

- Step 1 planning commit: `2da3ae1958932046efafc569a78f1809e4f1aabc`
- Step 1 bounded-repair commit: `ad9bec0a90bddafdb1a7a30dec4df351448daf74`

The final audit verdict was recorded through Codex/thread review; this note does not assert that a separate committed audit artifact exists.

## Thesis chapters supported

- Chapter 1 — aim, RQs, scope, contribution, and division of work;
- Chapter 3 — scoped methodology and evidence discipline;
- Chapter 4 — collaboration/system boundary and design rationale;
- Chapter 7 — limitations, validity, and scope; and
- Appendix — provenance and reproducibility references where useful.

## Limitations / unresolved items

These later-step checks remain open but are not blockers for Step 1:

- verify exact Obid n8n runtime compatibility in Step 3;
- verify the exact Obid webhook URL/path and `N8N_WEBHOOK_URL` forwarding path in Step 4;
- recover or recreate a reproducible inherited minimal-agent export/configuration with its connected model node in Step 6;
- record the exact Gemini model/version and credential-independent settings in Step 6;
- reconfirm both inherited baseline outputs under the Obid runtime before comparison; and
- finalize in Step 5 a valid schema-conforming risky case with `requires_approval: true` without expanding the allowed action or target set.

## Evidence still needed later

Step 1 produced planning and provenance evidence only. Later numbered steps must still produce:

- runtime proof;
- workflow exports;
- screenshots and logs;
- validation and HITL traces;
- repeated raw evaluation data, with failures retained;
- processed reliability and latency metrics; and
- final implementation evidence.
