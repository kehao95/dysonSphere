"""
Perturbation sensitivity experiment for displaced MDDS rings.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.orbital import (
    cone_angle_tolerance_for_fraction,
    drift_time_for_offset,
    equivalent_beta_fraction_from_pressure,
    perturbed_force_balance,
)


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

PHI_LEVELS_DEG = [0.5, 1.0, 1.5, 2.0]
CONE_OFFSETS_DEG = [0.1, 0.25, 0.5, 1.0, 2.0]
BETA_SCALES = [0.99, 0.995, 1.005, 1.01]
SOLAR_WIND_PRESSURE_N_M2 = 2.6e-9


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"No rows available for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    cone_rows = []
    for phi_deg in PHI_LEVELS_DEG:
        for offset_deg in CONE_OFFSETS_DEG:
            state = perturbed_force_balance(
                phi_deg=phi_deg,
                beta_scale=1.0,
                cone_angle_offset_deg=offset_deg,
            )
            cone_rows.append(
                {
                    "phi_deg": phi_deg,
                    "cone_angle_offset_deg": offset_deg,
                    "axial_residual_fraction": state.axial_residual_fraction_of_nominal,
                    "radial_residual_fraction": state.radial_residual_fraction_of_nominal,
                }
            )
    write_csv(RESULTS_DIR / "cone_angle_sensitivity.csv", cone_rows)

    beta_rows = []
    for phi_deg in PHI_LEVELS_DEG:
        for beta_scale in BETA_SCALES:
            state = perturbed_force_balance(
                phi_deg=phi_deg,
                beta_scale=beta_scale,
                cone_angle_offset_deg=0.0,
            )
            beta_rows.append(
                {
                    "phi_deg": phi_deg,
                    "beta_scale": beta_scale,
                    "axial_residual_fraction": state.axial_residual_fraction_of_nominal,
                    "radial_residual_fraction": state.radial_residual_fraction_of_nominal,
                }
            )
    write_csv(RESULTS_DIR / "beta_sensitivity.csv", beta_rows)

    solar_wind_beta_fraction = equivalent_beta_fraction_from_pressure(SOLAR_WIND_PRESSURE_N_M2)
    solar_wind_state = perturbed_force_balance(phi_deg=1.0, beta_scale=1.0 + solar_wind_beta_fraction)
    solar_wind_drift_time_s = drift_time_for_offset(
        residual_accel_m_s2=abs(solar_wind_state.axial_residual_accel_m_s2),
        offset_distance_m=1.0e6,
    )

    summary = {
        "assumptions": {
            "reference_solar_wind_dynamic_pressure_n_m2": SOLAR_WIND_PRESSURE_N_M2,
            "offset_distance_for_drift_time_m": 1.0e6,
            "note": "Solar wind comparison is an order-of-magnitude external-disturbance check, not a full plasma interaction model.",
        },
        "cone_angle_tolerance_deg": {
            "phi_1deg_for_1pct_axial_residual": cone_angle_tolerance_for_fraction(1.0, 0.01),
            "phi_1deg_for_5pct_axial_residual": cone_angle_tolerance_for_fraction(1.0, 0.05),
            "phi_1deg_for_10pct_axial_residual": cone_angle_tolerance_for_fraction(1.0, 0.10),
        },
        "solar_wind_reference_case_at_1deg": {
            "equivalent_beta_fraction": solar_wind_beta_fraction,
            "axial_residual_fraction": solar_wind_state.axial_residual_fraction_of_nominal,
            "drift_time_to_1000km_s": solar_wind_drift_time_s,
            "drift_time_to_1000km_days": solar_wind_drift_time_s / 86400.0,
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
