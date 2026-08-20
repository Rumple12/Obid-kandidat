# Obid Step 3 Local n8n Runtime

This directory defines the minimal local n8n environment created for Obid Step 3.

## Provenance

- The compatible Yacoub runtime pattern and version choice are `YACOUB_INHERITED` / `REFERENCE_ONLY` from `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9`.
- This Compose configuration, local container, manifest, and verification evidence are `OBID_CREATED`.
- Reusing the compatible image/version and minimal storage assumptions does not transfer authorship of Yacoub's runtime design.

## Scope

The environment contains one n8n service using pinned image `n8nio/n8n:1.123.37`, default SQLite-backed storage, and named volume `obid-n8n-data` mounted at `/home/node/.n8n`.

It intentionally has no PostgreSQL, Redis, Prometheus, Grafana, MCP, middleware, workflow, reverse proxy, production TLS, or Raspberry Pi configuration.

## Prerequisites

- Docker Desktop or Docker Engine
- Docker Compose
- free local host port `5678`, or a documented alternate `N8N_HOST_PORT`

## First run

From `infrastructure/docker/`:

```powershell
Copy-Item .env.example .env
```

Replace the example `N8N_ENCRYPTION_KEY` in the ignored `.env` with a long random local value. Do not print, commit, or share it. Keep the same value across restarts.

Validate and start:

```powershell
docker compose config --quiet
docker compose pull
docker compose up -d
docker compose ps
```

Open `http://localhost:5678` when the default host port is used. If this is a fresh n8n data volume, the first-user setup screen is expected. Keep owner credentials out of Git, evidence, chat, and screenshots.

## Normal stop and restart

Stop while preserving the named data volume:

```powershell
docker compose down
```

Restart with preserved state:

```powershell
docker compose up -d
```

Do **not** run `docker compose down -v` during normal work. It removes `obid-n8n-data` and destroys local n8n state.

## Verification commands

```powershell
docker compose config --quiet
docker compose ps
docker compose logs --tail 100 n8n
docker exec obid-n8n n8n --version
docker volume inspect obid-n8n-data
```

Inspect only the required safe container metadata with narrow formats:

```powershell
docker inspect --format '{{.Config.Image}}' obid-n8n
docker inspect --format '{{json (index .NetworkSettings.Ports "5678/tcp")}}' obid-n8n
docker inspect --format '{{range .Mounts}}{{printf "%s | %s | %s | rw=%t\n" .Type .Source .Destination .RW}}{{end}}' obid-n8n
```

Do not store generic `docker inspect obid-n8n` output as evidence because the complete container JSON may contain environment secrets such as `N8N_ENCRYPTION_KEY`.

The Step 3 manifest and evidence note record the observed environment and any pending manual UI checks.

## Step boundary

Step 3 verifies only runtime/version/node/network prerequisites. It does not import or create workflows, configure Gemini credentials, run middleware, call middleware endpoints, adopt schemas, implement agent/safety/HITL behavior, or execute evaluation cases. Those belong to later numbered steps.
