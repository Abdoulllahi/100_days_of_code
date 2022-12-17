'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-04 23:02:11
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-04 23:11:21
 # @ Description:
 '''
 
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

### Encryption ###
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
# and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt
# a message.


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         new_letter = alphabet[(alphabet.index(letter) + shift_amount) % 26]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

### Decryption ###
# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
# amount and print the decrypted text.
# e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND*
# decrypt a message.
# def decrypt(cipher_text, shift_amount):
#     decrypted_text = ""
#     for letter in cipher_text:
#         old_letter = alphabet[(alphabet.index(letter) - shift_amount) % 26]
#         decrypted_text += old_letter
#     print(f"The decoded text is: {decrypted_text}")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Bad entry")

### Caesar ###
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


### User experience and improvements
#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            final_letter = alphabet[(alphabet.index(letter) + shift_amount) % 26]
        else:
            final_letter = letter
        final_text += final_letter
    print(f"The {cipher_direction}d text is : {final_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)