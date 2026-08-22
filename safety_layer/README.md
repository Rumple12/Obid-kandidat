# Safety Layer Area

## Purpose and ownership

This active area is reserved for Obid-created runtime reliability controls. Yacoub's parser, action-policy, and HITL documents remain inherited specification/reference material under `reference/`; they do not prove runtime enforcement.

## Current population

- Step 8 now contains the Obid-created reusable runtime parser/schema validator, separate deterministic policy, stable outcome contract, one-off fault-injection harness, and enforcement-readiness evidence.
- The implementation uses the unchanged adopted Yacoub action schema as its authority. The portable workflows are sanitized and inactive; the temporary harness was disabled after verification.
- [`configuration-manifest.md`](configuration-manifest.md) is the discovery point for exact workflow IDs, hashes, node versions, provenance, and boundaries.
- Step 9 adds the versioned safety-v2 policy-context handling and actual native n8n Wait/form approval and denial path under [`hitl/`](hitl/). Its final portable workflows are inactive and sanitized; the original fail-closed subworkflow propagation attempt remains visible in the evidence.

## Boundary

Step 9 implements only the exact controlled `POLICY-HITL-REQUIRED` case. It adds no broad risk engine, validator/second agent, second model, contract field, or Step 10 repetition. Yacoub safety documents remain inherited specification/reference material and were not copied here as Obid-authored work.
