#!/usr/bin/env python3
"""
Generate Fig4: Low-latitude illustrative window
Bar chart showing sigma_max values at representative latitudes (0.1°, 0.5°, 1°)
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
BAR_COLOR = "#74d4c1"
BAR_STROKE = "#9ae3d4"
HIGHLIGHT_COLOR = "#ffd36f"
INTERP_BG = "#0e1b2c"
INTERP_STROKE = "#223a53"

# Physical constants
SIGMA_STAR = 1.53  # g/m^2, characteristic areal density at 1 AU (P_rad / g_sun)
AU_KM = 1.496e8  # km
R_EARTH_KM = 6371  # km


def sigma_max(phi_deg):
    """Maximum supportable areal density [g/m^2] for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    if phi_rad < 1e-10:
        return float("inf")
    return (2 * SIGMA_STAR) / (3 * math.sqrt(3) * math.sin(phi_rad))


def generate_svg():
    elements = []

    # Background
    elements.append(
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="{BG_COLOR}"/>'
    )

    # Title
    elements.append(
        f'<text x="{MARGIN}" y="48" fill="{TEXT_PRIMARY}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">Figure 4. Low-latitude window: supportable mass</text>'
    )
    elements.append(
        f'<text x="{MARGIN}" y="78" fill="{TEXT_SECONDARY}" font-size="16" font-family="Arial, Helvetica, sans-serif">Representative points at 0.1°, 0.5°, and 1° for the low-β framework.</text>'
    )

    # Data
    phis = [0.1, 0.5, 1.0]
    sigmas = [sigma_max(phi) for phi in phis]

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
        f'<text x="{chart_panel_x + 24}" y="{chart_panel_y + 26}" fill="{TEXT_TITLE}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Supportable areal density σ_max [g/m²]</text>'
    )

    # Chart area
    chart_margin_left = 70
    chart_margin_right = 40
    chart_margin_top = 50
    chart_margin_bottom = 70

    chart_x = chart_panel_x + chart_margin_left
    chart_y = chart_panel_y + chart_margin_top
    chart_w = chart_panel_w - chart_margin_left - chart_margin_right
    chart_h = chart_panel_h - chart_margin_top - chart_margin_bottom

    elements.append(
        f'<rect x="{chart_x}" y="{chart_y}" width="{chart_w}" height="{chart_h}" rx="8" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )

    # Y-axis range
    y_max = 400  # g/m^2 - enough to show all bars
    y_min = 0

    # Grid lines - horizontal
    y_ticks = [0, 100, 200, 300, 400]
    for tick in y_ticks:
        y_pos = chart_y + chart_h - (tick / y_max) * chart_h
        elements.append(
            f'<line x1="{chart_x}" y1="{y_pos:.1f}" x2="{chart_x + chart_w}" y2="{y_pos:.1f}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{chart_x - 10}" y="{y_pos + 5:.1f}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{tick}</text>'
        )

    # Bar chart
    bar_width = 60
    bar_spacing = (chart_w - len(phis) * bar_width) / (len(phis) + 1)

    for i, (phi, sigma) in enumerate(zip(phis, sigmas)):
        bar_x = chart_x + bar_spacing * (i + 1) + bar_width * i

        # Clamp sigma for display (cap at y_max for bar height, but show real value)
        sigma_display = min(sigma, y_max)
        bar_height = (sigma_display / y_max) * chart_h
        bar_y = chart_y + chart_h - bar_height

        # Draw bar
        elements.append(
            f'<rect x="{bar_x:.1f}" y="{bar_y:.1f}" width="{bar_width}" height="{bar_height:.1f}" rx="8" fill="{BAR_COLOR}" stroke="{BAR_STROKE}" stroke-width="1"/>'
        )

        # Value label above bar
        label_y = bar_y - 10
        elements.append(
            f'<text x="{bar_x + bar_width / 2:.1f}" y="{label_y:.1f}" fill="{TEXT_TITLE}" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="700" text-anchor="middle">{sigma:.1f}</text>'
        )

        # X-axis label
        elements.append(
            f'<text x="{bar_x + bar_width / 2:.1f}" y="{chart_y + chart_h + 25}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{phi}°</text>'
        )

    # X-axis title
    elements.append(
        f'<text x="{chart_x + chart_w / 2}" y="{chart_y + chart_h + 50}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Latitude φ</text>'
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
        f'<text x="{interp_x + 24}" y="{interp_y + 38}" fill="{TEXT_PRIMARY}" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Interpretation</text>'
    )

    # Bullet points
    bullet_start_y = interp_y + 80
    bullet_spacing = 48
    bullet_x = interp_x + 24

    interpretations = [
        ("0.1°", "Entry-level low-latitude regime"),
        ("0.5°", "Still highly permissive"),
        ("1.0°", "Meaningful but tighter benchmark"),
    ]

    for i, (label, desc) in enumerate(interpretations):
        y = bullet_start_y + i * bullet_spacing
        elements.append(
            f'<text x="{bullet_x}" y="{y}" fill="{BAR_COLOR}" font-size="17" font-family="Arial, Helvetica, sans-serif" font-weight="700">{label}</text>'
        )
        elements.append(
            f'<text x="{bullet_x + 60}" y="{y}" fill="{TEXT_SECONDARY}" font-size="15" font-family="Arial, Helvetica, sans-serif">{desc}</text>'
        )

    # Trend note
    trend_y = bullet_start_y + len(interpretations) * bullet_spacing + 20
    elements.append(
        f'<text x="{bullet_x}" y="{trend_y}" fill="{BAR_COLOR}" font-size="17" font-family="Arial, Helvetica, sans-serif" font-weight="700">Trend</text>'
    )
    elements.append(
        f'<text x="{bullet_x + 60}" y="{trend_y}" fill="{TEXT_SECONDARY}" font-size="15" font-family="Arial, Helvetica, sans-serif">σ_max ∝ 1/sin(φ) ≈ 1/φ for small φ</text>'
    )

    # Representative values section
    values_y = trend_y + 50
    elements.append(
        f'<text x="{bullet_x}" y="{values_y}" fill="{TEXT_PRIMARY}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Representative ideal values</text>'
    )

    for i, (phi, sigma) in enumerate(zip(phis, sigmas)):
        y = values_y + 32 + i * 28
        elements.append(
            f'<text x="{bullet_x}" y="{y}" fill="{HIGHLIGHT_COLOR}" font-size="15" font-family="Arial, Helvetica, sans-serif">{phi}°: {sigma:.1f} g/m²</text>'
        )

    # Physical scale note
    scale_y = values_y + 32 + len(phis) * 28 + 20
    phi_01_km = AU_KM * math.sin(math.radians(0.1))
    earth_radii = phi_01_km / R_EARTH_KM
    elements.append(
        f'<text x="{bullet_x}" y="{scale_y}" fill="#9fe4d6" font-size="14" font-family="Arial, Helvetica, sans-serif">0.1° offset ≈ {phi_01_km / 1e6:.2f} million km ≈ {earth_radii:.0f} Earth radii</text>'
    )

    # Assemble SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">
{chr(10).join(elements)}
</svg>'''

    return svg


if __name__ == "__main__":
    svg_content = generate_svg()
    output_path = "../results/low_latitude_window.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")
