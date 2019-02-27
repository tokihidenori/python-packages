import unittest
import sys
import os
import json
sys.path.append(f"{os.path.dirname(__file__)}/../../")
import easy_json

class TestLoadJson(unittest.TestCase):
    def test_success(self):
        self.assertEqual({'test': ['A', 'B', 'C', 'D']}, easy_json.read(f"{os.path.dirname(__file__)}/json/ok.json"))

    def test_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: easy_json.read(f"{os.path.dirname(__file__)}/rest.json"))

    def test_break_json_file(self):
        self.assertRaises(json.decoder.JSONDecodeError, lambda: easy_json.read(f"{os.path.dirname(__file__)}//json/break.json"))
