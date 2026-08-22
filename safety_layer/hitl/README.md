# Step 9 Human-in-the-Loop

This directory contains the `OBID_CREATED` runtime Human-in-the-Loop (HITL)
mechanism and its bounded readiness evidence. It turns a schema-valid,
policy-held action into an actual n8n wait, a manual `approve` or `deny`
decision, and a deterministic release or no-release outcome.

The final pinned-runtime shape is:

```text
runtime safety v2
  -> approval_required
  -> caller-embedded Wait 1.1 form
  -> manual human decision
  -> approve: release stored unchanged action to caller routing
  -> deny: release null and stop
```

The first implementation put the Wait inside a synchronous subworkflow. n8n
`1.123.37` persisted and resumed that child correctly but returned the
pre-wait input to the parent. That attempt failed closed and is retained in
the evidence. The compatibility repair embeds the same gate nodes directly in
the harness and CONFIG-OBID v3, avoiding post-Wait subworkflow propagation.

Key artifacts:

- [`runtime-hitl-v1.md`](runtime-hitl-v1.md): gate rules and compatibility repair;
- [`hitl-outcome-v1.md`](hitl-outcome-v1.md): stable internal outcomes;
- [`configuration-manifest.md`](configuration-manifest.md): exact versions,
  paths, hashes, and provenance;
- [`evidence/step-09-hitl-verification.md`](evidence/step-09-hitl-verification.md):
  actual pending, approval, denial, regression, and retained-failure evidence;
- [`workflows/step-09-hitl-harness.json`](workflows/step-09-hitl-harness.json):
  inactive, sanitized readiness harness;
- [`workflows/runtime-hitl-v1.json`](workflows/runtime-hitl-v1.json): retained
  standalone subworkflow form used by the original fail-closed attempt.

The form displays the stored held action but submits only a decision. No
resume URL, token, reviewer identity, credential, cookie, or account detail is
stored here. These are Step 9 readiness artifacts, not Step 10 repetitions or
evaluation results. No validator agent exists.
