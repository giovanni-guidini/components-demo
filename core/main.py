from typing import List

from core.helpers import get_emotion_class, get_fruit_class
from core.input import parse_input


class MainMenu(object):
    def __init__(self) -> None:
        self.emotion_class = get_emotion_class()
        self.fruit_class = get_fruit_class()

    menu_options_index = {"1": "Fruits", "2": "Emotions"}

    @property
    def _menu_options(self) -> List[str]:
        return [f"{key}.{value}" for key, value in self.menu_options_index.items()]

    def run(self, *args, **kwargs):
        loop = True
        while loop:
            print("Welcome to the Gallery!\n")
            print("\n".join(["Available expos:"] + self._menu_options))
            menu_choice = parse_input(
                "What are you interested in seeing? ",
                valid_input=self.menu_options_index.keys(),
                error_message="Invalid choice.\n"
                + "\n".join(["Available expos:"] + self._menu_options),
            )
            print(f"You selected the {self.menu_options_index[menu_choice]} expo.")
            loop = False
