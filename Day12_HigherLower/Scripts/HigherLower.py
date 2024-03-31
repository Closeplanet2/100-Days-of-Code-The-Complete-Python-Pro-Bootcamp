import random
import pyautogui
from Scripts.PlayerInput import string_input, int_input


class HigherLower:
    def __init__(self, loop_once=False, min_number=1, max_number=100):
        self.loop_once = loop_once
        self.min_number = min_number
        self.max_number = max_number

    def start_new_game(self):
        self.random_number = random.randint(self.min_number, self.max_number)
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}!")
        self.guesses_left = 10 if string_input("Choose a difficulty. Type 'easy' or 'hard': ",
                                               correct_values=["easy", "hard"]) == "easy" else 5

    def game_loop(self):
        while True:
            self.start_new_game()
            while self.guesses_left > 0:
                print(f"You have {self.guesses_left} attempts to guess the number.")
                user_guess = int_input("Make a guess: ")

                if user_guess == self.random_number:
                    print(f"You have won the game! The correct guess was {self.random_number}!")
                    break
                elif user_guess > self.random_number:
                    print("The number is too high. Try again!")
                else:
                    print("The number is too low. Try again!")
                self.guesses_left -= 1
            else:
                print(f"You have lost the game! The correct guess was {self.random_number}!")

            if not self.loop_once:
                pyautogui.hotkey('ctrl', 'l')
                continue
            else:
                return
