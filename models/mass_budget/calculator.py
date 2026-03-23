"""
Mass Budget Calculator for Micro-Displaced Dyson Swarm Nodes

Calculates system-level lightness number β and determines feasibility
of various payload/reflector configurations.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple
from .materials import get_material, Material, REFLECTOR_MATERIALS, PV_MATERIALS

# Import constants from orbital module
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from orbital.displaced_orbit import SIGMA_STAR


@dataclass
class MassBreakdown:
    """Detailed mass breakdown of a MDDS node."""

    reflector_area_m2: float
    reflector_mass_kg: float
    pv_area_m2: float
    pv_mass_kg: float
    structure_mass_kg: float
    total_mass_kg: float
    system_areal_density_g_m2: float
    system_beta: float


class SystemBudget:
    """
    Mass budget calculator for a decoupled solar sail node.

    The node consists of:
    - Reflector: Large-area thin film for thrust generation
    - Payload: PV cells + electronics for power/computation
    - Structure: Booms, tethers, deployment mechanisms
    """

    def __init__(
        self,
        reflector_material: str = "kapton_al_1um",
        pv_material: str = "cigs_flex",
        reflector_area_m2: float = 1000.0,
        pv_area_m2: float = 10.0,
        structure_mass_kg: float = 1.0,
    ):
        """
        Initialize mass budget calculator.

        Parameters
        ----------
        reflector_material : str
            Key for reflector material from database
        pv_material : str
            Key for PV material from database
        reflector_area_m2 : float
            Total reflector area in m²
        pv_area_m2 : float
            Total PV cell area in m²
        structure_mass_kg : float
            Mass of structural components (booms, tethers) in kg
        """
        self.reflector = get_material(reflector_material)
        self.pv = get_material(pv_material)
        self.A_r = reflector_area_m2
        self.A_p = pv_area_m2
        self.m_s = structure_mass_kg

    def reflector_mass(self) -> float:
        """Calculate reflector mass in kg."""
        # Convert g/m² to kg/m²
        sigma_r = self.reflector.areal_density / 1000
        return sigma_r * self.A_r

    def pv_mass(self) -> float:
        """Calculate PV cell mass in kg."""
        sigma_p = self.pv.areal_density / 1000
        return sigma_p * self.A_p

    def total_mass(self) -> float:
        """Calculate total system mass in kg."""
        return self.reflector_mass() + self.pv_mass() + self.m_s

    def system_areal_density(self) -> float:
        """
        Calculate system areal density σ_sys = m_total / A_reflector.

        Returns
        -------
        float
            System areal density in g/m²
        """
        m_total = self.total_mass()
        sigma_sys_kg_m2 = m_total / self.A_r
        return sigma_sys_kg_m2 * 1000  # Convert to g/m²

    def system_beta(self) -> float:
        """
        Calculate system lightness number β = σ* / σ_sys.

        Returns
        -------
        float
            System lightness number (dimensionless)
        """
        sigma_sys_kg_m2 = self.system_areal_density() / 1000
        return SIGMA_STAR / sigma_sys_kg_m2

    def max_displacement_angle(self) -> float:
        """
        Calculate maximum displacement angle achievable (small angle approx).

        For small φ: β ≈ sin(φ), so φ ≈ arcsin(β)

        Returns
        -------
        float
            Maximum displacement angle in degrees
        """
        beta = self.system_beta()
        if beta >= 1:
            return 90.0  # Full levitation
        phi_rad = np.arcsin(beta)
        return np.degrees(phi_rad)

    def power_output(self, solar_flux_w_m2: float = 1361.0) -> float:
        """
        Calculate electrical power output from PV cells.

        Parameters
        ----------
        solar_flux_w_m2 : float
            Solar flux at operating distance (default: 1361 W/m² at 1 AU)

        Returns
        -------
        float
            Electrical power output in Watts
        """
        return self.A_p * solar_flux_w_m2 * self.pv.efficiency

    def get_breakdown(self) -> MassBreakdown:
        """
        Get complete mass breakdown.

        Returns
        -------
        MassBreakdown
            Detailed mass breakdown dataclass
        """
        return MassBreakdown(
            reflector_area_m2=self.A_r,
            reflector_mass_kg=self.reflector_mass(),
            pv_area_m2=self.A_p,
            pv_mass_kg=self.pv_mass(),
            structure_mass_kg=self.m_s,
            total_mass_kg=self.total_mass(),
            system_areal_density_g_m2=self.system_areal_density(),
            system_beta=self.system_beta(),
        )

    def __repr__(self) -> str:
        bd = self.get_breakdown()
        return (
            f"SystemBudget:\n"
            f"  Reflector: {self.reflector.name}\n"
            f"    Area = {bd.reflector_area_m2:.1f} m²\n"
            f"    Mass = {bd.reflector_mass_kg:.3f} kg\n"
            f"  PV: {self.pv.name}\n"
            f"    Area = {bd.pv_area_m2:.1f} m²\n"
            f"    Mass = {bd.pv_mass_kg:.3f} kg\n"
            f"  Structure: {bd.structure_mass_kg:.3f} kg\n"
            f"  ───────────────────────\n"
            f"  Total mass: {bd.total_mass_kg:.3f} kg\n"
            f"  System σ: {bd.system_areal_density_g_m2:.2f} g/m²\n"
            f"  System β: {bd.system_beta:.4f}\n"
            f"  Max φ: {self.max_displacement_angle():.2f}°\n"
            f"  Power: {self.power_output():.1f} W\n"
        )


def find_optimal_ratio(
    target_beta: float,
    reflector_material: str = "kapton_al_1um",
    pv_material: str = "cigs_flex",
    structure_fraction: float = 0.1,
    pv_power_required_w: float = 100.0,
) -> Optional[SystemBudget]:
    """
    Find the reflector area needed for a given target β and power requirement.

    Parameters
    ----------
    target_beta : float
        Target system lightness number
    reflector_material : str
        Key for reflector material
    pv_material : str
        Key for PV material
    structure_fraction : float
        Structure mass as fraction of total non-reflector mass
    pv_power_required_w : float
        Required electrical power output in Watts

    Returns
    -------
    SystemBudget or None
        Optimized system budget, or None if infeasible
    """
    refl = get_material(reflector_material)
    pv = get_material(pv_material)

    # Required PV area for power
    solar_flux = 1361.0  # W/m² at 1 AU
    A_p = pv_power_required_w / (solar_flux * pv.efficiency)

    # PV mass
    m_p = (pv.areal_density / 1000) * A_p  # kg

    # Structure mass (as fraction of payload)
    m_s = structure_fraction * m_p

    # Payload mass (non-reflector)
    m_payload = m_p + m_s

    # Required system areal density for target β
    # β = σ* / σ_sys
    # σ_sys = σ* / β
    sigma_sys_target = (SIGMA_STAR / target_beta) * 1000  # g/m²

    # Reflector areal density
    sigma_r = refl.areal_density  # g/m²

    # System: σ_sys = (m_r + m_payload) / A_r
    #              = σ_r + m_payload / A_r
    # Therefore: A_r = m_payload / (σ_sys - σ_r)

    denominator = sigma_sys_target - sigma_r
    if denominator <= 0:
        # Reflector alone is too heavy
        print(
            f"Infeasible: reflector σ = {sigma_r:.2f} g/m² > target σ_sys = {sigma_sys_target:.2f} g/m²"
        )
        return None

    A_r = (m_payload * 1000) / denominator  # Convert kg to g, then divide

    # Check if result is reasonable
    if A_r < A_p:
        print(f"Warning: reflector area ({A_r:.1f} m²) < PV area ({A_p:.1f} m²)")

    return SystemBudget(
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=A_r,
        pv_area_m2=A_p,
        structure_mass_kg=m_s,
    )


def design_space_sweep(
    beta_range: Tuple[float, float] = (0.01, 0.1),
    power_range: Tuple[float, float] = (10, 1000),
    n_points: int = 20,
    reflector_material: str = "kapton_al_1um",
    pv_material: str = "cigs_flex",
) -> dict:
    """
    Sweep design space to find feasible configurations.

    Returns
    -------
    dict
        Arrays of beta, power, reflector_area, total_mass, feasible
    """
    betas = np.linspace(beta_range[0], beta_range[1], n_points)
    powers = np.linspace(power_range[0], power_range[1], n_points)

    results = {
        "beta": [],
        "power_w": [],
        "reflector_area_m2": [],
        "total_mass_kg": [],
        "feasible": [],
    }

    for beta in betas:
        for power in powers:
            budget = find_optimal_ratio(
                target_beta=beta,
                pv_power_required_w=power,
                reflector_material=reflector_material,
                pv_material=pv_material,
            )

            results["beta"].append(beta)
            results["power_w"].append(power)

            if budget is not None:
                results["reflector_area_m2"].append(budget.A_r)
                results["total_mass_kg"].append(budget.total_mass())
                results["feasible"].append(True)
            else:
                results["reflector_area_m2"].append(np.nan)
                results["total_mass_kg"].append(np.nan)
                results["feasible"].append(False)

    # Convert to numpy arrays
    for key in results:
        results[key] = np.array(results[key])

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("Mass Budget Calculator: Micro-Displaced Dyson Swarm Node")
    print("=" * 70)

    print(f"\nCritical areal density σ* = {SIGMA_STAR * 1000:.3f} g/m²")

    # Example 1: Baseline configuration
    print("\n--- Example 1: Baseline Configuration ---\n")
    budget = SystemBudget(
        reflector_material="kapton_al_1um",
        pv_material="cigs_flex",
        reflector_area_m2=1000,
        pv_area_m2=10,
        structure_mass_kg=1.0,
    )
    print(budget)

    # Example 2: Find optimal for target β
    print("\n--- Example 2: Design for β = 0.02, 100W ---\n")
    optimal = find_optimal_ratio(
        target_beta=0.02,
        pv_power_required_w=100,
        reflector_material="kapton_al_1um",
        pv_material="cigs_flex",
    )
    if optimal:
        print(optimal)

    # Example 3: Compare materials
    print("\n--- Example 3: Material Comparison (100W, β=0.03) ---\n")
    for refl in ["kapton_al_2um", "kapton_al_1um", "cp1_al"]:
        print(f"\nReflector: {refl}")
        opt = find_optimal_ratio(
            target_beta=0.03, pv_power_required_w=100, reflector_material=refl
        )
        if opt:
            print(f"  Reflector area needed: {opt.A_r:.1f} m²")
            print(f"  Total mass: {opt.total_mass():.2f} kg")
