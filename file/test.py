import unittest
import os
import json

import packages.file.main as file

class TestLoadJson(unittest.TestCase):
    def test_success(self):
        self.assertEqual({'test': ['A', 'B', 'C', 'D']}, file.load_json(f"{os.path.dirname(__file__)}/json/ok.json"))

    def test_not_found(self):
        self.assertRaises(FileNotFoundError, lambda: file.load_json(f"{os.path.dirname(__file__)}/rest.json"))

    def test_break_json_file(self):
        self.assertRaises(json.decoder.JSONDecodeError, lambda: file.load_json(f"{os.path.dirname(__file__)}/json/break.json"))
