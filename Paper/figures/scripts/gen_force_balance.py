#!/usr/bin/env python3
"""
Generate a HoverDisk force-balance diagram.

The diagram shows the force balance for one point on an offset disk:

1. Solar-sail thrust
2. Gravity toward the star / central body
3. The centrifugal term associated with orbital motion

In the co-rotating view these three vectors close:

    F_sail + F_g + F_cf = 0

The same geometry can be read in the inertial view as an equivalent inward
centripetal demand toward the offset-disk center:

    F_sail + F_g = F_c
"""

import math


def v_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def v_scale(a, s):
    return (a[0] * s, a[1] * s)


def v_norm(a):
    mag = math.hypot(a[0], a[1])
    if mag == 0:
        return (0.0, 0.0)
    return (a[0] / mag, a[1] / mag)


def svg_arrow(x1, y1, x2, y2, color, width, marker_id, dash="", opacity=1.0):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{width}" marker-end="url(#{marker_id})"'
        f'{dash_attr} opacity="{opacity}"/>\n'
    )


def svg_line(x1, y1, x2, y2, color, width, dash="", opacity=1.0):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{width}"{dash_attr} opacity="{opacity}"/>\n'
    )


def generate_svg():
    width, height = 1120, 620

    # Layout anchors.
    star_x, star_y = 140, 400
    disk_center_x, disk_center_y = 140, 305
    sail_cx, sail_cy = 430, 305

    # Geometry in the meridional section.
    rho = sail_cx - disk_center_x
    z = star_y - sail_cy
    phi = math.atan2(z, rho)
    phi_deg = math.degrees(phi)

    # Force construction.
    gravity_dir = v_norm((star_x - sail_cx, star_y - sail_cy))
    gravity_mag = 1.0

    # Use a clear upward thrust direction for the conceptual figure.
    thrust_angle_deg = 35.0
    thrust_angle = math.radians(thrust_angle_deg)
    thrust_dir = (math.cos(thrust_angle), -math.sin(thrust_angle))

    # Vertical balance fixes the thrust magnitude; the radial residual becomes
    # the inward centripetal demand toward the offset-disk center.
    thrust_mag = (gravity_mag * gravity_dir[1]) / (-thrust_dir[1])
    gravity_vec = v_scale(gravity_dir, gravity_mag)
    thrust_vec = v_scale(thrust_dir, thrust_mag)
    centripetal_vec = v_add(gravity_vec, thrust_vec)
    centrifugal_vec = (-centripetal_vec[0], 0.0)

    # Scale the displayed vectors.
    force_scale = 96.0
    fg_end = v_add((sail_cx, sail_cy), v_scale(gravity_vec, force_scale))
    fs_end = v_add((sail_cx, sail_cy), v_scale(thrust_vec, force_scale))
    fcf_end = v_add((sail_cx, sail_cy), v_scale(centrifugal_vec, force_scale))
    fc_end = v_add((sail_cx, sail_cy), v_scale(centripetal_vec, force_scale))

    # Construction points for vector addition.
    thrust_then_gravity = v_add(fs_end, v_scale(gravity_vec, force_scale))
    gravity_then_thrust = v_add(fg_end, v_scale(thrust_vec, force_scale))

    # Sail surface is drawn perpendicular to the thrust vector.
    tangent = (thrust_dir[1], -thrust_dir[0])
    sail_half = 58
    sail_x1 = sail_cx - sail_half * tangent[0]
    sail_y1 = sail_cy - sail_half * tangent[1]
    sail_x2 = sail_cx + sail_half * tangent[0]
    sail_y2 = sail_cy + sail_half * tangent[1]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <defs>
    <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#ff7272"/>
    </marker>
    <marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#6ec6ff"/>
    </marker>
    <marker id="arrow-gold" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#ffd36f"/>
    </marker>
    <marker id="arrow-green" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#74d4c1"/>
    </marker>
  </defs>

  <rect width="{width}" height="{height}" fill="#08111f"/>

  <text x="40" y="54" fill="#f3f6fb" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">HoverDisk Force Balance</text>
  <text x="40" y="84" fill="#aebfd1" font-size="16" font-family="Arial, Helvetica, sans-serif">Sail thrust, gravity, and orbital centrifugal balance for an offset disk.</text>
