
from os import environ
from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions

from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit


def get_emotion_class():
    emoji_support = environ.get('SUPPORTS_EMOJI', 'no')
    if emoji_support.lower() == 'yes' or emoji_support.lower() == 'true':
        return EmojiEmotions()
    return AsciiEmotions()

def get_fruit_class():
    fruit_support = environ.get('SUPPORTS_EMOJI', 'no')
    if fruit_support.lower() == 'yes' or fruit_support.lower() == 'true':
        return EmojiFruit()
    return AsciiFruit()

def int_to_emotion(n: int):
    emotion_class = get_emotion_class()
    if n <= 0:
        return emotion_class.crying()
    elif n < 10:
        return emotion_class.frown()
    elif n < 50:
        return emotion_class.bored()
    return emotion_class.smile()

