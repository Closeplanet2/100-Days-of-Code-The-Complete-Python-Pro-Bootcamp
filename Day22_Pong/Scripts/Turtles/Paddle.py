from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y, move_amount):
        super().__init__()
        self.move_amount = move_amount
        self.shape("square")
        self.color("#ffffff")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def set_movement(self, up_key, down_key, custom_turtle):
        custom_turtle.add_onkeypress(key=up_key, func=self.paddle_up)
        custom_turtle.add_onkeypress(key=down_key, func=self.paddle_down)

    def paddle_up(self):
        new_y = self.ycor() + self.move_amount
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - self.move_amount
        self.goto(self.xcor(), new_y)