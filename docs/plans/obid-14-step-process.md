# Obid 14-Step Thesis Process

**Process status:** Locked in Step 1

**Execution rule:** Only the explicitly requested current step may be executed

**Minimum target:** Tier 1.5 Obid decision/reliability layer on the frozen Yacoub-compatible workflow-to-action system

## Process-wide controls

- The current task, root `AGENTS.md`, and active Obid planning documents outrank historical reference material.
- `reference/` and the upstream Yacoub repository are read-only.
- Yacoub-authored implementation and evidence remain inherited and must be labeled as such.
- Shared contracts and endpoint semantics cannot change silently.
- Each step ends with a bounded completion gate before the next step begins.
- Raw failures and negative evidence are retained.
- Optional validator/multi-agent work never displaces validation, HITL, repeated evaluation, or report quality.
- Thesis prose follows frozen evidence; planned behavior is not presented as an observed result.

# Phase 1 - Collaboration and project foundation

## Step 1 - Lock Obid scope and the Yacoub-Obid collaboration boundary

### Goal

Freeze the thesis contribution, collaboration/provenance boundary, research questions, Tier 1.5 pass condition, evaluation direction, out-of-scope work, and numbered process before implementation begins.

### Work to complete

- Inspect the root instructions, bootstrap README, handoff reference, approved Obid plan, professor assignment, frozen Yacoub commit, relevant handoff artifacts, and the successful structure of Yacoub's bounded process.
- Verify exact sensor/action contracts, action values/target, middleware routes, deterministic baseline, minimal agent baseline, memory choice, model evidence, and actual safety/HITL state.
- Reconcile meaningful scope contradictions without hiding them.
- Lock RQ1-RQ3, ownership, provenance, compatibility, Tier 1.5, and the 14-step process.

### Expected artifacts

- `docs/plans/obid-14-step-process.md`
- `docs/plans/implementation-plan.md`
- `docs/ongoing/project-overview.md`
- `docs/ongoing/obid-scope.md`
- `docs/ongoing/research-questions.md`
- `docs/ongoing/collaboration-boundary.md`
- `docs/ongoing/yacoub-handoff.md`
- `docs/ongoing/report-outline.md`
- `docs/decisions.md`

### Evidence required

- frozen commit and upstream branch verification
- exact source paths in the active handoff
- documented contradictions and `[CHECK]` items
- clean Markdown/path checks where practical
- `git diff --check`, status, and diff summary
- confirmation that `reference/` did not change

### Which thesis chapters it feeds

- Chapter 1: aim, RQs, scope, limitations, division of work
- Chapter 3: bounded evidence-first method
- Chapter 4: contribution and architecture boundary
- Chapter 7: scope and validity limitations

### Explicit boundaries / what must not be started

- No n8n, Docker, middleware, workflow, schema, prompt, memory, ReAct, validator, policy, HITL, evaluation, or report implementation.
- No full Step 2 repository structure.
- No changes or copies from `reference/`.

### Completion criteria

- All nine requested documents exist and agree on ownership, RQs, Tier 1.5, and exclusions.
- Exact frozen handoff semantics and gaps are recorded with source paths.
- Validation checks pass or all exceptions are reported.
- Step 2 has not started.

## Step 2 - Build the Obid repository/Codex foundation and document the Yacoub handoff

### Goal

Create the smallest active repository structure and working conventions needed for reproducible Obid implementation while keeping inherited Yacoub material frozen and traceable.

### Work to complete

- Create only the approved active implementation, evidence, and documentation directories.
- Establish naming, configuration, raw-evidence, and provenance conventions.
- Convert Step 1 handoff findings into reproducible read-only source references and a handoff verification checklist.
- Document how Codex/AI assistance and human verification will be recorded.
- Confirm repository commands, branch/commit discipline, and ignore rules.

### Expected artifacts

- approved active repository directory skeleton
- repository working/contribution guide updates
- provenance and evidence naming conventions
- handoff verification checklist
- AI-tool-use recording convention
- Step 2 report note/evidence record

### Evidence required

- tree listing of the approved structure
- link/path validation
- proof no Yacoub artifact was silently copied or modified
- version-control status and review record

### Which thesis chapters it feeds

- Chapter 3: development, evidence, version control, and AI-tool methodology
- Chapter 4: repository and collaboration organization
- Appendix: reproducibility and artifact map

### Explicit boundaries / what must not be started

