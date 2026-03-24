"""
Mass-budget and utilization calculations for decoupled MDDS nodes.

The most important design variable is the PV fill factor

    lambda = A_pv / A_reflector

because it simultaneously determines:
- payload power density,
- relative energy utilization versus an all-collector Dyson Swarm, and
- the areal-density penalty that reduces the achievable displacement angle.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np

from models.orbital.displaced_orbit import DisplacedOrbit, SIGMA_STAR
from models.structural.geometry import NodeStructure, StructuralDesignResult

from .materials import Material, get_material


@dataclass(frozen=True)
class MassBreakdown:
    """Detailed mass breakdown of a single MDDS node."""

    reflector_area_m2: float
    reflector_mass_kg: float
    pv_area_m2: float
    pv_mass_kg: float
    structure_mass_kg: float
    total_mass_kg: float
    reflector_areal_density_g_m2: float
    pv_areal_density_g_m2: float
    structure_areal_density_g_m2: float
    system_areal_density_g_m2: float
    system_beta: float
    pv_fill_factor: float
    absolute_utilization: float
    relative_dyson_utilization: float


@dataclass(frozen=True)
class AngleFeasibility:
    """Feasibility summary for a target displacement angle and material pair."""

    phi_deg: float
    beta_required: float
    sigma_limit_g_m2: float
    pv_fill_factor_max: float
    absolute_utilization_max: float
    relative_dyson_utilization_max: float
    reflector_material: str
    pv_material: str
    feasible: bool


@dataclass(frozen=True)
class PowerAngleDesign:
    """Solved node design for a target power and displacement angle."""

    phi_deg: float
    power_required_w: float
    reflector_material: str
    pv_material: str
    reflector_area_m2: float
    pv_area_m2: float
    pv_fill_factor: float
    structure_mass_kg: float
    structure_areal_density_g_m2: float
    system_areal_density_g_m2: float
    sigma_limit_g_m2: float
    achieved_power_w: float
    feasible: bool


@dataclass(frozen=True)
class FillFactorPowerThreshold:
    """Minimum-power node design that achieves a target PV fill factor."""

    phi_deg: float
    target_fill_factor: float
    reflector_material: str
    pv_material: str
    reflector_area_m2: float
    pv_area_m2: float
    power_w: float
    structure_mass_kg: float
    structure_areal_density_g_m2: float
    system_areal_density_g_m2: float
    sigma_limit_g_m2: float
    margin_g_m2: float
    feasible: bool


@dataclass(frozen=True)
class FixedMassAllowance:
    """Maximum fixed bus/control mass allowed for a target angle, fill factor, and power."""

    phi_deg: float
    power_required_w: float
    target_fill_factor: float
    reflector_material: str
    pv_material: str
    reflector_area_m2: float
    pv_area_m2: float
    reflector_mass_kg: float
    pv_mass_kg: float
    variable_structure_mass_kg: float
    total_mass_budget_kg: float
    fixed_mass_max_kg: float
    sigma_limit_g_m2: float
    feasible: bool


class SystemBudget:
    """
    Mass budget calculator for a decoupled MDDS node.

    Parameters are expressed for one reflector-payload unit. The "structure"
    term captures all non-reflector, non-PV hardware that still scales with the
    node area, such as booms, tethers, deployment hardware, and avionics mass
    amortized over the reflector footprint.
    """

    def __init__(
        self,
        reflector_material: str = "cp1_subsystem_nasa_2009",
        pv_material: str = "cigs_space_projection_2002",
        reflector_area_m2: float = 1000.0,
        pv_area_m2: float = 100.0,
        structure_mass_kg: float = 0.0,
    ):
        if reflector_area_m2 <= 0.0:
            raise ValueError("reflector_area_m2 must be positive.")
        if pv_area_m2 < 0.0:
            raise ValueError("pv_area_m2 must be non-negative.")
        if structure_mass_kg < 0.0:
            raise ValueError("structure_mass_kg must be non-negative.")

        self.reflector = get_material(reflector_material)
        self.pv = get_material(pv_material)
        self.A_r = reflector_area_m2
        self.A_p = pv_area_m2
        self.m_s = structure_mass_kg

    @classmethod
    def from_fill_factor(
        cls,
        reflector_material: str,
        pv_material: str,
        fill_factor: float,
        reflector_area_m2: float = 1.0,
        extra_areal_density_g_m2: float = 0.0,
    ) -> "SystemBudget":
        """
        Create a system budget from the PV fill factor lambda = A_p / A_r.

        ``extra_areal_density_g_m2`` captures non-PV, non-reflector mass as an
        areal-density equivalent distributed over the reflector footprint.
        """
        if fill_factor < 0.0:
            raise ValueError("fill_factor must be non-negative.")
        if extra_areal_density_g_m2 < 0.0:
            raise ValueError("extra_areal_density_g_m2 must be non-negative.")

        structure_mass_kg = reflector_area_m2 * extra_areal_density_g_m2 / 1000.0
        return cls(
            reflector_material=reflector_material,
            pv_material=pv_material,
            reflector_area_m2=reflector_area_m2,
            pv_area_m2=reflector_area_m2 * fill_factor,
            structure_mass_kg=structure_mass_kg,
        )

    def pv_fill_factor(self) -> float:
        """Return lambda = A_p / A_r."""
        return self.A_p / self.A_r

    def reflector_mass(self) -> float:
        """Return reflector mass in kg."""
        return (self.reflector.areal_density / 1000.0) * self.A_r

    def pv_mass(self) -> float:
        """Return PV mass in kg."""
        return (self.pv.areal_density / 1000.0) * self.A_p

    def structure_areal_density(self) -> float:
        """Return extra structural areal density in g/m^2."""
        return 1000.0 * self.m_s / self.A_r

    def total_mass(self) -> float:
        """Return total mass in kg."""
        return self.reflector_mass() + self.pv_mass() + self.m_s

    def system_areal_density(self) -> float:
        """Return total areal density sigma_sys in g/m^2."""
        return 1000.0 * self.total_mass() / self.A_r

    def system_beta(self) -> float:
        """Return the system lightness number beta = sigma* / sigma_sys."""
        sigma_sys_kg_m2 = self.system_areal_density() / 1000.0
        return SIGMA_STAR / sigma_sys_kg_m2

    def max_displacement_angle_deg(self) -> float:
        """Return the maximum exact displacement angle supported by this node."""
        return DisplacedOrbit.max_supported_angle_deg(self.system_beta())

    def power_output(self, solar_flux_w_m2: float = 1361.0) -> float:
        """Return electrical output in W."""
        efficiency = self.pv.efficiency or 0.0
        return self.A_p * solar_flux_w_m2 * efficiency

    def electrical_power_density(self, solar_flux_w_m2: float = 1361.0) -> float:
        """Return electrical output per reflector area in W/m^2."""
        return self.power_output(solar_flux_w_m2=solar_flux_w_m2) / self.A_r

    def absolute_utilization(self) -> float:
        """
        Return electrical utilization versus incident stellar flux on reflector area.

        This equals ``lambda * eta_pv`` for the decoupled architecture.
        """
        return self.pv_fill_factor() * (self.pv.efficiency or 0.0)

    def relative_dyson_utilization(self, reference_efficiency: float | None = None) -> float:
        """
        Return utilization relative to an all-collector Dyson Swarm.

        If ``reference_efficiency`` is omitted, we compare against a Dyson Swarm
        using the same PV technology over the full shell area, so the ratio
        reduces to the PV fill factor ``lambda``.
        """
        if reference_efficiency is None:
            reference_efficiency = self.pv.efficiency or 0.0
        if reference_efficiency <= 0.0:
            return 0.0
        return self.absolute_utilization() / reference_efficiency

    def get_breakdown(self) -> MassBreakdown:
        """Return a structured mass/utilization summary."""
        return MassBreakdown(
            reflector_area_m2=self.A_r,
            reflector_mass_kg=self.reflector_mass(),
            pv_area_m2=self.A_p,
            pv_mass_kg=self.pv_mass(),
            structure_mass_kg=self.m_s,
            total_mass_kg=self.total_mass(),
            reflector_areal_density_g_m2=self.reflector.areal_density,
            pv_areal_density_g_m2=self.pv.areal_density,
            structure_areal_density_g_m2=self.structure_areal_density(),
            system_areal_density_g_m2=self.system_areal_density(),
            system_beta=self.system_beta(),
            pv_fill_factor=self.pv_fill_factor(),
            absolute_utilization=self.absolute_utilization(),
            relative_dyson_utilization=self.relative_dyson_utilization(),
        )

    def __repr__(self) -> str:
        bd = self.get_breakdown()
        return (
            "SystemBudget(\n"
            f"  reflector = {self.reflector.name}\n"
            f"  pv = {self.pv.name}\n"
            f"  lambda = {bd.pv_fill_factor:.3f}\n"
            f"  sigma_sys = {bd.system_areal_density_g_m2:.2f} g/m^2\n"
            f"  beta = {bd.system_beta:.5f}\n"
            f"  phi_max = {self.max_displacement_angle_deg():.3f} deg\n"
            f"  eta_abs = {bd.absolute_utilization:.4f}\n"
            f"  eta_rel = {bd.relative_dyson_utilization:.4f}\n"
            ")"
        )


def max_fill_factor_for_angle(
    phi_deg: float,
    reflector_material: str,
    pv_material: str,
    extra_areal_density_g_m2: float = 0.0,
    r_au: float = 1.0,
) -> AngleFeasibility:
    """
    Return the maximum PV fill factor allowed by the displaced-orbit mass budget.

    The total areal density constraint is

        sigma_reflector + lambda * sigma_pv + sigma_extra <= sigma_max(phi)
    """
    orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi_deg)
    sigma_limit = orbit.max_areal_density()
    reflector = get_material(reflector_material)
    pv = get_material(pv_material)

    numerator = sigma_limit - reflector.areal_density - extra_areal_density_g_m2
    fill_factor_max = max(0.0, numerator / pv.areal_density)
    candidate = SystemBudget.from_fill_factor(
        reflector_material=reflector_material,
        pv_material=pv_material,
        fill_factor=fill_factor_max,
        reflector_area_m2=1.0,
        extra_areal_density_g_m2=extra_areal_density_g_m2,
    )

    return AngleFeasibility(
        phi_deg=phi_deg,
        beta_required=orbit.required_beta_exact(),
        sigma_limit_g_m2=sigma_limit,
        pv_fill_factor_max=fill_factor_max,
        absolute_utilization_max=candidate.absolute_utilization(),
        relative_dyson_utilization_max=candidate.relative_dyson_utilization(),
        reflector_material=reflector_material,
        pv_material=pv_material,
        feasible=fill_factor_max > 0.0,
    )


def find_optimal_ratio(
    target_beta: float,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "cigs_space_projection_2002",
    extra_areal_density_g_m2: float = 0.0,
    pv_power_required_w: float = 100.0,
    solar_flux_w_m2: float = 1361.0,
) -> Optional[SystemBudget]:
    """
    Solve for the reflector area required to meet a target beta and power output.
    """
    if target_beta <= 0.0:
        raise ValueError("target_beta must be positive.")

    pv = get_material(pv_material)
    reflector = get_material(reflector_material)
    efficiency = pv.efficiency or 0.0
    if efficiency <= 0.0:
        raise ValueError("PV material must define an efficiency.")

    required_pv_area = pv_power_required_w / (solar_flux_w_m2 * efficiency)
    sigma_target = (SIGMA_STAR / target_beta) * 1000.0
    denominator = sigma_target - reflector.areal_density - extra_areal_density_g_m2
    if denominator <= 0.0:
        return None

    reflector_area = required_pv_area * pv.areal_density / denominator
    return SystemBudget.from_fill_factor(
        reflector_material=reflector_material,
        pv_material=pv_material,
        fill_factor=required_pv_area / reflector_area,
        reflector_area_m2=reflector_area,
        extra_areal_density_g_m2=extra_areal_density_g_m2,
    )


def design_for_angle_power_with_structure(
    phi_deg: float,
    pv_power_required_w: float,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "ultralight_tandem_2021",
    structure_model: Optional[NodeStructure] = None,
    r_au: float = 1.0,
    solar_flux_w_m2: float = 1361.0,
    area_bounds_m2: Tuple[float, float] = (1.0, 1.0e8),
) -> Optional[PowerAngleDesign]:
    """
    Solve for the reflector area needed to satisfy both power and angle limits.

    Unlike ``find_optimal_ratio``, this function treats structural mass as a
    geometry-dependent quantity that scales with reflector size.
    """
    if pv_power_required_w <= 0.0:
        raise ValueError("pv_power_required_w must be positive.")

    if structure_model is None:
        structure_model = NodeStructure()

    orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi_deg)
    sigma_limit = orbit.max_areal_density()
    reflector = get_material(reflector_material)
    pv = get_material(pv_material)
    pv_efficiency = pv.efficiency or 0.0
    if pv_efficiency <= 0.0:
        raise ValueError("PV material must define an efficiency.")

    required_pv_area = pv_power_required_w / (solar_flux_w_m2 * pv_efficiency)

    def sigma_margin(reflector_area_m2: float) -> float:
        structure_sigma = structure_model.extra_areal_density(reflector_area_m2)
        fill_factor = required_pv_area / reflector_area_m2
        sigma_system = reflector.areal_density + fill_factor * pv.areal_density + structure_sigma
        return sigma_limit - sigma_system

    lo, hi = area_bounds_m2
    if lo <= 0.0:
        raise ValueError("area_bounds_m2 must be positive.")

    if sigma_margin(hi) < 0.0:
        return None

    while sigma_margin(lo) >= 0.0 and lo > 1.0e-12:
        lo *= 0.5
        if lo <= 1.0e-12:
            break

    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if sigma_margin(mid) >= 0.0:
            hi = mid
        else:
            lo = mid

    reflector_area = hi
    fill_factor = required_pv_area / reflector_area
    structure_mass = structure_model.total_structure_mass(reflector_area)
    budget = SystemBudget(
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=reflector_area,
        pv_area_m2=required_pv_area,
        structure_mass_kg=structure_mass,
    )

    return PowerAngleDesign(
        phi_deg=phi_deg,
        power_required_w=pv_power_required_w,
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=reflector_area,
        pv_area_m2=required_pv_area,
        pv_fill_factor=fill_factor,
        structure_mass_kg=structure_mass,
        structure_areal_density_g_m2=budget.structure_areal_density(),
        system_areal_density_g_m2=budget.system_areal_density(),
        sigma_limit_g_m2=sigma_limit,
        achieved_power_w=budget.power_output(solar_flux_w_m2=solar_flux_w_m2),
        feasible=budget.system_areal_density() <= sigma_limit + 1.0e-9,
    )


def minimum_power_for_fill_factor_with_structure(
    phi_deg: float,
    target_fill_factor: float,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "ultralight_tandem_2021",
    structure_model: Optional[NodeStructure] = None,
    r_au: float = 1.0,
    solar_flux_w_m2: float = 1361.0,
    area_bounds_m2: Tuple[float, float] = (1.0, 1.0e8),
) -> Optional[FillFactorPowerThreshold]:
    """
    Return the minimum-power node that can sustain ``target_fill_factor``.

    At fixed ``lambda = A_p / A_r``, the reflector and PV contributions to the
    areal density are constant, while the structural term decreases with node
    size. The smallest feasible reflector area therefore gives the minimum node
    power required to realize that fill factor at the requested angle.
    """
    if target_fill_factor <= 0.0:
        raise ValueError("target_fill_factor must be positive.")

    if structure_model is None:
        structure_model = NodeStructure()

    orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi_deg)
    sigma_limit = orbit.max_areal_density()
    reflector = get_material(reflector_material)
    pv = get_material(pv_material)
    pv_efficiency = pv.efficiency or 0.0
    if pv_efficiency <= 0.0:
        raise ValueError("PV material must define an efficiency.")

    constant_sigma = reflector.areal_density + target_fill_factor * pv.areal_density
    if constant_sigma >= sigma_limit:
        return None

    def sigma_margin(reflector_area_m2: float) -> float:
        structure_sigma = structure_model.extra_areal_density(reflector_area_m2)
        sigma_system = constant_sigma + structure_sigma
        return sigma_limit - sigma_system

    lo, hi = area_bounds_m2
    if lo <= 0.0:
        raise ValueError("area_bounds_m2 must be positive.")

    if sigma_margin(hi) < 0.0:
        return None

    while sigma_margin(lo) >= 0.0 and lo > 1.0e-12:
        lo *= 0.5
        if lo <= 1.0e-12:
            break

    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if sigma_margin(mid) >= 0.0:
            hi = mid
        else:
            lo = mid

    reflector_area = hi
    pv_area = target_fill_factor * reflector_area
    structure_mass = structure_model.total_structure_mass(reflector_area)
    budget = SystemBudget(
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=reflector_area,
        pv_area_m2=pv_area,
        structure_mass_kg=structure_mass,
    )

    return FillFactorPowerThreshold(
        phi_deg=phi_deg,
        target_fill_factor=target_fill_factor,
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=reflector_area,
        pv_area_m2=pv_area,
        power_w=budget.power_output(solar_flux_w_m2=solar_flux_w_m2),
        structure_mass_kg=structure_mass,
        structure_areal_density_g_m2=budget.structure_areal_density(),
        system_areal_density_g_m2=budget.system_areal_density(),
        sigma_limit_g_m2=sigma_limit,
        margin_g_m2=sigma_limit - budget.system_areal_density(),
        feasible=budget.system_areal_density() <= sigma_limit + 1.0e-9,
    )


def max_fixed_mass_for_angle_power_fill_factor(
    phi_deg: float,
    pv_power_required_w: float,
    target_fill_factor: float,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "ultralight_tandem_2021",
    structure_model: Optional[NodeStructure] = None,
    r_au: float = 1.0,
    solar_flux_w_m2: float = 1361.0,
) -> FixedMassAllowance:
    """
    Return the maximum fixed non-scaling mass allowed by the angle-power budget.

    Unlike ``minimum_power_for_fill_factor_with_structure``, this function holds
    both power and fill factor fixed, which uniquely determines the reflector
    area. The remaining mass margin can then be interpreted as the allowable
    fixed bus / deployment / control mass.
    """
    if pv_power_required_w <= 0.0:
        raise ValueError("pv_power_required_w must be positive.")
    if target_fill_factor <= 0.0:
        raise ValueError("target_fill_factor must be positive.")

    if structure_model is None:
        structure_model = NodeStructure()

    orbit = DisplacedOrbit(r_au=r_au, phi_deg=phi_deg)
    sigma_limit = orbit.max_areal_density()
    reflector = get_material(reflector_material)
    pv = get_material(pv_material)
    pv_efficiency = pv.efficiency or 0.0
    if pv_efficiency <= 0.0:
        raise ValueError("PV material must define an efficiency.")

    pv_area = pv_power_required_w / (solar_flux_w_m2 * pv_efficiency)
    reflector_area = pv_area / target_fill_factor

    reflector_mass = (reflector.areal_density / 1000.0) * reflector_area
    pv_mass = (pv.areal_density / 1000.0) * pv_area
    variable_structure_mass = (
        structure_model.total_structure_mass(reflector_area) - structure_model.fixed_mass_kg
    )
    total_mass_budget = sigma_limit * reflector_area / 1000.0
    fixed_mass_max = total_mass_budget - reflector_mass - pv_mass - variable_structure_mass

    return FixedMassAllowance(
        phi_deg=phi_deg,
        power_required_w=pv_power_required_w,
        target_fill_factor=target_fill_factor,
        reflector_material=reflector_material,
        pv_material=pv_material,
        reflector_area_m2=reflector_area,
        pv_area_m2=pv_area,
        reflector_mass_kg=reflector_mass,
        pv_mass_kg=pv_mass,
        variable_structure_mass_kg=variable_structure_mass,
        total_mass_budget_kg=total_mass_budget,
        fixed_mass_max_kg=fixed_mass_max,
        sigma_limit_g_m2=sigma_limit,
        feasible=fixed_mass_max >= 0.0,
    )


def design_space_sweep(
    phi_range_deg: Tuple[float, float] = (0.1, 5.0),
    n_points: int = 50,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "cigs_space_projection_2002",
    extra_areal_density_g_m2: float = 0.0,
    r_au: float = 1.0,
) -> Dict[str, np.ndarray]:
    """Sweep angle and return the maximum fill factor / utilization envelope."""
    phi_values = np.linspace(phi_range_deg[0], phi_range_deg[1], n_points)

    results = {
        "phi_deg": phi_values,
        "beta_required": np.zeros(n_points),
        "sigma_limit_g_m2": np.zeros(n_points),
        "pv_fill_factor_max": np.zeros(n_points),
        "absolute_utilization_max": np.zeros(n_points),
        "relative_dyson_utilization_max": np.zeros(n_points),
    }

    for i, phi_deg in enumerate(phi_values):
        summary = max_fill_factor_for_angle(
            phi_deg=float(phi_deg),
            reflector_material=reflector_material,
            pv_material=pv_material,
            extra_areal_density_g_m2=extra_areal_density_g_m2,
            r_au=r_au,
        )
        results["beta_required"][i] = summary.beta_required
        results["sigma_limit_g_m2"][i] = summary.sigma_limit_g_m2
        results["pv_fill_factor_max"][i] = summary.pv_fill_factor_max
        results["absolute_utilization_max"][i] = summary.absolute_utilization_max
        results["relative_dyson_utilization_max"][i] = (
            summary.relative_dyson_utilization_max
        )

    return results


if __name__ == "__main__":
    print("=" * 76)
    print("MDDS Mass Budget and Dyson-Swarm Utilization Trade Study")
    print("=" * 76)

    budget = SystemBudget.from_fill_factor(
        reflector_material="cp1_subsystem_nasa_2009",
        pv_material="ultralight_tandem_2021",
        fill_factor=0.5,
        reflector_area_m2=1000.0,
    )
    print("\nRepresentative node\n")
    print(budget)

    print("\nMaximum fill factor at 1 deg\n")
    for pv_key in (
        "ultralight_tandem_2021",
        "cigs_space_projection_2002",
        "miasole_flex_03w_2018",
    ):
        summary = max_fill_factor_for_angle(
            phi_deg=1.0,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material=pv_key,
        )
        print(
            f"{pv_key:<28} lambda_max={summary.pv_fill_factor_max:.3f} "
            f"eta_abs={summary.absolute_utilization_max:.3f}"
        )
