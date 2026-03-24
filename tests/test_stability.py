import math
import unittest

from models.orbital import (
    beta_tolerance_for_fraction,
    cone_angle_tolerance_for_fraction,
    drift_time_for_offset,
    equivalent_beta_fraction_from_pressure,
    linearized_optimal_response,
    optimal_cone_angle_rad,
    perturbed_force_balance,
)


class StabilityTests(unittest.TestCase):
    def test_nominal_perturbation_state_has_zero_residual(self):
        state = perturbed_force_balance(phi_deg=1.0)
        self.assertLess(abs(state.axial_residual_accel_m_s2), 1e-15)
        self.assertLess(abs(state.radial_residual_accel_m_s2), 1e-15)

    def test_beta_tolerance_is_linear(self):
        self.assertAlmostEqual(beta_tolerance_for_fraction(0.05), 0.05)

    def test_optimal_cone_angle_matches_closed_form_radians(self):
        self.assertAlmostEqual(optimal_cone_angle_rad(), 0.6154797086703874)

    def test_linearized_axial_response_matches_exact_small_angle(self):
        exact = perturbed_force_balance(phi_deg=1.0, cone_angle_offset_deg=0.5)
        linearized = linearized_optimal_response(cone_angle_offset_deg=0.5)
        self.assertAlmostEqual(
            exact.axial_residual_fraction_of_nominal,
            abs(linearized.axial_fraction_approx),
            delta=2.0e-4,
        )

    def test_linearized_radial_response_matches_exact_small_angle(self):
        exact = perturbed_force_balance(phi_deg=1.0, cone_angle_offset_deg=0.1)
        linearized = linearized_optimal_response(cone_angle_offset_deg=0.1)
        self.assertAlmostEqual(
            exact.radial_residual_fraction_of_nominal,
            abs(linearized.radial_fraction_approx),
            delta=1.0e-5,
        )

    def test_linearized_axial_quadratic_coefficient_predicts_one_percent_tolerance(self):
        linearized = linearized_optimal_response(cone_angle_offset_deg=3.31)
        self.assertAlmostEqual(abs(linearized.axial_fraction_approx), 0.01, delta=5.0e-4)

    def test_cone_angle_tolerance_is_positive(self):
        self.assertGreater(cone_angle_tolerance_for_fraction(1.0, 0.01), 0.0)

    def test_equivalent_beta_fraction_from_pressure_is_small_for_nanopascal_disturbance(self):
        frac = equivalent_beta_fraction_from_pressure(2.6e-9)
        self.assertLess(frac, 1e-3)

    def test_drift_time_matches_constant_acceleration_formula(self):
        accel = 1.0e-6
        offset = 1000.0
        expected = math.sqrt(2.0 * offset / accel)
        self.assertAlmostEqual(drift_time_for_offset(accel, offset), expected)


if __name__ == "__main__":
    unittest.main()
