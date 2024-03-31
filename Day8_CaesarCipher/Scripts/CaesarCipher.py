import string
from Scripts.Array import wrap_array
from Scripts.PlayerInput import get_user_input, get_user_int_input

numbers = [str(num) for num in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?', ' ']
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
letters = letters_lower + letters_upper + numbers + symbols

class CaesarCipher:
    def __init__(self, loop_once=False):
        self.loop_once = loop_once

    def game_loop(self):
        while True:
            encode_type = get_user_input("Type 'encode' to encrypt, type 'decode' to decrypt: ", correct_values=["encode", "decode"])
            shift_amount = get_user_int_input("Shift Amount: ")

            new_player_message = ""
            for char in get_user_input("Type your message: "):
                new_char = wrap_array(letters, char, shift_amount if encode_type == "encode" else -shift_amount)
                new_player_message += new_char

            print(f"Your new message: {new_player_message}")
            if self.loop_once:
                return
