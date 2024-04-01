from Scripts.CustomTurtle import CustomTurtle
import pandas
import turtle
import time

GAME_SLEEP = 0.1

class USStatesGame:
    def __init__(self):
        self.custom_turtle = CustomTurtle()
        self.data = pandas.read_csv("Data/50_states.csv")
        self.all_states = self.data.state.to_list()

    def game_start(self):
        self.guessed_states = []
        self.custom_turtle.start_screen(title="US States Game!", width=700, height=450)
        self.custom_turtle.c_screen.addshape("Images/blank_states_img.gif")
        turtle.shape("Images/blank_states_img.gif")
        # turtle.onscreenclick(self.get_mouse_click)

    # def get_mouse_click(self, x, y):
    #     print(x, y)

    def test_user_input(self):
        input_title = f"{len(self.guessed_states)} / 50 States Correct"
        input_prompt = "Whats another states name?"

        answer_state = self.custom_turtle.c_screen.textinput(title=input_title, prompt=input_prompt).title()
        if answer_state == "Exit":
            return True
        elif answer_state in self.all_states and answer_state not in self.guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = self.data[self.data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            self.guessed_states.append(state_data.state.item())
            return False

    def game_loop(self):
        self.game_start()
        while True:
            time.sleep(GAME_SLEEP)
            self.custom_turtle.update_screen()

            if self.test_user_input():
                missing_states = []
                for state in self.all_states:
                    if state not in self.guessed_states:
                        missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("Data/States_to_learn.csv")
                break

            if len(self.guessed_states) >= 50:
                print("Win")
                break
