from Scripts.Hangman import Hangman

while True:
    hangman = Hangman(3)
    hangman.game_loop()
    x = bool(input("Do you wish to play again?"))
    if not x: break
