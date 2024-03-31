from Scripts.BlackJack import BlackJack

while True:
    blackjack = BlackJack()
    blackjack.game_loop()
    player_input = bool(input("\nDo you wish to play again?"))
    if not player_input: break