# Shared-Interface and Yacoub Handoff Provenance

**Established:** Step 2

**Authoritative collaborator source:** `Rumple12/new-yacoub-thesis`

**Frozen commit:** `278318340bfa4e4650a97a2baba73f63bd868ed9`

**Step 2 status:** Provenance reference frozen; no active schema, middleware, workflow, baseline, safety runtime, or evidence copy adopted.

## Provenance rule

The frozen Yacoub repository supplies collaborator-authored implementation, interfaces, baselines, designs, and evidence. Obid may later adopt, reproduce, configure, or verify only the narrow artifacts authorized by the applicable numbered step. That work does not transfer original authorship.

The active architecture is:

```text
Obid-kandidat/
  Obid-owned implementation
  + documented compatibility with frozen new-yacoub-thesis
```

It is not a copied Yacoub project presented as Obid work.

Use the provenance vocabulary defined in `docs/ongoing/repository-structure.md`. A Yacoub-authored contract is both collaborator-originated and a `SHARED_INTERFACE`; the frozen source remains `REFERENCE_ONLY` until Step 5 adopts an active, provenance-labelled copy or immutable equivalent.

## Frozen-source authority and local reference caveat

The local reference location is:

`reference/new-yacoub-thesis (final project iteration)/`

Its nested Git `HEAD` identifies the frozen commit, but its working tree is not a clean checkout and appears pruned/changed relative to that commit. The reason for that local state cannot be proven from repository contents. Therefore:

- exact provenance checks use the frozen commit object or upstream commit;
- the local working-tree state is not treated as the exact authoritative source;
- nothing under `reference/` is modified to make it clean;
- later adoption must name the frozen commit and source path.

## Sensor-event contract

### Locked semantics

- `sensor_id`
- `timestamp`
- `type`
- `value`
- `unit`
- `type = temperature`
- `unit = C`

### Artifact record

