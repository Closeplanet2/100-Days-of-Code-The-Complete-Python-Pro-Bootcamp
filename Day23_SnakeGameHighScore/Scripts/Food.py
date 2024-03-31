from turtle import Turtle

class Food(Turtle):
    def __init__(self, food_pos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#5FD8FF")
        self.speed("fastest")
        self.update_position(food_pos)

    def update_position(self, food_pos):
        self.goto(food_pos[0], food_pos[1])