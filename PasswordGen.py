import random
import time
import string
import os

print("Please enter the digits for your password:")
digits = int(input())
print("Please select all of the items in your password:")
cap = input("Capitalized letter?[1]Yes/[2]No\n")
low = input("Lower-cased letter?[1]Yes/[2]No\n")
num = input("Numbers?[1]Yes/[2]No\n")
char = input("Special Characters?[1]Yes/[2]No\n")
password = []

for i in range (digits):
    if low == "1":
        lower_upper_alphabet = string.ascii_letters
        random_low = (random.choice(lower_upper_alphabet)).lower()
    if cap == "1":
        lower_upper_alphabet = string.ascii_letters
        random_high = (random.choice(lower_upper_alphabet)).capitalize()
    if num == "1":
        random_num = random.randint(0, 9)
    if char == "1":
        random_char = random.choice("!@#$%^&*()_")
    choice = random.randint(1, 4)
    if choice == 1 and low == "1":
        password.append(random_low)
    elif choice == 2 and cap == "1":
        password.append(random_high)
    elif choice == 3 and num == "1":
        password.append(random_num)
    elif choice == 4 and char == "1":
        password.append(random_char)
bl = ""
for x in password:
    bl += str(x)
print(bl)