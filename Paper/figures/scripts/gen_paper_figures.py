#!/usr/bin/env python
"""Generate publication-style figures for the MDDS manuscript.

The manuscript figures are intentionally conservative: white background,
minimal decoration, journal-readable labels, and color choices that remain
legible when printed in grayscale. This script is the canonical generator for
the figures used by ``Paper/content/manuscript.md``.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]
CONCEPT = ROOT / "concept"
RESULTS = ROOT / "results"

SIGMA_STAR = 1.53  # g m^-2
AU_KM = 1.496e8
R_EARTH_KM = 6371.0
THETA_EARTH_DEG = math.degrees(math.atan(R_EARTH_KM / AU_KM))

BLACK = "#1a1a1a"
GRAY = "#6f6f6f"
LIGHT = "#d9d9d9"
LIGHTER = "#eeeeee"
BLUE = "#2f6f9f"
BLUE_LIGHT = "#7aa6c2"
ORANGE = "#d7852f"
GREEN = "#2a8c6a"
RED = "#b94a48"
PURPLE = "#7a5ea8"


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "mathtext.fontset": "dejavuserif",
            "font.size": 8.5,
            "axes.labelsize": 8.5,
            "axes.titlesize": 9.0,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "legend.fontsize": 7.5,
            "figure.dpi": 140,
            "savefig.dpi": 300,
            "svg.fonttype": "none",
            "axes.edgecolor": BLACK,
            "axes.linewidth": 0.8,
            "grid.color": "#d0d0d0",
            "grid.linewidth": 0.45,
            "grid.alpha": 0.85,
        }
    )


def save(fig: plt.Figure, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    svg_path = base.with_suffix(".svg")
    fig.savefig(svg_path, bbox_inches="tight", pad_inches=0.03)
    svg_path.write_text(
        "\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n",
        encoding="utf-8",
    )
    fig.savefig(
        base.with_suffix(".jpg"),
        bbox_inches="tight",
        pad_inches=0.03,
        facecolor="white",
        dpi=300,
    )
    plt.close(fig)


def beta_min(phi_deg: np.ndarray | float) -> np.ndarray | float:
    return (3.0 * math.sqrt(3.0) / 2.0) * np.sin(np.deg2rad(phi_deg))


def sigma_max(phi_deg: np.ndarray | float) -> np.ndarray | float:
    return SIGMA_STAR / beta_min(phi_deg)


def sync_radius(phi_deg: np.ndarray | float) -> np.ndarray | float:
    return (1.0 - math.sqrt(2.0) * np.tan(np.deg2rad(phi_deg))) ** (1.0 / 3.0)


def arrow(ax, start, end, color=BLACK, lw=1.0, ms=9, style="-|>", **kwargs):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        mutation_scale=ms,
        linewidth=lw,
        color=color,
        shrinkA=0,
        shrinkB=0,
        **kwargs,
    )
    ax.add_patch(patch)
    return patch


def clean_axis(ax) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def orbit_normal(inc_deg: float, node_deg: float) -> np.ndarray:
    inc = math.radians(inc_deg)
    node = math.radians(node_deg)
    normal = np.array(
        [
            math.sin(inc) * math.sin(node),
            -math.sin(inc) * math.cos(node),
            math.cos(inc),
        ]
    )
    return normal / np.linalg.norm(normal)


def orbit_points(inc_deg: float, node_deg: float, n: int = 480) -> np.ndarray:
    theta = np.linspace(0.0, 2.0 * np.pi, n)
    pts = np.column_stack([np.cos(theta), np.sin(theta), np.zeros_like(theta)])
    inc = math.radians(inc_deg)
    node = math.radians(node_deg)
    rx = np.array(
        [
            [1, 0, 0],
            [0, math.cos(inc), -math.sin(inc)],
            [0, math.sin(inc), math.cos(inc)],
        ]
    )
    rz = np.array(
        [
            [math.cos(node), -math.sin(node), 0],
            [math.sin(node), math.cos(node), 0],
            [0, 0, 1],
        ]
    )
    return pts @ rx.T @ rz.T


def project(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    return x + 0.16 * y, 0.92 * z - 0.23 * y


def plot_projected_orbit(ax, pts: np.ndarray, color: str, lw: float = 1.0) -> None:
    x, y = project(pts)
    front = pts[:, 1] <= 0
    for wanted_front, ls, alpha in [(False, (0, (3, 2)), 0.42), (True, "-", 0.95)]:
        mask = front == wanted_front
        start = None
        for i, keep in enumerate(mask):
            if keep and start is None:
                start = i
            if start is not None and (not keep or i == len(mask) - 1):
                end = i if not keep else i + 1
                if end - start > 1:
                    ax.plot(x[start:end], y[start:end], color=color, lw=lw, ls=ls, alpha=alpha)
                start = None


def generate_keplerian_deadlock() -> None:
    fig = plt.figure(figsize=(7.2, 3.3))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.45, 1.0], wspace=0.28)
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    orbits = [(0, 0), (58, 0), (58, 90), (58, 45), (42, 135)]
    colors = [BLUE, ORANGE, GREEN, PURPLE, GRAY]

    shell = Ellipse((0, 0), 2.0, 1.74, facecolor="none", edgecolor=LIGHT, lw=0.9, ls=(0, (3, 2)))
    ax.add_patch(shell)
    for orbit, color in zip(orbits, colors):
        plot_projected_orbit(ax, orbit_points(*orbit), color=color, lw=1.1)

    intersections: list[np.ndarray] = []
    for i in range(len(orbits)):
        for j in range(i + 1, len(orbits)):
            d = np.cross(orbit_normal(*orbits[i]), orbit_normal(*orbits[j]))
            norm = np.linalg.norm(d)
            if norm > 1e-9:
                d = d / norm
                intersections.extend([d, -d])

    unique: list[np.ndarray] = []
    for point in intersections:
        if not any(np.linalg.norm(point - old) < 0.05 for old in unique):
            unique.append(point)
    if unique:
        points = np.array(unique)
        px, py = project(points)
        ax.scatter(px, py, s=18, facecolor="white", edgecolor=RED, linewidth=0.9, zorder=5)

    ax.add_patch(Circle((0, 0), 0.075, facecolor="#f2b05e", edgecolor=BLACK, lw=0.5, zorder=6))
    ax.text(0, -1.03, "(a) same-radius Keplerian planes", ha="center", va="top", color=BLACK)
    ax.text(0.0, 0.98, "pairwise nodal crossings", ha="center", va="bottom", color=RED)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.08, 1.08)
    ax.set_aspect("equal")
    clean_axis(ax)

    planes = np.arange(1, 11)
    node_lines = planes * (planes - 1) / 2
    ax2.plot(planes, node_lines, color=BLACK, lw=1.3)
    ax2.scatter(planes, node_lines, s=16, color=BLUE, zorder=3)
    ax2.set_xlabel("number of orbital planes, $P$")
    ax2.set_ylabel("pairwise nodal lines")
    ax2.set_title(r"$N_{\rm node}=P(P-1)/2$", pad=4)
    ax2.grid(True)
    ax2.set_xlim(1, 10)
    ax2.set_ylim(0, 46)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.text(0.02, -0.25, "(b) topology burden scaling", transform=ax2.transAxes, color=BLACK)

    save(fig, CONCEPT / "keplerian_deadlock")


def generate_force_balance() -> None:
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    clean_axis(ax)
    ax.set_aspect("equal")
    ax.set_xlim(-1.65, 1.75)
    ax.set_ylim(-0.36, 1.35)

    star = np.array([-1.20, 0.0])
    center = np.array([0.0, 0.62])
    body = np.array([1.05, 0.62])

    ax.axhline(star[1], color=LIGHT, lw=0.8, ls=(0, (3, 2)))
    ax.axhline(center[1], color=LIGHT, lw=0.8, ls=(0, (3, 2)))
    ax.plot([center[0], body[0]], [center[1], body[1]], color=GRAY, lw=0.8, ls=(0, (2, 2)))
    ax.plot([star[0], body[0]], [star[1], body[1]], color=LIGHT, lw=0.9)

    ax.add_patch(Circle(star, 0.075, facecolor="#f2b05e", edgecolor=BLACK, lw=0.5))
    ax.add_patch(Circle(center, 0.025, facecolor=BLACK, edgecolor=BLACK))
    ax.add_patch(Circle(body, 0.035, facecolor=BLACK, edgecolor=BLACK))

    g_end = body + 0.68 * (star - body) / np.linalg.norm(star - body)
    sail_end = body + np.array([0.46, 0.55])
    c_end = body + np.array([-0.62, 0.0])
    cf_end = body + np.array([0.46, 0.0])

    arrow(ax, body, g_end, RED, 1.2, 10)
    arrow(ax, body, sail_end, BLUE, 1.2, 10)
    arrow(ax, body, c_end, GREEN, 1.2, 10)
    arrow(ax, body, cf_end, GRAY, 1.0, 9, alpha=0.75)

    ax.text(g_end[0] - 0.05, g_end[1] - 0.08, r"$F_g$", color=RED, ha="right")
    ax.text(sail_end[0] + 0.02, sail_end[1], r"$F_{\rm SRP}$", color=BLUE, ha="left")
    ax.text(c_end[0] - 0.02, c_end[1] + 0.05, r"$F_c$", color=GREEN, ha="right")
    ax.text(cf_end[0] + 0.02, cf_end[1] - 0.07, r"$F_{\rm cf}$", color=GRAY, ha="left")

    phi = math.degrees(math.atan2(body[1] - star[1], body[0] - star[0]))
    ax.add_patch(Arc(star, 0.50, 0.50, theta1=0, theta2=phi, color=BLACK, lw=0.8))
    ax.text(star[0] + 0.31, star[1] + 0.08, r"$\phi$", ha="center")
    ax.text(0.50, 0.55, r"$\rho$", color=GRAY, ha="center", va="top")
    ax.text(star[0] - 0.06, star[1] - 0.11, "star", ha="center", va="top")
    ax.text(center[0], center[1] + 0.09, "displaced\norbit centre", ha="center", va="bottom", color=GRAY)
    ax.text(body[0] + 0.03, body[1] - 0.12, "collector", ha="left", va="top")

    ax.text(
        -1.48,
        1.14,
        r"reduced branch balance:  $F_{\rm SRP}+F_g=F_c$",
        ha="left",
        va="center",
        color=BLACK,
    )
    ax.text(-1.48, -0.31, "Meridional section; lengths are schematic.", color=GRAY, ha="left", va="bottom")
    save(fig, CONCEPT / "force_balance")


def draw_ring(ax, y0: float, color: str, label: str, zorder: int) -> None:
    t = np.linspace(0, 2 * np.pi, 360)
    x = np.cos(t)
    y = 0.35 * np.sin(t) + y0
    back = np.sin(t) < 0
    ax.plot(x[back], y[back], color=color, lw=1.0, ls=(0, (3, 2)), alpha=0.5, zorder=zorder)
    ax.plot(x[~back], y[~back], color=color, lw=1.2, zorder=zorder + 1)
    idx = np.linspace(0, len(t) - 1, 16, dtype=int)
    ax.scatter(x[idx], y[idx], s=10, color=color, edgecolor="white", linewidth=0.35, zorder=zorder + 2)
    ax.text(1.10, y0 + 0.02, label, color=color, ha="left", va="center")


def generate_mdds_stratified() -> None:
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0), gridspec_kw={"width_ratios": [1.6, 0.9]})
    for axis in (ax, ax2):
        clean_axis(axis)

    ax.set_aspect("equal")
    ax.set_xlim(-1.25, 1.55)
    ax.set_ylim(-0.90, 0.92)
    draw_ring(ax, 0.24, BLUE, r"$+\phi$ band", 3)
    draw_ring(ax, 0.00, BLACK, "reference plane", 2)
    draw_ring(ax, -0.24, BLUE, r"$-\phi$ band", 1)
    ax.add_patch(Circle((0, 0), 0.07, facecolor="#f2b05e", edgecolor=BLACK, lw=0.5, zorder=10))
    ax.plot([-1.1, 1.1], [0, 0], color=LIGHT, lw=0.8, zorder=0)
    ax.annotate("", xy=(0.78, 0.24), xytext=(0.78, 0.0), arrowprops=dict(arrowstyle="<->", color=RED, lw=0.9))
    ax.text(0.83, 0.12, r"$z=r\sin\phi$", color=RED, va="center")
    ax.text(0, -0.78, "(a) layered displaced rings", ha="center", color=BLACK)

    ax2.set_xlim(-0.2, 1.1)
    ax2.set_ylim(-0.55, 0.55)
    for y, color, label in [(0.25, BLUE, r"$+\phi$"), (0, BLACK, "0"), (-0.25, BLUE, r"$-\phi$")]:
        ax2.plot([0.15, 0.95], [y, y], color=color, lw=1.4)
        ax2.text(1.0, y, label, color=color, va="center", ha="left")
    ax2.annotate("", xy=(0.5, 0.25), xytext=(0.5, -0.25), arrowprops=dict(arrowstyle="<->", color=RED, lw=0.9))
    ax2.text(0.55, 0, "normal\nseparation", color=RED, va="center")
    ax2.text(0.5, -0.48, "(b) stratification replaces crossings", ha="center", color=BLACK)
    save(fig, CONCEPT / "mdds_stratified_rings")


def generate_support_curves() -> None:
    phi = np.linspace(0.1, 5.0, 400)
    ref = np.array([0.1, 0.5, 1.0])
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.0))

    axes[0].plot(phi, beta_min(phi), color=BLUE, lw=1.5)
    axes[0].scatter(ref, beta_min(ref), color=RED, s=18, zorder=3)
    for p in ref:
        axes[0].annotate(f"{p:g}$^\\circ$", (p, beta_min(p)), xytext=(5, 5), textcoords="offset points")
    axes[0].set_xlabel(r"latitude $\phi$ [deg]")
    axes[0].set_ylabel(r"required lightness number $\beta_{\min}$")
    axes[0].set_title("(a) support requirement", loc="left")
    axes[0].set_xlim(0, 5)
    axes[0].set_ylim(0, 0.235)
    axes[0].grid(True)
    axes[0].spines["top"].set_visible(False)
    axes[0].spines["right"].set_visible(False)

    axes[1].plot(phi, sigma_max(phi), color=GREEN, lw=1.5)
    axes[1].scatter(ref, sigma_max(ref), color=RED, s=18, zorder=3)
    for p in ref:
        axes[1].annotate(f"{sigma_max(p):.1f}", (p, sigma_max(p)), xytext=(5, 5), textcoords="offset points")
    axes[1].set_xlabel(r"latitude $\phi$ [deg]")
    axes[1].set_ylabel(r"supportable areal density $\sigma_{\max}$ [g m$^{-2}$]")
    axes[1].set_title("(b) mass-per-area ceiling", loc="left")
    axes[1].set_xlim(0, 5)
    axes[1].set_ylim(0, 380)
    axes[1].grid(True)
    axes[1].spines["top"].set_visible(False)
    axes[1].spines["right"].set_visible(False)

    save(fig, RESULTS / "support_curves")


def generate_low_latitude_window() -> None:
    labels = [r"$\theta_\oplus$", r"$0.1^\circ$", r"$0.5^\circ$", r"$1.0^\circ$"]
    phis = np.array([THETA_EARTH_DEG, 0.1, 0.5, 1.0])
    values = sigma_max(phis)

    fig, ax = plt.subplots(figsize=(5.7, 3.2))
    x = np.arange(len(labels))
    bars = ax.bar(x, values, color=[ORANGE, BLUE, BLUE_LIGHT, BLUE_LIGHT], edgecolor=BLACK, linewidth=0.6)
    ax.set_yscale("log")
    ax.set_ylabel(r"$\sigma_{\max}$ [g m$^{-2}$]")
    ax.set_xticks(x, labels)
    ax.set_ylim(10, 2.5e4)
    ax.grid(True, axis="y", which="both")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(160, color=GRAY, lw=0.9, ls=(0, (4, 2)))
    ax.text(3.35, 160, "flown sailcraft scale\n(~160 g m$^{-2}$)", color=GRAY, ha="right", va="bottom")
    for rect, val in zip(bars, values):
        label = f"{val/1000:.2f} kg m$^{{-2}}$" if val >= 1000 else f"{val:.1f}"
        ax.text(rect.get_x() + rect.get_width() / 2, val * 1.12, label, ha="center", va="bottom", fontsize=7.2)
    save(fig, RESULTS / "low_latitude_window")


def generate_sync_radius() -> None:
    phi = np.linspace(0, 1.0, 300)
    radius = sync_radius(phi)
    shift = (1.0 - radius) * AU_KM / 1e6
    refs = np.array([0.1, 0.5, 1.0])
    ref_shift = (1.0 - sync_radius(refs)) * AU_KM / 1e6

    fig, ax = plt.subplots(figsize=(5.9, 3.0))
    ax.plot(phi, shift, color=BLUE, lw=1.5)
    ax.scatter(refs, ref_shift, color=RED, s=20, zorder=3)
    for p, s in zip(refs, ref_shift):
        ax.annotate(f"{s:.2f}", (p, s), xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel(r"latitude $\phi$ [deg]")
    ax.set_ylabel(r"inward radius shift [$10^6$ km]")
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, max(shift) * 1.12)
    ax.grid(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax2 = ax.twinx()
    ax2.set_ylim(1.0, min(radius) - 0.001)
    ax2.set_ylabel(r"$r_{\rm sync}$ [AU]")
    ax2.spines["top"].set_visible(False)
    save(fig, RESULTS / "sync_radius")


def generate_support_continuum() -> None:
    fig, ax = plt.subplots(figsize=(6.4, 2.1))
    clean_axis(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    y = 0.55
    ax.plot([0.08, 0.92], [y, y], color=BLACK, lw=1.0)
    ax.scatter([0.08, 0.34, 0.92], [y, y, y], s=[28, 28, 28], color=[BLACK, BLUE, GRAY], zorder=3)
    ax.plot([0.08, 0.34], [y, y], color=BLUE, lw=5.0, alpha=0.35, solid_capstyle="round")
    ax.text(0.08, 0.72, "Keplerian\nswarm", ha="center", va="bottom")
    ax.text(0.34, 0.72, "low-latitude\nMDDS screen", color=BLUE, ha="center", va="bottom")
    ax.text(0.92, 0.72, "statite / bubble\naccess", color=GRAY, ha="center", va="bottom")
    ax.text(0.50, 0.26, "exact high-latitude force-law connection deferred", color=RED, ha="center")
    ax.annotate("", xy=(0.74, 0.42), xytext=(0.42, 0.42), arrowprops=dict(arrowstyle="->", color=RED, lw=0.9))
    save(fig, RESULTS / "support_continuum")


GENERATORS = {
    "keplerian_deadlock": generate_keplerian_deadlock,
    "force_balance": generate_force_balance,
    "mdds_stratified_rings": generate_mdds_stratified,
    "support_curves": generate_support_curves,
    "low_latitude_window": generate_low_latitude_window,
    "sync_radius": generate_sync_radius,
    "support_continuum": generate_support_continuum,
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("figures", nargs="*", choices=sorted(GENERATORS), help="Figures to generate; default: all")
    args = parser.parse_args()
    setup_style()
    names = args.figures or list(GENERATORS)
    for name in names:
        GENERATORS[name]()
        print(f"generated {name}")


if __name__ == "__main__":
    main()