| Attribute | Record |
| --- | --- |
| Origin | Yacoub thesis / collaborator-provided |
| Frozen source path | `shared_interfaces/json-schema/sensor-event.schema.json` |
| Frozen source | `Rumple12/new-yacoub-thesis` at `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Provenance | `SHARED_INTERFACE`; original authorship remains Yacoub |
| Step 2 active-copy status | Not copied or adopted |
| Later adoption | Step 5 may adopt/verify an exact provenance-labelled active interface artifact or immutable reference |
| Modification rule | Obid may not modify the Yacoub source. Active semantics may not change without explicit authorization and a new compatibility decision. |
| Future action | Step 5 schema adoption and no-drift verification |

The frozen schema also requires one object, the five required fields, a numeric `value`, a non-empty `sensor_id`, a `date-time` string, and no additional properties. The inherited middleware performs only partial inline normalization/checking; that behavior is not full schema enforcement.

## Agent-action contract

### Locked semantics

- `action_id`
- `target`
- `reason`
- `requires_approval`
- actions `fan_on`, `fan_off`
- target `fan_1`

### Artifact record

| Attribute | Record |
| --- | --- |
| Origin | Yacoub thesis / collaborator-provided |
| Frozen source path | `shared_interfaces/json-schema/agent-action.schema.json` |
| Frozen source | `Rumple12/new-yacoub-thesis` at `278318340bfa4e4650a97a2baba73f63bd868ed9` |
| Provenance | `SHARED_INTERFACE`; original authorship remains Yacoub |
| Step 2 active-copy status | Not copied or adopted |
| Later adoption | Step 5 may adopt/verify an exact provenance-labelled active interface artifact or immutable reference |
| Modification rule | Obid may not modify the Yacoub source or silently widen fields, actions, targets, or types. |
| Future action | Step 5 schema adoption, risky-case design, and no-drift verification |

The frozen schema requires exactly the four fields, a non-empty `reason`, Boolean `requires_approval`, and no additional properties.

## Middleware interface

### Locked collaborator-provided semantics

| Interface | Meaning |
| --- | --- |
| `GET /status` | Returns middleware status and simulated state |
| `POST /sensor-event` | Receives/normalizes a sensor event and forwards it through configured `N8N_WEBHOOK_URL` |
| `POST /fan/on` | Sets the collaborator-provided simulated fan state to on |
| `POST /fan/off` | Sets the collaborator-provided simulated fan state to off |

Action mapping:

- `fan_on -> POST /fan/on`
- `fan_off -> POST /fan/off`

### Artifact records

| Artifact | Origin and frozen source path | Provenance | Later adoption/copy | Modification rule | Future step |
| --- | --- | --- | --- | --- | --- |
| Middleware entry point | Yacoub: `middleware/api/app.py` | `YACOUB_INHERITED`, current copy `REFERENCE_ONLY` | Do not copy merely to populate Obid. Step 4 may run/reference the actual boundary. | Never modify Yacoub source. | Step 4 |
| Middleware routes | Yacoub: `middleware/api/routes.py` | Implementation `YACOUB_INHERITED`; endpoint semantics `SHARED_INTERFACE` | Do not copy in Step 2. | Endpoint semantics cannot drift silently. | Step 4 |
| Mock sensor/fan state | Yacoub: `middleware/gpio/mock_sensor.py` | `YACOUB_INHERITED`, current copy `REFERENCE_ONLY` | No active copy planned by default. | Never represent an Obid substitute as Yacoub middleware. | Step 4 verification/context |
| n8n sender | Yacoub: `middleware/webhooks/n8n_sender.py` | `YACOUB_INHERITED`, `N8N_WEBHOOK_URL` behavior is shared integration context | Do not copy in Step 2. | Never modify Yacoub source. | Step 4 |

If the actual collaborator middleware is unavailable in Step 4, a narrowly authorized local substitute may be created only as `TEST_DOUBLE`, must faithfully emulate the documented boundary, and must never become a competing middleware architecture.

## Inherited threshold and action behavior

The comparison semantics remain:

```text
value >= 30.0 C -> fan_on
otherwise -> fan_off
```

This behavior is `YACOUB_INHERITED`. Step 6 may reproduce/verify it as a comparison baseline but may not attribute the rule or original workflow to Obid.

## Baseline comparison artifacts

| Artifact | Origin and frozen source path | Provenance | Later adoption/copy | Modification rule | Future step |
| --- | --- | --- | --- | --- | --- |
| Deterministic workflow | Yacoub: `cognitive_logic/workflows/deterministic-baseline.json` | `YACOUB_INHERITED`, current copy `REFERENCE_ONLY` | Step 6 may narrowly import/reproduce it with provenance. | Frozen source is immutable; any compatibility repair applies only to an active reproduction and must be logged. | Step 6 |
| Deterministic description | Yacoub: `cognitive_logic/workflows/deterministic-baseline.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` | Use as source/verification context. | Do not edit/copy as Obid-authored design. | Step 6 |
| Deterministic runtime note | Yacoub: `cognitive_logic/workflows/evidence/step-06-runtime-verification.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` evidence | Do not copy as Obid evidence. | Never alter or treat as an Obid run. | Step 6 context |
| Minimal agent workflow | Yacoub: `cognitive_logic/workflows/agent-minimal.json` | `YACOUB_INHERITED`, current copy `REFERENCE_ONLY` | Step 6 may narrowly import/recreate a reproducible baseline. | Preserve baseline semantics; log required compatibility repair. | Step 6 |
| Minimal agent description | Yacoub: `cognitive_logic/workflows/agent-minimal.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` | Use as verification context. | Do not edit/copy as Obid-authored design. | Step 6 |
| Baseline prompt | Yacoub: `cognitive_logic/prompts/system-prompt-v1.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` until Step 6 | Step 6 may use/reproduce it only as part of the inherited baseline. | Obid's later prompt must be separately identified as `OBID_CREATED`. | Step 6; Obid prompt in Step 7 |
| Baseline memory choice | Yacoub: `cognitive_logic/memory/memory-choice-v1.md` | `YACOUB_INHERITED`; stateless/no-memory baseline | Step 6 records/verifies the choice. | Do not add memory to the comparison baseline. | Step 6 |
| Minimal-agent runtime note | Yacoub: `cognitive_logic/workflows/evidence/step-07/step-07-runtime-verification.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` evidence | Do not copy as Obid evidence. | Never alter or treat as an Obid run. | Step 6 context |

The frozen runtime evidence identifies a Google Gemini Chat Model, while the committed minimal-agent export omits the connected model node and exact model/settings. Step 6 must resolve this reproducibility gap without rewriting Yacoub history.

## Safety handoff

Yacoub supplied design/specification artifacts, not runtime enforcement.

| Artifact | Origin and frozen source path | Provenance | Later adoption/copy | Modification rule | Future step |
| --- | --- | --- | --- | --- | --- |
| Parser/validation design | Yacoub: `safety_layer/parsers/output-validation-v1.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` specification | Use as source context; do not copy as proof of runtime validation. | Frozen source is immutable. | Step 8 implements `OBID_CREATED` runtime validation. |
| Action-policy design | Yacoub: `safety_layer/policies/action-policy-v1.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` specification | Use as source context; no Step 2 adoption. | Frozen source is immutable. | Step 8 implements `OBID_CREATED` deterministic policy. |
| HITL design | Yacoub: `safety_layer/approvals/hitl-v1.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` specification | Use as source context; do not claim an approval runtime exists. | Frozen source is immutable. | Step 9 implements `OBID_CREATED` actual HITL. |

Related frozen examples are `safety_layer/examples/allowed-case.md`, `blocked-case.md`, and `risky-approval-case.md`. They remain expected-behavior references and are not Obid runtime evidence.

| Safety example | Origin and frozen source path | Provenance | Later adoption/copy | Modification rule | Future step |
| --- | --- | --- | --- | --- | --- |
| Allowed case | Yacoub: `safety_layer/examples/allowed-case.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` expected behavior | Use only as source context; new runtime evidence must be generated by Obid. | Frozen source is immutable. | Step 8 |
| Blocked case | Yacoub: `safety_layer/examples/blocked-case.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` expected behavior | Use only as source context; do not copy as proof of blocking. | Frozen source is immutable. | Step 8 |
| Risky approval case | Yacoub: `safety_layer/examples/risky-approval-case.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` expected behavior | Use only as source context; Step 5 defines the valid risky case and Step 9 generates actual HITL evidence. | Frozen source is immutable. | Steps 5 and 9 |

## Existing Yacoub runtime and Raspberry Pi evidence

Yacoub's prior pinned runtime/configuration, screenshots, logs, evaluation material, and Raspberry Pi evidence are `YACOUB_INHERITED` and `REFERENCE_ONLY` for Obid.

Relevant frozen locations include:

- `infrastructure/docker/`
- `cognitive_logic/workflows/evidence/`
- `evaluation/`
- `evaluation/results/pi-validation/`
- `infrastructure/os/raspberry-pi-notes.md`
- `infrastructure/docker/pi-deployment-notes.md`

They must not be copied into active Obid folders merely to populate the repository, must not be reported as new Obid results, and are not modified. Later Obid runtime/evaluation evidence must be newly generated and labelled `OBID_CREATED` while retaining the inherited comparison source.

| Artifact group | Origin and frozen source path | Provenance | Later adoption/copy | Modification rule | Future step |
| --- | --- | --- | --- | --- | --- |
| Pinned runtime/configuration | Yacoub: `infrastructure/docker/` | `YACOUB_INHERITED`, current content `REFERENCE_ONLY` | Step 3 compares configuration/version; do not copy the whole runtime. | Frozen source is immutable. | Step 3 |
| Workflow runtime evidence | Yacoub: `cognitive_logic/workflows/evidence/` | `YACOUB_INHERITED`, `REFERENCE_ONLY` evidence | Use as baseline context only; generate new Obid verification evidence. | Never alter or relabel as Obid runs. | Step 6 |
| Evaluation material/results | Yacoub: `evaluation/` | `YACOUB_INHERITED`, `REFERENCE_ONLY` | Do not copy into active evaluation to create apparent results. | Frozen source/results are immutable. | Steps 5 and 10 use new Obid artifacts. |
| Raspberry Pi results | Yacoub: `evaluation/results/pi-validation/` | `YACOUB_INHERITED`, `REFERENCE_ONLY` evidence | No Obid adoption required; cite only as inherited context if relevant. | Never alter or claim as Obid hardware evidence. | Report context only if later needed. |
| Raspberry Pi notes | Yacoub: `infrastructure/os/raspberry-pi-notes.md` and `infrastructure/docker/pi-deployment-notes.md` | `YACOUB_INHERITED`, `REFERENCE_ONLY` | No active copy planned. | Frozen sources are immutable. | Report context only if later needed. |

## Step 2 freeze statement

Step 2 freezes this handoff and provenance reference only. Active schema adoption/verification belongs to Step 5, baseline reproduction belongs to Step 6, runtime safety belongs to Steps 8-9, and reportable repeated evaluation belongs to Step 10.
