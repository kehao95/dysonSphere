import math


def generate_svg():
    width, height = 980, 560
    cx, cy = 300, 290  # center of the orbital view

    # Orbital ring parameters
    r_major = 185  # semi-major axis (horizontal radius)
    r_minor = 70  # semi-minor axis (vertical radius for 3D tilt effect)

    # Three latitude bands: +phi, ecliptic (0), -phi
    # phi ~ 8 degrees -> y_offset = r_major * tan(8°) ≈ 26
    phi_deg = 8
    y_offset = r_major * math.tan(math.radians(phi_deg))  # ~26 pixels

    bands = [
        {
            "y_offset": -y_offset,
            "color": "#ffd36f",
            "label": "+φ band",
            "is_displaced": True,
        },
        {
            "y_offset": 0,
            "color": "#6fd0c1",
            "label": "Ecliptic (seed orbit)",
            "is_displaced": False,
        },
        {
            "y_offset": y_offset,
            "color": "#ffd36f",
            "label": "−φ band",
            "is_displaced": True,
        },
    ]

    n_nodes = 12  # nodes per band
    node_radius = 4.5

    def ellipse_point(theta, cx, cy, rx, ry):
        """Get point on ellipse at angle theta"""
        x = cx + rx * math.cos(theta)
        y = cy + ry * math.sin(theta)
        return x, y

    def is_front(theta):
        """Front half: theta in [0, pi] (bottom half in screen coords)"""
        # sin(theta) > 0 means bottom half = front
        return math.sin(theta) >= 0

    def generate_ellipse_paths(cx, cy, rx, ry, color, n_points=180):
        """Generate front (solid) and back (dashed) paths for an ellipse"""
        front_segments = []
        back_segments = []
        current_segment = []
        current_is_front = None

        for i in range(n_points + 1):
            theta = 2 * math.pi * i / n_points
            x, y = ellipse_point(theta, cx, cy, rx, ry)
            pt_is_front = is_front(theta)

            if current_is_front is None:
                current_is_front = pt_is_front
                current_segment = [(x, y)]
            elif pt_is_front == current_is_front:
                current_segment.append((x, y))
            else:
                # Transition - save current segment and start new one
                if current_is_front:
                    front_segments.append(current_segment)
                else:
                    back_segments.append(current_segment)
                current_is_front = pt_is_front
                current_segment = [
                    current_segment[-1],
                    (x, y),
                ]  # overlap for continuity

        # Save last segment
        if current_segment:
            if current_is_front:
                front_segments.append(current_segment)
            else:
                back_segments.append(current_segment)

        paths = []

        # Back paths (dashed, dimmer)
        for seg in back_segments:
            if len(seg) < 2:
                continue
            d = f"M {seg[0][0]:.1f} {seg[0][1]:.1f}"
            for x, y in seg[1:]:
                d += f" L {x:.1f} {y:.1f}"
            paths.append(
                f'  <path d="{d}" fill="none" stroke="{color}" stroke-width="2.2" stroke-dasharray="6,4" opacity="0.4"/>'
            )

        # Front paths (solid)
        for seg in front_segments:
            if len(seg) < 2:
                continue
            d = f"M {seg[0][0]:.1f} {seg[0][1]:.1f}"
            for x, y in seg[1:]:
                d += f" L {x:.1f} {y:.1f}"
            paths.append(
                f'  <path d="{d}" fill="none" stroke="{color}" stroke-width="2.2"/>'
            )

        return paths

    def generate_nodes(cx, cy, rx, ry, color, n_nodes):
        """Generate nodes distributed on ellipse, with front/back styling"""
        back_nodes = []
        front_nodes = []

        for i in range(n_nodes):
            theta = 2 * math.pi * i / n_nodes
            x, y = ellipse_point(theta, cx, cy, rx, ry)

            if is_front(theta):
                front_nodes.append(
                    f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{node_radius}" fill="{color}"/>'
                )
            else:
                back_nodes.append(
                    f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{node_radius - 0.5}" fill="{color}" opacity="0.4"/>'
                )

        return back_nodes, front_nodes

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <!-- Background -->
  <rect x="0" y="0" width="{width}" height="{height}" fill="#08111f"/>
  
  <!-- Title -->
  <text x="40" y="54" fill="#f3f6fb" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">MDDS Low-Latitude Stratification</text>
  <text x="40" y="84" fill="#aebfd1" font-size="16" font-family="Arial, Helvetica, sans-serif">Off-plane displacement creates separated latitude bands; light pressure supplies only the vertical component.</text>
  
