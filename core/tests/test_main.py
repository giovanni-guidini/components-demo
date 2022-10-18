import os
from unittest import mock

import pytest

from core.main import get_emotion_class, int_to_emotion
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

@pytest.mark.parametrize("value,result", [(-10, "TT-TT"), (50, ":)"), (49, ":|")])
def test_int_to_emotion(value, result):
    assert int_to_emotion(value) == result