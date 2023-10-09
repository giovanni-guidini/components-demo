class EmotionsInterface:
    def smile(self):
        raise NotImplementedError()

    def frown(self):
        raise NotImplementedError()

    def bored(self):
        raise NotImplementedError()

    def crying(self):
        raise NotImplementedError()

    def unamused(self):
        raise NotImplementedError()


from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions
