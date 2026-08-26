# Obid thesis report-writing map

## Map purpose and use

This file is a structured source-and-claim plan for the MIUN-based Obid thesis. It is not thesis prose and does not indicate that a chapter has been written. `READY_TO_DRAFT` means only that the frozen repository sources needed for a bounded first draft have been mapped.

The map follows the headings currently present under `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/`. Every entry records its purpose, intended claim or question, evidence sources, planned presentation, provenance, caveats, and status.

Allowed status values are used exactly as follows:

- `SKELETON_ONLY`: heading and writing plan exist, but substantive drafting is outside this bootstrap task.
- `READY_TO_DRAFT`: frozen source mapping is complete enough to draft. This applies to every Chapter 6 entry.
- `DRAFTED_NEEDS_AUDIT`: a substantive first draft exists and remains under the audit/repair/re-audit gate. This applies to every Chapter 4 and 5 entry.
- `NEEDS_REFERENCE`: external academic or authoritative literature must be researched and cited later.
- `NEEDS_FIGURE`: a later figure may be derived from frozen architecture or evidence; no figure exists yet.
- `CHECK_METADATA`: an Obid-specific metadata decision or confirmed value is missing.

## Source-of-truth and evidence controls

### Content source priority

1. The report-bootstrap task prompt.
2. Root `AGENTS.md`.
3. `docs/ongoing/final-implementation-freeze.md`, `docs/ongoing/final-artifact-manifest.json`, `docs/ongoing/final-evidence-inventory.md`, and `docs/ongoing/final-claim-evidence-map.md`.
4. Locked research questions, active scope/provenance documents, and `docs/decisions.md`.
5. Frozen Step 10 raw and processed experimental evidence.
6. Step 1–11 report notes.
7. Earlier implementation/readiness evidence from Steps 3–9.
8. `reference/` and frozen Yacoub material for inherited context and provenance only.
9. The uploaded Yacoub LaTeX thesis and approved PDF for organization and passing-format guidance only.

If a Yacoub report source conflicts with active Obid repository evidence, the Obid repository controls. The official MIUN template controls the document framework; Yacoub's LaTeX organization may inform harmless structural choices but never Obid claims or results.

### Evidence hierarchy for result claims

Use this order exactly:

1. Step 5 pre-observation oracle and protocol: `evaluation/cases/obid-evaluation-cases.json` and `evaluation/evaluation-protocol.md`.
2. Step 10 locked raw observations and pending snapshots under `evaluation/results/step-10/raw/`.
3. The append-only denial-R03 correction, where relevant: `evaluation/results/step-10/corrections/rq2-hitl-denial-r03-interpretation.md`.
4. Step 10 processed CSVs and `processed/traceability.csv`.
5. Step 10 evidence and report note for narrative support.

Steps 3–9 readiness evidence supports environment, design, implementation, and engineering-development claims. It must not replace Step 10 evidence for final RQ1–RQ3 performance claims.

Path convention: any entry using `raw/<file>` resolves to `evaluation/results/step-10/raw/<file>`; `processed/<file>` resolves to `evaluation/results/step-10/processed/<file>`; and `corrections/<file>` resolves to `evaluation/results/step-10/corrections/<file>`. All other paths are repository-relative unless explicitly identified as an external format reference.

### Report-note index

| Step shorthand used in entries | Exact report-note path |
|---:|---|
| Step 1 | `docs/report-notes/step-01-scope-and-collaboration-boundary.md` |
| Step 2 | `docs/report-notes/step-02-repository-codex-and-handoff-foundation.md` |
| Step 3 | `docs/report-notes/step-03-n8n-runtime-and-yacoub-compatibility.md` |
| Step 4 | `docs/report-notes/step-04-yacoub-compatible-integration-boundary.md` |
| Step 5 | `docs/report-notes/step-05-contract-and-evaluation-freeze.md` |
| Step 6 | `docs/report-notes/step-06-yacoub-handoff-baselines.md` |
| Step 7 | `docs/report-notes/step-07-obid-single-agent-cognitive-layer.md` |
| Step 8 | `docs/report-notes/step-08-runtime-validation-and-policy.md` |
| Step 9 | `docs/report-notes/step-09-human-in-the-loop-runtime.md` |
| Step 10 | `docs/report-notes/step-10-repeated-reliability-evaluation.md` |
| Step 11 | `docs/report-notes/step-11-final-implementation-and-evidence-freeze.md` |

### Frozen identities

| Identity | Frozen value | Report use |
|---|---|---|
| Repository HEAD at Step 12 start | `490b95c2e81a194033d6130d53af30c655785e1d` | Report-bootstrap checkpoint |
| `FINAL_IMPLEMENTATION_EVIDENCE_CONTENT_HEAD` | `abd36e3d3e88acb8a516a4a0b36f649e1c1f48eb` | Substantive implementation and evidence the thesis may describe |
| Step 11 metadata checkpoint | `9efcb4310753b74ded574f35d5123e19e999bdcd` | Freeze/inventory documentation; do not conflate with the substantive head |
| Frozen Yacoub commit | `278318340bfa4e4650a97a2baba73f63bd868ed9` | Inherited source and provenance anchor |
| Final artifact manifest | `OBID_FINAL_ARTIFACT_FREEZE_V1` | Machine-readable path/hash integrity index |
| Experiment freeze | `STEP10_EXPERIMENT_FREEZE_V1` | Step 10 configuration and protocol identity |
| Raw-data lock | `STEP10_RAW_DATA_LOCK_V1` | Immutable primary observations |
| Freeze gate | `FINAL_IMPLEMENTATION_EVIDENCE_FREEZE: ACTIVE` | No new implementation semantics or experiments without formal reopening |

### Exact research questions

**RQ1**

> How accurately and consistently does the extended n8n-based agentic decision layer produce the expected IoT action across defined normal, malformed, and state-dependent test cases?

**RQ2**

> How effectively do runtime structured-output validation, action policies, and Human-in-the-Loop approval prevent invalid or risky agent actions from reaching the shared IoT action interface?

**RQ3**

> What reliability and latency differences are observed between the inherited minimal agent baseline and the extended Obid agentic workflow under the same defined IoT test cases?

The wording, order, comparator, and scope must not be changed.

### Frozen configuration summary

| Item | `CONFIG-BASELINE` | `CONFIG-OBID` |
|---|---|---|
| Provenance | `YACOUB_INHERITED` | `OBID_CREATED` |
| Final workflow | `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json` | `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json` |
| Prompt | `cognitive_logic/baselines/yacoub/system-prompt-v1.md` | `cognitive_logic/obid/prompts/system-prompt-v1.md` |
| Agent/model topology | One inherited minimal LLM decision with one Gemini node | One Decision Agent with one Gemini node |
| Model | `models/gemini-2.5-flash` | `models/gemini-2.5-flash` |
| Stored generation options | `{}` | `{}` |
| Fallback model | None | None |
| Tools | Inherited route plumbing; no Obid agent tools | Exactly two read-only tools |
| Memory | Stateless/no memory | One process-local two-interaction window |
| ReAct bound | Not a ReAct agent | `maxIterations: 3` |
| Structured behavior | Minimal parse and route | Structured candidate or internal `no_action` |
| Runtime reliability | No Obid validator, policy, or HITL | Contract-specific validation, deterministic policy, and actual HITL |
| Action boundary | Yacoub-inherited middleware and simulated fan | Yacoub-inherited middleware and simulated fan |

Shared frozen semantics are `value >= 30.0 C -> fan_on`, `value < 30.0 C -> fan_off`, target `fan_1`, and endpoint meanings `GET /status`, `POST /sensor-event`, `POST /fan/on`, and `POST /fan/off`. Runtime is n8n `1.123.37` from `n8nio/n8n:1.123.37`, digest `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885`.

### Frozen numerical anchors for later Chapter 6 drafting

- RQ1 `CONFIG-OBID`: High 5/5, Low 5/5, Threshold 5/5, Malformed 5/5, Memory A 5/5, Memory B 5/5, Memory C 5/5; total 35/35 within the frozen cases.
- RQ2: invalid action 5/5; assigned approval 5/5; assigned denial 4/5; planned decisions 5 approve/5 deny; actual decisions 6 approve/4 deny; one human protocol deviation; final invalid or unapproved crossings 0.
- RQ3 reliability: both configurations 5/5 for High, Low, Threshold, Memory A, and Memory C; Baseline 0/5 versus Obid 5/5 for Malformed and Memory B.
- RQ3 automated-latency medians: High 2130 ms Baseline versus 3792 ms Obid; Low 2105 ms versus 4472 ms; Threshold 2083 ms versus 4487 ms. Raw five observations, minimum, maximum, and supplementary means remain in frozen Step 10 evidence.
- Human waiting is excluded from RQ3 automated latency. No statistical significance claim and no standard deviation as a primary frozen metric are supported.

| RQ3 automated-latency cell | Five raw observations (ms) | Median / min / max (ms) | Supplementary mean (ms) |
|---|---|---|---:|
| High — `CONFIG-BASELINE` | 4631, 2130, 2056, 2184, 2016 | 2130 / 2016 / 4631 | 2603.4 |
| High — `CONFIG-OBID` | 4660, 3524, 4803, 3792, 3672 | 3792 / 3524 / 4803 | 4090.2 |
| Low — `CONFIG-BASELINE` | 2250, 2009, 2065, 2105, 2164 | 2105 / 2009 / 2250 | 2118.6 |
| Low — `CONFIG-OBID` | 4472, 5565, 4358, 4237, 5282 | 4472 / 4237 / 5565 | 4782.8 |
| Threshold — `CONFIG-BASELINE` | 2059, 2252, 2083, 2152, 1998 | 2083 / 1998 / 2252 | 2108.8 |
| Threshold — `CONFIG-OBID` | 4279, 4487, 4365, 4689, 4593 | 4487 / 4279 / 4689 | 4482.6 |

## Global claim, provenance, metadata, and source warnings

### Unsupported claims that must not appear

The following task-specified claims are unsupported:

- universal agent reliability;
- production safety;
- statistically significant improvement;
- physical Obid hardware validation;
- full Raspberry Pi Obid deployment;
- multi-agent implementation;
- validator-agent comparison;
- model superiority;
- memory-strategy superiority;
- generic security enforcement;
- durable long-term memory;
- 5/5 assigned denials;
- a final invalid/unapproved crossing count of 1;
- an exact 5/5 planned-versus-actual HITL balance;
- the deterministic baseline as the primary RQ3 comparator when the actual comparator is the inherited minimal-agent `CONFIG-BASELINE`; and
- hidden chain-of-thought analysis.

Also exclude or qualify: arbitrary-input prevention; a claim that the agent naturally generated `fan_reverse`; autonomous risk discovery; full repeated Gemini-to-HITL risk generation; empirically proven timeout, replay/idempotency, reviewer identity, or cryptographic action integrity; generic JSON Schema-engine behavior; direct monetary comparison; exact reason-text fidelity; causal attribution of latency to one component; scalability; population estimates; or generality beyond the frozen domain, model, runtime, seams, and cases.

Denial R03 must remain incorrect against its assigned denial oracle. Its actual human input was `approve`, so the valid held action was approved before release. The immutable historical crossing flag of 1 does not control the final RQ2 safety interpretation; the append-only correction establishes zero invalid or unapproved crossings.

### Provenance warnings

- Workflow-to-action infrastructure, middleware/action API, threshold/action semantics, deterministic baseline, minimal-agent baseline semantics, and Raspberry Pi/action-side evidence are `YACOUB_INHERITED`.
- Sensor/action contracts and compatible endpoint meanings are `SHARED_INTERFACE` with Yacoub origin. Shared use does not imply co-authorship.
- Chapter 4 middleware/shared-contract design must be labelled `YACOUB_INHERITED` / `SHARED_INTERFACE`; Obid's integration verification is `OBID_CREATED`.
- Chapter 5 Decision Agent, prompt, tools, controlled ReAct behavior, bounded memory, and internal decision envelope are `OBID_CREATED`.
- Chapter 5 runtime validation, deterministic policy, actual HITL, evaluation seams, and evaluation tooling are `OBID_CREATED`.
- Chapter 6 Step 10 orchestration, raw observations, processing, traceability, correction, and reported evidence are `OBID_CREATED`; the comparator behavior remains inherited.
- Raspberry Pi/action-side material may appear only as `YACOUB_INHERITED` / `REFERENCE_ONLY` context, never as new Obid validation.
- Reproduction, verification, compatible configuration, integration, or comparison never transfers authorship.
- The active minimal baseline is a provenance-labelled compatible reproduction with documented repairs, not a byte-identical copy of an incomplete draft.

### Metadata gaps

Do not copy collaborator-specific personal metadata or guess any missing Obid value.

| Missing or unconfirmed item | Required treatment |
|---|---|
| Final thesis title | Retain `% [CHECK METADATA: final thesis title]` |
| Subtitle | Retain `% [CHECK METADATA: final thesis subtitle]` |
| Full Obid author name | Confirm from an active authorized source |
| Supervisor | Retain a check placeholder |
| Examiner | Retain a check placeholder |
| Registration number | Retain a check placeholder |
| Exact main field of study wording | Retain a check placeholder |
| Exact study-programme wording | Retain a check placeholder |
| Course credits | Retain a check placeholder |
| Course code | Retain a check placeholder |
| Publication semester/year | Confirm; do not infer merely from build date |
| DiVA publication choice and personal fields | Confirm before final submission |
| Acknowledgements or foreword choice and approved names | Confirm with author |
| English and Swedish keywords | Choose only after the abstract is stable |
| Required AI-tool disclosure wording/location | Confirm MIUN/course requirement |

### Source and reference caveats

- The official MIUN ZIP is the primary layout/build blueprint. Preserve its class and flat file structure.
- The Yacoub LaTeX ZIP is a working organization/compile reference only. Do not copy its technical claims, results, old scope, or personal metadata.
- The approved Yacoub PDF is a visual/passing-format reference only. It cannot override frozen Obid evidence.
- `reference/` is read-only source/history/collaborator material.
- Yacoub's old two-case, single-run, specification-only-safety, stateless-Obid, Raspberry Pi-as-Obid, and CSV-measurement claims do not describe the final Obid study.
- No web reference search or bibliography import is authorized in this bootstrap. `literature.bib` remains a build placeholder.
- Repository implementation documents are not substitutes for external theory/related-work sources.
- No active final report screenshots or figures exist. Later figures must be derived only from frozen architecture/data and must not expose credentials, owner/project data, transient HITL URLs, the retained local username/path, or hidden reasoning.
- Use repository-relative paths in prose, tables, and figures; do not reproduce absolute temporary checkout paths found in three readiness evidence files.

## Front matter

### FM-01 — Title page and thesis metadata

- **Purpose:** Populate the MIUN title page with verified Obid-specific bibliographic and course data.
- **Main claim/question:** What is the final approved identity of this bachelor thesis and its authoring context?
- **Frozen source artifacts:** `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/thesis.tex`; `docs/ongoing/project-overview.md`.
- **Relevant report note(s):** `docs/report-notes/step-01-scope-and-collaboration-boundary.md`.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** MIUN title-page rendering supplied by `miunthesis.cls`; no custom figure.
- **References needed later:** None.
- **Provenance:** MIUN layout/template; all personal and thesis metadata must be Obid-specific.
- **Limitations/caveats:** Title, subtitle, author, field, credits, supervisor, examiner, course code, registration number, programme, and date-related metadata remain unconfirmed; do not copy Yacoub metadata.
- **Status:** `SKELETON_ONLY`, `CHECK_METADATA`.

### FM-02 — DiVA publication page

- **Purpose:** Preserve the official publication-information sheet required by the MIUN structure.
- **Main claim/question:** Which verified publication and personal-data choices belong in the final DiVA sheet?
- **Frozen source artifacts:** `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/Diva_publish.pdf`; `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/thesis.tex`.
- **Relevant report note(s):** None.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None; this is an official included PDF page.
- **References needed later:** Official MIUN/DiVA submission instructions.
- **Provenance:** Official MIUN template infrastructure.
- **Limitations/caveats:** Publication choice and personal fields are not frozen Obid evidence and require explicit confirmation.
- **Status:** `SKELETON_ONLY`, `CHECK_METADATA`, `NEEDS_REFERENCE`.

### FM-03 — Abstract

- **Purpose:** Later provide a self-contained English summary of aim, method, bounded results, conclusion, and principal limitations.
- **Main claim/question:** What did the frozen Obid study investigate, observe, and conclude within its exact scope?
- **Frozen source artifacts:** `docs/ongoing/research-questions.md`; `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-claim-evidence-map.md`; final Chapter 6 tables once drafted.
- **Relevant report note(s):** `docs/report-notes/step-10-repeated-reliability-evaluation.md`; `docs/report-notes/step-11-final-implementation-and-evidence-freeze.md`.
- **Raw evidence:** Use only through the final Chapter 6 interpretation; primary source is `evaluation/results/step-10/raw/run-records.jsonl`.
- **Processed evidence:** `evaluation/results/step-10/processed/rq1-summary.csv`; `rq2-summary.csv` with correction; `rq3-reliability.csv`; `rq3-latency.csv`.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** None ordinarily in the abstract.
- **Provenance:** Mixed claims must retain `YACOUB_INHERITED`, `SHARED_INTERFACE`, and `OBID_CREATED` boundaries.
- **Limitations/caveats:** Draft last; keep R03 correction, simulated boundary, descriptive n=5/cell, and no universal/safety/significance claims. Final keywords remain unconfirmed.
- **Status:** `SKELETON_ONLY`, `CHECK_METADATA`.

