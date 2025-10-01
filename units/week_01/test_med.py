import sys
import unittest
from unittest.mock import patch, call

try:
    from units.week_01.med import diagnose_symptoms
except:
    from med import diagnose_symptoms

# Since the prompt is to "replicate existing code" I think it is fair to expect that the
# function output should match the existing code's output exactly
class TestPriceCoffee(unittest.TestCase):
    # Use the "patch" decorator to mock the print function so we can capture its output
    @patch('builtins.print')
    def test_flu(self, mock_print):
        diagnose_symptoms(True, True)
        mock_print.assert_has_calls([
            call('------------------------------'),
            call('Patient Symptoms: Fever (True), Persistent Cough (True)'),
            call('Diagnosis: Flu - Recommend rest and hydration.')
        ])
        # Write success message directly to stdout since we mocked `print`
        sys.stdout.write("\n✅ Flu diagnosis test successful!\n")

    @patch('builtins.print')
    def test_infection(self, mock_print):
        diagnose_symptoms(True, False)
        mock_print.assert_has_calls([
            call('------------------------------'),
            call('Patient Symptoms: Fever (True), Persistent Cough (False)'),
            call('Diagnosis: Possible Infection - Recommend primary care physician visit.')
        ])
        sys.stdout.write("\n✅ Possible Infection diagnosis test successful!\n")

    @patch('builtins.print')
    def test_cold(self, mock_print):
        diagnose_symptoms(False, True)
        mock_print.assert_has_calls([
            call('------------------------------'),
            call('Patient Symptoms: Fever (False), Persistent Cough (True)'),
            call('Diagnosis: Cold/Allergies - Recommend over-the-counter medication.')
        ])
        sys.stdout.write("\n✅ Cold/Allergies diagnosis test successful!\n")

    @patch('builtins.print')
    def test_general_checkup(self, mock_print):
        diagnose_symptoms(False, False)
        mock_print.assert_has_calls([
            call('------------------------------'),
            call('Patient Symptoms: Fever (False), Persistent Cough (False)'),
            call('Diagnosis: General Check-up - Patient appears healthy.')
        ])
        sys.stdout.write("\n✅ General Check-up diagnosis test successful!\n")

# Run the tests if being called directly
if __name__ == '__main__':
    unittest.main()
