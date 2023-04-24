from core import MenuContext, MenuInterface


class TestMenuInterface(object):
    def test_init(self):
        menu_interface = MenuInterface()
        assert menu_interface._context == MenuContext()
        assert menu_interface.loop == True
        assert menu_interface.parent == None
        assert menu_interface.name == ""
