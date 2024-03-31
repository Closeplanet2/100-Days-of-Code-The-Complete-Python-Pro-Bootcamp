from Scripts.CustomTurtle import CustomTurtle, goto_single_turtle, move_single_turtles_forward
from Scripts.Food import Food
from Scripts.Scoreboard import Scoreboard
import time
import random

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_SIZE = 3
CELLS_X = 30
CELLS_Y = 30
FOOD_BOUNDARY = 50
FOOD_SCORE = 1
LOOSE_BOUNDARY = 30
STARTING_Y = 0

class SnakeGame:
    def __init__(self, game_height=600, game_width=600):
        self.game_height = game_height
        self.game_width = game_width
        self.food = Food(self.return_new_food_position())
        self.scoreboard = Scoreboard(0, 0 + int(game_height / 2.5))
        self.custom_turtle = CustomTurtle()
        self.custom_turtle.add_on_key(func=self.Up, key="Up")
        self.custom_turtle.add_on_key(func=self.Down, key="Down")
        self.custom_turtle.add_on_key(func=self.Left, key="Left")
        self.custom_turtle.add_on_key(func=self.Right, key="Right")

    def cell_size_x(self):
        return int(self.game_width / CELLS_X)

    def cell_size_y(self):
        return int(self.game_height / CELLS_Y)

    def return_snake_head(self):
        return self.custom_turtle.stored_turtles[0]

    def return_snake_tail(self):
        return self.custom_turtle.stored_turtles[len(self.custom_turtle.stored_turtles) - 1]

    def return_new_food_position(self):
        food_width = int((self.game_width - FOOD_BOUNDARY) / 2)
        food_height = int((self.game_height - FOOD_BOUNDARY) / 2)
        food_x = random.randint(-food_width, food_width)
        food_y = random.randint(-food_height, food_height)
        return [food_x, food_y]

    def game_start(self):
        for turtle in self.custom_turtle.stored_turtles: turtle.goto(self.game_height + 1000, self.game_width + 1000)
        self.custom_turtle.stored_turtles.clear()
        for i in range(0, STARTING_SIZE, 1):
            x = 0 - i * self.cell_size_x()
            self.custom_turtle.create_turtle(x=x, y=STARTING_Y, penup=True)
        self.custom_turtle.start_screen(title="The Snake Game!", width=self.game_width, height=self.game_height)
        self.custom_turtle.update_screen()

    def move_snake(self):
        self.custom_turtle.update_screen()
        time.sleep(0.1)
        for i in range(len(self.custom_turtle.stored_turtles) - 1, 0, -1):
            new_x = self.custom_turtle.stored_turtles[i - 1].xcor()
            new_y = self.custom_turtle.stored_turtles[i - 1].ycor()
            goto_single_turtle(self.custom_turtle.stored_turtles[i], new_x, new_y)
        move_single_turtles_forward(self.return_snake_head(), self.cell_size_x())

        snake_head = self.return_snake_head()
        snake_tail = self.return_snake_tail()
        if snake_head.distance(self.food) < self.cell_size_x() - 5:
            self.food.update_position(self.return_new_food_position())
            self.scoreboard.add_score(FOOD_SCORE)
            self.custom_turtle.create_turtle(x=snake_tail.xcor(), y=snake_tail.ycor(), penup=True)

        game_loose_width = int((self.game_width - LOOSE_BOUNDARY) / 2)
        game_loose_height = int((self.game_height - LOOSE_BOUNDARY) / 2)
        if snake_head.xcor() > game_loose_width or snake_head.xcor() < -game_loose_width or snake_head.ycor() > game_loose_height or snake_head.ycor() < -game_loose_height:
            self.scoreboard.reset_scoreboard()
            self.game_start()
        if len(self.custom_turtle.return_colliding_turtles(snake_head, self.cell_size_x() - 5)) > 0:
            self.scoreboard.reset_scoreboard()
            self.game_start()

    def Up(self):
        if self.return_snake_head().heading() != DOWN:
            self.return_snake_head().setheading(UP)

    def Down(self):
        if self.return_snake_head().heading() != UP:
            self.return_snake_head().setheading(DOWN)

    def Left(self):
        if self.return_snake_head().heading() != RIGHT:
            self.return_snake_head().setheading(LEFT)

    def Right(self):
        if self.return_snake_head().heading() != LEFT:
            self.return_snake_head().setheading(RIGHT)

    def game_loop(self):
        self.game_start()
        while True:
            self.move_snake()