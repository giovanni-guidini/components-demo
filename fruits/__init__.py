class FruitInterface:
    def banana(self) -> str:
        raise NotImplementedError()

    def apple(self) -> str:
        raise NotImplementedError()

    def cherry(self) -> str:
        raise NotImplementedError()

    def grape(self) -> str:
        raise NotImplementedError()

    def pineapple(self) -> str:
        raise NotImplementedError()


from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit
