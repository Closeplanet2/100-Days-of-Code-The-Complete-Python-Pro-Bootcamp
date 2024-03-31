from Scripts.QuizQuestion import QuizQuestion
from Scripts.PlayerInput import string_input

class QuizGame:
    def __init__(self, loop_once=False):
        self.loop_once = loop_once
        self.stored_questions = []
        self.current_index = 0
        self.current_score = 0

    def add_question(self, prompt_message, list_of_answers, correct_answer):
        self.stored_questions.append(QuizQuestion(prompt_message, list_of_answers, correct_answer))

    def reset_game(self):
        self.current_index = 0
        self.current_score = 0

    def game_loop(self):
        if not self.stored_questions:
            return
        self.reset_game()
        while True:
            current_question = self.stored_questions[self.current_index]
            question_prompt = current_question.return_quiz_prompt(self.current_index)
            user_input = string_input(question_prompt, correct_values=["True", "False"])

            if user_input == current_question.correct_answer:
                self.current_score += 1
                print(f"You got it right!\nThe correct answer was: {current_question.correct_answer}.\nYour current score is: {self.current_score}/{len(self.stored_questions)}")
            else:
                print(f"That's wrong.\nThe correct answer was: {current_question.correct_answer}.\nYour current score is: {self.current_score}/{len(self.stored_questions)}")

            self.current_index += 1
            if self.current_index >= len(self.stored_questions):
                print(f"You have finished the quiz! Your final score is: {self.current_score}/{len(self.stored_questions)}")
                if self.loop_once:
                    return
                else:
                    self.reset_game()
                    print("\n\n\n\n\n\n")