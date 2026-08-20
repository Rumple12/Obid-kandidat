# Obid Step 3 Runtime Manifest

**Snapshot date:** 2026-08-20

**Provenance:** `OBID_CREATED`

**Compatibility reference:** `YACOUB_INHERITED` / `REFERENCE_ONLY` runtime configuration from `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9`, especially `infrastructure/docker/docker-compose.yml`, `.env.example`, and `README.md`.

## Observed environment

| Item | Observed value |
| --- | --- |
| Host | Microsoft Windows 11 Home, version `10.0.26200`, build `26200`, 64-bit |
| Docker context | `desktop-linux` |
| Docker CLI | `29.5.2`, build `79eb04c` |
| Docker Engine | `29.5.2` |
| Docker Compose | `v5.1.3` |
| Requested image | `n8nio/n8n:1.123.37` |
| Image ID | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Repository digest | `n8nio/n8n@sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Runtime-reported n8n | `1.123.37` |
| Container | `obid-n8n` |
| Compose project | `obid-step3` |
| Port mapping | host `5678` -> container `5678/tcp` on IPv4 and IPv6 |
| Data store | n8n default local SQLite storage |
| Named volume | `obid-n8n-data` |
| Volume mount | `obid-n8n-data` -> `/home/node/.n8n`, read/write |
| Timezone | `GENERIC_TIMEZONE=Europe/Stockholm`; `TZ=Europe/Stockholm` |
| Diagnostics | disabled |
| Version notifications | disabled |

The running image contains `n8n-nodes-base` version `1.121.25` and `@n8n/n8n-nodes-langchain` version `1.122.27`. Package inspection verified the node identities required by the frozen deterministic and minimal-agent exports. Exact evidence is in `evidence/step-03-runtime-verification.md`.

## Compatibility choices

- The exact frozen Yacoub n8n version is used; there is no version or port deviation.
- The runtime keeps the same minimal one-service, SQLite, named-volume, local-host approach. PostgreSQL, Redis, monitoring, MCP, middleware, and reverse-proxy services are absent.
- Obid-specific project, container, and volume names preserve ownership separation and do not change workflow assumptions.
- The Obid Compose file requires a locally supplied encryption key instead of permitting a committed/default placeholder at runtime. The real key is held only in the ignored `.env` file and is not recorded here.
- The Compose file exposes `TZ` as a separate safe setting; the observed `GENERIC_TIMEZONE` and `TZ` values both match the frozen Stockholm setting.
- `host.docker.internal` resolves from the running container. Endpoint reachability and shared-interface behavior remain Step 4 work.

## Application-state persistence

Owner/application initialization persistence is **VERIFIED**. After the human reported completing the private local owner setup, a bounded verification on 2026-08-20 used `docker compose down` without `-v`, confirmed that `obid-n8n-data` still existed, and restarted the service with `docker compose up -d`. The recreated container remounted the volume at `/home/node/.n8n`, reported n8n `1.123.37`, and returned HTTP `200`.

A privacy-safe browser check after restart found that both `/` and an explicit `/setup` request resolved to `/signin`: the owner-setup prompt was absent and the sign-in prompt was present. This verifies that the persisted instance no longer behaved as a fresh uninitialized instance. No owner identity, credential, or secret was requested, inspected, or recorded.
