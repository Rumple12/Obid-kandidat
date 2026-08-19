"""Mock sensor and actuator state for PC-first middleware development."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


_state: dict[str, Any] = {
    "fan": "off",
    "last_sensor_event": None,
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def mock_temperature_event(value: float = 31.4) -> dict[str, Any]:
    return {
        "sensor_id": "temp_sensor_1",
        "timestamp": utc_now(),
        "type": "temperature",
        "value": value,
        "unit": "C",
    }


def normalize_sensor_event(payload: dict[str, Any]) -> dict[str, Any]:
    event = mock_temperature_event() if not payload else dict(payload)
    required_fields = ("sensor_id", "timestamp", "type", "value", "unit")
    missing = [field for field in required_fields if field not in event]

    if missing:
        return {
            "error": "missing_required_field",
            "missing": missing,
            "message": "Step 4 uses a minimal inline check; JSON schemas come in Step 5.",
        }

    if event["type"] != "temperature":
        return {
            "error": "unsupported_sensor_type",
            "message": "Step 4 middleware only accepts temperature events.",
        }

    try:
        event["value"] = float(event["value"])
    except (TypeError, ValueError):
        return {
            "error": "invalid_value",
            "message": "Temperature value must be numeric.",
        }

    _state["last_sensor_event"] = event
    return event


def fan_on(reason: str) -> dict[str, Any]:
    _state["fan"] = "on"
    return {
        "status": "ok",
        "action": "fan_on",
        "fan": _state["fan"],
        "simulated": True,
        "reason": reason,
    }


def fan_off(reason: str) -> dict[str, Any]:
    _state["fan"] = "off"
    return {
        "status": "ok",
        "action": "fan_off",
        "fan": _state["fan"],
        "simulated": True,
        "reason": reason,
    }


def get_state() -> dict[str, Any]:
    return {
        "fan": _state["fan"],
        "last_sensor_event": _state["last_sensor_event"],
        "hardware": "simulated",
    }
