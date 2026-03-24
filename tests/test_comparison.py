import unittest

from models.comparison import (
    equivalent_ring_half_angle_deg,
    ideal_ring_power,
    ideal_swarm_power,
    mdds_relative_to_ideal_swarm,
    required_efficiency_ratio_to_match_swarm,
    ring_capture_fraction,
)


class ComparisonTests(unittest.TestCase):
    def test_ring_capture_fraction_half_sphere(self):
        self.assertAlmostEqual(ring_capture_fraction(90.0), 1.0)

    def test_ring_capture_fraction_small_angle(self):
        self.assertAlmostEqual(ring_capture_fraction(1.0), 0.01745240643728351)

    def test_equivalent_ring_half_angle_inverts_fraction(self):
        self.assertAlmostEqual(
            equivalent_ring_half_angle_deg(ring_capture_fraction(15.0)),
            15.0,
        )

    def test_full_swarm_is_full_luminosity_times_efficiency(self):
        efficiency = 0.2
        self.assertAlmostEqual(
            ideal_swarm_power(efficiency=efficiency),
            efficiency * 3.828e26,
        )

    def test_ring_is_always_below_full_swarm(self):
        self.assertLess(
            ideal_ring_power(half_angle_deg=10.0, efficiency=0.25),
            ideal_swarm_power(efficiency=0.25),
        )

    def test_relative_to_swarm_reduces_to_fill_factor_for_equal_efficiency(self):
        self.assertAlmostEqual(
            mdds_relative_to_ideal_swarm(
                pv_fill_factor=0.525,
                mdds_efficiency=0.274,
                swarm_efficiency=0.274,
            ),
            0.525,
        )

    def test_required_efficiency_ratio_is_inverse_fill_factor(self):
        self.assertAlmostEqual(required_efficiency_ratio_to_match_swarm(0.5), 2.0)

    def test_same_shell_ratio_is_capped_by_unit_fill_factor(self):
        self.assertAlmostEqual(
            mdds_relative_to_ideal_swarm(
                pv_fill_factor=2.0,
                mdds_efficiency=0.25,
                swarm_efficiency=0.25,
            ),
            1.0,
        )


if __name__ == "__main__":
    unittest.main()
