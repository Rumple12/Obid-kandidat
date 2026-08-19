"""Aggregate Step 9 raw evaluation CSV files.

This script intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable


SUMMARY_FIELDS = [
    "mode",
    "test_case_id",
    "run_count",
    "success_count",
    "failure_count",
    "average_latency_ms",
    "min_latency_ms",
    "max_latency_ms",
    "expected_action",
    "observed_action",
]


RESOURCE_FIELDS = [
    "mode",
    "test_case_id",
    "run_count",
    "success_count",
    "failure_count",
    "average_latency_ms",
    "min_latency_ms",
    "max_latency_ms",
    "expected_action",
    "observed_action",
    "cpu_available_count",
    "ram_available_count",
    "thermal_available_count",
    "cpu_percent_values",
    "ram_usage_values",
    "ram_percent_values",
    "thermal_c_values",
]


SAFETY_FIELDS = [
    "mode",
    "test_case_id",
    "run_count",
    "success_count",
    "failure_count",
    "average_latency_ms",
    "min_latency_ms",
    "max_latency_ms",
    "expected_action",
    "observed_action",
    "expected_safety_result",
    "observed_safety_result",
]


def read_rows(raw_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(raw_dir.glob("*.csv")):
        with path.open("r", newline="", encoding="utf-8") as f:
            rows.extend(csv.DictReader(f))
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def as_float(value: str) -> float | None:
    try:
        if not value:
            return None
        return float(value)
    except ValueError:
        return None


def format_float(value: float | None) -> str:
    return "" if value is None else f"{value:.3f}"


def unique_join(values: Iterable[str]) -> str:
    cleaned = sorted({value for value in values if value})
    return "|".join(cleaned)


def grouped_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row.get("mode", ""), row.get("test_case_id", ""))].append(row)

    output: list[dict[str, str]] = []
    for (mode, case_id), group in sorted(groups.items()):
        latencies = [item for item in (as_float(row.get("latency_ms", "")) for row in group) if item is not None]
        output.append(
            {
                "mode": mode,
                "test_case_id": case_id,
                "run_count": str(len(group)),
                "success_count": str(sum(1 for row in group if row.get("success") == "true")),
                "failure_count": str(sum(1 for row in group if row.get("success") == "false")),
                "average_latency_ms": format_float(statistics.mean(latencies) if latencies else None),
                "min_latency_ms": format_float(min(latencies) if latencies else None),
                "max_latency_ms": format_float(max(latencies) if latencies else None),
                "expected_action": unique_join(row.get("expected_action", "") for row in group),
                "observed_action": unique_join(row.get("observed_action", "") for row in group),
            }
        )
    return output


def resource_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    base = grouped_summary(rows)
    lookup = {(row["mode"], row["test_case_id"]): row for row in base}
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row.get("mode", ""), row.get("test_case_id", ""))].append(row)

    output: list[dict[str, str]] = []
    for key, group in sorted(groups.items()):
        row = dict(lookup[key])
        cpu_values = [item.get("cpu_percent", "") for item in group if item.get("cpu_percent") not in {"", "not_available"}]
        ram_values = [item.get("ram_usage", "") for item in group if item.get("ram_usage") not in {"", "not_available"}]
        ram_percent_values = [item.get("ram_percent", "") for item in group if item.get("ram_percent") not in {"", "not_available"}]
        thermal_values = [item.get("thermal_c", "") for item in group if item.get("thermal_c") not in {"", "not_available"}]
        row.update(
            {
                "cpu_available_count": str(len(cpu_values)),
                "ram_available_count": str(len(ram_values)),
                "thermal_available_count": str(len(thermal_values)),
                "cpu_percent_values": "|".join(cpu_values),
                "ram_usage_values": "|".join(ram_values),
                "ram_percent_values": "|".join(ram_percent_values),
                "thermal_c_values": "|".join(thermal_values),
            }
        )
        output.append(row)
    return output


def safety_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    safety_rows = [row for row in rows if row.get("mode") == "safety"]
    base = grouped_summary(safety_rows)
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in safety_rows:
        groups[(row.get("mode", ""), row.get("test_case_id", ""))].append(row)

    output: list[dict[str, str]] = []
    for row in base:
        group = groups[(row["mode"], row["test_case_id"])]
        row = dict(row)
        row["expected_safety_result"] = unique_join(item.get("expected_safety_result", "") for item in group)
        row["observed_safety_result"] = unique_join(item.get("observed_safety_result", "") for item in group)
        output.append(row)
    return output


def baseline_vs_agent(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    workflow_rows = [row for row in rows if row.get("mode") in {"deterministic", "agent"}]
    return grouped_summary(workflow_rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Aggregate Step 9 evaluation results.")
    parser.add_argument("--raw-dir", default="evaluation/results/raw")
    parser.add_argument("--output-dir", default="evaluation/results/processed")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    raw_dir = Path(args.raw_dir)
    output_dir = Path(args.output_dir)
    rows = read_rows(raw_dir)

    write_csv(output_dir / "summary_latency.csv", SUMMARY_FIELDS, grouped_summary(rows))
    write_csv(output_dir / "summary_resources.csv", RESOURCE_FIELDS, resource_summary(rows))
    write_csv(output_dir / "safety_outcomes.csv", SAFETY_FIELDS, safety_summary(rows))
    write_csv(output_dir / "baseline_vs_agent.csv", SUMMARY_FIELDS, baseline_vs_agent(rows))

    if not rows:
        print(f"No raw CSV rows found in {raw_dir}. Wrote empty summary files.")
    else:
        print(f"Aggregated {len(rows)} raw rows into {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
