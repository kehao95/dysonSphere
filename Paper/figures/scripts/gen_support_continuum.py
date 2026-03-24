#!/usr/bin/env python3
"""
Generate Fig6: Support Continuum - Full Spectrum View
Shows the complete β_min(φ) and ν(φ) curves from Keplerian limit to branch endpoint,
marking the two key thresholds: β=1 (bubble/statite entry) and ν=0 (branch terminus).
"""

import math

# SVG dimensions
WIDTH = 1020
HEIGHT = 680
MARGIN = 40

# Colors (matching existing figure style)
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

# Curve colors
BETA_COLOR = "#74d4c1"  # Teal for β_min
NU_COLOR = "#f4a259"  # Orange for ν
THRESHOLD_COLOR = "#e07a5f"  # Red-orange for threshold lines
POINT_COLOR = "#ffffff"

# Physical constants
SIGMA_STAR = 1.53  # g/m², characteristic areal density at 1 AU


def beta_min(phi_deg):
    """Minimum lightness number for given latitude angle"""
    phi_rad = math.radians(phi_deg)
    return (3 * math.sqrt(3) / 2) * math.sin(phi_rad)


def nu_squared(phi_deg):
    """Orbital rate ratio squared: ν² = 1 - √2 tan(φ)"""
    phi_rad = math.radians(phi_deg)
    return 1 - math.sqrt(2) * math.tan(phi_rad)


def nu(phi_deg):
    """Orbital rate ratio"""
    nu_sq = nu_squared(phi_deg)
    if nu_sq < 0:
        return 0
    return math.sqrt(nu_sq)


def sigma_max(phi_deg):
    """Maximum system areal density in g/m²"""
    b = beta_min(phi_deg)
    if b <= 0:
        return float("inf")
    return SIGMA_STAR / b


