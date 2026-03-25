#!/usr/bin/env python3
"""
Generate a blog-facing Dyson fan concept figure.

Requirements:
- no visual expansion of the angular axis
- literal 0°–90° fan
- Sun on the left
- Dyson support spectrum unfolded to the right as a sector
- key points called out with labels:
  θ⊕, 0.1°, 0.5°, 22.6°, 35.3°, 90°
"""

from __future__ import annotations

import math
from pathlib import Path


WIDTH = 1600
HEIGHT = 960

BG = "#08111f"
TEXT = "#f3f6fb"
SUBTEXT = "#adc0d3"
MUTED = "#8fa3b7"
WHITE = "#ffffff"

SUN = "#ffb65c"
SUN_GLOW = "#ffcf8b"
PANEL = "#0d1828"
PANEL_STROKE = "#21374f"

KEP = "#5fa8ff"
ENTRY = "#f4a259"
FRONTIER = "#74d4c1"
MID = "#2a9d8f"
BUBBLE = "#ffd166"
TERM = "#e76f51"
POLAR = "#b48cff"

AU_KM = 149_597_870.7
R_EARTH_KM = 6371.0
SIGMA_STAR = 1.53


def theta_earth_deg() -> float:
    return math.degrees(math.atan(R_EARTH_KM / AU_KM))


def beta_min(phi_deg: float) -> float:
    return (3 * math.sqrt(3) / 2) * math.sin(math.radians(phi_deg))


def sigma_max(phi_deg: float) -> float:
    return SIGMA_STAR / beta_min(phi_deg)


def fmt_sigma(phi_deg: float) -> str:
    sigma = sigma_max(phi_deg)
    if sigma >= 1000:
        return f"{sigma / 1000:.2f} kg/m²"
    return f"{sigma:.1f} g/m²"


def t(x: float, y: float, text: str, size: int, color: str, weight: str = "400",
      anchor: str = "start") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{size}" '
        f'font-family="Arial, Helvetica, sans-serif" font-weight="{weight}" '
        f'text-anchor="{anchor}">{text}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str | None = None,
         sw: float = 1.0, rx: float = 14, opacity: float = 1.0) -> str:
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" fill="{fill}" opacity="{opacity}"{stroke_attr}/>'
    )


def line(x1: float, y1: float, x2: float, y2: float, color: str,
         sw: float = 2.0, dash: str | None = None, opacity: float = 1.0) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{sw}" opacity="{opacity}"{dash_attr}/>'
    )


def circle(x: float, y: float, r: float, fill: str, stroke: str | None = None,
           sw: float = 1.5, opacity: float = 1.0) -> str:
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return (
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" '
        f'opacity="{opacity}"{stroke_attr}/>'
    )


def sector_path(cx: float, cy: float, r_inner: float, r_outer: float,
                a0_deg: float, a1_deg: float) -> str:
    a0 = math.radians(a0_deg)
    a1 = math.radians(a1_deg)
    x0o = cx + r_outer * math.cos(a0)
    y0o = cy - r_outer * math.sin(a0)
    x1o = cx + r_outer * math.cos(a1)
    y1o = cy - r_outer * math.sin(a1)
    x1i = cx + r_inner * math.cos(a1)
    y1i = cy - r_inner * math.sin(a1)
    x0i = cx + r_inner * math.cos(a0)
    y0i = cy - r_inner * math.sin(a0)
    return (
        f"M {x0o:.1f} {y0o:.1f} "
        f"A {r_outer:.1f} {r_outer:.1f} 0 0 0 {x1o:.1f} {y1o:.1f} "
        f"L {x1i:.1f} {y1i:.1f} "
        f"A {r_inner:.1f} {r_inner:.1f} 0 0 1 {x0i:.1f} {y0i:.1f} Z"
    )


