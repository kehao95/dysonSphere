#!/usr/bin/env python3
"""
Generate a blog-oriented panoramic infographic for the Dyson support continuum.

This is intentionally more visual than the manuscript figures. It highlights:
- θ⊕ as the Earth-radius entry point
- the approximate present lightweight-sail frontier around 0.1°–0.5°
- the β = 1 architecture threshold at ~22.6°
- the payload-optimized branch endpoint at ~35.3°
"""

from __future__ import annotations

import math
from pathlib import Path


WIDTH = 1440
HEIGHT = 900

BG = "#08111f"
PANEL = "#0d1828"
PANEL_STROKE = "#21374f"
TEXT = "#f3f6fb"
SUBTEXT = "#adc0d3"
MUTED = "#8fa3b7"
GRID = "#193249"

KEP = "#5fa8ff"
ENTRY = "#f4a259"
FRONTIER = "#74d4c1"
BUBBLE = "#ffd166"
TERMINUS = "#e76f51"
WHITE = "#ffffff"

AU_KM = 149_597_870.7
R_EARTH_KM = 6371.0
SIGMA_STAR = 1.53


def beta_min(phi_deg: float) -> float:
    return (3 * math.sqrt(3) / 2) * math.sin(math.radians(phi_deg))


def sigma_max(phi_deg: float) -> float:
    return SIGMA_STAR / beta_min(phi_deg)


def fmt_sigma(phi_deg: float) -> str:
    sigma = sigma_max(phi_deg)
    if sigma >= 1000:
        return f"{sigma / 1000:.2f} kg/m²"
    return f"{sigma:.1f} g/m²"


def scale(phi_deg: float, phi_max: float, x0: float, x1: float) -> float:
    phi_floor = 0.001
    num = math.log10(phi_deg / phi_floor + 1.0)
    den = math.log10(phi_max / phi_floor + 1.0)
    return x0 + (num / den) * (x1 - x0)


def t(x: float, y: float, text: str, size: int, color: str, weight: str = "400",
      anchor: str = "start") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{size}" '
        f'font-family="Arial, Helvetica, sans-serif" font-weight="{weight}" '
        f'text-anchor="{anchor}">{text}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str | None = None,
         sw: float = 1.0, rx: float = 14) -> str:
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" fill="{fill}"{stroke_attr}/>'
    )


def line(x1: float, y1: float, x2: float, y2: float, color: str,
         sw: float = 2.0, dash: str | None = None, opacity: float = 1.0) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{sw}" opacity="{opacity}"{dash_attr}/>'
    )


def circle(x: float, y: float, r: float, fill: str, stroke: str | None = None,
           sw: float = 1.5) -> str:
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}"{stroke_attr}/>'


