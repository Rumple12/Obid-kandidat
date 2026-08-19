# Integration Area

## Purpose and ownership

This active area is reserved for the Yacoub-compatible integration test boundary, configuration/endpoint mapping, and new Obid verification evidence. The collaborator middleware remains Yacoub-owned.

## Planned population

Step 4 verifies webhook forwarding, middleware reachability, `/status`, `/sensor-event`, `/fan/on`, `/fan/off`, and the locked action mapping.

If the actual Yacoub middleware is unavailable, any future explicitly authorized local substitute must be a strict `TEST_DOUBLE` that faithfully emulates the boundary and is never represented as Yacoub middleware.

## Step 2 boundary

No adapter, webhook, server, client, middleware copy, test double, or runtime integration implementation is created here in Step 2. A competing middleware architecture does not belong in this area.
