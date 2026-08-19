# Canonical Codex Workflow

**Established:** Step 2

**Purpose:** Define the persistent role sequence and logical completion gate for bounded Obid repository work.

## Canonical sequence

```text
current explicitly requested step
  -> step-runner-obid
  -> human/manual action if unavoidable
  -> evidence captured
  -> audit-review-obid
  -> if REPAIR REQUIRED:
       repair-fix-obid
       -> repair evidence
       -> audit-review-obid again
       -> repeat bounded repair/re-audit only if still required
  -> after audit PASS: report-scribe-obid
  -> step logically complete
  -> next explicitly requested step
```

No role may use this sequence to start the next numbered step automatically.

## 1. Current step input

The current task must identify one bounded repository task or numbered thesis step. The active source-of-truth order is the current task, root `AGENTS.md`, active planning/decision documents, and only then read-only reference material.

If a direct contradiction prevents the assigned work, the active role stops and reports it instead of changing scope, contracts, ownership, or research questions.

## 2. `step-runner-obid`

The step runner is the implementation/change role.

It must:

- inspect the current tree and applicable canonical documents first;
- summarize findings, intended new files, intended updates, and step boundaries before editing;
- make only the smallest changes required by the current task;
- preserve `reference/`, inherited provenance, and existing unrelated work;
- avoid all future-step functionality;
- verify the changed state and return unresolved checks.

Its successful return means the assigned change is ready for review. It is not by itself the logical step-completion gate.

## 3. Human/manual action when unavoidable

Some later runtime steps may require a human to use a local UI, provide credentials without exposing them, approve an action, or capture evidence unavailable to automation.

When manual action is required:

- the step runner gives bounded, reproducible instructions;
- the human performs only the required action;
- secrets are not committed or pasted into evidence;
- the resulting observation is captured at an explicit evidence path;
- unperformed manual work remains an unresolved check, not a claimed success.

## 4. Evidence

Evidence must be sufficient for the current step's completion criteria and must keep ownership/configuration identity visible. Depending on the step, it may include source paths, diffs, checks, screenshots, transcripts, exported configurations, raw outputs, failures, or review notes.

Planned behavior is not runtime evidence. Failed, rejected, timed-out, malformed, missing, and unexpected outcomes are retained when they occur.

## 5. `audit-review-obid`

The audit role is read-only and does not edit.

It checks:

- current-step scope and explicit exclusions;
- correctness and internal consistency;
- Yacoub/Obid ownership and provenance;
- shared-interface compatibility;
- evidence sufficiency and claim traceability;
- required files, validation, and completion criteria.

Findings should be classified as `BLOCKER`, `MAJOR`, `MINOR`, or `NOTE`, with exact paths and a bounded repair expectation where applicable. The verdict is:

- `PASS` when no required repair remains; or
- `REPAIR REQUIRED` when an actionable finding prevents completion.

## 6. `repair-fix-obid` and re-audit

The repair role acts only on accepted audit findings. It applies the smallest bounded correction, verifies it, and does not redesign, add features, reopen scope, or start the next step.

After repair, `audit-review-obid` reviews the repaired state again. Repair is not complete merely because a patch was applied.

## 7. `report-scribe-obid`

The report-scribe role runs only after audit `PASS`. It creates or updates the concise step note under `docs/report-notes/` and records:

- what the step established;
- evidence and artifact paths;
- provenance and ownership;
- thesis chapters supported;
- limitations and unresolved later-step checks;
- evidence still required in future steps.

It does not write full thesis chapters, invent results, or turn planned functionality into completed functionality.

## Logical completion and commits

The logical step-completion gate is:

```text
audit PASS + required report-support evidence
```

A Git commit may occur before review, after a repair, after report-scribing, or at another intentional checkpoint. Commit timing is not the logical completion gate and a clean working tree does not prove that a step passed audit.

## Later report-production transition

Steps 12-14 transition primarily from implementation/evaluation work to report writing, finalization, and submission checks. Their exact bounded tasks will be defined when requested. Step 2 does not create additional permanent roles for that later phase.
