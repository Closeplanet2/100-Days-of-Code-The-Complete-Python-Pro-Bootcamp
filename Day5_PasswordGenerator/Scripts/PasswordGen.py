import string
import random

numbers = [str(num) for num in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
letters = letters_lower + letters_upper

def get_user_int_input(prompt_text, default_int=None):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            if default_int is not None:
                return default_int
            print("Invalid number!")

class PasswordGen:
    def __init__(self, one_password=True):
        self.one_password = one_password

    def generate_password(self):
        num_letters = get_user_int_input("How many letters would you like in your password?\n")
        num_symbols = get_user_int_input("How many symbols should be in your password?\n")
        num_numbers = get_user_int_input("How many numbers should be in your password?\n")

        password_letters = [random.choice(letters) for _ in range(num_letters)]
        password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

        password = password_letters + password_symbols + password_numbers
        random.shuffle(password)

        return ''.join(password)

    def game_loop(self):
        while True:
            gen_password = self.generate_password()
            print(f"Your password is: {gen_password}\n\n\n\n\n\n")
            if self.one_password:
                return