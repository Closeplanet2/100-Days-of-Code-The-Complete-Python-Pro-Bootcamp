from Scripts.QuizGame import QuizGame

quizGame = QuizGame()
quizGame.add_question("A slug's blood is green", ["True, False"], "True")
quizGame.add_question("The loudest animal is the African Elephant", ["True, False"], "False")
quizGame.add_question("Approximately one quarter of human bones are in the feet", ["True, False"], "True")
quizGame.add_question("The total surface are of a human lungs is the size of a football pitch", ["True, False"], "True")
quizGame.game_loop()