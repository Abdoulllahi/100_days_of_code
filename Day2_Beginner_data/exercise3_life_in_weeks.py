# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_age = 90- int(age)
months = remaining_age * 12
weeks = remaining_age * 52
days = remaining_age * 365
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)