def linear_scale(val, val_min, val_max, out_min, out_max):
    """Map value to output coordinate (linear scale)"""
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
        f'<text x="{MARGIN}" y="40" fill="{TEXT_PRIMARY}" font-size="26" font-family="Arial, Helvetica, sans-serif" font-weight="700">Support Continuum: From Keplerian to Radiation-Dominated</text>'
    )
    elements.append(
        f'<text x="{MARGIN}" y="68" fill="{TEXT_SECONDARY}" font-size="15" font-family="Arial, Helvetica, sans-serif">The full spectrum from pure orbital support (φ=0) to branch terminus (φ≈35.3°)</text>'
    )

    # Key threshold values
    # β = 1 threshold: φ = arcsin(2/(3√3)) ≈ 22.638°
    phi_beta1 = math.degrees(math.asin(2 / (3 * math.sqrt(3))))
    nu_at_beta1 = nu(phi_beta1)

    # ν = 0 threshold: φ = arctan(1/√2) ≈ 35.264°
    phi_nu0 = math.degrees(math.atan(1 / math.sqrt(2)))
    beta_at_nu0 = beta_min(phi_nu0)

    # Chart panel
    chart_panel_x = 60
    chart_panel_y = 100
    chart_panel_w = 600
    chart_panel_h = 500

    elements.append(
        f'<rect x="{chart_panel_x}" y="{chart_panel_y}" width="{chart_panel_w}" height="{chart_panel_h}" rx="16" fill="{PANEL_BG}" stroke="{PANEL_STROKE}" stroke-width="1.5"/>'
    )

    # Chart title
    elements.append(
        f'<text x="{chart_panel_x + 24}" y="{chart_panel_y + 28}" fill="{TEXT_TITLE}" font-size="17" font-family="Arial, Helvetica, sans-serif" font-weight="700">Support Parameters vs. Latitude</text>'
    )

    # Chart area
    chart_margin_left = 70
    chart_margin_right = 70
    chart_margin_top = 50
    chart_margin_bottom = 70

    chart_x = chart_panel_x + chart_margin_left
    chart_y = chart_panel_y + chart_margin_top
    chart_w = chart_panel_w - chart_margin_left - chart_margin_right
    chart_h = chart_panel_h - chart_margin_top - chart_margin_bottom

    elements.append(
        f'<rect x="{chart_x}" y="{chart_y}" width="{chart_w}" height="{chart_h}" rx="8" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )

    # Axis ranges
    # Extend to 38° for visual clarity, but curves terminate at branch endpoint (φ≈35.26°)
    phi_min, phi_max = 0, 38  # degrees
    y_min, y_max = 0, 1.6  # for both β and ν (same scale)

    # Grid lines - horizontal
    y_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    for tick in y_ticks:
        y_pos = linear_scale(tick, y_min, y_max, chart_y + chart_h, chart_y)
        dash = "4 6" if tick != 1.0 else "none"
        color = THRESHOLD_COLOR if tick == 1.0 else GRID_COLOR
        width = 1.5 if tick == 1.0 else 1
        elements.append(
            f'<line x1="{chart_x}" y1="{y_pos:.1f}" x2="{chart_x + chart_w}" y2="{y_pos:.1f}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'
        )
        # Left axis labels (β)
        elements.append(
            f'<text x="{chart_x - 10}" y="{y_pos + 5:.1f}" fill="{BETA_COLOR}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="end">{tick:.1f}</text>'
        )
        # Right axis labels (ν)
        elements.append(
            f'<text x="{chart_x + chart_w + 10}" y="{y_pos + 5:.1f}" fill="{NU_COLOR}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="start">{tick:.1f}</text>'
        )

    # β = 1 label
    y_beta1 = linear_scale(1.0, y_min, y_max, chart_y + chart_h, chart_y)
    elements.append(
        f'<text x="{chart_x + chart_w - 5}" y="{y_beta1 - 8:.1f}" fill="{THRESHOLD_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif" text-anchor="end">β = 1 (bubble/statite threshold)</text>'
    )

    # Grid lines - vertical
    x_ticks_phi = [0, 5, 10, 15, 20, 25, 30, 35]
    for phi in x_ticks_phi:
        x_pos = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        elements.append(
            f'<line x1="{x_pos:.1f}" y1="{chart_y}" x2="{x_pos:.1f}" y2="{chart_y + chart_h}" stroke="{GRID_COLOR}" stroke-width="1" stroke-dasharray="4 6"/>'
        )
        label = f"{phi}°"
        elements.append(
            f'<text x="{x_pos:.1f}" y="{chart_y + chart_h + 20}" fill="{TEXT_LABEL}" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">{label}</text>'
        )

    # X-axis label
    elements.append(
        f'<text x="{chart_x + chart_w / 2}" y="{chart_y + chart_h + 48}" fill="{TEXT_LABEL}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Latitude φ [degrees]</text>'
    )

    # Y-axis labels
    elements.append(
        f'<text x="{chart_x - 50}" y="{chart_y + chart_h / 2}" fill="{BETA_COLOR}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle" transform="rotate(-90, {chart_x - 50}, {chart_y + chart_h / 2})">β_min (lightness number)</text>'
    )
    elements.append(
        f'<text x="{chart_x + chart_w + 50}" y="{chart_y + chart_h / 2}" fill="{NU_COLOR}" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle" transform="rotate(90, {chart_x + chart_w + 50}, {chart_y + chart_h / 2})">ν (orbital rate ratio)</text>'
    )

    # Draw β_min curve (only up to phi_nu0 where the branch terminates)
    beta_points = []
    for i in range(401):
        phi = phi_nu0 * (i / 400)  # Stop at branch terminus, not phi_max
        if phi < 0.01:
            phi = 0.01  # avoid division issues
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        b = beta_min(phi)
        y = linear_scale(b, y_min, y_max, chart_y + chart_h, chart_y)
        y = max(chart_y, min(chart_y + chart_h, y))
        beta_points.append(f"{x:.2f},{y:.2f}")

    elements.append(
        f'<polyline points="{" ".join(beta_points)}" fill="none" stroke="{BETA_COLOR}" stroke-width="2.5"/>'
    )

    # Draw ν curve (only up to phi_nu0 where ν becomes 0)
    nu_points = []
    for i in range(401):
        phi = phi_nu0 * (i / 400)
        x = linear_scale(phi, phi_min, phi_max, chart_x, chart_x + chart_w)
        n = nu(phi)
        y = linear_scale(n, y_min, y_max, chart_y + chart_h, chart_y)
        y = max(chart_y, min(chart_y + chart_h, y))
        nu_points.append(f"{x:.2f},{y:.2f}")

    elements.append(
        f'<polyline points="{" ".join(nu_points)}" fill="none" stroke="{NU_COLOR}" stroke-width="2.5"/>'
    )

    # Mark threshold points

    # 1. Keplerian limit (φ=0, β=0, ν=1)
    x_kep = linear_scale(0, phi_min, phi_max, chart_x, chart_x + chart_w)
    y_nu1 = linear_scale(1.0, y_min, y_max, chart_y + chart_h, chart_y)
    y_beta0 = linear_scale(0, y_min, y_max, chart_y + chart_h, chart_y)
    elements.append(
        f'<circle cx="{x_kep:.1f}" cy="{y_nu1:.1f}" r="6" fill="{NU_COLOR}"/>'
    )
    elements.append(
        f'<circle cx="{x_kep:.1f}" cy="{y_beta0:.1f}" r="6" fill="{BETA_COLOR}"/>'
    )

    # 2. β = 1 threshold (φ ≈ 22.64°)
    x_beta1 = linear_scale(phi_beta1, phi_min, phi_max, chart_x, chart_x + chart_w)
    y_beta1_pt = linear_scale(1.0, y_min, y_max, chart_y + chart_h, chart_y)
    y_nu_at_beta1 = linear_scale(nu_at_beta1, y_min, y_max, chart_y + chart_h, chart_y)

    # Vertical line at β=1 threshold
    elements.append(
        f'<line x1="{x_beta1:.1f}" y1="{chart_y}" x2="{x_beta1:.1f}" y2="{chart_y + chart_h}" stroke="{THRESHOLD_COLOR}" stroke-width="1.5" stroke-dasharray="6 4"/>'
    )
    elements.append(
        f'<circle cx="{x_beta1:.1f}" cy="{y_beta1_pt:.1f}" r="6" fill="{POINT_COLOR}" stroke="{THRESHOLD_COLOR}" stroke-width="2"/>'
    )
    elements.append(
        f'<circle cx="{x_beta1:.1f}" cy="{y_nu_at_beta1:.1f}" r="6" fill="{NU_COLOR}"/>'
    )

    # 3. ν = 0 threshold (φ ≈ 35.26°, β = 1.5)
    x_nu0 = linear_scale(phi_nu0, phi_min, phi_max, chart_x, chart_x + chart_w)
    y_nu0 = linear_scale(0, y_min, y_max, chart_y + chart_h, chart_y)
    y_beta_at_nu0 = linear_scale(beta_at_nu0, y_min, y_max, chart_y + chart_h, chart_y)

    # Vertical line at ν=0 threshold
    elements.append(
        f'<line x1="{x_nu0:.1f}" y1="{chart_y}" x2="{x_nu0:.1f}" y2="{chart_y + chart_h}" stroke="{THRESHOLD_COLOR}" stroke-width="1.5" stroke-dasharray="6 4"/>'
    )
    elements.append(
        f'<circle cx="{x_nu0:.1f}" cy="{y_nu0:.1f}" r="6" fill="{POINT_COLOR}" stroke="{THRESHOLD_COLOR}" stroke-width="2"/>'
    )
    elements.append(
        f'<circle cx="{x_nu0:.1f}" cy="{y_beta_at_nu0:.1f}" r="6" fill="{BETA_COLOR}"/>'
    )

    # Legend / Interpretation panel
    interp_x = 700
    interp_y = 100
    interp_w = 280
    interp_h = 500

    elements.append(
        f'<rect x="{interp_x}" y="{interp_y}" width="{interp_w}" height="{interp_h}" rx="18" fill="{PANEL_BG}" stroke="{PANEL_STROKE}" stroke-width="1.5"/>'
    )

    # Legend title
    elements.append(
        f'<text x="{interp_x + 20}" y="{interp_y + 32}" fill="{TEXT_PRIMARY}" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">Key Points</text>'
    )

    # Three threshold boxes
    box_y = interp_y + 60
    box_h = 120
    box_spacing = 10

    # Box 1: Keplerian limit
    elements.append(
        f'<rect x="{interp_x + 15}" y="{box_y}" width="{interp_w - 30}" height="{box_h}" rx="10" fill="{CHART_BG}" stroke="{CHART_STROKE}" stroke-width="1"/>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y + 22}" fill="{TEXT_TITLE}" font-size="13" font-family="Arial, Helvetica, sans-serif" font-weight="700">① Keplerian Limit</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y + 44}" fill="{TEXT_SECONDARY}" font-size="12" font-family="Arial, Helvetica, sans-serif">φ = 0°</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y + 62}" fill="{BETA_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">β = 0 (no radiation support)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y + 80}" fill="{NU_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">ν = 1 (pure orbital support)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y + 100}" fill="{TEXT_LABEL}" font-size="11" font-family="Arial, Helvetica, sans-serif">Traditional Dyson Swarm regime</text>'
    )

    # Box 2: β = 1 threshold
    box_y2 = box_y + box_h + box_spacing
    elements.append(
        f'<rect x="{interp_x + 15}" y="{box_y2}" width="{interp_w - 30}" height="{box_h}" rx="10" fill="{CHART_BG}" stroke="{THRESHOLD_COLOR}" stroke-width="1.5"/>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y2 + 22}" fill="{TEXT_TITLE}" font-size="13" font-family="Arial, Helvetica, sans-serif" font-weight="700">② Bubble/Statite Entry</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y2 + 44}" fill="{TEXT_SECONDARY}" font-size="12" font-family="Arial, Helvetica, sans-serif">φ ≈ 22.6°</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y2 + 62}" fill="{BETA_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">β = 1 (full levitation possible)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y2 + 80}" fill="{NU_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">ν ≈ 0.64 (still orbital)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y2 + 100}" fill="{TEXT_LABEL}" font-size="11" font-family="Arial, Helvetica, sans-serif">Statite architecture becomes viable</text>'
    )

    # Box 3: ν = 0 threshold
    box_y3 = box_y2 + box_h + box_spacing
    elements.append(
        f'<rect x="{interp_x + 15}" y="{box_y3}" width="{interp_w - 30}" height="{box_h}" rx="10" fill="{CHART_BG}" stroke="{THRESHOLD_COLOR}" stroke-width="1.5"/>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y3 + 22}" fill="{TEXT_TITLE}" font-size="13" font-family="Arial, Helvetica, sans-serif" font-weight="700">③ Branch Terminus</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y3 + 44}" fill="{TEXT_SECONDARY}" font-size="12" font-family="Arial, Helvetica, sans-serif">φ ≈ 35.3° (= α_opt)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y3 + 62}" fill="{BETA_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">β = 1.5</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y3 + 80}" fill="{NU_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">ν = 0 (no orbital support)</text>'
    )
    elements.append(
        f'<text x="{interp_x + 25}" y="{box_y3 + 100}" fill="{TEXT_LABEL}" font-size="11" font-family="Arial, Helvetica, sans-serif">Payload-friendly branch ends here</text>'
    )

    # Curve legend at bottom
    legend_y = box_y3 + box_h + 25
    elements.append(
        f'<line x1="{interp_x + 25}" y1="{legend_y}" x2="{interp_x + 55}" y2="{legend_y}" stroke="{BETA_COLOR}" stroke-width="2.5"/>'
    )
    elements.append(
        f'<text x="{interp_x + 65}" y="{legend_y + 4}" fill="{BETA_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">β_min(φ)</text>'
    )

    legend_y2 = legend_y + 22
    elements.append(
        f'<line x1="{interp_x + 25}" y1="{legend_y2}" x2="{interp_x + 55}" y2="{legend_y2}" stroke="{NU_COLOR}" stroke-width="2.5"/>'
    )
    elements.append(
        f'<text x="{interp_x + 65}" y="{legend_y2 + 4}" fill="{NU_COLOR}" font-size="12" font-family="Arial, Helvetica, sans-serif">ν(φ)</text>'
    )

    # Assemble SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none">
{chr(10).join(elements)}
</svg>'''

    return svg


if __name__ == "__main__":
    svg_content = generate_svg()
    output_path = "../results/support_continuum.svg"
    with open(output_path, "w") as f:
        f.write(svg_content)
    print(f"Generated {output_path}")