### FM-04 — Sammanfattning

- **Purpose:** Later provide a faithful Swedish counterpart to the final English abstract.
- **Main claim/question:** How can the approved English summary be translated without changing evidence or provenance?
- **Frozen source artifacts:** Same artifacts as FM-03; final approved English abstract.
- **Relevant report note(s):** `docs/report-notes/step-10-repeated-reliability-evaluation.md`; `docs/report-notes/step-11-final-implementation-and-evidence-freeze.md`.
- **Raw evidence:** Same bounded use as FM-03.
- **Processed evidence:** Same bounded use as FM-03.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** None ordinarily.
- **Provenance:** Must exactly preserve the mixed provenance in the English abstract.
- **Limitations/caveats:** Draft after the English abstract; do not alter numerical qualifiers; Swedish keywords remain unconfirmed.
- **Status:** `SKELETON_ONLY`, `CHECK_METADATA`.

### FM-05 — Acknowledgements/Foreword

- **Purpose:** Reserve optional personal front matter.
- **Main claim/question:** Should this page be included, which heading should be used, and whom may the author acknowledge?
- **Frozen source artifacts:** `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/00-acknowledgements.tex`.
- **Relevant report note(s):** None.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Obid authorial statement; not an implementation/evidence claim.
- **Limitations/caveats:** Requires author approval; do not copy collaborator-specific acknowledgements or disclose personal data without approval.
- **Status:** `SKELETON_ONLY`, `CHECK_METADATA`.

### FM-06 — Table of contents

- **Purpose:** Provide the MIUN-generated navigation structure for the final eight-chapter report and appendix.
- **Main claim/question:** Does the final generated hierarchy match the approved report structure?
- **Frozen source artifacts:** `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/thesis.tex`; chapter and appendix `.tex` files.
- **Relevant report note(s):** None.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Automatically generated table of contents.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** MIUN template infrastructure; Obid report organization.
- **Limitations/caveats:** Do not add Chapter 9; regenerate only through normal LaTeX compilation.
- **Status:** `SKELETON_ONLY`.

### FM-07 — Terminology / Notation

- **Purpose:** Define recurring project-specific and literature-derived terms consistently.
- **Main claim/question:** Which terms require short definitions or project-specific qualifications for a reader?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `cognitive_logic/obid/`; `shared_interfaces/json-schema/`; `safety_layer/`.
- **Relevant report note(s):** `docs/report-notes/step-07-obid-single-agent-cognitive-layer.md`; `step-08-runtime-validation-and-policy.md`; `step-09-human-in-the-loop-runtime.md`.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Term; working definition; project-specific qualification. Reserve `CONFIG-BASELINE`, `CONFIG-OBID`, agentic workflow, bounded memory, HITL, JSON Schema, middleware, n8n, ReAct, RQ, shared action interface, and structured output.
- **Expected future figure(s):** None.
- **References needed later:** Authoritative definitions for non-project-specific terms.
- **Provenance:** Project-specific configuration labels are `OBID_CREATED`; contract and middleware terms retain `SHARED_INTERFACE` / `YACOUB_INHERITED`; general terms require external sources.
- **Limitations/caveats:** Alphabetize after Chapters 2, 4, and 5 stabilize; define terms again at first body use; do not polish definitions before reference work.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

## Chapter 1 — Introduction

### Chapter 1 overview

- **Purpose:** Establish the problem, aim, exact RQs, bounded scope, contribution, collaboration boundary, and report route.
- **Main claim/question:** Why is a stronger decision/reliability layer worth studying on top of the inherited workflow-to-action system?
- **Frozen source artifacts:** `docs/ongoing/project-overview.md`; `obid-scope.md`; `research-questions.md`; `collaboration-boundary.md`; `final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 1, 2, 10, and 11 report notes.
- **Raw evidence:** None directly; result previews must defer to Chapter 6.
- **Processed evidence:** None directly.
- **Expected table(s):** Contribution and provenance summary.
- **Expected future figure(s):** None currently required.
- **References needed later:** IoT event-action systems, workflow automation, LLM agents, and runtime control motivation.
- **Provenance:** Mixed; inherited system context must remain distinct from Obid's extension.
- **Limitations/caveats:** No project diary, implementation detail, or full result argument; do not imply broad generality.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 1.1 Background and Motivation

- **Purpose:** Introduce the IoT event-to-action setting and motivation for measurable agent runtime controls.
- **Main claim/question:** Why can an LLM-based decision layer require reliability measurement, validation, policy, and human oversight before action release?
- **Frozen source artifacts:** `docs/ongoing/project-overview.md`; `docs/ongoing/obid-scope.md`.
- **Relevant report note(s):** `docs/report-notes/step-01-scope-and-collaboration-boundary.md`; Step 8 and Step 9 notes for bounded project context.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** IoT event-action systems; workflow automation; LLM agents; runtime assurance.
- **Provenance:** General motivation from literature; project context is mixed `YACOUB_INHERITED` / `OBID_CREATED`.
- **Limitations/caveats:** Do not motivate with unsupported claims that all agents are unsafe or that this system is production-ready.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 1.2 Problem Statement

- **Purpose:** State the bounded technical and empirical problem.
- **Main claim/question:** Can the extended layer select expected actions consistently and prevent invalid or unapproved actions at the shared boundary under defined tests?
- **Frozen source artifacts:** `docs/ongoing/research-questions.md`; `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 1 and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** Problem context supported by Chapter 2 sources.
- **Provenance:** The problem concerns the `OBID_CREATED` extension over `YACOUB_INHERITED` infrastructure and `SHARED_INTERFACE` boundaries.
- **Limitations/caveats:** Frame one controlled scenario, not universal agent reliability or production safety.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 1.3 Aim

- **Purpose:** State the thesis objective in one bounded, evidence-aligned form.
- **Main claim/question:** The aim is to implement and evaluate Obid's stronger single-agent decision/reliability layer while preserving the inherited interface.
- **Frozen source artifacts:** `docs/ongoing/project-overview.md`; `docs/ongoing/obid-scope.md`; `docs/ongoing/final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 1 and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** None beyond background support.
- **Provenance:** Aim centers `OBID_CREATED`; infrastructure and contracts remain inherited/shared.
- **Limitations/caveats:** Do not claim rebuilding middleware, baselines, contracts, or hardware.
- **Status:** `SKELETON_ONLY`.

### 1.4 Research Questions

- **Purpose:** Present RQ1–RQ3 verbatim.
- **Main claim/question:** Use the exact three locked questions reproduced in this map.
- **Frozen source artifacts:** `docs/ongoing/research-questions.md`; `docs/ongoing/final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 1, 10, and 11 report notes.
- **Raw evidence:** None in this section.
- **Processed evidence:** None in this section.
- **Expected table(s):** Optional compact RQ-to-chapter/evidence guide; not required.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** RQs and evaluation framing are `OBID_CREATED`; RQ3 names the `YACOUB_INHERITED` minimal-agent comparator.
- **Limitations/caveats:** Do not paraphrase, reorder, substitute the deterministic anchor, or add a multi-agent question.
- **Status:** `SKELETON_ONLY`.

### 1.5 Scope and Delimitations

- **Purpose:** Make the narrow Tier 1.5 study boundary explicit.
- **Main claim/question:** What was intentionally included and excluded to answer RQ1–RQ3 with the smallest defensible system?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/decisions.md`; `docs/ongoing/final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 1, 9, and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** In-scope versus out-of-scope summary, if useful.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Scope decisions are `OBID_CREATED`; inherited boundaries remain labelled.
- **Limitations/caveats:** One scenario, one primary model, one agent, one memory strategy, simulated fan; no validator agent, hardware/device/model comparison, production deployment, or scalability study.
- **Status:** `SKELETON_ONLY`.

### 1.6 Contributions

- **Purpose:** Identify the defensible Obid contribution without absorbing inherited work.
- **Main claim/question:** Which cognitive, runtime-reliability, HITL, and evaluation artifacts were created by Obid?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/final-claim-evidence-map.md`; `docs/ongoing/final-artifact-manifest.json`.
- **Relevant report note(s):** Steps 7–11 report notes.
- **Raw evidence:** `evaluation/results/step-10/raw/` supports the evaluation contribution, not implementation authorship.
- **Processed evidence:** Step 10 processed outputs support the analysis contribution.
- **Expected table(s):** Contribution; artifact/evidence; provenance; boundary.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Explicit `OBID_CREATED`, `YACOUB_INHERITED`, and `SHARED_INTERFACE` separation.
- **Limitations/caveats:** Reuse, compatible reconstruction, testing, and comparison do not transfer authorship; Pi evidence remains inherited/reference-only.
- **Status:** `SKELETON_ONLY`.

### 1.7 AI Tool Use and Disclosure

- **Purpose:** Reserve a transparent disclosure of material AI/Codex assistance and human verification.
- **Main claim/question:** What assistance was used, what was human-verified, and which audit controls bounded it?
- **Frozen source artifacts:** `docs/ongoing/ai-tool-use.md`; `docs/ongoing/codex-workflow.md`; root `AGENTS.md`.
- **Relevant report note(s):** `docs/report-notes/step-02-repository-codex-and-handoff-foundation.md`.
- **Raw evidence:** None; full chat histories and hidden reasoning are intentionally not repository evidence.
- **Processed evidence:** None.
- **Expected table(s):** Optional compact disclosure table if institutionally appropriate.
- **Expected future figure(s):** None.
- **References needed later:** Official MIUN/course AI-use policy.
- **Provenance:** Obid methodology/disclosure material.
- **Limitations/caveats:** Do not claim hidden chain-of-thought retention; exact required wording and placement are unconfirmed.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`, `CHECK_METADATA`.

### 1.8 Division of Work and Collaboration Boundary

- **Purpose:** Describe one integrated system with two separately attributable thesis contributions.
- **Main claim/question:** Where does inherited Yacoub responsibility end and Obid's new contribution begin?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/yacoub-handoff.md`; `docs/decisions.md`; `docs/collaboration/shared-interface-provenance.md`.
- **Relevant report note(s):** Steps 1, 2, 4, 6, and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Division-of-work matrix by component and evidence.
- **Expected future figure(s):** Optional provenance-band boundary figure later, shared with Chapter 4 if not duplicated.
- **References needed later:** Citation details for Yacoub's thesis/repository.
- **Provenance:** This section exists to enforce `YACOUB_INHERITED`, `SHARED_INTERFACE`, `OBID_CREATED`, and `REFERENCE_ONLY`.
- **Limitations/caveats:** Shared use is not co-authorship; do not copy Yacoub technical claims or personal metadata.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 1.9 Report Outline

- **Purpose:** Give a concise roadmap of the eight chapters and appendix.
- **Main claim/question:** How does the report progress from background and method to design, implementation, results, discussion, and conclusions?
- **Frozen source artifacts:** Current chapter files under `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/`; `docs/ongoing/report-outline.md`.
- **Relevant report note(s):** None.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Obid report organization using the MIUN/Yacoub eight-chapter convention.
- **Limitations/caveats:** Draft last; do not narrate numbered repository steps or introduce a ninth chapter.
- **Status:** `SKELETON_ONLY`.

## Chapter 2 — Theory and Related Work

### Chapter 2 overview

- **Purpose:** Build the external conceptual basis needed to understand the selected workflow, agent, memory, validation, policy, HITL, and evaluation design.
- **Main claim/question:** Which established concepts and prior work explain the system without turning repository implementation notes into theory?
- **Frozen source artifacts:** Current Chapter 2 skeleton; project terminology in `docs/ongoing/final-implementation-freeze.md` is routing context only.
- **Relevant report note(s):** Steps 7–10 report notes identify concepts that need literature, but are not literature themselves.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Optional related-work comparison table after references are selected.
- **Expected future figure(s):** Optional conceptual overview only if it materially improves explanation; no project architecture result figure here.
- **References needed later:** All Chapter 2 topics listed below.
- **Provenance:** External literature for general theory; Obid/Yacoub sources only for project positioning and terminology.
- **Limitations/caveats:** Do not copy Yacoub's bibliography, invent BibTeX, or cite repository notes as substitutes for academic/authoritative sources.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.1 Workflow Automation and Orchestration

- **Purpose:** Explain workflow automation, orchestration, nodes, triggers, routing, and execution flow.
- **Main claim/question:** How do workflow systems coordinate data and actions across components?
- **Frozen source artifacts:** `infrastructure/docker/runtime-manifest.md`; `integration/yacoub_compat/boundary-map.md` for later project linkage only.
- **Relevant report note(s):** Steps 3 and 4 report notes for applied context.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Optional terminology comparison of workflow, orchestration, and automation.
- **Expected future figure(s):** None currently planned.
- **References needed later:** Workflow automation and orchestration literature.
- **Provenance:** General claims from external sources; applied n8n configuration is `OBID_CREATED` on an inherited-compatible context.
- **Limitations/caveats:** Keep general concepts separate from claims that a specific frozen workflow executed.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.2 n8n and Low-Code Workflow Automation

- **Purpose:** Introduce n8n as the selected low-code orchestration environment.
- **Main claim/question:** Which n8n concepts are necessary to understand the workflow implementation and native Wait/form behavior?
- **Frozen source artifacts:** `infrastructure/docker/docker-compose.yml`; `infrastructure/docker/runtime-manifest.md`.
- **Relevant report note(s):** Steps 3, 7, and 9 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Optional project-relevant n8n node/category glossary.
- **Expected future figure(s):** None.
- **References needed later:** Official n8n documentation; low-code workflow automation research.
- **Provenance:** General platform description from authoritative external sources; frozen runtime setup is `OBID_CREATED`.
- **Limitations/caveats:** Cite the version actually used, n8n `1.123.37`; avoid advertising language or claims about platform-wide reliability.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.3 IoT Event-Action Systems

- **Purpose:** Explain event-to-decision-to-action patterns and observable device-state boundaries.
- **Main claim/question:** How can sensor events drive controlled actuator actions through software boundaries?
- **Frozen source artifacts:** `docs/ongoing/project-overview.md`; `integration/yacoub_compat/boundary-map.md`; shared schemas.
- **Relevant report note(s):** Steps 1 and 4 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Optional mapping of event, decision, action, and observable state roles.
- **Expected future figure(s):** Optional generic event-action flow distinct from the Chapter 4 project architecture.
- **References needed later:** IoT event-action and actuator-control literature.
- **Provenance:** General theory external; project middleware/action path `YACOUB_INHERITED`; compatibility boundary `SHARED_INTERFACE`.
- **Limitations/caveats:** The Obid experiment stops at a simulated fan; do not generalize to physical deployment.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.4 Middleware and API Boundaries

- **Purpose:** Explain middleware separation, API contracts, ingress/egress, and compatibility seams.
- **Main claim/question:** Why does a stable middleware/API boundary allow the decision layer to be extended without rebuilding action infrastructure?
- **Frozen source artifacts:** `docs/ongoing/yacoub-handoff.md`; `docs/ongoing/collaboration-boundary.md`; `integration/yacoub_compat/boundary-map.md`.
- **Relevant report note(s):** Step 4 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Optional API-boundary concept and project example mapping.
- **Expected future figure(s):** None here; final boundary figure belongs in Chapter 4.
- **References needed later:** Middleware, REST/API boundaries, and interface compatibility.
- **Provenance:** General theory external; project middleware and routes `YACOUB_INHERITED`; endpoint meanings `SHARED_INTERFACE`.
- **Limitations/caveats:** Do not imply Obid authored the Python middleware or that endpoint reachability proves agent correctness.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.5 Structured Data and JSON Contracts

- **Purpose:** Explain structured data, JSON, schema constraints, and interface contracts.
- **Main claim/question:** How can an explicit JSON contract delimit valid sensor events and actions?
- **Frozen source artifacts:** `shared_interfaces/json-schema/sensor-event.schema.json`; `shared_interfaces/json-schema/agent-action.schema.json`; `shared_interfaces/contract-freeze.md`.
- **Relevant report note(s):** Step 5 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Contract concepts and frozen project examples.
- **Expected future figure(s):** None.
- **References needed later:** JSON specification; JSON Schema draft 2020-12; interface-contract literature.
- **Provenance:** General standards external; schemas are Yacoub-originated `SHARED_INTERFACE`; Obid no-drift verification is `OBID_CREATED`.
- **Limitations/caveats:** The runtime action validator implements the frozen contract constraints, not a generic complete JSON Schema engine.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.6 LLM Agents and Agentic Workflows

- **Purpose:** Define agentic workflows, model/tool/environment interaction, and bounded autonomy.
- **Main claim/question:** What distinguishes a tool-capable agentic decision workflow from one minimal LLM decision?
- **Frozen source artifacts:** `cognitive_logic/obid/configuration-manifest.md`; baseline manifest for later applied comparison.
- **Relevant report note(s):** Steps 6 and 7 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** General agentic-workflow features versus the frozen project realization.
- **Expected future figure(s):** None; project topology belongs in Chapter 4.
- **References needed later:** LLM agents and tool-using agentic workflow research.
- **Provenance:** General theory external; `CONFIG-OBID` realization `OBID_CREATED`; minimal baseline `YACOUB_INHERITED`.
- **Limitations/caveats:** Do not describe `CONFIG-OBID` as multi-agent, unbounded, or merely a prompt around an LLM.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.7 ReAct and Tool Use

