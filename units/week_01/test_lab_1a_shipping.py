import unittest
from unittest.mock import patch, call

try:
    from units.week_01.lab_1a_shipping import calculate_shipping_cost
except:
    from lab_1a_shipping import calculate_shipping_cost

class TestPriceLab1aShipping(unittest.TestCase):
    @patch('builtins.print') # (Run within a print patch so that we don't get log spam)
    def test_all_possible_inputs(self, mock_print):
        # Test all possible outcomes, including boundary conditions
        self.assertEqual(calculate_shipping_cost(1,    "A"), 10.00)
        self.assertEqual(calculate_shipping_cost(5,    "A"), 10.00)
        self.assertEqual(calculate_shipping_cost(5.1,  "A"), 15.00)
        self.assertEqual(calculate_shipping_cost(10,   "A"), 15.00)
        self.assertEqual(calculate_shipping_cost(10.1, "A"), 20.00)
        self.assertEqual(calculate_shipping_cost(100,  "A"), 20.00)

        self.assertEqual(calculate_shipping_cost(1,    "B"), 15.00)
        self.assertEqual(calculate_shipping_cost(5,    "B"), 15.00)
        self.assertEqual(calculate_shipping_cost(5.1,  "B"), 20.00)
        self.assertEqual(calculate_shipping_cost(10,   "B"), 20.00)
        self.assertEqual(calculate_shipping_cost(10.1, "B"), 25.00)
        self.assertEqual(calculate_shipping_cost(100,  "B"), 25.00)

        self.assertEqual(calculate_shipping_cost(1,    "C"), 20.00)
        self.assertEqual(calculate_shipping_cost(5,    "C"), 20.00)
        self.assertEqual(calculate_shipping_cost(5.1,  "C"), 25.00)
        self.assertEqual(calculate_shipping_cost(10,   "C"), 25.00)
        self.assertEqual(calculate_shipping_cost(10.1, "C"), 30.00)
        self.assertEqual(calculate_shipping_cost(100,  "C"), 30.00)

    @patch('builtins.print')
    def test_zone_normalization(self, mock_print):
        # Should accept lower case zones
        self.assertEqual(calculate_shipping_cost(1, "a"), 10.00)

    def test_logs(self):
        # Should make all the expected logs
        with patch('builtins.print') as mock_print:
            calculate_shipping_cost(1, "A")
            mock_print.assert_has_calls([
                call("\n--- Shipping Cost Check ---"),
                call("Package Details: 1 kg to Zone A"),
                call("Calculated Shipping Cost: 10.00"),
                call("----------------------------"),
            ])

    def test_invalid_zone(self):
        # Should return nothing and print an error if the zone is invalid
        with patch('builtins.print') as mock_print:
            self.assertIsNone(calculate_shipping_cost(1, "d"))
            mock_print.assert_any_call("Error: Invalid shipping zone specified.")
