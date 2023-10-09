from emotions import EmotionsInterface


class AsciiEmotions(EmotionsInterface):
    def smile(self):
        return ":)"

    def frown(self):
        return ":("

    def bored(self):
        return ":|"

    def crying(self):
        return "TT-TT"

    def unamused(self):
        return '--"'
