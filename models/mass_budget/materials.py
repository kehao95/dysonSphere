"""
Materials database for Micro-Displaced Dyson Swarm feasibility analysis.

The entries below intentionally distinguish between:
- source-backed, currently demonstrated materials that are suitable for the
  present feasibility paper; and
- lightweight placeholder estimates retained only for exploratory sweeps.

For the publication-facing analysis we use the explicitly source-backed entries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class Material:
    """Material properties used in the mass-budget calculations."""

    name: str
    category: str  # "reflector", "pv_cell", "structure"
    areal_density: float  # g/m^2
    reflectivity: Optional[float] = None
    efficiency: Optional[float] = None
    absorptivity: Optional[float] = None
    emissivity: Optional[float] = None
    specific_power_w_kg: Optional[float] = None
    reference_irradiance_w_m2: Optional[float] = None
    source: str = ""
    source_url: str = ""
    notes: str = ""


def _areal_density_from_specific_power(
    efficiency: float, specific_power_w_kg: float, irradiance_w_m2: float
) -> float:
    """Convert efficiency and specific power into areal density (g/m^2)."""
    return 1000.0 * efficiency * irradiance_w_m2 / specific_power_w_kg


# -----------------------------------------------------------------------------
# Reflector / sail subsystem materials
# -----------------------------------------------------------------------------

REFLECTOR_MATERIALS: Dict[str, Material] = {
    "cp1_subsystem_nasa_2009": Material(
        name="CP1 sail subsystem (NASA 2009)",
        category="reflector",
        areal_density=5.0,
        reflectivity=0.90,
        absorptivity=0.10,
        emissivity=0.03,
        source="NASA Tech Brief: Solar Sails for Space Exploration",
        source_url="https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110012917.pdf",
        notes="Source-backed near-term subsystem target used as the optimistic reflector case.",
    ),
    "kapton_76um_nasa_2001": Material(
        name="7.6 um aluminized Kapton (NASA 2001)",
        category="reflector",
        areal_density=11.0,
        reflectivity=0.88,
        absorptivity=0.12,
        emissivity=0.03,
        source="NASA report on solar sail material limits",
        source_url="https://ntrs.nasa.gov/api/citations/20010067713/downloads/20010067713.pdf",
        notes="Conservative reflector case close to the thinnest robust Kapton film discussed by NASA.",
    ),
    "ikaros_sail_2010": Material(
        name="IKAROS sail membrane",
        category="reflector",
        areal_density=7.5,
        reflectivity=0.85,
        absorptivity=0.15,
        emissivity=0.05,
        source="JAXA IKAROS mission data / repository legacy estimate",
        source_url="https://www.isas.jaxa.jp/missions/spacecraft/past/ikaros.html",
        notes="Mission-scale reference point; includes integrated sail hardware overhead.",
    ),
    # Legacy exploratory estimates retained for quick sweeps.
    "kapton_al_2um": Material(
        name="Aluminized Kapton (2 um, estimate)",
        category="reflector",
        areal_density=2.8,
        reflectivity=0.88,
        absorptivity=0.12,
        emissivity=0.03,
        notes="Legacy estimate retained for exploratory use only.",
    ),
    "kapton_al_1um": Material(
        name="Aluminized Kapton (1 um, estimate)",
        category="reflector",
        areal_density=1.4,
        reflectivity=0.88,
        absorptivity=0.12,
        emissivity=0.03,
        notes="Legacy estimate retained for exploratory use only.",
    ),
}


# -----------------------------------------------------------------------------
# Photovoltaic materials
# -----------------------------------------------------------------------------

cigs_space_projection_density = _areal_density_from_specific_power(
    efficiency=0.15, specific_power_w_kg=1153.13, irradiance_w_m2=1353.0
)
ultralight_tandem_density = _areal_density_from_specific_power(
    efficiency=0.274, specific_power_w_kg=5000.0, irradiance_w_m2=1000.0
)

PV_MATERIALS: Dict[str, Material] = {
    "cigs_space_projection_2002": Material(
        name="Flexible CIGS on 20 um SS foil (NASA/FSEC 2002 projection)",
        category="pv_cell",
        areal_density=cigs_space_projection_density,
        efficiency=0.15,
        absorptivity=0.85,
        emissivity=0.85,
        specific_power_w_kg=1153.13,
        reference_irradiance_w_m2=1353.0,
        source="NASA/FSEC CIGS thin-film space solar cell projection",
        source_url="https://ntrs.nasa.gov/api/citations/20030000597/downloads/20030000597.pdf",
        notes="Projected high-specific-power CIGS on 20 um stainless-steel foil; best source-backed CIGS case found.",
    ),
    "ultralight_tandem_2021": Material(
        name="Ultralight flexible InGaP/GaAs tandem (2021)",
        category="pv_cell",
        areal_density=ultralight_tandem_density,
        efficiency=0.274,
        absorptivity=0.90,
        emissivity=0.85,
        specific_power_w_kg=5000.0,
        reference_irradiance_w_m2=1000.0,
        source="Peer-reviewed ultralight tandem cell with >5000 W/kg",
        source_url="https://www.sciencedirect.com/science/article/abs/pii/S0927024821004185",
        notes="State-of-the-art ultralight cell. Areal density is an upper bound because the source reports >5000 W/kg.",
    ),
    "miasole_flex_03w_2018": Material(
        name="MiaSole FLEX-03W commercial CIGS module",
        category="pv_cell",
        areal_density=1700.0,
        efficiency=0.167,
        absorptivity=0.85,
        emissivity=0.85,
        specific_power_w_kg=98.0,
        reference_irradiance_w_m2=1000.0,
        source="MiaSole FLEX-03W datasheet",
        source_url="https://miasole.com/wp-content/uploads/2017/11/flex-03w_datasheet.pdf",
        notes="Commercial flexible module; useful as a conservative 'off-the-shelf' comparison.",
    ),
    # Legacy exploratory estimates retained for continuity.
    "cigs_flex": Material(
        name="Flexible CIGS Thin-Film (legacy estimate)",
        category="pv_cell",
        areal_density=80.0,
        efficiency=0.15,
        absorptivity=0.85,
        emissivity=0.85,
        notes="Legacy estimate retained for exploratory use only.",
    ),
    "gaas_flex": Material(
        name="Flexible GaAs (legacy estimate)",
        category="pv_cell",
        areal_density=200.0,
        efficiency=0.29,
        absorptivity=0.90,
        emissivity=0.85,
        notes="Legacy estimate retained for exploratory use only.",
    ),
}


# -----------------------------------------------------------------------------
# Structure materials
# -----------------------------------------------------------------------------

STRUCTURE_MATERIALS: Dict[str, Material] = {
    "cf_boom": Material(
        name="Carbon-fiber deployable boom",
        category="structure",
        areal_density=50.0,
        source="Repository placeholder value",
        notes="Per-metre mass proxy retained for exploratory structural scaling.",
    ),
    "acs3_composite_boom_2023": Material(
        name="ACS3 composite boom (NASA 2023)",
        category="structure",
        areal_density=23.428571428571427,
        source="NASA ACS3 mission update",
        source_url="https://ntrs.nasa.gov/api/citations/20230008378/downloads/Wilkie_ACS3_mission_update_ISSS_2023_20230530_rev_a.pdf",
        notes="Per-metre boom mass derived from 0.164 kg per 7.0 m boom in the ACS3 flight-system appendix.",
    ),
    "tether_dyneema": Material(
        name="Dyneema tether",
        category="structure",
        areal_density=0.97,
        source="Repository placeholder value",
        notes="Per-metre mass proxy retained for exploratory structural scaling.",
    ),
    "dyneema_1p25mm_usspars": Material(
        name="Dyneema braid 1.25 mm (U.S. Spars)",
        category="structure",
        areal_density=1.0,
        source="U.S. Spars Pure Dyneema product page",
        source_url="https://www.usspars.com/ropes/pure-dyneema/",
        notes="Per-metre mass derived from 0.10 kg/100 m for 1.25 mm SK78 braid.",
    ),
    "dyneema_2mm_usspars": Material(
        name="Dyneema braid 2.0 mm (U.S. Spars)",
        category="structure",
        areal_density=2.0,
        source="U.S. Spars Pure Dyneema product page",
        source_url="https://www.usspars.com/ropes/pure-dyneema/",
        notes="Per-metre mass derived from 0.20 kg/100 m for 2.0 mm SK78 braid.",
    ),
}


def get_all_materials() -> Dict[str, Material]:
    """Return all material entries."""
    all_materials: Dict[str, Material] = {}
    all_materials.update(REFLECTOR_MATERIALS)
    all_materials.update(PV_MATERIALS)
    all_materials.update(STRUCTURE_MATERIALS)
    return all_materials


def get_material(name: str) -> Material:
    """Return a material by key name."""
    all_materials = get_all_materials()
    if name not in all_materials:
        raise KeyError(f"Material '{name}' not found. Available: {list(all_materials)}")
    return all_materials[name]


def list_materials_by_category(category: str) -> Dict[str, Material]:
    """Return materials filtered by category."""
    return {k: v for k, v in get_all_materials().items() if v.category == category}


def print_materials_table() -> None:
    """Print a compact table of the source-backed publication candidates."""
    print("\n" + "=" * 88)
    print("SOURCE-BACKED MATERIAL CANDIDATES")
    print("=" * 88)

    print("\nReflectors\n")
    print(f"{'Key':<28} {'sigma [g/m^2]':>14} {'R':>6} {'Source':<32}")
    print("-" * 88)
    for key in ("cp1_subsystem_nasa_2009", "kapton_76um_nasa_2001", "ikaros_sail_2010"):
        mat = REFLECTOR_MATERIALS[key]
        print(
            f"{key:<28} {mat.areal_density:>14.1f} {mat.reflectivity or 0:>6.2f} {mat.source[:32]:<32}"
        )

    print("\nPV materials\n")
    print(f"{'Key':<28} {'sigma [g/m^2]':>14} {'eta':>8} {'SP [W/kg]':>12}")
    print("-" * 88)
    for key in (
        "cigs_space_projection_2002",
        "ultralight_tandem_2021",
        "miasole_flex_03w_2018",
    ):
        mat = PV_MATERIALS[key]
        print(
            f"{key:<28} {mat.areal_density:>14.1f} {mat.efficiency or 0:>8.3f} {mat.specific_power_w_kg or 0:>12.1f}"
        )


if __name__ == "__main__":
    print_materials_table()
