import colorgram as cg
import turtle as turtle_module
import random

class ImageDrawer:
    def __init__(self, image_path, color_amount=30, number_of_dots=100):
        self.image_path = image_path
        self.color_amount = color_amount
        self.number_of_dots = number_of_dots

        turtle_module.colormode(255)
        self.tim = turtle_module.Turtle()
        self.tim.speed("fastest")
        self.tim.penup()
        self.tim.hideturtle()

        self.rgb_colors = []
        for color in cg.extract(self.image_path, color_amount):
            self.rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    def game_loop(self):
        self.tim.setheading(225)
        self.tim.forward(300)
        self.tim.setheading(0)

        for i in range(1, self.number_of_dots + 1, 1):
            self.tim.dot(20, random.choice(self.rgb_colors))
            self.tim.forward(50)

            if i % 10 == 0:
                self.tim.setheading(90)
                self.tim.forward(50)
                self.tim.setheading(180)
                self.tim.forward(500)
                self.tim.setheading(0)

        screen = turtle_module.Screen()
        screen.exitonclick()

