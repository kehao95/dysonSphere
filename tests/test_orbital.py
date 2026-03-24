import math
import unittest

from models.orbital import OPTIMAL_CONE_ANGLE_DEG, SIGMA_STAR, DisplacedOrbit


class OrbitalModelTests(unittest.TestCase):
    def test_sigma_star_reference_value(self):
        self.assertLess(abs(SIGMA_STAR * 1000.0 - 1.53), 0.01)

    def test_minimum_beta_at_one_degree(self):
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
        self.assertAlmostEqual(orbit.required_beta_exact(), 0.04534268199557577)

    def test_optimal_cone_angle_matches_closed_form(self):
        self.assertAlmostEqual(OPTIMAL_CONE_ANGLE_DEG, 35.264389682754654)

    def test_force_balance_closes_at_minimum_beta_solution(self):
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
        fb = orbit.force_balance()

        radial_total = fb.sail_radial_accel_m_s2 + fb.centripetal_accel_m_s2
        axial_total = fb.sail_axial_accel_m_s2

        expected_radial = fb.gravitational_accel_m_s2 * math.cos(math.radians(1.0))
        expected_axial = fb.gravitational_accel_m_s2 * math.sin(math.radians(1.0))

        self.assertLess(abs(radial_total - expected_radial) / expected_radial, 1e-12)
        self.assertLess(abs(axial_total - expected_axial) / expected_axial, 1e-12)

    def test_max_supported_angle_inverts_minimum_beta(self):
        orbit = DisplacedOrbit(r_au=1.0, phi_deg=2.0)
        phi_max = DisplacedOrbit.max_supported_angle_deg(orbit.required_beta_exact())
        self.assertAlmostEqual(phi_max, 2.0)


if __name__ == "__main__":
    unittest.main()
