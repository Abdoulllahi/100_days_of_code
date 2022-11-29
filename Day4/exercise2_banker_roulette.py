# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_index = random.randint(0, len(names) - 1)
loser = names[name_index]
print(loser + " is going to pay the meal today!")