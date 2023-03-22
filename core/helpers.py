from os import environ

import emotions
import fruits


def get_emotion_class():
    emoji_support = environ.get("SUPPORTS_EMOJI", "no")
    if emoji_support.lower() == "yes" or emoji_support.lower() == "true":
        return emotions.EmojiEmotions()
    return emotions.AsciiEmotions()


def get_fruit_class():
    emoji_support = environ.get("SUPPORTS_EMOJI", "no")
    if emoji_support.lower() == "yes" or emoji_support.lower() == "true":
        return fruits.EmojiFruit()
    return fruits.AsciiFruit()
