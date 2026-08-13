"""Collect lightweight Step 9 evaluation metrics.

This script intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


FIELDNAMES = [
    "timestamp_utc",
    "mode",
    "test_case_id",
    "run_index",
    "webhook_url",
    "input_temperature",
    "expected_action",
    "observed_action",
    "expected_safety_result",
    "observed_safety_result",
    "http_status",
    "success",
    "latency_ms",
    "cpu_percent",
    "ram_usage",
    "ram_percent",
    "thermal_c",
    "observed_response",
    "error",
    "notes",
]


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_cases(path: Path, mode: str, case_id: str | None) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = [case for case in data.get("test_cases", []) if case.get("mode") == mode]
    if case_id:
        cases = [case for case in cases if case.get("id") == case_id]
    if not cases:
        raise SystemExit(f"No test cases found for mode={mode!r} case_id={case_id!r}")
    return cases


def default_output_path(mode: str) -> Path:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return Path("evaluation") / "results" / "raw" / f"run_{stamp}_{mode}.csv"


def resolve_output_path(value: str | None, mode: str) -> Path:
    if not value:
        return default_output_path(mode)
    path = Path(value)
    if path.exists() and path.is_dir():
        return path / default_output_path(mode).name
    if str(value).endswith(("/", "\\")):
        return path / default_output_path(mode).name
    return path


def post_json(url: str, payload: dict[str, Any], timeout: float) -> tuple[int | str, str, str]:
    body = json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            text = response.read().decode("utf-8", errors="replace")
            return response.status, text, ""
    except HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        return exc.code, text, str(exc)
    except URLError as exc:
        return "not_available", "", str(exc)
    except TimeoutError as exc:
        return "not_available", "", str(exc)


def compact_text(value: str, limit: int = 700) -> str:
    value = value.replace("\r", " ").replace("\n", " ").strip()
    return value if len(value) <= limit else value[: limit - 3] + "..."


def find_action(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("action", "action_id", "expected_action", "observed_action"):
            item = value.get(key)
            if item in {"fan_on", "fan_off"}:
                return item
        for item in value.values():
            found = find_action(item)
            if found:
                return found
    elif isinstance(value, list):
        for item in value:
            found = find_action(item)
            if found:
                return found
    elif isinstance(value, str):
        if "fan_on" in value:
            return "fan_on"
        if "fan_off" in value:
            return "fan_off"
    return ""


def observed_action_from_response(text: str) -> str:
    if not text:
        return ""
    try:
        return find_action(json.loads(text))
    except json.JSONDecodeError:
        return find_action(text)


def docker_stats(container: str) -> dict[str, str]:
    command = [
        "docker",
        "stats",
        "--no-stream",
        "--format",
        "{{json .}}",
        container,
    ]
    try:
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        line = completed.stdout.strip().splitlines()[0]
        data = json.loads(line)
        return {
            "cpu_percent": data.get("CPUPerc", "not_available"),
            "ram_usage": data.get("MemUsage", "not_available"),
            "ram_percent": data.get("MemPerc", "not_available"),
        }
    except (FileNotFoundError, subprocess.SubprocessError, IndexError, json.JSONDecodeError):
        return {
            "cpu_percent": "not_available",
            "ram_usage": "not_available",
            "ram_percent": "not_available",
        }


def thermal_c() -> str:
    linux_thermal = Path("/sys/class/thermal/thermal_zone0/temp")
    if linux_thermal.exists():
        try:
            raw = float(linux_thermal.read_text(encoding="utf-8").strip())
            return f"{raw / 1000:.2f}"
        except (OSError, ValueError):
            return "not_available"
    return "not_available"


def workflow_row(
    *,
    mode: str,
    case: dict[str, Any],
    run_index: int,
    webhook_url: str,
    timeout: float,
    n8n_container: str,
) -> dict[str, str]:
    payload = case.get("sensor_event", {})
    expected_action = case.get("expected_action", "")
    start = time.perf_counter()
    status, response_text, error = post_json(webhook_url, payload, timeout)
    latency_ms = (time.perf_counter() - start) * 1000
    observed_action = observed_action_from_response(response_text)
    resources = docker_stats(n8n_container)

    http_ok = isinstance(status, int) and 200 <= status < 300
    action_ok = bool(observed_action) and observed_action == expected_action
    success = "true" if http_ok and action_ok else "false"
    notes = ""
    if http_ok and not observed_action:
        notes = "HTTP succeeded but expected action was not found in response."
    elif http_ok and observed_action != expected_action:
        notes = "HTTP succeeded but observed action did not match expected action."

    return {
        "timestamp_utc": utc_now(),
        "mode": mode,
        "test_case_id": case.get("id", ""),
        "run_index": str(run_index),
        "webhook_url": webhook_url,
        "input_temperature": str(payload.get("value", "")),
        "expected_action": expected_action,
        "observed_action": observed_action,
        "expected_safety_result": "",
        "observed_safety_result": "",
        "http_status": str(status),
        "success": success,
        "latency_ms": f"{latency_ms:.3f}",
        "cpu_percent": resources["cpu_percent"],
        "ram_usage": resources["ram_usage"],
        "ram_percent": resources["ram_percent"],
        "thermal_c": thermal_c(),
        "observed_response": compact_text(response_text),
        "error": compact_text(error),
        "notes": notes,
    }


def safety_row(case: dict[str, Any], run_index: int, n8n_container: str) -> dict[str, str]:
    resources = docker_stats(n8n_container)
    expected = case.get("expected_safety_result", "")
    return {
        "timestamp_utc": utc_now(),
        "mode": "safety",
        "test_case_id": case.get("id", ""),
        "run_index": str(run_index),
        "webhook_url": "",
        "input_temperature": "",
        "expected_action": "",
        "observed_action": "",
        "expected_safety_result": expected,
        "observed_safety_result": "specification_only_not_runtime_enforced",
        "http_status": "",
        "success": "not_applicable",
        "latency_ms": "",
        "cpu_percent": resources["cpu_percent"],
        "ram_usage": resources["ram_usage"],
        "ram_percent": resources["ram_percent"],
        "thermal_c": thermal_c(),
        "observed_response": compact_text(json.dumps(case.get("input_action", {}))),
        "error": "",
        "notes": "Step 8 safety cases document expected behavior only; no runtime enforcement tested.",
    }


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect Step 9 evaluation metrics.")
    parser.add_argument("--mode", choices=["deterministic", "agent", "safety"], required=True)
    parser.add_argument("--webhook-url", default="", help="n8n test webhook URL for workflow modes.")
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--dataset", default="evaluation/datasets/test-cases.json")
    parser.add_argument("--output", default="")
    parser.add_argument("--case-id", default="", help="Optional single test case id to run.")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--n8n-container", default="new-yacoub-n8n")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1")
    if args.mode in {"deterministic", "agent"} and not args.webhook_url:
        raise SystemExit("--webhook-url is required for deterministic and agent modes")

    cases = load_cases(Path(args.dataset), args.mode, args.case_id or None)
    rows: list[dict[str, str]] = []
    for run_index in range(1, args.runs + 1):
        for case in cases:
            if args.mode == "safety":
                rows.append(safety_row(case, run_index, args.n8n_container))
            else:
                rows.append(
                    workflow_row(
                        mode=args.mode,
                        case=case,
                        run_index=run_index,
                        webhook_url=args.webhook_url,
                        timeout=args.timeout,
                        n8n_container=args.n8n_container,
                    )
                )

    output = resolve_output_path(args.output or None, args.mode)
    write_rows(output, rows)
    print(f"Wrote {len(rows)} rows to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
