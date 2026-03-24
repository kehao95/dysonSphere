"""
Controlled-variable benchmark comparison between MDDS, ideal Dyson Swarm,
and ideal Dyson Ring.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.comparison import (
    equivalent_ring_half_angle_deg,
    mdds_relative_to_ideal_swarm,
    required_efficiency_ratio_to_match_swarm,
)
from models.mass_budget import get_material, max_fill_factor_for_angle
from models.orbital import DisplacedOrbit


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"
SOLAR_FLUX_1AU = 1361.0

PHI_GRID_DEG = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
EXTRA_AREAL_DENSITIES = [0.0, 5.0, 10.0]

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
        "label": "CP1 + commercial CIGS",
        "reflector": "cp1_subsystem_nasa_2009",
        "pv": "miasole_flex_03w_2018",
    },
]


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def specific_power_required(efficiency: float, sigma_pv_g_m2: float) -> float:
    """Return required electrical specific power in W/kg at 1 AU."""
    if sigma_pv_g_m2 <= 0.0:
        return math.inf
    return 1000.0 * efficiency * SOLAR_FLUX_1AU / sigma_pv_g_m2


def critical_phi_for_same_efficiency_parity(extra_sigma: float) -> float:
    """
    Return the largest phi for which CP1 + ultralight tandem still reaches lambda >= 1.
    """
    lo, hi = 0.01, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lam = max_fill_factor_for_angle(
            phi_deg=mid,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="ultralight_tandem_2021",
            extra_areal_density_g_m2=extra_sigma,
        ).pv_fill_factor_max
        if lam >= 1.0:
            lo = mid
        else:
            hi = mid
    return lo


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    threshold_rows = []
    for phi_deg in PHI_GRID_DEG:
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=phi_deg)
        sigma_max = orbit.max_areal_density()
        for reflector_key in ("cp1_subsystem_nasa_2009", "kapton_76um_nasa_2001"):
            reflector = get_material(reflector_key)
            for extra_sigma in EXTRA_AREAL_DENSITIES:
                pv_sigma_threshold = max(0.0, sigma_max - reflector.areal_density - extra_sigma)
                threshold_rows.append(
                    {
                        "phi_deg": phi_deg,
                        "reflector": reflector_key,
                        "extra_areal_density_g_m2": extra_sigma,
                        "sigma_max_total_g_m2": sigma_max,
                        "pv_sigma_threshold_same_efficiency_g_m2": pv_sigma_threshold,
                        "required_specific_power_27p4pct_w_kg": specific_power_required(
                            efficiency=0.274,
                            sigma_pv_g_m2=pv_sigma_threshold,
                        ),
                        "required_specific_power_15pct_w_kg": specific_power_required(
                            efficiency=0.15,
                            sigma_pv_g_m2=pv_sigma_threshold,
                        ),
                    }
                )
    write_csv(RESULTS_DIR / "parity_thresholds.csv", threshold_rows)

    comparison_rows = []
    for phi_deg in PHI_GRID_DEG:
        for extra_sigma in EXTRA_AREAL_DENSITIES:
            for case in CASES:
                summary = max_fill_factor_for_angle(
                    phi_deg=phi_deg,
                    reflector_material=case["reflector"],
                    pv_material=case["pv"],
                    extra_areal_density_g_m2=extra_sigma,
                )
                pv = get_material(case["pv"])
                relative_same_eta = mdds_relative_to_ideal_swarm(
                    pv_fill_factor=summary.pv_fill_factor_max,
                    mdds_efficiency=pv.efficiency or 0.0,
                    swarm_efficiency=pv.efficiency or 0.0,
                )
                relative_vs_15pct = mdds_relative_to_ideal_swarm(
                    pv_fill_factor=summary.pv_fill_factor_max,
                    mdds_efficiency=pv.efficiency or 0.0,
                    swarm_efficiency=0.15,
                )
                comparison_rows.append(
                    {
                        "case": case["label"],
                        "phi_deg": phi_deg,
                        "extra_areal_density_g_m2": extra_sigma,
                        "beta_required": summary.beta_required,
                        "pv_fill_factor_max": summary.pv_fill_factor_max,
                        "relative_to_ideal_swarm_same_eta": relative_same_eta,
                        "relative_to_ideal_swarm_vs_15pct_baseline": relative_vs_15pct,
                        "equivalent_ideal_ring_half_angle_deg_same_eta": equivalent_ring_half_angle_deg(
                            min(1.0, relative_same_eta)
                        ),
                        "efficiency_ratio_needed_for_parity": required_efficiency_ratio_to_match_swarm(
                            relative_same_eta
                        ),
                    }
                )
    write_csv(RESULTS_DIR / "current_material_comparison.csv", comparison_rows)

    best_1deg = max_fill_factor_for_angle(
        phi_deg=1.0,
        reflector_material="cp1_subsystem_nasa_2009",
        pv_material="ultralight_tandem_2021",
    )
    best_1deg_plus_margin = max_fill_factor_for_angle(
        phi_deg=1.0,
        reflector_material="cp1_subsystem_nasa_2009",
        pv_material="ultralight_tandem_2021",
        extra_areal_density_g_m2=5.0,
    )

    summary = {
        "controlled_assumptions": {
            "same_orbital_radius": True,
            "same_ideal_collector_physics": True,
            "aging_ignored": True,
            "thermal_degradation_ignored": True,
            "maintenance_losses_ignored": True,
        },
        "headline_1deg": {
            "sigma_max_total_g_m2": DisplacedOrbit(1.0, 1.0).max_areal_density(),
            "cp1_pv_threshold_same_efficiency_g_m2_no_margin": DisplacedOrbit(1.0, 1.0).max_areal_density()
            - get_material("cp1_subsystem_nasa_2009").areal_density,
            "cp1_pv_threshold_same_efficiency_g_m2_plus5_margin": DisplacedOrbit(1.0, 1.0).max_areal_density()
            - get_material("cp1_subsystem_nasa_2009").areal_density
            - 5.0,
            "best_current_case_relative_to_ideal_swarm_same_eta": best_1deg.pv_fill_factor_max,
            "best_current_case_relative_to_ideal_swarm_vs_15pct_baseline": mdds_relative_to_ideal_swarm(
                pv_fill_factor=best_1deg.pv_fill_factor_max,
                mdds_efficiency=get_material("ultralight_tandem_2021").efficiency,
                swarm_efficiency=0.15,
            ),
            "best_current_case_equivalent_ring_half_angle_deg": equivalent_ring_half_angle_deg(
                best_1deg.pv_fill_factor_max
            ),
            "efficiency_ratio_needed_for_parity_same_shell": required_efficiency_ratio_to_match_swarm(
                best_1deg.pv_fill_factor_max
            ),
            "best_current_case_relative_same_eta_plus5_margin": best_1deg_plus_margin.pv_fill_factor_max,
        },
        "critical_phi_same_efficiency_parity_deg": {
            "cp1_plus_ultralight_extra0": critical_phi_for_same_efficiency_parity(0.0),
            "cp1_plus_ultralight_extra5": critical_phi_for_same_efficiency_parity(5.0),
            "cp1_plus_ultralight_extra10": critical_phi_for_same_efficiency_parity(10.0),
        },
        "material_gap": {
            "ultralight_tandem_sigma_g_m2": get_material("ultralight_tandem_2021").areal_density,
            "space_cigs_sigma_g_m2": get_material("cigs_space_projection_2002").areal_density,
            "commercial_cigs_sigma_g_m2": get_material("miasole_flex_03w_2018").areal_density,
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
