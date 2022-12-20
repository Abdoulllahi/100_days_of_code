'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-17 13:50:59
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-20 15:42:55
 # @ Description:
 '''

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# TODO: asking the question

# TODO: Check if the question is correct

# TODO: Check if we are at the end of the quiz

question_bank = [Question(text = question["text"], answer = question["answer"])
                 for question in question_data]
quiz = QuizBrain(question_list = question_bank)
quiz.next_question()