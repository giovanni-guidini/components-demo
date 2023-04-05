from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MenuContext:
    loop: bool = True
    parent: object = None
    name: str = ""


class MenuInterface:
    menu_options_index: Dict[str, str] = {}
    _context: MenuContext = MenuContext()

    def __init__(self, *, parent=None, name="") -> None:
        self._context.loop = True
        self._context.parent = parent
        self._context.name = name

    @property
    def loop(self):
        return self._context.loop

    @property
    def parent(self):
        return self._context.parent

    @property
    def name(self):
        return self._context.name

    def set_loop(self, update_value: bool):
        self._context.loop = update_value

    @property
    def menu_options(self) -> List[str]:
        if self.menu_options_index == {}:
            return ["No options yet"]

        return [f"{key}. {value}" for key, value in self.menu_options_index.items()]

    def run(self, *args, **kwargs):
        raise NotImplementedError()