- **Purpose:** Explain the ReAct concept and observable tool-use cycles relevant to the bounded implementation.
- **Main claim/question:** How can an agent alternate between selecting permitted tools, receiving observations, and producing a final decision?
- **Frozen source artifacts:** `cognitive_logic/obid/react/react-control-v1.md`; `cognitive_logic/obid/tools/tool-definitions-v1.md` for later project linkage.
- **Relevant report note(s):** Step 7 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** ReAct concept; frozen observable implementation; explicit boundary.
- **Expected future figure(s):** Optional abstract tool-observation loop, not chain-of-thought.
- **References needed later:** Original ReAct paper and relevant tool-use literature.
- **Provenance:** Theory external; controlled observable implementation `OBID_CREATED`.
- **Limitations/caveats:** Discuss only observable calls, inputs, outputs, order, and termination; hidden chain-of-thought was not requested or retained.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.8 Memory in LLM-Agent Workflows

- **Purpose:** Explain conversational/window memory and state-dependent decisions.
- **Main claim/question:** How can bounded recent context affect subsequent tool selection or action suppression?
- **Frozen source artifacts:** `cognitive_logic/obid/memory/window-buffer-v1.md`; evaluation memory-case definitions for later applied linkage.
- **Relevant report note(s):** Step 7 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Memory types or properties relevant to the chosen window design.
- **Expected future figure(s):** Optional active-window illustration.
- **References needed later:** LLM-agent memory, bounded/window memory, and state management.
- **Provenance:** Theory external; one frozen memory implementation `OBID_CREATED`.
- **Limitations/caveats:** Process-local, two completed interactions, no restart durability, no physical deletion proof, and no memory-strategy superiority claim.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.9 Structured Output and Runtime Validation

- **Purpose:** Explain structured output and why runtime checks are distinct from prompt instructions.
- **Main claim/question:** How can a runtime boundary determine whether candidate output conforms before release?
- **Frozen source artifacts:** `cognitive_logic/obid/structured-output/decision-envelope-v1.md`; `safety_layer/validator/runtime-action-validator-v1.md`; shared action schema.
- **Relevant report note(s):** Steps 7 and 8 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Prompted structure versus runtime-enforced structure.
- **Expected future figure(s):** None.
- **References needed later:** Structured LLM output, runtime validation, and schema enforcement.
- **Provenance:** General concepts external; internal envelope and runtime validator `OBID_CREATED`; action contract `SHARED_INTERFACE`.
- **Limitations/caveats:** Do not equate structured prompting with enforcement or claim generic security validation.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.10 Deterministic Safety Policies

- **Purpose:** Explain deterministic gates that classify already-validated candidates.
- **Main claim/question:** How can `ALLOW`, `BLOCK`, and `APPROVAL_REQUIRED` constrain release independently of an LLM?
- **Frozen source artifacts:** `safety_layer/policies/runtime-action-policy-v1.md`; `safety_layer/outcomes/safety-outcome-v1.md`.
- **Relevant report note(s):** Step 8 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Policy outcome and release semantics.
- **Expected future figure(s):** Optional policy decision tree, later derived from the frozen policy.
- **References needed later:** Deterministic policy gates, guardrails, and policy enforcement.
- **Provenance:** General theory external; specific policy `OBID_CREATED`.
- **Limitations/caveats:** The policy is narrow and contract-specific; avoid production-safety or arbitrary-risk claims.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.11 Human-in-the-Loop

- **Purpose:** Explain human approval as a runtime control point.
- **Main claim/question:** How can a valid held action remain unreleased until a human approves or denies it?
- **Frozen source artifacts:** `safety_layer/hitl/runtime-hitl-v1.md`; `safety_layer/hitl/hitl-outcome-v1.md` for applied linkage.
- **Relevant report note(s):** Step 9 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Pending, approval, and denial concepts.
- **Expected future figure(s):** Optional generic HITL state transition.
- **References needed later:** HITL, human oversight, and approval-gate literature.
- **Provenance:** General concepts external; final executable gate `OBID_CREATED`; original concept may be cited as inherited Yacoub specification with care.
- **Limitations/caveats:** Do not imply autonomous risk discovery, reviewer identity evidence, replay guarantees, or population-level human response times.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.12 Reliability Evaluation of LLM and Agent Systems

- **Purpose:** Ground repeated correctness, consistency, negative-outcome retention, and latency description.
- **Main claim/question:** How can a bounded repeated evaluation report observed reliability and latency without inferential overreach?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/process_results.py` for later method linkage.
- **Relevant report note(s):** Step 10 report note.
- **Raw evidence:** None in theory.
- **Processed evidence:** None in theory.
- **Expected table(s):** Evaluation concepts and their later operationalization.
- **Expected future figure(s):** None.
- **References needed later:** Reliability/consistency evaluation of LLM agents; descriptive latency measurement; failure reporting.
- **Provenance:** General method concepts external; frozen evaluation design and execution `OBID_CREATED`.
- **Limitations/caveats:** Literature choice must fit five repetitions per cell and descriptive analysis; do not imply significance or population estimates.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 2.13 Related Work and Positioning

- **Purpose:** Compare the bounded contribution with relevant agentic IoT/workflow-control studies.
- **Main claim/question:** What gap does runtime-validated, policy-controlled, HITL-capable single-agent evaluation address within the selected literature?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/ongoing/final-claim-evidence-map.md`; frozen Yacoub thesis only for collaborator context.
- **Relevant report note(s):** Steps 1 and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Related work; system/domain; agents/tools/memory; runtime controls; evaluation; relation to Obid.
- **Expected future figure(s):** None currently planned.
- **References needed later:** Agentic IoT, low-code agent workflows, structured-output validation, HITL control, and reliability studies.
- **Provenance:** External works cited normally; Yacoub explicitly collaborator/reference; Obid positioning `OBID_CREATED`.
- **Limitations/caveats:** Do not copy Yacoub bibliography or claim novelty/superiority without a literature-supported comparison.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

## Chapter 3 — Methodology

### Chapter 3 overview

- **Purpose:** Explain the research/design process and the frozen repeated-evaluation method without narrating repository steps as a diary.
- **Main claim/question:** How were configurations, cases, repetition, ordering, measurements, raw retention, processing, correction, and validity controls defined and applied?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/cases/obid-evaluation-cases.json`; Step 10 experiment/raw/processed manifests; final freeze package.
- **Relevant report note(s):** Steps 1–11, with Steps 5, 10, and 11 primary for the final method.
- **Raw evidence:** Step 10 raw artifacts document execution integrity and retained outcomes.
- **Processed evidence:** Step 10 processed manifest, traceability, and scripts document derivation.
- **Expected table(s):** Configuration, case, order, measurement, provenance, and limitation tables mapped below.
- **Expected future figure(s):** Optional evaluation-flow diagram derived from frozen protocol.
- **References needed later:** Research/design methodology, validity, and descriptive repeated evaluation.
- **Provenance:** Method design/execution `OBID_CREATED`; inherited comparator and interface explicitly labelled.
- **Limitations/caveats:** Planning and readiness are not result evidence; no new runs or retrospective protocol edits.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.1 Research and Design Approach

- **Purpose:** Describe the bounded design/build/verify/evaluate approach and audit discipline.
- **Main claim/question:** Which method connected artifact construction, human verification, audit gates, freeze, and evidence-backed reporting?
- **Frozen source artifacts:** `docs/plans/implementation-plan.md`; `docs/ongoing/codex-workflow.md`; root `AGENTS.md`; `docs/decisions.md`.
- **Relevant report note(s):** Steps 1–11 report notes.
- **Raw evidence:** None directly.
- **Processed evidence:** None directly.
- **Expected table(s):** Phase; purpose; produced evidence; completion gate.
- **Expected future figure(s):** Optional method flow from design freeze to raw lock and reporting.
- **References needed later:** Appropriate design science, constructive, or engineering research method source; AI-assistance disclosure guidance.
- **Provenance:** Obid methodology.
- **Limitations/caveats:** Reorganize academically; do not write “Step 1, then Step 2”; audits are completion review, not experiment data.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.2 Collaboration and Provenance Boundary

- **Purpose:** Operationalize authorship labels and inherited/shared/created artifact handling in the method.
- **Main claim/question:** How was one integrated system evaluated while keeping two thesis contributions separately attributable?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; `docs/collaboration/shared-interface-provenance.md`; `docs/ongoing/yacoub-handoff.md`; `docs/decisions.md`.
- **Relevant report note(s):** Steps 1, 2, 4, 6, and 11 report notes.
- **Raw evidence:** Step 10 records identify configuration IDs; no inherited raw results are recast as Obid-created.
- **Processed evidence:** `evaluation/results/step-10/processed/traceability.csv`.
- **Expected table(s):** Artifact class; Yacoub/Shared/Obid provenance; methodological use.
- **Expected future figure(s):** Optional provenance band shared with Chapter 4.
- **References needed later:** Citation for Yacoub's thesis/repository; authorship/collaboration rules only if institutionally required.
- **Provenance:** Explicit persistent vocabulary.
- **Limitations/caveats:** Verification and compatible reproduction do not transfer authorship; Pi evidence remains inherited/reference-only.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.3 Controlled Temperature-to-Fan Scenario

- **Purpose:** Define the bounded domain, sensor/action semantics, state, and observable endpoint.
- **Main claim/question:** What controlled scenario makes correctness, state dependence, validation, and HITL observable?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `shared_interfaces/contract-freeze.md`; both shared schemas; `evaluation/evaluation-protocol.md`.
- **Relevant report note(s):** Steps 4 and 5 report notes.
- **Raw evidence:** `evaluation/results/step-10/raw/run-records.jsonl` records stimuli, actions, endpoints, and fan state.
- **Processed evidence:** None needed to define the scenario.
- **Expected table(s):** Sensor fields; threshold; allowed actions; target; endpoint; state semantics.
- **Expected future figure(s):** Optional scenario boundary diagram.
- **References needed later:** IoT scenario design and controlled-test context.
- **Provenance:** Semantics and simulated boundary `YACOUB_INHERITED` / `SHARED_INTERFACE`; test scenario formalization `OBID_CREATED`.
- **Limitations/caveats:** One sensor type, one target, simulated fan; no physical Obid hardware experiment.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.4 Baseline and Extended Configuration Definitions

- **Purpose:** Fix the two configurations compared under RQ3.
- **Main claim/question:** What exactly constitutes `CONFIG-BASELINE` and `CONFIG-OBID`, and which controls are common?
- **Frozen source artifacts:** `cognitive_logic/baselines/yacoub/baseline-manifest.md`; `cognitive_logic/obid/configuration-manifest.md`; `docs/ongoing/final-artifact-manifest.json`; final workflows and prompts.
- **Relevant report note(s):** Steps 6, 7, 9, 10, and 11 report notes.
- **Raw evidence:** Step 10 run records contain configuration identities.
- **Processed evidence:** `processed/rq3-reliability.csv`; `processed/rq3-latency.csv`.
- **Expected table(s):** `CONFIG-BASELINE` versus `CONFIG-OBID`: model, workflow, prompt, tools, memory, iterations, safety, HITL, provenance.
- **Expected future figure(s):** None; architecture comparison can be placed in Chapter 4.
- **References needed later:** None beyond Chapter 2 concepts.
- **Provenance:** Baseline semantics `YACOUB_INHERITED`; Obid configuration `OBID_CREATED`.
- **Limitations/caveats:** The deterministic baseline is contextual only, not the RQ3 comparator; model provider backend/defaults are not immutable.
- **Status:** `SKELETON_ONLY`.

### 3.5 Frozen Evaluation Protocol

- **Purpose:** Establish that cases, expectations, timing, order, and retention rules preceded observation.
- **Main claim/question:** How was result-driven oracle or protocol change prevented?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/cases/obid-evaluation-cases.json`; `evaluation/results/step-10/experiment-freeze.json`; `experiment-freeze.md`.
- **Relevant report note(s):** Steps 5, 10, and 11 report notes.
- **Raw evidence:** `raw/planned-order.json`; raw manifest.
- **Processed evidence:** None.
- **Expected table(s):** Frozen artifact; identity/hash; pre-observation role.
- **Expected future figure(s):** Freeze→execute→lock→process flow.
- **References needed later:** Preregistration/frozen-protocol or reproducible evaluation principles, if used.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** No later evidence may be described as if it established the pre-observation oracle; operational restorations were non-semantic.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.6 Repeated-Run Design and Order Control

- **Purpose:** Explain repetition count, five-round block rotation, configuration pairing, memory-sequence integrity, and HITL order.
- **Main claim/question:** How were five repetitions per cell executed without result-driven ordering or replacement?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/raw/planned-order.json`.
- **Relevant report note(s):** Steps 5 and 10 report notes.
- **Raw evidence:** `raw/run-order.csv`; `raw/attempt-events.jsonl`; `raw/run-records.jsonl`.
- **Processed evidence:** `processed/traceability.csv`.
- **Expected table(s):** Five-round H/L/T/M/S rotation; deterministic pair order; alternating HITL A/B order.
- **Expected future figure(s):** Optional order/control timeline.
- **References needed later:** Repeated-measures/order-control literature if needed.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** n=5/cell supports descriptive consistency only; every attempt remains in the denominator; memory A→B→C is indivisible.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.7 Case Matrix

- **Purpose:** Map each frozen case to RQ, injection seam, configuration, expected terminal, and observable oracle.
- **Main claim/question:** Which normal, malformed, invalid-action, HITL, and state-dependent cases operationalize RQ1–RQ3?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`.
- **Relevant report note(s):** Step 5 report note.
- **Raw evidence:** Later actual outcomes in `raw/run-records.jsonl`.
- **Processed evidence:** Later summaries by case family.
- **Expected table(s):** Case ID; input; injection point; configuration; RQ; expected terminal/action/state; repetition.
- **Expected future figure(s):** None.
- **References needed later:** Test-case design literature if required.
- **Provenance:** Case/oracle design `OBID_CREATED`; threshold and action semantics inherited/shared.
- **Limitations/caveats:** Malformed case bypasses inherited normalization at a direct comparable seam; invalid action is injected post-agent; HITL enters controlled policy input.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.8 Correctness and Consistency Measurement

- **Purpose:** Define expected-outcome correctness and modal observable-outcome agreement for RQ1.
- **Main claim/question:** How are accuracy and run-to-run consistency computed without exact-scoring reason wording?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/process_results.py`.
- **Relevant report note(s):** Steps 5 and 10 report notes.
- **Raw evidence:** `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq1-summary.csv`; `processed/traceability.csv`.
- **Expected table(s):** Metric; numerator/denominator; grouping; treatment of failure/missing outcomes.
- **Expected future figure(s):** None in methodology.
- **References needed later:** Accuracy/consistency reporting for repeated LLM-agent evaluations.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Exact reason text is not a metric; correctness is limited to the frozen observable oracle and five attempts per family.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.9 Safety and HITL Measurement

- **Purpose:** Define RQ2 observations for validator/policy outcomes, waiting, human decision, release, endpoints, and deviations.
- **Main claim/question:** How is assigned-oracle correctness distinguished from whether an invalid or unapproved action actually crossed?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/cases/obid-evaluation-cases.json`; R03 correction.
- **Relevant report note(s):** Steps 8, 9, 10, and 11 report notes.
- **Raw evidence:** `raw/hitl-pending.jsonl`; `raw/run-records.jsonl`; `raw/attempt-events.jsonl`.
- **Processed evidence:** `processed/rq2-summary.csv`; `processed/hitl-timing.csv`; `processed/traceability.csv`, interpreted through the correction.
- **Expected table(s):** RQ2 measure; evidence field; success/failure rule; correction treatment.
- **Expected future figure(s):** Optional HITL state/measurement diagram.
- **References needed later:** HITL and runtime assurance evaluation.
- **Provenance:** Runtime controls/evaluation `OBID_CREATED`; action interface `SHARED_INTERFACE`; endpoint semantics inherited.
- **Limitations/caveats:** Retain assigned denial 4/5, actual 6/4, deviation 1, crossings 0; do not let historical crossing=1 control the final interpretation.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.10 Automated Latency Measurement

