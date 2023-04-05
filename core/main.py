from typing import List

from core import MenuInterface
from core.helpers import get_emotion_class, get_fruit_class
from core.input import parse_input


class MainMenu(MenuInterface):
    def __init__(self) -> None:
        super().__init__(parent=None, name="Main Menu")
        self.emotion_class = get_emotion_class()
        self.fruit_class = get_fruit_class()

    menu_options_index = {"1": "Fruits", "2": "Emotions"}

    def run(self, *args, **kwargs):
        while self.loop:
            print("Welcome to the Gallery!\n")
            print("\n".join(["Available expos:"] + self.menu_options))
            menu_choice = parse_input(
                "What are you interested in seeing? ",
                valid_input=self.menu_options_index.keys(),
                error_message="Invalid choice.\n"
                + "\n".join(["Available expos:"] + self.menu_options),
            )
            print(f"You selected the {self.menu_options_index[menu_choice]} expo.")
            self.set_loop(False)
