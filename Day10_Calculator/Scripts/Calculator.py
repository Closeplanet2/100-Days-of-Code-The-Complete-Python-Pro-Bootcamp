from Scripts.PlayerInput import float_input, string_input

class Calculator:
    def __init__(self, loop_once=False):
        self.loop_once = loop_once
        self.current_value = None

    def game_loop(self):
        while True:
            first_number = self.current_value if self.current_value is not None and string_input(
                f"Do you want to use the stored current value of {self.current_value} as the first number?", correct_values=["y", "n"]) == "y" else float_input("What's the first number?: ")

            operation = string_input("Pick an operation (+, -, *, /): ", correct_values=["+", "-", "*", "/"])
            second_number = float_input("What's the next number?: ")
            calculation = f"{first_number} {operation} {second_number}"
            answer = eval(calculation)
            print(f"{calculation} = {answer}")

            if self.loop_once:
                return

            self.current_value = answer