"""

    # Reference geometry.
    svg += f"""
  <!-- Reference structure -->
  <line x1="{star_x:.1f}" y1="120" x2="{star_x:.1f}" y2="500" stroke="#43607d" stroke-width="1.2" stroke-dasharray="6,5" opacity="0.45"/>
  <text x="{star_x + 10:.1f}" y="134" fill="#6e89a4" font-size="11" font-family="Arial, Helvetica, sans-serif" opacity="0.75">rotation axis</text>

  <line x1="70" y1="{star_y:.1f}" x2="510" y2="{star_y:.1f}" stroke="#4fc3f7" stroke-width="1.0" stroke-dasharray="6,5" opacity="0.35"/>
  <text x="516" y="{star_y + 4:.1f}" fill="#4fc3f7" font-size="11" font-family="Arial, Helvetica, sans-serif" opacity="0.65">equatorial plane</text>

  <line x1="85" y1="{disk_center_y:.1f}" x2="505" y2="{disk_center_y:.1f}" stroke="#74d4c1" stroke-width="1.0" stroke-dasharray="7,5" opacity="0.25"/>
  <text x="510" y="{disk_center_y + 4:.1f}" fill="#74d4c1" font-size="11" font-family="Arial, Helvetica, sans-serif" opacity="0.7">offset disk plane</text>

  <circle cx="{star_x:.1f}" cy="{star_y:.1f}" r="22" fill="#ffb65c"/>
  <text x="{star_x:.1f}" y="{star_y + 42:.1f}" fill="#ffd49a" font-size="13" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">star</text>

  <circle cx="{disk_center_x:.1f}" cy="{disk_center_y:.1f}" r="5" fill="#74d4c1"/>
  <text x="{disk_center_x - 18:.1f}" y="{disk_center_y - 16:.1f}" fill="#74d4c1" font-size="12" font-family="Arial, Helvetica, sans-serif">offset-disk center</text>

  <line x1="{disk_center_x:.1f}" y1="{disk_center_y:.1f}" x2="{sail_cx:.1f}" y2="{sail_cy:.1f}" stroke="#5d748b" stroke-width="1.2" stroke-dasharray="5,4" opacity="0.55"/>
  <text x="{(disk_center_x + sail_cx) / 2:.1f}" y="{disk_center_y - 10:.1f}" fill="#90a7bd" font-size="12" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">orbital radius ρ</text>

  <line x1="{star_x:.1f}" y1="{star_y:.1f}" x2="{sail_cx:.1f}" y2="{sail_cy:.1f}" stroke="#ffb74d" stroke-width="1.1" stroke-dasharray="5,4" opacity="0.45"/>
"""

    phi_arc_r = 58
    arc_end_x = star_x + phi_arc_r * math.cos(phi)
    arc_end_y = star_y - phi_arc_r * math.sin(phi)
    svg += f"""
  <path d="M {star_x + phi_arc_r:.1f} {star_y:.1f} A {phi_arc_r} {phi_arc_r} 0 0 0 {arc_end_x:.1f} {arc_end_y:.1f}" fill="none" stroke="#ffb74d" stroke-width="1.4" opacity="0.6"/>
  <text x="{star_x + 42:.1f}" y="{star_y - 18:.1f}" fill="#ffb74d" font-size="14" font-family="Arial, Helvetica, sans-serif">φ</text>
"""

    # Sunlight cue.
    svg += "\n  <!-- Sunlight cue -->\n"
    sunlight_dir = (-gravity_dir[0], -gravity_dir[1])
    for offset in (-26, -13, 0, 13, 26):
        ray_start_x = sail_cx - 125 * sunlight_dir[0] + offset * tangent[0] * 0.5
        ray_start_y = sail_cy - 125 * sunlight_dir[1] + offset * tangent[1] * 0.5
        ray_end_x = sail_cx + offset * tangent[0] * 0.5
        ray_end_y = sail_cy + offset * tangent[1] * 0.5
        svg += (
            f'  <line x1="{ray_start_x:.1f}" y1="{ray_start_y:.1f}" '
            f'x2="{ray_end_x:.1f}" y2="{ray_end_y:.1f}" stroke="#ffd54f" '
            f'stroke-width="1.5" opacity="0.4"/>\n'
        )
    svg += f'  <text x="{sail_cx - 135:.1f}" y="{sail_cy - 36:.1f}" fill="#ffd54f" font-size="12" font-family="Arial, Helvetica, sans-serif" opacity="0.8">sunlight</text>\n'

    # HoverDisk element.
    svg += f"""
  <!-- HoverDisk element -->
  <line x1="{sail_x1:.1f}" y1="{sail_y1:.1f}" x2="{sail_x2:.1f}" y2="{sail_y2:.1f}" stroke="#9bd3ff" stroke-width="7" stroke-linecap="round"/>
  <line x1="{sail_x1:.1f}" y1="{sail_y1:.1f}" x2="{sail_x2:.1f}" y2="{sail_y2:.1f}" stroke="#e7f4ff" stroke-width="1.6" stroke-linecap="round" opacity="0.55"/>
  <circle cx="{sail_cx:.1f}" cy="{sail_cy:.1f}" r="4.2" fill="#ffffff"/>
  <text x="{sail_cx + 24:.1f}" y="{sail_cy + 60:.1f}" fill="#cfe6fb" font-size="12" font-family="Arial, Helvetica, sans-serif">HoverDisk element</text>
