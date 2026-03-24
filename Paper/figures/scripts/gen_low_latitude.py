#!/usr/bin/env python3
"""
Generate Fig4: Low-latitude illustrative window
Bar chart showing sigma_max values at representative latitudes (θ⊕, 0.1°, 0.5°, 1°)
Uses log scale to accommodate the wide range of values.
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
THETA_EARTH_COLOR = "#f4a259"  # Orange for θ⊕
THETA_EARTH_STROKE = "#f7c08a"
HIGHLIGHT_COLOR = "#ffd36f"
INTERP_BG = "#0e1b2c"
INTERP_STROKE = "#223a53"

# Physical constants
SIGMA_STAR = 1.53  # g/m^2, characteristic areal density at 1 AU (P_rad / g_sun)
AU_KM = 1.496e8  # km
R_EARTH_KM = 6371  # km
THETA_EARTH_DEG = math.degrees(math.atan(R_EARTH_KM / AU_KM))  # ≈ 0.00244°


def sigma_max(phi_deg):
    """Maximum supportable areal density [g/m^2] for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    if phi_rad < 1e-10:
        return float("inf")
    return (2 * SIGMA_STAR) / (3 * math.sqrt(3) * math.sin(phi_rad))


def log_scale(val, val_min, val_max, out_min, out_max):
    """Map value (log scale) to output coordinate"""
    if val <= 0 or val_min <= 0 or val_max <= 0:
        return out_min
    log_val = math.log10(val)
    log_min = math.log10(val_min)
    log_max = math.log10(val_max)
    if log_max == log_min:
        return (out_min + out_max) / 2
    t = (log_val - log_min) / (log_max - log_min)
    return out_min + t * (out_max - out_min)


