'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-17 13:53:45
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-20 15:45:53
 # @ Description:
 '''

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        
        
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
            