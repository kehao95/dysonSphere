"""
Materials Database for Solar Sail and Payload Components

Contains areal densities and properties of materials relevant to
Micro-Displaced Dyson Swarm node construction.

Data sources:
- NASA solar sail technology reports
- JAXA IKAROS mission data
- Published thin-film solar cell specifications
"""

from dataclasses import dataclass
from typing import Dict, Optional
import json


@dataclass
class Material:
    """Material properties for mass budget calculations."""

    name: str
    category: str  # 'reflector', 'pv_cell', 'structure'
    areal_density: float  # g/m²
    reflectivity: Optional[float] = None  # 0-1, for reflectors
    efficiency: Optional[float] = None  # 0-1, for PV cells
    absorptivity: Optional[float] = None  # 0-1, solar absorptivity
    emissivity: Optional[float] = None  # 0-1, IR emissivity
    notes: str = ""
    source: str = ""


# =============================================================================
# REFLECTOR MATERIALS (Solar Sail Films)
# =============================================================================

REFLECTOR_MATERIALS: Dict[str, Material] = {
    # Flight-proven
    "kapton_al_2um": Material(
        name="Aluminized Kapton (2 μm)",
        category="reflector",
        areal_density=2.8,  # g/m²
        reflectivity=0.88,
        absorptivity=0.12,
        emissivity=0.03,  # Back-side aluminum
        notes="Standard space-qualified material",
        source="NASA Sail Materials Assessment",
    ),
    "kapton_al_1um": Material(
        name="Aluminized Kapton (1 μm)",
        category="reflector",
        areal_density=1.4,  # g/m²
        reflectivity=0.88,
        absorptivity=0.12,
        emissivity=0.03,
        notes="Thinner variant, more fragile",
        source="Estimated from 2μm data",
    ),
    "ikaros_sail": Material(
        name="IKAROS Sail Material",
        category="reflector",
        areal_density=7.5,  # g/m² (including LCD steering devices)
        reflectivity=0.85,
        absorptivity=0.15,
        emissivity=0.05,
        notes="JAXA IKAROS mission (2010), polyimide + aluminum",
        source="JAXA IKAROS data",
    ),
    # Advanced (near-term)
    "cp1_al": Material(
        name="CP1 Aluminized Polymer",
        category="reflector",
        areal_density=1.0,  # g/m²
        reflectivity=0.90,
        absorptivity=0.10,
        emissivity=0.03,
        notes="NASA advanced sail material",
        source="NASA In-Space Propulsion",
    ),
    # Theoretical/future
    "ultrathin_al": Material(
        name="Ultrathin Aluminum Film",
        category="reflector",
        areal_density=0.3,  # g/m² (100nm Al)
        reflectivity=0.92,
        absorptivity=0.08,
        emissivity=0.02,
        notes="Theoretical, requires substrate",
        source="Materials science projection",
    ),
}


# =============================================================================
# PHOTOVOLTAIC MATERIALS
# =============================================================================

PV_MATERIALS: Dict[str, Material] = {
    # Current technology
    "cigs_flex": Material(
        name="Flexible CIGS Thin-Film",
        category="pv_cell",
        areal_density=80,  # g/m²
        efficiency=0.15,  # 15%
        absorptivity=0.85,
        emissivity=0.85,
        notes="Copper Indium Gallium Selenide, flexible substrate",
        source="MiaSolé, Alta Devices",
    ),
    "gaas_flex": Material(
        name="Flexible GaAs",
        category="pv_cell",
        areal_density=200,  # g/m²
        efficiency=0.29,  # 29%
        absorptivity=0.90,
        emissivity=0.85,
        notes="Gallium Arsenide, epitaxial lift-off",
        source="Alta Devices",
    ),
    "perovskite": Material(
        name="Perovskite Thin-Film",
        category="pv_cell",
        areal_density=50,  # g/m²
        efficiency=0.20,  # 20% (lab)
        absorptivity=0.85,
        emissivity=0.85,
        notes="Emerging technology, stability TBD",
        source="Research literature (2024)",
    ),
    # Advanced/future
    "ultrathin_gaas": Material(
        name="Ultrathin GaAs",
        category="pv_cell",
        areal_density=100,  # g/m²
        efficiency=0.30,
        absorptivity=0.90,
        emissivity=0.85,
        notes="Next-generation lightweight GaAs",
        source="Projection",
    ),
    # Space standard (reference)
    "standard_space_pv": Material(
        name="Standard Triple-Junction",
        category="pv_cell",
        areal_density=850,  # g/m² (including coverglass)
        efficiency=0.30,
        absorptivity=0.92,
        emissivity=0.85,
        notes="Traditional rigid space solar cells",
        source="Spectrolab",
    ),
}


