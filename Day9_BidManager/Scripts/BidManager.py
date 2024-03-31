from Scripts.PlayerInput import string_input, float_input, bool_input
import pyautogui

def find_highest_bid(bidmap):
    if len(bidmap) == 0: return None
    highest_key = ""
    highest_value = 0
    for key in bidmap:
        if bidmap[key] > highest_value:
            highest_key = key
            highest_value = bidmap[key]
    return highest_key

class BidManager:
    def __init__(self, loop_once=False):
        self.loop_once = loop_once
        self.bidmap = {}

    def game_loop(self):
        while True:
            user_name = string_input("Enter name or 'cancel'? ")
            if not user_name.lower() == "cancel":
                bid_amount = float_input("What's your bid?: £")
                self.bidmap[user_name] = bid_amount
                next_bid = bool_input("Are there any more bidders? ")
                pyautogui.hotkey('ctrl', 'l')
                if next_bid:
                    continue
            highest_key = find_highest_bid(self.bidmap)
            print(f"The winner is {highest_key} with a bid of £{self.bidmap[highest_key]}")
            if self.loop_once:
                return
            else:
                print("\n\n\n\n\n")