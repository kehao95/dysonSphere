#!/usr/bin/env python3
"""Generate manuscript figures as lightweight SVG assets.

This script avoids external plotting dependencies so the paper figures remain
reproducible in a minimal Python environment.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONCEPT = ROOT / "concept"
RESULTS = ROOT / "results"

SIGMA_STAR = 1.53
AU_KM = 149_597_870.7
EARTH_DIAMETER_KM = 12_742.0
EARTH_ANGULAR_DIAMETER_DEG = math.degrees(2.0 * math.atan(EARTH_DIAMETER_KM / (2.0 * AU_KM)))


def beta_min(phi_deg: float) -> float:
    return (3.0 * math.sqrt(3.0) / 2.0) * math.sin(math.radians(phi_deg))


def sigma_max(phi_deg: float) -> float:
    return SIGMA_STAR / beta_min(phi_deg)


def sync_radius_ratio(phi_deg: float) -> float:
    factor = 1.0 - math.sqrt(2.0) * math.tan(math.radians(phi_deg))
    return factor ** (1.0 / 3.0)


def svg_header(width: int, height: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" fill="none">\n'
    )


def svg_footer() -> str:
    return "</svg>\n"


def write_svg(path: Path, body: str, width: int, height: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg_header(width, height) + body + svg_footer())


def polyline(points: list[tuple[float, float]], color: str, width: float) -> str:
    pts = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return (
        f'<polyline points="{pts}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>\n'
    )


def circle(x: float, y: float, r: float, fill: str, stroke: str = "none", sw: float = 0.0) -> str:
    return (
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw:.2f}"/>\n'
    )


def line(x1: float, y1: float, x2: float, y2: float, color: str, width: float, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
        f'stroke="{color}" stroke-width="{width:.2f}"{dash_attr}/>\n'
    )


def text(x: float, y: float, content: str, size: int = 16, fill: str = "#e8eef7", anchor: str = "start",
         weight: str = "400") -> str:
    return (
        f'<text x="{x:.2f}" y="{y:.2f}" fill="{fill}" font-size="{size}" '
        f'font-family="Arial, Helvetica, sans-serif" font-weight="{weight}" '
        f'text-anchor="{anchor}">{content}</text>\n'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", sw: float = 0.0,
         rx: float = 0.0) -> str:
    return (
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx:.2f}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"/>\n'
    )


def generate_fig1_deadlock() -> None:
    width, height = 980, 560
    cx, cy = 330, 290
    orbit_r = 180
    body = ""
    body += rect(0, 0, width, height, "#08111f")
    body += text(40, 54, "Figure 1. Keplerian deadlock schematic", 28, "#f3f6fb", "start", "700")
    body += text(
        40,
        84,
        "All Keplerian orbital planes at fixed radius pass through the star, creating unavoidable nodal intersections.",
        16,
        "#aebfd1",
    )
    body += circle(cx, cy, 22, "#ffb65c")
    body += text(cx, cy + 50, "Star", 16, "#ffd49a", "middle", "700")

    body += circle(cx, cy, orbit_r, "none", "#3a6288", 2.0)
    body += circle(cx, cy, orbit_r, "none", "#6fd0c1", 2.0)
    body += line(cx - orbit_r, cy, cx + orbit_r, cy, "#6fd0c1", 2.0)
    body += line(cx, cy - orbit_r, cx, cy + orbit_r, "#e2b15d", 2.0)
    body += line(cx - 130, cy - 130, cx + 130, cy + 130, "#ffd36f", 2.0)
    body += line(cx - 130, cy + 130, cx + 130, cy - 130, "#ffd36f", 2.0)
    body += circle(cx, cy - orbit_r, 7, "#ff7b7b")
    body += circle(cx, cy + orbit_r, 7, "#ff7b7b")
    body += text(cx + 20, cy - orbit_r - 8, "Shared node", 15, "#ffb0b0")
    body += text(cx + 20, cy + orbit_r + 24, "Shared node", 15, "#ffb0b0")

    right_x = 600
    body += rect(right_x, 130, 320, 280, "#0e1b2c", "#223a53", 1.5, 18)
    bullets = [
        "Same heliocentric radius",
        "Different orbital planes",
        "All planes must cross the star",
        "Nodes cannot be eliminated geometrically",
        "Collision management worsens with density",
    ]
    body += text(right_x + 24, 170, "Implication for dense swarms", 22, "#f0f5fb", "start", "700")
    y = 210
    for item in bullets:
        body += circle(right_x + 30, y - 5, 4.5, "#74d4c1")
        body += text(right_x + 48, y, item, 17, "#c7d5e2")
        y += 38

    write_svg(CONCEPT / "fig1_keplerian_deadlock.svg", body, width, height)


def generate_fig2_stratified() -> None:
    width, height = 980, 560
    cx, cy = 300, 290
    body = ""
    body += rect(0, 0, width, height, "#08111f")
    body += text(40, 54, "Figure 2. MDDS low-latitude stratification concept", 28, "#f3f6fb", "start", "700")
    body += text(
        40,
        84,
        "Small off-plane displacements create separated latitude bands without requiring full radiative support.",
        16,
        "#aebfd1",
    )
    body += circle(cx, cy, 26, "#ffb65c")
    body += text(cx, cy + 54, "Star", 16, "#ffd49a", "middle", "700")

    for yoff, color, label in [(-68, "#ffd36f", "+phi band"), (0, "#6fd0c1", "Ecliptic seed"), (68, "#ffd36f", "-phi band")]:
        body += f'<ellipse cx="{cx}" cy="{cy + yoff}" rx="185" ry="46" fill="none" stroke="{color}" stroke-width="2.2"/>\n'
        for k in range(10):
            angle = (k / 10.0) * 2.0 * math.pi
            x = cx + 185 * math.cos(angle)
            y = cy + yoff + 46 * math.sin(angle)
            body += circle(x, y, 4.6, color)
        body += text(cx + 210, cy + yoff + 4, label, 16, color)

    body += line(cx + 210, cy - 68, cx + 210, cy + 68, "#95abc0", 1.5, "6 6")
    body += text(cx + 232, cy - 4, "Off-plane separation", 16, "#c7d5e2")

    right_x = 580
    body += rect(right_x, 120, 330, 300, "#0e1b2c", "#223a53", 1.5, 18)
    body += text(right_x + 24, 165, "Architecture intuition", 22, "#f0f5fb", "start", "700")
    bullets = [
        "Nodes remain primarily orbital",
        "SRP supplies only the off-plane component",
        "Bands share a common stellar axis",
        "Geometric layering replaces nodal crossing",
        "Low latitude is the natural first deployment region",
    ]
    y = 206
    for item in bullets:
        body += circle(right_x + 30, y - 5, 4.5, "#74d4c1")
        body += text(right_x + 48, y, item, 17, "#c7d5e2")
        y += 42

    write_svg(CONCEPT / "fig2_mdds_stratified_rings.svg", body, width, height)


def generate_fig3_support_curves() -> None:
    width, height = 1120, 580
    body = ""
    body += rect(0, 0, width, height, "#08111f")
    body += text(40, 48, "Figure 3. Latitude support curves", 28, "#f3f6fb", "start", "700")
    body += text(40, 78, "Left: beta_min(phi). Right: sigma_max(phi).", 16, "#aebfd1")

    panels = [
        {
            "x0": 60,
            "y0": 120,
            "w": 460,
            "h": 380,
            "title": "Required lightness number beta_min(phi)",
            "color": "#74d4c1",
            "x_min": 0.05,
            "x_max": 5.0,
            "y_max": 0.23,
            "ticks": [0.1, 0.5, 1.0, 2.0, 5.0],
            "series": beta_min,
        },
        {
            "x0": 600,
            "y0": 120,
            "w": 460,
            "h": 380,
            "title": "Low-latitude sigma_max(phi) [g/m^2]",
            "color": "#ffd36f",
            "x_min": 0.05,
            "x_max": 1.2,
            "y_max": 360.0,
            "ticks": [0.1, 0.5, 1.0],
            "series": sigma_max,
        },
    ]

    for idx, panel in enumerate(panels):
        x0 = panel["x0"]
        y0 = panel["y0"]
        w = panel["w"]
        h = panel["h"]
        title = panel["title"]
        color = panel["color"]
        x_min = panel["x_min"]
        x_max = panel["x_max"]
        y_max = panel["y_max"]
        x_ticks = panel["ticks"]
        phi_values = [x_min + i * ((x_max - x_min) / 240.0) for i in range(241)]
        values = [panel["series"](p) for p in phi_values]
        body += rect(x0, y0, w, h, "#0d1828", "#21374f", 1.5, 16)
        body += text(x0 + 18, y0 + 30, title, 18, "#eaf2fb", "start", "700")
        plot_x0 = x0 + 58
        plot_y0 = y0 + 48
        plot_w = w - 88
        plot_h = h - 88
        body += rect(plot_x0, plot_y0, plot_w, plot_h, "#0a1320", "#173049", 1.0, 8)
        pts = []
        for phi, val in zip(phi_values, values):
            px = plot_x0 + (phi - x_min) / (x_max - x_min) * plot_w
            py = plot_y0 + plot_h - (val / y_max) * plot_h
            pts.append((px, py))
        for frac in [0.0, 0.25, 0.5, 0.75, 1.0]:
            gy = plot_y0 + plot_h - frac * plot_h
            body += line(plot_x0, gy, plot_x0 + plot_w, gy, "#183147", 1.0, "4 6")
        for x_tick in x_ticks:
            gx = plot_x0 + (x_tick - x_min) / (x_max - x_min) * plot_w
            body += line(gx, plot_y0, gx, plot_y0 + plot_h, "#183147", 1.0, "4 6")
            body += text(gx, plot_y0 + plot_h + 24, f"{x_tick:g}", 14, "#b8c7d6", "middle")
        body += polyline(pts, color, 3.4)
        body += text(plot_x0 + plot_w / 2, y0 + h - 20, "Latitude phi [deg]", 14, "#b8c7d6", "middle")
        tick_labels = ["0", f"{y_max*0.25:.2f}" if idx == 0 else f"{y_max*0.25:.0f}",
                       f"{y_max*0.5:.2f}" if idx == 0 else f"{y_max*0.5:.0f}",
                       f"{y_max*0.75:.2f}" if idx == 0 else f"{y_max*0.75:.0f}",
                       f"{y_max:.2f}" if idx == 0 else f"{y_max:.0f}"]
        for frac, label in zip([0.0, 0.25, 0.5, 0.75, 1.0], tick_labels):
            ty = plot_y0 + plot_h - frac * plot_h + 5
            body += text(plot_x0 - 10, ty, label, 13, "#b8c7d6", "end")

    for phi, label in [(0.1, "0.1 deg"), (0.5, "0.5 deg"), (1.0, "1 deg")]:
        bx = 60 + 58 + (phi - 0.05) / (5.0 - 0.05) * (460 - 88)
        by = 120 + 48 + (460 - 88) - (beta_min(phi) / 0.23) * (380 - 88)
        body += circle(bx, by, 5.2, "#ffffff")
        body += text(bx + 10, by - 10, label, 13, "#d9e5f0")
        sx = 600 + 58 + (phi - 0.05) / (1.2 - 0.05) * (460 - 88)
        sy = 120 + 48 + (460 - 88) - (sigma_max(phi) / 360.0) * (380 - 88)
        body += circle(sx, sy, 5.2, "#ffffff")
        body += text(sx + 10, sy - 10, label, 13, "#d9e5f0")

    write_svg(RESULTS / "fig3_support_curves.svg", body, width, height)


def generate_fig4_low_latitude_window() -> None:
    width, height = 1020, 620
    body = ""
    body += rect(0, 0, width, height, "#08111f")
    body += text(40, 48, "Figure 4. Low-latitude illustrative window", 28, "#f3f6fb", "start", "700")
    body += text(40, 78, "Representative points at 0.1 deg, 0.5 deg, and 1 deg for the low-beta framework.", 16, "#aebfd1")

    x0, y0, w, h = 70, 120, 500, 420
    body += rect(x0, y0, w, h, "#0d1828", "#21374f", 1.5, 16)
    plot_x0 = x0 + 60
    plot_y0 = y0 + 44
    plot_w = w - 95
    plot_h = h - 84
    body += rect(plot_x0, plot_y0, plot_w, plot_h, "#0a1320", "#173049", 1.0, 8)

    x_ticks = [0.1, 0.5, 1.0]
    max_sigma = 360.0
    for frac in [0.0, 0.25, 0.5, 0.75, 1.0]:
        gy = plot_y0 + plot_h - frac * plot_h
        body += line(plot_x0, gy, plot_x0 + plot_w, gy, "#183147", 1.0, "4 6")
        label = f"{max_sigma*frac:.0f}"
        body += text(plot_x0 - 10, gy + 5, label, 13, "#b8c7d6", "end")

    for idx, phi in enumerate(x_ticks):
        gx = plot_x0 + idx * (plot_w / (len(x_ticks) - 1))
        body += line(gx, plot_y0, gx, plot_y0 + plot_h, "#183147", 1.0, "4 6")
        body += text(gx, plot_y0 + plot_h + 24, f"{phi:g}", 14, "#b8c7d6", "middle")
        sigma = sigma_max(phi)
        bar_top = plot_y0 + plot_h - (sigma / max_sigma) * plot_h
        body += rect(gx - 28, bar_top, 56, plot_y0 + plot_h - bar_top, "#74d4c1", "#9ae3d4", 1.0, 8)
        body += text(gx, bar_top - 10, f"{sigma:.1f}", 13, "#edf5fb", "middle", "700")
        body += text(gx, plot_y0 + plot_h + 44, "deg", 12, "#93a9bc", "middle")

    body += text(plot_x0 + plot_w / 2, y0 + h - 18, "Latitude phi [deg]", 14, "#b8c7d6", "middle")
    body += text(x0 + 24, y0 + 26, "Supportable areal density sigma_max [g/m^2]", 18, "#eaf2fb", "start", "700")

    rx, ry, rw, rh = 620, 120, 330, 420
    body += rect(rx, ry, rw, rh, "#0e1b2c", "#223a53", 1.5, 18)
    body += text(rx + 24, ry + 38, "Interpretation", 22, "#f0f5fb", "start", "700")
    points = [
        ("0.1 deg", "Entry-level low-latitude regime"),
        ("0.5 deg", "Still highly permissive"),
        ("1.0 deg", "Meaningful but tighter benchmark"),
        ("Trend", "Small-angle support scales roughly as 1/phi"),
    ]
    y = ry + 86
    for label, desc in points:
        body += text(rx + 24, y, label, 17, "#74d4c1", "start", "700")
        body += text(rx + 120, y, desc, 16, "#c7d5e2")
        y += 52
    body += text(rx + 24, ry + 286, "Representative ideal values", 18, "#f0f5fb", "start", "700")
    body += text(rx + 24, ry + 322, "0.1 deg: 337.4 g/m^2", 16, "#ffd36f")
    body += text(rx + 24, ry + 356, "0.5 deg: 67.5 g/m^2", 16, "#ffd36f")
    body += text(rx + 24, ry + 390, "1.0 deg: 33.8 g/m^2", 16, "#ffd36f")
    body += text(rx + 24, ry + 436, "0.1 deg is about 41 Earth radii", 15, "#9fe4d6")

    write_svg(RESULTS / "fig4_low_latitude_window.svg", body, width, height)


def generate_fig5_sync_radius() -> None:
    width, height = 1020, 620
    body = ""
    body += rect(0, 0, width, height, "#08111f")
    body += text(40, 48, "Figure 5. Earth-synchronous radius correction", 28, "#f3f6fb", "start", "700")
    body += text(40, 78, "The synchronization branch changes ring radius while leaving the support curve unchanged.", 16, "#aebfd1")

    x0, y0, w, h = 70, 120, 500, 420
    body += rect(x0, y0, w, h, "#0d1828", "#21374f", 1.5, 16)
    plot_x0 = x0 + 60
    plot_y0 = y0 + 44
    plot_w = w - 95
    plot_h = h - 84
    body += rect(plot_x0, plot_y0, plot_w, plot_h, "#0a1320", "#173049", 1.0, 8)

    phi_values = [0.05 + i * (1.15 / 240.0) for i in range(241)]
    values = [(1.0 - sync_radius_ratio(phi)) * AU_KM / 1e6 for phi in phi_values]
    y_max = 1.5
    for frac in [0.0, 0.25, 0.5, 0.75, 1.0]:
        gy = plot_y0 + plot_h - frac * plot_h
        body += line(plot_x0, gy, plot_x0 + plot_w, gy, "#183147", 1.0, "4 6")
        body += text(plot_x0 - 10, gy + 5, f"{y_max*frac:.1f}", 13, "#b8c7d6", "end")
    for x_tick in [0.1, 0.5, 1.0]:
        gx = plot_x0 + (x_tick - 0.05) / 1.15 * plot_w
        body += line(gx, plot_y0, gx, plot_y0 + plot_h, "#183147", 1.0, "4 6")
        body += text(gx, plot_y0 + plot_h + 24, f"{x_tick:g}", 14, "#b8c7d6", "middle")
    pts = []
    for phi, val in zip(phi_values, values):
        px = plot_x0 + (phi - 0.05) / 1.15 * plot_w
        py = plot_y0 + plot_h - (val / y_max) * plot_h
        pts.append((px, py))
    body += polyline(pts, "#ffcf76", 3.4)
    for phi in [0.1, 0.5, 1.0]:
        px = plot_x0 + (phi - 0.05) / 1.15 * plot_w
        val = (1.0 - sync_radius_ratio(phi)) * AU_KM / 1e6
        py = plot_y0 + plot_h - (val / y_max) * plot_h
        body += circle(px, py, 5.2, "#ffffff")
        body += text(px + 10, py - 10, f"{phi:g} deg", 13, "#d9e5f0")

    body += text(x0 + 24, y0 + 26, "Inward shift from 1 AU [million km]", 18, "#eaf2fb", "start", "700")
    body += text(plot_x0 + plot_w / 2, y0 + h - 18, "Latitude phi [deg]", 14, "#b8c7d6", "middle")

    rx, ry, rw, rh = 620, 120, 330, 420
    body += rect(rx, ry, rw, rh, "#0e1b2c", "#223a53", 1.5, 18)
    body += text(rx + 24, ry + 38, "Reading the branch", 22, "#f0f5fb", "start", "700")
    bullets = [
        "0.1 deg -> about 0.12 million km inward",
        "0.5 deg -> about 0.62 million km inward",
        "1.0 deg -> about 1.24 million km inward",
        "Support curve itself is unchanged",
        "Synchronization is an operational geometry choice",
    ]
    y = ry + 92
    for item in bullets:
        body += circle(rx + 28, y - 5, 4.5, "#74d4c1")
        body += text(rx + 44, y, item, 16, "#c7d5e2")
        y += 48

    write_svg(RESULTS / "fig5_sync_radius_shift.svg", body, width, height)


def main() -> None:
    generate_fig1_deadlock()
    generate_fig2_stratified()
    generate_fig3_support_curves()
    generate_fig4_low_latitude_window()
    generate_fig5_sync_radius()
    print("Generated figures in", ROOT)


if __name__ == "__main__":
    main()
