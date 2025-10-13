import sys, os, unittest
from unittest.mock import patch, call

from .read_json import read_json

class TestReadJson(unittest.TestCase):
    def test_read_nothing(self):
        # It should return "None" if no file is found
        result = read_json('utils/no_such_file.json')
        self.assertEqual(result, None)
