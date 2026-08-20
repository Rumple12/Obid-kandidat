# Step 3 Runtime Verification Evidence

**Execution windows:** 2026-08-20, approximately 13:49-13:56 CEST for initial runtime verification and 14:18-14:20 CEST for the owner-state persistence continuation (`UTC+02:00`)

**Evidence provenance:** `OBID_CREATED`

**Frozen comparison source:** `YACOUB_INHERITED` / `REFERENCE_ONLY`, `Rumple12/new-yacoub-thesis` commit `278318340bfa4e4650a97a2baba73f63bd868ed9`

## Verdict summary

| Check | Status | Observation |
| --- | --- | --- |
| Compose configuration | `VERIFIED` | `docker compose config --quiet` exited `0`. |
| Startup | `VERIFIED` | The one-service Compose project started `obid-n8n`; logs reported version `1.123.37` and `Editor is now accessible via: http://localhost:5678`. |
| Exact n8n version | `VERIFIED` | Requested tag, image metadata, startup log, and `n8n --version` agree on `1.123.37`. |
| Container state | `VERIFIED` | `obid-n8n` was `running` after initial startup and after the persistence restart. |
| Host HTTP | `VERIFIED` | `GET http://localhost:5678/` returned HTTP `200` with n8n HTML. No middleware endpoint was called. |
| Browser/UI | `VERIFIED` | The initial pre-owner restart returned to the setup screen; after private owner setup and the second restart, both `/` and `/setup` resolved to `/signin`. No credentials were created by or captured in the verification. |
| Named-volume persistence | `VERIFIED` | `obid-n8n-data` remained after `docker compose down`, remounted at `/home/node/.n8n`, and retained the initialized SQLite file after `docker compose up -d`. |
| Application/owner-state persistence | `VERIFIED` | After private manual owner setup, a non-destructive restart retained initialization: both `/` and `/setup` resolved to `/signin`, and the owner-setup prompt was absent. |
| Required node capability | `VERIFIED` | All node identities required by the frozen workflow exports plus the Google Gemini Chat Model node were present in installed runtime packages. |
| Docker-to-host name resolution | `VERIFIED` | `host.docker.internal` resolved inside `obid-n8n` to IPv4 `192.168.65.254`. No endpoint request was made. |
| Frozen-version compatibility | `VERIFIED` | Actual Obid runtime version exactly matches Yacoub's pinned `1.123.37`; no version substitution occurred. |

## Host and runtime observations

Observed at `2026-08-20T13:52:30+02:00` unless otherwise noted:

| Item | Observation |
| --- | --- |
| Host OS | Microsoft Windows 11 Home `10.0.26200`, build `26200`, 64-bit |
| Docker CLI | `Docker version 29.5.2, build 79eb04c` |
| Docker Engine | `29.5.2`, Linux containers through context `desktop-linux` |
| Docker Compose | `Docker Compose version v5.1.3` |
| Requested image | `n8nio/n8n:1.123.37` |
| Image ID | `sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Repository digest | `n8nio/n8n@sha256:913c83834b7130d701a121aab50c16dedd1739ab9317caa19d7ba2686d1de885` |
| Image platform | Linux `amd64` |
| Runtime command | `docker compose exec -T n8n n8n --version` |
| Runtime output | `1.123.37` |
| Container and port | `obid-n8n`; `0.0.0.0:5678->5678/tcp` and `[::]:5678->5678/tcp` |
| Storage | `obid-n8n-data` mounted read/write at `/home/node/.n8n`; default SQLite |
| Safe runtime settings | `N8N_HOST=localhost`, `N8N_PORT=5678`, `N8N_PROTOCOL=http`, `N8N_SECURE_COOKIE=false`, Stockholm timezones, diagnostics and version notifications disabled |

No encryption key or other secret was printed into this evidence. The real local `.env` is ignored.

## Frozen-source comparison

The exact frozen files were inspected with `git show` at the stated commit rather than from the dirty/pruned upstream working tree:

- `infrastructure/docker/docker-compose.yml`
- `infrastructure/docker/.env.example`
- `infrastructure/docker/README.md`
- `cognitive_logic/workflows/deterministic-baseline.json`
- `cognitive_logic/workflows/agent-minimal.json`

The frozen runtime uses one n8n service, image `n8nio/n8n:1.123.37`, internal/default host port `5678`, SQLite through a named volume, Stockholm timezone, disabled diagnostics and version notifications, and no additional database or monitoring service. The Obid runtime preserves these relevant assumptions while using Obid-specific names.

## Startup and HTTP/UI evidence

1. Preflight found Docker CLI and Compose installed, host port `5678` free, no existing Obid container/volume, and one unrelated stopped Yacoub container. The unrelated container was not changed.
2. The first daemon query failed because Docker Desktop was not running. Docker Desktop was started through its installed application; Docker Engine then answered normally. This recoverable preflight failure is retained here and did not require a configuration deviation.
3. A real ignored `.env` was created from `.env.example`; a random local encryption key was generated without printing it.
4. `docker compose config --quiet` exited `0`; `docker compose pull` and `docker compose up -d` completed successfully.
5. Startup logs completed migrations, reported `Version: 1.123.37`, and announced the editor at `http://localhost:5678`.
6. Host HTTP returned `200` and content type `text/html; charset=utf-8`.
7. Browser inspection showed the fresh "Set up owner account" form. After the non-destructive down/up cycle, the UI again loaded successfully at `/setup`.

The browser observation proves UI availability, not owner-account completion. No screenshot was fabricated or stored.

## Persistence evidence

Before restart, the named mount was:

```text
obid-n8n-data -> /home/node/.n8n (volume, read/write)
database.sqlite: 659456 bytes; modified 2026-08-20T11:50:14.364Z
```

The persistence sequence was:

1. `docker compose down` exited `0`; no `-v` option was used.
2. `docker volume inspect obid-n8n-data` succeeded while the service was down.
3. `docker compose up -d` exited `0`.
4. The recreated container mounted the same named volume at `/home/node/.n8n`.
5. The SQLite file still had size `659456` bytes and modification time `2026-08-20T11:50:14.364Z`.
6. Runtime version remained `1.123.37` and host HTTP again returned `200`.

The initial sequence verified volume and initialized runtime-file persistence while owner setup was still pending.

### Owner/application-state continuation

After the human reported completing local owner setup without supplying any identity or credential information, the following bounded continuation was observed on 2026-08-20:

1. At `14:18:36+02:00`, `obid-n8n` was running, HTTP returned `200`, and `obid-n8n-data` was mounted read/write at `/home/node/.n8n`.
2. `docker compose down` began at `14:19:13+02:00` and exited `0`. The `-v` option was not used.
3. `docker volume inspect obid-n8n-data` succeeded while the container was down.
4. `docker compose up -d` began at `14:19:15+02:00` and exited `0`.
5. The recreated container mounted `obid-n8n-data` read/write at `/home/node/.n8n` and reached HTTP `200` by `14:19:28+02:00`.
6. The restarted runtime reported `1.123.37`; logs reported readiness on port `5678` and editor availability.
7. A privacy-safe browser probe returned `/signin` for both `/` and an explicit `/setup` request. The probe recorded only route and prompt-presence booleans: the owner-setup prompt was absent and the sign-in prompt was present.

Final result: named-volume, initialized runtime-file, and owner/application-state persistence are all `VERIFIED`. No account identity, form value, credential, cookie, or secret was inspected or recorded.

## Required node-capability matrix

Frozen workflow node types were read from the two workflow JSON exports. Availability was then checked without importing either workflow by reading the installed package manifests and instantiating the corresponding node descriptions inside the running container.

| Required capability | Runtime package/node identity | Status | Verification method |
| --- | --- | --- | --- |
| Sticky Note | `n8n-nodes-base.stickyNote` | `AVAILABLE` | Installed `n8n-nodes-base` manifest and node description (`Sticky Note`) |
| Webhook | `n8n-nodes-base.webhook` | `AVAILABLE` | Installed manifest and node description (`Webhook`) |
| If | `n8n-nodes-base.if` | `AVAILABLE` | Installed manifest and node description (`If`) |
| Set | `n8n-nodes-base.set` | `AVAILABLE` | Installed manifest and node description (`Set`) |
| HTTP Request | `n8n-nodes-base.httpRequest` | `AVAILABLE` | Installed manifest and node description (`HTTP Request`) |
| Code | `n8n-nodes-base.code` | `AVAILABLE` | Installed manifest and node description (`Code`) |
| Basic LLM Chain | `@n8n/n8n-nodes-langchain.chainLlm` | `AVAILABLE` | Installed LangChain manifest and node description (`Basic LLM Chain`) |
| Google Gemini Chat Model | `@n8n/n8n-nodes-langchain.lmChatGoogleGemini` | `AVAILABLE` | Installed LangChain manifest and node description (`Google Gemini Chat Model`) |

Observed package versions were `n8n-nodes-base` `1.121.25` and `@n8n/n8n-nodes-langchain` `1.122.27`. No workflow was imported, no Gemini credential was configured, and no exact Gemini model or generation setting was selected. Those baseline details remain Step 6 work.

## Network prerequisite

A Node.js DNS lookup executed inside `obid-n8n` returned:

```text
host.docker.internal -> 192.168.65.254 (IPv4)
```

This verifies name resolution only. `/status`, `/sensor-event`, `/fan/on`, and `/fan/off` were not called, and middleware reachability/semantics were not tested.

## Deviations, warnings, and pending work

- **Version/port deviation:** none. The requested and actual n8n version is `1.123.37`; host and container ports are both `5678`.
- **Ownership separation:** Compose project, container, and volume names are Obid-specific by design.
- **Secret handling difference:** Obid requires an explicit ignored local encryption key instead of allowing a runtime placeholder. This does not change workflow compatibility.
- **Startup warnings:** n8n emitted future-facing deprecation notices for SQLite pool size, task runners, Code-node environment access, and Git bare-repository behavior. They did not prevent startup. No speculative configuration expansion was made in Step 3.
- **Resolved manual checkpoint:** the human reported local owner setup succeeded without sharing credentials. The subsequent non-destructive restart and privacy-safe `/signin` result verified persisted initialization. No owner data was captured.

## Scope confirmation

This run did not start or call Yacoub middleware, import/create a workflow, adopt/copy a schema, configure Gemini, create an evaluation artifact, or execute a Step 4 integration test. The running Obid n8n environment is only a Step 3 runtime compatibility prerequisite.
