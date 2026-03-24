"""
Source-backed fixed-bus budget analysis for MDDS nodes.

This run asks how much fixed bus / deployment / control mass can be tolerated
once angle, node power, and target shell-relative utilization are all fixed.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.mass_budget import (
    max_fixed_mass_for_angle_power_fill_factor,
    minimum_power_for_fill_factor_with_structure,
)
from models.structural import NodeStructure


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

PHI_LEVELS_DEG = [1.0, 2.0]
POWER_LEVELS_W = [10000.0, 30000.0, 100000.0]
TARGET_FILL_FACTORS = [0.05, 0.10, 0.25]
ACS3_BUS_MASS_KG = 8.3

SCENARIOS = [
    {
        "label": "acs3_lines_dyneema_1p25mm",
        "structure": NodeStructure(
            topology="cross",
            boom_material="acs3_composite_boom_2023",
            tether_material="dyneema_1p25mm_usspars",
            fixed_mass_kg=ACS3_BUS_MASS_KG,
            line_mass_margin_factor=1.0,
        ),
    },
    {
        "label": "acs3_lines_dyneema_2mm",
        "structure": NodeStructure(
            topology="cross",
            boom_material="acs3_composite_boom_2023",
            tether_material="dyneema_2mm_usspars",
            fixed_mass_kg=ACS3_BUS_MASS_KG,
            line_mass_margin_factor=1.0,
        ),
    },
]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    allowance_rows = []
    power_rows = []

    for scenario in SCENARIOS:
        for phi_deg in PHI_LEVELS_DEG:
            for power_w in POWER_LEVELS_W:
                for target_fill_factor in TARGET_FILL_FACTORS:
                    allowance = max_fixed_mass_for_angle_power_fill_factor(
                        phi_deg=phi_deg,
                        pv_power_required_w=power_w,
                        target_fill_factor=target_fill_factor,
                        structure_model=scenario["structure"],
                    )
                    allowance_rows.append(
                        {
                            "scenario": scenario["label"],
                            "phi_deg": phi_deg,
                            "power_w": power_w,
                            "target_fill_factor": target_fill_factor,
                            "reflector_area_m2": allowance.reflector_area_m2,
                            "pv_area_m2": allowance.pv_area_m2,
                            "variable_structure_mass_kg": allowance.variable_structure_mass_kg,
                            "total_mass_budget_kg": allowance.total_mass_budget_kg,
                            "fixed_mass_max_kg": allowance.fixed_mass_max_kg,
                            "acs3_bus_mass_kg": ACS3_BUS_MASS_KG,
                            "acs3_bus_margin_kg": allowance.fixed_mass_max_kg - ACS3_BUS_MASS_KG,
                            "acs3_bus_ratio_to_allowance": ACS3_BUS_MASS_KG / allowance.fixed_mass_max_kg
                            if allowance.fixed_mass_max_kg > 0.0
                            else None,
                            "feasible_for_acs3_bus": allowance.fixed_mass_max_kg >= ACS3_BUS_MASS_KG,
                            "feasible_even_before_fixed_mass": allowance.feasible,
                        }
                    )

    for scenario in SCENARIOS:
        for phi_deg in PHI_LEVELS_DEG:
            for target_fill_factor in TARGET_FILL_FACTORS:
                threshold = minimum_power_for_fill_factor_with_structure(
                    phi_deg=phi_deg,
                    target_fill_factor=target_fill_factor,
                    structure_model=scenario["structure"],
                )
                power_rows.append(
                    {
                        "scenario": scenario["label"],
                        "phi_deg": phi_deg,
                        "target_fill_factor": target_fill_factor,
                        "acs3_bus_mass_kg": ACS3_BUS_MASS_KG,
                        "minimum_power_w_for_acs3_bus": None if threshold is None else threshold.power_w,
                        "feasible": threshold is not None,
                    }
                )

    write_csv(RESULTS_DIR / "fixed_mass_allowance.csv", allowance_rows)
    write_csv(RESULTS_DIR / "power_required_for_acs3_bus.csv", power_rows)

    def find_allowance(phi_deg: float, power_w: float, target_fill_factor: float, scenario: str) -> dict:
        for row in allowance_rows:
            if (
                row["scenario"] == scenario
                and row["phi_deg"] == phi_deg
                and row["power_w"] == power_w
                and row["target_fill_factor"] == target_fill_factor
            ):
                return row
        raise KeyError((phi_deg, power_w, target_fill_factor, scenario))

    def find_power(phi_deg: float, target_fill_factor: float, scenario: str) -> dict:
        for row in power_rows:
            if (
                row["scenario"] == scenario
                and row["phi_deg"] == phi_deg
                and row["target_fill_factor"] == target_fill_factor
            ):
                return row
        raise KeyError((phi_deg, target_fill_factor, scenario))

    summary = {
        "assumptions": {
            "acs3_bus_mass_kg": ACS3_BUS_MASS_KG,
            "phi_levels_deg": PHI_LEVELS_DEG,
            "power_levels_w": POWER_LEVELS_W,
            "target_fill_factors": TARGET_FILL_FACTORS,
        },
        "headline": {
            "one_deg_10kw": {
                "allowance_for_10pct": find_allowance(1.0, 10000.0, 0.10, "acs3_lines_dyneema_1p25mm"),
                "allowance_for_25pct": find_allowance(1.0, 10000.0, 0.25, "acs3_lines_dyneema_1p25mm"),
            },
            "two_deg_10kw": {
                "allowance_for_10pct": find_allowance(2.0, 10000.0, 0.10, "acs3_lines_dyneema_1p25mm"),
                "allowance_for_25pct": find_allowance(2.0, 10000.0, 0.25, "acs3_lines_dyneema_1p25mm"),
            },
            "power_required_for_acs3_bus": {
                "one_deg_10pct": find_power(1.0, 0.10, "acs3_lines_dyneema_1p25mm"),
                "one_deg_25pct": find_power(1.0, 0.25, "acs3_lines_dyneema_1p25mm"),
                "two_deg_10pct": find_power(2.0, 0.10, "acs3_lines_dyneema_1p25mm"),
            },
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