- **Purpose:** Define the comparable automated timing window and descriptive summaries for RQ3.
- **Main claim/question:** How is full automated ingress-to-terminal latency compared for High, Low, and Threshold across the two configurations?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/experiment-freeze.json`.
- **Relevant report note(s):** Steps 5 and 10 report notes.
- **Raw evidence:** Thirty eligible observations in `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq3-latency.csv`; `processed/traceability.csv`.
- **Expected table(s):** Eligible cases; start/end boundaries; exclusions; five raw values; median/min/max; supplementary mean.
- **Expected future figure(s):** None in method; result distribution/observation figure later.
- **References needed later:** Latency measurement and descriptive statistics.
- **Provenance:** Measurements `OBID_CREATED`; comparator inherited.
- **Limitations/caveats:** Human waiting excluded; n=5/cell; mean supplementary; no primary standard deviation, significance, outlier removal, or component causality.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.11 Raw-Data Retention and Failure Handling

- **Purpose:** Explain immutable raw retention, denominators, missing/failed outcomes, and no replacement.
- **Main claim/question:** How were failures and deviations preserved before processing?
- **Frozen source artifacts:** `evaluation/results/step-10/raw/raw-data-manifest.json`; `raw-data-manifest.md`; `docs/decisions.md` D-012.
- **Relevant report note(s):** Steps 2, 5, 10, and 11 report notes.
- **Raw evidence:** All files under `evaluation/results/step-10/raw/`, especially `run-records.jsonl` and `attempt-events.jsonl`.
- **Processed evidence:** `processed/traceability.csv` confirms linkage but does not replace raw authority.
- **Expected table(s):** Raw artifact; purpose; record count; hash; failure-retention role.
- **Expected future figure(s):** None.
- **References needed later:** Reproducible data-retention practice if required.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Raw evidence is immutable; do not hide two non-success baseline malformed runs, R03, missing telemetry, or operational deviations.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.12 Processing, Traceability, and Reproducibility

- **Purpose:** Explain orchestration, extraction, deterministic processing, hashing, and raw-to-summary linkage.
- **Main claim/question:** Can each reported result be traced to a frozen raw run and execution identity?
- **Frozen source artifacts:** `evaluation/results/step-10/run_step10.py`; `extract_n8n_execution.js`; `process_results.py`; final artifact manifest.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Raw manifest and all raw files.
- **Processed evidence:** `processed/processed-data-manifest.json`; `processed/traceability.csv`; all processed CSVs.
- **Expected table(s):** Tool; input; output; integrity role; traceability role.
- **Expected future figure(s):** Raw→processor→summary→claim traceability flow.
- **References needed later:** Reproducible computational evaluation and data provenance.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Historical processed RQ2 output remains immutable; append-only correction changes interpretation, not bytes; credentials/provider backend are not frozen artifacts.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 3.13 Threats and Limitations of the Method

- **Purpose:** Consolidate internal, construct, external, and reproducibility threats before interpreting results.
- **Main claim/question:** Which design and measurement boundaries restrict the conclusions?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-evidence-inventory.md`; `docs/ongoing/final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 6–11 report notes.
- **Raw evidence:** Raw failures, deviations, pending snapshots, and missing telemetry where relevant.
- **Processed evidence:** RQ summaries, latency, HITL timing, telemetry, and correction.
- **Expected table(s):** Threat category; evidence/basis; likely effect; mitigation; residual limitation.
- **Expected future figure(s):** None.
- **References needed later:** Research-validity framework.
- **Provenance:** Threat analysis `OBID_CREATED`; inherited limitations labelled by source.
- **Limitations/caveats:** Cover one model/domain, n=5/cell, simulated boundary, controlled seams, provider defaults, process-local memory, session-specific HITL time, unequal workload, no cost, missing token telemetry, and no model/memory/device/multi-agent comparison.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

## Chapter 4 — Choice of Approach / System Design

### Chapter 4 overview

- **Purpose:** Present the rationale and final frozen system design as an academic design argument.
- **Main claim/question:** Why was a bounded single-agent cognitive/reliability extension selected while preserving the inherited workflow-to-action boundary?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/decisions.md`; `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-artifact-manifest.json`; final workflow and component records.
- **Relevant report note(s):** Steps 1, 4–9, and 11 report notes.
- **Raw evidence:** None required for the design rationale; Step 10 raw evidence may confirm evaluation-oriented observability but not motivate post hoc design changes.
- **Processed evidence:** None required.
- **Expected table(s):** Design goals/constraints; alternatives; architecture components; provenance; safety/HITL outcomes.
- **Expected future figure(s):** Final frozen Obid architecture with provenance bands.
- **References needed later:** Agentic workflows, ReAct/tool use, bounded memory, structured output, runtime validation, deterministic policy, and HITL.
- **Provenance:** Mixed and explicit: infrastructure/baselines `YACOUB_INHERITED`; contracts `SHARED_INTERFACE`; decision/reliability design `OBID_CREATED`.
- **Limitations/caveats:** Bounded research design, not production architecture; no multi-agent, validator agent, new hardware, model comparison, or memory comparison.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.1 Design Goals and Constraints

- **Purpose:** Derive the smallest design capable of answering RQ1–RQ3.
- **Main claim/question:** Which goals and constraints connect expected-action consistency, runtime release control, fair baseline comparison, and evidence traceability?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/ongoing/project-overview.md`; `docs/decisions.md` D-001, D-005–D-011, D-015; `docs/ongoing/final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 1, 5, 9, and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Design goal/constraint; design response; evidence source; RQ link.
- **Expected future figure(s):** None.
- **References needed later:** Requirements/design rationale literature only if needed.
- **Provenance:** Design decisions `OBID_CREATED`; compatibility constraints inherit Yacoub semantics and shared contracts.
- **Limitations/caveats:** One scenario/model/agent/memory configuration, simulated boundary, and descriptive repeated evaluation; do not present as production requirements coverage.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`.

### 4.2 Inherited Collaboration Boundary

- **Purpose:** Establish what the design reuses and where Obid begins.
- **Main claim/question:** How does the Obid layer connect to Yacoub-owned middleware, baseline semantics, and shared contracts without redesigning them?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/yacoub-handoff.md`; `docs/collaboration/shared-interface-provenance.md`; `integration/yacoub_compat/boundary-map.md`; `shared_interfaces/contract-freeze.md`.
- **Relevant report note(s):** Steps 1, 2, 4, 5, 6, and 11 report notes.
- **Raw evidence:** Step 4 integration observations are readiness/context evidence only.
- **Processed evidence:** None.
- **Expected table(s):** Inherited component; shared seam; Obid use/verification; provenance.
- **Expected future figure(s):** Provenance-banded collaboration boundary, possibly combined with Section 4.11.
- **References needed later:** Yacoub thesis/repository citation; general interface-boundary sources in Chapter 2.
- **Provenance:** Middleware, API, threshold, baselines, Pi evidence `YACOUB_INHERITED`; schemas/endpoints `SHARED_INTERFACE`; Obid boundary verification `OBID_CREATED`.
- **Limitations/caveats:** Do not claim middleware, baselines, schemas, or Pi/action-side evidence as Obid-authored; shared does not mean co-authored.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.3 Alternatives and Scope Decisions

- **Purpose:** Explain evaluated design alternatives and why they were excluded or selected.
- **Main claim/question:** Why choose an extended single-agent layer instead of deterministic-only, multi-agent, multi-model, multi-device, hardware-expansion, or validator-agent designs?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/decisions.md` D-006–D-010 and D-015; `docs/ongoing/final-implementation-freeze.md` deferred-work section.
- **Relevant report note(s):** Steps 1, 6, 7, 9, and 11 report notes.
- **Raw evidence:** None; exclusions were design/scope decisions rather than unrun comparative results.
- **Processed evidence:** None.
- **Expected table(s):** Alternative; decision; rationale; frozen status; evidentiary consequence.
- **Expected future figure(s):** None.
- **References needed later:** Single-agent versus multi-agent design literature only if making a general tradeoff argument.
- **Provenance:** Scope and selected design `OBID_CREATED`; deterministic and minimal baselines inherited.
- **Limitations/caveats:** Do not imply alternatives were experimentally compared. Explicitly record: one primary model, one bounded-memory strategy, no new hardware/device comparison, no validator agent, and preserved middleware/contracts.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`.

### 4.4 Chosen Agentic Architecture

- **Purpose:** Define the complete selected component topology.
- **Main claim/question:** How does a single Decision Agent progress from event and read-only observations to a validated/policy-controlled action or internal no-op?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-artifact-manifest.json`; `cognitive_logic/obid/configuration-manifest.md`; `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`.
- **Relevant report note(s):** Steps 7–9 and 11 report notes.
- **Raw evidence:** None primary; readiness executions in Steps 7–9 support runtime existence.
- **Processed evidence:** None.
- **Expected table(s):** Component; role; input/output; implementation artifact; provenance.
- **Expected future figure(s):** Final frozen Obid architecture.
- **References needed later:** Agentic workflow architecture and tool-using agents.
- **Provenance:** Decision Agent, prompt, tools, memory, validation, policy, and HITL `OBID_CREATED`; final endpoint boundary inherited/shared.
- **Limitations/caveats:** Exactly one agent, one Gemini node, two read-only tools, one memory configuration, `maxIterations: 3`; not multi-agent and not merely prompt-only safety.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.5 Tool-Use and Controlled ReAct Design

- **Purpose:** Explain why and how the agent receives exactly two bounded read-only tools.
- **Main claim/question:** How do deterministic threshold computation and current-state observation support an observable, bounded tool-use cycle?
- **Frozen source artifacts:** `cognitive_logic/obid/tools/tool-definitions-v1.md`; `cognitive_logic/obid/react/react-control-v1.md`; `cognitive_logic/obid/prompts/system-prompt-v1.md`; final v3 workflow.
- **Relevant report note(s):** Step 7 report note and cognitive verification evidence.
- **Raw evidence:** None from Step 10 is required for design; Step 7 readiness records observable calls.
- **Processed evidence:** None.
- **Expected table(s):** Tool; read-only input; output; permitted role; prohibited effects.
- **Expected future figure(s):** Optional bounded event→tool observation→decision flow.
- **References needed later:** ReAct; LLM tool use; bounded agent execution.
- **Provenance:** Tool definitions, wrapper choices, ReAct control, and prompt `OBID_CREATED`; status data comes from inherited middleware.
- **Limitations/caveats:** Neither tool executes fan actions; do not report hidden reasoning or a generic tool platform; retained compatibility failures belong to implementation history.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.6 Bounded-Memory Design

- **Purpose:** Explain the selected state representation and its role in duplicate suppression.
- **Main claim/question:** How can two recent completed interactions provide state context while bounding model-visible memory?
- **Frozen source artifacts:** `cognitive_logic/obid/memory/window-buffer-v1.md`; `evaluation/cases/obid-evaluation-cases.json`; final v3 workflow.
- **Relevant report note(s):** Steps 5 and 7 report notes.
- **Raw evidence:** Step 7 readiness supports inclusion/eviction/isolation; Step 10 raw memory A/B/C records support later results, not the original design claim.
- **Processed evidence:** `processed/rq1-summary.csv` and `rq3-reliability.csv` are later result sources.
- **Expected table(s):** Window length; session key; cold/warm behavior; state use; limitation.
- **Expected future figure(s):** Active two-interaction window and A→B→C state sequence.
- **References needed later:** Bounded/window memory in LLM-agent systems.
- **Provenance:** Memory implementation and state-dependent oracle `OBID_CREATED`.
- **Limitations/caveats:** One process-local strategy; not restart-durable; exclusion from active context is not physical deletion; no superiority or component-ablation claim.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.7 Structured Output and Shared Contract Boundary

- **Purpose:** Separate the internal decision envelope from the unchanged shared action object.
- **Main claim/question:** How can `emit_action` or internal `no_action` support state-aware decisions without changing the shared action contract?
- **Frozen source artifacts:** `cognitive_logic/obid/structured-output/decision-envelope-v1.md`; both shared JSON schemas; `shared_interfaces/contract-freeze.md`; final v3 workflow.
- **Relevant report note(s):** Steps 5 and 7 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Internal envelope fields versus nested shared action fields; emitted action versus no-op boundary.
- **Expected future figure(s):** Optional envelope-to-contract mapping.
- **References needed later:** Structured output and interface-contract literature.
- **Provenance:** Internal envelope/no-op `OBID_CREATED`; action and sensor contracts Yacoub-originated `SHARED_INTERFACE`.
- **Limitations/caveats:** `no_action` is absence of a shared action, not a new `action_id`; do not claim Obid authored or expanded the schemas.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.8 Runtime Validation and Deterministic Policy

- **Purpose:** Describe the release-control design after cognition.
- **Main claim/question:** How do parse, contract-specific validation, and deterministic policy produce `ALLOW`, `BLOCK`, or `APPROVAL_REQUIRED` before endpoint routing?
- **Frozen source artifacts:** `safety_layer/validator/runtime-action-validator-v1.md`; `safety_layer/policies/runtime-action-policy-v1.md`; `safety_layer/outcomes/safety-outcome-v1.md`; `safety_layer/workflows/runtime-safety-v1.json`; `runtime-safety-v2-hitl.json`.
- **Relevant report note(s):** Steps 8, 9, and 11 report notes.
- **Raw evidence:** Step 8 readiness evidence supports enforcement existence; Step 10 invalid/HITL raw records support final outcomes.
- **Processed evidence:** RQ2 summary and traceability are later result sources.
- **Expected table(s):** Parse/validation/policy outcome; reason code; held/released action; endpoint behavior.
- **Expected future figure(s):** Validator→policy decision tree.
- **References needed later:** Runtime validation, deterministic policy, guardrails, and defense-in-depth.
- **Provenance:** Validator, reason codes, policy, and runtime wiring `OBID_CREATED`; enforced action contract `SHARED_INTERFACE`.
- **Limitations/caveats:** Handwritten deterministic contract-specific implementation, not a generic schema or security engine; invalid actions cannot be rescued by HITL.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.9 Human-in-the-Loop Design

- **Purpose:** Define pending, approval, denial, held-action integrity, and release invariants.
- **Main claim/question:** How does the final native Wait/form gate prevent release while pending and release only the unchanged held action after actual approval?
- **Frozen source artifacts:** `safety_layer/hitl/runtime-hitl-v1.md`; `safety_layer/hitl/hitl-outcome-v1.md`; `safety_layer/hitl/workflows/step-09-hitl-harness.json`; `runtime-hitl-v1.json`; `safety_layer/workflows/runtime-safety-v2-hitl.json`; final v3 workflow.
- **Relevant report note(s):** Step 9 and Step 11 report notes.
- **Raw evidence:** Step 9 readiness evidence; Step 10 `raw/hitl-pending.jsonl`, run records, and attempt events for later results.
- **Processed evidence:** `processed/hitl-timing.csv`; `processed/rq2-summary.csv` with correction.
- **Expected table(s):** Pending/approve/deny invariants; stored action; human decision; release and endpoint behavior.
- **Expected future figure(s):** HITL state transition and caller-embedded Wait placement.
- **References needed later:** HITL and human oversight.
- **Provenance:** Executable mechanism, context, form, timing, integrity check, and repair `OBID_CREATED`; original specification `YACOUB_INHERITED` / `REFERENCE_ONLY`.
- **Limitations/caveats:** Distinguish final embedded Wait/form from retained child-Wait propagation failure; field-level integrity is not cryptographic; controlled policy input is not autonomous risk discovery.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.10 Evaluation-Oriented Design Decisions

- **Purpose:** Show how seams, observable terminals, state, timing, and versioning were designed to support RQ evidence.
- **Main claim/question:** Which design choices make malformed input, invalid action, HITL waiting, endpoint non-execution, state dependence, and latency traceable?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/experiment-freeze.json`; `raw/raw-data-manifest.json`; safety/HITL harnesses.
- **Relevant report note(s):** Steps 5, 8, 9, and 10 report notes.
- **Raw evidence:** `raw/run-records.jsonl`; `attempt-events.jsonl`; `hitl-pending.jsonl`.
- **Processed evidence:** `processed/traceability.csv`.
- **Expected table(s):** Design seam; case family; injected input/context; expected terminal; retained observation.
- **Expected future figure(s):** Optional evaluation-seam overlay on architecture.
- **References needed later:** Evaluation observability and fault-injection literature if used.
- **Provenance:** Evaluation seams and protocol `OBID_CREATED`; shared boundary retained.
- **Limitations/caveats:** Exact controlled seams bound the claims; invalid action was post-agent injection and HITL was controlled policy input.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 4.11 Final System Architecture

- **Purpose:** Present one authoritative end-to-end frozen architecture.
- **Main claim/question:** What exact path connects sensor/test event, cognition, two tools, bounded memory, structured candidate/no-op, validation, policy, HITL, inherited middleware, and simulated state?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-artifact-manifest.json`; `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`; `safety_layer/workflows/runtime-safety-v2-hitl.json`; `integration/yacoub_compat/boundary-map.md`.
- **Relevant report note(s):** Step 11 report note, supported by Steps 4 and 7–9.
- **Raw evidence:** None required for the diagram; readiness and Step 10 evidence validate represented runtime paths.
- **Processed evidence:** None.
- **Expected table(s):** Optional architecture element; artifact path/hash; provenance.
- **Expected future figure(s):** Final agentic architecture with clear `YACOUB_INHERITED`, `SHARED_INTERFACE`, and `OBID_CREATED` bands.
- **References needed later:** None specific beyond concepts already established in Chapter 2.
- **Provenance:** Mixed, labelled at component level.
- **Limitations/caveats:** Exclude credentials, owner/project data, transient HITL URLs, screenshots, physical hardware, and any unimplemented validator-agent branch.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_FIGURE`.

### 4.12 Summary of Chosen Approach

- **Purpose:** Close the design chapter by connecting constraints, decisions, architecture, and RQs.
- **Main claim/question:** Why is the frozen single-agent plus deterministic runtime-control architecture the selected bounded approach?
- **Frozen source artifacts:** `docs/ongoing/final-claim-evidence-map.md`; `docs/ongoing/final-implementation-freeze.md`; `docs/decisions.md`.
- **Relevant report note(s):** Step 11 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None; refer to earlier chapter tables.
- **Expected future figure(s):** None beyond Section 4.11.
- **References needed later:** None new.
- **Provenance:** Mixed; summary must preserve all prior labels.
- **Limitations/caveats:** Draft after Sections 4.1–4.11; summarize rationale rather than results or chronology.
- **Status:** `DRAFTED_NEEDS_AUDIT`.

## Chapter 5 — Implementation

### Chapter 5 overview

