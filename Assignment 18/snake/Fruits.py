import arcade
import random

class Apple(arcade.Sprite):
    def __init__ (self,width,height):
        super().__init__("images/pngfind.com-apple-icon-png-56881.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Rock(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("images/pngwing.com.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Pear(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("images/pngfind.com-pear-png-971896.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0