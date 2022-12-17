print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, 15?"))
people = float(input("How many people to split the bill?"))

bill_per_person = round(((bill * (1 + percentage / 100)) / people), 2)
print(f"Each person should pay: ${bill_per_person}")