"""

    # Force vectors.
    svg += "\n  <!-- Force vectors -->\n"
    svg += svg_arrow(sail_cx, sail_cy, fs_end[0], fs_end[1], "#6ec6ff", 2.4, "arrow-blue")
    svg += f'  <text x="{fs_end[0] + 8:.1f}" y="{fs_end[1] - 4:.1f}" fill="#6ec6ff" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">sail</tspan></text>\n'

    svg += svg_arrow(sail_cx, sail_cy, fg_end[0], fg_end[1], "#ff7272", 2.4, "arrow-red")
    svg += f'  <text x="{fg_end[0] - 34:.1f}" y="{fg_end[1] + 16:.1f}" fill="#ff7272" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">g</tspan></text>\n'

    svg += svg_arrow(sail_cx, sail_cy, fcf_end[0], fcf_end[1], "#ffd36f", 2.4, "arrow-gold")
    svg += f'  <text x="{fcf_end[0] + 8:.1f}" y="{fcf_end[1] + 18:.1f}" fill="#ffd36f" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">cf</tspan></text>\n'

    svg += svg_arrow(sail_cx, sail_cy, fc_end[0], fc_end[1], "#74d4c1", 2.8, "arrow-green")
    svg += f'  <text x="{fc_end[0] - 28:.1f}" y="{fc_end[1] - 10:.1f}" fill="#74d4c1" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">c</tspan></text>\n'

    # Vector addition construction.
    svg += "\n  <!-- Vector construction -->\n"
    svg += svg_line(fs_end[0], fs_end[1], thrust_then_gravity[0], thrust_then_gravity[1], "#ff7272", 1.2, "4,4", 0.5)
    svg += svg_line(fg_end[0], fg_end[1], gravity_then_thrust[0], gravity_then_thrust[1], "#6ec6ff", 1.2, "4,4", 0.5)
    svg += svg_line(fc_end[0], fc_end[1], sail_cx, sail_cy, "#ffd36f", 1.2, "4,4", 0.45)
    svg += f'  <text x="{sail_cx - 32:.1f}" y="{sail_cy - 76:.1f}" fill="#90a7bd" font-size="11" font-family="Arial, Helvetica, sans-serif" opacity="0.8">F<tspan baseline-shift="sub" font-size="8">sail</tspan> + F<tspan baseline-shift="sub" font-size="8">g</tspan> = F<tspan baseline-shift="sub" font-size="8">c</tspan></text>\n'
    svg += f'  <text x="{sail_cx - 8:.1f}" y="{sail_cy + 42:.1f}" fill="#90a7bd" font-size="11" font-family="Arial, Helvetica, sans-serif" opacity="0.8">F<tspan baseline-shift="sub" font-size="8">sail</tspan> + F<tspan baseline-shift="sub" font-size="8">g</tspan> + F<tspan baseline-shift="sub" font-size="8">cf</tspan> = 0</text>\n'

    # Explanation panel.
    panel_x = 700
    panel_y = 108
    panel_w = 360
    panel_h = 410
    svg += f"""
  <!-- Explanation panel -->
  <rect x="{panel_x}" y="{panel_y}" width="{panel_w}" height="{panel_h}" rx="16" fill="#0e1b2c" stroke="#223a53" stroke-width="1.5"/>

  <text x="{panel_x + 24}" y="{panel_y + 34}" fill="#f0f5fb" font-size="18" font-family="Arial, Helvetica, sans-serif" font-weight="700">How to read the balance</text>

  <circle cx="{panel_x + 28}" cy="{panel_y + 68}" r="4" fill="#6ec6ff"/>
  <text x="{panel_x + 44}" y="{panel_y + 73}" fill="#6ec6ff" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">sail</tspan></text>
  <text x="{panel_x + 92}" y="{panel_y + 73}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">solar-sail thrust</text>

  <circle cx="{panel_x + 28}" cy="{panel_y + 98}" r="4" fill="#ff7272"/>
  <text x="{panel_x + 44}" y="{panel_y + 103}" fill="#ff7272" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">g</tspan></text>
  <text x="{panel_x + 76}" y="{panel_y + 103}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">gravity toward the star</text>

  <circle cx="{panel_x + 28}" cy="{panel_y + 128}" r="4" fill="#ffd36f"/>
  <text x="{panel_x + 44}" y="{panel_y + 133}" fill="#ffd36f" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">cf</tspan></text>
  <text x="{panel_x + 83}" y="{panel_y + 133}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">centrifugal term from</text>
  <text x="{panel_x + 83}" y="{panel_y + 151}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">orbital motion</text>

  <circle cx="{panel_x + 28}" cy="{panel_y + 158}" r="4" fill="#74d4c1"/>
  <text x="{panel_x + 44}" y="{panel_y + 163}" fill="#74d4c1" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">c</tspan></text>
  <text x="{panel_x + 74}" y="{panel_y + 163}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">equivalent inward</text>
  <text x="{panel_x + 74}" y="{panel_y + 181}" fill="#c7d5e2" font-size="13" font-family="Arial, Helvetica, sans-serif">centripetal demand</text>

  <line x1="{panel_x + 22}" y1="{panel_y + 202}" x2="{panel_x + panel_w - 22}" y2="{panel_y + 202}" stroke="#223a53" stroke-width="1"/>

  <text x="{panel_x + 24}" y="{panel_y + 232}" fill="#f0f5fb" font-size="16" font-family="Arial, Helvetica, sans-serif" font-weight="700">Co-rotating view</text>
  <text x="{panel_x + 30}" y="{panel_y + 264}" fill="#dbe6f0" font-size="16" font-family="Arial, Helvetica, sans-serif">F<tspan baseline-shift="sub" font-size="11">sail</tspan> + F<tspan baseline-shift="sub" font-size="11">g</tspan> + F<tspan baseline-shift="sub" font-size="11">cf</tspan> = 0</text>
  <text x="{panel_x + 30}" y="{panel_y + 290}" fill="#98adbf" font-size="13" font-family="Arial, Helvetica, sans-serif">The three applied terms close as a static vector polygon.</text>

  <line x1="{panel_x + 22}" y1="{panel_y + 310}" x2="{panel_x + panel_w - 22}" y2="{panel_y + 310}" stroke="#223a53" stroke-width="1"/>

  <text x="{panel_x + 24}" y="{panel_y + 340}" fill="#f0f5fb" font-size="16" font-family="Arial, Helvetica, sans-serif" font-weight="700">Equivalent inertial view</text>
  <text x="{panel_x + 30}" y="{panel_y + 372}" fill="#dbe6f0" font-size="16" font-family="Arial, Helvetica, sans-serif">F<tspan baseline-shift="sub" font-size="11">sail</tspan> + F<tspan baseline-shift="sub" font-size="11">g</tspan> = F<tspan baseline-shift="sub" font-size="11">c</tspan></text>
  <text x="{panel_x + 30}" y="{panel_y + 398}" fill="#98adbf" font-size="13" font-family="Arial, Helvetica, sans-serif">F<tspan baseline-shift="sub" font-size="10">c</tspan> points toward the offset-disk center and represents</text>
  <text x="{panel_x + 30}" y="{panel_y + 418}" fill="#98adbf" font-size="13" font-family="Arial, Helvetica, sans-serif">the required inward acceleration, not a separate actuator.</text>
  <text x="{panel_x + 30}" y="{panel_y + 450}" fill="#74d4c1" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="600">F<tspan baseline-shift="sub" font-size="10">c</tspan> = m · ω² · ρ</text>
  <text x="{panel_x + 30}" y="{panel_y + 480}" fill="#667a8e" font-size="11" font-family="Arial, Helvetica, sans-serif" font-style="italic">Dashed auxiliary lines show vector addition and closure.</text>

  <text x="40" y="566" fill="#6e8398" font-size="12" font-family="Arial, Helvetica, sans-serif">Conceptual meridional section; not to scale.</text>
  <text x="40" y="586" fill="#6e8398" font-size="12" font-family="Arial, Helvetica, sans-serif">Current figure intent: thrust + gravity + centrifugal closure, with the same sum read as centripetal demand toward the offset-disk center.</text>
</svg>"""

    return svg


if __name__ == "__main__":
    print(generate_svg())
