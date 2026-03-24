"""
Integrated structural design-map experiment for MDDS nodes.

This run couples:

- exact displaced-orbit angle limits,
- explicit node structure scaling,
- required node power, and
- relative energy performance against ideal Dyson Swarm / Dyson Ring baselines.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.comparison import equivalent_ring_half_angle_deg, mdds_relative_to_ideal_swarm
from models.mass_budget import (
    design_for_angle_power_with_structure,
    get_material,
    minimum_power_for_fill_factor_with_structure,
)
from models.structural import NodeStructure


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

PHI_LEVELS_DEG = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
POWER_LEVELS_W = [100.0, 300.0, 1000.0, 3000.0, 10000.0, 30000.0, 100000.0]
TARGET_FILL_FACTORS = [0.01, 0.05, 0.10, 0.25, 0.50]

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
]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def max_angle_for_power_target(
    power_w: float,
    target_fill_factor: float,
    structure: NodeStructure,
    reflector_material: str = "cp1_subsystem_nasa_2009",
    pv_material: str = "ultralight_tandem_2021",
    phi_bounds_deg: tuple[float, float] = (0.05, 6.5),
) -> float:
    """Return the largest angle where the target fill factor remains achievable."""

    def feasible(phi_deg: float) -> bool:
        threshold = minimum_power_for_fill_factor_with_structure(
            phi_deg=phi_deg,
            target_fill_factor=target_fill_factor,
            reflector_material=reflector_material,
            pv_material=pv_material,
            structure_model=structure,
        )
        return threshold is not None and threshold.power_w <= power_w

    lo, hi = phi_bounds_deg
    if not feasible(lo):
        return 0.0
    if feasible(hi):
        return hi

    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    return lo


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    pv = get_material("ultralight_tandem_2021")

    design_rows = []
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
                    design_rows.append(
                        {
                            "scenario": scenario["label"],
                            "phi_deg": phi_deg,
                            "power_required_w": power_w,
                            "feasible": False,
                        }
                    )
                    continue

                relative_same_eta = mdds_relative_to_ideal_swarm(
                    pv_fill_factor=design.pv_fill_factor,
                    mdds_efficiency=pv.efficiency or 0.0,
                    swarm_efficiency=pv.efficiency or 0.0,
                )
                design_rows.append(
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
                        "relative_to_ideal_swarm_same_eta": relative_same_eta,
                        "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                            min(1.0, relative_same_eta)
                        ),
                    }
                )

    write_csv(RESULTS_DIR / "design_grid.csv", design_rows)

    threshold_rows = []
    for phi_deg in PHI_LEVELS_DEG:
        for target_fill_factor in TARGET_FILL_FACTORS:
            for scenario in SCENARIOS:
                threshold = minimum_power_for_fill_factor_with_structure(
                    phi_deg=phi_deg,
                    target_fill_factor=target_fill_factor,
                    reflector_material="cp1_subsystem_nasa_2009",
                    pv_material="ultralight_tandem_2021",
                    structure_model=scenario["structure"],
                )
                if threshold is None:
                    threshold_rows.append(
                        {
                            "scenario": scenario["label"],
                            "phi_deg": phi_deg,
                            "target_fill_factor": target_fill_factor,
                            "relative_to_ideal_swarm_same_eta": target_fill_factor,
                            "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                                min(1.0, target_fill_factor)
                            ),
                            "feasible": False,
                        }
                    )
                    continue

                threshold_rows.append(
                    {
                        "scenario": scenario["label"],
                        "phi_deg": phi_deg,
                        "target_fill_factor": target_fill_factor,
                        "relative_to_ideal_swarm_same_eta": target_fill_factor,
                        "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                            min(1.0, target_fill_factor)
                        ),
                        "feasible": threshold.feasible,
                        "minimum_power_w": threshold.power_w,
                        "reflector_area_m2": threshold.reflector_area_m2,
                        "reflector_side_m": threshold.reflector_area_m2 ** 0.5,
                        "pv_area_m2": threshold.pv_area_m2,
                        "structure_mass_kg": threshold.structure_mass_kg,
                        "structure_areal_density_g_m2": threshold.structure_areal_density_g_m2,
                        "system_areal_density_g_m2": threshold.system_areal_density_g_m2,
                        "sigma_limit_g_m2": threshold.sigma_limit_g_m2,
                        "margin_g_m2": threshold.margin_g_m2,
                    }
                )

    write_csv(RESULTS_DIR / "power_thresholds_by_angle.csv", threshold_rows)

    angle_rows = []
    for power_w in POWER_LEVELS_W:
        for target_fill_factor in TARGET_FILL_FACTORS:
            for scenario in SCENARIOS:
                max_angle_deg = max_angle_for_power_target(
                    power_w=power_w,
                    target_fill_factor=target_fill_factor,
                    structure=scenario["structure"],
                )
                angle_rows.append(
                    {
                        "scenario": scenario["label"],
                        "power_w": power_w,
                        "target_fill_factor": target_fill_factor,
                        "relative_to_ideal_swarm_same_eta": target_fill_factor,
                        "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                            min(1.0, target_fill_factor)
                        ),
                        "max_angle_deg": max_angle_deg,
                    }
                )

    write_csv(RESULTS_DIR / "angle_thresholds_by_power.csv", angle_rows)

    def threshold_entry(
        phi_deg: float,
        target_fill_factor: float,
        structure: NodeStructure,
    ) -> dict | None:
        threshold = minimum_power_for_fill_factor_with_structure(
            phi_deg=phi_deg,
            target_fill_factor=target_fill_factor,
            structure_model=structure,
        )
        if threshold is None:
            return None
        return {
            "minimum_power_w": threshold.power_w,
            "reflector_area_m2": threshold.reflector_area_m2,
            "structure_areal_density_g_m2": threshold.structure_areal_density_g_m2,
        }

    cross_light = SCENARIOS[0]["structure"]
    cross_nominal = SCENARIOS[1]["structure"]
    perimeter_nominal = SCENARIOS[2]["structure"]

    design_1deg_10kw_cross_light = design_for_angle_power_with_structure(
        phi_deg=1.0,
        pv_power_required_w=10000.0,
        structure_model=cross_light,
    )
    design_1deg_10kw_cross_nominal = design_for_angle_power_with_structure(
        phi_deg=1.0,
        pv_power_required_w=10000.0,
        structure_model=cross_nominal,
    )
    design_2deg_10kw_cross_light = design_for_angle_power_with_structure(
        phi_deg=2.0,
        pv_power_required_w=10000.0,
        structure_model=cross_light,
    )

    summary = {
        "assumptions": {
            "reflector": "cp1_subsystem_nasa_2009",
            "pv": "ultralight_tandem_2021",
            "phi_levels_deg": PHI_LEVELS_DEG,
            "power_levels_w": POWER_LEVELS_W,
            "target_fill_factors": TARGET_FILL_FACTORS,
            "note": "Relative-to-Swarm results assume the same PV efficiency on both architectures and no degradation/control losses for any concept.",
        },
        "headline_thresholds": {
            "one_deg": {
                "cross_light": {
                    "relative_0p10": threshold_entry(1.0, 0.10, cross_light),
                    "relative_0p25": threshold_entry(1.0, 0.25, cross_light),
                    "relative_0p50": threshold_entry(1.0, 0.50, cross_light),
                },
                "cross_nominal": {
                    "relative_0p10": threshold_entry(1.0, 0.10, cross_nominal),
                    "relative_0p25": threshold_entry(1.0, 0.25, cross_nominal),
                },
            },
            "two_deg": {
                "cross_light": {
                    "relative_0p05": threshold_entry(2.0, 0.05, cross_light),
                    "relative_0p10": threshold_entry(2.0, 0.10, cross_light),
                },
                "perimeter_nominal": {
                    "relative_0p05": threshold_entry(2.0, 0.05, perimeter_nominal),
                },
            },
        },
        "ten_kw_examples": {
            "cross_light_at_1deg": {
                "relative_to_ideal_swarm_same_eta": design_1deg_10kw_cross_light.pv_fill_factor,
                "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                    design_1deg_10kw_cross_light.pv_fill_factor
                ),
            },
            "cross_nominal_at_1deg": {
                "relative_to_ideal_swarm_same_eta": design_1deg_10kw_cross_nominal.pv_fill_factor,
                "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                    design_1deg_10kw_cross_nominal.pv_fill_factor
                ),
            },
            "cross_light_at_2deg": {
                "relative_to_ideal_swarm_same_eta": design_2deg_10kw_cross_light.pv_fill_factor,
                "equivalent_ideal_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                    design_2deg_10kw_cross_light.pv_fill_factor
                ),
            },
        },
        "max_angle_by_power": {
            "cross_light": {
                "power_10kw_relative_0p10_deg": max_angle_for_power_target(10000.0, 0.10, cross_light),
                "power_10kw_relative_0p25_deg": max_angle_for_power_target(10000.0, 0.25, cross_light),
                "power_30kw_relative_0p25_deg": max_angle_for_power_target(30000.0, 0.25, cross_light),
            },
            "cross_nominal": {
                "power_10kw_relative_0p10_deg": max_angle_for_power_target(10000.0, 0.10, cross_nominal),
                "power_10kw_relative_0p25_deg": max_angle_for_power_target(10000.0, 0.25, cross_nominal),
            },
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
