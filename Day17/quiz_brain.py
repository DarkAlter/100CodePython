class BrainQuiz:
       
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if(len(self.question_list) > self.question_number):
            return True
        else:
            return False

    def next(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {cur_question.text} (True / False) :")
        self.checkAnswer(answer, cur_question.answer)

    def checkAnswer(self, answer, trueAnswer):
        if answer.lower() == trueAnswer.lower():
            print("You Right")
            self.score +=1
            print(f"Your score {self.score}/{self.question_number}")
        else:
            print("You are wrong")
            print(f"the correct answer is {trueAnswer}")
            print(f"Your score {self.score}/{self.question_number}")
    def finalScore(self):
        print(f"Your Final score {self.score}/{self.question_number}")
