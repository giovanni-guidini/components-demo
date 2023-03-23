import inspect
from os import environ
from typing import Callable, List

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


def list_available_methods(klass: object) -> List[Callable]:
    if not inspect.isclass(klass):
        raise Exception(f"{type(klass)} is not a class.")
    klass_methods = [x for x in dir(klass) if inspect.isfunction(getattr(klass, x))]
    return klass_methods
