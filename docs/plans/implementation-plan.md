# Obid Tier 1.5 Implementation Plan

**Plan status:** Scope-locked in Step 1

**Execution rule:** Implement only the currently requested numbered step

**Strategy:** Complete the smallest evidence-producing system that answers RQ1-RQ3

## Narrowed strategy

```text
scope lock
  -> preserve collaboration interface
  -> verify handoff baseline
  -> extend cognitive layer
  -> implement reliability layer
  -> evaluate repeatedly
  -> freeze
  -> write from evidence
```

This sequence protects the Yacoub-Obid ownership boundary and ensures that Obid's thesis contribution is the extended agentic decision and reliability layer, not inherited workflow/action infrastructure.

## 1. Scope lock

Step 1 fixes the contribution, research questions, Tier 1.5 pass condition, exclusions, provenance rules, and 14-step process before implementation starts.

Control points:

- one controlled temperature-to-fan scenario
- one primary model configuration
- one main single-agent design
- one bounded-memory configuration
- runtime validation, deterministic policy, and actual HITL are mandatory
- repeated evaluation is mandatory
- validator/two-agent work is optional

## 2. Preserve the collaboration interface

Obid must integrate through the frozen Yacoub-compatible boundaries:

- sensor event: `sensor_id`, `timestamp`, `type`, `value`, `unit`
- allowed actions: `fan_on`, `fan_off`
- allowed target: `fan_1`
- action fields: `action_id`, `target`, `reason`, `requires_approval`
- middleware routes: `/status`, `/sensor-event`, `/fan/on`, `/fan/off`
- inherited deterministic threshold: `value >= 30.0 C -> fan_on`, otherwise `fan_off`

The interface will be adopted and frozen before the Obid decision layer is built. If a mismatch blocks execution, work stops for an explicit compatibility decision; the contract is not silently edited.

## 3. Verify the handoff baseline

The inherited deterministic and minimal-agent baselines must run in the same controlled Obid environment used for later comparison.

Verification must establish:

- exact n8n version and workflow export identity
- exact primary baseline model name/version and relevant settings
- stateless/no-memory baseline status
- matching high/low behavior through the inherited fan endpoints
- raw execution evidence and known limitations
- provenance labels separating verification work from Yacoub authorship

The frozen minimal agent JSON is not sufficient by itself because it omits the connected Google model node shown in runtime evidence. This must be resolved in Step 6, not assumed in Step 1.

## 4. Extend the cognitive layer

The main Obid workflow will add the smallest stronger decision layer needed to study agentic behavior:

- one documented system prompt
- explicit tool definitions and use
- controlled ReAct-style behavior with bounded iterations/actions
- one bounded-memory configuration with explicit inclusion/eviction/reset rules
- structured output conforming to the inherited action contract

The extended workflow remains one agent. Broad autonomy, multiple models, multiple devices, and production orchestration remain out of scope.

## 5. Implement the reliability layer

Reliability is implemented as runtime behavior, not documentation:

1. parse and validate the structured action against the frozen schema;
2. apply deterministic action/target/approval policy;
3. block invalid output with an observable reason;
4. route valid approval-required output into an actual HITL wait;
5. record approve/reject decisions;
6. release only already-valid, approved actions;
7. prove that blocked or rejected actions do not call either fan endpoint.

Validation, policy, and HITL are separate observable stages so RQ2 can attribute outcomes correctly.

## 6. Evaluate repeatedly

Step 5 will freeze the actual cases and run protocol. At minimum the cases will cover:

- normal high temperature
- normal low temperature
- threshold/boundary behavior
- malformed or missing input
- unsupported/invalid action
- risky/HITL behavior
- state-dependent/bounded-memory behavior if feasible

The preferred initial target is five repetitions per case per evaluated core configuration, subject to Step 5 finalization. Comparable inherited-baseline and Obid runs use the same cases and record configuration IDs, action outcomes, validation/policy/HITL outcomes, errors, and end-to-end latency.

Human wait time should be separated from automated processing time where feasible. Missing or failed measurements are recorded as missing/failed, not replaced or discarded.

## 7. Freeze implementation and evidence

After repeated evaluation:

- stop feature work;
- identify the final commit/configuration;
- retain raw outputs and failures unchanged;
- generate traceable summaries from raw evidence;
- inventory figures, logs, tables, and configuration files;
- allow only narrow corrections required for accuracy or reproducibility.

Optional validator/two-agent work is skipped unless the core is already stable and its addition cannot invalidate or delay the freeze.

## 8. Write from evidence

Thesis writing follows the frozen artifacts:

- design claims trace to decisions and configurations;
- implementation claims trace to versioned files and runtime proof;
- results trace to raw and processed evaluation evidence;
- discussion distinguishes observation, interpretation, limitation, and future work;
- inherited Yacoub contributions are cited as inherited at every relevant boundary.

No result, run count, safety outcome, or hardware claim may be written before evidence exists.

## Evidence discipline

Every reportable run should later preserve, where feasible:

- case ID and repetition number
- configuration and workflow identifiers
- input event
- raw model output
- parsed structured output or parse failure
- validator and policy outcome/reason
- HITL request and decision, if applicable
- endpoint called or proof of no endpoint call
- observed fan result
- timing fields
- error/timeout notes

Exact schemas and storage locations are Step 5 work and are not created in Step 1.

## Risk controls

| Risk | Control |
| --- | --- |
| Scope expands to professor brief's broad suggestions | Treat multi-agent, multi-model, multi-device, hardware, and scalability work as optional/out of scope |
| Yacoub work is misattributed | Preserve commit/path provenance and label inherited evidence |
| Contract drift | Freeze exact fields/actions/targets; require explicit decision for change |
| Safety exists only on paper | Require runtime validation, policy, endpoint non-execution proof, and actual HITL |
| Baseline is not reproducible | Resolve missing exact Gemini/export configuration in Step 6 |
| Evaluation hides failures | Retain raw failures and report denominators/failure categories |
| Optional comparison consumes core time | Gate it after Step 9 stability and before Step 10 only if harmless |
| Report outruns evidence | Freeze evidence before substantive results claims |

## Plan completion condition

This implementation plan succeeds when the frozen Tier 1.5 system answers RQ1-RQ3 with repeated, traceable evidence while remaining compatible with and correctly attributing the Yacoub handoff.
