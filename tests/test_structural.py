import unittest

from models.mass_budget import (
    design_for_angle_power_with_structure,
    max_fixed_mass_for_angle_power_fill_factor,
    minimum_power_for_fill_factor_with_structure,
)
from models.structural import NodeStructure


class StructuralTests(unittest.TestCase):
    def test_extra_areal_density_drops_with_size(self):
        structure = NodeStructure(topology="cross", fixed_mass_kg=1.0)
        sigma_small = structure.extra_areal_density(100.0)
        sigma_large = structure.extra_areal_density(10000.0)
        self.assertGreater(sigma_small, sigma_large)

    def test_perimeter_topology_is_heavier_than_cross(self):
        cross = NodeStructure(topology="cross", fixed_mass_kg=1.0)
        perimeter = NodeStructure(topology="perimeter", fixed_mass_kg=1.0)
        self.assertGreater(
            perimeter.extra_areal_density(1000.0),
            cross.extra_areal_density(1000.0),
        )

    def test_structural_design_solver_finds_feasible_100w_node(self):
        structure = NodeStructure(topology="cross", fixed_mass_kg=1.0)
        design = design_for_angle_power_with_structure(
            phi_deg=1.0,
            pv_power_required_w=100.0,
            reflector_material="cp1_subsystem_nasa_2009",
            pv_material="ultralight_tandem_2021",
            structure_model=structure,
        )
        self.assertIsNotNone(design)
        self.assertTrue(design.feasible)
        self.assertGreater(design.reflector_area_m2, design.pv_area_m2)

    def test_heavier_structure_requires_larger_area(self):
        light = NodeStructure(topology="cross", fixed_mass_kg=0.5)
        heavy = NodeStructure(topology="perimeter", fixed_mass_kg=5.0)
        design_light = design_for_angle_power_with_structure(
            phi_deg=1.0,
            pv_power_required_w=100.0,
            structure_model=light,
        )
        design_heavy = design_for_angle_power_with_structure(
            phi_deg=1.0,
            pv_power_required_w=100.0,
            structure_model=heavy,
        )
        self.assertIsNotNone(design_light)
        self.assertIsNotNone(design_heavy)
        self.assertGreater(design_heavy.reflector_area_m2, design_light.reflector_area_m2)

    def test_minimum_power_threshold_hits_target_fill_factor(self):
        structure = NodeStructure(
            topology="cross", fixed_mass_kg=0.5, line_mass_margin_factor=1.1
        )
        threshold = minimum_power_for_fill_factor_with_structure(
            phi_deg=1.0,
            target_fill_factor=0.10,
            structure_model=structure,
        )
        self.assertIsNotNone(threshold)
        self.assertTrue(threshold.feasible)
        self.assertAlmostEqual(threshold.pv_area_m2 / threshold.reflector_area_m2, 0.10)
        self.assertAlmostEqual(threshold.power_w, 3130.911412723143, places=6)

    def test_heavier_structure_requires_more_power_for_same_fill_factor(self):
        light = NodeStructure(
            topology="cross", fixed_mass_kg=0.5, line_mass_margin_factor=1.1
        )
        heavy = NodeStructure(topology="cross", fixed_mass_kg=1.0, line_mass_margin_factor=1.2)
        threshold_light = minimum_power_for_fill_factor_with_structure(
            phi_deg=1.0,
            target_fill_factor=0.10,
            structure_model=light,
        )
        threshold_heavy = minimum_power_for_fill_factor_with_structure(
            phi_deg=1.0,
            target_fill_factor=0.10,
            structure_model=heavy,
        )
        self.assertIsNotNone(threshold_light)
        self.assertIsNotNone(threshold_heavy)
        self.assertGreater(threshold_heavy.power_w, threshold_light.power_w)

    def test_fixed_mass_allowance_matches_known_1deg_10kw_10pct_case(self):
        structure = NodeStructure(
            topology="cross",
            boom_material="acs3_composite_boom_2023",
            tether_material="dyneema_1p25mm_usspars",
            fixed_mass_kg=8.3,
            line_mass_margin_factor=1.0,
        )
        allowance = max_fixed_mass_for_angle_power_fill_factor(
            phi_deg=1.0,
            pv_power_required_w=10000.0,
            target_fill_factor=0.10,
            structure_model=structure,
        )
        self.assertTrue(allowance.feasible)
        self.assertAlmostEqual(allowance.reflector_area_m2, 268.1583421378655)
        self.assertAlmostEqual(allowance.fixed_mass_max_kg, 5.109079167082795, places=6)

    def test_two_degree_quarter_swarm_case_can_be_infeasible_even_before_fixed_mass(self):
        structure = NodeStructure(
            topology="cross",
            boom_material="acs3_composite_boom_2023",
            tether_material="dyneema_1p25mm_usspars",
            fixed_mass_kg=8.3,
            line_mass_margin_factor=1.0,
        )
        allowance = max_fixed_mass_for_angle_power_fill_factor(
            phi_deg=2.0,
            pv_power_required_w=10000.0,
            target_fill_factor=0.25,
            structure_model=structure,
        )
        self.assertFalse(allowance.feasible)
        self.assertLess(allowance.fixed_mass_max_kg, 0.0)


if __name__ == "__main__":
    unittest.main()
