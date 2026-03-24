#!/usr/bin/env python3
"""Generate manuscript figures 3, 4, 5 using Matplotlib.

These are data-driven figures that benefit from programmatic generation
to ensure numerical accuracy.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

# Configure matplotlib for publication quality
plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 14,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)

# Physical constants
SIGMA_STAR = 1.53  # g/m^2, critical areal density for solar sail
AU_KM = 149_597_870.7  # km per AU

# Output directories
ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)


def beta_min(phi_deg: float | np.ndarray) -> float | np.ndarray:
    """Minimum required lightness number for latitude phi.

    β_min(φ) = (3√3/2) sin(φ)
    """
    return (3.0 * np.sqrt(3.0) / 2.0) * np.sin(np.radians(phi_deg))


def sigma_max(phi_deg: float | np.ndarray) -> float | np.ndarray:
    """Maximum supportable areal density at latitude phi.

    σ_max(φ) = σ* / β_min(φ) = 2σ* / (3√3 sin(φ))
    """
    return SIGMA_STAR / beta_min(phi_deg)


def sync_radius_ratio(phi_deg: float | np.ndarray) -> float | np.ndarray:
    """Earth-synchronous radius as fraction of 1 AU.

    r_sync(φ) / a_⊕ = (1 - √2 tan(φ))^(1/3)
    """
    factor = 1.0 - np.sqrt(2.0) * np.tan(np.radians(phi_deg))
    return np.power(factor, 1.0 / 3.0)


def inward_shift_million_km(phi_deg: float | np.ndarray) -> float | np.ndarray:
    """Inward shift from 1 AU in million km."""
    return (1.0 - sync_radius_ratio(phi_deg)) * AU_KM / 1e6


def generate_fig3_support_curves():
    """Generate Figure 3: Support curves with two panels.

    Panel (a): Full range β_min(φ) with critical thresholds (0-40°)
    Panel (b): Low-latitude detail with β_min and σ_max (0-5°)
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("#0A0E17")

    # Colors
    bg_color = "#0D1520"
    grid_color = "#1E3A5F"
    text_color = "#E0E8F0"
    curve_color = "#00D4FF"  # cyan for β_min
    sigma_color = "#FFD93D"  # gold for σ_max
    threshold_color1 = "#FFD93D"  # gold for β=1
    threshold_color2 = "#FF6B9D"  # pink for β=1.5

    # Critical values from theory
    phi_beta1 = np.degrees(np.arcsin(2 / (3 * np.sqrt(3))))  # ≈ 22.638°
    phi_c = np.degrees(np.arctan(1 / np.sqrt(2)))  # ≈ 35.264°
    beta_at_phi_c = 1.5

    # ============================================================
    # Panel (a): Full range with critical thresholds
    # ============================================================
    ax1.set_facecolor(bg_color)

    phi_full = np.linspace(0.1, 40, 500)
    beta_full = beta_min(phi_full)

    # Plot main curve
    ax1.plot(phi_full, beta_full, color=curve_color, linewidth=2.5, zorder=3)

    # Critical threshold 1: β = 1
    ax1.axhline(
        y=1.0,
        color=threshold_color1,
        linewidth=1.5,
        linestyle="--",
        alpha=0.8,
        zorder=2,
    )
    ax1.plot(
        phi_beta1,
        1.0,
        "s",
        color=threshold_color1,
        markersize=12,
        markeredgecolor="white",
        markeredgewidth=2,
        zorder=4,
    )
    ax1.annotate(
        f"β = 1\nφ ≈ {phi_beta1:.1f}°",
        (phi_beta1, 1.0),
        textcoords="offset points",
        xytext=(-50, 15),
        fontsize=10,
        color=threshold_color1,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor=bg_color,
            edgecolor=threshold_color1,
            alpha=0.95,
        ),
        arrowprops=dict(arrowstyle="->", color=threshold_color1, lw=1.5),
        zorder=5,
    )

    # Critical threshold 2: Branch endpoint
    ax1.axhline(
        y=1.5,
        color=threshold_color2,
        linewidth=1.5,
        linestyle="--",
        alpha=0.8,
        zorder=2,
    )
    ax1.plot(
        phi_c,
        beta_at_phi_c,
        "D",
        color=threshold_color2,
        markersize=12,
        markeredgecolor="white",
        markeredgewidth=2,
        zorder=4,
    )
    ax1.annotate(
        f"Branch endpoint\nφ_c ≈ {phi_c:.1f}°, β = 1.5",
        (phi_c, beta_at_phi_c),
        textcoords="offset points",
        xytext=(10, -40),
        fontsize=10,
        color=threshold_color2,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor=bg_color,
            edgecolor=threshold_color2,
            alpha=0.95,
        ),
        arrowprops=dict(arrowstyle="->", color=threshold_color2, lw=1.5),
        zorder=5,
    )

    # Mark low-latitude reference points
    ref_phis = [0.5, 1.0, 2.0]
    for p in ref_phis:
        b = beta_min(p)
        ax1.plot(
            p,
            b,
            "o",
            color="white",
            markersize=6,
            markeredgecolor=curve_color,
            markeredgewidth=2,
            zorder=4,
        )

    # Shaded regions
    phi_fill = np.linspace(0.1, phi_beta1, 200)
    ax1.fill_between(
        phi_fill, 0, beta_min(phi_fill), alpha=0.15, color=curve_color, zorder=1
    )
    ax1.text(
        10,
        0.35,
        "Low-β MDDS\nregime",
        fontsize=11,
        color=curve_color,
        ha="center",
        fontweight="bold",
    )

    phi_fill2 = np.linspace(phi_beta1, phi_c, 200)
    ax1.fill_between(
        phi_fill2,
        1.0,
        beta_min(phi_fill2),
        alpha=0.15,
        color=threshold_color1,
        zorder=1,
    )
    ax1.text(29, 1.18, "Transition", fontsize=10, color=threshold_color1, ha="center")

    ax1.set_xlabel(r"Latitude $\phi$ [deg]", color=text_color, fontsize=12)
    ax1.set_ylabel(r"$\beta_{\min}$", color=text_color, fontsize=12)
    ax1.set_title(
        r"(a) Full Range with Critical Thresholds",
        color=text_color,
        fontsize=13,
        pad=10,
    )
    ax1.set_xlim(0, 40)
    ax1.set_ylim(0, 1.7)
    ax1.grid(True, color=grid_color, alpha=0.3, linestyle="--")
    ax1.tick_params(colors=text_color)
    for spine in ax1.spines.values():
        spine.set_color(grid_color)

    # ============================================================
    # Panel (b): Low-latitude detail with both β_min and σ_max
    # ============================================================
    ax2.set_facecolor(bg_color)

    phi_low = np.linspace(0.1, 5.0, 500)
    beta_low = beta_min(phi_low)
    sigma_low = sigma_max(phi_low)

    # Plot β_min on left axis
    (line1,) = ax2.plot(
        phi_low,
        beta_low,
        color=curve_color,
        linewidth=2.5,
        label=r"$\beta_{\min}(\phi)$",
    )
    ax2.set_ylabel(r"$\beta_{\min}$", color=curve_color, fontsize=12)
    ax2.tick_params(axis="y", colors=curve_color)
    ax2.set_ylim(0, 0.25)

    # Create secondary y-axis for σ_max
    ax2b = ax2.twinx()
    ax2b.set_facecolor(bg_color)
    (line2,) = ax2b.plot(
        phi_low,
        sigma_low,
        color=sigma_color,
        linewidth=2.5,
        linestyle="--",
        label=r"$\sigma_{\max}(\phi)$",
    )
    ax2b.set_ylabel(r"$\sigma_{\max}$ [g/m²]", color=sigma_color, fontsize=12)
    ax2b.tick_params(axis="y", colors=sigma_color)
    ax2b.set_ylim(0, 80)
    ax2b.spines["right"].set_color(grid_color)

    # Mark reference points on both curves
    for p in ref_phis:
        b = beta_min(p)
        s = sigma_max(p)
        ax2.plot(
            p,
            b,
            "o",
            color="white",
            markersize=8,
            markeredgecolor=curve_color,
            markeredgewidth=2,
            zorder=4,
        )
        ax2b.plot(
            p,
            s,
            "s",
            color="white",
            markersize=8,
            markeredgecolor=sigma_color,
            markeredgewidth=2,
            zorder=4,
        )
        # Annotate with values
        ax2.annotate(
            f"{p}°\nβ={b:.4f}\nσ={s:.1f}",
            (p, b),
            textcoords="offset points",
            xytext=(12, 5),
            fontsize=9,
            color=text_color,
            bbox=dict(
                boxstyle="round,pad=0.2",
                facecolor=bg_color,
                edgecolor=grid_color,
                alpha=0.9,
            ),
        )

    ax2.set_xlabel(r"Latitude $\phi$ [deg]", color=text_color, fontsize=12)
    ax2.set_title(r"(b) Low-Latitude Detail", color=text_color, fontsize=13, pad=10)
    ax2.set_xlim(0, 5)
    ax2.grid(True, color=grid_color, alpha=0.3, linestyle="--")
    ax2.tick_params(axis="x", colors=text_color)
    for spine in ax2.spines.values():
        spine.set_color(grid_color)

    # Combined legend
    lines = [line1, line2]
    labels = [
        r"$\beta_{\min}(\phi) = \frac{3\sqrt{3}}{2}\sin\phi$",
        r"$\sigma_{\max}(\phi) = \frac{2\sigma^*}{3\sqrt{3}\sin\phi}$",
    ]
    ax2.legend(
        lines,
        labels,
        loc="upper right",
        fontsize=9,
        facecolor=bg_color,
        edgecolor=grid_color,
        labelcolor=text_color,
    )

    # Add σ* annotation
    props = dict(
        boxstyle="round,pad=0.3", facecolor="#152238", edgecolor=grid_color, alpha=0.95
    )
    ax2b.text(
        0.98,
        0.02,
        f"$\\sigma^* = {SIGMA_STAR}$ g/m²",
        transform=ax2b.transAxes,
        fontsize=10,
        ha="right",
        va="bottom",
        color=text_color,
        bbox=props,
    )

    plt.tight_layout()

    # Save
    output_path = RESULTS / "fig3_support_curves.png"
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_path}")

    output_pdf = RESULTS / "fig3_support_curves.pdf"
    fig.savefig(output_pdf, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_pdf}")

    plt.close(fig)