- Do not bring up n8n or create Docker/runtime files intended for Step 3.
- Do not adopt/copy contracts, build workflows, implement agents, or define evaluation cases.
- Do not change the Step 1 scope without a new explicit decision.

### Completion criteria

- The repository has a minimal reviewed foundation for Steps 3-11.
- Evidence/provenance conventions distinguish Yacoub sources from Obid outputs.
- The handoff checklist identifies every unresolved compatibility item for later steps.
- No runtime functionality has begun.

# Phase 2 - Shared runtime and compatibility

## Step 3 - Bring up Obid's n8n environment and verify Yacoub compatibility

### Goal

Establish a reproducible Obid n8n runtime compatible with the frozen Yacoub workflow exports and network assumptions.

### Work to complete

- Pin and document the n8n/runtime environment.
- Start the minimal local runtime.
- Compare the selected version with Yacoub's pinned `n8nio/n8n:1.123.37` and record any narrowly required compatibility choice.
- Verify UI availability, persistence, relevant built-in/LangChain node availability, and host-to-container networking assumptions.
- Do not yet build or modify thesis workflows.

### Expected artifacts

- minimal runtime configuration
- exact version/configuration record
- startup and persistence instructions
- runtime proof logs/screenshots
- compatibility findings and Step 3 report note

### Evidence required

- successful startup and UI access
- exact image/version identifiers
- restart/persistence proof appropriate to the setup
- availability/compatibility check for required Yacoub node types
- recorded failures or deviations

### Which thesis chapters it feeds

- Chapter 3: reproducible environment
- Chapter 4: platform/version choice
- Chapter 5: runtime setup

### Explicit boundaries / what must not be started

- No integration adapter, contract adoption, evaluation cases, baseline execution, Obid agent, validation, or HITL.
- No PostgreSQL, Prometheus/Grafana, MCP, Pi deployment, or n8n core modification unless separately authorized.

### Completion criteria

- The pinned runtime starts reproducibly and exposes the node/runtime capabilities needed for the handoff.
- Compatibility deviations are resolved narrowly or explicitly blocked; none are hidden.
- Step 4 can test the interface without changing shared contracts.

## Step 4 - Establish the Yacoub-compatible integration test boundary

### Goal

Prove the exact sensor-to-n8n and n8n-to-middleware seams that later workflows will use, without adding agent intelligence.

### Work to complete

- Bring up or reference the inherited middleware/action boundary without redesigning it.
- Verify `/status`, `/sensor-event`, `/fan/on`, and `/fan/off` semantics.
- Verify `N8N_WEBHOOK_URL`, Docker host alias, webhook test/active modes, and endpoint reachability.
- Exercise a minimal compatible event and direct simulated fan actions.
- Record request/response shapes, network addresses, and observable non-hardware behavior.

### Expected artifacts

- integration-boundary test plan
- environment/endpoint map
- minimal non-agent test workflow or disposable test receiver, if required and explicitly bounded
- request/response transcripts and screenshots
- compatibility findings and Step 4 report note

### Evidence required

- middleware status proof
- accepted compatible sensor event
- event observed at the n8n boundary
- observable simulated `fan_on` and `fan_off` results
- malformed request behavior recorded without inventing schema enforcement

### Which thesis chapters it feeds

- Chapter 3: integration verification method
- Chapter 4: shared boundary design
- Chapter 5: network and API integration

### Explicit boundaries / what must not be started

- Do not adopt/change schemas or freeze evaluation cases before Step 5.
- Do not implement deterministic/agent baselines, Obid cognition, runtime safety, memory, HITL, or evaluation scripts.
- Do not rebuild Yacoub middleware or add real GPIO.

### Completion criteria

- Both seams work with the documented Yacoub-compatible semantics.
- Exact Obid webhook URL/path and forwarding configuration are recorded.
- No contract or middleware redesign was introduced.

## Step 5 - Adopt/freeze the shared contracts and freeze Obid's evaluation cases

### Goal

Create the versioned experimental boundary: adopt the inherited contracts with provenance and freeze the cases, expected outcomes, metrics, repetition rules, and evidence format used by all later configurations.

### Work to complete

- Adopt the exact frozen sensor-event and action contracts without claiming authorship.
- Add provenance and compatibility checks around the adopted copies/references.
- Define expected outcomes for normal high, normal low, `30.0 C` boundary, malformed/missing input, unsupported/invalid action, risky/HITL, and state-dependent/bounded-memory behavior if feasible.
- Define comparison configurations, run-order controls, timing boundaries, success/failure categories, and handling of missing data.
- Finalize the repetition count; start from the preferred target of five per case/configuration.
- Define a valid `requires_approval: true` case without expanding allowed actions/targets.

### Expected artifacts

- provenance-labeled shared contract artifacts or immutable references
- contract compatibility checks
- frozen evaluation dataset/case catalog
- expected-outcome oracle
- evaluation protocol and metrics definitions
- raw-evidence format/schema and Step 5 report note

### Evidence required

- JSON/schema parse checks
- contract comparison against frozen Yacoub commit
- review showing every required case category is represented
- unambiguous expected action/control outcome per case
- documented repetition and timing rules

### Which thesis chapters it feeds

- Chapter 3: experiment design and measurement
- Chapter 4: contract and test-boundary choice
- Chapter 5: data/contract implementation
- Chapter 6: result table structure
- Chapter 7: validity and limitations

### Explicit boundaries / what must not be started

- Do not execute reportable experimental runs.
- Do not implement or upgrade baselines, the Obid agent, validation, policy, or HITL.
- Do not broaden actions, targets, devices, models, or RQs.

### Completion criteria

- Contracts match the frozen handoff exactly or an explicit blocking contradiction is reported.
- Cases and expected results are frozen and versioned.
- The protocol can answer RQ1-RQ3 and retains every failed run.
- No result is claimed and no dataset outcome is fabricated.

# Phase 3 - From handoff baseline to Obid contribution

## Step 6 - Establish the Yacoub handoff baselines

### Goal

Produce reproducible, provenance-labeled deterministic and minimal-agent comparison anchors in the Obid environment before any Obid cognitive upgrade.

### Work to complete

- Import/verify the deterministic workflow and exact `>= 30.0 C` rule.
- Import/recreate the minimal agent baseline faithfully.
- Resolve the missing connected model node/export gap.
- Record exact Google Gemini model name/version, relevant generation settings, prompt identity, and stateless/no-memory choice.
- Run only the bounded baseline verification cases needed to prove readiness.
- Keep Yacoub authorship explicit in all active copies/configurations and evidence.

### Expected artifacts

- reproducible deterministic baseline configuration/export
- reproducible minimal-agent baseline configuration/export
- exact baseline model/prompt/memory manifest
- baseline provenance manifest
- readiness verification logs/screenshots and Step 6 report note

### Evidence required

- deterministic high/low/boundary routing proof
- minimal-agent high/low structured output and endpoint proof
- proof no memory node/ReAct/safety/HITL was added to the inherited baseline
- exact config/version capture
- documented compatibility repairs, if any

### Which thesis chapters it feeds

- Chapter 3: comparison controls
- Chapter 4: inherited baseline selection
- Chapter 5: verified integration baseline
- Chapter 6: comparison anchor description
- Chapter 7: baseline limitations

### Explicit boundaries / what must not be started

- Do not add Obid ReAct, tools, bounded memory, runtime validation, action policy, HITL, or repeated evaluation.
- Do not improve the baseline under the guise of reproducing it.
- Do not claim the baselines as Obid-authored.

### Completion criteria

- Both baseline configurations are reproducible and compatible in the Obid runtime.
- The exact minimal-agent model and settings are recorded.
- The configurations are ready to receive the Step 5 cases later without additional semantic changes.

## Step 7 - Upgrade the handoff into the real Obid single-agent system

### Goal

Implement the bounded Obid-owned cognitive contribution while preserving the inherited input/action semantics.

### Work to complete

- Implement one main agent workflow and system prompt.
- Define explicit tools and prove controlled tool selection/use.
- Implement bounded ReAct-style behavior with limits on iterations, tools, and actions.
- Implement one bounded-memory configuration with documented reset, inclusion, and eviction behavior.
- Produce structured action output matching the inherited action contract.
- Add configuration identifiers and raw reasoning/tool/memory trace evidence appropriate to the platform without exposing secrets.

### Expected artifacts

- main Obid workflow export
- system prompt and tool definitions
- controlled ReAct configuration/design note
- bounded-memory configuration/design note
- structured-output configuration
- narrow cognitive verification evidence and Step 7 report note

### Evidence required

