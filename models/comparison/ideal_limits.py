"""
Idealized comparison baselines for Dyson Swarm, Dyson Ring, and MDDS.

These functions intentionally ignore material aging, thermal degradation,
maintenance, and control losses so that all architectures are compared under the
same clean upper-bound assumptions.
"""

from __future__ import annotations

import math

from models.orbital.displaced_orbit import AU, L_SUN


def stellar_flux(radius_au: float = 1.0, luminosity_w: float = L_SUN) -> float:
    """Return stellar irradiance at ``radius_au``."""
    radius_m = radius_au * AU
    return luminosity_w / (4.0 * math.pi * radius_m**2)


def shell_area(radius_au: float = 1.0) -> float:
    """Return the area of a full spherical shell at ``radius_au``."""
    radius_m = radius_au * AU
    return 4.0 * math.pi * radius_m**2


def collector_power(
    collector_area_m2: float,
    efficiency: float,
    radius_au: float = 1.0,
    luminosity_w: float = L_SUN,
) -> float:
    """Return ideal electrical power from collector area ``collector_area_m2``."""
    return collector_area_m2 * efficiency * stellar_flux(
        radius_au=radius_au, luminosity_w=luminosity_w
    )


def shell_coverage_from_area(collector_area_m2: float, radius_au: float = 1.0) -> float:
    """Return the shell-coverage fraction of a collector area."""
    return collector_area_m2 / shell_area(radius_au=radius_au)


def ideal_swarm_power(
    efficiency: float,
    coverage_fraction: float = 1.0,
    luminosity_w: float = L_SUN,
) -> float:
    """
    Return the ideal Dyson-Swarm power upper bound.

    ``coverage_fraction = 1`` corresponds to complete 4*pi coverage.
    """
    if not 0.0 <= coverage_fraction <= 1.0:
        raise ValueError("coverage_fraction must lie in [0, 1].")
    return efficiency * coverage_fraction * luminosity_w


def ring_capture_fraction(half_angle_deg: float) -> float:
    """
    Return the luminosity fraction intercepted by a complete spherical band.

    The band is centered on the equatorial plane and spans latitudes
    ``[-half_angle_deg, +half_angle_deg]`` on a sphere of radius ``r``.
    """
    if not 0.0 <= half_angle_deg <= 90.0:
        raise ValueError("half_angle_deg must lie in [0, 90].")
    return math.sin(math.radians(half_angle_deg))


def equivalent_ring_half_angle_deg(capture_fraction: float) -> float:
    """Invert ``ring_capture_fraction`` and return the equivalent band half-angle."""
    if not 0.0 <= capture_fraction <= 1.0:
        raise ValueError("capture_fraction must lie in [0, 1].")
    return math.degrees(math.asin(capture_fraction))


def ideal_ring_power(
    half_angle_deg: float,
    efficiency: float,
    luminosity_w: float = L_SUN,
) -> float:
    """
    Return the ideal Dyson-Ring power upper bound for a complete spherical band.
    """
    return efficiency * ring_capture_fraction(half_angle_deg) * luminosity_w


def mdds_relative_to_ideal_swarm(
    pv_fill_factor: float,
    mdds_efficiency: float,
    swarm_efficiency: float,
) -> float:
    """
    Return MDDS power relative to an ideal Dyson Swarm under controlled variables.

    If both architectures use the same PV technology, this reduces to the PV
    fill factor ``pv_fill_factor``.
    """
    if swarm_efficiency <= 0.0:
        raise ValueError("swarm_efficiency must be positive.")
    if pv_fill_factor < 0.0:
        raise ValueError("pv_fill_factor must be non-negative.")
    effective_fill_factor = min(1.0, pv_fill_factor)
    return effective_fill_factor * mdds_efficiency / swarm_efficiency


def required_efficiency_ratio_to_match_swarm(pv_fill_factor: float) -> float:
    """
    Return the efficiency multiplier MDDS needs to match an ideal Dyson Swarm.
    """
    effective_fill_factor = min(1.0, pv_fill_factor)
    if effective_fill_factor <= 0.0:
        return math.inf
    return 1.0 / effective_fill_factor
