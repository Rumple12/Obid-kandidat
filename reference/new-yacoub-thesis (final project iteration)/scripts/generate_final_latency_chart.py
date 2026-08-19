from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "thesis"
    / "MiunThesisTemplate-master"
    / "MiunThesisTemplate-master"
    / "Figures"
    / "final-workflow-latency-summary.png"
)

LABELS = [
    "Local det. high",
    "Local det. low",
    "Local agent high",
    "Local agent low",
    "Pi high",
    "Pi low",
]

LATENCY_MS = [480, 177, 2670, 2000, 437, 200]

COLORS = [
    "#4C78A8",
    "#4C78A8",
    "#F58518",
    "#F58518",
    "#54A24B",
    "#54A24B",
]


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    positions = range(len(LABELS))
    bars = ax.barh(positions, LATENCY_MS, color=COLORS, height=0.62)

    ax.set_yticks(list(positions), labels=LABELS)
    ax.invert_yaxis()
    ax.set_xlabel("Approx. latency (ms)")
    ax.set_title("Final workflow latency observations", pad=12, weight="bold")
    ax.grid(axis="x", color="#d9d9d9", linewidth=0.8, alpha=0.85)
    ax.set_axisbelow(True)

    xmax = max(LATENCY_MS) * 1.18
    ax.set_xlim(0, xmax)
    for bar, value in zip(bars, LATENCY_MS):
        ax.text(
            value + max(LATENCY_MS) * 0.025,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,} ms",
            va="center",
            fontsize=9,
        )



    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUTPUT, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
