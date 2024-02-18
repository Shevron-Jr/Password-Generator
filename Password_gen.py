#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Shevron Password Generator!")
nr_letters= int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))

"""
#Easy Level Generator
password = " "
for p in range(1, nr_letters + 1):
  password += random.choice(letters)
for p in range(1, nr_numbers + 1):
  password += random.choice(numbers)
for p in range(1, nr_symbols + 1):
  password += random.choice(symbols)

print(f"Your password is: {password}")
"""


#Hard Level
password = []

for p in range(1, nr_letters + 1):
  password += random.choice(letters)
for p in range(1, nr_numbers + 1):
  password += random.choice(numbers)
for p in range(1, nr_symbols + 1):
  password += random.choice(symbols)

random.shuffle(password)
print(password)

final_password = ""
for char in password:
  final_password += char

print(f"Your password is: {final_password}")