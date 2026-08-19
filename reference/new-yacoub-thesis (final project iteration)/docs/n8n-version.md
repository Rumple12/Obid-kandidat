# n8n version pin

This file records the exact n8n version and documentation assumptions used in
the **new-yacoub** thesis.

The purpose is to prevent source-of-truth drift during implementation and
report writing.

---

## Status

Version pin status: **runtime verified locally on Windows with Docker Desktop**

Docker Hub metadata verified that the selected image tag exists on 2026-04-24.

Runtime verification succeeded locally on Windows with Docker Desktop on
2026-04-25. n8n opened at `http://localhost:5678` and displayed the owner
account setup screen.

---

## Chosen n8n version

n8n version: `1.123.37`

Docker image tag: `n8nio/n8n:1.123.37`

Reason:

This is an explicit pinned image tag available from the official `n8nio/n8n`
Docker Hub repository at the time the local baseline was created. The thesis
does not compare n8n versions, so the version is pinned to keep setup,
screenshots, logs, and report text aligned.

---

## Date pinned

Date pinned: `2026-04-24`

---

## Verification notes

- Tag existence verified through Docker Hub tag metadata on 2026-04-24.
- Initial runtime verification attempt on 2026-04-25 was blocked because the
  `docker` command was not available in PowerShell.
- Docker Desktop was then installed locally on Windows.
- Runtime verification succeeded on 2026-04-25 with `docker compose up -d`.
- Browser verification succeeded at `http://localhost:5678`.
- Screenshot proof: `infrastructure/docker/evidence/n8n-localhost-5678-success-2026-04-25.png`.
- Evidence log: `infrastructure/docker/evidence/n8n-runtime-proof-2026-04-25.txt`.

---

## Thesis usage context

This thesis uses n8n as:

- the self-hosted workflow engine
- the runtime for the deterministic baseline path
- the runtime for the minimal agent-enhanced path
- the integration point between middleware and workflow logic

The thesis does **not** treat n8n version comparison as a research goal.

---

## Docs/pages relied on

The following documentation categories are relevant to this thesis:

- n8n Docker/self-hosting documentation for local container setup
- n8n workflow fundamentals for later workflow creation
- n8n webhook behavior for the middleware-to-n8n event path

Phase 0 does not rely on MCP documentation and does not modify n8n core.

Concrete documentation URLs should be added here when implementation moves into
workflow creation and the exact pages used are known.

---

## Locked assumptions

The current assumptions are:

1. n8n will be used in a self-hosted local setup first.
2. Development starts on PC before Raspberry Pi deployment.
3. n8n is part of the workflow orchestration layer, not the thesis subject by itself.
4. The thesis evaluates system behavior and integration, not broad n8n version benchmarking.
5. n8n core will not be modified unless explicitly required.
6. The first local baseline uses n8n's default local SQLite-backed storage and a Docker volume.
7. PostgreSQL is deferred unless the baseline proves it is necessary.

---

## Update rule

If any of the following changes:

- n8n version
- Docker image tag
- relevant docs relied upon
- runtime assumptions tied to n8n behavior

then this file must be updated together with:

- `docs/decisions.md`
- `docs/plans/implementation-plan.md`
- `docs/ongoing/integration-contract.md` if interface behavior changes

---

## Finalization checklist

Before implementation moves beyond the local baseline, confirm:

- exact n8n version
- exact Docker image tag
- pin date
- successful `docker compose up -d` on a Docker-enabled machine
- screenshot or terminal log showing n8n running locally
- any version-specific limitations or notes
