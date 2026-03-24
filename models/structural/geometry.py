"""
Geometry-based structural scaling model for a decoupled MDDS node.

The aim is not to claim a flight-ready structural design, but to replace the
abstract "extra areal density" knob with an explicit scaling law based on node
size, support topology, line densities, and a fixed payload-bus mass.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from models.mass_budget.materials import get_material


@dataclass(frozen=True)
class StructuralBreakdown:
    """Detailed structural mass breakdown for one reflector-payload unit."""

    reflector_area_m2: float
    reflector_side_m: float
    topology: str
    boom_total_length_m: float
    boom_mass_kg: float
    tether_total_length_m: float
    tether_mass_kg: float
    fixed_mass_kg: float
    total_structure_mass_kg: float
    extra_areal_density_g_m2: float


@dataclass(frozen=True)
class StructuralDesignResult:
    """Solved node design for a target angle and power requirement."""

    phi_deg: float
    power_required_w: float
    reflector_area_m2: float
    pv_area_m2: float
    pv_fill_factor: float
    structure_mass_kg: float
    structure_areal_density_g_m2: float
    system_areal_density_g_m2: float
    sigma_limit_g_m2: float
    margin_g_m2: float
    feasible: bool


class NodeStructure:
    """
    Explicit structural model for a square decoupled MDDS node.

    Two support topologies are provided:

    - ``cross``: four radial booms from the center hub to the corners
    - ``perimeter``: four edge booms tracing the perimeter of the square sail

    The payload bus is suspended below the reflector by corner tethers.
    """

    def __init__(
        self,
        topology: str = "cross",
        boom_material: str = "cf_boom",
        tether_material: str = "tether_dyneema",
        payload_standoff_fraction: float = 0.25,
        fixed_mass_kg: float = 1.0,
        line_mass_margin_factor: float = 1.2,
    ):
        if topology not in {"cross", "perimeter"}:
            raise ValueError("topology must be 'cross' or 'perimeter'.")
        if payload_standoff_fraction < 0.0:
            raise ValueError("payload_standoff_fraction must be non-negative.")
        if fixed_mass_kg < 0.0:
            raise ValueError("fixed_mass_kg must be non-negative.")
        if line_mass_margin_factor <= 0.0:
            raise ValueError("line_mass_margin_factor must be positive.")

        self.topology = topology
        self.boom = get_material(boom_material)
        self.tether = get_material(tether_material)
        self.payload_standoff_fraction = payload_standoff_fraction
        self.fixed_mass_kg = fixed_mass_kg
        self.line_mass_margin_factor = line_mass_margin_factor

    def reflector_side_length(self, reflector_area_m2: float) -> float:
        """Return square reflector side length."""
        if reflector_area_m2 <= 0.0:
            raise ValueError("reflector_area_m2 must be positive.")
        return math.sqrt(reflector_area_m2)

    def boom_total_length(self, reflector_area_m2: float) -> float:
        """Return total boom length in metres for the chosen topology."""
        side = self.reflector_side_length(reflector_area_m2)
        if self.topology == "cross":
            return 2.0 * math.sqrt(2.0) * side
        return 4.0 * side

    def tether_total_length(self, reflector_area_m2: float) -> float:
        """
        Return total payload-tether length in metres.

        Four tethers are assumed, each running from a sail corner to the payload
        bus suspended below the sail center.
        """
        side = self.reflector_side_length(reflector_area_m2)
        standoff = self.payload_standoff_fraction * side
        tether_single = math.sqrt(0.5 * side**2 + standoff**2)
        return 4.0 * tether_single

    def boom_mass(self, reflector_area_m2: float) -> float:
        """Return boom mass in kg."""
        linear_density_kg_m = self.boom.areal_density / 1000.0
        return (
            self.line_mass_margin_factor
            * linear_density_kg_m
            * self.boom_total_length(reflector_area_m2)
        )

    def tether_mass(self, reflector_area_m2: float) -> float:
        """Return tether mass in kg."""
        linear_density_kg_m = self.tether.areal_density / 1000.0
        return (
            self.line_mass_margin_factor
            * linear_density_kg_m
            * self.tether_total_length(reflector_area_m2)
        )

    def total_structure_mass(self, reflector_area_m2: float) -> float:
        """Return total structure mass in kg."""
        return (
            self.boom_mass(reflector_area_m2)
            + self.tether_mass(reflector_area_m2)
            + self.fixed_mass_kg
        )

    def extra_areal_density(self, reflector_area_m2: float) -> float:
        """Return extra non-PV/non-reflector areal density in g/m^2."""
        return 1000.0 * self.total_structure_mass(reflector_area_m2) / reflector_area_m2

    def get_breakdown(self, reflector_area_m2: float) -> StructuralBreakdown:
        """Return a detailed structural breakdown."""
        boom_mass = self.boom_mass(reflector_area_m2)
        tether_mass = self.tether_mass(reflector_area_m2)
        total = boom_mass + tether_mass + self.fixed_mass_kg
        return StructuralBreakdown(
            reflector_area_m2=reflector_area_m2,
            reflector_side_m=self.reflector_side_length(reflector_area_m2),
            topology=self.topology,
            boom_total_length_m=self.boom_total_length(reflector_area_m2),
            boom_mass_kg=boom_mass,
            tether_total_length_m=self.tether_total_length(reflector_area_m2),
            tether_mass_kg=tether_mass,
            fixed_mass_kg=self.fixed_mass_kg,
            total_structure_mass_kg=total,
            extra_areal_density_g_m2=1000.0 * total / reflector_area_m2,
        )
