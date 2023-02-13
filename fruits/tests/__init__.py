
from fruits import FruitInterface


def test_interface_has_attributes():
    interface = FruitInterface()
    list_of_available_fruits = interface.FRUITS_AVAILABLE
    for fruit in list_of_available_fruits:
        assert hasattr(interface, fruit) and callable(getattr(interface, fruit))