"""
Structural-closure experiment for explicit MDDS node geometry.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.comparison import mdds_relative_to_ideal_swarm
from models.mass_budget import design_for_angle_power_with_structure, get_material
from models.structural import NodeStructure


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

POWER_LEVELS_W = [100.0, 1000.0, 10000.0]
PHI_LEVELS_DEG = [0.5, 1.0, 1.5]

SCENARIOS = [
    {
        "label": "cross_light",
        "structure": NodeStructure(topology="cross", fixed_mass_kg=0.5, line_mass_margin_factor=1.1),
    },
    {
        "label": "cross_nominal",
        "structure": NodeStructure(topology="cross", fixed_mass_kg=1.0, line_mass_margin_factor=1.2),
    },
    {
        "label": "perimeter_nominal",
        "structure": NodeStructure(topology="perimeter", fixed_mass_kg=1.0, line_mass_margin_factor=1.2),
    },
    {
        "label": "perimeter_heavy",
        "structure": NodeStructure(topology="perimeter", fixed_mass_kg=5.0, line_mass_margin_factor=1.3),
    },
]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    rows = []
    pv = get_material("ultralight_tandem_2021")
    for phi_deg in PHI_LEVELS_DEG:
        for power_w in POWER_LEVELS_W:
            for scenario in SCENARIOS:
                design = design_for_angle_power_with_structure(
                    phi_deg=phi_deg,
                    pv_power_required_w=power_w,
                    reflector_material="cp1_subsystem_nasa_2009",
                    pv_material="ultralight_tandem_2021",
                    structure_model=scenario["structure"],
                )
                if design is None:
                    rows.append(
                        {
                            "scenario": scenario["label"],
                            "phi_deg": phi_deg,
                            "power_required_w": power_w,
                            "feasible": False,
                        }
                    )
                    continue

                rows.append(
                    {
                        "scenario": scenario["label"],
                        "phi_deg": phi_deg,
                        "power_required_w": power_w,
                        "feasible": design.feasible,
                        "reflector_area_m2": design.reflector_area_m2,
                        "reflector_side_m": design.reflector_area_m2 ** 0.5,
                        "pv_area_m2": design.pv_area_m2,
                        "pv_fill_factor": design.pv_fill_factor,
                        "structure_mass_kg": design.structure_mass_kg,
                        "structure_areal_density_g_m2": design.structure_areal_density_g_m2,
                        "system_areal_density_g_m2": design.system_areal_density_g_m2,
                        "sigma_limit_g_m2": design.sigma_limit_g_m2,
                        "margin_g_m2": design.sigma_limit_g_m2 - design.system_areal_density_g_m2,
                        "relative_to_ideal_swarm_same_eta": mdds_relative_to_ideal_swarm(
                            pv_fill_factor=design.pv_fill_factor,
                            mdds_efficiency=pv.efficiency or 0.0,
                            swarm_efficiency=pv.efficiency or 0.0,
                        ),
                    }
                )

    write_csv(RESULTS_DIR / "structural_designs.csv", rows)

    def power_for_fill(phi_deg: float, target_fill: float, structure: NodeStructure) -> float:
        lo, hi = 1.0, 1.0e8
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            design = design_for_angle_power_with_structure(
                phi_deg=phi_deg,
                pv_power_required_w=mid,
                reflector_material="cp1_subsystem_nasa_2009",
                pv_material="ultralight_tandem_2021",
                structure_model=structure,
            )
            if design.pv_fill_factor >= target_fill:
                hi = mid
            else:
                lo = mid
        return hi

    cross_light = NodeStructure(topology="cross", fixed_mass_kg=0.5, line_mass_margin_factor=1.1)
    cross_nominal = NodeStructure(topology="cross", fixed_mass_kg=1.0, line_mass_margin_factor=1.2)
    one_deg_cross_light_100w = design_for_angle_power_with_structure(
        phi_deg=1.0,
        pv_power_required_w=100.0,
        structure_model=cross_light,
    )
    one_deg_cross_light_10kw = design_for_angle_power_with_structure(
        phi_deg=1.0,
        pv_power_required_w=10000.0,
        structure_model=cross_light,
    )

    summary = {
        "assumptions": {
            "reflector": "cp1_subsystem_nasa_2009",
            "pv": "ultralight_tandem_2021",
            "structure_line_densities": {
                "cf_boom_g_per_m": get_material("cf_boom").areal_density,
                "tether_dyneema_g_per_m": get_material("tether_dyneema").areal_density,
            },
            "note": "Structure model is geometry-explicit but still exploratory because line-density values are placeholders.",
        },
        "headline_1deg": {
            "cross_light_100w": {
                "reflector_area_m2": one_deg_cross_light_100w.reflector_area_m2,
                "reflector_side_m": one_deg_cross_light_100w.reflector_area_m2 ** 0.5,
                "pv_fill_factor": one_deg_cross_light_100w.pv_fill_factor,
                "structure_areal_density_g_m2": one_deg_cross_light_100w.structure_areal_density_g_m2,
            },
            "cross_light_10kw": {
                "reflector_area_m2": one_deg_cross_light_10kw.reflector_area_m2,
                "reflector_side_m": one_deg_cross_light_10kw.reflector_area_m2 ** 0.5,
                "pv_fill_factor": one_deg_cross_light_10kw.pv_fill_factor,
                "structure_areal_density_g_m2": one_deg_cross_light_10kw.structure_areal_density_g_m2,
            },
        },
        "power_thresholds_for_fill_factor_at_1deg": {
            "cross_light": {
                "lambda_0p01": power_for_fill(1.0, 0.01, cross_light),
                "lambda_0p05": power_for_fill(1.0, 0.05, cross_light),
                "lambda_0p10": power_for_fill(1.0, 0.10, cross_light),
                "lambda_0p25": power_for_fill(1.0, 0.25, cross_light),
            },
            "cross_nominal": {
                "lambda_0p01": power_for_fill(1.0, 0.01, cross_nominal),
                "lambda_0p05": power_for_fill(1.0, 0.05, cross_nominal),
                "lambda_0p10": power_for_fill(1.0, 0.10, cross_nominal),
                "lambda_0p25": power_for_fill(1.0, 0.25, cross_nominal),
            },
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
