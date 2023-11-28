import unittest
from io import StringIO
from typing import List
from unittest.mock import patch

from core.main import MainMenu


class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.main_menu = MainMenu()

    def test_init_values(self):
        self.assertEqual(self.main_menu.name, "Main Menu")
        self.assertEqual(self.main_menu.parent, None)

    def test_menu_options(self):
        expected_options = ["1. Fruits", "2. Emotions"]
        self.assertEqual(self.main_menu.menu_options, expected_options)

    @patch("builtins.input", side_effect=["1"])
    def test_menu_choice_fruits(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.main_menu.run()
            output_lines = fake_output.getvalue().strip().split("\n")
        expected_output = [
            "Welcome to the Gallery!",
            "",
            "Available expos:",
            "1. Fruits",
            "2. Emotions",
            "You selected the Fruits expo.",
        ]
        assert len(output_lines) == 6
        self.assertEqual(expected_output, output_lines)

    @patch("builtins.input", side_effect=["2"])
    def test_menu_choice_emotions(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.main_menu.run()
            output_lines = fake_output.getvalue().strip().split("\n")
        expected_output = [
            "Welcome to the Gallery!",
            "",
            "Available expos:",
            "1. Fruits",
            "2. Emotions",
            "You selected the Emotions expo.",
        ]
        self.assertEqual(expected_output, output_lines)

    @patch("builtins.input", side_effect=["3", "1"])
    def test_invalid_menu_choice(self, mock_input):
        expected_output = "Invalid choice."
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.main_menu.run()
            output_lines = fake_output.getvalue().strip().split("\n")
        expected_output = [
            "Welcome to the Gallery!",
            "",
            "Available expos:",
            "1. Fruits",
            "2. Emotions",
            "Invalid choice.",
            "Available expos:",
            "1. Fruits",
            "2. Emotions",
            "You selected the Fruits expo.",
        ]
        self.assertEqual(expected_output, output_lines)
