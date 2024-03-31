from Scripts.CustomTurtle import CustomTurtle
from Scripts.Turtles.Paddle import Paddle
from Scripts.Turtles.Ball import Ball
from Scripts.Turtles.Scoreboard import Scoreboard
import time

GAME_SLEEP = 0.1
PADDLE_MOVE_AMOUNT = 30
BALL_MOVE_AMOUNT = 20
PADDLE_OFFSET = 50
WALL_BOUNDARY = 40
PADDLE_CHECK = 80
SPEED_INCREASE_FACTOR = 1.12

class Pong:
    def __init__(self, game_height, game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.custom_turtle = CustomTurtle()

        self.paddle_a = self.custom_turtle.add_turtle(Paddle((game_width / 2) - PADDLE_OFFSET, 0, PADDLE_MOVE_AMOUNT))
        self.paddle_a.set_movement("Up", "Down", self.custom_turtle)
        self.paddle_b = self.custom_turtle.add_turtle(Paddle((-game_width / 2) + PADDLE_OFFSET, 0, PADDLE_MOVE_AMOUNT))
        self.paddle_b.set_movement("w", "s", self.custom_turtle)
        self.ball = self.custom_turtle.add_turtle(Ball(0, 0, BALL_MOVE_AMOUNT, SPEED_INCREASE_FACTOR))
        self.scoreboard = self.custom_turtle.add_turtle(Scoreboard())

    def game_start(self):
        self.custom_turtle.start_screen(title="THE PONG GAME!", width=self.game_width, height=self.game_height)

    def game_loop(self):
        self.game_start()
        while True:
            time.sleep(GAME_SLEEP)
            self.custom_turtle.c_screen.listen()
            self.custom_turtle.update_screen()

            self.ball.move_ball()
            self.ball.check_paddle_collisions(self.game_height, self.game_width, WALL_BOUNDARY, PADDLE_CHECK, self.paddle_a, self.paddle_b)
            game_state = self.ball.check_paddle_missed(self.game_width, WALL_BOUNDARY)

            if game_state == 0:
                continue
            elif game_state == 1:
                self.scoreboard.increase_l_score()
            elif game_state == 2:
                self.scoreboard.increase_r_score()

        self.custom_turtle.c_screen.exitonclick()