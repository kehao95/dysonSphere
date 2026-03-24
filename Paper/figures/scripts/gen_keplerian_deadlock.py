import math
import numpy as np


def generate_svg():
    width, height = 980, 560
    cx, cy = 320, 300
    r = 180  # orbital radius (same for all orbits, on a sphere)

    orbit_colors = ["#6fd0c1", "#74b3ce", "#9fa8da", "#ce93d8", "#f0a875"]

    # Each orbit defined by (inclination, ascending_node) in degrees
    orbits = [
        (0, 0),  # equatorial
        (60, 0),  # inclined 60°, ascending node at 0°
        (60, 90),  # inclined 60°, ascending node at 90°
        (60, 45),  # inclined 60°, ascending node at 45°
        (45, 135),  # inclined 45°, ascending node at 135°
    ]

    # 3D to 2D projection (oblique view)
    def project(x, y, z):
        view_angle = math.radians(20)
        px = cx + x
        py = cy - z * math.cos(view_angle) - y * math.sin(view_angle) * 0.3
        return px, py

    # Generate points on an orbit with more resolution
    def orbit_points_3d(inc_deg, node_deg, n=360):
        inc = math.radians(inc_deg)
        node = math.radians(node_deg)
        points = []
        for i in range(n):
            theta = 2 * math.pi * i / n
            # Start with equatorial orbit
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            z = 0
            # Rotate around x-axis by inclination
            y2 = y * math.cos(inc) - z * math.sin(inc)
            z2 = y * math.sin(inc) + z * math.cos(inc)
            y, z = y2, z2
            # Rotate around z-axis by ascending node
            x2 = x * math.cos(node) - y * math.sin(node)
            y2 = x * math.sin(node) + y * math.cos(node)
            x, y = x2, y2
            points.append((x, y, z))
        return points

    def orbit_normal(inc_deg, node_deg):
        inc = math.radians(inc_deg)
        node = math.radians(node_deg)
        nx = -(-math.sin(inc)) * math.sin(node)
        ny = (-math.sin(inc)) * math.cos(node)
        nz = math.cos(inc)
        return np.array([nx, ny, nz])

    def find_intersection_points(orb1, orb2):
        n1 = orbit_normal(*orb1)
        n2 = orbit_normal(*orb2)
        line_dir = np.cross(n1, n2)
        norm = np.linalg.norm(line_dir)
        if norm < 1e-10:
            return []
        line_dir = line_dir / norm
        p1 = line_dir * r
        p2 = -line_dir * r
        return [tuple(p1), tuple(p2)]

    # Split orbit into front (y < 0) and back (y > 0) segments
    def split_orbit_segments(pts_3d):
        """
        Split orbit points into continuous segments based on y coordinate.
        Returns list of (is_front, segment_points) tuples.
        is_front = True means y < 0 (closer to viewer)
        """
        if not pts_3d:
            return []

        segments = []
        current_front = pts_3d[0][1] < 0
        current_segment = [pts_3d[0]]

        for i in range(1, len(pts_3d)):
            pt = pts_3d[i]
            is_front = pt[1] < 0

            if is_front == current_front:
                current_segment.append(pt)
            else:
                # Transition point - finish current segment and start new one
                # Add interpolated crossing point to both segments
                prev_pt = pts_3d[i - 1]
                # Linear interpolation to find y=0 crossing
                t = (
                    -prev_pt[1] / (pt[1] - prev_pt[1])
                    if abs(pt[1] - prev_pt[1]) > 1e-10
                    else 0.5
                )
                cross_x = prev_pt[0] + t * (pt[0] - prev_pt[0])
                cross_y = 0
                cross_z = prev_pt[2] + t * (pt[2] - prev_pt[2])
                cross_pt = (cross_x, cross_y, cross_z)

                current_segment.append(cross_pt)
                segments.append((current_front, current_segment))

                current_front = is_front
                current_segment = [cross_pt, pt]

        # Handle wrap-around: check if first and last segments can be merged
        if segments and current_front == segments[0][0]:
            # Merge last segment with first
            current_segment.extend(segments[0][1][1:])  # skip duplicate crossing point
            segments[0] = (current_front, current_segment)
        else:
            segments.append((current_front, current_segment))

        return segments

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <!-- Background -->
  <rect x="0" y="0" width="{width}" height="{height}" fill="#08111f"/>
  
  <!-- Title -->
  <text x="40" y="54" fill="#f3f6fb" font-size="28" font-family="Arial, Helvetica, sans-serif" font-weight="700">Keplerian Deadlock</text>
  <text x="40" y="84" fill="#aebfd1" font-size="16" font-family="Arial, Helvetica, sans-serif">Every pair of orbital planes intersects at exactly 2 points on the sphere.</text>
  
  <!-- Shell outline -->
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#3a5068" stroke-width="1" stroke-dasharray="4,4" opacity="0.5"/>
  
  <!-- Star -->
  <circle cx="{cx}" cy="{cy}" r="28" fill="#ffb65c"/>
  <text x="{cx}" y="{cy + 60}" fill="#ffd49a" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="600" text-anchor="middle">Star</text>
  
