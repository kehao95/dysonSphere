"""
Linearized stability-response analysis around the optimal MDDS cone angle.
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
    linearized_optimal_response,
    optimal_cone_angle_rad,
    perturbed_force_balance,
)


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

DELTA_ALPHA_DEG = [0.1, 0.25, 0.5, 1.0, 2.0]


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
    for delta_deg in DELTA_ALPHA_DEG:
        exact = perturbed_force_balance(phi_deg=1.0, cone_angle_offset_deg=delta_deg)
        linearized = linearized_optimal_response(cone_angle_offset_deg=delta_deg)
        rows.append(
            {
                "delta_alpha_deg": delta_deg,
                "delta_alpha_rad": linearized.cone_angle_offset_rad,
                "exact_axial_fraction": exact.axial_residual_fraction_of_nominal,
                "approx_axial_fraction": abs(linearized.axial_fraction_approx),
                "axial_relative_error": abs(
                    exact.axial_residual_fraction_of_nominal
                    - abs(linearized.axial_fraction_approx)
                )
                / exact.axial_residual_fraction_of_nominal,
                "exact_radial_fraction": exact.radial_residual_fraction_of_nominal,
                "approx_radial_fraction": abs(linearized.radial_fraction_approx),
                "radial_relative_error": abs(
                    exact.radial_residual_fraction_of_nominal
                    - abs(linearized.radial_fraction_approx)
                )
                / exact.radial_residual_fraction_of_nominal,
            }
        )

    write_csv(RESULTS_DIR / "linearized_vs_exact.csv", rows)

    summary = {
        "closed_form": {
            "optimal_cone_angle_rad": optimal_cone_angle_rad(),
            "optimal_cone_angle_deg": 35.264389682754654,
            "axial_fraction_formula": "eps_beta - 3 * delta_alpha_rad^2",
            "radial_fraction_formula": "eps_beta - (3/sqrt(2)) * delta_alpha_rad",
            "interpretation": "Axial response is second-order in cone-angle error, radial response is first-order.",
        },
        "headline_checks": {
            "delta_0p5_deg": rows[2],
            "delta_1p0_deg": rows[3],
            "delta_2p0_deg": rows[4],
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