- **Purpose:** Describe the frozen implementation as one integrated system while retaining component lineage and evidence boundaries.
- **Main claim/question:** How was the selected single-agent cognition, runtime reliability, HITL, and evaluation support implemented on the Yacoub-compatible n8n boundary?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-artifact-manifest.json`; final baseline/Obid/safety/HITL workflows; runtime and evaluation manifests.
- **Relevant report note(s):** Steps 3–11 report notes, with Steps 7–9 primary for the Obid implementation.
- **Raw evidence:** Step 10 raw data demonstrates evaluated execution; Steps 3–9 evidence demonstrates implementation/readiness.
- **Processed evidence:** Step 10 processed outputs only where evaluation tooling or traceability is described.
- **Expected table(s):** Runtime; integration; baseline; version lineage; tools; memory; validation; policy; HITL; seams; tooling; frozen identities.
- **Expected future figure(s):** Implemented end-to-end component path.
- **References needed later:** Official n8n/node documentation and Chapter 2 concepts where technical behavior needs external grounding.
- **Provenance:** Component-level `YACOUB_INHERITED`, `SHARED_INTERFACE`, and `OBID_CREATED`.
- **Limitations/caveats:** Do not invent an Obid Python middleware section, hide retained failures, or describe readiness observations as Step 10 results.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.1 System Overview

- **Purpose:** Orient the reader to the implemented runtime components and data/action flow.
- **Main claim/question:** Which frozen artifacts collectively implement `CONFIG-BASELINE`, `CONFIG-OBID`, validation/policy, HITL, and the inherited action boundary?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-artifact-manifest.json`; `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`.
- **Relevant report note(s):** Steps 6–9 and 11 report notes.
- **Raw evidence:** None directly; Step 10 confirms final evaluated topology.
- **Processed evidence:** None.
- **Expected table(s):** Component; final artifact; role; provenance; evaluation use.
- **Expected future figure(s):** Implemented end-to-end component path, potentially reuse Chapter 4 architecture with implementation identifiers.
- **References needed later:** None new.
- **Provenance:** Mixed and explicit.
- **Limitations/caveats:** Avoid repeating all Chapter 4 rationale; state one agent, actual runtime controls, and simulated endpoint.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_FIGURE`.

### 5.2 Frozen n8n Runtime

- **Purpose:** Document the reproducible execution environment.
- **Main claim/question:** What exact n8n, container image/digest, persistence, timezone, node, and model-control environment hosted the workflows?
- **Frozen source artifacts:** `infrastructure/docker/docker-compose.yml`; `infrastructure/docker/runtime-manifest.md`; `infrastructure/docker/evidence/step-03-runtime-verification.md`; `evaluation/results/step-10/experiment-freeze.json`.
- **Relevant report note(s):** Steps 3, 6, 10, and 11 report notes.
- **Raw evidence:** `raw/operational-deviations.jsonl` records three pre-run non-semantic restorations.
- **Processed evidence:** None.
- **Expected table(s):** n8n version; image/digest; storage; port; timezone; model; options; fallback; credential prerequisite.
- **Expected future figure(s):** None.
- **References needed later:** Official n8n and Docker documentation for platform behavior, if cited.
- **Provenance:** Active runtime configuration/evidence `OBID_CREATED`; reproduced compatibility assumptions originate with Yacoub.
- **Limitations/caveats:** Private credential attachment remains external; provider backend/defaults are not immutable; no Pi deployment.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`.

### 5.3 Yacoub-Compatible Integration Boundary

- **Purpose:** Describe how n8n exchanges events/status/actions with the actual inherited middleware.
- **Main claim/question:** How are `/sensor-event`, `/status`, `/fan/on`, and `/fan/off` reached without a competing middleware implementation?
- **Frozen source artifacts:** `integration/yacoub_compat/boundary-map.md`; `integration/yacoub_compat/test-plan.md`; `integration/yacoub_compat/workflows/step-04-boundary-test.json`; `integration/yacoub_compat/evidence/step-04-integration-verification.md`; shared schemas.
- **Relevant report note(s):** Step 4 report note; Step 11 provenance summary.
- **Raw evidence:** Step 4 one-off integration executions only; Step 10 endpoint fields are final experimental observations.
- **Processed evidence:** `processed/traceability.csv` where endpoint linkage is needed later.
- **Expected table(s):** Direction; host/container address; endpoint; payload/action semantics; ownership.
- **Expected future figure(s):** Inbound/outbound network boundary map.
- **References needed later:** API/middleware concepts already established in Chapter 2.
- **Provenance:** Middleware, normalization, routes, state, and responses `YACOUB_INHERITED`; semantics `SHARED_INTERFACE`; workflow/test observations `OBID_CREATED`.
- **Limitations/caveats:** Do not claim an Obid Python middleware implementation; inherited `{}`/empty normalization is not Obid validation; use repository-relative paths only.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_FIGURE`.

### 5.4 Inherited Minimal Agent Baseline

- **Purpose:** Describe the executable `CONFIG-BASELINE` used for RQ3 comparison.
- **Main claim/question:** How does the inherited stateless one-decision workflow parse and route model output under the shared semantics?
- **Frozen source artifacts:** `cognitive_logic/baselines/yacoub/minimal-agent-baseline.json`; `system-prompt-v1.md`; `memory-choice-v1.md`; `baseline-manifest.md`; `evidence/step-06-baseline-verification.md`.
- **Relevant report note(s):** Steps 6, 10, and 11 report notes.
- **Raw evidence:** Step 6 one-off readiness; Step 10 baseline records are final performance evidence.
- **Processed evidence:** `processed/rq3-reliability.csv`; `processed/rq3-latency.csv`.
- **Expected table(s):** Workflow; model; prompt; parser; routing; memory; limitations; reproduction repair; provenance.
- **Expected future figure(s):** Optional compact baseline flow beside the Obid flow.
- **References needed later:** Citation for Yacoub's source/report and official Gemini/n8n node details if needed.
- **Provenance:** Baseline architecture, prompt, parser/routing, no-memory semantics `YACOUB_INHERITED`; reconstruction/sanitization/readiness evidence `OBID_CREATED`.
- **Limitations/caveats:** RQ3 comparator is this minimal agent, not the deterministic anchor; output fences and missing historical modelName are retained limitations; no Obid validator/policy/HITL.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.5 CONFIG-OBID Decision Agent

- **Purpose:** Describe the final one-agent cognitive execution and preserved v1/v2/v3 lineage.
- **Main claim/question:** How does the Decision Agent accept a valid event, use bounded tools/memory, and produce an internal structured decision?
- **Frozen source artifacts:** `cognitive_logic/obid/workflows/obid-agent-v1.json`; `obid-agent-v2-safety.json`; `obid-agent-v3-hitl.json`; `cognitive_logic/obid/configuration-manifest.md`.
- **Relevant report note(s):** Steps 7–9 and 11 report notes.
- **Raw evidence:** Step 7 readiness supports cognition/tool/memory existence; Step 10 final records support evaluated behavior.
- **Processed evidence:** RQ1 and RQ3 reliability summaries later quantify output.
- **Expected table(s):** v1 cognitive snapshot; v2 safety integration; v3 HITL integration; unchanged components.
- **Expected future figure(s):** One-agent node/component path.
- **References needed later:** n8n AI Agent and Gemini node authoritative documentation.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Present lineage by capability, not as a project diary; exactly one agent/model node; no validator agent or fallback model.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.6 System Prompt and Structured Decision Envelope

- **Purpose:** Explain the prompt constraints and the parser-visible internal output shape.
- **Main claim/question:** How are permitted tools, threshold semantics, state use, duplicate suppression, and final decision structure represented?
- **Frozen source artifacts:** `cognitive_logic/obid/prompts/system-prompt-v1.md`; `cognitive_logic/obid/structured-output/decision-envelope-v1.md`; final v3 workflow.
- **Relevant report note(s):** Step 7 report note and cognitive verification evidence.
- **Raw evidence:** Step 7 outputs support readiness; Step 10 raw `CONFIG-OBID` records support final outcomes.
- **Processed evidence:** `processed/rq1-summary.csv` and `rq3-reliability.csv` only for later result linkage.
- **Expected table(s):** Prompt constraint; runtime representation; observable evidence; enforcement boundary.
- **Expected future figure(s):** Optional internal envelope example/mapping.
- **References needed later:** Structured-output prompting and agent instruction design.
- **Provenance:** Prompt and envelope `OBID_CREATED`; nested shared action fields `SHARED_INTERFACE`; threshold meaning inherited.
- **Limitations/caveats:** Prompt text alone is not reliability/safety evidence; `no_action` remains internal; do not reveal or infer hidden reasoning.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.7 Tool Implementation

- **Purpose:** Describe the executable temperature-threshold and fan-status tool nodes.
- **Main claim/question:** What deterministic/read-only behavior, inputs, outputs, and boundaries does each tool implement?
- **Frozen source artifacts:** `cognitive_logic/obid/tools/tool-definitions-v1.md`; embedded tool nodes/subworkflow in `obid-agent-v3-hitl.json`; `cognitive_logic/obid/evidence/step-07-cognitive-verification.md`.
- **Relevant report note(s):** Step 7 report note.
- **Raw evidence:** Step 7 readiness execution evidence for call identity/order and retained repair failures.
- **Processed evidence:** None.
- **Expected table(s):** Tool name; n8n node type; input; output; side effects; call constraints.
- **Expected future figure(s):** Optional two-tool call flow.
- **References needed later:** Official n8n Tool Code/Workflow Tool documentation.
- **Provenance:** Tool definitions/wrappers `OBID_CREATED`; threshold semantics and `/status` source inherited/shared.
- **Limitations/caveats:** Neither tool executes an action; report singleton-enum/wrapper/legacy HTTP Tool repairs as bounded compatibility history, not result rows.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.8 Controlled ReAct Execution

- **Purpose:** Describe the bounded observable agent/tool cycle and termination controls.
- **Main claim/question:** How are tool choices constrained and completion bounded at `maxIterations: 3`?
- **Frozen source artifacts:** `cognitive_logic/obid/react/react-control-v1.md`; system prompt; final v3 workflow; Step 7 evidence.
- **Relevant report note(s):** Step 7 report note.
- **Raw evidence:** Step 7 readiness executions retain tool count/order and final output; no hidden reasoning.
- **Processed evidence:** None.
- **Expected table(s):** Max iterations; allowed tools; per-tool call bounds; retained observations; termination behavior.
- **Expected future figure(s):** Observable bounded tool-use cycle.
- **References needed later:** ReAct and n8n Agent execution documentation.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** `intermediateSteps: false`; hidden chain-of-thought/scratchpad was not collected; model-call count is not a reasoning-step measure.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.9 Bounded Memory

- **Purpose:** Describe the Simple Memory node, window size, session key, state behavior, isolation, and eviction evidence.
- **Main claim/question:** How does a two-interaction process-local window make recent state available across A→B→C?
- **Frozen source artifacts:** `cognitive_logic/obid/memory/window-buffer-v1.md`; final v3 workflow; Step 7 cognitive evidence.
- **Relevant report note(s):** Steps 7, 10, and 11 report notes.
- **Raw evidence:** Step 7 readiness for inclusion/eviction/isolation; Step 10 raw memory sequences for evaluated outcomes.
- **Processed evidence:** `processed/rq1-summary.csv`; `processed/rq3-reliability.csv`.
- **Expected table(s):** `contextWindowLength: 2`; custom session key; cold/warm/reset behavior; evidence; limitation.
- **Expected future figure(s):** A→B→C session/state sequence and active-window view.
- **References needed later:** n8n Simple Memory documentation and bounded-memory literature.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Process-local and not restart-durable; active-window exclusion is not physical deletion; no memory-strategy comparison or causal ablation.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.10 Runtime Action Validation

- **Purpose:** Describe parsing and deterministic enforcement of every frozen action-contract constraint.
- **Main claim/question:** How are malformed JSON, root type, required/extra fields, enums, target, reason, and Boolean approval flag checked before policy?
- **Frozen source artifacts:** `safety_layer/validator/runtime-action-validator-v1.md`; `safety_layer/workflows/runtime-safety-v1.json`; `runtime-safety-v2-hitl.json`; action schema.
- **Relevant report note(s):** Steps 8, 9, and 11 report notes.
- **Raw evidence:** Step 8 readiness matrix; Step 10 invalid-action records.
- **Processed evidence:** `processed/rq2-summary.csv`; `processed/traceability.csv`.
- **Expected table(s):** Constraint; stable reason code; validation status; terminal/release behavior.
- **Expected future figure(s):** Optional validator stage flow.
- **References needed later:** JSON Schema/validation concepts and n8n Code node documentation.
- **Provenance:** Validator implementation/reason codes `OBID_CREATED`; enforced schema Yacoub-originated `SHARED_INTERFACE`.
- **Limitations/caveats:** Handwritten deterministic JavaScript specific to the frozen contract, not a general draft-2020-12 library or generic security engine; no coercion/repair.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.11 Deterministic Action Policy

- **Purpose:** Describe the policy stage and structural release invariant.
- **Main claim/question:** How are schema-valid actions routed to direct release, block, or approval-required hold?
- **Frozen source artifacts:** `safety_layer/policies/runtime-action-policy-v1.md`; `safety_layer/outcomes/safety-outcome-v1.md`; both safety workflows.
- **Relevant report note(s):** Steps 8 and 9 report notes.
- **Raw evidence:** Step 8 readiness; Step 10 invalid/HITL raw records.
- **Processed evidence:** `processed/rq2-summary.csv` interpreted through correction.
- **Expected table(s):** `ALLOW`; `BLOCK`; `APPROVAL_REQUIRED`; prerequisites; held/released action; endpoint eligibility.
- **Expected future figure(s):** Policy decision tree, possibly combined with validation.
- **References needed later:** Deterministic policy/guardrail literature.
- **Provenance:** `OBID_CREATED`; endpoint/action meanings inherited/shared.
- **Limitations/caveats:** Narrow allowlist/policy context; no dynamic risk engine, autonomous risk discovery, or generic security enforcement.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.12 Human-in-the-Loop Runtime

- **Purpose:** Describe native n8n waiting, form decision, held-action snapshot, integrity comparison, release/denial routing, and timing fields.
- **Main claim/question:** How does the final caller-embedded gate implement actual approve/deny behavior?
- **Frozen source artifacts:** `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`; `safety_layer/workflows/runtime-safety-v2-hitl.json`; `safety_layer/hitl/runtime-hitl-v1.md`; `hitl-outcome-v1.md`; `hitl/workflows/step-09-hitl-harness.json`; `runtime-hitl-v1.json`.
- **Relevant report note(s):** Steps 9, 10, and 11 report notes.
- **Raw evidence:** Step 9 readiness; Step 10 `raw/hitl-pending.jsonl`, run records, and attempt events.
- **Processed evidence:** `processed/hitl-timing.csv`; `processed/rq2-summary.csv` plus correction.
- **Expected table(s):** Wait/form; displayed/stored fields; allowed decision; integrity check; approve/deny terminal; timing fields.
- **Expected future figure(s):** Pending→approve/deny runtime flow and repaired caller placement.
- **References needed later:** Official n8n Wait/form documentation; HITL sources.
- **Provenance:** Runtime HITL implementation and bounded repair `OBID_CREATED`; original Yacoub HITL concept `YACOUB_INHERITED` / `REFERENCE_ONLY`.
- **Limitations/caveats:** Retain original child-Wait propagation failure and fail-closed outcome; no reviewer identity, cryptographic integrity, timeout/replay/idempotency proof, or general human-time estimate.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.13 Evaluation Seams and Harnesses

- **Purpose:** Describe controlled ingress and injection points that isolate components under test.
- **Main claim/question:** How do direct pre-decision, post-agent/pre-validator, and policy-input seams produce attributable observations?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`; `safety_layer/workflows/step-08-safety-harness.json`; `safety_layer/hitl/workflows/step-09-hitl-harness.json`; final workflows.
- **Relevant report note(s):** Steps 5, 8, 9, and 10 report notes.
- **Raw evidence:** Step 10 raw records and pending snapshots identify seam/case behavior.
- **Processed evidence:** `processed/traceability.csv`; RQ summaries.
- **Expected table(s):** Seam; injected object/context; component under test; bypassed component; expected/observed terminal.
- **Expected future figure(s):** Evaluation seams overlaid on the implementation path.
- **References needed later:** Fault-injection/test-seam literature if used.
- **Provenance:** Harnesses/seams `OBID_CREATED`; contracts/endpoints retain original labels.
- **Limitations/caveats:** `fan_reverse` was injected post-agent; HITL repetitions entered at exact controlled policy input; do not claim natural invalid generation or autonomous risk discovery.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.14 Repeated Evaluation Tooling

- **Purpose:** Describe automated schedule execution, n8n evidence extraction, raw locking, processing, and traceability.
- **Main claim/question:** How were 85 planned attempts orchestrated and transformed into reproducible summaries without replacing failures?
- **Frozen source artifacts:** `evaluation/results/step-10/run_step10.py`; `extract_n8n_execution.js`; `process_results.py`; `experiment-freeze.json`; raw and processed manifests.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** `raw/planned-order.json`; `run-order.csv`; `run-records.jsonl`; `attempt-events.jsonl`; `hitl-pending.jsonl`; `operational-deviations.jsonl`.
- **Processed evidence:** All eight processed outputs and `processed-data-manifest.json`.
- **Expected table(s):** Tool; input; output; validation/hash checks; traceability role.
- **Expected future figure(s):** Orchestration→raw lock→processor→tables pipeline.
- **References needed later:** Reproducible experiment tooling/provenance if discussed generally.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Processor preserves failures and historical RQ2 flag; correction is append-only; no outlier removal, replacement, hidden reasoning, or cost estimation.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 5.15 Final Configuration and Reproducibility

