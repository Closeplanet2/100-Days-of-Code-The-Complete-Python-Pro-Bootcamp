
class QuizQuestion:
    def __init__(self, prompt_message, list_of_answers, correct_answer):
        self.prompt_message = prompt_message
        self.list_of_answers = list_of_answers
        self.correct_answer = correct_answer

    def return_quiz_prompt(self, index):
        return f"Q.{index + 1}: {self.prompt_message} {self.list_of_answers}?: "