import unittest
from unittest.mock import patch, call

try:
    from units.week_01.lab_1a_finance import generate_financial_advice
except:
    from lab_1a_finance import generate_financial_advice

class TestPriceLab1aShipping(unittest.TestCase):
    def test_string_inputs(self):
        # Test all possible outcomes when using only string parameters
        self.assertEqual(generate_financial_advice("short", "low" ), "High-Yield Savings Account" )
        self.assertEqual(generate_financial_advice("short", "high"), "Short-Term Corporate Bonds" )
        self.assertEqual(generate_financial_advice("long",  "low" ), "Government Bonds/Index Fund")
        self.assertEqual(generate_financial_advice("long",  "high"), "Diversified Stock Portfolio")

    def test_number_inputs(self):
        # Test all possible outcomes when using numeric parameters
        self.assertEqual(generate_financial_advice(4.9, "low" ), "High-Yield Savings Account" )
        self.assertEqual(generate_financial_advice(4.9, "high"), "Short-Term Corporate Bonds" )
        self.assertEqual(generate_financial_advice(5,   "low" ), "Government Bonds/Index Fund")
        self.assertEqual(generate_financial_advice(5,   "high"), "Diversified Stock Portfolio")

    def test_invalid_horizon(self):
        # It should throw a ValueError if horizon is invalid
        with self.assertRaises(ValueError) as context:
            generate_financial_advice("shot", "low")
        self.assertTrue('Invalid time horizon.' in str(context.exception))

    def test_invalid_risk(self):
        # It should throw a ValueError if risk is invalid
        with self.assertRaises(ValueError) as context:
            generate_financial_advice("short", "lo")
        self.assertTrue('Invalid risk tolerance.' in str(context.exception))

    def test_invalid_negative_horizon(self):
        # It should throw a ValueError if time horizon is negative
        with self.assertRaises(ValueError) as context:
            generate_financial_advice(-1, "low")
        self.assertTrue('Invalid time horizon.' in str(context.exception))
