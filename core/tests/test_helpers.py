import os
import unittest
from unittest import mock

import fruits
from core.helpers import get_emotion_class, get_fruit_class
from emotions import EmotionsInterface
from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions


def test_select_emotion_emoji():
    with mock.patch.dict(os.environ, {"SUPPORTS_EMOJI": "True"}):
        emotion_class = get_emotion_class()
        assert isinstance(emotion_class, EmotionsInterface)
        assert isinstance(emotion_class, EmojiEmotions)


def test_select_emotion_default():
    with mock.patch.dict(os.environ, {}):
        emotion_class = get_emotion_class()
        assert isinstance(emotion_class, EmotionsInterface)
        assert isinstance(emotion_class, AsciiEmotions)


def test_select_emotion_no_support_to_emoji():
    with mock.patch.dict(os.environ, {"SUPPORTS_EMOJI": "False"}):
        emotion_class = get_emotion_class()
        assert isinstance(emotion_class, EmotionsInterface)
        assert isinstance(emotion_class, AsciiEmotions)


def test_select_emotion_fallback():
    with mock.patch.dict(os.environ, {"SUPPORTS_EMOJI": "Random Value"}):
        emotion_class = get_emotion_class()
        assert isinstance(emotion_class, EmotionsInterface)
        assert isinstance(emotion_class, AsciiEmotions)


class TestGetFruitClass(unittest.TestCase):
    @mock.patch("core.helpers.environ")
    def test_get_fruit_class_emoji_support_true(self, mock_environ):
        mock_environ.get.return_value = "true"
        expected = fruits.EmojiFruit
        actual = get_fruit_class()
        self.assertIsInstance(actual, expected)

    @mock.patch("core.helpers.environ")
    def test_get_fruit_class_emoji_support_yes(self, mock_environ):
        mock_environ.get.return_value = "yes"
        expected = fruits.EmojiFruit
        actual = get_fruit_class()
        self.assertIsInstance(actual, expected)

    @mock.patch("core.helpers.environ")
    def test_get_fruit_class_emoji_support_no(self, mock_environ):
        mock_environ.get.return_value = "no"
        expected = fruits.AsciiFruit
        actual = get_fruit_class()
        self.assertIsInstance(actual, expected)

    @mock.patch("core.helpers.environ")
    def test_get_fruit_class_emoji_support_false(self, mock_environ):
        mock_environ.get.return_value = "false"
        expected = fruits.AsciiFruit
        actual = get_fruit_class()
        self.assertIsInstance(actual, expected)
