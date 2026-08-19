# Local n8n Docker Baseline

This folder contains the Step 3 local self-hosted n8n baseline for the
new-yacoub thesis repository.

The baseline is intentionally small:

- Docker Compose
- one self-hosted n8n service
- n8n's default local SQLite-based storage persisted in a Docker volume
- no PostgreSQL
- no Prometheus or Grafana
- no MCP
- no middleware or workflows yet

## Prerequisites

- Docker Desktop or Docker Engine with Docker Compose support

The baseline was runtime verified locally on Windows with Docker Desktop on
2026-04-25. n8n opened at `http://localhost:5678` and displayed the owner
account setup screen.

Verification evidence is stored in `infrastructure/docker/evidence/`.

## First Run

From this folder:

```powershell
Copy-Item .env.example .env
docker compose up -d
docker compose logs -f n8n
```

Then open:

```text
http://localhost:5678
```

n8n should show its first-user setup page. Complete the local owner setup in
the browser.

## Shutdown

Stop the container while keeping local n8n data:

```powershell
docker compose down
```

Stop and remove the local n8n data volume:

```powershell
docker compose down -v
```

Only use `docker compose down -v` when you intentionally want to reset local
n8n state.

## Basic Checks

Useful local checks:

```powershell
docker compose ps
docker compose logs n8n
```

Expected result:

- the `n8n` service is running
- port `5678` is available on the host
- the browser can reach `http://localhost:5678`

## Raspberry Pi Notes

Raspberry Pi deployment is a later Tier 1.5 validation step, not part of this
baseline.

Future Pi validation should check:

- whether the same pinned image tag is available for the Pi architecture
- available RAM and CPU headroom during startup and workflow execution
- persistent storage path and backup approach
- thermal collection method
- whether the same Compose file can be reused unchanged or needs a Pi-specific
  override

Do not add Pi deployment complexity until the local PC baseline, middleware,
contract, workflow, safety, and evaluation path are stable.
