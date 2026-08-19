# Research Questions

**Status:** Locked in Step 1

**Constraint:** The core questions do not depend on a validator/two-agent architecture.

## RQ1

**How accurately and consistently does the extended n8n-based agentic decision layer produce the expected IoT action across defined normal, malformed, and state-dependent test cases?**

### What it measures

- exact expected-action accuracy
- consistency across repeated runs of the same case
- handling of normal high/low and threshold inputs
- behavior on malformed or missing input
- behavior in at least one frozen state-dependent case using the one bounded-memory configuration
- failure categories rather than only an aggregate success rate

### Planned evidence

- Step 5 frozen test-case definitions, including at least one state-dependent/bounded-memory case with an explicit expected state transition or expected state-dependent outcome
- versioned workflow/model/prompt/memory configuration identifiers
- raw structured outputs for every repetition
- expected-versus-observed action records
- per-case and aggregate correctness/consistency summaries
- retained malformed, failed, timed-out, or ambiguous runs

### Feeding steps

- Step 5 freezes cases and expected results, including the required state-dependent case and its expected state transition or state-dependent outcome.
- Steps 6-9 establish the baseline and extended workflow configurations.
- Step 10 runs the repeated evaluation and executes the frozen state-dependent case with the one bounded-memory configuration.
- Step 11 freezes evidence.
- Steps 12-14 report and interpret the results.

## RQ2

**How effectively do runtime structured-output validation, action policies, and Human-in-the-Loop approval prevent invalid or risky agent actions from reaching the shared IoT action interface?**

### What it measures

- rejection of malformed structured output
- rejection of missing, extra, or wrongly typed fields
- rejection of unsupported actions and targets
- correct routing of approval-required actions
- actual approve/reject behavior at runtime
- whether any invalid or unapproved risky action reaches `/fan/on` or `/fan/off`
- false blocks or incorrect releases, if observed

### Planned evidence

- runtime validator outcomes and reason codes
- deterministic policy decisions
- HITL request, reviewer decision, and post-decision execution records
- middleware/action endpoint logs showing execution or non-execution
- allowed, blocked, and risky case traces
- negative evidence and raw failures retained unchanged

### Feeding steps

- Step 5 freezes malformed, unsupported, and risky cases.
- Step 8 implements runtime validation and policy enforcement.
- Step 9 implements actual HITL behavior.
- Step 10 repeats safety and approval cases.
- Step 11 freezes the evidence.
- Steps 12-14 report and discuss effectiveness and limits.

## RQ3

**What reliability and latency differences are observed between the inherited minimal agent baseline and the extended Obid agentic workflow under the same defined IoT test cases?**

### What it measures

- difference in expected-action success rate
- difference in run-to-run consistency
- difference in blocked/failed/timeout rates
- automated processing latency under a common comparable automated case subset
- separately reported HITL component and total elapsed times, without mixing human wait time into the automated baseline-versus-Obid comparison

### Planned evidence

- a verified, versioned inherited minimal-agent baseline
- a versioned Obid workflow configuration
- a common comparable automated case subset and identical repetition rules for the baseline-versus-Obid automated latency result
- raw start/end timestamps or monotonic elapsed-time records
- per-configuration latency distributions and reliability summaries
- exclusion of human approval wait time from the automated baseline-versus-Obid latency comparison
- for HITL cases, separate records where technically possible for automated processing before the wait, human wait time, automated processing after approval/rejection, and total HITL elapsed time
- HITL human wait time reported separately and never merged into the main automated baseline-versus-Obid latency result
- an explicit instrumentation limitation whenever a timing component cannot be separated; no component is guessed

### Feeding steps

- Step 5 freezes the common comparable automated case subset and the separate HITL timing rules.
- Step 6 verifies the inherited baselines.
- Steps 7-9 create the extended Obid configuration.
- Step 10 runs the comparison.
- Step 11 freezes raw and processed evidence.
- Steps 12-14 present and interpret the differences.

## Evaluation direction locked in Step 1

Step 5 will generate and freeze the actual dataset. It must include at least:

- normal high-temperature case
- normal low-temperature case
- threshold/boundary case
- malformed or missing input
- unsupported/invalid action
- risky/HITL case
- at least one state-dependent/bounded-memory case using the one bounded-memory configuration, with an explicit expected state transition or expected state-dependent outcome

Step 5 must record each relevant case's injection point, component under test, expected terminal stage, expected outcome, and ownership/attribution of that outcome. Step 10 must execute the frozen state-dependent case. The case remains narrow and does not introduce a comparison of memory strategies.

## Malformed-case attribution locked in Step 1

- Malformed sensor-event handling performed by inherited Yacoub middleware is integration/context evidence and is not automatically counted as Obid agent decision correctness.
- Malformed or invalid agent-generated action output tested against Obid runtime validation or policy belongs to RQ2.
- RQ1 malformed cases must be injected and terminated so that the measured behavior is attributable to the Obid decision layer.

The preferred initial target is **five repetitions per case per evaluated core configuration**, subject to Step 5 finalization. This is a plan, not a claim that runs have occurred.

## Interpretation limits

- Results apply to the frozen scenario, workflow, model, prompt, memory, and runtime configuration.
- The study does not establish production safety, broad scalability, hardware generality, or model-family superiority.
- Optional validator-agent results, if later produced, are supplementary and do not redefine RQ1-RQ3.
