
from fruits import FruitInterface


class AsciiFruit(FruitInterface):
    def banana(self):
        return "     _      \n   _ \\'-_,# \n  _\\'--','`|\n  \\`---`  / \n   `----'`  \n"

    def apple(self) -> str:
        return "  ,--./,-.  \n / #      \\ \n|          |\n \\        / \n  `._,._,'  \n"

    def grape(self) -> str:
        return "  \\   \n ()() \n()()()\n ()() \n  ()  \n"
    
    def cherry(self) -> str:
        return """\n   __.--~~.,-.__\n   `~-._.-(`-.__`-.\n           \    `~~`\n      .--./ \\\n     /#   \  \.--.\n     \    /  /#   \\\n      '--'   \    /\n              '--'\n"""












