"""
Thermal Equilibrium Analysis for MDDS Nodes

Calculates steady-state temperatures for reflector and payload modules
in the decoupled solar sail architecture.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional

# Physical Constants
STEFAN_BOLTZMANN = 5.67e-8  # W/(m²·K⁴)
SOLAR_FLUX_1AU = 1361.0  # W/m² at 1 AU


@dataclass
class ThermalState:
    """Thermal equilibrium state of a component."""

    temperature_k: float
    absorbed_power_w: float
    radiated_power_w: float
    distance_au: float


class ThermalEquilibrium:
    """
    Calculate thermal equilibrium for spacecraft components.

    Steady-state energy balance:
        α * S * A_proj = ε * σ_SB * T⁴ * A_rad

    where:
        α = solar absorptivity
        S = solar flux
        A_proj = projected area facing Sun
        ε = infrared emissivity
        σ_SB = Stefan-Boltzmann constant
        T = equilibrium temperature
        A_rad = radiating area
    """

    def __init__(
        self,
        distance_au: float = 1.0,
        absorptivity: float = 0.1,
        emissivity: float = 0.9,
        area_ratio: float = 2.0,  # A_rad / A_proj (e.g., 2 for flat plate radiating both sides)
    ):
        """
        Initialize thermal equilibrium calculator.

        Parameters
        ----------
        distance_au : float
            Distance from Sun in AU
        absorptivity : float
            Solar absorptivity (0-1)
        emissivity : float
            Infrared emissivity (0-1)
        area_ratio : float
            Ratio of radiating area to projected area
        """
        self.distance_au = distance_au
        self.alpha = absorptivity
        self.epsilon = emissivity
        self.area_ratio = area_ratio

    def solar_flux(self) -> float:
        """Get solar flux at current distance."""
        return SOLAR_FLUX_1AU / (self.distance_au**2)

    def equilibrium_temperature(self) -> float:
        """
        Calculate equilibrium temperature.

        From energy balance:
            T = (α * S / (ε * σ_SB * A_ratio))^(1/4)

        Returns
        -------
        float
            Equilibrium temperature in Kelvin
        """
        S = self.solar_flux()
        T4 = (self.alpha * S) / (self.epsilon * STEFAN_BOLTZMANN * self.area_ratio)
        return T4**0.25

    def equilibrium_temperature_celsius(self) -> float:
        """Return equilibrium temperature in Celsius."""
        return self.equilibrium_temperature() - 273.15

    def get_state(self, area_m2: float = 1.0) -> ThermalState:
        """
        Get full thermal state for a given area.

        Parameters
        ----------
        area_m2 : float
            Projected area facing Sun in m²

        Returns
        -------
        ThermalState
            Complete thermal equilibrium state
        """
        S = self.solar_flux()
        T = self.equilibrium_temperature()

        absorbed = self.alpha * S * area_m2
        radiated = self.epsilon * STEFAN_BOLTZMANN * (T**4) * area_m2 * self.area_ratio

        return ThermalState(
            temperature_k=T,
            absorbed_power_w=absorbed,
            radiated_power_w=radiated,
            distance_au=self.distance_au,
        )


def reflector_temperature(
    distance_au: float = 1.0,
    reflectivity: float = 0.90,
    emissivity_front: float = 0.05,
    emissivity_back: float = 0.90,
) -> float:
    """
    Calculate equilibrium temperature of a thin reflector film.

    For a thin film:
    - Front side faces Sun, reflects most, absorbs little
    - Back side radiates to space

    Parameters
    ----------
    distance_au : float
        Distance from Sun
    reflectivity : float
        Solar reflectivity of front surface
    emissivity_front : float
        IR emissivity of front (reflective) surface
    emissivity_back : float
        IR emissivity of back surface

    Returns
    -------
    float
        Equilibrium temperature in Kelvin
    """
    S = SOLAR_FLUX_1AU / (distance_au**2)
    absorptivity = 1 - reflectivity

    # Energy balance: absorbed = radiated from both sides
    # α * S = (ε_front + ε_back) * σ * T⁴
    total_emissivity = emissivity_front + emissivity_back

    T4 = (absorptivity * S) / (total_emissivity * STEFAN_BOLTZMANN)
    return T4**0.25


def payload_temperature(
    distance_au: float = 1.0,
    pv_efficiency: float = 0.20,
    absorptivity: float = 0.85,
    emissivity: float = 0.85,
) -> float:
    """
    Calculate equilibrium temperature of PV payload module.

    For PV cells, some absorbed energy is converted to electricity,
    reducing the thermal load.

    Energy balance:
        α * S = η * α * S + ε * σ * T⁴ * A_ratio
        (absorbed) = (electrical) + (radiated)

    Parameters
    ----------
    distance_au : float
        Distance from Sun
    pv_efficiency : float
        Electrical conversion efficiency
    absorptivity : float
        Solar absorptivity of PV surface
    emissivity : float
        IR emissivity

    Returns
    -------
    float
        Equilibrium temperature in Kelvin
    """
    S = SOLAR_FLUX_1AU / (distance_au**2)

    # Thermal load = absorbed - converted to electricity
    thermal_load = absorptivity * S * (1 - pv_efficiency)

    # Assuming radiating from back side only (front faces Sun)
    # For double-sided radiation, multiply emissivity by 2
    T4 = thermal_load / (emissivity * STEFAN_BOLTZMANN)
    return T4**0.25


def compare_architectures(distance_au: float = 1.0):
    """
    Compare thermal characteristics of coupled vs decoupled architectures.

    Coupled: Same surface must reflect AND generate power
    Decoupled: Separate reflector and PV modules
    """
    print(f"\n=== Thermal Comparison at {distance_au} AU ===\n")

    # Decoupled architecture
    T_refl = reflector_temperature(
        distance_au=distance_au,
        reflectivity=0.90,
        emissivity_front=0.05,
        emissivity_back=0.90,
    )

    T_payload = payload_temperature(
        distance_au=distance_au, pv_efficiency=0.20, absorptivity=0.85, emissivity=0.85
    )

    print("DECOUPLED Architecture:")
    print(f"  Reflector: {T_refl:.1f} K ({T_refl - 273.15:.1f} °C)")
    print(f"  Payload:   {T_payload:.1f} K ({T_payload - 273.15:.1f} °C)")

    # Coupled architecture (hypothetical sail that also generates power)
    # Must absorb significantly to generate power, increasing temperature
    T_coupled = payload_temperature(
        distance_au=distance_au,
        pv_efficiency=0.10,  # Lower efficiency due to compromise
        absorptivity=0.50,  # Must absorb for power
        emissivity=0.50,  # Compromise between reflection and emission
    )

    print("\nCOUPLED Architecture (hypothetical):")
    print(f"  Combined:  {T_coupled:.1f} K ({T_coupled - 273.15:.1f} °C)")

    print("\n→ Decoupled reflector is significantly cooler")
    print("→ Reduced thermal stress on thin film materials")


if __name__ == "__main__":
    print("=" * 60)
    print("Thermal Analysis: Micro-Displaced Dyson Swarm")
    print("=" * 60)

    compare_architectures(distance_au=1.0)

    print("\n--- Temperature vs Distance ---\n")
    print(f"{'Distance [AU]':>12} {'Reflector [K]':>14} {'Payload [K]':>12}")
    print("-" * 42)

    for d in [0.5, 0.7, 1.0, 1.5, 2.0]:
        T_r = reflector_temperature(distance_au=d)
        T_p = payload_temperature(distance_au=d)
        print(f"{d:>12.1f} {T_r:>14.1f} {T_p:>12.1f}")
