# Safety Layer Area

## Purpose and ownership

This active area is reserved for Obid-created runtime reliability controls. Yacoub's parser, action-policy, and HITL documents remain inherited specification/reference material under `reference/`; they do not prove runtime enforcement.

## Current population

- Step 8 now contains the Obid-created reusable runtime parser/schema validator, separate deterministic policy, stable outcome contract, one-off fault-injection harness, and enforcement-readiness evidence.
- The implementation uses the unchanged adopted Yacoub action schema as its authority. The portable workflows are sanitized and inactive; the temporary harness was disabled after verification.
- [`configuration-manifest.md`](configuration-manifest.md) is the discovery point for exact workflow IDs, hashes, node versions, provenance, and boundaries.
- Step 9 remains responsible for actual HITL approve/deny behavior and its runtime evidence.

## Boundary

Step 8 stops at `APPROVAL_REQUIRED` / hold. No approval UI, human decision, release-after-approval, second agent/model, broad risk engine, or repeated Step 10 evaluation belongs to the current artifacts. Yacoub safety documents remain inherited specification/reference material and were not copied here as Obid-authored work.