- **Purpose:** Give exact final workflow, prompt, runtime, contract, data, and hash identities needed to reproduce or audit the study.
- **Main claim/question:** Which values and artifacts are frozen, and which external prerequisites/defaults remain outside repository control?
- **Frozen source artifacts:** `docs/ongoing/final-artifact-manifest.json`; `docs/ongoing/final-implementation-freeze.md`; `evaluation/results/step-10/experiment-freeze.json`; runtime manifest; contract freeze; raw/processed manifests.
- **Relevant report note(s):** Steps 3, 6, 10, and 11 report notes.
- **Raw evidence:** Raw manifest and hashes.
- **Processed evidence:** Processed manifest and hashes.
- **Expected table(s):** Frozen identity; repository path; SHA-256/value; provenance; external prerequisite/limitation.
- **Expected future figure(s):** None.
- **References needed later:** Official platform/model API documentation if exact reproducibility assumptions are discussed.
- **Provenance:** Manifest/freeze/reproducibility packaging `OBID_CREATED`; baseline artifacts inherited; contracts shared.
- **Limitations/caveats:** Stored options `{}`; provider defaults/backend may change; private credential required but not frozen; model settings beyond stored options are not invented; simulated fan only.
- **Status:** `DRAFTED_NEEDS_AUDIT`, `NEEDS_REFERENCE`.

### 5.16 Summary of Implementation

- **Purpose:** Close the chapter with the implemented capability chain and traceable artifact boundary.
- **Main claim/question:** What final implementation exists between the event ingress and inherited simulated action boundary?
- **Frozen source artifacts:** `docs/ongoing/final-claim-evidence-map.md`; `docs/ongoing/final-implementation-freeze.md`; final artifact manifest.
- **Relevant report note(s):** Step 11 report note.
- **Raw evidence:** None directly.
- **Processed evidence:** None directly.
- **Expected table(s):** None; point back to the chapter's implementation tables.
- **Expected future figure(s):** None beyond Section 5.1.
- **References needed later:** None new.
- **Provenance:** Summarize `OBID_CREATED` implementation without absorbing inherited/shared components.
- **Limitations/caveats:** Draft after Sections 5.1–5.15; do not preview full results or claim runtime controls beyond their frozen seams.
- **Status:** `DRAFTED_NEEDS_AUDIT`.

## Chapter 6 — Results

### Chapter 6 overview

- **Purpose:** Present the frozen Step 10 observations that answer RQ1–RQ3, plus integrity, timing, telemetry, failures, and the R03 correction.
- **Main claim/question:** What was observed across the 85 retained primary attempts under the exact frozen configurations, cases, and protocol?
- **Frozen source artifacts:** Step 5 oracle/protocol; `evaluation/results/step-10/experiment-freeze.json`; all locked raw and processed Step 10 artifacts; R03 correction; final freeze/claim map.
- **Relevant report note(s):** Steps 10 and 11 report notes; Steps 6–9 notes only for implementation/readiness context.
- **Raw evidence:** `evaluation/results/step-10/raw/` is primary for observations.
- **Processed evidence:** All outputs under `evaluation/results/step-10/processed/`, with `processed/traceability.csv` and the correction hierarchy.
- **Expected table(s):** Dataset integrity; RQ1; RQ2 invalid/HITL/R03; RQ3 reliability/latency; HITL timing; telemetry; negative outcomes.
- **Expected future figure(s):** Optional RQ1 correctness, paired RQ3 reliability, latency observations, and segmented HITL timing, all derived only from frozen data.
- **References needed later:** None for raw numerical facts; method/interpretation citations belong in Chapters 2, 3, and 7.
- **Provenance:** Step 10 orchestration, observations, processing, correction, and tables `OBID_CREATED`; comparator `YACOUB_INHERITED`; contracts `SHARED_INTERFACE`.
- **Limitations/caveats:** Report results before interpretation; descriptive n=5/cell; simulated fan; no significance, universal reliability, production safety, or causal component attribution.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.1 Evaluation Overview

- **Purpose:** Orient the reader to the experiment phases, RQs, case families, and primary measures.
- **Main claim/question:** How do 70 core, five invalid-action, and ten HITL records map to the three RQs?
- **Frozen source artifacts:** `evaluation/evidence/step-10-repeated-evaluation.md`; `evaluation/results/step-10/experiment-freeze.json`; `processed/summary.md`; Step 5 case/protocol artifacts.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`; `raw/run-order.csv`.
- **Processed evidence:** `processed/summary.md`; all RQ summary CSVs.
- **Expected table(s):** RQ; case families; configurations; primary records; primary metric; principal evidence.
- **Expected future figure(s):** Optional experiment overview only if not redundant with Chapter 3.
- **References needed later:** None.
- **Provenance:** `OBID_CREATED` evaluation; inherited comparator clearly labelled.
- **Limitations/caveats:** Step 10 results control; Steps 3–9 readiness evidence is not a substitute; no optional validator-agent records.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.2 Execution Integrity and Dataset

- **Purpose:** Demonstrate schedule completion, raw locking, uniqueness, order integrity, and failure retention before reporting outcomes.
- **Main claim/question:** Were all 85 scheduled attempts retained without replacement or result-driven tuning?
- **Frozen source artifacts:** `evaluation/results/step-10/raw/raw-data-manifest.json`; `raw-data-manifest.md`; `experiment-freeze.json`; final artifact manifest.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** `raw/planned-order.json`; `raw/run-order.csv`; `raw/run-records.jsonl`; `raw/attempt-events.jsonl`; `raw/operational-deviations.jsonl`.
- **Processed evidence:** `processed/traceability.csv`; `processed/processed-data-manifest.json`.
- **Expected table(s):** Core 70; invalid 5; HITL 10; total 85; automated-latency eligible 30; unique run/execution IDs; replaced runs 0; order deviations 0.
- **Expected future figure(s):** Optional run-order/integrity timeline.
- **References needed later:** None.
- **Provenance:** Scheduling, records, locks, processing, and traceability `OBID_CREATED`.
- **Limitations/caveats:** Three pre-run non-semantic restorations are retained; two baseline malformed non-success executions remain in denominators; child executions are linked evidence, not extra repetitions.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.3 RQ1 — CONFIG-OBID Accuracy and Consistency

- **Purpose:** Report expected-outcome correctness and modal agreement for all seven RQ1 families.
- **Main claim/question:** Within the frozen cases, how accurately and consistently did `CONFIG-OBID` produce the expected observable outcome?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`; final v3 workflow.
- **Relevant report note(s):** Steps 10 and 11 report notes; Step 7 note for implementation context.
- **Raw evidence:** `evaluation/results/step-10/raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq1-summary.csv`; `processed/traceability.csv`.
- **Expected table(s):** High, Low, Threshold, Malformed, Memory A, Memory B, Memory C: each 5/5 and 100% modal agreement; total 35/35.
- **Expected future figure(s):** Optional case-family correctness/consistency chart.
- **References needed later:** None for the result values.
- **Provenance:** `CONFIG-OBID` and evaluation `OBID_CREATED`; expected threshold/action semantics inherit the shared Yacoub boundary.
- **Limitations/caveats:** Exact frozen cases, one domain/model/memory configuration, n=5/family; natural-language reason not exact-scored; no universal reliability claim.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.4 RQ2 — Invalid-Action Validation Results

- **Purpose:** Report repeated handling of the frozen unsupported-action injection.
- **Main claim/question:** Did the runtime validator prevent the injected `fan_reverse` candidate from reaching policy release or either action endpoint?
- **Frozen source artifacts:** Action schema; `evaluation/cases/obid-evaluation-cases.json`; validator/policy workflows and specifications.
- **Relevant report note(s):** Steps 8, 10, and 11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`; `raw/attempt-events.jsonl`.
- **Processed evidence:** `processed/rq2-summary.csv`; `processed/traceability.csv`.
- **Expected table(s):** Five attempts; `UNKNOWN_ACTION`; schema invalid; policy/release absent; `/fan/on: 0`; `/fan/off: 0`; fan off; correctness 5/5.
- **Expected future figure(s):** Optional invalid-action outcome flow; no chart required for one family.
- **References needed later:** None for the result; theory citations belong in Chapters 2/7.
- **Provenance:** Injection, validator, policy, observations, and processing `OBID_CREATED`; rejected contract `SHARED_INTERFACE`.
- **Limitations/caveats:** One post-agent fault-injected unsupported action; do not claim the model naturally generated it, every invalid form was repeated, or arbitrary-input prevention.
- **Status:** `READY_TO_DRAFT`.

### 6.5 RQ2 — HITL Pending, Approval, and Denial Results

- **Purpose:** Report all waiting-state observations and assigned/actual human-decision outcomes.
- **Main claim/question:** Did actions remain held while pending, and what happened after assigned approval or denial trials?
- **Frozen source artifacts:** HITL case definitions/protocol; final v3 workflow; safety-v2 and HITL harness.
- **Relevant report note(s):** Steps 9, 10, and 11 report notes.
- **Raw evidence:** `raw/hitl-pending.jsonl`; `raw/run-records.jsonl`; `raw/attempt-events.jsonl`.
- **Processed evidence:** `processed/rq2-summary.csv`; `processed/hitl-timing.csv`; `processed/traceability.csv`, subject to R03 correction.
- **Expected table(s):** Ten pending safe snapshots; assigned approval 5/5; assigned denial 4/5; planned 5 approve/5 deny; actual 6 approve/4 deny; deviation 1; invalid/unapproved crossings 0.
- **Expected future figure(s):** Optional pending/approve/deny outcome figure.
- **References needed later:** None for observed values.
- **Provenance:** HITL runtime/evaluation `OBID_CREATED`; approved action and endpoint semantics shared/inherited.
- **Limitations/caveats:** Exact controlled policy-input seam; no autonomous risk discovery; assigned family and actual decision must be separated; do not report a balanced actual 5/5 split.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.6 RQ2 — Denial-R03 Protocol Deviation and Correction

- **Purpose:** Transparently reconcile planned denial, actual approval, assigned correctness, and the historical processed crossing flag.
- **Main claim/question:** How should `S10_EVAL-HITL-01B_CONFIG-OBID_R03` be interpreted without rewriting history?
- **Frozen source artifacts:** `evaluation/results/step-10/corrections/rq2-hitl-denial-r03-interpretation.md`; Step 5 HITL oracle/protocol.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** R03 row in `raw/run-records.jsonl`; `raw/attempt-events.jsonl`; `raw/hitl-pending.jsonl`; `raw/planned-order.json`; `raw/run-order.csv`.
- **Processed evidence:** Historical `processed/rq2-summary.csv` and `processed/summary.md` retain crossing=1; `processed/traceability.csv` links the row.
- **Expected table(s):** Planned deny; actual approve; safe pending; assigned result incorrect; protocol deviation 1; action released only after approval; final invalid/unapproved crossings 0.
- **Expected future figure(s):** None; a precise correction table is preferable.
- **References needed later:** None.
- **Provenance:** Raw observation, processing history, append-only correction, and interpretation `OBID_CREATED`.
- **Limitations/caveats:** R03 is not a successful denial. Historical crossing=1 is immutable but not the final safety conclusion. Preserve denial correctness 4/5, deviation 1, and crossings 0 together.
- **Status:** `READY_TO_DRAFT`.

### 6.7 RQ3 — Reliability Comparison

- **Purpose:** Compare expected observable outcomes across the seven common case families.
- **Main claim/question:** Where did `CONFIG-BASELINE` and `CONFIG-OBID` show the same or different repeated reliability?
- **Frozen source artifacts:** Step 5 oracle/protocol; baseline and final v3 workflows; final configuration manifest.
- **Relevant report note(s):** Steps 6, 7, 10, and 11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq3-reliability.csv`; `processed/traceability.csv`.
- **Expected table(s):** High 5/5 vs 5/5; Low 5/5 vs 5/5; Threshold 5/5 vs 5/5; Malformed 0/5 vs 5/5; Memory A 5/5 vs 5/5; Memory B 0/5 vs 5/5; Memory C 5/5 vs 5/5.
- **Expected future figure(s):** Paired reliability by case family.
- **References needed later:** None for values.
- **Provenance:** Baseline semantics `YACOUB_INHERITED`; Obid workflow and all Step 10 measurement/processing `OBID_CREATED`.
- **Limitations/caveats:** Baseline absence of memory is not itself scored as failure; its duplicate `fan_on` at Memory B is the scored outcome; comparator is minimal-agent `CONFIG-BASELINE`, not deterministic anchor.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.8 RQ3 — Automated Latency Comparison

- **Purpose:** Report all frozen automated-latency observations and descriptive summaries for the comparable subset.
- **Main claim/question:** What latency differences were observed for High, Low, and Threshold between the complete configurations?
- **Frozen source artifacts:** `evaluation/evaluation-protocol.md`; `experiment-freeze.json`; processed manifest.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Thirty eligible rows and five observations per cell in `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq3-latency.csv`; `processed/traceability.csv`; `processed/processed-data-manifest.json`.
- **Expected table(s):** Six configuration/case rows showing all five raw values, median, minimum, maximum, and supplementary mean. Medians: High 2130 vs 3792 ms; Low 2105 vs 4472 ms; Threshold 2083 vs 4487 ms.
- **Expected future figure(s):** Per-cell raw-observation distribution/strip plot with median markers.
- **References needed later:** None for values; descriptive-statistics interpretation cited in Chapters 3/7.
- **Provenance:** Measurements/processing `OBID_CREATED`; baseline comparator inherited.
- **Limitations/caveats:** Human wait excluded; n=5/cell; mean supplementary; no standard deviation as primary frozen metric, significance, confidence interval, outlier removal, or causal component attribution.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.9 HITL Timing Observations

- **Purpose:** Report pre-wait automation, human wait, post-decision automation, and total time separately for all ten trials.
- **Main claim/question:** What session-specific timing components were observed around the human gate?
- **Frozen source artifacts:** Step 5 timing rules; final HITL implementation.
- **Relevant report note(s):** Steps 9, 10, and 11 report notes.
- **Raw evidence:** Timing fields in `raw/run-records.jsonl`.
- **Processed evidence:** `processed/hitl-timing.csv`; `processed/traceability.csv`.
- **Expected table(s):** Ten rows: assigned trial, actual decision, pre-wait ms, human-wait ms, post-decision ms, total ms.
- **Expected future figure(s):** Optional segmented timing observations, clearly separating human wait.
- **References needed later:** None for values.
- **Provenance:** Timing instrumentation/observations `OBID_CREATED`.
- **Limitations/caveats:** Session-specific observations, not population estimates; human waiting must remain outside RQ3 automated latency; R03 actual decision is approve.
- **Status:** `READY_TO_DRAFT`, `NEEDS_FIGURE`.

### 6.10 LLM and Token Telemetry Availability

- **Purpose:** Report which model-call, token, and cost fields were available without filling missing data.
- **Main claim/question:** How complete was direct LLM/token telemetry across the 85 primary records?
- **Frozen source artifacts:** Step 10 raw/processed manifests and processor.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`.
- **Processed evidence:** `processed/llm-telemetry.csv`.
- **Expected table(s):** 85 primary; 65 positive model-call paths; 20 zero-call paths; tokens available 64; not applicable 20; unavailable 1; direct cost unavailable 85.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Telemetry extraction and availability classification `OBID_CREATED`; provider-supplied fields remain provider-dependent.
- **Limitations/caveats:** Do not estimate cost, invent missing tokens, infer hidden reasoning from call counts, or treat zero-call paths as missing when not applicable.
- **Status:** `READY_TO_DRAFT`.

### 6.11 Retained Failures and Negative Outcomes

- **Purpose:** Present incorrect, failed, missing, and development/readiness observations without hiding or mixing categories.
- **Main claim/question:** Which negative outcomes were retained, and how should each be classified as an experimental result, implementation-development evidence, or a provider/measurement limitation?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-evidence-inventory.md`; Step 6–10 evidence files.
- **Relevant report note(s):** Steps 6–11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`; `raw/attempt-events.jsonl`; raw operational deviations.
- **Processed evidence:** RQ summaries, telemetry, and correction.
- **Expected table(s):** Five baseline malformed failures including two non-success; five baseline Memory-B duplicate actions; denial R03; child-Wait fail-closed; fenced baseline outputs; Step 7 tool-schema/wrapper/HTTP failures and quota interruptions; one missing token record; cost unavailable.
- **Expected future figure(s):** None; classification table is preferable.
- **References needed later:** None.
- **Provenance:** Experimental/development evidence labelled per component; baseline semantics inherited, observations and preservation `OBID_CREATED`.
- **Limitations/caveats:** Do not merge readiness failures into Step 10 denominators, erase them, or describe provider interruptions as final experimental rows.
- **Status:** `READY_TO_DRAFT`.

### 6.12 Summary of Results

- **Purpose:** Concisely restate the principal observed outcomes before Chapter 7 interpretation.
- **Main claim/question:** What bounded findings directly follow from the frozen RQ tables?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-claim-evidence-map.md`; Step 10 frozen summaries.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Trace through the sources mapped in Sections 6.2–6.11.
- **Processed evidence:** RQ1/RQ2/RQ3/latency/telemetry tables plus correction.
- **Expected table(s):** None; refer to preceding tables.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Mixed results with explicit comparator attribution.
- **Limitations/caveats:** Summarize observations only; defer causal explanation, tradeoffs, validity, and broader implications to Chapter 7.
- **Status:** `READY_TO_DRAFT`.

## Chapter 7 — Discussion

### Chapter 7 overview

