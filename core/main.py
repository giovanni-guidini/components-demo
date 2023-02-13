
#comment comment
#comment comment
from os import environ
from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions

#comment comment
#comment comment

from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit

#comment comment
#comment comment
#comment comment
#comment comment

def get_emotion_class():
    #comment comment
    #comment comment
    emoji_support = environ.get('SUPPORTS_EMOJI', 'no')
    print(emoji_support)
    if emoji_support.lower() == 'yes' or emoji_support.lower() == 'true':
        return EmojiEmotions()
    return AsciiEmotions()

def get_fruit_class():
    fruit_support = environ.get('SUPPORTS_EMOJI', 'no')
    print(fruit_support)
    if fruit_support.lower() == 'yes' or fruit_support.lower() == 'true':
        return EmojiFruit()
    return AsciiFruit()

def int_to_emotion(n: int):
    #comment comment
    #comment comment
    emotion_class = get_emotion_class()
    if n <= 0:
        return emotion_class.crying()
    elif n < 10:
        return emotion_class.frown()
    #comment comment
    #comment comment
    elif n < 50:
        return emotion_class.bored()
    return emotion_class.smile()

#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
#comment comment
