import sys, os, unittest
from unittest.mock import patch, call

from .lab_2a_shipping import calculate_shipping_cost

class Lab2aTests(unittest.TestCase):
    def test_rules_tax(self):
        # It should be able to trigger all the rules that affect tax
        result = calculate_shipping_cost(1, 'A', 'A')
        self.assertEqual(result['tax'], 0.0)

        result = calculate_shipping_cost(1, 'B', 'A')
        self.assertEqual(result['tax'], 0.12)

        result = calculate_shipping_cost(1, 'C', 'A')
        self.assertEqual(result['tax'], 0.15)

    def test_rules_cost(self):
        # It should be able to trigger all the rules that affect cost
        # Shipping to zone A
        result = calculate_shipping_cost(1, 'A', 'A')
        self.assertEqual(result['cost'], 10.0)

        result = calculate_shipping_cost(6, 'A', 'A')
        self.assertEqual(result['cost'], 15.0)

        result = calculate_shipping_cost(11, 'A', 'A')
        self.assertEqual(result['cost'], 20.0)

        # Shipping to zone B
        result = calculate_shipping_cost(1, 'A', 'B')
        self.assertEqual(result['cost'], 15.0)

        result = calculate_shipping_cost(6, 'A', 'B')
        self.assertEqual(result['cost'], 20.0)

        result = calculate_shipping_cost(11, 'A', 'B')
        self.assertEqual(result['cost'], 25.0)

        # Shipping to zone C
        result = calculate_shipping_cost(1, 'A', 'C')
        self.assertEqual(result['cost'], 20.0)

        result = calculate_shipping_cost(6, 'A', 'C')
        self.assertEqual(result['cost'], 25.0)

        result = calculate_shipping_cost(11, 'A', 'C')
        self.assertEqual(result['cost'], 30.0)

    def test_rules_total(self):
        # It should be able to calculate the total cost correctly
        result = calculate_shipping_cost(1, 'A', 'A')
        self.assertAlmostEqual(result['total_cost'], 10.0)

        result = calculate_shipping_cost(1, 'B', 'A')
        self.assertAlmostEqual(result['total_cost'], 11.2)

        result = calculate_shipping_cost(1, 'C', 'A')
        self.assertAlmostEqual(result['total_cost'], 11.5)

        result = calculate_shipping_cost(6, 'B', 'A')
        self.assertAlmostEqual(result['total_cost'], 16.8)

        result = calculate_shipping_cost(11, 'C', 'A')
        self.assertAlmostEqual(result['total_cost'], 23)
