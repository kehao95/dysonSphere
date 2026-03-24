"""
Canonical first-pass feasibility experiment for the MDDS concept.

Outputs:
- results/angle_tradeoff.csv
- results/utilization_tradeoff.csv
- results/summary.json
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.mass_budget import SystemBudget, max_fill_factor_for_angle
from models.orbital import DisplacedOrbit
from models.thermal import payload_temperature, reflector_temperature


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"


CASES = [
    {
        "label": "CP1 + ultralight tandem",
        "reflector": "cp1_subsystem_nasa_2009",
        "pv": "ultralight_tandem_2021",
    },
    {
        "label": "CP1 + projected space CIGS",
        "reflector": "cp1_subsystem_nasa_2009",
        "pv": "cigs_space_projection_2002",
    },
    {
        "label": "CP1 + commercial CIGS module",
        "reflector": "cp1_subsystem_nasa_2009",
        "pv": "miasole_flex_03w_2018",
    },
    {
        "label": "Kapton + ultralight tandem",
        "reflector": "kapton_76um_nasa_2001",
        "pv": "ultralight_tandem_2021",
    },
]

ANGLE_GRID_DEG = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
UTILIZATION_TARGETS = [0.05, 0.10, 0.25, 0.50]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    angle_rows = []
    for phi_deg in ANGLE_GRID_DEG:
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=phi_deg)
        for case in CASES:
            summary = max_fill_factor_for_angle(
                phi_deg=phi_deg,
                reflector_material=case["reflector"],
                pv_material=case["pv"],
            )
            angle_rows.append(
                {
                    "case": case["label"],
                    "phi_deg": phi_deg,
                    "beta_required": summary.beta_required,
                    "sigma_limit_g_m2": summary.sigma_limit_g_m2,
                    "pv_fill_factor_max": summary.pv_fill_factor_max,
                    "relative_dyson_utilization_max": summary.relative_dyson_utilization_max,
                    "absolute_utilization_max": summary.absolute_utilization_max,
                    "vertical_displacement_km": orbit.vertical_displacement(),
                }
            )
    write_csv(RESULTS_DIR / "angle_tradeoff.csv", angle_rows)

    utilization_rows = []
    for case in CASES:
        for utilization in UTILIZATION_TARGETS:
            budget = SystemBudget.from_fill_factor(
                reflector_material=case["reflector"],
                pv_material=case["pv"],
                fill_factor=utilization,
                reflector_area_m2=1.0,
            )
            utilization_rows.append(
                {
                    "case": case["label"],
                    "relative_dyson_utilization_target": utilization,
                    "system_areal_density_g_m2": budget.system_areal_density(),
                    "system_beta": budget.system_beta(),
                    "phi_max_deg": budget.max_displacement_angle_deg(),
                    "absolute_utilization": budget.absolute_utilization(),
                }
            )
    write_csv(RESULTS_DIR / "utilization_tradeoff.csv", utilization_rows)

    one_degree_orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
    one_degree_force = one_degree_orbit.force_balance()
    best_case_one_degree = max_fill_factor_for_angle(
        phi_deg=1.0,
        reflector_material="cp1_subsystem_nasa_2009",
        pv_material="ultralight_tandem_2021",
    )

    summary = {
        "experiment": "20260323_mdds_feasibility",
        "assumptions": {
            "orbit_model": "ideal specular sail, exact displaced circular orbit, SRP-only",
            "comparison_metric": "relative Dyson utilization = PV fill factor versus an all-collector Dyson Swarm using the same PV technology",
            "angle_limit_definition": "maximum sustainable displacement angle for the given material pair and fill factor",
        },
        "reference_ring_phi_1_deg": {
            "beta_required": one_degree_force.beta,
            "cone_angle_deg": one_degree_force.cone_angle_deg,
            "omega_ratio": one_degree_force.omega_ratio,
            "period_days": one_degree_force.period_days,
            "vertical_displacement_km": one_degree_force.displacement_km,
            "sigma_limit_g_m2": one_degree_force.areal_density_g_m2,
            "gravity_accel_m_s2": one_degree_force.gravitational_accel_m_s2,
            "sail_radial_accel_m_s2": one_degree_force.sail_radial_accel_m_s2,
            "sail_axial_accel_m_s2": one_degree_force.sail_axial_accel_m_s2,
            "centripetal_accel_m_s2": one_degree_force.centripetal_accel_m_s2,
            "photon_pressure_n_m2": one_degree_force.photon_pressure_n_m2,
            "sail_force_radial_n_m2": one_degree_force.sail_force_radial_n_m2,
            "sail_force_axial_n_m2": one_degree_force.sail_force_axial_n_m2,
        },
        "best_case_current_materials_at_1_deg": {
            "case": "CP1 + ultralight tandem",
            "pv_fill_factor_max": best_case_one_degree.pv_fill_factor_max,
            "relative_dyson_utilization_max": best_case_one_degree.relative_dyson_utilization_max,
            "absolute_utilization_max": best_case_one_degree.absolute_utilization_max,
        },
        "reflector_only_angle_limits_deg": {
            "cp1_subsystem_nasa_2009": SystemBudget.from_fill_factor(
                reflector_material="cp1_subsystem_nasa_2009",
                pv_material="ultralight_tandem_2021",
                fill_factor=0.0,
            ).max_displacement_angle_deg(),
            "kapton_76um_nasa_2001": SystemBudget.from_fill_factor(
                reflector_material="kapton_76um_nasa_2001",
                pv_material="ultralight_tandem_2021",
                fill_factor=0.0,
            ).max_displacement_angle_deg(),
        },
        "thermal_snapshot_1au": {
            "reflector_k": reflector_temperature(distance_au=1.0, reflectivity=0.90),
            "payload_k_ultralight_tandem": payload_temperature(
                distance_au=1.0,
                pv_efficiency=0.274,
                absorptivity=0.90,
                emissivity=0.85,
            ),
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
