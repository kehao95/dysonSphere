"""
Flight-heritage gap analysis for MDDS-relevant solar-sail systems.

This run benchmarks real integrated solar-sail spacecraft against the exact
MDDS areal-density requirement, and decomposes ACS3 into subsystem slices to
show where the gap actually sits.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.orbital import DisplacedOrbit, SIGMA_STAR


RUN_DIR = Path(__file__).resolve().parent
RESULTS_DIR = RUN_DIR / "results"

PHI_LEVELS_DEG = [0.5, 1.0, 2.0]
ULTRALIGHT_TANDEM_SIGMA_G_M2 = 54.8

CASES = [
    {
        "label": "acs3_total_system",
        "source": "NASA ACS3 mission update (2023)",
        "deployed_area_m2": 80.0,
        "mass_kg": 16.0,
        "notes": "Total spacecraft mass including sail.",
    },
    {
        "label": "acs3_sail_boom_subsystem",
        "source": "NASA ACS3 mission update (2023)",
        "deployed_area_m2": 80.0,
        "mass_kg": 7.7,
        "notes": "Sail-Boom Subsystem (SBS) only.",
    },
    {
        "label": "acs3_bus_only",
        "source": "NASA ACS3 mission update (2023)",
        "deployed_area_m2": 80.0,
        "mass_kg": 8.3,
        "notes": "ACS3 spacecraft bus mass only.",
    },
    {
        "label": "acs3_membrane_plus_booms",
        "source": "NASA ACS3 mission update (2023)",
        "deployed_area_m2": 80.0,
        "mass_kg": 4.0 * 0.085 + 4.0 * 0.164,
        "notes": "ACS3 membrane and booms only, excluding the rest of the SBS and bus.",
    },
    {
        "label": "nea_scout_total_system",
        "source": "NASA NEA Scout paper (2017)",
        "deployed_area_m2": 86.0,
        "mass_kg": 14.0,
        "notes": "Upper-bound total system mass from the published 'less than 14 kg' statement.",
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

    rows = []
    for case in CASES:
        sigma_g_m2 = 1000.0 * case["mass_kg"] / case["deployed_area_m2"]
        beta = SIGMA_STAR / (sigma_g_m2 / 1000.0)
        phi_max_deg = DisplacedOrbit.max_supported_angle_deg(beta)

        row = {
            "case": case["label"],
            "source": case["source"],
            "deployed_area_m2": case["deployed_area_m2"],
            "mass_kg": case["mass_kg"],
            "system_areal_density_g_m2": sigma_g_m2,
            "beta": beta,
            "max_supported_angle_deg": phi_max_deg,
            "notes": case["notes"],
        }

        for phi_deg in PHI_LEVELS_DEG:
            sigma_limit = DisplacedOrbit(phi_deg=phi_deg).max_areal_density()
            allowed_mass = sigma_limit * case["deployed_area_m2"] / 1000.0
            row[f"sigma_limit_at_{str(phi_deg).replace('.', 'p')}_deg_g_m2"] = sigma_limit
            row[f"allowed_mass_at_{str(phi_deg).replace('.', 'p')}_deg_kg"] = allowed_mass
            row[f"mass_reduction_factor_to_{str(phi_deg).replace('.', 'p')}_deg"] = (
                case["mass_kg"] / allowed_mass
            )

        if case["label"] == "acs3_membrane_plus_booms":
            for phi_deg in PHI_LEVELS_DEG:
                sigma_limit = DisplacedOrbit(phi_deg=phi_deg).max_areal_density()
                leftover_sigma = sigma_limit - sigma_g_m2
                lambda_max = max(0.0, leftover_sigma / ULTRALIGHT_TANDEM_SIGMA_G_M2)
                row[f"ultralight_tandem_lambda_max_at_{str(phi_deg).replace('.', 'p')}_deg"] = lambda_max

        rows.append(row)

    write_csv(RESULTS_DIR / "heritage_gap.csv", rows)

    def by_label(label: str) -> dict:
        for row in rows:
            if row["case"] == label:
                return row
        raise KeyError(label)

    acs3_total = by_label("acs3_total_system")
    acs3_membrane_booms = by_label("acs3_membrane_plus_booms")
    nea_total = by_label("nea_scout_total_system")

    summary = {
        "headline": {
            "acs3_total_system": {
                "sigma_g_m2": acs3_total["system_areal_density_g_m2"],
                "beta": acs3_total["beta"],
                "max_supported_angle_deg": acs3_total["max_supported_angle_deg"],
                "reduction_factor_to_1deg": acs3_total["mass_reduction_factor_to_1p0_deg"],
            },
            "nea_scout_total_system": {
                "sigma_g_m2": nea_total["system_areal_density_g_m2"],
                "beta": nea_total["beta"],
                "max_supported_angle_deg": nea_total["max_supported_angle_deg"],
                "reduction_factor_to_1deg": nea_total["mass_reduction_factor_to_1p0_deg"],
            },
            "acs3_membrane_plus_booms": {
                "sigma_g_m2": acs3_membrane_booms["system_areal_density_g_m2"],
                "beta": acs3_membrane_booms["beta"],
                "max_supported_angle_deg": acs3_membrane_booms["max_supported_angle_deg"],
                "ultralight_tandem_lambda_max_at_1deg": acs3_membrane_booms[
                    "ultralight_tandem_lambda_max_at_1p0_deg"
                ],
            },
        },
        "interpretation": {
            "key_point": "Flight-demonstrated sailcraft validate deployable sail technology, but current integrated spacecraft are still several times too massive for 1-degree-class MDDS operation at 1 AU.",
            "acs3_decomposition": "ACS3 membrane plus booms alone are light enough for multi-degree displaced-orbit operation in principle, while the integrated spacecraft overhead drives the total system down to only ~0.17 deg.",
        },
    }

    with (RESULTS_DIR / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)


if __name__ == "__main__":
    main()
