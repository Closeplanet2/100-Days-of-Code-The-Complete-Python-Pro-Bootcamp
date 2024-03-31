from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("#FFFFFF")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.write_score()
        self.increase_score(0)

    def increase_score(self, amount):
        self.score += amount
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))