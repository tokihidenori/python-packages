import unittest
import sys
import os
import json
import easy_json

class TestWrite(unittest.TestCase):
    def test_success(self):
        test_json_path = f"{os.path.dirname(__file__)}/json/testWrite.json"
        easy_json.write(test_json_path, {'test': ['A', 'B', 'C', 'D']})
        self.assertEqual(easy_json.read(test_json_path), easy_json.read(f"{os.path.dirname(__file__)}/json/ok.json"))
        os.remove(test_json_path)

    def test_not_found_dir(self):
        self.assertRaises(FileNotFoundError, lambda: easy_json.write(f"{os.path.dirname(__file__)}/json2/testWrite.json", {'test': ['A', 'B', 'C', 'D']}))
