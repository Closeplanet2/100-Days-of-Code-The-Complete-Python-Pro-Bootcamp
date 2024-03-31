from turtle import Turtle, Screen

class EtchASketch:
    def __init__(self, sensitivity_x=10, sensitivity_rotate=10):
        self.sensitivity_x = sensitivity_x
        self.sensitivity_rotate = sensitivity_rotate
        self.c_turtle = Turtle()
        self.c_screen = Screen()

    def start_game(self):
        self.c_screen.listen()
        self.c_screen.onkey(key="w", fun=self.move_forwards)
        self.c_screen.onkey(key="s", fun=self.move_backwards)
        self.c_screen.onkey(key="a", fun=self.rotate_anti_clockwise)
        self.c_screen.onkey(key="d", fun=self.rotate_clockwise)
        self.c_screen.exitonclick()

    def move_forwards(self):
        self.c_turtle.forward(self.sensitivity_x)

    def move_backwards(self):
        self.c_turtle.backward(self.sensitivity_x)

    def rotate_clockwise(self):
        self.c_turtle.right(self.sensitivity_rotate)

    def rotate_anti_clockwise(self):
        self.c_turtle.left(self.sensitivity_rotate)

