# Step 03 - Local n8n Baseline

## What was built

- A local self-hosted n8n runtime baseline was created under `infrastructure/docker/`.
- The baseline uses Docker Compose with the pinned image `n8nio/n8n:1.123.37`.
- n8n uses its default local SQLite-backed storage persisted in a Docker volume.
- The baseline intentionally excludes PostgreSQL, Prometheus/Grafana, MCP, middleware, workflows, and Raspberry Pi deployment.

## Why it matters for the thesis

This step proves the first Yacoub runtime layer can be started locally before adding middleware, contracts, workflows, safety logic, and hardware complexity. It supports the PC-first development decision and creates a reproducible workflow-engine baseline for later measurement.

## Evidence produced

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- `infrastructure/docker/README.md`
- `docs/n8n-version.md`
- `docs/decisions.md` decision D-011
- `infrastructure/docker/evidence/n8n-runtime-proof-2026-04-25.txt`
- `infrastructure/docker/evidence/n8n-localhost-5678-success-2026-04-25.png`

## Report chapters it feeds

- Chapter 4 - Choice of approach: local self-hosted n8n, PC-first development, simple Docker baseline.
- Chapter 5 - Implementation: infrastructure setup and runtime reproducibility.
- Chapter 6 - Results: later runtime evidence can reference the baseline, but no performance result is produced yet.

## Limitations or assumptions

- The runtime was verified locally on Windows with Docker Desktop on 2026-04-25.
- The proof shows n8n reaches the owner setup screen, not that workflows or middleware integration exist.
- No latency, RAM, CPU, or thermal measurement has been produced by this step.
- Raspberry Pi validation remains a later Tier 1.5 step and is not part of this baseline.

## Screenshots/logs still needed

- The existing screenshot proves the local n8n owner setup screen.
- Later steps still need workflow screenshots, middleware request/response logs, Docker/resource logs, and measurement CSVs.
