from question_model import Question
from data import question_data
from random import choice
from quiz_brain import BrainQuiz
question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

score = 0
total = len(question_bank)



quiz = BrainQuiz(question_bank)
while quiz.still_has_question():
    quiz.next()
quiz.finalScore()


    
    