- normal high/low/boundary decisions in an isolated or simulated path
- explicit tool-use trace
- bounded iteration/termination proof
- memory inclusion/eviction/reset proof
- contract-shaped raw output examples, including retained failures

### Which thesis chapters it feeds

- Chapter 2: applied agent/tool/ReAct/memory concepts
- Chapter 4: Obid cognitive design
- Chapter 5: main agent implementation
- Chapter 7: cognitive tradeoffs and limits

### Explicit boundaries / what must not be started

- Do not claim runtime safety from structured output alone.
- Do not implement the Step 8 validator/policy or Step 9 HITL prematurely.
- Do not add multiple agents/models/devices, MCP, real GPIO, or broad autonomy.
- Any valid action execution before Step 8 must remain narrowly controlled and clearly non-safety evidence.

### Completion criteria

- One Obid agent demonstrably uses the intended tools, bounded ReAct behavior, and bounded memory.
- It emits the frozen action shape without changing the shared contract.
- Its behavior/configuration is versioned and ready for the runtime reliability layer.

## Step 8 - Convert the documented safety design into runtime validation and policy enforcement

### Goal

Make structured-output validation and deterministic action policy executable, observable, and capable of preventing invalid output from reaching the inherited fan endpoints.

### Work to complete

- Parse output with explicit error handling.
- Validate the full frozen action schema at runtime, including required fields, types, enum/target, and no extra fields.
- Apply a deterministic action policy after schema validation.
- Produce stable allowed/blocked/approval-required outcomes and reason codes.
- Prove invalid, unsupported, or malformed output cannot call `/fan/on` or `/fan/off`.
- Prepare the approval-required branch for Step 9 without pretending a real human interaction exists yet.

### Expected artifacts

- runtime validator implementation/workflow nodes
- deterministic policy implementation
- validation/policy outcome format
- negative-case runtime traces
- endpoint non-execution evidence
- updated architecture/config documentation and Step 8 report note

### Evidence required

- allowed valid `fan_on` and `fan_off` path proof
- malformed JSON and missing/extra/wrong-type field rejection
- unsupported action/target rejection
- valid approval-required classification
- logs showing no fan endpoint call for blocked outputs

### Which thesis chapters it feeds

- Chapter 2: structured validation and policy concepts
- Chapter 4: reliability-layer design
- Chapter 5: validator/policy implementation
- Chapter 6: preliminary control outcomes
- Chapter 7: limitations of deterministic controls

### Explicit boundaries / what must not be started

- Do not claim actual HITL until Step 9 supplies a real approve/reject interaction.
- Do not add a validator agent, multi-agent architecture, repeated full evaluation, or new contracts.
- Do not move enforcement into or redesign Yacoub middleware unless explicitly authorized.

### Completion criteria

- Every action reaching a fan endpoint has first passed runtime schema validation and deterministic policy.
- Required negative cases are blocked with observable reasons and endpoint non-execution proof.
- The approval-required branch is well defined for actual HITL implementation.

## Step 9 - Implement actual HITL behavior and, only if the core is stable, an optional validator-agent comparison

### Goal

Complete the core reliability path with a real, auditable human approval interaction that controls whether a valid risky action can proceed.

### Work to complete

- Implement an actual pause/wait or approval mechanism supported by the chosen n8n setup.
- Present the input/action/policy context needed for a human decision.
- Accept only explicit approve/reject decisions.
- On approval, release only an already schema-valid, policy-eligible action.
- On rejection/timeout, prevent action execution and record the outcome.
- Verify resume/retry/idempotency behavior narrowly enough for the scenario.
- Assess core stability. Only then decide whether a minimal validator-agent comparison is safe and useful.

### Expected artifacts

- HITL workflow/path and reviewer interaction definition
- approve, reject, and timeout/error traces
- post-decision endpoint/non-endpoint evidence
- core stability checklist
- explicit include/defer decision for optional validator-agent work
- optional supplementary workflow/evidence only if approved and safe
- Step 9 report note

### Evidence required

- one actual approval that releases a valid action
- one actual rejection that prevents action execution
- reviewer decision audit record
- proof invalid actions cannot be approved around the schema/policy gate
- timeout/error behavior record
- stability evidence before any optional work begins

### Which thesis chapters it feeds

- Chapter 2: HITL/oversight concepts
- Chapter 4: approval architecture and optional-design decision
- Chapter 5: actual HITL implementation
- Chapter 6: approval/rejection outcomes
- Chapter 7: human latency, oversight, and limitations

