import sys, os, unittest
from unittest.mock import patch, call

from .generate_file_path import generate_file_path

original_cwd = os.getcwd()

class TestGenerateFilePath(unittest.TestCase):
    def test_file_path_generation(self):
        # Carefully construct the expected path so this test will work on any computer
        ## Get the absolute path of this testing file
        this_file_path = os.path.abspath(__file__)

        ## Go up one level to the "week_02" directory
        week_02_dir = os.path.join(os.path.dirname(this_file_path), '..')

        ## Add the target file name to the path
        target_file_path = os.path.join(week_02_dir, 'test.json')

        ## Re-normalize
        expected_file_path = os.path.realpath(target_file_path)

        # Test!
        actual_path = generate_file_path('test.json')
        self.assertEqual(actual_path, expected_file_path)
