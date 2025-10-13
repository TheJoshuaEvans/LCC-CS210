import sys, os, unittest
from unittest.mock import patch, call

from .write_json import write_json

original_cwd = os.getcwd()

OUTPUT_FILE_NAME = 'test_write_json_output.json'

# Construct the expected final path so we can retrieve the file and check its contents
this_dir = os.path.dirname(__file__)
test_output_file = os.path.realpath(os.path.join(this_dir, 'test_output', OUTPUT_FILE_NAME))

class TestWriteJson(unittest.TestCase):
    def test_write_json(self):
        json = {"test": "data"}
        write_result = write_json(f'utils/test_output/{OUTPUT_FILE_NAME}', json)
        self.assertEqual(write_result, True)

        # Check the file was written correctly
        with open(test_output_file, 'r') as f:
            data = f.read()
            self.assertEqual(data, '{\n    "test": "data"\n}')

    def tearDown(self):
        # Delete the test output file if it exists
        if os.path.exists(test_output_file):
            os.remove(test_output_file)