### Explicit boundaries / what must not be started

- Do not make optional validator/two-agent work a core dependency.
- Do not compare multiple models/devices or expand the RQs.
- Do not begin the full repeated evaluation before all core paths pass readiness checks.

### Completion criteria

- Runtime validation, policy, and actual HITL form one end-to-end enforced path.
- Approve/reject behavior is observable, auditable, and endpoint-safe.
- The core is declared ready for repeated evaluation.
- Optional validator work is either explicitly deferred or completed without displacing the core.

# Phase 4 - Evaluation and freeze

## Step 10 - Run the repeated reliability evaluation

### Goal

Execute the frozen Step 5 protocol against the identified core configurations and collect the raw evidence needed to answer RQ1-RQ3.

### Work to complete

- Lock exact runtime/model/workflow/prompt/memory/validator/policy/HITL configuration IDs.
- Run the frozen cases with the finalized repetition count.
- Use the same applicable cases for the inherited minimal-agent baseline and extended Obid workflow.
- Record raw model/action/control/endpoint/timing outcomes for every attempt.
- Separate automated processing latency from human wait time where feasible.
- Summarize accuracy, consistency, blocked/released outcomes, failures, and latency without altering raw data.

### Expected artifacts

- immutable raw run records
- configuration/run manifest
- processed reliability and latency summaries
- RQ1/RQ2/RQ3 evidence tables/figures
- failure/missing-data inventory
- evaluation execution note and Step 10 report note

### Evidence required

- required repetition count achieved or an explicit deviation with reason
- every planned case/configuration represented
- traceability from summaries to raw run IDs
- retained failures, rejects, timeouts, and missing measurements
- calculation/aggregation verification

### Which thesis chapters it feeds

- Chapter 3: actual execution protocol
- Chapter 5: evaluation instrumentation
- Chapter 6: primary results
- Chapter 7: interpretation and validity

### Explicit boundaries / what must not be started

- No new features, prompts, memory strategies, models, devices, or case changes during reportable runs.
- Do not rerun selectively to replace failures.
- Do not delete, hand-edit, or fabricate raw outcomes.
- Do not begin full chapter prose before the run set is reviewed.

### Completion criteria

- The finalized run matrix is complete or transparently qualified.
- Summaries reproduce from raw evidence and directly support RQ1-RQ3.
- Negative and missing outcomes remain visible.

## Step 11 - Freeze implementation and final evidence

### Goal

Stop feature development and establish the exact implementation/evidence state used by the thesis.

### Work to complete

- Identify final commit, workflow exports, configurations, and dependency versions.
- Inventory raw/processed results, logs, screenshots, figures, and limitations.
- Verify every planned report claim can trace to evidence.
- Check provenance labels and Yacoub/Obid separation.
- Permit only narrow bug/documentation fixes required for accuracy, then refreeze if necessary.
- Record known failures and unresolved limitations.

### Expected artifacts

- implementation freeze record
- evidence manifest/checksums or equivalent integrity record
- final architecture diagram
- claim-to-evidence/RQ matrix
- provenance audit
- final limitations and unresolved-items list
- Step 11 report note

### Evidence required

- clean or fully explained version-control state
- reproducible final configuration identifiers
- raw-to-summary integrity check
- link/path and evidence inventory validation
- explicit no-new-feature declaration

### Which thesis chapters it feeds

- Chapter 3: final method/configuration
- Chapter 4: final design
- Chapter 5: final implementation
- Chapter 6: frozen results
- Chapter 7: limitations
- Appendix: reproducibility package

### Explicit boundaries / what must not be started

- No new workflow, model, device, architecture, optional agent, case, or measurement axis.
- No rewriting raw evidence.
- Do not alter frozen behavior to improve reported results.

### Completion criteria

- One exact implementation/evidence state is designated for the report.
- RQ evidence and provenance are complete and reviewable.
- Remaining work is thesis production, not system expansion.

# Phase 5 - Thesis production

## Step 12 - Write Choice of Approach, Implementation, and Results

### Goal

Draft Chapters 4-6 directly from the frozen design, implementation, and evaluation evidence.

### Work to complete

- Write Choice of Approach/System Design with alternatives and ownership boundary.
- Write Implementation with reproducible Obid details and concise inherited integration context.
- Write Results as observations organized by RQ and frozen tables/figures.
- Add precise artifact/evidence references and provenance labels.
- Keep interpretation largely for Discussion.

