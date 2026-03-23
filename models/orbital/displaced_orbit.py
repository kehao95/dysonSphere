"""
Displaced Orbit Dynamics for Micro-Displaced Dyson Swarm

Based on McInnes (1999) "Solar Sailing: Technology, Dynamics and Mission Applications"

This module calculates the orbital dynamics of solar-sail-displaced orbits,
where solar radiation pressure provides an out-of-plane force component
to maintain non-Keplerian orbits.
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional

# Physical Constants (SI units)
C = 2.998e8  # Speed of light [m/s]
G = 6.674e-11  # Gravitational constant [m³/(kg·s²)]
L_SUN = 3.828e26  # Solar luminosity [W]
M_SUN = 1.989e30  # Solar mass [kg]
AU = 1.496e11  # Astronomical unit [m]

# Derived Constants
SIGMA_STAR = L_SUN / (2 * np.pi * C * G * M_SUN)  # Critical areal density [kg/m²]
# ≈ 1.53e-3 kg/m² = 1.53 g/m²

P0_1AU = L_SUN / (4 * np.pi * C * AU**2)  # Radiation pressure at 1 AU [Pa]
# ≈ 4.56e-6 Pa


@dataclass
class DisplacedOrbitParams:
    """Parameters for a displaced circular orbit."""

    r_au: float  # Orbital radius [AU]
    phi_deg: float  # Displacement angle [degrees]
    beta: float  # Lightness number achieved
    omega: float  # Angular velocity [rad/s]
    period_days: float  # Orbital period [days]
    displacement_km: float  # Vertical displacement [km]


class DisplacedOrbit:
    """
    Calculator for displaced non-Keplerian orbits using solar radiation pressure.

    The orbit is displaced by angle φ above (or below) the ecliptic plane.
    A tilted solar sail provides the out-of-plane force component needed
    to maintain this configuration.
    """

    def __init__(self, r_au: float = 1.0, phi_deg: float = 1.0):
        """
        Initialize displaced orbit calculator.

        Parameters
        ----------
        r_au : float
            Orbital radius in AU (default: 1.0)
        phi_deg : float
            Displacement angle in degrees (default: 1.0)
        """
        self.r_au = r_au
        self.r = r_au * AU  # Convert to meters
        self.phi_deg = phi_deg
        self.phi = np.radians(phi_deg)  # Convert to radians

    def required_beta(self) -> float:
        """
        Calculate the minimum lightness number β required for this displaced orbit.

        For small displacement angles, β ≈ sin(φ).

        Returns
        -------
        float
            Required lightness number (dimensionless)
        """
        # For circular displaced orbit (simplified, small angle approximation)
        # More exact: β = tan(φ) / cos(φ) for pure displacement
        # But accounting for orbital motion, the axial component is:
        # β_axial ≈ sin(φ)

        return np.sin(self.phi)

    def required_beta_exact(self) -> float:
        """
        Calculate exact β required, accounting for orbital dynamics.

        For a circular orbit at radius r, displaced by angle φ:
        The sail must provide both radial and axial force components.

        Returns
        -------
        float
            Required lightness number (exact calculation)
        """
        phi = self.phi

        # For a displaced circular orbit:
        # The required β depends on the orbital angular velocity
        # and the geometric configuration.

        # Simplified model: axial force balance
        # F_grav * sin(φ) = F_rad * sin(θ)
        # where θ is sail tilt angle

        # For optimal steering (sail normal along radial direction modified by tilt):
        # β_required ≈ sin(φ) / cos²(φ) for small φ
        # ≈ tan(φ) * sec(φ)

        # More conservative estimate:
        return np.tan(phi) / np.cos(phi)

    def vertical_displacement(self) -> float:
        """
        Calculate the vertical displacement above/below the ecliptic plane.

        Returns
        -------
        float
            Vertical displacement in kilometers
        """
        d_m = self.r * np.sin(self.phi)
        return d_m / 1000  # Convert to km

    def orbital_period(self) -> float:
        """
        Calculate the orbital period of the displaced orbit.

        For a displaced orbit, the effective radius for period calculation
        is the projected radius in the orbital plane: r_eff = r * cos(φ)

        Returns
        -------
        float
            Orbital period in days
        """
        # Effective radius for Keplerian period
        r_eff = self.r * np.cos(self.phi)

        # Kepler's third law: T² = (4π²/GM) * r³
        T_seconds = 2 * np.pi * np.sqrt(r_eff**3 / (G * M_SUN))

        return T_seconds / (24 * 3600)  # Convert to days

    def angular_velocity(self) -> float:
        """
        Calculate the angular velocity of the displaced orbit.

        Returns
        -------
        float
            Angular velocity in rad/s
        """
        T_seconds = self.orbital_period() * 24 * 3600
        return 2 * np.pi / T_seconds

    def max_areal_density(self) -> float:
        """
        Calculate the maximum allowable system areal density for this orbit.

        σ_max = σ* / β_required

        Returns
        -------
        float
            Maximum areal density in g/m²
        """
        beta = self.required_beta()
        sigma_max_kg_m2 = SIGMA_STAR / beta
        return sigma_max_kg_m2 * 1000  # Convert to g/m²

    def get_params(self) -> DisplacedOrbitParams:
        """
        Get all orbital parameters as a dataclass.

        Returns
        -------
        DisplacedOrbitParams
            Collected orbital parameters
        """
        return DisplacedOrbitParams(
            r_au=self.r_au,
            phi_deg=self.phi_deg,
            beta=self.required_beta(),
            omega=self.angular_velocity(),
            period_days=self.orbital_period(),
            displacement_km=self.vertical_displacement(),
        )

    def __repr__(self) -> str:
        params = self.get_params()
        return (
            f"DisplacedOrbit(\n"
            f"  r = {params.r_au} AU\n"
            f"  φ = {params.phi_deg}°\n"
            f"  β_required = {params.beta:.4f}\n"
            f"  displacement = {params.displacement_km:.2e} km\n"
            f"  period = {params.period_days:.2f} days\n"
            f")"
        )


def parameter_sweep(
    r_au: float = 1.0,
    phi_range_deg: Tuple[float, float] = (0.1, 10.0),
    n_points: int = 100,
) -> dict:
    """
    Sweep displacement angle and calculate key parameters.

    Parameters
    ----------
    r_au : float
        Orbital radius in AU
    phi_range_deg : tuple
        Range of displacement angles (min, max) in degrees
    n_points : int
        Number of points in sweep

    Returns
    -------
    dict
        Dictionary with arrays: phi_deg, beta, displacement_km, sigma_max_g_m2
    """
    phi_values = np.linspace(phi_range_deg[0], phi_range_deg[1], n_points)

    results = {
        "phi_deg": phi_values,
        "beta": np.zeros(n_points),
        "displacement_km": np.zeros(n_points),
        "sigma_max_g_m2": np.zeros(n_points),
    }

    for i, phi in enumerate(phi_values):
        orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi)
        results["beta"][i] = orbit.required_beta()
        results["displacement_km"][i] = orbit.vertical_displacement()
        results["sigma_max_g_m2"][i] = orbit.max_areal_density()

    return results


# Quick reference calculations
if __name__ == "__main__":
    print("=" * 60)
    print("Micro-Displaced Dyson Swarm: Orbital Dynamics")
    print("=" * 60)

    print(f"\nCritical areal density σ* = {SIGMA_STAR * 1000:.3f} g/m²")
    print(f"Radiation pressure at 1 AU = {P0_1AU:.3e} Pa")

    print("\n--- Example Displaced Orbits at 1 AU ---\n")

    for phi in [0.5, 1.0, 2.0, 5.0]:
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=phi)
        params = orbit.get_params()
        print(f"φ = {phi}°:")
        print(f"  β required = {params.beta:.4f}")
        print(f"  Vertical displacement = {params.displacement_km:.2e} km")
        print(f"  Max σ = {orbit.max_areal_density():.1f} g/m²")
        print()