# =============================================================================
# STRUCTURAL MATERIALS
# =============================================================================

STRUCTURE_MATERIALS: Dict[str, Material] = {
    "cf_boom": Material(
        name="Carbon Fiber Deployable Boom",
        category="structure",
        areal_density=50,  # g/m of boom, convert as needed
        notes="TRAC or similar rollable boom, ~50g per meter length",
        source="ATK/Northrop Grumman",
    ),
    "tether_dyneema": Material(
        name="Dyneema Tether",
        category="structure",
        areal_density=0.97,  # g/m for 1mm diameter
        notes="Ultra-high molecular weight polyethylene",
        source="DSM Dyneema",
    ),
    "al_frame": Material(
        name="Aluminum Tubular Frame",
        category="structure",
        areal_density=100,  # g/m for thin-wall tube
        notes="6061-T6 aluminum, thin wall",
        source="Standard aerospace",
    ),
}


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================


def get_all_materials() -> Dict[str, Material]:
    """Return all materials in a single dictionary."""
    all_materials = {}
    all_materials.update(REFLECTOR_MATERIALS)
    all_materials.update(PV_MATERIALS)
    all_materials.update(STRUCTURE_MATERIALS)
    return all_materials


def get_material(name: str) -> Material:
    """Get a material by its key name."""
    all_mats = get_all_materials()
    if name not in all_mats:
        raise KeyError(
            f"Material '{name}' not found. Available: {list(all_mats.keys())}"
        )
    return all_mats[name]


def list_materials_by_category(category: str) -> Dict[str, Material]:
    """List all materials in a given category."""
    return {k: v for k, v in get_all_materials().items() if v.category == category}


def print_materials_table():
    """Print a formatted table of all materials."""
    print("\n" + "=" * 80)
    print("MATERIALS DATABASE")
    print("=" * 80)

    for category in ["reflector", "pv_cell", "structure"]:
        print(f"\n--- {category.upper()} ---\n")
        mats = list_materials_by_category(category)

        if category == "reflector":
            print(f"{'Name':<30} {'σ [g/m²]':>10} {'R':>6} {'α':>6} {'ε':>6}")
            print("-" * 60)
            for key, mat in mats.items():
                print(
                    f"{mat.name:<30} {mat.areal_density:>10.1f} "
                    f"{mat.reflectivity or 0:>6.2f} "
                    f"{mat.absorptivity or 0:>6.2f} "
                    f"{mat.emissivity or 0:>6.2f}"
                )

        elif category == "pv_cell":
            print(f"{'Name':<30} {'σ [g/m²]':>10} {'η':>6} {'α':>6}")
            print("-" * 55)
            for key, mat in mats.items():
                print(
                    f"{mat.name:<30} {mat.areal_density:>10.1f} "
                    f"{mat.efficiency or 0:>6.2f} "
                    f"{mat.absorptivity or 0:>6.2f}"
                )

        else:
            print(f"{'Name':<30} {'σ':>15} {'Notes':<30}")
            print("-" * 75)
            for key, mat in mats.items():
                print(
                    f"{mat.name:<30} {mat.areal_density:>10.1f} g/m²  {mat.notes[:30]}"
                )


if __name__ == "__main__":
    print_materials_table()

    print("\n" + "=" * 80)
    print("QUICK REFERENCE: Critical areal density σ* ≈ 1.53 g/m²")
    print("=" * 80)
    print("\nFor β = 1 (full levitation), need σ < 1.53 g/m²")
    print("For β = 0.017 (1° displacement), can have σ < 90 g/m²")
    print("For β = 0.05 (2.9° displacement), can have σ < 30.6 g/m²")
