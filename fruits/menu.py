import inspect

from core import MenuInterface
from core.input import parse_input
from fruits import FruitInterface


class FruitsMenu(MenuInterface):
    def __init__(self, *, parent: MenuInterface, fruit_obj: FruitInterface) -> None:
        super().__init__(parent=parent, name="Fruits")
        self.fruit_obj = fruit_obj
        self.menu_options_index = self._generate_menu_option_index()

    def _generate_menu_option_index(self):
        if not self.fruit_obj:
            return {}
        my_defined_methods = sorted(
            [
                member[0]
                for member in inspect.getmembers(self.fruit_obj)
                if not member[0].startswith("__")
            ]
        )
        return {str(idx): value for idx, value in enumerate(my_defined_methods)}

    def run(self, *args, **kwargs):
        while self.loop:
            print("Welcome to the Fruits exhibit!\n")
            print("\n".join(["Available fruits:"] + self.menu_options))
            menu_choice = parse_input(
                "What are you interested in seeing? ",
                valid_input=self.menu_options_index.keys(),
                error_message="Invalid choice.\n"
                + "\n".join(["Available fruits:"] + self.menu_options),
            )
            fruit_selected = self.menu_options_index[menu_choice]
            fruit_method = getattr(self.fruit_obj, fruit_selected)
            print("\n")
            print(fruit_method())
            self.set_loop(False)
