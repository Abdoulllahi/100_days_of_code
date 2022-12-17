#TODO: Create a new class called Question that will have a __init__ method with two attributes: text and answer

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

quest_1 = Question("quest0", "ans")
print(quest_1.answer)