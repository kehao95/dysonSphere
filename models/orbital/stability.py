"""
Perturbation sensitivity utilities for displaced MDDS orbits.

This module does not attempt a full closed-loop attitude/orbit controller.
Instead, it quantifies how much residual acceleration appears when the sail
lightness number or cone angle deviates from the nominal displaced-orbit
solution.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .displaced_orbit import DisplacedOrbit, P0_1AU


@dataclass(frozen=True)
class PerturbationState:
    """Residual-force summary for a perturbed displaced orbit."""

    phi_deg: float
    beta_nominal: float
    beta_actual: float
    cone_angle_nominal_deg: float
    cone_angle_actual_deg: float
    axial_balance_accel_m_s2: float
    radial_balance_accel_m_s2: float
    axial_residual_accel_m_s2: float
    radial_residual_accel_m_s2: float
    axial_residual_fraction_of_nominal: float
    radial_residual_fraction_of_nominal: float


@dataclass(frozen=True)
class LinearizedPerturbationResponse:
    """Closed-form local response near the minimum-beta cone angle."""

    cone_angle_offset_deg: float
    cone_angle_offset_rad: float
    beta_fraction_error: float
    axial_fraction_approx: float
    radial_fraction_approx: float


def srp_axial_factor(cone_angle_deg: float) -> float:
    """Return ``cos^2(alpha) sin(alpha)``."""
    alpha = math.radians(cone_angle_deg)
    return math.cos(alpha) ** 2 * math.sin(alpha)


def srp_radial_factor(cone_angle_deg: float) -> float:
    """Return ``cos^3(alpha)``."""
    alpha = math.radians(cone_angle_deg)
    return math.cos(alpha) ** 3


def optimal_cone_angle_rad() -> float:
    """Return the low-beta optimal cone angle in radians."""
    return math.atan(1.0 / math.sqrt(2.0))


def linearized_optimal_response(
    cone_angle_offset_deg: float,
    beta_fraction_error: float = 0.0,
) -> LinearizedPerturbationResponse:
    """
    Return the local residual fractions around the optimal cone angle.

    Let ``delta`` be the cone-angle offset in radians and ``eps`` the
    fractional beta error. Around the practical low-beta optimum
    ``alpha_opt = arctan(1/sqrt(2))``, the SRP factors satisfy:

        axial / axial_nominal  ~=  eps - 3 delta^2
        radial / radial_nominal ~= eps - (3/sqrt(2)) delta

    Therefore the axial response is second-order in cone-angle error while the
    radial response is first-order.
    """
    delta_rad = math.radians(cone_angle_offset_deg)
    return LinearizedPerturbationResponse(
        cone_angle_offset_deg=cone_angle_offset_deg,
        cone_angle_offset_rad=delta_rad,
        beta_fraction_error=beta_fraction_error,
        axial_fraction_approx=beta_fraction_error - 3.0 * delta_rad**2,
        radial_fraction_approx=beta_fraction_error - (3.0 / math.sqrt(2.0)) * delta_rad,
    )


def perturbed_force_balance(
    phi_deg: float,
    beta_scale: float = 1.0,
    cone_angle_offset_deg: float = 0.0,
    r_au: float = 1.0,
) -> PerturbationState:
    """
    Return residual accelerations when beta and cone angle deviate from nominal.

    The orbital-rate ratio is held at the nominal minimum-beta solution so the
    returned residuals can be interpreted as the control effort required to stay
    on the original displaced ring.
    """
    orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi_deg)
    nominal = orbit.get_params()
    nominal_fb = orbit.force_balance()

    beta_actual = nominal.beta * beta_scale
    cone_actual_deg = nominal.cone_angle_deg + cone_angle_offset_deg

    g_sun = nominal_fb.gravitational_accel_m_s2
    axial_required = g_sun * math.sin(math.radians(phi_deg))
    radial_required = nominal_fb.sail_radial_accel_m_s2

    axial_actual = g_sun * beta_actual * srp_axial_factor(cone_actual_deg)
    radial_actual = g_sun * beta_actual * srp_radial_factor(cone_actual_deg)

    axial_residual = axial_actual - axial_required
    radial_residual = radial_actual - radial_required

    return PerturbationState(
        phi_deg=phi_deg,
        beta_nominal=nominal.beta,
        beta_actual=beta_actual,
        cone_angle_nominal_deg=nominal.cone_angle_deg,
        cone_angle_actual_deg=cone_actual_deg,
        axial_balance_accel_m_s2=axial_required,
        radial_balance_accel_m_s2=radial_required,
        axial_residual_accel_m_s2=axial_residual,
        radial_residual_accel_m_s2=radial_residual,
        axial_residual_fraction_of_nominal=abs(axial_residual) / axial_required
        if axial_required > 0.0
        else 0.0,
        radial_residual_fraction_of_nominal=abs(radial_residual) / radial_required
        if radial_required > 0.0
        else 0.0,
    )


def cone_angle_tolerance_for_fraction(
    phi_deg: float,
    residual_fraction: float,
    r_au: float = 1.0,
) -> float:
    """
    Return the symmetric cone-angle offset giving the requested axial residual.

    The result is approximate because the axial response is not perfectly
    symmetric away from the optimum, but around the low-beta optimum the
    asymmetry is very small.
    """
    if residual_fraction < 0.0:
        raise ValueError("residual_fraction must be non-negative.")

    lo, hi = 0.0, 30.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        perturbed = perturbed_force_balance(
            phi_deg=phi_deg, beta_scale=1.0, cone_angle_offset_deg=mid, r_au=r_au
        )
        if perturbed.axial_residual_fraction_of_nominal >= residual_fraction:
            hi = mid
        else:
            lo = mid
    return hi


def beta_tolerance_for_fraction(residual_fraction: float) -> float:
    """
    Return the fractional beta error corresponding to an axial residual fraction.

    At fixed cone angle, the axial SRP term scales linearly with beta.
    """
    if residual_fraction < 0.0:
        raise ValueError("residual_fraction must be non-negative.")
    return residual_fraction


def equivalent_beta_fraction_from_pressure(
    disturbance_pressure_n_m2: float,
    distance_au: float = 1.0,
) -> float:
    """
    Convert an external pressure perturbation to an equivalent beta fraction.
    """
    if disturbance_pressure_n_m2 < 0.0:
        raise ValueError("disturbance_pressure_n_m2 must be non-negative.")
    srp_pressure = P0_1AU / (distance_au**2)
    if srp_pressure <= 0.0:
        return 0.0
    return disturbance_pressure_n_m2 / srp_pressure


def drift_time_for_offset(
    residual_accel_m_s2: float,
    offset_distance_m: float,
) -> float:
    """
    Return constant-acceleration drift time to move by ``offset_distance_m``.
    """
    if residual_accel_m_s2 <= 0.0:
        return math.inf
    if offset_distance_m < 0.0:
        raise ValueError("offset_distance_m must be non-negative.")
    return math.sqrt(2.0 * offset_distance_m / residual_accel_m_s2)
