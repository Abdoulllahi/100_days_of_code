# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
tens = name.count("t") + name.count("r") + name.count("u") + name.count("e")
units = name.count("l") + name.count("o") + name.count("v") + name.count("e")
score = tens * 10 + units
if(score > 90 or score < 10):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score < 50 and score > 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")