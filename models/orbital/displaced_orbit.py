"""
Displaced circular orbit dynamics for the Micro-Displaced Dyson Swarm.

This module models an ideal specular solar sail that maintains a circular orbit
at a constant latitude above or below the ecliptic plane. The formulation keeps
the full force balance between gravity, centripetal demand, and solar-radiation
pressure (SRP), rather than collapsing immediately to the small-angle
approximation.

Assumptions
-----------
- Circular heliocentric orbit at fixed spherical radius ``r``.
- Constant displacement angle ``phi`` from the ecliptic.
- Ideal perfectly reflecting sail.
- Sail normal lies in the meridional plane containing the Sun-line and the
  displaced orbit point.
- SRP only; no solar-wind, attitude-control, or multi-body perturbations.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np

# Physical constants (SI units)
C = 2.998e8  # Speed of light [m/s]
G = 6.674e-11  # Gravitational constant [m^3/(kg*s^2)]
L_SUN = 3.828e26  # Solar luminosity [W]
M_SUN = 1.989e30  # Solar mass [kg]
AU = 1.496e11  # Astronomical unit [m]

# Derived constants
MU_SUN = G * M_SUN
SIGMA_STAR = L_SUN / (2 * math.pi * C * G * M_SUN)  # Critical areal density [kg/m^2]
P0_1AU = L_SUN / (4 * math.pi * C * AU**2)  # Radiation pressure at 1 AU [Pa]

# Optimal cone angle for maximizing the axial SRP component per unit beta
OPTIMAL_CONE_ANGLE_RAD = math.atan(1.0 / math.sqrt(2.0))
OPTIMAL_CONE_ANGLE_DEG = math.degrees(OPTIMAL_CONE_ANGLE_RAD)
LOW_BETA_FACTOR = 1.5 * math.sqrt(3.0)  # 3*sqrt(3)/2


@dataclass(frozen=True)
class DisplacedOrbitParams:
    """Minimum-beta solution for a displaced circular orbit."""

    r_au: float
    phi_deg: float
    beta: float
    cone_angle_deg: float
    omega_ratio: float
    omega: float
    period_days: float
    displacement_km: float
    max_areal_density_g_m2: float


@dataclass(frozen=True)
class ForceBalance:
    """Force and acceleration bookkeeping for one displaced orbit solution."""

    phi_deg: float
    beta: float
    cone_angle_deg: float
    omega_ratio: float
    period_days: float
    areal_density_g_m2: float
    displacement_km: float
    gravitational_accel_m_s2: float
    sail_accel_m_s2: float
    sail_radial_accel_m_s2: float
    sail_axial_accel_m_s2: float
    centripetal_accel_m_s2: float
    photon_pressure_n_m2: float
    sail_force_radial_n_m2: float
    sail_force_axial_n_m2: float


class DisplacedOrbit:
    """
    Ideal-sail displaced circular orbit solver.

    The exact force balance in cylindrical coordinates is

    ``beta * cos(alpha)^3 = cos(phi) * (1 - nu^2)``
    ``beta * cos(alpha)^2 * sin(alpha) = sin(phi)``

    where ``alpha`` is the sail cone angle (between the Sun-line and the sail
    normal), ``phi`` is the displacement latitude, and
    ``nu = omega / sqrt(mu / r^3)`` is the orbital-rate ratio relative to the
    Keplerian circular rate at the same heliocentric radius.
    """

    def __init__(self, r_au: float = 1.0, phi_deg: float = 1.0):
        if r_au <= 0:
            raise ValueError("Orbital radius must be positive.")
        if not 0.0 <= phi_deg < 90.0:
            raise ValueError("Displacement angle must be in [0, 90) degrees.")

        self.r_au = r_au
        self.r = r_au * AU
        self.phi_deg = phi_deg
        self.phi = math.radians(phi_deg)

    @property
    def sin_phi(self) -> float:
        return math.sin(self.phi)

    @property
    def cos_phi(self) -> float:
        return math.cos(self.phi)

    @property
    def tan_phi(self) -> float:
        return math.tan(self.phi)

    def keplerian_angular_velocity(self) -> float:
        """Return the Keplerian angular velocity at ``self.r``."""
        return math.sqrt(MU_SUN / self.r**3)

    def keplerian_period_days(self) -> float:
        """Return the Keplerian orbital period at ``self.r`` in days."""
        return 2.0 * math.pi / self.keplerian_angular_velocity() / 86400.0

    def vertical_displacement(self) -> float:
        """Return the vertical displacement above the ecliptic in km."""
        return self.r * self.sin_phi / 1000.0

    def cone_angle_for_omega_ratio(self, omega_ratio: float) -> float:
        """
        Return the sail cone angle for a specified angular-rate ratio.

        ``omega_ratio`` is ``omega / omega_kepler`` and must lie in ``[0, 1)``.
        """
        if not 0.0 <= omega_ratio < 1.0:
            raise ValueError("omega_ratio must lie in [0, 1).")

        denominator = 1.0 - omega_ratio**2
        if denominator <= 0.0:
            raise ValueError("omega_ratio must be strictly less than 1.")

        tan_alpha = self.tan_phi / denominator
        return math.atan(tan_alpha)

    def beta_for_cone_angle(self, cone_angle_deg: float) -> float:
        """Return the required beta for a specified cone angle."""
        alpha = math.radians(cone_angle_deg)
        cos_alpha = math.cos(alpha)
        sin_alpha = math.sin(alpha)
        denominator = cos_alpha**2 * sin_alpha
        if denominator <= 0.0:
            raise ValueError("cone_angle_deg must be between 0 and 90 degrees.")
        return self.sin_phi / denominator

    def beta_for_omega_ratio(self, omega_ratio: float) -> float:
        """Return the required beta for a specified angular-rate ratio."""
        if not 0.0 <= omega_ratio < 1.0:
            raise ValueError("omega_ratio must lie in [0, 1).")

        radial_term = self.cos_phi * (1.0 - omega_ratio**2)
        if radial_term <= 0.0:
            raise ValueError("omega_ratio must keep a positive radial force margin.")

        numerator = (radial_term**2 + self.sin_phi**2) ** 1.5
        denominator = radial_term**2
        return numerator / denominator

    def minimum_beta_solution(self) -> DisplacedOrbitParams:
        """
        Return the minimum-beta solution for the requested displaced orbit.

        For all realistic ``beta < 1`` cases in this project, the relevant
        branch is the low-beta branch:

        ``beta_min = (3*sqrt(3)/2) * sin(phi)``
        ``alpha_opt = arctan(1/sqrt(2)) = 35.264... deg``
        ``omega_ratio^2 = 1 - sqrt(2) * tan(phi)``
        """
        if self.tan_phi <= 1.0 / math.sqrt(2.0):
            beta = LOW_BETA_FACTOR * self.sin_phi
            cone_angle = OPTIMAL_CONE_ANGLE_RAD
            omega_ratio = math.sqrt(max(0.0, 1.0 - math.sqrt(2.0) * self.tan_phi))
        else:
            # High-latitude boundary where the orbit reduces to a static hover.
            beta = 1.0 / self.cos_phi**2
            cone_angle = self.phi
            omega_ratio = 0.0

        omega = omega_ratio * self.keplerian_angular_velocity()
        if omega > 0.0:
            period_days = 2.0 * math.pi / omega / 86400.0
        else:
            period_days = math.inf

        return DisplacedOrbitParams(
            r_au=self.r_au,
            phi_deg=self.phi_deg,
            beta=beta,
            cone_angle_deg=math.degrees(cone_angle),
            omega_ratio=omega_ratio,
            omega=omega,
            period_days=period_days,
            displacement_km=self.vertical_displacement(),
            max_areal_density_g_m2=(SIGMA_STAR / beta) * 1000.0,
        )

    def required_beta(self) -> float:
        """Compatibility alias for the minimum exact beta."""
        return self.minimum_beta_solution().beta

    def required_beta_exact(self) -> float:
        """Compatibility alias for the minimum exact beta."""
        return self.minimum_beta_solution().beta

    def required_beta_small_angle(self) -> float:
        """Return the legacy small-angle estimate ``beta ~= sin(phi)``."""
        return self.sin_phi

    def angular_velocity(self) -> float:
        """Return the minimum-beta angular velocity in rad/s."""
        return self.minimum_beta_solution().omega

    def orbital_period(self) -> float:
        """Return the minimum-beta orbital period in days."""
        return self.minimum_beta_solution().period_days

    def max_areal_density(self) -> float:
        """Return the maximum system areal density in g/m^2."""
        return self.minimum_beta_solution().max_areal_density_g_m2

    def get_params(self) -> DisplacedOrbitParams:
        """Return the minimum-beta solution as a dataclass."""
        return self.minimum_beta_solution()

    def force_balance(
        self,
        beta: float | None = None,
        cone_angle_deg: float | None = None,
        omega_ratio: float | None = None,
        areal_density_g_m2: float | None = None,
    ) -> ForceBalance:
        """
        Compute force balance for a concrete sail configuration.

        If no arguments are given, the minimum-beta solution is used.
        """
        if beta is None or cone_angle_deg is None or omega_ratio is None:
            solution = self.minimum_beta_solution()
            beta = solution.beta if beta is None else beta
            cone_angle_deg = (
                solution.cone_angle_deg if cone_angle_deg is None else cone_angle_deg
            )
            omega_ratio = solution.omega_ratio if omega_ratio is None else omega_ratio

        alpha = math.radians(cone_angle_deg)
        cos_alpha = math.cos(alpha)
        sin_alpha = math.sin(alpha)
        if not 0.0 <= omega_ratio < 1.0:
            raise ValueError("omega_ratio must lie in [0, 1).")

        if areal_density_g_m2 is None:
            areal_density_g_m2 = (SIGMA_STAR / beta) * 1000.0
        sigma_kg_m2 = areal_density_g_m2 / 1000.0

        g_sun = MU_SUN / self.r**2
        sail_accel = beta * g_sun * cos_alpha**2
        sail_radial = sail_accel * cos_alpha
        sail_axial = sail_accel * sin_alpha
        centripetal = g_sun * self.cos_phi - sail_radial
        photon_pressure = 2.0 * P0_1AU * cos_alpha**2 / self.r_au**2

        period_days = math.inf
        if omega_ratio > 0.0:
            omega = omega_ratio * self.keplerian_angular_velocity()
            period_days = 2.0 * math.pi / omega / 86400.0

        return ForceBalance(
            phi_deg=self.phi_deg,
            beta=beta,
            cone_angle_deg=cone_angle_deg,
            omega_ratio=omega_ratio,
            period_days=period_days,
            areal_density_g_m2=areal_density_g_m2,
            displacement_km=self.vertical_displacement(),
            gravitational_accel_m_s2=g_sun,
            sail_accel_m_s2=sail_accel,
            sail_radial_accel_m_s2=sail_radial,
            sail_axial_accel_m_s2=sail_axial,
            centripetal_accel_m_s2=centripetal,
            photon_pressure_n_m2=photon_pressure,
            sail_force_radial_n_m2=sigma_kg_m2 * sail_radial,
            sail_force_axial_n_m2=sigma_kg_m2 * sail_axial,
        )

    @staticmethod
    def max_supported_angle_deg(beta: float) -> float:
        """
        Invert the minimum-beta requirement and return the maximum angle in deg.

        For all realistic ``beta < 1`` cases, the low-beta branch applies:
        ``phi_max = asin(beta / (3*sqrt(3)/2))``.
        """
        if beta <= 0.0:
            return 0.0
        if beta <= 1.5:
            ratio = min(1.0, beta / LOW_BETA_FACTOR)
            return math.degrees(math.asin(ratio))

        # Beyond the low-beta branch, invert beta = sec(phi)^2.
        cos_phi = min(1.0, math.sqrt(1.0 / beta))
        return math.degrees(math.acos(cos_phi))

    def __repr__(self) -> str:
        params = self.minimum_beta_solution()
        return (
            "DisplacedOrbit(\n"
            f"  r = {params.r_au:.3f} AU\n"
            f"  phi = {params.phi_deg:.3f} deg\n"
            f"  beta_min = {params.beta:.5f}\n"
            f"  cone = {params.cone_angle_deg:.3f} deg\n"
            f"  omega/omega_kepler = {params.omega_ratio:.5f}\n"
            f"  displacement = {params.displacement_km:.3e} km\n"
            f"  sigma_max = {params.max_areal_density_g_m2:.2f} g/m^2\n"
            ")"
        )


def parameter_sweep(
    r_au: float = 1.0,
    phi_range_deg: Tuple[float, float] = (0.1, 10.0),
    n_points: int = 100,
) -> Dict[str, np.ndarray]:
    """Sweep displacement angle and report minimum-beta orbit properties."""
    phi_values = np.linspace(phi_range_deg[0], phi_range_deg[1], n_points)

    results = {
        "phi_deg": phi_values,
        "beta_min": np.zeros(n_points),
        "beta_small_angle": np.zeros(n_points),
        "cone_angle_deg": np.zeros(n_points),
        "omega_ratio": np.zeros(n_points),
        "period_days": np.zeros(n_points),
        "displacement_km": np.zeros(n_points),
        "sigma_max_g_m2": np.zeros(n_points),
    }

    for i, phi_deg in enumerate(phi_values):
        orbit = DisplacedOrbit(r_au=r_au, phi_deg=float(phi_deg))
        params = orbit.minimum_beta_solution()
        results["beta_min"][i] = params.beta
        results["beta_small_angle"][i] = orbit.required_beta_small_angle()
        results["cone_angle_deg"][i] = params.cone_angle_deg
        results["omega_ratio"][i] = params.omega_ratio
        results["period_days"][i] = params.period_days
        results["displacement_km"][i] = params.displacement_km
        results["sigma_max_g_m2"][i] = params.max_areal_density_g_m2

    return results


if __name__ == "__main__":
    print("=" * 72)
    print("Micro-Displaced Dyson Swarm: Exact Displaced-Orbit Force Balance")
    print("=" * 72)
    print(f"Critical areal density sigma* = {SIGMA_STAR * 1000:.3f} g/m^2")
    print(f"Radiation pressure at 1 AU = {P0_1AU:.3e} Pa")
    print(f"Optimal cone angle = {OPTIMAL_CONE_ANGLE_DEG:.3f} deg")

    for phi_deg in (0.5, 1.0, 2.0, 5.0):
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=phi_deg)
        params = orbit.minimum_beta_solution()
        print("\n---")
        print(f"phi = {phi_deg:.1f} deg")
        print(f"beta_min = {params.beta:.5f}")
        print(f"cone = {params.cone_angle_deg:.3f} deg")
        print(f"omega/omega_kepler = {params.omega_ratio:.5f}")
        print(f"displacement = {params.displacement_km:.3e} km")
        print(f"sigma_max = {params.max_areal_density_g_m2:.2f} g/m^2")