def generate() -> str:
    phi_theta = math.degrees(math.atan(R_EARTH_KM / AU_KM))
    phi_beta1 = math.degrees(math.asin(2 / (3 * math.sqrt(3))))
    phi_terminus = math.degrees(math.atan(1 / math.sqrt(2)))

    phi_max = 36.0
    x0, x1 = 110, 1320
    y_band = 310
    band_h = 72

    x_theta = scale(phi_theta, phi_max, x0, x1)
    x_01 = scale(0.1, phi_max, x0, x1)
    x_05 = scale(0.5, phi_max, x0, x1)
    x_beta1 = scale(phi_beta1, phi_max, x0, x1)
    x_term = scale(phi_terminus, phi_max, x0, x1)

    parts: list[str] = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">')
    parts.append(rect(0, 0, WIDTH, HEIGHT, BG, rx=0))

    parts.append(t(70, 72, "Dyson Support Continuum", 34, TEXT, "700"))
    parts.append(t(70, 108, "A panoramic view from the Keplerian swarm limit to bubble-capable support", 18, SUBTEXT))
    parts.append(t(70, 136, "Key marked points: θ⊕ entry scale, 0.1°–0.5° current lightweight frontier, 22.6° bubble/statite entry, 35.3° branch endpoint", 15, MUTED))
    parts.append(t(70, 160, "Horizontal spacing is visually expanded near φ = 0 so the entry window remains legible.", 14, MUTED))

    # Main continuum panel
    parts.append(rect(60, 190, 1320, 280, PANEL, PANEL_STROKE, 1.5, 18))
    parts.append(t(90, 230, "Support-and-Stratification Spectrum", 20, TEXT, "700"))

    # Spectrum base
    parts.append(rect(x0, y_band, x1 - x0, band_h, "#0a1320", "#173049", 1.0, 18))
    parts.append(rect(x0, y_band, x_theta - x0, band_h, KEP, rx=18))
    parts.append(rect(x_theta, y_band, x_01 - x_theta, band_h, ENTRY, rx=0))
    parts.append(rect(x_01, y_band, x_05 - x_01, band_h, FRONTIER, rx=0))
    parts.append(rect(x_05, y_band, x_beta1 - x_05, band_h, "#2a9d8f", rx=0))
    parts.append(rect(x_beta1, y_band, x_term - x_beta1, band_h, BUBBLE, rx=0))
    parts.append(rect(x_term, y_band, x1 - x_term, band_h, TERMINUS, rx=18))

    parts.append(t(x0 + 18, y_band + 28, "Keplerian", 18, BG, "700"))
    parts.append(t(x0 + 18, y_band + 52, "pure orbital support", 14, BG))

    parts.append(t((x_theta + x_05) / 2, y_band + 28, "Low-β MDDS", 18, BG, "700", "middle"))
    parts.append(t((x_theta + x_05) / 2, y_band + 52, "entry and present frontier", 14, BG, "400", "middle"))

    parts.append(t((x_05 + x_beta1) / 2, y_band + 28, "Mixed-support expansion", 18, BG, "700", "middle"))
    parts.append(t((x_05 + x_beta1) / 2, y_band + 52, "harder but still orbital-radiative", 14, BG, "400", "middle"))

    parts.append(t((x_beta1 + x_term) / 2, y_band + 28, "Bubble-capable region", 18, BG, "700", "middle"))
    parts.append(t((x_beta1 + x_term) / 2, y_band + 52, "β ≥ 1 available", 14, BG, "400", "middle"))

    # Reference lines and labels
    for phi, label, color, y_text in [
        (phi_theta, "θ⊕\nEarth-radius scale", ENTRY, 270),
        (0.1, "0.1°", FRONTIER, 250),
        (0.5, "0.5°", FRONTIER, 250),
        (phi_beta1, "22.6°\nβ = 1", BUBBLE, 250),
        (phi_terminus, "35.3°\nν = 0", TERMINUS, 250),
    ]:
        x = scale(phi, phi_max, x0, x1)
        parts.append(line(x, 252, x, y_band + band_h + 120, color, 2.0, "6 6", 0.9))
        parts.append(circle(x, y_band + band_h / 2, 8, WHITE, color, 3))
        dy = 0
        for line_text in label.split("\n"):
            parts.append(t(x, y_text + dy, line_text, 15, color, "700", "middle"))
            dy += 18

    # Bracket for current frontier
    frontier_y = y_band + band_h + 76
    parts.append(line(x_01, frontier_y, x_05, frontier_y, FRONTIER, 4))
    parts.append(line(x_01, frontier_y - 10, x_01, frontier_y + 10, FRONTIER, 4))
    parts.append(line(x_05, frontier_y - 10, x_05, frontier_y + 10, FRONTIER, 4))
    parts.append(t((x_01 + x_05) / 2, frontier_y + 30, "Approximate present lightweight-sail frontier", 15, FRONTIER, "700", "middle"))
    parts.append(t((x_01 + x_05) / 2, frontier_y + 52, "roughly 0.1°–0.5° in the optimistic architecture sense", 13, SUBTEXT, "400", "middle"))

    # Bottom explanatory panels
    card_y = 520
    card_h = 300
    card_w = 392
    gap = 22
    card_xs = [60, 60 + card_w + gap, 60 + 2 * (card_w + gap)]

    # Card 1
    parts.append(rect(card_xs[0], card_y, card_w, card_h, PANEL, PANEL_STROKE, 1.5, 18))
    parts.append(t(card_xs[0] + 24, card_y + 34, "① Entry Point: θ⊕", 22, ENTRY, "700"))
    parts.append(t(card_xs[0] + 24, card_y + 68, "Take the angular radius of Earth as seen from the Sun.", 15, SUBTEXT))
    parts.append(t(card_xs[0] + 24, card_y + 102, f"φ ≈ {phi_theta:.5f}°", 18, TEXT, "700"))
    parts.append(t(card_xs[0] + 24, card_y + 130, f"β_min ≈ {beta_min(phi_theta):.2e}", 16, TEXT))
    parts.append(t(card_xs[0] + 24, card_y + 158, f"σ_max ≈ {fmt_sigma(phi_theta)}", 16, TEXT))
    parts.append(t(card_xs[0] + 24, card_y + 194, "Geometric meaning: about one Earth radius", 15, SUBTEXT))
    parts.append(t(card_xs[0] + 24, card_y + 220, "of off-plane separation at 1 AU.", 15, SUBTEXT))
    parts.append(t(card_xs[0] + 24, card_y + 258, "This is the point where the continuum starts to", 15, MUTED))
    parts.append(t(card_xs[0] + 24, card_y + 282, "feel near-entry rather than purely futuristic.", 15, MUTED))

    # Card 2
    parts.append(rect(card_xs[1], card_y, card_w, card_h, PANEL, PANEL_STROKE, 1.5, 18))
    parts.append(t(card_xs[1] + 24, card_y + 34, "② Present Human Frontier", 22, FRONTIER, "700"))
    parts.append(t(card_xs[1] + 24, card_y + 68, "A useful rough bracket for lightweight sailcraft-style", 15, SUBTEXT))
    parts.append(t(card_xs[1] + 24, card_y + 92, "systems is around 0.1°–0.5° in this framework.", 15, SUBTEXT))
    parts.append(t(card_xs[1] + 24, card_y + 130, f"0.1°  →  σ_max ≈ {fmt_sigma(0.1)}", 17, TEXT, "700"))
    parts.append(t(card_xs[1] + 24, card_y + 158, f"0.5°  →  σ_max ≈ {fmt_sigma(0.5)}", 17, TEXT, "700"))
    parts.append(t(card_xs[1] + 24, card_y + 194, "This is not a claim that full MDDS is solved today.", 15, MUTED))
    parts.append(t(card_xs[1] + 24, card_y + 218, "It is a claim that the low-angle part of the spectrum", 15, MUTED))
    parts.append(t(card_xs[1] + 24, card_y + 242, "already overlaps plausible human lightweight-spacecraft", 15, MUTED))
    parts.append(t(card_xs[1] + 24, card_y + 266, "mass-per-area scales.", 15, MUTED))

    # Card 3
    parts.append(rect(card_xs[2], card_y, card_w, card_h, PANEL, PANEL_STROKE, 1.5, 18))
    parts.append(t(card_xs[2] + 24, card_y + 34, "③ Bubble Threshold", 22, BUBBLE, "700"))
    parts.append(t(card_xs[2] + 24, card_y + 68, "At φ ≈ 22.6°, β reaches 1.", 15, SUBTEXT))
    parts.append(t(card_xs[2] + 24, card_y + 102, "This is where bubble/statite-like architectures", 15, SUBTEXT))
    parts.append(t(card_xs[2] + 24, card_y + 126, "enter the admissible design space.", 15, SUBTEXT))
    parts.append(t(card_xs[2] + 24, card_y + 162, "Important nuance:", 17, TEXT, "700"))
    parts.append(t(card_xs[2] + 24, card_y + 190, "this is not the end of the whole continuum.", 15, MUTED))
    parts.append(t(card_xs[2] + 24, card_y + 214, "It is the point where purely radiative-support", 15, MUTED))
    parts.append(t(card_xs[2] + 24, card_y + 238, "architectures become available as an option.", 15, MUTED))
    parts.append(t(card_xs[2] + 24, card_y + 274, f"The current payload-optimized branch ends later, at about {phi_terminus:.1f}°.", 15, MUTED))

    parts.append(t(720, 870, "Micro-Displaced Dyson Swarm (MDDS): not a single object, but a low-β working segment inside a continuous Dyson support spectrum.", 16, SUBTEXT, "400", "middle"))
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "results" / "blog_dyson_panorama.svg"
    out.write_text(generate(), encoding="utf-8")
    print(f"Generated {out}")


if __name__ == "__main__":
    main()
