

class FruitInterface:
    FRUITS_AVAILABLE = [
        "banana",
        "apple",
        "cherry",
        "grape",
        "coconut",
        "avocado",
        "kiwi"
    ]

    def banana(self) -> str:
        raise NotImplementedError()

    def apple(self) -> str:
        raise NotImplementedError()
    
    def cherry(self) -> str:
        raise NotImplementedError()

    def grape(self) -> str:
        raise NotImplementedError()
    
    def coconut(self) -> str:
        raise NotImplementedError()
    
    def avocado(self) -> str:
        raise NotImplementedError()
    
    def kiwi(self) -> str:
        raise NotImplementedError()
