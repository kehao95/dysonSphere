import unittest

from models.thermal import ThermalEquilibrium, payload_temperature, reflector_temperature


class ThermalTests(unittest.TestCase):
    def test_reflector_runs_cooler_than_payload_at_1au(self):
        self.assertLess(
            reflector_temperature(distance_au=1.0),
            payload_temperature(distance_au=1.0),
        )

    def test_equilibrium_state_closes_energy_balance(self):
        thermal = ThermalEquilibrium(distance_au=1.0, absorptivity=0.1, emissivity=0.9)
        state = thermal.get_state(area_m2=2.0)
        self.assertLess(
            abs(state.absorbed_power_w - state.radiated_power_w) / state.absorbed_power_w,
            1e-12,
        )


if __name__ == "__main__":
    unittest.main()