def generate_svg():
    elements = []

    # Background
    elements.append(
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="{BG_COLOR}"/>'
    )

    # Title
    elements.append(
        f'<text x="{MARGIN}" y="48" fill="{TEXT_PRIMARY}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">Low-Latitude Window: Supportable Mass</text>'
    )
    elements.append(
        f'<text x="{MARGIN}" y="78" fill="{TEXT_SECONDARY}" font-size="16" font-family="Arial, Helvetica, sans-serif">Representative points from θ⊕ to 1° (log scale)</text>'
    )

    # Data - include theta_earth
    phi_labels = ["θ⊕", "0.1°", "0.5°", "1°"]
    phis = [THETA_EARTH_DEG, 0.1, 0.5, 1.0]
    sigmas = [sigma_max(phi) for phi in phis]
    is_theta_earth = [True, False, False, False]

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
        f'<text x="{chart_panel_x + 24}" y="{chart_panel_y + 26}" fill="{TEXT_TITLE}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Supportable areal density σ_max (log scale)</text>'
    )

    # Chart area
    chart_margin_left = 80
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

    # Y-axis range (log scale)
    y_min = 10  # g/m^2
    y_max = 20000  # g/m^2

    # Grid lines - horizontal (log scale)
    y_ticks = [10, 100, 1000, 10000]
    for tick in y_ticks:
        y_pos = chart_y + chart_h - log_scale(tick, y_min, y_max, 0, chart_h)
        elements.append(
            f'<line x1="{chart_x}" y1="{y_pos:.1f}" x2="{chart_x + chart_w}" y2="{y_pos:.1f}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        # Format label
        if tick >= 1000:
            label = f"{tick // 1000}k"
        else:
            label = str(tick)
        elements.append(
            f'<text x="{chart_x - 10}" y="{y_pos + 5:.1f}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{label}</text>'
        )

    # Y-axis unit label
    elements.append(
        f'<text x="{chart_x - 55}" y="{chart_y + chart_h / 2}" fill="{TEXT_LABEL}" font-size="12" font-family="Arial, Helvetica, sans-serif" text-anchor="middle" transform="rotate(-90, {chart_x - 55}, {chart_y + chart_h / 2})">[g/m²]</text>'
    )

    # Bar chart
    bar_width = 55
    bar_spacing = (chart_w - len(phis) * bar_width) / (len(phis) + 1)

    for i, (phi_label, phi, sigma, is_te) in enumerate(
        zip(phi_labels, phis, sigmas, is_theta_earth)
    ):
        bar_x = chart_x + bar_spacing * (i + 1) + bar_width * i

        # Log scale for bar height
        bar_height = log_scale(sigma, y_min, y_max, 0, chart_h)
        bar_y = chart_y + chart_h - bar_height

        # Choose color based on whether it's theta_earth
        color = THETA_EARTH_COLOR if is_te else BAR_COLOR
        stroke = THETA_EARTH_STROKE if is_te else BAR_STROKE

        # Draw bar
        elements.append(
            f'<rect x="{bar_x:.1f}" y="{bar_y:.1f}" width="{bar_width}" height="{bar_height:.1f}" rx="8" fill="{color}" stroke="{stroke}" stroke-width="1"/>'
        )

        # Value label above bar
        label_y = bar_y - 10
        # Format value
        if sigma >= 1000:
            value_str = f"{sigma / 1000:.2f} kg/m²"
        else:
            value_str = f"{sigma:.1f} g/m²"
        elements.append(
            f'<text x="{bar_x + bar_width / 2:.1f}" y="{label_y:.1f}" fill="{TEXT_TITLE}" font-size="12" font-family="Arial, Helvetica, sans-serif" font-weight="700" text-anchor="middle">{value_str}</text>'
        )

        # X-axis label
        elements.append(
            f'<text x="{bar_x + bar_width / 2:.1f}" y="{chart_y + chart_h + 25}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{phi_label}</text>'
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
    bullet_start_y = interp_y + 75
    bullet_spacing = 42
    bullet_x = interp_x + 24

    interpretations = [
        ("θ⊕", "Earth angular radius (~0.00244°)", THETA_EARTH_COLOR),
        ("0.1°", "Entry-level low-latitude regime", BAR_COLOR),
        ("0.5°", "Still highly permissive", BAR_COLOR),
        ("1.0°", "Meaningful but tighter benchmark", BAR_COLOR),
    ]

    for i, (label, desc, color) in enumerate(interpretations):
        y = bullet_start_y + i * bullet_spacing
        elements.append(
            f'<text x="{bullet_x}" y="{y}" fill="{color}" font-size="16" font-family="Arial, Helvetica, sans-serif" font-weight="700">{label}</text>'
        )
        elements.append(
            f'<text x="{bullet_x + 50}" y="{y}" fill="{TEXT_SECONDARY}" font-size="14" font-family="Arial, Helvetica, sans-serif">{desc}</text>'
        )

    # Trend note
    trend_y = bullet_start_y + len(interpretations) * bullet_spacing + 15
    elements.append(
        f'<text x="{bullet_x}" y="{trend_y}" fill="{BAR_COLOR}" font-size="16" font-family="Arial, Helvetica, sans-serif" font-weight="700">Trend</text>'
    )
    elements.append(
        f'<text x="{bullet_x + 50}" y="{trend_y}" fill="{TEXT_SECONDARY}" font-size="14" font-family="Arial, Helvetica, sans-serif">σ_max ∝ 1/sin(φ) ≈ 1/φ for small φ</text>'
    )

    # Representative values section
    values_y = trend_y + 45
    elements.append(
        f'<text x="{bullet_x}" y="{values_y}" fill="{TEXT_PRIMARY}" font-size="17" font-family="Arial, Helvetica, sans-serif" font-weight="700">Representative ideal values</text>'
    )

    for i, (phi_label, sigma) in enumerate(zip(phi_labels, sigmas)):
        y = values_y + 28 + i * 24
        if sigma >= 1000:
            value_str = f"{sigma / 1000:.2f} kg/m²"
        else:
            value_str = f"{sigma:.1f} g/m²"
        color = THETA_EARTH_COLOR if i == 0 else HIGHLIGHT_COLOR
        elements.append(
            f'<text x="{bullet_x}" y="{y}" fill="{color}" font-size="14" font-family="Arial, Helvetica, sans-serif">{phi_label}: {value_str}</text>'
        )

    # Physical scale note
    scale_y = values_y + 28 + len(phi_labels) * 24 + 15
    elements.append(
        f'<text x="{bullet_x}" y="{scale_y}" fill="#9fe4d6" font-size="13" font-family="Arial, Helvetica, sans-serif">θ⊕ offset ≈ 1 Earth radius at 1 AU</text>'
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