'''

    # First pass: draw all back segments (dashed, behind star)
    svg += "  <!-- Back segments (dashed) -->\n"
    for (inc, node), color in zip(orbits, orbit_colors):
        pts_3d = orbit_points_3d(inc, node)
        segments = split_orbit_segments(pts_3d)

        for is_front, seg_pts in segments:
            if is_front:
                continue  # Skip front segments in first pass
            pts_2d = [project(*p) for p in seg_pts]
            if len(pts_2d) < 2:
                continue
            path_d = f"M {pts_2d[0][0]:.1f} {pts_2d[0][1]:.1f}"
            for px, py in pts_2d[1:]:
                path_d += f" L {px:.1f} {py:.1f}"
            svg += f'  <path d="{path_d}" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="6,4" opacity="0.5"/>\n'

    # Second pass: draw all front segments (solid, in front of star)
    svg += "\n  <!-- Front segments (solid) -->\n"
    for (inc, node), color in zip(orbits, orbit_colors):
        pts_3d = orbit_points_3d(inc, node)
        segments = split_orbit_segments(pts_3d)

        for is_front, seg_pts in segments:
            if not is_front:
                continue  # Skip back segments in second pass
            pts_2d = [project(*p) for p in seg_pts]
            if len(pts_2d) < 2:
                continue
            path_d = f"M {pts_2d[0][0]:.1f} {pts_2d[0][1]:.1f}"
            for px, py in pts_2d[1:]:
                path_d += f" L {px:.1f} {py:.1f}"
            svg += f'  <path d="{path_d}" fill="none" stroke="{color}" stroke-width="2"/>\n'

    # Find all intersection points
    all_intersections = []
    for i in range(len(orbits)):
        for j in range(i + 1, len(orbits)):
            inters = find_intersection_points(orbits[i], orbits[j])
            all_intersections.extend(inters)

    # Remove duplicates
    unique_intersections = []
    for p in all_intersections:
        is_dup = False
        for existing in unique_intersections:
            if np.linalg.norm(np.array(p) - np.array(existing)) < 1:
                is_dup = True
                break
        if not is_dup:
            unique_intersections.append(p)

    # Separate front and back intersection points
    front_intersections = [p for p in unique_intersections if p[1] <= 0]
    back_intersections = [p for p in unique_intersections if p[1] > 0]

    # Draw back intersection points first (smaller, dimmer)
    svg += "\n  <!-- Back intersection points -->\n"
    for p3d in back_intersections:
        px, py = project(*p3d)
        svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="#ff6b6b" stroke="#ffaaaa" stroke-width="1" opacity="0.5"/>\n'

    # Draw front intersection points (larger, brighter)
    svg += "\n  <!-- Front intersection points -->\n"
    for p3d in front_intersections:
        px, py = project(*p3d)
        svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="#ff6b6b" stroke="#ffaaaa" stroke-width="1.5"/>\n'

    n_orbits = len(orbits)
    n_pairs = n_orbits * (n_orbits - 1) // 2
    n_crossings = len(unique_intersections)

    svg += f'''
  <!-- Annotation -->
  <text x="{cx}" y="520" fill="#ff9999" font-size="14" font-family="Arial, Helvetica, sans-serif" text-anchor="middle">Red dots = true 3D intersection points ({n_crossings} for {n_orbits} orbits)</text>
  
  <!-- Right panel -->
  <rect x="580" y="130" width="360" height="300" rx="16" fill="#0e1b2c" stroke="#223a53" stroke-width="1.5"/>
  
  <text x="610" y="172" fill="#f0f5fb" font-size="20" font-family="Arial, Helvetica, sans-serif" font-weight="700">The crossing problem</text>
  
  <circle cx="620" cy="215" r="4" fill="#6fd0c1"/>
  <text x="640" y="220" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">{n_orbits} orbits shown</text>
  
  <circle cx="620" cy="253" r="4" fill="#6fd0c1"/>
  <text x="640" y="258" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">Each pair intersects at 2 points</text>
  
  <circle cx="620" cy="291" r="4" fill="#6fd0c1"/>
  <text x="640" y="296" fill="#c7d5e2" font-size="15" font-family="Arial, Helvetica, sans-serif">{n_orbits} orbits → {n_pairs} pairs → {n_pairs * 2} crossings</text>
  
  <circle cx="620" cy="329" r="4" fill="#ff6b6b"/>
  <text x="640" y="334" fill="#ffcccc" font-size="15" font-family="Arial, Helvetica, sans-serif">N orbits → N(N-1) crossing points</text>
  
  <text x="610" y="390" fill="#8899aa" font-size="13" font-family="Arial, Helvetica, sans-serif" font-style="italic">Collision management grows as O(N²)</text>
  
  <text x="610" y="415" fill="#667788" font-size="12" font-family="Arial, Helvetica, sans-serif">This is the Keplerian deadlock:</text>
  <text x="610" y="432" fill="#667788" font-size="12" font-family="Arial, Helvetica, sans-serif">more coverage = more intersections</text>
</svg>'''

    return svg


print(generate_svg())