- **Purpose:** Interpret the frozen results through limitations, research questions, tradeoffs, provenance, validity, relevance, ethics, and future work.
- **Main claim/question:** What do the observed outcomes mean within—and only within—the frozen design and evidence boundary?
- **Frozen source artifacts:** Final Chapter 6 tables; `docs/ongoing/final-claim-evidence-map.md`; `final-evidence-inventory.md`; `final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 6–11 report notes.
- **Raw evidence:** Consult raw Step 10 records and correction whenever processed summaries are ambiguous.
- **Processed evidence:** RQ1/RQ2/RQ3/latency/HITL/telemetry tables and traceability.
- **Expected table(s):** Optional synthesis of finding, interpretation, limitation, and implication.
- **Expected future figure(s):** None currently required; reuse Chapter 6 figures rather than inventing new measurements.
- **References needed later:** Reliability/latency tradeoffs, agent memory/tool use, validation/guardrails, HITL, validity, IoT relevance, and ethics.
- **Provenance:** Interpret mixed evidence while retaining component ownership.
- **Limitations/caveats:** Begin with limitations; no universal, production-safety, significance, superiority, hardware, or causal-component claims.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.1 Limitations First

- **Purpose:** State the audited limits before interpreting positive outcomes.
- **Main claim/question:** What must a reader know to avoid overgeneralizing the results?
- **Frozen source artifacts:** `docs/ongoing/final-implementation-freeze.md`; `docs/ongoing/final-evidence-inventory.md`; `docs/ongoing/final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 6–11 report notes.
- **Raw evidence:** Raw failures, deviations, pending snapshots, and missing telemetry.
- **Processed evidence:** All final summaries and correction.
- **Expected table(s):** Limitation; affected claim/RQ; evidence; reporting consequence.
- **Expected future figure(s):** None.
- **References needed later:** Validity/limitations framework.
- **Provenance:** Obid analysis; inherited limitations labelled.
- **Limitations/caveats:** Include one domain/model/target, simulated fan, n=5/cell, descriptive analysis, controlled seams, process-local memory, provider defaults, unequal workloads, session-specific HITL, unavailable cost, missing token row, and no optional comparisons.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.2 Interpretation of RQ1

- **Purpose:** Interpret `CONFIG-OBID` correctness and consistency across normal, malformed, and state-dependent families.
- **Main claim/question:** What can 35/35 and 100% family modal agreement support within the frozen cases?
- **Frozen source artifacts:** Chapter 6 RQ1 table; `docs/ongoing/final-claim-evidence-map.md` RQ1-01–RQ1-03.
- **Relevant report note(s):** Steps 7, 10, and 11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq1-summary.csv`; traceability.
- **Expected table(s):** Optional claim/evidence/limit synthesis.
- **Expected future figure(s):** Reuse RQ1 result figure if created.
- **References needed later:** Reliability/consistency interpretation for LLM-agent systems.
- **Provenance:** Obid workflow/evaluation `OBID_CREATED`; threshold/action interface inherited/shared.
- **Limitations/caveats:** Bounded exact cases, not universal agent reliability; one malformed form and one memory sequence; no reason-text fidelity or memory-strategy superiority.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.3 Interpretation of RQ2

- **Purpose:** Interpret invalid-action blocking, pending-state protection, approval, denial, and R03.
- **Main claim/question:** How effectively did the implemented controls prevent invalid or unapproved release in the controlled trials?
- **Frozen source artifacts:** Chapter 6 RQ2 tables; R03 correction; claim map RQ2-01–RQ2-04.
- **Relevant report note(s):** Steps 8–11 report notes.
- **Raw evidence:** `raw/run-records.jsonl`; `raw/hitl-pending.jsonl`; `raw/attempt-events.jsonl`.
- **Processed evidence:** `processed/rq2-summary.csv`; `hitl-timing.csv`; traceability, interpreted through correction.
- **Expected table(s):** Control; repeated observation; effectiveness evidence; boundary.
- **Expected future figure(s):** Reuse any Chapter 6 HITL result figure.
- **References needed later:** Runtime validation, deterministic guardrails, and HITL effectiveness.
- **Provenance:** Runtime controls/evaluation `OBID_CREATED`; schema/endpoint shared/inherited.
- **Limitations/caveats:** Retain invalid 5/5, approval 5/5, denial 4/5, deviation 1, actual 6/4, crossings 0. No production safety, arbitrary-input prevention, autonomous risk discovery, or final crossing count 1.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.4 Interpretation of RQ3

- **Purpose:** Interpret reliability similarities/differences and higher observed Obid automated latency.
- **Main claim/question:** What configuration-level differences were observed under the common cases?
- **Frozen source artifacts:** Chapter 6 RQ3 reliability and latency tables; claim map RQ3-01–RQ3-02.
- **Relevant report note(s):** Steps 6, 7, 10, and 11 report notes.
- **Raw evidence:** Eligible core rows in `raw/run-records.jsonl`.
- **Processed evidence:** `processed/rq3-reliability.csv`; `processed/rq3-latency.csv`; traceability.
- **Expected table(s):** Observation; likely bounded explanation; evidence; alternative explanation/limit.
- **Expected future figure(s):** Reuse Chapter 6 reliability and latency figures.
- **References needed later:** Agent reliability/latency interpretation.
- **Provenance:** Baseline `YACOUB_INHERITED`; Obid/evaluation `OBID_CREATED`.
- **Limitations/caveats:** No statistical significance, population inference, model superiority, or component-level causality; deterministic anchor was not compared.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.5 Reliability and Latency Tradeoff

- **Purpose:** Discuss the empirical tradeoff between broader correct behavior in two families and additional automated workload/latency.
- **Main claim/question:** How should improved frozen-case reliability in malformed/Memory B be weighed against higher observed latency in High/Low/Threshold?
- **Frozen source artifacts:** Final configuration descriptions and Chapter 6 RQ3 tables.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Thirty latency records and seventy core reliability records.
- **Processed evidence:** `processed/rq3-reliability.csv`; `processed/rq3-latency.csv`.
- **Expected table(s):** Reliability difference; latency difference; workload distinction; interpretation limit.
- **Expected future figure(s):** Optional combined comparison using only frozen values.
- **References needed later:** Reliability-latency tradeoffs in agent systems.
- **Provenance:** Analysis `OBID_CREATED`; baseline inherited.
- **Limitations/caveats:** Complete configurations perform different work; cannot isolate tools, memory, validation, policy, or HITL overhead individually; no significance claim.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`, `NEEDS_FIGURE`.

### 7.6 Role of Tools and Bounded Memory

- **Purpose:** Relate observable tool/memory design to state-dependent behavior without claiming causal superiority.
- **Main claim/question:** What bounded interpretation is supported by readiness tool observations and the Memory A/B/C outcomes?
- **Frozen source artifacts:** Tool/memory/ReAct records; final workflow; memory case oracle.
- **Relevant report note(s):** Steps 7, 10, and 11 report notes.
- **Raw evidence:** Step 7 readiness executions; Step 10 memory-sequence records.
- **Processed evidence:** `processed/rq1-summary.csv`; `processed/rq3-reliability.csv`.
- **Expected table(s):** Design feature; observable evidence; likely role; unsupported inference.
- **Expected future figure(s):** Optional reuse of memory sequence figure.
- **References needed later:** Tool use and bounded memory in LLM agents.
- **Provenance:** Tools/memory/evaluation `OBID_CREATED`; status source inherited.
- **Limitations/caveats:** No ablation, memory-strategy comparison, durable-memory claim, or proof that one component alone caused the reliability difference.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.7 Significance of Runtime Validation and HITL

- **Purpose:** Discuss the practical meaning of executable controls beyond prompt-only instructions.
- **Main claim/question:** What does observed validation, pending, approval, denial, and fail-closed behavior contribute within the bounded action interface?
- **Frozen source artifacts:** Validator/policy/HITL specifications and workflows; final claim map.
- **Relevant report note(s):** Steps 8–11 report notes.
- **Raw evidence:** Step 10 invalid/HITL records and pending snapshots; Step 9 retained child-Wait failure.
- **Processed evidence:** RQ2 summary, HITL timing, correction, and traceability.
- **Expected table(s):** Control; runtime effect; repeated evidence; residual limitation.
- **Expected future figure(s):** Optional reuse of validator/policy/HITL flow.
- **References needed later:** Runtime validation, deterministic guardrails, human oversight, fail-safe behavior.
- **Provenance:** Executable controls/evidence `OBID_CREATED`; original concepts and endpoint semantics attributed separately.
- **Limitations/caveats:** No generic security, production safety, autonomous risk discovery, timeout/replay/idempotency, or cryptographic integrity claim.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.8 Inherited and Obid Attribution

- **Purpose:** Reflect on why provenance matters to the interpretation of an integrated collaborative system.
- **Main claim/question:** Which conclusions concern inherited infrastructure versus the new Obid layer and evidence?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; `docs/ongoing/yacoub-handoff.md`; `docs/ongoing/final-claim-evidence-map.md`; final artifact manifest.
- **Relevant report note(s):** Steps 1, 2, 4, 6, and 11 report notes.
- **Raw evidence:** Step 10 records distinguish configurations but do not transfer ownership.
- **Processed evidence:** RQ3 tables retain comparator labels.
- **Expected table(s):** Claim area; owned artifact; observed evidence; permitted wording.
- **Expected future figure(s):** None; reuse provenance architecture.
- **References needed later:** Citation details for Yacoub source/report.
- **Provenance:** Explicit persistent vocabulary.
- **Limitations/caveats:** Pi/action-side evidence `YACOUB_INHERITED` / `REFERENCE_ONLY`; contracts shared but Yacoub-originated; reconstruction and evaluation do not transfer baseline authorship.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.9 Threats to Validity

- **Purpose:** Assess internal, construct, external, and reproducibility threats against the actual frozen study.
- **Main claim/question:** How might controlled seams, protocol deviation, provider/runtime behavior, sampling, workload differences, and simulation affect conclusions?
- **Frozen source artifacts:** Final freeze methodological limitations; final evidence inventory; experiment/raw/processed manifests.
- **Relevant report note(s):** Steps 6–11 report notes.
- **Raw evidence:** Operational deviations, failures, pending snapshots, and missing telemetry.
- **Processed evidence:** All final summaries and correction.
- **Expected table(s):** Validity category; threat; evidence; mitigation; residual risk.
- **Expected future figure(s):** None.
- **References needed later:** Established validity framework.
- **Provenance:** Obid analysis; component origins retained.
- **Limitations/caveats:** Do not invent speculative threats as observed defects or claim mitigations that were not implemented/tested.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.10 Broader IoT Relevance

- **Purpose:** Discuss carefully which design ideas might transfer conceptually beyond the temperature/fan case.
- **Main claim/question:** Which aspects of contract boundaries, controlled tools, deterministic release policy, and HITL may be relevant to other IoT workflows?
- **Frozen source artifacts:** Final architecture and scope documents; no new empirical source.
- **Relevant report note(s):** Steps 1 and 11 report notes.
- **Raw evidence:** None beyond the bounded study.
- **Processed evidence:** None beyond the bounded study.
- **Expected table(s):** Optional transferable principle; required adaptation; unsupported generalization.
- **Expected future figure(s):** None.
- **References needed later:** Related IoT control contexts and generalization literature.
- **Provenance:** Discussion inference clearly marked; not new evidence.
- **Limitations/caveats:** No device/hardware/model/scalability generality, physical deployment, or production claim can follow from one simulated scenario.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.11 Ethical and Societal Considerations

- **Purpose:** Discuss human oversight, action accountability, transparency, privacy minimization, and automation boundaries.
- **Main claim/question:** What ethical and societal considerations arise when an LLM-mediated workflow can propose IoT actions?
- **Frozen source artifacts:** HITL design; evidence privacy review; AI-tool-use documentation; final evidence inventory.
- **Relevant report note(s):** Steps 2, 9, 10, and 11 report notes.
- **Raw evidence:** No personal reviewer identity or hidden reasoning was collected; pending/actions/timing are non-private controlled records.
- **Processed evidence:** Telemetry availability may support transparency limitations.
- **Expected table(s):** Consideration; implemented control; remaining issue.
- **Expected future figure(s):** None.
- **References needed later:** Ethics of AI-mediated control, human oversight, accountability, and privacy.
- **Provenance:** Project controls/evidence `OBID_CREATED`; ethical framework external.
- **Limitations/caveats:** Do not overstate ethical assurance from a narrow technical prototype; avoid reproducing local username/path, credentials, URLs, or private account data.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### 7.12 Future Work

- **Purpose:** Identify evidence-aligned extensions that were deliberately outside the frozen thesis.
- **Main claim/question:** What should be tested next without implying it was implemented here?
- **Frozen source artifacts:** `docs/ongoing/obid-scope.md`; `docs/decisions.md` D-015; `docs/ongoing/final-implementation-freeze.md` deferred-work section.
- **Relevant report note(s):** Steps 9 and 11 report notes.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** Future extension; motivating limitation; required new evidence; freeze impact.
- **Expected future figure(s):** None; do not diagram an unimplemented branch as current architecture.
- **References needed later:** Literature motivating selected future directions.
- **Provenance:** Future-work proposals, not completed contributions.
- **Limitations/caveats:** Validator-agent/two-agent work is deferred after final freeze; other candidates include broader cases/models/devices, physical hardware, durable memory, larger samples, timeout/replay/idempotency, and richer telemetry.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

## Chapter 8 — Conclusions

### Chapter 8 overview

- **Purpose:** Close the thesis with direct bounded answers, contribution, achievements, omissions, and future work.
- **Main claim/question:** What can the frozen study conclude, and what remains outside its evidence?
- **Frozen source artifacts:** Final Chapters 6–7; `docs/ongoing/final-claim-evidence-map.md`; `final-implementation-freeze.md`.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Trace only through Chapter 6 claims.
- **Processed evidence:** Final RQ tables and correction.
- **Expected table(s):** Optional compact RQ answer/evidence/limit table.
- **Expected future figure(s):** None.
- **References needed later:** None new.
- **Provenance:** Mixed; final contribution must remain Obid-specific.
- **Limitations/caveats:** Introduce no new results, methods, literature, or implementation claims.
- **Status:** `SKELETON_ONLY`.

### 8.1 Direct Answers to the Research Questions