def ray_point(cx: float, cy: float, r: float, ang_deg: float) -> tuple[float, float]:
    a = math.radians(ang_deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def generate() -> str:
    phi_theta = theta_earth_deg()
    phi_beta1 = math.degrees(math.asin(2 / (3 * math.sqrt(3))))
    phi_term = math.degrees(math.atan(1 / math.sqrt(2)))

    cx, cy = 230, 820
    r_inner = 170
    r_outer = 760

    parts: list[str] = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">')
    parts.append(rect(0, 0, WIDTH, HEIGHT, BG, rx=0))

    parts.append(t(60, 68, "Dyson Architecture Fan", 34, TEXT, "700"))
    parts.append(t(60, 104, "Literal 0°–90° support spectrum with key architectural thresholds", 18, SUBTEXT))
    parts.append(t(60, 132, "Small angles are not visually expanded. Entry-level points are indicated by callouts rather than magnified wedges.", 14, MUTED))

    # Sun
    parts.append(circle(cx, cy, 86, SUN_GLOW, opacity=0.16))
    parts.append(circle(cx, cy, 62, SUN_GLOW, opacity=0.26))
    parts.append(circle(cx, cy, 40, SUN, stroke="#ffd49a", sw=2))
    parts.append(t(cx, cy + 98, "Sun", 18, "#ffd49a", "700", "middle"))

    # Fan background
    parts.append(rect(340, 120, 1210, 780, PANEL, PANEL_STROKE, 1.5, 18, 0.42))

    # Main sector regions
    sectors = [
        (0.0, 0.5, ENTRY, "entry-scale"),
        (0.5, phi_beta1, MID, "mixed-support MDDS"),
        (phi_beta1, phi_term, BUBBLE, "bubble-capable"),
        (phi_term, 90.0, POLAR, "high-latitude radiative-support continuum"),
    ]
    for a0, a1, color, _ in sectors:
        parts.append(
            f'<path d="{sector_path(cx, cy, r_inner, r_outer, a0, a1)}" fill="{color}" opacity="0.82"/>'
        )

    # Guide arcs
    for r, op in [(260, 0.16), (430, 0.13), (600, 0.10)]:
        x0, y0 = ray_point(cx, cy, r, 0)
        x1, y1 = ray_point(cx, cy, r, 90)
        parts.append(
            f'<path d="M {x0:.1f} {y0:.1f} A {r:.1f} {r:.1f} 0 0 0 {x1:.1f} {y1:.1f}" stroke="{WHITE}" stroke-width="1" opacity="{op}" fill="none" stroke-dasharray="5 6"/>'
        )

    # Anchor rays
    key_rays = [
        (0.0, KEP, "0°", "Keplerian swarm limit"),
        (phi_theta, ENTRY, "θ⊕", "Earth-radius entry scale"),
        (0.1, FRONTIER, "0.1°", None),
        (0.5, FRONTIER, "0.5°", None),
        (phi_beta1, BUBBLE, "22.6°", "β = 1 : bubble/statite entry"),
        (phi_term, TERM, "35.3°", "ν = 0 : branch endpoint"),
        (90.0, POLAR, "90°", "formal polar radiative-support endpoint"),
    ]

    label_positions = {
        "0°": (1024, 820, "start"),
        "θ⊕": (944, 772, "start"),
        "22.6°": (944, 500, "start"),
        "35.3°": (880, 338, "start"),
        "90°": (320, 172, "middle"),
    }

    for ang, color, title, subtitle in key_rays:
        x1, y1 = ray_point(cx, cy, r_outer, ang)
        parts.append(line(cx, cy, x1, y1, color, 2.4, "8 7", 0.95))
        parts.append(circle(x1, y1, 6, WHITE, color, 2.5))
        if subtitle is not None:
            if title in label_positions:
                lx, ly, anchor = label_positions[title]
            else:
                lx, ly = ray_point(cx, cy, r_outer + 34, ang)
                anchor = "start"
            parts.append(t(lx, ly, title, 18, color, "700", anchor))
            parts.append(t(lx, ly + 24, subtitle, 14, SUBTEXT, "400", anchor))

    # Current frontier bracket on the arc
    x01, y01 = ray_point(cx, cy, 635, 0.1)
    x05, y05 = ray_point(cx, cy, 635, 0.5)
    parts.append(line(x01, y01, x05, y05, FRONTIER, 8, opacity=0.95))
    parts.append(t(760, 272, "Approximate present human lightweight-sail frontier", 17, FRONTIER, "700"))
    parts.append(t(760, 298, "roughly 0.1°–0.5° in the optimistic architecture sense", 14, SUBTEXT))

    # Region labels
    region_labels = [
        (12, 470, "Low-β MDDS", BG),
        (30, 560, "Support-assisted", BG),
        (30, 590, "stratified swarm", BG),
        (55, 610, "Bubble-capable", BG),
        (55, 640, "support region", BG),
        (79, 540, "Beyond the current", BG),
        (79, 570, "payload-optimized", BG),
        (79, 600, "branch", BG),
    ]
    for ang, radius, text, color in region_labels:
        x, y = ray_point(cx, cy, radius, ang)
        parts.append(t(x, y, text, 22, color, "700", "middle"))

    # Callout panel for tiny low-angle markers
    parts.append(rect(1040, 150, 430, 280, "#0e1b2c", "#223a53", 1.5, 18))
    parts.append(t(1070, 190, "Low-angle callouts", 24, TEXT, "700"))

    callouts = [
        (ENTRY, "θ⊕ ≈ 0.00244°", f"β_min ≈ {beta_min(phi_theta):.2e}; σ_max ≈ {fmt_sigma(phi_theta)}"),
        (FRONTIER, "0.1°", f"σ_max ≈ {fmt_sigma(0.1)}"),
        (FRONTIER, "0.5°", f"σ_max ≈ {fmt_sigma(0.5)}"),
    ]
    y = 232
    for color, head, body in callouts:
        parts.append(circle(1086, y - 5, 5, color))
        parts.append(t(1102, y, head, 18, color, "700"))
        parts.append(t(1210, y, body, 15, SUBTEXT))
        y += 52

    parts.append(t(1070, 386, "These points are physically tiny in angle, so the fan does not magnify them.", 15, MUTED))
    parts.append(t(1070, 412, "Their importance comes from the mass-per-area threshold, not from visual width.", 15, MUTED))

    parts.append(t(800, 916, "MDDS is the low-β, low-latitude working segment inside a broader Dyson support continuum.", 18, SUBTEXT, "400", "middle"))
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "results" / "blog_dyson_fan.svg"
    out.write_text(generate(), encoding="utf-8")
    print(f"Generated {out}")


if __name__ == "__main__":
    main()
