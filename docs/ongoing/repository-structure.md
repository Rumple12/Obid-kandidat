# Active Repository Structure and Conventions

**Established:** Step 2

**Status:** Foundation only; reserved areas do not imply runtime implementation exists.

## Active structure

```text
Obid-kandidat/
|-- AGENTS.md
|-- README.md
|-- .gitignore
|-- docs/
|   |-- collaboration/
|   |-- ongoing/
|   |-- plans/
|   |-- report-notes/
|   `-- decisions.md
|-- cognitive_logic/
|-- safety_layer/
|-- shared_interfaces/
|-- integration/
|-- evaluation/
`-- reference/
```

Only concise boundary READMEs are created in the reserved top-level areas during Step 2.

## Area purposes and ownership

### `docs/`

Active Obid planning, collaboration/provenance records, persistent working conventions, accepted decisions, and concise report-support notes. Step 1 documents remain canonical. Later steps update documentation only within their assigned scope.

### `cognitive_logic/`

Reserved active area for provenance-labelled inherited baselines in Step 6 and Obid-created agent workflow, prompt, tools, controlled ReAct behavior, and bounded memory in Step 7. It contains no cognitive implementation in Step 2.

### `safety_layer/`

Reserved active area for Obid-created runtime validation and deterministic policy in Step 8 and actual HITL artifacts/tests in Step 9. Frozen Yacoub safety documents remain source/specification material under `reference/` until a later step acts on them.

### `shared_interfaces/`

Reserved active area for Step 5 adoption/verification of the Yacoub-authored compatible schemas with explicit provenance. No active schema copy exists in Step 2, and no contract may drift silently.

### `integration/`

Reserved active area for the Step 4 Yacoub-compatible integration test boundary, endpoint/configuration map, and new Obid evidence. It is not a competing middleware implementation area.

### `evaluation/`

Reserved active area for the Step 5 frozen case/protocol/evidence definitions and Step 10 repeated raw and processed evaluation evidence. No dataset, case catalog, run, or result exists in Step 2.

### `reference/`

Read-only source, history, background, and collaborator material. It is not the active implementation area. Historical instructions are not active Obid instructions. Files here are never silently copied or presented as Obid-created work.

## Reference versus active artifacts

```text
reference/
  = immutable source/history/collaborator context

active top-level folders
  = Obid thesis working artifacts
  + narrowly adopted/reproduced inherited artifacts only when a later step
    requires them and records exact provenance
```

The active architecture remains Obid-owned work plus documented compatibility with the frozen Yacoub repository. It is not a copied Yacoub repository relabelled as Obid work.

## Provenance vocabulary

Use these labels in later manifests, evidence indexes, adopted-artifact notes, and report-support material when origin could be ambiguous:

| Label | Meaning |
| --- | --- |
| `YACOUB_INHERITED` | Originated in Yacoub's thesis and is reused, reproduced, configured, or verified by Obid without transferring authorship. |
| `SHARED_INTERFACE` | A collaboration interface whose original authorship and frozen source remain traceable; compatibility is required. |
| `OBID_CREATED` | Created as part of the Obid thesis in an authorized numbered step. |
| `TEST_DOUBLE` | A local substitute that faithfully emulates a documented Yacoub-compatible boundary; it is never represented as Yacoub middleware. |
| `REFERENCE_ONLY` | Source, history, background, or collaborator evidence that is not part of the active Obid implementation. |

One artifact may need two dimensions in prose, for example a Yacoub-authored schema used as a `SHARED_INTERFACE`. Do not mechanically label every Markdown line. Apply labels where they prevent authorship, compatibility, or evidence ambiguity.

Future artifacts receive labels only when they actually exist.

## Evidence naming convention

Use short filenames that retain the identifiers needed to trace the evidence. Prefer:

```text
step-<NN>_<artifact-or-case>[_cfg-<configuration>][_run-<NN>][_<UTC timestamp>].<ext>
```

Use only the components that add value. Examples of future names, not created evidence:

- `step-04_status-boundary_20260819T143000Z.txt`
- `step-09_hitl-reject_cfg-obid-core_20260819T150500Z.png`
- `step-10_case-high-temp_cfg-obid-core_run-03.json`

Conventions:

- use stable step and case/configuration IDs from the applicable future protocol;
- use zero-padded run numbers when repetitions exist;
- use UTC timestamps in compact `YYYYMMDDTHHMMSSZ` form when time disambiguation matters;
- keep provenance/configuration identity in the filename or an adjacent manifest;
- preserve raw failures and error outputs under their actual run IDs;
- never create placeholder evidence that could be mistaken for a real run.

The Step 5 protocol may refine evidence fields and storage paths without changing these lightweight traceability goals.

## Population by numbered step

| Area | First planned population step | Boundary |
| --- | --- | --- |
| `integration/` | Step 4 | Verify the shared boundary; no competing middleware architecture. |
| `shared_interfaces/` | Step 5 | Adopt/verify exact compatible contracts with provenance; no silent drift. |
| `evaluation/` | Step 5 | Freeze cases/protocol/format; reportable repeated results wait until Step 10. |
| `cognitive_logic/` | Step 6 | Establish inherited baselines first; Obid cognitive implementation follows in Step 7. |
| `safety_layer/` | Step 8 | Runtime validator/policy in Step 8; actual HITL in Step 9. |
| `docs/report-notes/` | After each audit `PASS` | Concise report support only; no full thesis prose. |

Runtime infrastructure is intentionally absent. Step 3 decides and creates the minimal authorized runtime structure.
