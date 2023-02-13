

from fruits.ascii import AsciiFruit
from fruits.emoji import EmojiFruit


class TestAsciiFruits():
    fruit_class = AsciiFruit()
    def test_banana(self):
        assert self.fruit_class.banana() == """     _      
   _ \\'-_,# 
  _\\'--','`|
  \\`---`  / 
   `----'`  
"""

    def test_grape(self):
        assert self.fruit_class.grape() == """  \\   
 ()() 
()()()
 ()() 
  ()  
"""

    def test_cherry(self):
        assert self.fruit_class.cherry() == """
   __.--~~.,-.__
   `~-._.-(`-.__`-.
           \\    `~~`
      .--./ \\
     /#   \\  \\.--.
     \\    /  /#   \\
      '--'   \\    /
              '--'
"""

class TestEmojiFruits():
    fruit_class = EmojiFruit()
    def test_banana(self):
        assert self.fruit_class.banana() == "🍌"
    
    def test_grape(self):
        assert self.fruit_class.grape() == "🍇"

    def test_apple(self):
        assert self.fruit_class.apple() == "🍎"

    def test_cherry(self):
        assert self.fruit_class.cherry() == "🍒"