- **Purpose:** Answer RQ1, RQ2, and RQ3 plainly after results and discussion stabilize.
- **Main claim/question:** What one bounded answer follows for each exact locked RQ?
- **Frozen source artifacts:** Final Chapter 6 tables; Chapter 7 interpretations; `docs/ongoing/final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** As traced in Chapter 6.
- **Processed evidence:** RQ1 summary; RQ2 summary with correction; RQ3 reliability and latency.
- **Expected table(s):** RQ; direct answer; key evidence; limitation.
- **Expected future figure(s):** None.
- **References needed later:** None new.
- **Provenance:** RQ answers `OBID_CREATED` evaluation/analysis with inherited comparator labelled.
- **Limitations/caveats:** RQ1 bounded cases only; RQ2 denial 4/5/deviation 1/crossings 0; RQ3 descriptive configuration differences with human wait excluded.
- **Status:** `SKELETON_ONLY`.

### 8.2 Final Contribution

- **Purpose:** State the defensible Obid contribution in the integrated system.
- **Main claim/question:** What new decision/reliability capability and evidence did Obid add?
- **Frozen source artifacts:** `docs/ongoing/collaboration-boundary.md`; final implementation freeze; claim map `ARCH-01`, `COMPAT-01`, and `PROV-01`.
- **Relevant report note(s):** Steps 7–11 report notes.
- **Raw evidence:** Step 10 raw evidence supports evaluation contribution.
- **Processed evidence:** Final Step 10 summaries support result contribution.
- **Expected table(s):** None; refer to Chapter 1 contribution table.
- **Expected future figure(s):** None.
- **References needed later:** None new.
- **Provenance:** Stronger single-agent cognition, runtime validation/policy/HITL, and repeated evaluation `OBID_CREATED`; infrastructure/baselines/contracts excluded from authorship claim.
- **Limitations/caveats:** Do not call inherited workflow-to-action infrastructure, middleware, contracts, baselines, or Pi evidence the Obid contribution.
- **Status:** `SKELETON_ONLY`.

### 8.3 What Was Achieved

- **Purpose:** Summarize implemented and evidenced outcomes that passed the final freeze.
- **Main claim/question:** Which core Tier 1.5 capabilities and bounded RQ observations were established?
- **Frozen source artifacts:** Final freeze package; final claim-evidence map.
- **Relevant report note(s):** Steps 7–11 report notes.
- **Raw evidence:** Locked Step 10 raw package.
- **Processed evidence:** Final Step 10 tables and correction.
- **Expected table(s):** Optional achieved capability; evidence; RQ link.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Obid-created capabilities/results with inherited boundary explicitly acknowledged.
- **Limitations/caveats:** “Achieved” means within the frozen architecture, cases, seams, and simulated action boundary.
- **Status:** `SKELETON_ONLY`.

### 8.4 What Was Not Achieved

- **Purpose:** State the principal non-results and excluded claims.
- **Main claim/question:** Which important capabilities/comparisons/generalizations remain unsupported?
- **Frozen source artifacts:** Final freeze methodological limitations and deferred-work section; final evidence inventory.
- **Relevant report note(s):** Steps 9 and 11 report notes.
- **Raw evidence:** Absence from the frozen experiment, not a failed observation unless explicitly recorded.
- **Processed evidence:** None.
- **Expected table(s):** Not achieved; evidence gap; reporting consequence.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Scope/limitations statement.
- **Limitations/caveats:** Include no physical Obid hardware, multi-agent/validator comparison, model/memory/device comparison, production-safety proof, inferential generalization, direct cost comparison, or durable memory.
- **Status:** `SKELETON_ONLY`.

### 8.5 Future Work

- **Purpose:** End with a short prioritized set of evidence-generating extensions.
- **Main claim/question:** Which next studies directly address the reported limitations?
- **Frozen source artifacts:** `docs/decisions.md` D-015; final freeze deferred-work section; Chapter 7 future-work map.
- **Relevant report note(s):** Step 11 report note.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None unless Chapter 7 table is referenced.
- **Expected future figure(s):** None.
- **References needed later:** None new beyond Chapter 7.
- **Provenance:** Proposed future work only.
- **Limitations/caveats:** Clearly use future tense; validator agent remains deferred and was not part of the frozen thesis.
- **Status:** `SKELETON_ONLY`.

## Appendix A — Report Artifact Index

### Appendix A overview

- **Purpose:** Provide a concise repository-oriented index from report claims to frozen artifacts without reproducing full code or raw datasets.
- **Main claim/question:** Where can a reader locate final implementation, contracts, safety/HITL, evaluation, correction, traceability, and freeze artifacts?
- **Frozen source artifacts:** `docs/ongoing/final-artifact-manifest.json`; `docs/ongoing/final-evidence-inventory.md`; `docs/ongoing/final-claim-evidence-map.md`.
- **Relevant report note(s):** Steps 1–11 report notes, especially Step 11.
- **Raw evidence:** Index only; raw files remain under `evaluation/results/step-10/raw/`.
- **Processed evidence:** Index only; processed files remain under `evaluation/results/step-10/processed/`.
- **Expected table(s):** Repository path; identity/use; hash/record count where relevant; provenance; caveat.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Index organization `OBID_CREATED`; each artifact retains its own persistent label.
- **Limitations/caveats:** Repository-relative paths only; no full source-code reproduction, absolute local paths, credentials, secrets, personal data, transient HITL URLs, or Yacoub screenshots.
- **Status:** `SKELETON_ONLY`.

### A.1 Final Implementation Artifacts

- **Purpose:** Index the final frozen implementation and its integrity metadata.
- **Main claim/question:** Which final files and hashes define the implementation the thesis describes?
- **Frozen source artifacts:** `docs/ongoing/final-artifact-manifest.json`; `docs/ongoing/final-implementation-freeze.md`.
- **Relevant report note(s):** Step 11 report note.
- **Raw evidence:** None directly.
- **Processed evidence:** None directly.
- **Expected table(s):** Artifact identity; repository path; SHA-256; role; provenance.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Manifest `OBID_CREATED`; indexed items retain inherited/shared/created labels.
- **Limitations/caveats:** The manifest indexes 61 frozen artifacts at the substantive head; it is not a substitute for the files and intentionally does not self-reference Step 11 documentation.
- **Status:** `SKELETON_ONLY`.

### A.2 Baseline and Configuration Exports

- **Purpose:** Index the deterministic anchor, actual minimal-agent comparator, Obid v1/v2/v3 lineage, prompts, and configuration manifests.
- **Main claim/question:** Which exports define comparison/context and the final evaluated configuration?
- **Frozen source artifacts:** `cognitive_logic/baselines/yacoub/`; `cognitive_logic/obid/workflows/`; `cognitive_logic/obid/configuration-manifest.md`; final freeze.
- **Relevant report note(s):** Steps 6, 7, 8, 9, and 11 report notes.
- **Raw evidence:** Step 10 records reference final configuration IDs.
- **Processed evidence:** RQ3 processed outputs reference Baseline/Obid identities.
- **Expected table(s):** Configuration ID; artifact/path; hash; role; model; memory; provenance; evaluated/context status.
- **Expected future figure(s):** None.
- **References needed later:** Yacoub source citation.
- **Provenance:** Deterministic/minimal baselines `YACOUB_INHERITED`; Obid workflows `OBID_CREATED`.
- **Limitations/caveats:** Deterministic anchor is not RQ3 comparator; v1/v2 are lineage snapshots, while v3 is final `CONFIG-OBID`; do not copy Yacoub claims.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

### A.3 Prompts, Tools, and Memory

- **Purpose:** Index the Obid cognitive-layer records and executable locations.
- **Main claim/question:** Where are the prompt, tool, ReAct, memory, and structured-envelope specifications frozen?
- **Frozen source artifacts:** `cognitive_logic/obid/prompts/`; `tools/`; `react/`; `memory/`; `structured-output/`; final v3 workflow.
- **Relevant report note(s):** Step 7 report note.
- **Raw evidence:** Step 7 readiness evidence; Step 10 records where relevant.
- **Processed evidence:** RQ1/RQ3 summaries only as result links.
- **Expected table(s):** Artifact; path; embedded executable node; hash; purpose; provenance.
- **Expected future figure(s):** None.
- **References needed later:** None in artifact index.
- **Provenance:** `OBID_CREATED`; inherited threshold/status semantics separately labelled.
- **Limitations/caveats:** Exactly two read-only tools, one process-local memory strategy, no hidden reasoning, and no action-execution tool.
- **Status:** `SKELETON_ONLY`.

### A.4 Shared Contracts

- **Purpose:** Index the adopted sensor/action schemas and no-drift record.
- **Main claim/question:** Which exact shared contract bytes and hashes governed the interface and validation?
- **Frozen source artifacts:** `shared_interfaces/contract-freeze.md`; `shared_interfaces/json-schema/sensor-event.schema.json`; `shared_interfaces/json-schema/agent-action.schema.json`; shared-interface provenance record.
- **Relevant report note(s):** Steps 1, 2, 5, and 11 report notes.
- **Raw evidence:** Step 10 records contain contract-shaped inputs/actions but do not establish authorship.
- **Processed evidence:** None.
- **Expected table(s):** Contract; path; SHA-256; key constraints; provenance.
- **Expected future figure(s):** None.
- **References needed later:** JSON/JSON Schema citations belong in Chapter 2, not necessarily here.
- **Provenance:** Yacoub-originated `SHARED_INTERFACE`; Obid adoption/hash verification `OBID_CREATED`.
- **Limitations/caveats:** No contract drift, extra action, risk field, target, or internal `no_action` addition; shared use is not co-authorship.
- **Status:** `SKELETON_ONLY`.

### A.5 Runtime Safety and Policy

- **Purpose:** Index validator, policy, outcomes, final/relevant workflow snapshots, harness, and readiness evidence.
- **Main claim/question:** Which artifacts establish executable validation and deterministic release policy?
- **Frozen source artifacts:** `safety_layer/validator/`; `safety_layer/policies/`; `safety_layer/outcomes/`; `safety_layer/workflows/runtime-safety-v1.json`; `runtime-safety-v2-hitl.json`; Step 8 harness/evidence.
- **Relevant report note(s):** Steps 8, 9, and 11 report notes.
- **Raw evidence:** Step 8 one-off readiness; Step 10 invalid/HITL records.
- **Processed evidence:** RQ2 summary and traceability.
- **Expected table(s):** Artifact; version; path/hash; final role; evaluation seam.
- **Expected future figure(s):** None.
- **References needed later:** None in artifact index.
- **Provenance:** Runtime safety/policy `OBID_CREATED`; contract `SHARED_INTERFACE`; inherited design cited as reference-only where used.
- **Limitations/caveats:** Validator is contract-specific, policy narrow, Step 8 approval-required was hold only; actual HITL arrives in Step 9.
- **Status:** `SKELETON_ONLY`.

### A.6 Human-in-the-Loop Artifacts

- **Purpose:** Index final and retained HITL workflows, specifications, evidence, and integration.
- **Main claim/question:** Which artifacts distinguish the final embedded Wait/form gate from the original child-Wait failure?
- **Frozen source artifacts:** `safety_layer/hitl/`; `safety_layer/workflows/runtime-safety-v2-hitl.json`; `cognitive_logic/obid/workflows/obid-agent-v3-hitl.json`.
- **Relevant report note(s):** Steps 9 and 11 report notes.
- **Raw evidence:** Step 10 `raw/hitl-pending.jsonl`, run records, and attempt events.
- **Processed evidence:** `processed/hitl-timing.csv`; RQ2 summary plus correction.
- **Expected table(s):** Artifact; role; final/retained status; path/hash; observed use.
- **Expected future figure(s):** None.
- **References needed later:** None in artifact index.
- **Provenance:** Final runtime mechanics/repair/evidence `OBID_CREATED`; original concept `YACOUB_INHERITED` / `REFERENCE_ONLY`.
- **Limitations/caveats:** Keep failure and repair distinct; no transient URLs/tokens or reviewer identity; harness is the controlled policy-input seam.
- **Status:** `SKELETON_ONLY`.

### A.7 Evaluation Protocol

- **Purpose:** Index the pre-observation oracle, protocol, experiment freeze, and runner/extractor/processor.
- **Main claim/question:** Which artifacts fixed cases, order, repetitions, timing, and execution identity before observation?
- **Frozen source artifacts:** `evaluation/cases/obid-evaluation-cases.json`; `evaluation/evaluation-protocol.md`; `evaluation/results/step-10/experiment-freeze.json`; `experiment-freeze.md`; evaluation tooling.
- **Relevant report note(s):** Steps 5, 10, and 11 report notes.
- **Raw evidence:** `raw/planned-order.json`; `raw/run-order.csv`.
- **Processed evidence:** `processed/traceability.csv`.
- **Expected table(s):** Artifact; path/hash; role; pre/post-observation status.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** `OBID_CREATED`; inherited threshold/action semantics within the oracle labelled.
- **Limitations/caveats:** Protocol is frozen; no run replacement or retrospective oracle change; safety cases outside core RQ3 comparison.
- **Status:** `SKELETON_ONLY`.

### A.8 Raw Step 10 Results

- **Purpose:** Index every locked raw artifact with its record/use and integrity hash.
- **Main claim/question:** Where are the immutable primary observations, schedule, events, pending snapshots, deviations, and lock metadata?
- **Frozen source artifacts:** `evaluation/results/step-10/raw/`; `docs/ongoing/final-artifact-manifest.json`.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** `planned-order.json`; `run-order.csv`; `run-records.jsonl`; `attempt-events.jsonl`; `hitl-pending.jsonl`; `operational-deviations.jsonl`; raw manifests.
- **Processed evidence:** None; processed traceability may be cross-linked.
- **Expected table(s):** Raw artifact; record count/use; SHA-256; privacy/interpretation note.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Raw files are immutable and primary; no full data reproduction in appendix; preserve failures; repository-relative paths only.
- **Status:** `SKELETON_ONLY`.

### A.9 Processed Step 10 Results

- **Purpose:** Index every deterministic derived output and its interpretation boundary.
- **Main claim/question:** Which processed files support RQ1, RQ2, RQ3, timing, telemetry, and traceability?
- **Frozen source artifacts:** `evaluation/results/step-10/processed/`; `processed/processed-data-manifest.json`; processing script.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** Raw inputs referenced through traceability.
- **Processed evidence:** `rq1-summary.csv`; `rq2-summary.csv`; `rq3-reliability.csv`; `rq3-latency.csv`; `hitl-timing.csv`; `llm-telemetry.csv`; `traceability.csv`; `summary.md`.
- **Expected table(s):** Processed artifact; rows/use; SHA-256; source raw fields; interpretation caveat.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** RQ2 summary/summary.md preserve historical crossing=1 and require the append-only correction; mean is supplementary; no hidden missing-value replacement.
- **Status:** `SKELETON_ONLY`.

### A.10 Correction and Traceability

- **Purpose:** Make the R03 interpretation and raw-to-summary linkage auditable.
- **Main claim/question:** How can a reader trace every summary row while preserving both historical processing and final safety interpretation?
- **Frozen source artifacts:** `evaluation/results/step-10/corrections/rq2-hitl-denial-r03-interpretation.md`; `evaluation/results/step-10/processed/traceability.csv`.
- **Relevant report note(s):** Steps 10 and 11 report notes.
- **Raw evidence:** R03 run/event/pending/order artifacts.
- **Processed evidence:** Historical RQ2 outputs plus traceability.
- **Expected table(s):** Claim/summary row; raw run ID; top-level execution ID; correction applicability; final interpretation.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** `OBID_CREATED`.
- **Limitations/caveats:** Historical crossing=1 remains immutable but is not the final RQ2 safety interpretation; R03 remains an incorrect assigned denial; child IDs are not extra trials.
- **Status:** `SKELETON_ONLY`.

### A.11 Freeze Manifest

- **Purpose:** Index the final freeze documents and identities that constrain the report.
- **Main claim/question:** Which files define the substantive head, artifact integrity, evidence hierarchy, supported claims, limitations, and post-freeze rule?
- **Frozen source artifacts:** `docs/ongoing/final-artifact-manifest.json`; `final-evidence-inventory.md`; `final-claim-evidence-map.md`; `final-implementation-freeze.md`; `docs/decisions.md` D-015.
- **Relevant report note(s):** Step 11 report note.
- **Raw evidence:** Indexed through the final inventory/manifest.
- **Processed evidence:** Indexed through the final inventory/manifest.
- **Expected table(s):** Freeze identity; value/path; role; status.
- **Expected future figure(s):** None.
- **References needed later:** None.
- **Provenance:** Step 11 freeze documentation `OBID_CREATED`.
- **Limitations/caveats:** Distinguish substantive head `abd36e…` from metadata checkpoint `9efcb4…`; later report-only artifacts do not reopen or rewrite the evidence freeze.
- **Status:** `SKELETON_ONLY`.

## Back matter — References

### Reference list

- **Purpose:** Provide the final bibliography generated from verified citations used in the thesis.
- **Main claim/question:** Which sources actually support each theory, method, platform, related-work, and interpretation claim?
- **Frozen source artifacts:** `thesis/MiunThesisTemplate-master/MiunThesisTemplate-master/literature.bib` is currently an empty/comment-only build placeholder.
- **Relevant report note(s):** None.
- **Raw evidence:** None.
- **Processed evidence:** None.
- **Expected table(s):** None.
- **Expected future figure(s):** None.
- **References needed later:** All `NEEDS_REFERENCE` topics mapped above; authoritative MIUN/n8n/JSON Schema sources; academic ReAct, agent, memory, HITL, IoT, reliability, validity, and ethics sources; proper Yacoub collaborator citation.
- **Provenance:** Bibliographic work belongs to the Obid report; cited works retain normal authorship.
- **Limitations/caveats:** Do not web-search or add references during bootstrap; do not copy Yacoub's bibliography or invent BibTeX.
- **Status:** `SKELETON_ONLY`, `NEEDS_REFERENCE`.

## Coverage and status index

| Area | Current mapped entries | Heading coverage | Required status gate | Map result |
|---|---:|---|---|---|
| Front matter | 7 | Title metadata, DiVA sheet, Abstract, Sammanfattning, Acknowledgements/Foreword, contents, terminology | Metadata gaps explicit | Complete |
| Chapter 1 | 10 | Chapter overview plus all 9 current subsections | Must remain not drafted | `SKELETON_ONLY` |
| Chapter 2 | 14 | Chapter overview plus all 13 current subsections | References deferred | `SKELETON_ONLY`, `NEEDS_REFERENCE` |
| Chapter 3 | 14 | Chapter overview plus all 13 current subsections | Must remain not drafted | `SKELETON_ONLY` |
| Chapter 4 | 13 | Chapter overview plus all 12 current subsections | Every entry must include `DRAFTED_NEEDS_AUDIT` | Complete |
| Chapter 5 | 17 | Chapter overview plus all 16 current subsections | Every entry must include `DRAFTED_NEEDS_AUDIT` | Complete |
| Chapter 6 | 13 | Chapter overview plus all 12 current subsections | Every entry must include `READY_TO_DRAFT` | Complete |
| Chapter 7 | 13 | Chapter overview plus all 12 current subsections | Must remain not drafted | `SKELETON_ONLY` |
| Chapter 8 | 6 | Chapter overview plus all 5 current subsections | Must remain not drafted | `SKELETON_ONLY` |
| Appendix A | 12 | Appendix overview plus all 11 current subsections | Artifact index only | `SKELETON_ONLY` |
| References | 1 | Bibliography placeholder | No sources added in bootstrap | `SKELETON_ONLY`, `NEEDS_REFERENCE` |
| **Total** | **120** | All current front-matter/report/appendix areas mapped | No full prose | Complete |

### Validation checklist for the next report-writing task

- [x] Exact RQ1–RQ3 reproduced without rewriting.
- [x] Evidence hierarchy recorded with the R03 correction above processed interpretation.
- [x] Step 12 start HEAD, substantive content head, Step 11 metadata checkpoint, Yacoub commit, manifest, experiment freeze, raw lock, and freeze gate recorded.
- [x] Final `CONFIG-BASELINE` and `CONFIG-OBID` identities, model/runtime, tools, memory, iteration bound, validation, policy, HITL, and simulated action boundary recorded.
- [x] All current front-matter items and metadata gaps mapped.
- [x] Every current Chapter 1–8 subsection mapped.
- [x] Every current Appendix A subsection mapped.
- [x] Every Chapter 4 overview/subsection is drafted and includes `DRAFTED_NEEDS_AUDIT` while completing the audit/re-audit gate; Chapter 5 has completed its audit/repair/re-audit gate and is locked; every Chapter 6 overview/subsection remains `READY_TO_DRAFT`.
- [x] Chapter 6 maps Step 10 raw and processed sources, R03 correction, negative evidence, telemetry, and automated-latency boundaries.
- [x] All task-specified unsupported-claim warnings listed.
- [x] Important component and evidence provenance warnings listed.
- [x] Yacoub LaTeX/PDF use restricted to structural/visual reference; Yacoub content/results/metadata excluded.
- [x] External references and figures remain future placeholders only.
- [x] No new experiment, image, implementation change, evidence rewrite, or substantive thesis prose is part of this map.

## Recommended next bounded writing task

Complete the targeted Chapter 4 re-audit. After Chapter 4 passes, draft Chapter 6 from Sections 6.1–6.12 using the mapped frozen artifacts. Chapter 5 has completed its audit/repair/re-audit gate and remains locked. References and the final architecture figure should remain separately scoped unless explicitly requested.
