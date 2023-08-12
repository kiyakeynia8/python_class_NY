import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sunny Forest")
arcade.set_background_color(arcade.color.BLUE_YONDER)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.MSU_GREEN)

arcade.draw_circle_filled(90, SCREEN_HEIGHT-85, 75, arcade.color.SUNRAY)

def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 15, 75, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y + 20, 35, arcade.color.DARK_GREEN)

a = SCREEN_HEIGHT / 8
b = [i*a for i in range(8)]
print(b)

for i in range(1,8):
    draw_tree(random.randrange(b[i-1]+30, b[i]-30), random.randrange(SCREEN_HEIGHT / 3))

arcade.finish_render()
arcade.run()