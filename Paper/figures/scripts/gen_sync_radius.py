#!/usr/bin/env python3
"""
Generate Fig5: Earth-synchronous radius correction
Shows how much the orbit radius shifts inward to achieve Earth-synchronous period
"""

import math

# SVG dimensions
WIDTH = 1020
HEIGHT = 620
MARGIN = 40

# Colors
BG_COLOR = "#08111f"
PANEL_BG = "#0d1828"
PANEL_STROKE = "#21374f"
CHART_BG = "#0a1320"
CHART_STROKE = "#173049"
GRID_COLOR = "#183147"
TEXT_PRIMARY = "#f3f6fb"
TEXT_SECONDARY = "#aebfd1"
TEXT_LABEL = "#b8c7d6"
TEXT_TITLE = "#eaf2fb"
TEXT_ANNOTATION = "#d9e5f0"
CURVE_COLOR = "#74d4c1"
POINT_COLOR = "#ffffff"
INTERP_BG = "#0e1b2c"
INTERP_STROKE = "#223a53"
BULLET_COLOR = "#74d4c1"

# Physical constants
AU_KM = 1.496e8  # 1 AU in km
SIGMA_STAR = 1.53  # g/m^2, characteristic areal density at 1 AU (P_rad / g_sun)


def beta_min(phi_deg):
    """Minimum lightness number for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    return (3 * math.sqrt(3) / 2) * math.sin(phi_rad)


def sync_radius_au(phi_deg):
    """
    Calculate the Earth-synchronous orbit radius in AU.
    For displaced orbit with light pressure, the effective gravity is reduced,
    so the synchronous radius is closer to the Sun.

    Returns radius in AU.
    """
    beta = beta_min(phi_deg)
    # For Earth-sync: r_sync = 1 AU * (1 - beta)^(1/3)
    r_sync_au = (1 - beta) ** (1 / 3)
    return r_sync_au


def linear_scale(val, val_min, val_max, out_min, out_max):
    """Map value (linear scale) to output coordinate"""
    if val_max == val_min:
        return (out_min + out_max) / 2
    t = (val - val_min) / (val_max - val_min)
    return out_min + t * (out_max - out_min)


def generate_svg():
    elements = []

    # Background
    elements.append(
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="{BG_COLOR}"/>'
    )

    # Title
    elements.append(
        f'<text x="{MARGIN}" y="48" fill="{TEXT_PRIMARY}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">Earth-Synchronous Orbit Radius</text>'
    )
    elements.append(
        f'<text x="{MARGIN}" y="78" fill="{TEXT_SECONDARY}" font-size="16" font-family="Arial, Helvetica, sans-serif">Orbit radius to achieve 1-year period with light pressure assist.</text>'
    )

    # Data range - focus on low latitude window (0 to 1 degree)
    phi_min, phi_max = 0, 1.0  # degrees
    highlight_phis = [0.1, 0.5, 1.0]

    # Chart panel
    chart_panel_x = 70
    chart_panel_y = 120
    chart_panel_w = 480
    chart_panel_h = 420

    elements.append(
        f'<rect x="{chart_panel_x}" y="{chart_panel_y}" width="{chart_panel_w}" height="{chart_panel_h}" rx="16" fill="{PANEL_BG}" stroke="{PANEL_STROKE}" stroke-width="1.5"/>'
    )

    # Chart title
    elements.append(
        f'<text x="{chart_panel_x + 24}" y="{chart_panel_y + 26}" fill="{TEXT_TITLE}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Synchronous orbit radius [AU]</text>'
    )

    # Chart area
    chart_margin_left = 70
    chart_margin_right = 30
    chart_margin_top = 50
    chart_margin_bottom = 70

    chart_x = chart_panel_x + chart_margin_left
    chart_y = chart_panel_y + chart_margin_top
    chart_w = chart_panel_w - chart_margin_left - chart_margin_right
    chart_h = chart_panel_h - chart_margin_top - chart_margin_bottom

    elements.append(
        f'<rect x="{chart_x}" y="{chart_y}" width="{chart_w}" height="{chart_h}" rx="8" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )

    # Y-axis range: show radius in AU, from ~0.98 to 1.0 to emphasize small change
    y_min = 0.98
    y_max = 1.00

    # Grid lines - horizontal
    y_ticks = [0.98, 0.985, 0.99, 0.995, 1.00]
    for tick in y_ticks:
        y_pos = linear_scale(tick, y_min, y_max, chart_y + chart_h, chart_y)
        elements.append(
            f'<line x1="{chart_x}" y1="{y_pos:.1f}" x2="{chart_x + chart_w}" y2="{y_pos:.1f}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{chart_x - 10}" y="{y_pos + 5:.1f}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{tick:.3f}</text>'
        )

    # Grid lines - vertical (linear scale from 0)
    x_ticks_phi = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    for phi in x_ticks_phi:
        x_pos = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        elements.append(
            f'<line x1="{x_pos:.1f}" y1="{chart_y}" x2="{x_pos:.1f}" y2="{chart_y + chart_h}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        label = f"{phi:.1f}" if phi > 0 else "0"
        elements.append(
            f'<text x="{x_pos:.1f}" y="{chart_y + chart_h + 20}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{label}</text>'
        )

    # X-axis label
    elements.append(
        f'<text x="{chart_x + chart_w / 2}" y="{chart_y + chart_h + 48}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Latitude φ [deg]</text>'
    )

    # Curve (linear interpolation from 0 to phi_max)
    points = []
    for i in range(201):
        phi = phi_max * (i / 200)  # linear from 0 to phi_max
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        r_au = sync_radius_au(phi)
        y = linear_scale(r_au, y_min, y_max, chart_y + chart_h, chart_y)
        # Clamp y to chart area
        y = max(chart_y, min(chart_y + chart_h, y))
        points.append(f"{x:.2f},{y:.2f}")

    elements.append(
        f'<polyline points="{" ".join(points)}" fill="none" stroke="{CURVE_COLOR}" stroke-width="2.5"/>'
    )

    # Highlight points
    for phi in highlight_phis:
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        r_au = sync_radius_au(phi)
        y = linear_scale(r_au, y_min, y_max, chart_y + chart_h, chart_y)
        y = max(chart_y, min(chart_y + chart_h, y))
        elements.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{POINT_COLOR}"/>'
        )
        # Position label to avoid overflow: for rightmost point, place label to the left
        if phi == highlight_phis[-1]:  # Last point (rightmost)
            label_x = x - 10
            anchor = "end"
        else:
            label_x = x + 10
            anchor = "start"
        elements.append(
            f'<text x="{label_x:.1f}" y="{y - 10:.1f}" fill="{TEXT_ANNOTATION}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="{anchor}">{phi}° → {r_au:.4f} AU</text>'
        )

    # Interpretation panel
    interp_x = 600
    interp_y = 120
    interp_w = 360
    interp_h = 420

    elements.append(
        f'<rect x="{interp_x}" y="{interp_y}" width="{interp_w}" height="{interp_h}" rx="18" fill="{INTERP_BG}" stroke="{INTERP_STROKE}" stroke-width="1.5"/>'
    )

    # Interpretation title
    elements.append(
        f'<text x="{interp_x + 24}" y="{interp_y + 38}" fill="{TEXT_PRIMARY}" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Reading the curve</text>'
    )

    # Bullet points with values
    bullet_y = interp_y + 80
    bullet_x = interp_x + 24
    bullet_spacing = 50

    for i, phi in enumerate(highlight_phis):
        r_au = sync_radius_au(phi)
        y = bullet_y + i * bullet_spacing
        elements.append(
            f'<circle cx="{bullet_x}" cy="{y - 5}" r="4.5" fill="{BULLET_COLOR}"/>'
        )
        elements.append(
            f'<text x="{bullet_x + 16}" y="{y}" fill="{TEXT_SECONDARY}" font-size="15" font-family="Arial, Helvetica, sans-serif">{phi}° → {r_au:.4f} AU</text>'
        )

    # Explanation
    explain_y = bullet_y + len(highlight_phis) * bullet_spacing + 30
    explanations = [
        "Light pressure reduces effective gravity",
        "Orbit moves slightly inward for 1-year period",
        "Change is small: &lt; 2% even at 1°",
        "σ_max curve remains unchanged",
    ]

    for i, text in enumerate(explanations):
        y = explain_y + i * 36
        elements.append(
            f'<circle cx="{bullet_x}" cy="{y - 5}" r="4.5" fill="{BULLET_COLOR}"/>'
        )
        elements.append(
            f'<text x="{bullet_x + 16}" y="{y}" fill="{TEXT_SECONDARY}" font-size="14" font-family="Arial, Helvetica, sans-serif">{text}</text>'
        )

    # Formula note
    formula_y = explain_y + len(explanations) * 36 + 30
    elements.append(
        f'<text x="{bullet_x}" y="{formula_y}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif">r_sync = 1 AU × (1 - β)^(1/3)</text>'
    )

    # Assemble SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">
{chr(10).join(elements)}
</svg>'''

    return svg


if __name__ == "__main__":
    svg_content = generate_svg()
    output_path = "../results/sync_radius.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")
