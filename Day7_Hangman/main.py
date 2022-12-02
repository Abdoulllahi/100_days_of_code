'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-02 08:20:04
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-02 08:38:47
 # @ Description: Hangman challenge
    we have chosen to organize the game in levels:
    easy level: 1 to 7 words
    intermediate level: 8 to 15 words
    difficult level: more than 15 words
'''

import json
import random

# @ This script was created to add words length as a value in the initial json file
# with open("Day7_Hangman/words_english.json", "r+") as file:
#     data = json.load(file)
#     for word in data:
#         data[word] = len(word)
#     file.seek(0)
#     json.dump(data, file, indent=4)
#     file.truncate()

level = input("Please choose a level: easy, medium or hard\n")

with open("Day7_Hangman/words_english.json", "r") as file:
    data = json.load(file)
    if (level == "easy"):
        words = [word for word in data.keys() if data[word] in range(1, 8)]
    elif (level == "medium"):
        words = [word for word in data.keys() if data[word] in range(8, 15)]
    elif (level == "hard"):
        words = [word for word in data.keys() if data[word] > 15]
    file.close()
random_word = random.choice(words)
guess = input("Guess a letter: ").lower()

for letter in random_word:
    if (letter == guess):
        print("Right")
    else:
        print("Wrong")
print(random_word)