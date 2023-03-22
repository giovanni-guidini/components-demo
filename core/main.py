from core.helpers import get_emotion_class, get_fruit_class
from core.input import parse_input


class MainMenu(object):
    main_menu_message = ["What are you interested in?", "1. Fruits", "2. Emotions"]

    def __init__(self) -> None:
        self.emotion_class = get_emotion_class()
        self.fruit_class = get_fruit_class()

    def run(self, *args, **kwargs):
        loop = True
        while loop:
            print("Welcome to the Gallery!\n")
            print("\n".join(self.main_menu_message))
            menu_choice = parse_input(
                "What are you interested in seeing?",
                valid_input=[1, 2],
                pre_process_input=int,
                error_message="Invalid choice.\n" + "\n".join(self.main_menu_message),
            )
            print(f"You selected {menu_choice}")
            loop = False
