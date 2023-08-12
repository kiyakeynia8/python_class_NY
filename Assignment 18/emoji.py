import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Face(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        # Draw the face
        x = 300
        y = 300
        radius = 180
        arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

        # Draw the right eye
        x = 370
        y = 350
        radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

        # Draw the left eye
        x = 230
        y = 350
        radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

        x = 300
        y = 250
        width = 120
        height = 5
        start_angle = 190
        end_angle = 350
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

        x = 250
        y = 400
        width = 120
        height = 2
        start_angle = 100
        end_angle = 250
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

        x = 410
        y = 400
        width = 150
        height = 2
        start_angle = 100
        end_angle = 250
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

def main():
    game = Face(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

if __name__ == "__main__":
    main()