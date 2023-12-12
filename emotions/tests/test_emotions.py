from emotions.ascii import AsciiEmotions
from emotions.emoji import EmojiEmotions


class TestAsciiEmotions:
    emotion_class = AsciiEmotions()

    def test_smile(self):
        assert self.emotion_class.smile() == ":)"

    def test_frown(self):
        assert self.emotion_class.frown() == ":("

    def test_bored(self):
        assert self.emotion_class.bored() == ":|"

    def test_unamused(self):
        assert self.emotion_class.unamused() == '--"'
    
    def test_surprised(self):
        assert self.emotion_class.surprised() == ":O"


class TestEmojiEmotions:
    emotion_class = EmojiEmotions()

    def test_smile(self):
        assert self.emotion_class.smile() == "🙂"

    def test_frown(self):
        assert self.emotion_class.frown() == "🙁"

    def test_bored(self):
        assert self.emotion_class.bored() == "😶"

    def test_unamused(self):
        assert self.emotion_class.unamused() == "😒"

    def test_surprised(self):
        assert self.emotion_class.surprised() == "😮"
