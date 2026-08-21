# Shared Interfaces Area

## Purpose and ownership

The sensor-event and agent-action contracts originate in Yacoub's frozen repository and retain Yacoub authorship. They are collaboration `SHARED_INTERFACE` artifacts whose exact provenance and compatible semantics are documented under `docs/collaboration/`.

## Active Step 5 artifacts

- `json-schema/sensor-event.schema.json`
- `json-schema/agent-action.schema.json`
- `contract-freeze.md`

The schemas are exact active copies from frozen commit `278318340bfa4e4650a97a2baba73f63bd868ed9`; matching SHA-256 evidence is recorded in `contract-freeze.md`. They remain Yacoub-authored `SHARED_INTERFACE` artifacts.

## Boundary

Step 5 adopted but did not redesign or implement runtime enforcement of either contract. No contract may silently drift, widen its fields/actions/targets, or be represented as Obid-authored. Runtime validation remains later Obid work.
