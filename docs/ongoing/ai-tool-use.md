# AI Tool Use Convention

**Established:** Step 2

**Purpose:** Provide a concise methodology and evidence convention for later disclosure and reproducibility of Codex/AI assistance. This file is not a chat diary.

## Principle

AI-generated or AI-modified work is not automatically correct, complete, original to Obid, or supported by evidence. It must pass the same human verification, runtime verification, provenance checks, and audit gate as other work.

## What to record

For a material AI-assisted task, record the following where relevant:

- **Role/thread:** for example `step-runner-obid`, `audit-review-obid`, `repair-fix-obid`, or `report-scribe-obid`.
- **Task/step:** the bounded request and numbered thesis step.
- **AI contribution:** what was drafted, generated, analyzed, or changed.
- **Affected artifacts:** exact repository paths.
- **Provenance:** whether inputs/outputs are `YACOUB_INHERITED`, `SHARED_INTERFACE`, `OBID_CREATED`, `TEST_DOUBLE`, or `REFERENCE_ONLY`.
- **Human verification:** review, command, UI action, comparison, or judgment performed by the researcher.
- **Audit result:** `PASS` or `REPAIR REQUIRED`, including the review reference when available.
- **Repair result:** accepted finding and bounded correction, if applicable.
- **Final evidence:** report note, manifest, source file, log, screenshot, export, or result path.
- **Limitations:** missing manual action, unavailable evidence, unresolved check, or tool limitation.

## Where to record it

Use the smallest artifact appropriate to the step:

- the step report-support note under `docs/report-notes/` for the concise narrative;
- a step-specific evidence or configuration manifest when runtime/evaluation detail later requires one;
- Git history for the exact repository change;
- `docs/decisions.md` only when a genuine project decision was made.

Do not duplicate the same long narrative across all locations.

## Concise entry pattern

Later step notes or manifests may use this pattern:

```text
Role/thread:
Step/task:
AI contribution:
Artifacts:
Provenance:
Human verification:
Audit verdict:
Repair, if any:
Final evidence:
Limitations/checks:
```

The fields are guidance, not a requirement to create empty placeholders.

## Human verification expectations

Verification should match the risk and claim:

- documentation changes: source comparison, link/path checks, diff review, and audit;
- configuration changes: parse/import/version checks and documented environment;
- runtime changes: actual execution evidence, expected-versus-observed behavior, and retained failures;
- evaluation changes: frozen protocol, traceable raw data, reproducible aggregation, and denominator checks;
- provenance-sensitive reuse: frozen commit/path comparison and explicit attribution.

If verification cannot be performed, record the work as pending or limited. Do not convert an AI suggestion into an observed result.

## What not to store

- full chat histories or routine conversational turns
- huge master prompts in repository guidance
- secrets, API keys, credentials, tokens, or private personal data
- hidden/internal chain-of-thought
- fabricated transcripts, screenshots, logs, runs, or audit verdicts

Store only the concise information needed to explain material assistance, verification, and evidence lineage.

## Relationship to thesis reporting

This convention supports the later Methodology, AI-tool-use disclosure, reproducibility discussion, and appendix. Final reporting must distinguish AI assistance, human verification, inherited collaborator material, and Obid-authored contribution.
