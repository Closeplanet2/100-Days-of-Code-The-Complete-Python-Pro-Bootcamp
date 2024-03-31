import random

class BlackJack:
    def __init__(self):
        self.player_hand = []
        self.computer_hand = []
        self.cards_in_deck = []
        self.computer_turn = False
        self.end_game = False
        self.generate_new_deck()
        self.deal_initial_cards()
        print(f"Computer's first card: {self.computer_hand[0]}")

    def generate_new_deck(self):
        self.cards_in_deck = [i for i in range(1, 14) for _ in range(4)]
        random.shuffle(self.cards_in_deck)

    def deal_initial_cards(self):
        self.deal_cards(self.player_hand, create_new_hand=True)
        self.deal_cards(self.computer_hand, create_new_hand=True)

    def deal_cards(self, hand, create_new_hand=False, cards_to_deal=2):
        if create_new_hand:
            hand.clear()
        random_cards = random.sample(self.cards_in_deck, cards_to_deal)
        self.cards_in_deck = [card for card in self.cards_in_deck if card not in random_cards]
        hand.extend(random_cards)
        if hand is self.player_hand:
            print(f"Your Cards: {self.player_hand} [{self.calculate_hand_total(self.player_hand)}]")

    def calculate_hand_total(self, hand):
        total_with_ace = sum(11 if card == 1 else min(card, 10) for card in hand)
        total_without_ace = sum(min(card, 10) for card in hand)
        return total_with_ace if total_with_ace <= 21 else total_without_ace

    def get_user_input(self):
        while True:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input in ['y', 'n']:
                return user_input

    def play_player_turn(self):
        user_input = self.get_user_input()
        if user_input == 'y':
            self.deal_cards(self.player_hand, create_new_hand=False, cards_to_deal=1)
            player_hand_total = self.calculate_hand_total(self.player_hand)
            if player_hand_total > 21:
                print("You have gone above 21!")
                return True
        else:
            self.computer_turn = True
        return False

    def play_computer_turn(self):
        computer_hand_total = self.calculate_hand_total(self.computer_hand)
        if computer_hand_total <= 16:
            self.deal_cards(self.computer_hand, create_new_hand=False, cards_to_deal=1)
        elif 17 <= computer_hand_total <= 21:
            self.end_game = True
        else:
            print("The PC has gone above 21!")
            print(f"Computer hand: {self.computer_hand} [{self.calculate_hand_total(self.computer_hand)}]")
            return True
        return False

    def game_loop(self):
        while True:
            if self.end_game:
                print(f"Your hand: {self.player_hand} [{self.calculate_hand_total(self.player_hand)}]")
                print(f"Computer hand: {self.computer_hand} [{self.calculate_hand_total(self.computer_hand)}]")
                player_hand_total = self.calculate_hand_total(self.player_hand)
                computer_hand_total = self.calculate_hand_total(self.computer_hand)
                if computer_hand_total >= player_hand_total:
                    print("Computer Wins")
                else:
                    print("Player Wins")
                return
            elif self.computer_turn:
                if self.play_computer_turn():
                    return
            else:
                if self.play_player_turn():
                    return