'''

    # First pass: draw all back elements (behind star)
    svg += "  <!-- Back elements -->\n"

    all_back_nodes = []
    all_front_nodes = []
    all_paths = []

    for band in bands:
        band_cy = cy + band["y_offset"]
        color = band["color"]

        # Generate paths
        paths = generate_ellipse_paths(cx, band_cy, r_major, r_minor, color)
        all_paths.extend(paths)

        # Generate nodes
        back_nodes, front_nodes = generate_nodes(
            cx, band_cy, r_major, r_minor, color, n_nodes
        )
        all_back_nodes.extend(back_nodes)
        all_front_nodes.extend(front_nodes)

    # Add back paths and nodes
    for path in all_paths:
        if "dasharray" in path:  # back paths have dasharray
            svg += path + "\n"

    for node in all_back_nodes:
        svg += node + "\n"

    # Star (drawn in middle layer)
    svg += f'''
  <!-- Star -->
  <circle cx="{cx}" cy="{cy}" r="26" fill="#ffb65c"/>
  
'''

    # Front elements
    svg += "  <!-- Front elements -->\n"

    for path in all_paths:
        if "dasharray" not in path:  # front paths don't have dasharray
            svg += path + "\n"

    for node in all_front_nodes:
        svg += node + "\n"

    # Labels for bands
    label_x = cx + r_major + 25
    svg += f'''
  <!-- Band labels -->
  <text x="{label_x}" y="{cy + bands[0]["y_offset"] + 5}" fill="{bands[0]["color"]}" font-size="15" font-family="Arial, Helvetica, sans-serif">{bands[0]["label"]}</text>
  <text x="{label_x}" y="{cy + bands[1]["y_offset"] + 5}" fill="{bands[1]["color"]}" font-size="15" font-family="Arial, Helvetica, sans-serif">{bands[1]["label"]}</text>
  <text x="{label_x}" y="{cy + bands[2]["y_offset"] + 5}" fill="{bands[2]["color"]}" font-size="15" font-family="Arial, Helvetica, sans-serif">{bands[2]["label"]}</text>
  
  <!-- Star label -->
  <text x="{cx}" y="{cy + 50}" fill="#ffd49a" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600" text-anchor="middle">Star</text>
  
'''

    # Angle annotation: draw from star center showing phi angle
    # Place the angle arc closer to the star for better visibility
    arc_radius = 60
    phi_offset = bands[0]["y_offset"]  # vertical offset for +phi band

    # Calculate the angle in radians
    # The actual 3D angle: the band is displaced by phi_offset in z, at radius r_major in xy
    phi_rad = math.atan2(abs(phi_offset), r_major)

    # Arc endpoints (from star center)
    arc_start_x = cx + arc_radius
    arc_start_y = cy
    arc_end_x = cx + arc_radius * math.cos(phi_rad)
    arc_end_y = cy - arc_radius * math.sin(phi_rad)

    # Label position (at middle of arc, slightly outside)
    label_angle = phi_rad / 2
    label_radius = arc_radius + 14
    label_x = cx + label_radius * math.cos(label_angle)
    label_y = cy - label_radius * math.sin(label_angle) + 5

    svg += f'''
  <!-- Angle annotation for φ -->
  <!-- Reference lines from star to band edges -->
  <line x1="{cx}" y1="{cy}" x2="{cx + r_major + 10}" y2="{cy}" stroke="#6fd0c1" stroke-width="1.5" opacity="0.6"/>
  <line x1="{cx}" y1="{cy}" x2="{cx + r_major + 10}" y2="{cy + phi_offset}" stroke="#ffd36f" stroke-width="1.5" opacity="0.6"/>
  
  <!-- Angle arc for φ -->
  <path d="M {arc_start_x:.1f} {arc_start_y:.1f} A {arc_radius} {arc_radius} 0 0 0 {arc_end_x:.1f} {arc_end_y:.1f}" fill="none" stroke="#ff9966" stroke-width="2"/>
  <text x="{label_x:.1f}" y="{label_y:.1f}" fill="#ff9966" font-size="16" font-family="Arial, Helvetica, sans-serif" font-weight="600">φ</text>
  
'''

    # Right panel with explanation
    svg += """  <!-- Right panel -->
  <rect x="580" y="120" width="360" height="320" rx="16" fill="#0e1b2c" stroke="#223a53" stroke-width="1.5"/>
  
  <text x="610" y="162" fill="#f0f5fb" font-size="20" font-family="Arial, Helvetica, sans-serif" font-weight="700">Architecture intuition</text>
  
  <circle cx="620" cy="205" r="4" fill="#74d4c1"/>
  <text x="640" y="210" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">Collectors remain primarily orbital</text>
  
  <circle cx="620" cy="245" r="4" fill="#74d4c1"/>
  <text x="640" y="250" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">SRP supplies only off-plane component</text>
  
  <circle cx="620" cy="285" r="4" fill="#74d4c1"/>
  <text x="640" y="290" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">Bands share a common stellar axis</text>
  
  <circle cx="620" cy="325" r="4" fill="#74d4c1"/>
  <text x="640" y="330" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">Geometric layering, no nodal crossings</text>
  
  <circle cx="620" cy="365" r="4" fill="#74d4c1"/>
  <text x="640" y="370" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">Low latitude = lowest β requirement</text>
  
  <text x="610" y="415" fill="#667788" font-size="12" font-family="Arial, Helvetica, sans-serif" font-style="italic">Solid = front half, dashed = back half</text>
  
</svg>"""

    return svg


print(generate_svg())
