
from os import environ
from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions

from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit


def get_emotion_class():
    emoji_support = environ.get('SUPPORTS_EMOJI', 'no')
    print(f"DEBUG emoji_support={emoji_support}")
    # comment
    if emoji_support.lower() == 'yes' or emoji_support.lower() == 'true':
        # unnecessary comment
        return EmojiEmotions()
    # unecessary comment
    return AsciiEmotions()

def get_fruit_class():
    fruit_support = environ.get('SUPPORTS_EMOJI', 'no')
    print(f"DEBUG fruit_support={fruit_support}")
    if fruit_support.lower() == 'yes' or fruit_support.lower() == 'true':
        return EmojiFruit()
    return AsciiFruit()

def int_to_emotion(n: int):
    print(f"DEBUG n={n}")
    emotion_class = get_emotion_class()
    if n <= 0:
        print(f"DEBUG returning crying")
        return emotion_class.crying()
    elif n < 10:
        print(f"DEBUG returning frown")
        return emotion_class.frown()
    elif n < 50:
        print(f"DEBUG returning bored")
        return emotion_class.bored()
    print(f"DEBUG returning smile")
    return emotion_class.smile()

# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comment comment
# comments comments
# comments comments
# comments comments
def func(a, b):
    return a + b
