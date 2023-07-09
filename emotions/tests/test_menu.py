import unittest
from io import StringIO
from unittest.mock import patch

from emotions.menu import EmotionsMenu
from emotions.emoji import EmojiEmotions
from emotions.ascii import AsciiEmotions


class TestFruitsMenu(unittest.TestCase):
    def test_init_emoji(self):
        fruits_menu = EmotionsMenu(parent=None, emotions_obj=EmojiEmotions())
        assert fruits_menu.name == "Emotions"
        assert fruits_menu.parent == None
        assert fruits_menu.menu_options_index == {
            "0": "bored",
            "1": "crying",
            "2": "frown",
            "3": "smile",
        }

    def test_init_ascii(self):
        fruits_menu = EmotionsMenu(parent=None, emotions_obj=AsciiEmotions())
        assert fruits_menu.name == "Emotions"
        assert fruits_menu.parent == None
        assert fruits_menu.menu_options_index == {
            "0": "bored",
            "1": "crying",
            "2": "frown",
            "3": "smile",
        }

    def test_menu_options(self):
        fruits_menu = EmotionsMenu(parent=None, emotions_obj=EmojiEmotions())
        assert fruits_menu.menu_options == [
            "0. bored",
            "1. crying",
            "2. frown",
            "3. smile",
        ]

    @patch("builtins.input", side_effect=["0"])
    def test_menu_choice_apple(self, mock_input):
        fruits_menu = EmotionsMenu(parent=None, emotions_obj=EmojiEmotions())
        with patch("sys.stdout", new=StringIO()) as fake_output:
            fruits_menu.run()
            output_lines = fake_output.getvalue().strip().split("\n")
        expected_output = [
            "Welcome to the Emotions exhibit!",
            "",
            "Available emotions:",
            "0. bored",
            "1. crying",
            "2. frown",
            "3. smile" "",
            "",
            "",
            "😶",
        ]
        self.assertEqual(expected_output, output_lines)
