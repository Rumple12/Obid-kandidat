"""Build the CONFIG-OBID n8n canvas composite used in Chapter 5."""

from __future__ import annotations

import hashlib
from pathlib import Path

from reportlab import rl_config
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


rl_config.useA85 = False

SOURCE_DIR = Path(__file__).resolve().parent
OUTPUT_PDF = SOURCE_DIR.parent / "config-obid-n8n-canvas.pdf"

PANELS = (
    (
        "config-obid-n8n-canvas-full.png",
        "5f46a3c7e46d82ce28532de986e055e469c30a7fd94334dbc7c6b74e0fb55632",
        "(a) Full caller canvas",
    ),
    (
        "config-obid-n8n-canvas-left.png",
        "6d755f4ac915a21c256cf47c971c757749110a1bb14f03d3f1d5e415223fc6e0",
        "(b) Input and cognitive decision region",
    ),
    (
        "config-obid-n8n-canvas-right.png",
        "d5b32a7cb2271daa103540a7b860a9311c04a6808f3c5ac311848d2ede05da95",
        "(c) Release-control and HITL region",
    ),
)


def verify_input(path: Path, expected_sha256: str) -> None:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected_sha256:
        raise ValueError(f"Unexpected screenshot content: {path.name}")


def image_size(path: Path) -> tuple[float, float]:
    width, height = ImageReader(str(path)).getSize()
    return float(width), float(height)


def draw_panel(
    pdf: canvas.Canvas,
    path: Path,
    label: str,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None:
    pdf.setFont("Helvetica-Bold", 7.6)
    pdf.setFillColor(HexColor("#202124"))
    pdf.drawString(x, y + height + 2.2 * mm, label)
    pdf.drawImage(
        str(path),
        x,
        y,
        width=width,
        height=height,
        preserveAspectRatio=True,
        anchor="c",
        mask="auto",
    )
    pdf.setStrokeColor(HexColor("#c8cdd3"))
    pdf.setLineWidth(0.35)
    pdf.rect(x, y, width, height, stroke=1, fill=0)


def build() -> None:
    paths = [SOURCE_DIR / filename for filename, _, _ in PANELS]
    for path, (_, expected_sha256, _) in zip(paths, PANELS, strict=True):
        verify_input(path, expected_sha256)

    full_w_px, full_h_px = image_size(paths[0])
    left_w_px, left_h_px = image_size(paths[1])
    right_w_px, right_h_px = image_size(paths[2])

    page_width = 180 * mm
    margin = 4 * mm
    label_space = 4 * mm
    section_gap = 2.5 * mm
    usable_width = page_width - 2 * margin

    full_width = usable_width
    full_height = full_width * full_h_px / full_w_px

    detail_width = 155 * mm
    left_height = detail_width * left_h_px / left_w_px
    right_height = detail_width * right_h_px / right_w_px

    right_y = margin
    left_y = right_y + right_height + label_space + section_gap
    full_y = left_y + left_height + label_space + section_gap
    page_height = full_y + full_height + label_space + margin

    pdf = canvas.Canvas(str(OUTPUT_PDF), pagesize=(page_width, page_height))
    pdf.setTitle("CONFIG-OBID n8n canvas")
    pdf.setSubject("Authoritative CONFIG-OBID caller canvas and two detail regions")
    pdf.setAuthor("Obid thesis project")

    draw_panel(
        pdf,
        paths[0],
        PANELS[0][2],
        margin,
        full_y,
        full_width,
        full_height,
    )
    draw_panel(
        pdf,
        paths[1],
        PANELS[1][2],
        margin,
        left_y,
        detail_width,
        left_height,
    )
    draw_panel(
        pdf,
        paths[2],
        PANELS[2][2],
        page_width - margin - detail_width,
        right_y,
        detail_width,
        right_height,
    )

    pdf.showPage()
    pdf.save()


if __name__ == "__main__":
    build()
