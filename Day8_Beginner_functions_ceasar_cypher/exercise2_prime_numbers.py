'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-04 22:47:13
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-04 22:47:18
 # @ Description:
 '''
import math
#Write your code below this line 👇
def prime_checker(number):
    message = "It's a prime number."
    for numbers in range(2, math.ceil(number / 2)):
        if number % numbers != 0:
            continue
        else:
            message = "It's not a prime number."
            break
    print(message)
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
