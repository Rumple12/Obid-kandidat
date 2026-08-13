"""Configurable n8n webhook sender placeholder for later workflow steps."""

from __future__ import annotations

import json
import os
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen


def send_sensor_event(event: dict[str, Any]) -> dict[str, Any]:
    webhook_url = os.getenv("N8N_WEBHOOK_URL", "").strip()

    if not webhook_url:
        return {
            "status": "skipped",
            "reason": "N8N_WEBHOOK_URL is not configured; n8n workflow wiring is pending Step 6.",
        }

    body = json.dumps(event).encode("utf-8")
    request = Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=5) as response:
            response_body = response.read().decode("utf-8", errors="replace")
            return {
                "status": "sent",
                "status_code": response.status,
                "response": response_body,
            }
    except URLError as exc:
        return {
            "status": "error",
            "reason": str(exc),
        }
