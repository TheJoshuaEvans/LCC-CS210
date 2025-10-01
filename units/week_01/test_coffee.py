# Import the standard unittest library
import unittest

# Adjust the import path so that the tests can be run as part of a complete test run
# from the root of the repository, as well as by directly calling this test file
try:
    # Running `python -m unittest` from root
    # This also allows the test explorer to work in VSCode
    from units.week_01.coffee import price_coffee
except:
    # Running `python units/week_01/test_coffee.py` from root
    from coffee import price_coffee

# Define a test suite
class TestPriceCoffee(unittest.TestCase):
    # Define a single test
    def test_all_possible_inputs(self):
        # Just go through all the possible combinations of inputs
        self.assertEqual(price_coffee("small", "oat"),      3.75)
        self.assertEqual(price_coffee("medium", "oat"),     4.75)
        self.assertEqual(price_coffee("large", "oat"),      6.25)

        self.assertEqual(price_coffee("small", "almond"),   3.50)
        self.assertEqual(price_coffee("medium", "almond"),  4.50)
        self.assertEqual(price_coffee("large", "almond"),   6.00)

        self.assertEqual(price_coffee("small", "dairy"),    3.00)
        self.assertEqual(price_coffee("medium", "dairy"),   4.00)
        self.assertEqual(price_coffee("large", "dairy"),    5.50)
        print("✅ Coffee pricing tests successful!")

# Run the tests if being called directly
if __name__ == '__main__':
    unittest.main()
