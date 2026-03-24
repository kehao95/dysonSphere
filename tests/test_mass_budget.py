import unittest

from models.mass_budget import SystemBudget, find_optimal_ratio, max_fill_factor_for_angle


class MassBudgetTests(unittest.TestCase):
    def test_relative_utilization_equals_fill_factor_for_same_pv_reference(self):
        budget = SystemBudget.from_fill_factor(
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="ultralight_tandem_2021",
            fill_factor=0.5,
            reflector_area_m2=100.0,
        )
        self.assertAlmostEqual(budget.relative_dyson_utilization(), 0.5)

    def test_one_degree_fill_factor_limit_for_cp1_plus_ultralight_tandem(self):
        summary = max_fill_factor_for_angle(
            phi_deg=1.0,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="ultralight_tandem_2021",
        )
        self.assertTrue(summary.feasible)
        self.assertAlmostEqual(summary.pv_fill_factor_max, 0.5248597974727819)

    def test_commercial_cigs_is_strongly_utilization_limited(self):
        summary = max_fill_factor_for_angle(
            phi_deg=1.0,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="miasole_flex_03w_2018",
        )
        self.assertLess(summary.pv_fill_factor_max, 0.02)

    def test_find_optimal_ratio_returns_feasible_design(self):
        budget = find_optimal_ratio(
            target_beta=0.04534268199557577,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="ultralight_tandem_2021",
            pv_power_required_w=100.0,
        )
        self.assertIsNotNone(budget)
        self.assertGreaterEqual(budget.power_output(), 100.0)


if __name__ == "__main__":
    unittest.main()
