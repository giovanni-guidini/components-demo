from fruits import FruitInterface


class EmojiFruit(FruitInterface):
    def banana(self):
        return "🍌"

    def apple(self) -> str:
        return "🍎"

    def cherry(self) -> str:
        return "🍒"

    def grape(self) -> str:
        return "🍇"

    def pineapple(self) -> str:
        return "🍍"
