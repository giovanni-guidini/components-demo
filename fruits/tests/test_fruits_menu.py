import unittest
from io import StringIO
from unittest.mock import patch

from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit
from fruits.menu import FruitsMenu


class TestFruitsMenu(unittest.TestCase):
    def test_init_emoji(self):
        fruits_menu = FruitsMenu(parent=None, fruit_obj=EmojiFruit())
        assert fruits_menu.name == "Fruits"
        assert fruits_menu.parent == None
        assert fruits_menu.menu_options_index == {
            "0": "apple",
            "1": "banana",
            "2": "cherry",
            "3": "grape",
            "4": "pineapple",
        }

    def test_init_ascii(self):
        fruits_menu = FruitsMenu(parent=None, fruit_obj=AsciiFruit())
        assert fruits_menu.name == "Fruits"
        assert fruits_menu.parent == None
        assert fruits_menu.menu_options_index == {
            "0": "apple",
            "1": "banana",
            "2": "cherry",
            "3": "grape",
            "4": "pineapple",
        }

    def test_menu_options(self):
        fruits_menu = FruitsMenu(parent=None, fruit_obj=EmojiFruit())
        assert fruits_menu.menu_options == [
            "0. apple",
            "1. banana",
            "2. cherry",
            "3. grape",
            "4. pineapple",
        ]

    @patch("builtins.input", side_effect=["0"])
    def test_menu_choice_apple(self, mock_input):
        fruits_menu = FruitsMenu(parent=None, fruit_obj=EmojiFruit())
        with patch("sys.stdout", new=StringIO()) as fake_output:
            fruits_menu.run()
            output_lines = fake_output.getvalue().strip().split("\n")
        expected_output = [
            "Welcome to the Fruits exhibit!",
            "",
            "Available fruits:",
            "0. apple",
            "1. banana",
            "2. cherry",
            "3. grape",
            "4. pineapple" "",
            "",
            "",
            "🍎",
        ]
        self.assertEqual(expected_output, output_lines)
