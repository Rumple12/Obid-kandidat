# Obid Thesis Report Outline

**Status:** High-level evidence/topic map only

**Template direction:** MIUN-style eight-chapter structure

**Constraint:** This is not thesis prose.

## 1. Introduction

Likely topics:

- IoT action reliability problem when an LLM can select tools/actions
- motivation for runtime controls and measurable repeated behavior
- aim and RQ1-RQ3
- one-system/two-contribution collaboration model
- Obid scope, limitations, and out-of-scope boundaries
- concise chapter roadmap

Likely evidence/inputs:

- `docs/ongoing/project-overview.md`
- `docs/ongoing/obid-scope.md`
- `docs/ongoing/research-questions.md`
- `docs/ongoing/collaboration-boundary.md`
- `docs/decisions.md`

Ownership caution: describe Yacoub's infrastructure and baselines as inherited context, not Obid implementation.

## 2. Theory and Related Work

Likely topics:

- agentic AI, tool use, and controlled ReAct-style patterns
- LLM non-determinism and structured output
- bounded memory and state-dependent behavior
- runtime validation and deterministic policy enforcement
- Human-in-the-Loop approval
- reliability, consistency, latency, and repeated evaluation concepts
- n8n as the chosen agentic workflow platform
- related IoT agentic systems at a scope appropriate to one scenario

Likely evidence/inputs:

- literature selected later under the approved plan/professor brief
- final implemented prompt/tool/memory/validation/HITL design boundaries
- terms and measurements fixed in Step 5

Boundary: do not turn the chapter into broad multi-agent, production-safety, scalability, or model-benchmarking coverage.

## 3. Methodology

Likely topics:

- bounded numbered development process
- evidence-first and version-controlled method
- collaboration/provenance method
- controlled case design and frozen expected outcomes
- configurations and repetition protocol
- reliability and latency metrics
- handling of failures, missing data, and human wait time
- validity, reproducibility, ethical/safety, and AI-tool-use considerations

Likely evidence/inputs:

- `docs/plans/obid-14-step-process.md`
- `docs/plans/implementation-plan.md`
- Step 5 case set and evaluation protocol
- Step 10 raw-run inventory
- Step 11 evidence freeze manifest

Boundary: methods describe what was actually done; planned methods not executed must be identified as such.

## 4. Choice of Approach / System Design

Likely topics:

- Tier 1.5 narrowing and rejected alternatives
- Yacoub-Obid architecture boundary
- rationale for one scenario, model, main agent, and bounded-memory configuration
- inherited versus upgraded components
- compatibility contracts and endpoint mapping
- controlled ReAct/tool/memory design
- runtime validation, policy, and HITL architecture
- optional validator-agent decision, whether included or rejected

Likely evidence/inputs:

- `docs/ongoing/collaboration-boundary.md`
- `docs/ongoing/yacoub-handoff.md`
- `docs/ongoing/obid-scope.md`
- `docs/decisions.md`
- final architecture/configuration artifacts from Steps 5-9

Ownership caution: distinguish design constraints inherited from Yacoub from design choices made by Obid.

## 5. Implementation

Likely topics:

- verified inherited environment and baseline integration
- main Obid workflow nodes and data path
- system prompt and explicit tools
- bounded ReAct execution controls
- bounded-memory implementation
- structured action generation
- runtime schema/output validator
- deterministic action-policy gate
- actual HITL pause/approve/reject/resume path
- logging and traceability needed for evaluation

Likely evidence/inputs:

- versioned implementation files from Steps 3-9
- workflow exports/screenshots
- runtime configuration records
- endpoint and non-execution traces
- narrow verification logs

Boundary: inherited middleware and baseline code should be summarized only to explain integration and must retain Yacoub provenance.

## 6. Results

Likely topics:

- frozen case/configuration/run counts
- RQ1 accuracy and consistency by case
- malformed, unsupported, boundary, and state-dependent outcomes
- RQ2 allowed/blocked/HITL outcomes and any control failures
- RQ3 reliability and latency comparison
- human-wait versus automated latency where available
- failures, timeouts, missing data, and negative results
- optional validator-agent results only in a clearly supplementary subsection

Likely evidence/inputs:

- Step 10 raw outputs and generated summaries
- Step 11 final evidence inventory
- traceable tables/figures derived from raw evidence

Boundary: report observations without explaining causes at length; do not omit failed runs.

## 7. Discussion

Likely topics:

- interpretation of RQ1-RQ3
- tradeoffs among stronger agent behavior, controls, reliability, and latency
- effect and limits of bounded memory and HITL
- comparison with related work
- internal, construct, and external validity
- single-scenario/model limitations
- inherited-baseline reproducibility limitations
- generalization limits and future work

Likely evidence/inputs:

- frozen Results chapter evidence
- limitation notes accumulated during Steps 3-11
- collaboration and provenance decisions

Boundary: do not convert thesis-scoped results into production-grade AI safety, scalability, hardware, or multi-agent claims.

## 8. Conclusions

Likely topics:

- direct concise answer to each research question
- Obid's separately defensible contribution
- confirmed limits of the evidence
- practical implications for the tested n8n/IoT boundary
- tightly scoped future work

Likely evidence/inputs:

- final RQ answers supported by Chapters 6-7
- evidence/provenance audit
- Step 11 frozen state

Boundary: no new results, methods, implementation claims, or literature arguments.

## Front matter, references, and appendix mapping

Although outside the eight numbered chapters, Step 14 should assemble:

- title/front matter, abstract, and Swedish summary as required
- terminology/acronyms if needed
- complete references
- appendices for contracts, configuration identifiers, case definitions, detailed result tables, and reproducibility information
- AI-tool-use disclosure required by the course/template

Only artifacts needed to support auditability should enter the appendix; inherited Yacoub artifacts keep explicit source/commit labels.
