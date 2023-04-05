from core import MenuContext, MenuInterface


class TestMenuInterface(object):
    def test_init(self):
        menu_interface = MenuInterface()
        assert menu_interface._context == MenuContext()
        assert menu_interface.loop == True
        assert menu_interface.parent == None

    def test_set_loop(self):
        menu_interface = MenuInterface()
        assert menu_interface.loop == True
        menu_interface.set_loop(False)
        assert menu_interface.loop == False

    def test_menu_options(self):
        menu_interface = MenuInterface()
        assert menu_interface.menu_options == ["No options yet"]
        menu_interface.menu_options_index = {
            "a": "avada kedavra",
            "b": "babling bumbling band of baboons",
            "c": "complete arse ronald weasley",
        }
        assert menu_interface.menu_options == [
            "a. avada kedavra",
            "b. babling bumbling band of baboons",
            "c. complete arse ronald weasley",
        ]
