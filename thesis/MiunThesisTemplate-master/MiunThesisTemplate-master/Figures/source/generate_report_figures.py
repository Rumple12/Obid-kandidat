#!/usr/bin/env python3
"""Regenerate the four final Obid thesis figures.

The script resolves the repository root from its own tracked location, reads the
two frozen Step 10 RQ3 CSV files directly, validates their complete expected
contents, and writes vector PDF figures beside the thesis Figure directory.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import math
import statistics
from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


FIGURE_NAMES = (
    "final-system-architecture.pdf",
    "config-obid-pipeline.pdf",
    "evaluation-evidence-flow.pdf",
    "rq3-results.pdf",
)

RELIABILITY_SHA256 = "95b57ba0d2a51656797eabeaf2cd0d8cae080e049a0ff82241d58ed307bc5ac5"
LATENCY_SHA256 = "520926e512e2942e8e1578dffdc5d7f064d449d3bb4e65d7b7b52f04dfbe711c"

CONFIGS = ("CONFIG-BASELINE", "CONFIG-OBID")
CASE_IDS = (
    "EVAL-HIGH-01",
    "EVAL-LOW-01",
    "EVAL-THRESHOLD-01",
    "EVAL-MALFORMED-01",
    "EVAL-MEMORY-01A",
    "EVAL-MEMORY-01B",
    "EVAL-MEMORY-01C",
)
CASE_LABELS = ("High", "Low", "Threshold", "Malformed", "Memory A", "Memory B", "Memory C")
LATENCY_CASE_IDS = CASE_IDS[:3]

EXPECTED_CORRECT = {
    ("EVAL-HIGH-01", "CONFIG-BASELINE"): 5,
    ("EVAL-HIGH-01", "CONFIG-OBID"): 5,
    ("EVAL-LOW-01", "CONFIG-BASELINE"): 5,
    ("EVAL-LOW-01", "CONFIG-OBID"): 5,
    ("EVAL-THRESHOLD-01", "CONFIG-BASELINE"): 5,
    ("EVAL-THRESHOLD-01", "CONFIG-OBID"): 5,
    ("EVAL-MALFORMED-01", "CONFIG-BASELINE"): 0,
    ("EVAL-MALFORMED-01", "CONFIG-OBID"): 5,
    ("EVAL-MEMORY-01A", "CONFIG-BASELINE"): 5,
    ("EVAL-MEMORY-01A", "CONFIG-OBID"): 5,
    ("EVAL-MEMORY-01B", "CONFIG-BASELINE"): 0,
    ("EVAL-MEMORY-01B", "CONFIG-OBID"): 5,
    ("EVAL-MEMORY-01C", "CONFIG-BASELINE"): 5,
    ("EVAL-MEMORY-01C", "CONFIG-OBID"): 5,
}

EXPECTED_LATENCY = {
    ("EVAL-HIGH-01", "CONFIG-BASELINE"): ([4631, 2130, 2056, 2184, 2016], 2130),
    ("EVAL-HIGH-01", "CONFIG-OBID"): ([4660, 3524, 4803, 3792, 3672], 3792),
    ("EVAL-LOW-01", "CONFIG-BASELINE"): ([2250, 2009, 2065, 2105, 2164], 2105),
    ("EVAL-LOW-01", "CONFIG-OBID"): ([4472, 5565, 4358, 4237, 5282], 4472),
    ("EVAL-THRESHOLD-01", "CONFIG-BASELINE"): ([2059, 2252, 2083, 2152, 1998], 2083),
    ("EVAL-THRESHOLD-01", "CONFIG-OBID"): ([4279, 4487, 4365, 4689, 4593], 4487),
}

RELIABILITY_HEADERS = (
    "case_id",
    "configuration",
    "attempted",
    "correct",
    "correctness_percentage",
    "modal_outcome_signature",
    "modal_count",
    "modal_agreement_percentage",
    "modal_tie_count",
    "visible_failure_categories",
    "raw_run_ids",
    "n8n_execution_ids",
)

LATENCY_HEADERS = (
    "case_id",
    "configuration",
    "attempted",
    "duration_values_available",
    "duration_completeness",
    "raw_duration_ms_by_repetition",
    "median_ms",
    "minimum_ms",
    "maximum_ms",
    "supplementary_mean_ms",
    "timing_start",
    "timing_end",
    "raw_run_ids",
    "n8n_execution_ids",
)

COLORS = {
    "ink": "#20262E",
    "muted": "#58616B",
    "line": "#4A5560",
    "blue": "#2C7FB8",
    "blue_dark": "#195A84",
    "blue_pale": "#E7F1F8",
    "gray": "#D9DEE3",
    "gray_pale": "#F2F4F5",
    "gold": "#B88A2A",
    "gold_pale": "#F7F0DD",
    "red": "#A44343",
    "red_pale": "#F8E8E8",
    "green": "#3B7A57",
    "green_pale": "#E7F2EB",
    "white": "#FFFFFF",
}


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.0,
            "axes.titlesize": 9.0,
            "axes.labelsize": 8.0,
            "xtick.labelsize": 7.3,
            "ytick.labelsize": 7.3,
            "legend.fontsize": 7.3,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.edgecolor": COLORS["line"],
            "axes.labelcolor": COLORS["ink"],
            "xtick.color": COLORS["ink"],
            "ytick.color": COLORS["ink"],
            "text.color": COLORS["ink"],
        }
    )


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    raise RuntimeError("Repository root not found above the generation script.")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_csv(path: Path, expected_headers: tuple[str, ...], expected_sha: str) -> list[dict[str, str]]:
    require(path.is_file(), f"Required frozen input is missing: {path.as_posix()}")
    actual_sha = sha256(path)
    require(
        actual_sha == expected_sha,
        f"Frozen input hash differs for {path.name}: expected {expected_sha}, observed {actual_sha}",
    )
    with path.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = tuple(reader.fieldnames or ())
        require(
            headers == expected_headers,
            f"Unexpected columns in {path.name}: expected {expected_headers}, observed {headers}",
        )
        return list(reader)


def unique_rows(rows: Iterable[dict[str, str]], source_name: str) -> dict[tuple[str, str], dict[str, str]]:
    indexed: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        key = (row["case_id"], row["configuration"])
        require(key not in indexed, f"Duplicate row {key} in {source_name}")
        indexed[key] = row
    return indexed


def validate_reliability(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    indexed = unique_rows(rows, "rq3-reliability.csv")
    expected_keys = {(case_id, config) for case_id in CASE_IDS for config in CONFIGS}
    require(set(indexed) == expected_keys, "rq3-reliability.csv does not contain exactly the 14 frozen case/configuration rows.")

    for key, expected_correct in EXPECTED_CORRECT.items():
        row = indexed[key]
        attempted = int(row["attempted"])
        correct = int(row["correct"])
        percentage = float(row["correctness_percentage"])
        require(attempted == 5, f"{key} attempted differs: expected 5, observed {attempted}")
        require(correct == expected_correct, f"{key} correct differs: expected {expected_correct}, observed {correct}")
        require(
            math.isclose(percentage, correct / attempted * 100.0, abs_tol=1e-9),
            f"{key} correctness_percentage is inconsistent with correct/attempted.",
        )
    return indexed


def validate_latency(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, object]]:
    raw_index = unique_rows(rows, "rq3-latency.csv")
    expected_keys = {(case_id, config) for case_id in LATENCY_CASE_IDS for config in CONFIGS}
    require(set(raw_index) == expected_keys, "rq3-latency.csv does not contain exactly the six frozen automated-latency rows.")

    validated: dict[tuple[str, str], dict[str, object]] = {}
    for key, (expected_values, expected_median) in EXPECTED_LATENCY.items():
        row = raw_index[key]
        values = [int(value) for value in row["raw_duration_ms_by_repetition"].split("|")]
        require(int(row["attempted"]) == 5, f"{key} attempted differs from 5.")
        require(int(row["duration_values_available"]) == 5, f"{key} does not retain five duration values.")
        require(row["duration_completeness"] == "5/5", f"{key} duration_completeness differs from 5/5.")
        require(len(values) == 5 and all(value > 0 for value in values), f"{key} must contain five positive durations.")
        require(values == expected_values, f"{key} raw durations differ: expected {expected_values}, observed {values}")
        require(int(row["median_ms"]) == expected_median, f"{key} stored median differs from {expected_median} ms.")
        require(statistics.median(values) == expected_median, f"{key} recalculated median differs from {expected_median} ms.")
        require(int(row["minimum_ms"]) == min(values), f"{key} stored minimum is inconsistent.")
        require(int(row["maximum_ms"]) == max(values), f"{key} stored maximum is inconsistent.")
        require(
            math.isclose(float(row["supplementary_mean_ms"]), statistics.mean(values), abs_tol=0.05),
            f"{key} stored supplementary mean is inconsistent.",
        )
        require(
            row["timing_start"] == "configuration ingress begins processing",
            f"{key} timing start differs from the frozen boundary.",
        )
        require(
            row["timing_end"] == "final automated terminal including Yacoub endpoint response",
            f"{key} timing end differs from the frozen boundary.",
        )
        validated[key] = {"values": values, "median": expected_median}
    return validated


def canvas(figsize: tuple[float, float]) -> tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def add_box(
    ax: plt.Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    text: str,
    *,
    facecolor: str = COLORS["white"],
    edgecolor: str = COLORS["line"],
    linewidth: float = 1.0,
    linestyle: str = "solid",
    fontsize: float = 7.6,
    weight: str = "normal",
    textcolor: str = COLORS["ink"],
    zorder: int = 3,
) -> None:
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=zorder,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        color=textcolor,
        linespacing=1.2,
        zorder=zorder + 1,
    )


def add_arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = COLORS["line"],
    linewidth: float = 1.15,
    linestyle: str = "solid",
    connectionstyle: str = "arc3",
    zorder: int = 4,
) -> None:
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=9,
        linewidth=linewidth,
        linestyle=linestyle,
        color=color,
        connectionstyle=connectionstyle,
        shrinkA=2,
        shrinkB=2,
        zorder=zorder,
    )
    ax.add_patch(arrow)


def add_arrow_label(ax: plt.Axes, x: float, y: float, text: str, *, fontsize: float = 6.8, color: str = COLORS["muted"]) -> None:
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=color,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.7, "alpha": 0.92},
        zorder=8,
    )


def add_routed_arrow(
    ax: plt.Axes,
    points: tuple[tuple[float, float], ...],
    *,
    color: str = COLORS["line"],
    linewidth: float = 1.15,
    linestyle: str = "solid",
    zorder: int = 2,
) -> None:
    require(len(points) >= 2, "A routed arrow needs at least two points.")
    if len(points) > 2:
        xs, ys = zip(*points[:-1])
        ax.plot(xs, ys, color=color, linewidth=linewidth, linestyle=linestyle, zorder=zorder)
    add_arrow(
        ax,
        points[-2],
        points[-1],
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=zorder + 1,
    )


def fixed_metadata(title: str) -> dict[str, object]:
    fixed_time = dt.datetime(2026, 8, 28, 0, 0, 0, tzinfo=dt.timezone.utc)
    return {
        "Title": title,
        "Author": "Obid thesis repository",
        "Subject": "Final thesis figure generated from frozen repository artifacts",
        "Keywords": "Obid thesis, reproducible figure",
        "Creator": "Figures/source/generate_report_figures.py",
        "CreationDate": fixed_time,
        "ModDate": fixed_time,
    }


def save_figure(fig: plt.Figure, output: Path, title: str) -> None:
    fig.savefig(
        output,
        format="pdf",
        bbox_inches="tight",
        pad_inches=0.04,
        metadata=fixed_metadata(title),
    )
    plt.close(fig)


def generate_final_system_architecture(output: Path) -> None:
    fig, ax = canvas((7.4, 5.0))

    bands = (
        (0.015, 0.30, COLORS["gray_pale"], COLORS["line"], "YACOUB_INHERITED"),
        (0.33, 0.23, COLORS["gold_pale"], COLORS["gold"], "SHARED_INTERFACE"),
        (0.575, 0.41, COLORS["blue_pale"], COLORS["blue_dark"], "OBID_CREATED"),
    )
    for x, width, fill, edge, label in bands:
        ax.add_patch(Rectangle((x, 0.045), width, 0.92, facecolor=fill, edgecolor=edge, linewidth=1.1, zorder=0))
        ax.add_patch(Rectangle((x, 0.895), width, 0.07, facecolor=edge, edgecolor=edge, linewidth=0, zorder=1))
        ax.text(x + width / 2, 0.93, label, color="white", ha="center", va="center", fontsize=7.7, fontweight="bold")

    add_box(ax, 0.04, 0.76, 0.25, 0.085, "Inherited workflow-to-\naction infrastructure", facecolor=COLORS["white"], weight="bold", fontsize=6.8)
    add_box(
        ax,
        0.04,
        0.57,
        0.25,
        0.125,
        "CONFIG-BASELINE\ninherited minimal agent\nstateless comparator",
        facecolor=COLORS["gray"],
        weight="bold",
        fontsize=6.9,
    )
    add_box(ax, 0.04, 0.315, 0.25, 0.11, "Middleware / action API\ninherited endpoint\nexecution", facecolor=COLORS["white"], weight="bold", fontsize=6.7)
    add_box(
        ax,
        0.04,
        0.105,
        0.25,
        0.125,
        "Simulated fan state\nevaluation boundary only\nno new physical Pi evidence",
        facecolor=COLORS["white"],
        weight="bold",
        fontsize=6.6,
    )

    add_box(ax, 0.355, 0.745, 0.18, 0.105, "Sensor-event\ncontract", facecolor=COLORS["white"], edgecolor=COLORS["gold"], weight="bold", fontsize=7.0)
    add_box(ax, 0.355, 0.46, 0.18, 0.105, "Four-field\naction contract", facecolor=COLORS["white"], edgecolor=COLORS["gold"], weight="bold", fontsize=7.0)
    add_box(ax, 0.355, 0.24, 0.18, 0.105, "Compatible endpoint\nmeanings", facecolor=COLORS["white"], edgecolor=COLORS["gold"], weight="bold", fontsize=6.8)

    add_box(
        ax,
        0.605,
        0.66,
        0.35,
        0.19,
        "CONFIG-OBID\nDecision Agent + two read-only tools\ntwo-interaction bounded memory\ninternal structured decision",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        linewidth=1.3,
        weight="bold",
        fontsize=6.9,
    )
    add_box(
        ax,
        0.605,
        0.38,
        0.35,
        0.18,
        "Runtime release control\naction validation -> deterministic policy\n-> conditional HITL\nBLOCK / ALLOW / APPROVAL_REQUIRED",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        linewidth=1.3,
        weight="bold",
        fontsize=6.6,
    )
    add_box(
        ax,
        0.605,
        0.135,
        0.35,
        0.15,
        "Controlled evaluation layer\npaired configurations, repeated runs,\nevidence capture and processing",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        linewidth=1.3,
        weight="bold",
        fontsize=6.9,
    )

    add_arrow(ax, (0.355, 0.795), (0.29, 0.635))
    add_arrow(ax, (0.535, 0.795), (0.605, 0.755))
    add_arrow(ax, (0.165, 0.57), (0.355, 0.515))
    add_arrow(ax, (0.78, 0.66), (0.78, 0.56), color=COLORS["blue_dark"])
    add_arrow(ax, (0.605, 0.47), (0.535, 0.515), color=COLORS["blue_dark"])
    add_arrow(ax, (0.355, 0.515), (0.29, 0.37))
    add_arrow(ax, (0.355, 0.292), (0.29, 0.355), linestyle="dashed")
    add_arrow(ax, (0.165, 0.315), (0.165, 0.23))

    add_routed_arrow(
        ax,
        ((0.29, 0.635), (0.315, 0.635), (0.315, 0.61), (0.555, 0.61), (0.555, 0.21), (0.605, 0.21)),
        color=COLORS["muted"],
        linestyle="dotted",
    )
    add_arrow(ax, (0.78, 0.38), (0.78, 0.285), color=COLORS["blue_dark"], linestyle="dotted")
    add_arrow(ax, (0.29, 0.165), (0.605, 0.195), color=COLORS["muted"], linestyle="dotted")

    add_arrow_label(ax, 0.245, 0.49, "candidate action", fontsize=6.1)

    save_figure(fig, output, "Final system architecture and provenance boundary")


def generate_config_obid_pipeline(output: Path) -> None:
    source_image = Path(__file__).with_name("config-obid-pipeline-figure3.png")
    if not source_image.is_file():
        _generate_config_obid_pipeline_fallback(output)
        return

    image = plt.imread(source_image)
    # The supplied artwork includes a copy of the thesis caption below the
    # diagram. Crop that copy so the unchanged LaTeX caption appears once.
    diagram = image[:1325, :, :]
    width_inches = 7.25
    height_inches = width_inches * diagram.shape[0] / diagram.shape[1]
    fig = plt.figure(figsize=(width_inches, height_inches), facecolor=COLORS["white"])
    ax = fig.add_axes((0, 0, 1, 1))
    ax.imshow(diagram, interpolation="none")
    ax.set_axis_off()
    save_figure(fig, output, "CONFIG-OBID decision and release pipeline")


def _generate_config_obid_pipeline_fallback(output: Path) -> None:
    fig, ax = canvas((7.4, 5.65))

    ax.add_patch(Rectangle((0.015, 0.69), 0.97, 0.27, facecolor=COLORS["blue_pale"], edgecolor=COLORS["blue_dark"], linewidth=1.0, zorder=0))
    ax.text(0.03, 0.935, "MODEL PROPOSAL - no release authority", fontsize=8.0, fontweight="bold", color=COLORS["blue_dark"], va="center")

    add_box(ax, 0.035, 0.785, 0.115, 0.085, "Sensor or\ntest event", weight="bold", fontsize=7.0)
    add_box(ax, 0.18, 0.785, 0.15, 0.085, "OBID_INPUT_\nHANDLING", facecolor=COLORS["white"], edgecolor=COLORS["blue_dark"], weight="bold", fontsize=6.9)
    add_box(
        ax,
        0.36,
        0.735,
        0.36,
        0.185,
        "Decision Agent (maxIterations: 3)\nGemini 2.5 Flash\ntemperature_threshold_tool - read-only\nfan_status_tool - read-only\ntwo-interaction bounded memory",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        linewidth=1.25,
        weight="bold",
        fontsize=6.6,
    )
    add_box(
        ax,
        0.755,
        0.765,
        0.205,
        0.125,
        "Internal decision envelope\nno_action OR emit_action\nproposal only",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        linewidth=1.25,
        weight="bold",
        fontsize=6.8,
    )
    add_arrow(ax, (0.15, 0.827), (0.18, 0.827), color=COLORS["blue_dark"])
    add_arrow(ax, (0.33, 0.827), (0.36, 0.827), color=COLORS["blue_dark"])
    add_arrow(ax, (0.72, 0.827), (0.755, 0.827), color=COLORS["blue_dark"])

    ax.add_patch(Rectangle((0.015, 0.04), 0.97, 0.61, facecolor=COLORS["gray_pale"], edgecolor=COLORS["line"], linewidth=1.0, zorder=0))
    ax.text(0.03, 0.625, "DETERMINISTIC RELEASE CONTROL", fontsize=8.0, fontweight="bold", color=COLORS["ink"], va="center")

    add_box(ax, 0.035, 0.47, 0.15, 0.085, "decision =\nno_action", facecolor=COLORS["gold_pale"], edgecolor=COLORS["gold"], weight="bold", fontsize=6.8)
    add_box(ax, 0.035, 0.34, 0.15, 0.085, "STOP\nno shared action", facecolor=COLORS["red_pale"], edgecolor=COLORS["red"], weight="bold", fontsize=6.9)

    add_box(ax, 0.245, 0.47, 0.17, 0.085, "decision = emit_action\nfour-field candidate", facecolor=COLORS["white"], edgecolor=COLORS["blue_dark"], weight="bold", fontsize=6.3)
    add_box(ax, 0.465, 0.47, 0.16, 0.085, "Runtime action\nvalidation", facecolor=COLORS["white"], edgecolor=COLORS["blue_dark"], weight="bold", fontsize=6.9)
    add_box(ax, 0.68, 0.47, 0.15, 0.085, "Deterministic\npolicy", facecolor=COLORS["white"], edgecolor=COLORS["blue_dark"], weight="bold", fontsize=6.9)

    add_routed_arrow(ax, ((0.83, 0.765), (0.83, 0.675), (0.11, 0.675), (0.11, 0.555)), color=COLORS["gold"])
    add_routed_arrow(ax, ((0.87, 0.765), (0.87, 0.67), (0.33, 0.67), (0.33, 0.555)), color=COLORS["blue_dark"])
    add_arrow_label(ax, 0.255, 0.655, "internal no_action is not a shared action", fontsize=6.2, color=COLORS["gold"])
    add_arrow(ax, (0.11, 0.47), (0.11, 0.425), color=COLORS["red"])
    add_arrow(ax, (0.415, 0.512), (0.465, 0.512), color=COLORS["blue_dark"])
    add_arrow(ax, (0.625, 0.512), (0.68, 0.512), color=COLORS["blue_dark"])

    add_box(ax, 0.45, 0.285, 0.13, 0.075, "BLOCK", facecolor=COLORS["red_pale"], edgecolor=COLORS["red"], weight="bold", textcolor=COLORS["red"])
    add_box(ax, 0.64, 0.285, 0.13, 0.075, "ALLOW", facecolor=COLORS["green_pale"], edgecolor=COLORS["green"], weight="bold", textcolor=COLORS["green"])
    add_box(ax, 0.82, 0.275, 0.14, 0.095, "APPROVAL_\nREQUIRED", facecolor=COLORS["gold_pale"], edgecolor=COLORS["gold"], weight="bold", textcolor=COLORS["gold"], fontsize=6.8)
    add_arrow(ax, (0.735, 0.47), (0.515, 0.36), color=COLORS["red"], connectionstyle="arc3,rad=0.15")
    add_arrow(ax, (0.755, 0.47), (0.705, 0.36), color=COLORS["green"], connectionstyle="arc3,rad=0.08")
    add_arrow(ax, (0.79, 0.47), (0.87, 0.37), color=COLORS["gold"], connectionstyle="arc3,rad=-0.12")
    add_arrow(ax, (0.545, 0.47), (0.515, 0.36), color=COLORS["red"], linestyle="dashed")
    add_arrow_label(ax, 0.535, 0.425, "invalid -> BLOCK; no HITL rescue", fontsize=6.1, color=COLORS["red"])

    add_box(ax, 0.45, 0.115, 0.13, 0.075, "STOP\nno release", facecolor=COLORS["red_pale"], edgecolor=COLORS["red"], weight="bold", fontsize=6.8)
    add_box(ax, 0.64, 0.115, 0.14, 0.075, "Inherited middleware\nendpoint", facecolor=COLORS["white"], edgecolor=COLORS["line"], weight="bold", fontsize=6.3)
    add_box(ax, 0.64, 0.052, 0.14, 0.043, "Simulated fan state", facecolor=COLORS["white"], edgecolor=COLORS["line"], weight="bold", fontsize=6.2)
    add_box(ax, 0.82, 0.115, 0.14, 0.075, "Native HITL\nWait / form", facecolor=COLORS["white"], edgecolor=COLORS["gold"], weight="bold", fontsize=6.7)
    add_arrow(ax, (0.515, 0.285), (0.515, 0.19), color=COLORS["red"])
    add_arrow(ax, (0.705, 0.285), (0.705, 0.19), color=COLORS["green"])
    add_arrow(ax, (0.89, 0.275), (0.89, 0.19), color=COLORS["gold"])
    add_arrow(ax, (0.705, 0.115), (0.705, 0.095), color=COLORS["line"])
    add_arrow(ax, (0.82, 0.152), (0.78, 0.152), color=COLORS["green"])
    add_arrow_label(ax, 0.80, 0.205, "approve - unchanged held action", fontsize=5.8, color=COLORS["green"])
    add_routed_arrow(ax, ((0.96, 0.152), (0.975, 0.152), (0.975, 0.235), (0.58, 0.235), (0.58, 0.19)), color=COLORS["red"])
    add_arrow_label(ax, 0.93, 0.235, "deny", fontsize=6.0, color=COLORS["red"])

    save_figure(fig, output, "CONFIG-OBID decision and release pipeline")


def generate_evaluation_evidence_flow(output: Path) -> None:
    fig, ax = canvas((7.25, 5.00))

    phases = (
        (0.675, 0.305, COLORS["blue_pale"], COLORS["blue_dark"], "1  FROZEN DESIGN — BEFORE OBSERVATION"),
        (0.325, 0.325, COLORS["gray_pale"], COLORS["line"], "2  IMMUTABLE RUNTIME EVIDENCE"),
        (0.005, 0.290, COLORS["gold_pale"], COLORS["gold"], "3  TRACEABLE CLAIMS AND FINAL FREEZE"),
    )
    for y, height, fill, edge, title in phases:
        ax.add_patch(Rectangle((0.015, y), 0.97, height, facecolor=fill, edgecolor=edge, linewidth=1.05, zorder=0))
        ax.text(0.03, y + height - 0.035, title, ha="left", va="center", fontsize=9.2, fontweight="bold", color=edge)

    # Phase 1: one unambiguous left-to-right frozen-design flow.
    add_box(
        ax,
        0.025,
        0.750,
        0.310,
        0.130,
        "Frozen cases & oracle\nshared contracts & protocol\nfixed before observation",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        weight="bold",
        fontsize=7.6,
    )
    add_box(
        ax,
        0.370,
        0.750,
        0.230,
        0.130,
        "Fixed run order &\nconfiguration pairing",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        weight="bold",
        fontsize=7.8,
    )
    add_box(
        ax,
        0.645,
        0.740,
        0.330,
        0.150,
        "Repeated runtime executions\ncore comparison | invalid-action\ninjection | actual HITL trials",
        facecolor=COLORS["white"],
        edgecolor=COLORS["blue_dark"],
        weight="bold",
        fontsize=7.5,
    )
    add_arrow(ax, (0.335, 0.815), (0.370, 0.815), color=COLORS["blue_dark"], linewidth=1.3)
    add_arrow(ax, (0.600, 0.815), (0.645, 0.815), color=COLORS["blue_dark"], linewidth=1.3)

    # Phase 2: a visible split between universal attempt records and HITL-only
    # snapshots, followed by a single merge before the raw-data lock.
    branch_point = (0.505, 0.565)
    add_routed_arrow(
        ax,
        ((0.810, 0.740), (0.810, 0.590), (0.505, 0.590), branch_point),
        color=COLORS["line"],
        linewidth=1.25,
    )
    ax.plot(*branch_point, marker="o", markersize=3.6, color=COLORS["line"], zorder=6)
    add_routed_arrow(ax, (branch_point, (0.265, 0.565), (0.265, 0.535)), color=COLORS["line"], linewidth=1.2)
    add_routed_arrow(ax, (branch_point, (0.7725, 0.565), (0.7725, 0.535)), color=COLORS["line"], linewidth=1.2)
    add_arrow_label(ax, 0.325, 0.548, "all attempts", fontsize=7.0, color=COLORS["ink"])
    add_arrow_label(ax, 0.685, 0.548, "HITL trials only", fontsize=7.0, color=COLORS["ink"])

    add_box(
        ax,
        0.015,
        0.415,
        0.500,
        0.120,
        "Attempt events + primary run records\nAll attempts; no result replacement\nFailures / rejects / timeouts\nand deviations retained",
        facecolor=COLORS["white"],
        edgecolor=COLORS["line"],
        weight="bold",
        fontsize=7.4,
    )
    add_box(
        ax,
        0.570,
        0.440,
        0.405,
        0.095,
        "Pending HITL snapshots\nConditional evidence",
        facecolor=COLORS["white"],
        edgecolor=COLORS["line"],
        weight="bold",
        fontsize=7.8,
    )

    merge_point = (0.525, 0.410)
    ax.plot((0.265, 0.265, 0.525), (0.415, 0.410, 0.410), color=COLORS["line"], linewidth=1.2, zorder=2)
    ax.plot((0.7725, 0.7725, 0.525), (0.440, 0.410, 0.410), color=COLORS["line"], linewidth=1.2, zorder=2)
    ax.plot(*merge_point, marker="o", markersize=3.6, color=COLORS["line"], zorder=6)

    add_box(
        ax,
        0.400,
        0.335,
        0.230,
        0.060,
        "Raw-data lock\nbefore processing",
        facecolor=COLORS["white"],
        edgecolor=COLORS["line"],
        weight="bold",
        fontsize=7.6,
    )
    add_box(
        ax,
        0.695,
        0.335,
        0.280,
        0.060,
        "Deterministic processing",
        facecolor=COLORS["white"],
        edgecolor=COLORS["line"],
        weight="bold",
        fontsize=7.8,
    )
    add_arrow(ax, merge_point, (0.515, 0.395), color=COLORS["line"], linewidth=1.25)
    add_arrow(ax, (0.630, 0.365), (0.695, 0.365), color=COLORS["line"], linewidth=1.25)

    # Phase 3: the main claim flow stays universal; traceability and R03 are
    # explicitly secondary supports that converge on the thesis claims.
    add_box(
        ax,
        0.040,
        0.175,
        0.210,
        0.065,
        "RQ1 / RQ2 / RQ3\nsummaries",
        facecolor=COLORS["white"],
        edgecolor=COLORS["gold"],
        weight="bold",
        fontsize=8.0,
    )
    add_box(
        ax,
        0.405,
        0.175,
        0.170,
        0.065,
        "Thesis claims",
        facecolor=COLORS["white"],
        edgecolor=COLORS["gold"],
        weight="bold",
        fontsize=8.1,
    )
    add_box(
        ax,
        0.735,
        0.175,
        0.220,
        0.065,
        "Independent audit &\nfinal freeze",
        facecolor=COLORS["white"],
        edgecolor=COLORS["gold"],
        weight="bold",
        fontsize=7.8,
    )
    add_arrow(ax, (0.250, 0.2075), (0.405, 0.2075), color=COLORS["gold"], linewidth=1.3)
    add_arrow(ax, (0.575, 0.2075), (0.735, 0.2075), color=COLORS["gold"], linewidth=1.3)

    add_box(
        ax,
        0.110,
        0.015,
        0.350,
        0.115,
        "Traceability\nsummary → primary run ID\n→ n8n execution ID → raw evidence",
        facecolor=COLORS["white"],
        edgecolor=COLORS["gold"],
        linewidth=1.0,
        linestyle="dashed",
        weight="bold",
        fontsize=7.0,
    )
    add_box(
        ax,
        0.520,
        0.015,
        0.455,
        0.115,
        "R03 interpretation correction\nRQ2 only\nraw and historical processed evidence\nunchanged",
        facecolor=COLORS["white"],
        edgecolor=COLORS["gold"],
        linewidth=1.0,
        linestyle="dashed",
        weight="bold",
        fontsize=6.9,
    )
    add_arrow(ax, (0.285, 0.130), (0.445, 0.175), color=COLORS["gold"], linewidth=1.15, linestyle="dashed")
    add_arrow(ax, (0.7475, 0.130), (0.535, 0.175), color=COLORS["gold"], linewidth=1.15, linestyle="dashed")

    # Continuous transition from processed evidence into the summary/claim
    # phase. The horizontal segment stays in the inter-phase gap, and the
    # final arrow enters the summaries box from the unobstructed left side.
    add_routed_arrow(
        ax,
        ((0.835, 0.335), (0.835, 0.312), (0.005, 0.312), (0.005, 0.2075), (0.040, 0.2075)),
        color=COLORS["gold"],
        linewidth=1.3,
        zorder=4,
    )

    save_figure(fig, output, "Frozen evaluation and evidence traceability flow")


def generate_rq3_results(
    output: Path,
    reliability: dict[tuple[str, str], dict[str, str]],
    latency: dict[tuple[str, str], dict[str, object]],
) -> None:
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.25, 3.60), gridspec_kw={"width_ratios": [1.05, 1.0]})

    family_centers = list(range(len(CASE_IDS)))
    bar_height = 0.27
    baseline_positions = [center - 0.17 for center in family_centers]
    obid_positions = [center + 0.17 for center in family_centers]
    baseline = [int(reliability[(case_id, "CONFIG-BASELINE")]["correct"]) for case_id in CASE_IDS]
    obid = [int(reliability[(case_id, "CONFIG-OBID")]["correct"]) for case_id in CASE_IDS]

    ax_a.barh(
        baseline_positions,
        baseline,
        bar_height,
        color=COLORS["gray_pale"],
        edgecolor=COLORS["line"],
        linewidth=0.8,
        hatch="////",
        zorder=2,
    )
    ax_a.barh(
        obid_positions,
        obid,
        bar_height,
        color=COLORS["blue"],
        edgecolor=COLORS["blue_dark"],
        linewidth=0.8,
        hatch="....",
        zorder=2,
    )

    ax_a.scatter(
        baseline,
        baseline_positions,
        s=25,
        marker="o",
        facecolors=COLORS["white"],
        edgecolors=COLORS["line"],
        linewidths=1.0,
        zorder=4,
    )
    ax_a.scatter(
        obid,
        obid_positions,
        s=25,
        marker="s",
        facecolors=COLORS["blue"],
        edgecolors=COLORS["blue_dark"],
        linewidths=1.0,
        zorder=4,
    )
    for count, y_position in zip(baseline, baseline_positions):
        if count == 0:
            ax_a.scatter(0, y_position, s=34, marker="x", color=COLORS["red"], linewidths=1.5, zorder=5)
        ax_a.text(
            4.48 if count else 0.20,
            y_position,
            f"{count}/5",
            ha="center" if count else "left",
            va="center",
            fontsize=7.4,
            fontweight="bold",
            color=COLORS["ink"] if count else COLORS["red"],
            zorder=6,
        )
    for count, y_position in zip(obid, obid_positions):
        ax_a.text(
            4.48,
            y_position,
            f"{count}/5",
            ha="center",
            va="center",
            fontsize=7.4,
            fontweight="bold",
            color=COLORS["white"],
            zorder=6,
        )

    ax_a.set_title("(a) Reliability correctness", loc="left", fontweight="bold", pad=8)
    ax_a.set_xlabel("Correct runs (out of 5)")
    ax_a.set_yticks(family_centers, CASE_LABELS)
    ax_a.set_xlim(-0.24, 5.66)
    ax_a.set_xticks(range(0, 6))
    ax_a.set_ylim(-0.58, len(CASE_IDS) - 0.42)
    ax_a.invert_yaxis()
    ax_a.tick_params(axis="both", labelsize=7.7)
    ax_a.grid(axis="x", color="#D7DADD", linewidth=0.6, alpha=0.85)
    ax_a.set_axisbelow(True)
    ax_a.spines[["top", "right", "left"]].set_visible(False)
    ax_a.tick_params(axis="y", length=0)

    case_centers = [0.0, 1.0, 2.0]
    config_offsets = {"CONFIG-BASELINE": -0.16, "CONFIG-OBID": 0.16}
    point_spread = (-0.050, -0.025, 0.0, 0.025, 0.050)
    marker_styles = {
        "CONFIG-BASELINE": dict(marker="o", facecolors=COLORS["white"], edgecolors=COLORS["line"]),
        "CONFIG-OBID": dict(marker="s", facecolors=COLORS["blue"], edgecolors=COLORS["blue_dark"]),
    }

    for center, case_id in zip(case_centers, LATENCY_CASE_IDS):
        for config in CONFIGS:
            position = center + config_offsets[config]
            values = latency[(case_id, config)]["values"]
            median = int(latency[(case_id, config)]["median"])
            ax_b.plot(
                [position - 0.105, position + 0.105],
                [median, median],
                color=COLORS["ink"],
                linewidth=2.0,
                solid_capstyle="butt",
                zorder=2,
            )
            ax_b.scatter(
                [position + amount for amount in point_spread],
                values,
                s=24,
                linewidths=1.0,
                zorder=3,
                **marker_styles[config],
            )
            ax_b.text(
                position - 0.13 if config == "CONFIG-BASELINE" else position + 0.13,
                median,
                f"{median}",
                ha="right" if config == "CONFIG-BASELINE" else "left",
                va="center",
                fontsize=7.1,
                fontweight="bold",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.35, "alpha": 0.88},
                zorder=5,
            )

    ax_b.set_title("(b) Automated latency", loc="left", fontweight="bold", pad=8)
    ax_b.set_ylabel("Duration (ms)")
    ax_b.set_xticks(case_centers, ("High", "Low", "Threshold"))
    ax_b.set_xlim(-0.52, 2.52)
    ax_b.set_ylim(1700, 5850)
    ax_b.set_yticks((2000, 3000, 4000, 5000))
    ax_b.tick_params(axis="both", labelsize=7.7)
    ax_b.grid(axis="y", color="#D7DADD", linewidth=0.6, alpha=0.85)
    ax_b.set_axisbelow(True)
    ax_b.spines[["top", "right"]].set_visible(False)
    ax_b.text(
        0.99,
        0.985,
        "Five raw observations per cell\nhuman waiting excluded",
        transform=ax_b.transAxes,
        ha="right",
        va="top",
        fontsize=6.8,
        color=COLORS["muted"],
        linespacing=1.25,
    )

    fig.legend(
        handles=(
            Line2D([0], [0], marker="o", color="none", markerfacecolor="white", markeredgecolor=COLORS["line"], label="CONFIG-BASELINE"),
            Line2D([0], [0], marker="s", color="none", markerfacecolor=COLORS["blue"], markeredgecolor=COLORS["blue_dark"], label="CONFIG-OBID"),
            Line2D([0], [0], color=COLORS["ink"], linewidth=2.0, label="Median"),
        ),
        loc="lower center",
        bbox_to_anchor=(0.5, 0.005),
        ncols=3,
        frameon=False,
        handlelength=1.8,
        columnspacing=1.8,
        fontsize=7.7,
    )

    fig.subplots_adjust(left=0.105, right=0.985, bottom=0.165, top=0.90, wspace=0.31)
    save_figure(fig, output, "RQ3 reliability and automated latency results")


def main() -> None:
    configure_matplotlib()
    script_dir = Path(__file__).resolve().parent
    figure_dir = script_dir.parent
    repo_root = find_repo_root(script_dir)

    processed_dir = repo_root / "evaluation" / "results" / "step-10" / "processed"
    reliability_path = processed_dir / "rq3-reliability.csv"
    latency_path = processed_dir / "rq3-latency.csv"

    reliability_rows = read_csv(reliability_path, RELIABILITY_HEADERS, RELIABILITY_SHA256)
    latency_rows = read_csv(latency_path, LATENCY_HEADERS, LATENCY_SHA256)
    reliability = validate_reliability(reliability_rows)
    latency = validate_latency(latency_rows)

    outputs = {name: figure_dir / name for name in FIGURE_NAMES}
    generate_final_system_architecture(outputs["final-system-architecture.pdf"])
    generate_config_obid_pipeline(outputs["config-obid-pipeline.pdf"])
    generate_evaluation_evidence_flow(outputs["evaluation-evidence-flow.pdf"])
    generate_rq3_results(outputs["rq3-results.pdf"], reliability, latency)

    for name in FIGURE_NAMES:
        path = outputs[name]
        require(path.is_file() and path.stat().st_size > 0, f"Figure was not created: {name}")
        print(f"created {path.relative_to(repo_root).as_posix()}  sha256={sha256(path)}")


if __name__ == "__main__":
    main()
