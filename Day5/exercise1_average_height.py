'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-11-29 11:19:29
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-11-29 11:28:00
 # @ Description:
 '''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
heights = 0
for height in student_heights:
    heights += height
print(round(heights / len(student_heights)))
