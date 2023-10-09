from emotions import EmotionsInterface


class EmojiEmotions(EmotionsInterface):
    def smile(self):
        return "🙂"

    def frown(self):
        return "🙁"

    def bored(self):
        return "😶"

    def crying(self):
        return "😭"

    def unamused(self):
        return "😒"