def generate_fig4_low_latitude_window():
    """Generate Figure 4: Low-latitude feasibility window bar chart."""

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#0A0E17")

    # Colors
    bg_color = "#0D1520"
    grid_color = "#1E3A5F"
    text_color = "#E0E8F0"
    colors = ["#00D4FF", "#00FF94", "#FF6B9D"]  # cyan, green, pink

    ax.set_facecolor(bg_color)

    # Data
    latitudes = [0.5, 1.0, 2.0]
    sigmas = [sigma_max(p) for p in latitudes]
    labels = ["0.5°", "1°", "2°"]

    # Verified values from manuscript:
    # β_min(0.5°) ≈ 0.0227, σ_max(0.5°) ≈ 67.5 g/m²
    # β_min(1.0°) ≈ 0.0453, σ_max(1.0°) ≈ 33.8 g/m²
    # β_min(2.0°) ≈ 0.0906, σ_max(2.0°) ≈ 16.9 g/m²

    bars = ax.bar(
        labels, sigmas, color=colors, edgecolor="white", linewidth=1.5, width=0.6
    )

    # Add value labels on bars
    for bar, sigma, lat in zip(bars, sigmas, latitudes):
        height = bar.get_height()
        beta = beta_min(lat)
        ax.annotate(
            f"{sigma:.1f} g/m²\n(β = {beta:.4f})",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 8),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color=text_color,
        )

    ax.set_xlabel("Latitude φ", color=text_color, fontsize=13)
    ax.set_ylabel(r"$\sigma_{\max}$ [g/m²]", color=text_color, fontsize=13)
    ax.set_title(
        "Low-Latitude Feasibility Window\nMaximum Supportable Areal Density at Representative Latitudes",
        color=text_color,
        fontsize=14,
        pad=15,
    )
    ax.set_ylim(0, 80)
    ax.grid(True, axis="y", color=grid_color, alpha=0.3, linestyle="--")
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_color(grid_color)

    # Add interpretation text box
    textstr = "\n".join(
        [
            "Key Trend: Window contracts as ~1/φ",
            "",
            "Physical Scale at 1 AU:",
            "  0.5° → 1.3M km separation",
            "  1°   → 2.6M km separation",
            "  2°   → 5.2M km separation",
        ]
    )
    props = dict(
        boxstyle="round,pad=0.5", facecolor="#152238", edgecolor=grid_color, alpha=0.95
    )
    ax.text(
        0.98,
        0.98,
        textstr,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="right",
        color=text_color,
        bbox=props,
        family="monospace",
    )

    plt.tight_layout()

    # Save PNG
    output_path = RESULTS / "fig4_low_latitude_window.png"
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_path}")

    # Save PDF
    output_pdf = RESULTS / "fig4_low_latitude_window.pdf"
    fig.savefig(output_pdf, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_pdf}")

    plt.close(fig)


def generate_fig5_sync_radius():
    """Generate Figure 5: Earth-synchronous radius correction."""

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#0A0E17")

    # Colors
    bg_color = "#0D1520"
    grid_color = "#1E3A5F"
    text_color = "#E0E8F0"
    curve_color = "#FFD93D"  # gold

    ax.set_facecolor(bg_color)

    # Generate curve data
    phi = np.linspace(0.1, 5.0, 500)
    shift = inward_shift_million_km(phi)

    # Reference points from manuscript:
    # 0.5° → r_sync ≈ 0.99587 AU → shift ≈ 0.62 million km
    # 1°   → r_sync ≈ 0.99170 AU → shift ≈ 1.24 million km
    # 2°   → r_sync ≈ 0.98326 AU → shift ≈ 2.50 million km
    ref_phis = [0.5, 1.0, 2.0]
    ref_shifts = [inward_shift_million_km(p) for p in ref_phis]
    ref_radii = [sync_radius_ratio(p) for p in ref_phis]

    # Plot main curve
    ax.plot(
        phi,
        shift,
        color=curve_color,
        linewidth=2.5,
        label=r"$\Delta r = a_\oplus (1 - r_{sync}/a_\oplus)$",
    )

    # Mark reference points
    point_colors = ["#00D4FF", "#00FF94", "#FF6B9D"]
    for p, s, r, c in zip(ref_phis, ref_shifts, ref_radii, point_colors):
        ax.plot(
            p,
            s,
            "o",
            color=c,
            markersize=10,
            markeredgecolor="white",
            markeredgewidth=2,
        )
        ax.annotate(
            f"{p}°\n{s:.2f}M km\n({r:.5f} AU)",
            (p, s),
            textcoords="offset points",
            xytext=(15, 5),
            fontsize=9,
            color=text_color,
            bbox=dict(
                boxstyle="round,pad=0.3", facecolor=bg_color, edgecolor=grid_color
            ),
        )

    ax.set_xlabel(r"Latitude $\phi$ [deg]", color=text_color, fontsize=13)
    ax.set_ylabel("Inward Shift from 1 AU [million km]", color=text_color, fontsize=13)
    ax.set_title(
        r"Earth-Synchronous Radius Correction: $r_{sync}(\phi) = a_\oplus (1 - \sqrt{2}\tan\phi)^{1/3}$",
        color=text_color,
        fontsize=14,
        pad=15,
    )
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 7)
    ax.grid(True, color=grid_color, alpha=0.3, linestyle="--")
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_color(grid_color)

    # Add secondary y-axis for AU
    # When inward shift = 0, r_sync = 1.0 AU (bottom of left axis)
    # When inward shift = 7M km, r_sync ≈ 0.953 AU (top of left axis)
    # So right axis should go from 1.0 (bottom) to ~0.953 (top) - need to invert
    ax2 = ax.twinx()
    ax2.set_facecolor(bg_color)
    ax2.set_ylabel(r"$r_{sync}$ [AU]", color="#8BA4C4", fontsize=12)
    # Set ylim with top value first to invert the axis direction
    r_sync_at_max_shift = 1.0 - 7 / (AU_KM / 1e6)  # ≈ 0.9532 AU
    ax2.set_ylim(1.0, r_sync_at_max_shift)  # 1.0 at bottom, 0.953 at top
    ax2.tick_params(colors="#8BA4C4")
    ax2.spines["right"].set_color(grid_color)
    ax2.spines["top"].set_visible(False)

    # Add interpretation text box
    textstr = "\n".join(
        [
            "Key Insight:",
            "Synchronization modifies orbital radius",
            "but does NOT change support curve β_min(φ)",
            "",
            "Operational geometry ≠ Support penalty",
        ]
    )
    props = dict(
        boxstyle="round,pad=0.5", facecolor="#152238", edgecolor=grid_color, alpha=0.95
    )
    ax.text(
        0.02,
        0.98,
        textstr,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        color=text_color,
        bbox=props,
    )

    plt.tight_layout()

    # Save PNG
    output_path = RESULTS / "fig5_sync_radius_shift.png"
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_path}")

    # Save PDF
    output_pdf = RESULTS / "fig5_sync_radius_shift.pdf"
    fig.savefig(output_pdf, facecolor=fig.get_facecolor(), edgecolor="none")
    print(f"Generated: {output_pdf}")

    plt.close(fig)


