"""HTTP routes for the minimal Step 4 middleware skeleton."""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from typing import Any
from urllib.parse import urlparse

from middleware.gpio.mock_sensor import (
    fan_off,
    fan_on,
    get_state,
    normalize_sensor_event,
)
from middleware.webhooks.n8n_sender import send_sensor_event


class MiddlewareRequestHandler(BaseHTTPRequestHandler):
    server_version = "NewYacoubMiddleware/0.1"

    def do_GET(self) -> None:
        path = urlparse(self.path).path

        if path == "/status":
            self._send_json(
                HTTPStatus.OK,
                {
                    "status": "ok",
                    "message": "middleware running",
                    "state": get_state(),
                },
            )
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found", "path": path})

    def do_POST(self) -> None:
        path = urlparse(self.path).path

        if path == "/sensor-event":
            self._handle_sensor_event()
            return

        if path == "/fan/on":
            self._send_json(HTTPStatus.OK, fan_on(reason="manual_api_call"))
            return

        if path == "/fan/off":
            self._send_json(HTTPStatus.OK, fan_off(reason="manual_api_call"))
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found", "path": path})

    def log_message(self, format: str, *args: Any) -> None:
        print(f"{self.address_string()} - {format % args}")

    def _handle_sensor_event(self) -> None:
        payload = self._read_json_body()
        if payload is None:
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {
                    "error": "invalid_json",
                    "message": "Request body must be valid JSON.",
                },
            )
            return

        event = normalize_sensor_event(payload)
        if "error" in event:
            self._send_json(HTTPStatus.BAD_REQUEST, event)
            return

        webhook_result = send_sensor_event(event)
        self._send_json(
            HTTPStatus.ACCEPTED,
            {
                "status": "accepted",
                "message": "sensor event received by middleware",
                "event": event,
                "n8n": webhook_result,
            },
        )

    def _read_json_body(self) -> dict[str, Any] | None:
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length) if length else b"{}"

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            return None

        return payload if isinstance(payload, dict) else None

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status.value)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
