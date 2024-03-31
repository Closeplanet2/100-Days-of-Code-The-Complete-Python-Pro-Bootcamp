import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

class RockPaperScissors:
    def __init__(self, one_game=False):
        self.one_game = one_game
        print("Let's Play Rock, Paper, Scissors!")

    def game_loop(self):
        while True:
            user_input = self.get_user_input()
            computer_input = random.randint(0, 2)

            print("Your Choice:")
            self.print_symbol(user_input)
            print("PC Choice:")
            self.print_symbol(computer_input)

            if user_input == computer_input:
                print("It's a Tie!")
            elif (user_input - computer_input) % 3 == 1:
                print("You Win!")
            else:
                print("You Lose!")

            if self.one_game:
                break

    def get_user_input(self):
        while True:
            user_input = input("What do you choose? 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").lower()
            if user_input in ['r', 'p', 's']:
                return {'r': 0, 'p': 1, 's': 2}[user_input]
            else:
                print("Invalid input!")

    def print_symbol(self, value):
        symbols = [rock, paper, scissors]
        print(symbols[value])