def print_verification_values():
    """Print computed values for manual verification against manuscript."""
    print("\n" + "=" * 60)
    print("VERIFICATION: Computed values vs. Manuscript")
    print("=" * 60)

    print(f"\nσ* = {SIGMA_STAR} g/m²")
    print(f"Coefficient (3√3/2) = {3 * np.sqrt(3) / 2:.6f}")
    print(f"Coefficient (2/(3√3)) = {2 / (3 * np.sqrt(3)):.6f}")

    print("\nReference latitudes:")
    for phi in [0.5, 1.0, 2.0]:
        b = beta_min(phi)
        s = sigma_max(phi)
        r = sync_radius_ratio(phi)
        shift = inward_shift_million_km(phi)
        print(f"\n  φ = {phi}°:")
        print(f"    β_min = {b:.6f}")
        print(f"    σ_max = {s:.2f} g/m²")
        print(f"    r_sync/a_⊕ = {r:.6f}")
        print(f"    Inward shift = {shift:.2f} million km")

    print("\n" + "=" * 60)


def main():
    """Generate all matplotlib figures."""
    print("Generating matplotlib figures for MDDS paper...")
    print(f"Output directory: {RESULTS}")

    # Print verification values first
    print_verification_values()

    # Generate figures
    generate_fig3_support_curves()
    generate_fig4_low_latitude_window()
    generate_fig5_sync_radius()

    print("\nAll figures generated successfully!")


if __name__ == "__main__":
    main()
