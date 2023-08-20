import random
import arcade
from Fruits import Apple,Pear,Rock
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="kiya game")
        arcade.set_background_color(arcade.color.KHAKI)
        
        self.snake = Snake(self)
        self.apple_food = Apple(self.width,self.height)
        self.rock = Rock(self.width,self.height)
        self.pear_food = Pear(self.width,self.height)

        self.a = 1
        self.s = "g"

    def on_draw(self):
        arcade.start_render()

        if self.s == "g":
            self.snake.draw()
            self.apple_food.draw()    
            self.rock.draw()
            self.pear_food.draw()
            arcade.draw_line(2, 2, 0, 500, arcade.color.WHITE, 5)
            arcade.draw_line(2, 2, 500, 0, arcade.color.WHITE, 5)
            arcade.draw_line(498, 498, 500, 0, arcade.color.WHITE, 5)
            arcade.draw_line(498, 498, 0, 500, arcade.color.WHITE, 5)

        elif self.s == "o":
            arcade.draw_text("Game Over", self.width/3, self.height/2, font_size=25)

        arcade.finish_render()

    def on_update(self, delta_time):
        if self.s == "g":
            self.snake.move()
            
            if self.snake.center_x < 2 or self.snake.center_y < 2 or self.snake.center_x > 498 or self.snake.center_y > 498:
                self.s = "o"

            for part in self.snake.body[1:]:
                if self.snake.body[0] == part:
                    self.s = "o"

            if arcade.check_for_collision(self.snake, self.apple_food):
                del self.apple_food
                self.snake.apple_eat()
                self.apple_food = Apple(self.width,self.height)

            elif arcade.check_for_collision(self.snake, self.rock):
                if len(self.snake.body) == 1 or len(self.snake.body) == 0:
                    self.s = "o"

                del self.rock
                self.snake.rock_eat()
                self.rock = Rock(self.width,self.height)

            elif arcade.check_for_collision(self.snake, self.pear_food):
                del self.pear_food
                self.snake.pear_eat()
                self.pear_food = Pear(self.width,self.height)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        if symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()