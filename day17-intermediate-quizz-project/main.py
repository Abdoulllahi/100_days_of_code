from data import question_data
from question_model import Question


#TODO: asking the question

#TODO: Check if the question is correct

#TODO: Check if we are at the end of the quiz

question_bank = [Question(text=question["text"], answer=question["answer"]) for question in question_data]
