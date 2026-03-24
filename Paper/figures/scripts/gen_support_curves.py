#!/usr/bin/env python3
"""
Generate Fig3: Latitude support curves
Left panel: beta_min(phi) - Required lightness number
Right panel: sigma_max(phi) - Maximum supportable areal density

Both panels use linear scales starting from 0.
"""

import math

# SVG dimensions
WIDTH = 1120
HEIGHT = 580
MARGIN_LEFT = 60
MARGIN_RIGHT = 60
MARGIN_TOP = 100
MARGIN_BOTTOM = 80
PANEL_GAP = 80

# Calculate panel dimensions
panel_width = (WIDTH - MARGIN_LEFT - MARGIN_RIGHT - PANEL_GAP) // 2
panel_height = HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Panel positions
left_panel_x = MARGIN_LEFT
right_panel_x = MARGIN_LEFT + panel_width + PANEL_GAP

# Chart area within panels
chart_margin = 58
chart_top = 48

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

# Physical constants
SIGMA_STAR = 1.53  # g/m^2, characteristic areal density at 1 AU (P_rad / g_sun)


def beta_min(phi_deg):
    """Minimum lightness number for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    return (3 * math.sqrt(3) / 2) * math.sin(phi_rad)


def sigma_max(phi_deg):
    """Maximum supportable areal density [g/m^2] for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    if phi_rad < 1e-10:
        return float("inf")
    return (2 * SIGMA_STAR) / (3 * math.sqrt(3) * math.sin(phi_rad))


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
        f'<text x="40" y="48" fill="{TEXT_PRIMARY}" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">Latitude Support Curves</text>'
    )
    elements.append(
        f'<text x="40" y="78" fill="{TEXT_SECONDARY}" font-size="16" font-family="Arial, Helvetica, sans-serif">Left: β_min(φ). Right: σ_max(φ).</text>'
    )

    # Data ranges - both start from 0
    phi_min, phi_max = 0, 5.0  # degrees

    # Sample points for highlighting
    highlight_phis = [0.1, 0.5, 1.0]

    # ===== LEFT PANEL: beta_min =====
    lp_x = left_panel_x
    lp_y = MARGIN_TOP

    # Panel background
    elements.append(
        f'<rect x="{lp_x}" y="{lp_y}" width="{panel_width}" height="{panel_height}" rx="16" fill="{PANEL_BG}" stroke="{PANEL_STROKE}" stroke-width="1.5"/>'
    )
    elements.append(
        f'<text x="{lp_x + 18}" y="{lp_y + 30}" fill="{TEXT_TITLE}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Required lightness number β_min(φ)</text>'
    )

    # Chart area
    chart_x = lp_x + chart_margin
    chart_y = lp_y + chart_top
    chart_w = panel_width - chart_margin - 30
    chart_h = panel_height - chart_top - 50

    elements.append(
        f'<rect x="{chart_x}" y="{chart_y}" width="{chart_w}" height="{chart_h}" rx="8" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )

    # Beta range for left panel
    beta_min_val = 0
    beta_max_val = 0.25  # Fixed max for nice display

    # Grid lines - horizontal (y-axis: beta)
    y_ticks = [0, 0.05, 0.10, 0.15, 0.20, 0.25]
    for tick in y_ticks:
        y_pos = linear_scale(
            tick, beta_min_val, beta_max_val, chart_y + chart_h, chart_y
        )
        elements.append(
            f'<line x1="{chart_x}" y1="{y_pos:.1f}" x2="{chart_x + chart_w}" y2="{y_pos:.1f}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{chart_x - 10}" y="{y_pos + 5:.1f}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{tick:.2f}</text>'
        )

    # Grid lines - vertical (x-axis: phi, linear from 0)
    x_ticks_phi = [0, 1, 2, 3, 4, 5]
    for phi in x_ticks_phi:
        x_pos = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        elements.append(
            f'<line x1="{x_pos:.1f}" y1="{chart_y}" x2="{x_pos:.1f}" y2="{chart_y + chart_h}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{x_pos:.1f}" y="{chart_y + chart_h + 20}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{phi}</text>'
        )

    # X-axis label
    elements.append(
        f'<text x="{chart_x + chart_w / 2}" y="{chart_y + chart_h + 42}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Latitude φ [deg]</text>'
    )

    # Curve - beta_min (start from small positive value to avoid phi=0)
    points = []
    for i in range(201):
        phi = 0.01 + (phi_max - 0.01) * (
            i / 200
        )  # start from 0.01 to avoid division issues
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        y = linear_scale(
            beta_min(phi), beta_min_val, beta_max_val, chart_y + chart_h, chart_y
        )
        # Clamp y to chart area
        y = max(chart_y, min(chart_y + chart_h, y))
        points.append(f"{x:.2f},{y:.2f}")

    elements.append(
        f'<polyline points="{" ".join(points)}" fill="none" stroke="{CURVE_COLOR}" stroke-width="2.5"/>'
    )

    # Highlight points
    for phi in highlight_phis:
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        beta = beta_min(phi)
        y = linear_scale(beta, beta_min_val, beta_max_val, chart_y + chart_h, chart_y)
        y = max(chart_y, min(chart_y + chart_h, y))
        elements.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{POINT_COLOR}"/>'
        )
        elements.append(
            f'<text x="{x + 10:.1f}" y="{y - 10:.1f}" fill="{TEXT_ANNOTATION}" font-size="13" font-family="Arial, Helvetica, sans-serif">{phi}° → β={beta:.4f}</text>'
        )

    # ===== RIGHT PANEL: sigma_max =====
    rp_x = right_panel_x
    rp_y = MARGIN_TOP

    # Panel background
    elements.append(
        f'<rect x="{rp_x}" y="{rp_y}" width="{panel_width}" height="{panel_height}" rx="16" fill="{PANEL_BG}" stroke="{PANEL_STROKE}" stroke-width="1.5"/>'
    )
    elements.append(
        f'<text x="{rp_x + 18}" y="{rp_y + 30}" fill="{TEXT_TITLE}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Max areal density σ_max(φ) [g/m²]</text>'
    )

    # Chart area
    chart_x2 = rp_x + chart_margin
    chart_y2 = rp_y + chart_top

    elements.append(
        f'<rect x="{chart_x2}" y="{chart_y2}" width="{chart_w}" height="{chart_h}" rx="8" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )

    # Sigma range - linear scale, start from 0
    sigma_min_val = 0
    sigma_max_val = 400  # g/m^2 - enough to show the interesting range

    # Grid lines - horizontal (y-axis: sigma)
    y_ticks_sigma = [0, 100, 200, 300, 400]
    for tick in y_ticks_sigma:
        y_pos = linear_scale(
            tick, sigma_min_val, sigma_max_val, chart_y2 + chart_h, chart_y2
        )
        elements.append(
            f'<line x1="{chart_x2}" y1="{y_pos:.1f}" x2="{chart_x2 + chart_w}" y2="{y_pos:.1f}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{chart_x2 - 10}" y="{y_pos + 5:.1f}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{tick}</text>'
        )

    # Grid lines - vertical (same as left panel)
    for phi in x_ticks_phi:
        x_pos = linear_scale(phi, phi_min, phi_max, chart_x2, chart_x2 + chart_w)
        elements.append(
            f'<line x1="{x_pos:.1f}" y1="{chart_y2}" x2="{x_pos:.1f}" y2="{chart_y2 + chart_h}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        elements.append(
            f'<text x="{x_pos:.1f}" y="{chart_y2 + chart_h + 20}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{phi}</text>'
        )

    # X-axis label
    elements.append(
        f'<text x="{chart_x2 + chart_w / 2}" y="{chart_y2 + chart_h + 42}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Latitude φ [deg]</text>'
    )

    # Curve - sigma_max (start from small positive value to avoid infinity)
    points = []
    for i in range(201):
        phi = 0.05 + (phi_max - 0.05) * (
            i / 200
        )  # start from 0.05 to avoid huge values
        x = linear_scale(phi, phi_min, phi_max, chart_x2, chart_x2 + chart_w)
        sigma = sigma_max(phi)
        # Clamp sigma for display
        sigma_clamped = min(sigma, sigma_max_val)
        y = linear_scale(
            sigma_clamped, sigma_min_val, sigma_max_val, chart_y2 + chart_h, chart_y2
        )
        # Clamp y to chart area
        y = max(chart_y2, min(chart_y2 + chart_h, y))
        points.append(f"{x:.2f},{y:.2f}")

    elements.append(
        f'<polyline points="{" ".join(points)}" fill="none" stroke="{CURVE_COLOR}" stroke-width="2.5"/>'
    )

    # Highlight points
    for phi in highlight_phis:
        x = linear_scale(phi, phi_min, phi_max, chart_x2, chart_x2 + chart_w)
        sigma = sigma_max(phi)
        sigma_clamped = min(sigma, sigma_max_val)
        y = linear_scale(
            sigma_clamped, sigma_min_val, sigma_max_val, chart_y2 + chart_h, chart_y2
        )
        y = max(chart_y2, min(chart_y2 + chart_h, y))
        elements.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{POINT_COLOR}"/>'
        )
        elements.append(
            f'<text x="{x + 10:.1f}" y="{y - 10:.1f}" fill="{TEXT_ANNOTATION}" font-size="13" font-family="Arial, Helvetica, sans-serif">{phi}° → {sigma:.1f} g/m²</text>'
        )

    # Assemble SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">
{chr(10).join(elements)}
</svg>'''

    return svg


if __name__ == "__main__":
    svg_content = generate_svg()
    output_path = "../results/support_curves.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")
