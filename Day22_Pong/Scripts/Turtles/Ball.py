from turtle import Turtle

class Ball(Turtle):
    def __init__(self, x, y, move_amount, speed_increase_factor):
        super().__init__()
        self.starting_speed = move_amount
        self.x_move = move_amount
        self.y_move = move_amount
        self.speed_increase_factor = speed_increase_factor
        self.color("#ffffff")
        self.shape("circle")
        self.penup()
        self.goto(x, y)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def check_paddle_collisions(self, game_height, game_width, wall_boundary, paddle_check, paddle_a, paddle_b):
        half_height = (game_height / 2) - wall_boundary
        if self.ycor() > half_height or self.ycor() < -half_height:
            self.y_move *= -1

        half_width = (game_width / 2) - paddle_check
        if self.distance(paddle_a) < 50 and self.xcor() > half_width:
            self.x_move *= -1
            self.x_move *= self.speed_increase_factor
            self.y_move *= self.speed_increase_factor
        if self.distance(paddle_b) < 50 and self.xcor() < -half_width:
            self.x_move *= -1
            self.x_move *= self.speed_increase_factor
            self.y_move *= self.speed_increase_factor

    def check_paddle_missed(self, game_width, wall_boundary):
        half_height = (game_width / 2) - wall_boundary
        if self.xcor() > half_height:
            self.reset_ball()
            return 1
        elif self.xcor() < -half_height:
            self.reset_ball()
            return 2
        return 0

    def reset_ball(self):
        self.x_move = self.starting_speed
        self.y_move = self.starting_speed
        self.goto(0, 0)
        self.x_move *= -1