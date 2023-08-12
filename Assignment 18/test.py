import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

class MyGame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def update(self):
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    game.run()

if __name__ == "__main__":
    main()