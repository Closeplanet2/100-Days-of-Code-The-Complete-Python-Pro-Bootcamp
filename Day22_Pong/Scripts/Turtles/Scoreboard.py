from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#ffffff")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.increase_l_score(0)
        self.increase_r_score(0)

    def increase_l_score(self, amount=1):
        self.l_score += amount
        self.update_scoreboard()

    def increase_r_score(self, amount=1):
        self.r_score += amount
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))