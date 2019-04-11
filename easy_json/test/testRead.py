import unittest
import sys
import os
import json
import easy_json

class TestRead(unittest.TestCase):
    def test_success(self):
        self.assertEqual({'test': ['A', 'B', 'C', 'D']}, easy_json.read(f"{os.path.dirname(__file__)}/json/ok.json"))

    def test_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: easy_json.read(f"{os.path.dirname(__file__)}/rest.json"))

    def test_break_json_file(self):
        self.assertRaises(json.decoder.JSONDecodeError, lambda: easy_json.read(f"{os.path.dirname(__file__)}//json/break.json"))
