from random_words import RandomWords

class Hangman:
    def __init__(self, min_letter_count):
        self.random_word = RandomWords().random_word(min_letter_count=min_letter_count)
        self.guessed_chars = []
        self.wrong_guesses = 0
        self.print_hangman()
        print(self.return_word_filled_in())

    def game_loop(self):
        while True:
            user_guess = self.get_user_guess()
            self.update_guessed_chars(user_guess)
            if self.check_game_over():
                break
            self.print_game_status()

    def get_user_guess(self):
        while True:
            user_guess = input("What is your next guess: ").strip()
            if len(user_guess) != 1:
                print("You must enter a single character!")
            else:
                return user_guess

    def update_guessed_chars(self, user_guess):
        self.guessed_chars.append(user_guess)
        if user_guess not in self.random_word:
            self.wrong_guesses += 1

    def check_game_over(self):
        if self.wrong_guesses >= 6:
            self.print_hangman()
            print("You have lost the game!!!!")
            return True
        elif all(char in self.guessed_chars for char in self.random_word):
            self.print_hangman()
            print("You have won the game!!!!")
            return True
        return False

    def return_word_filled_in(self):
        return ' '.join(char if char in self.guessed_chars else '_' for char in self.random_word)

    def print_hangman(self):
        hangman_parts = [
            "  +---+  ",
            "  |   |  ",
            "  O   |  " if self.wrong_guesses >= 1 else "      |  ",
            " /|\\  |  " if self.wrong_guesses >= 4 else (" /|   |  " if self.wrong_guesses == 3 else "      |  "),
            " / \\  |  " if self.wrong_guesses >= 6 else (" /    |  " if self.wrong_guesses == 5 else "      |  "),
            "==========="
        ]
        for line in hangman_parts:
            print(line)

    def print_game_status(self):
        self.print_hangman()
        print(self.return_word_filled_in())