### Expected artifacts

- draft Chapter 4
- draft Chapter 5
- draft Chapter 6
- figures/tables with source mapping
- chapter-level claim/evidence checklist

### Evidence required

- each technical claim maps to the Step 11 state
- each result maps to raw/processed evidence
- run counts and denominators are exact
- inherited artifacts are attributed to Yacoub
- figures/tables are reproducible and captioned accurately

### Which thesis chapters it feeds

- Chapter 4: Choice of Approach / System Design
- Chapter 5: Implementation
- Chapter 6: Results

### Explicit boundaries / what must not be started

- Do not add implementation or rerun experiments to make prose easier.
- Do not hide failures or merge planned and observed behavior.
- Do not write broad Introduction/Theory/Discussion prose assigned to Step 13.

### Completion criteria

- Chapters 4-6 form a coherent artifact-backed account.
- RQ result evidence is complete and provenance-safe.
- No unsupported safety, hardware, scalability, or authorship claim remains.

## Step 13 - Write Methodology, Discussion, Introduction, and Theory/Related Work

### Goal

Complete Chapters 1-3 and 7 around the already frozen system and results.

### Work to complete

- Write Methodology from the actual bounded process, case protocol, repetitions, metrics, and evidence handling.
- Write Discussion by interpreting RQ1-RQ3, comparing literature, and analyzing validity/limitations.
- Write Introduction with the final problem, aim, RQs, scope, collaboration split, and contribution.
- Write Theory/Related Work at the depth required to support the implemented concepts and discussion.
- Reconcile terminology, citations, and cross-references with Chapters 4-6.

### Expected artifacts

- draft Chapter 1
- draft Chapter 2
- draft Chapter 3
- draft Chapter 7
- validity/limitations matrix
- literature and terminology consistency check

### Evidence required

- Methodology matches actual execution, not the original plan alone
- Discussion cites exact Results evidence
- literature supports relevant claims with no fabricated references
- collaboration and AI-tool-use disclosures are accurate
- limitations reflect the one-scenario/model scope and baseline gaps

### Which thesis chapters it feeds

- Chapter 1: Introduction
- Chapter 2: Theory and Related Work
- Chapter 3: Methodology
- Chapter 7: Discussion

### Explicit boundaries / what must not be started

- Do not introduce new results, methods, architecture, or experiments.
- Do not broaden theory into multi-agent/scalability/hardware surveys unrelated to the frozen work.
- Do not overstate generalization or production safety.

### Completion criteria

- Chapters 1-3 and 7 accurately frame and interpret Chapters 4-6.
- RQ wording is identical throughout.
- Scope, provenance, validity, and limitations are internally consistent.

## Step 14 - Finish Conclusions, front matter, references, appendix, and submission package

### Goal

Produce a complete, internally consistent, submission-ready thesis package without adding new substantive work.

### Work to complete

- Write Conclusions with direct answers to RQ1-RQ3 and scoped future work.
- Complete abstract, Swedish summary, acknowledgements, terminology, and other required front matter.
- Finalize references and verify every citation.
- Assemble appendices for reproducibility, contracts, cases, configurations, detailed evidence, and AI-tool-use disclosure as appropriate.
- Audit figures, tables, numbering, cross-references, language, template requirements, and accessibility/readability.
- Build and inspect the final submission artifact and archive the evidence/package state.

### Expected artifacts

- Chapter 8
- completed front matter
- verified bibliography
- final appendices
- final thesis source and rendered submission file
- submission/evidence package manifest
- final compliance and provenance checklist

### Evidence required

- every RQ answer traces to Chapters 6-7
- all citations resolve and all figures/tables have sources
- no inherited work is misattributed
- final rendered document passes visual and template checks
- submission files match the frozen implementation/evidence state

### Which thesis chapters it feeds

- Chapter 8: Conclusions
- front matter
- references
- appendices
- whole-report consistency

### Explicit boundaries / what must not be started

- No new implementation, experiment, model, device, architecture, or result.
- No new claim that lacks evidence in the frozen thesis state.
- No removal of negative evidence merely to simplify the appendix or conclusions.

### Completion criteria

- The thesis answers RQ1-RQ3 concisely and within scope.
- The submission package is complete, rendered, checked, provenance-safe, and traceable to frozen evidence.
- All administrative/template requirements are satisfied.
