from Scripts.DataTrends import return_random_index
from Scripts.PlayerInput import string_input

class HigherLowerGame:
    def __init__(self, loop_once=False):
        self.loop_once = loop_once
        self.total_score = 0
        self.topicA = None
        self.topicB = None

    def start_new_game(self):
        self.total_score = 0
        print("Picking topic A.....")
        self.topicB = None
        self.topicA = return_random_index()
        self.pick_next_random()

    def pick_next_random(self):
        print("Picking next topic B.....")
        if not self.topicB is None:
            self.topicA = self.topicB
            self.topicB = None

        random_topic = return_random_index()
        while self.topicA[0] == random_topic[0]:
            random_topic = return_random_index()
        self.topicB = random_topic

    def game_loop(self):
        self.start_new_game()
        while True:
            print(f"Compare A: {self.topicA[0]}! Against B: {self.topicB[0]}!")
            user_input = string_input("Who has more followers? Type 'A' or 'B': ", lower=True, correct_values=["a", "b"])

            if user_input == "a" and self.topicA[1] >= self.topicB[1]:
                print(f"Well done! {self.topicA[0]} has {self.topicA[1]} whilst {self.topicB[0]} only has {self.topicB[1]}")
                self.total_score += 1
                self.pick_next_random()
                continue
            elif user_input == "b" and self.topicB[1] >= self.topicA[1]:
                print(f"Well done! {self.topicB[0]} has {self.topicB[1]} whilst {self.topicA[0]} only has {self.topicA[1]}")
                self.total_score += 1
                self.pick_next_random()
                continue
            else:
                print(f"You have guessed wrong! {self.topicA[0]} has {self.topicA[1]} whilst {self.topicB[0]} has {self.topicB[1]}")
                print(f"your total score is {self.total_score}")
                if self.loop_once:
                    return
                self.start_new_game()