import random
import os

os.system("title Password Generator")
chars = ''
password = ''

try:
    length = int(input("Length- "))
except:
    print("Invalid or No Length Detected, Defaulting to 10")
    length = 10

print("\nU- Uppercase\nL- Lowercase\nN- Numbers\nS- Symbols")
options = input("Which Options Would You Like? [U, L, N, S]- ")
options = options.lower()

options = options.split(",")
options = ''.join(options)

if "u" in options:
    chars = chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if "l" in options:
    chars = chars + "abcdefghijklmnopqrstuvwxyz"
if "n" in options:
    chars = chars + "12345678901234567890"
if "s" in options:
    chars = chars + "-=_+,./<>?:;"

if options == '' or chars == '':
    print("No Options Selected, Using All Possible Characters")
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678901234567890-=_+,./<>?:;"

try:
    numofpasses = int(input("\nHow Many Passwords Would You Like to Generate?- "))
except:
    print("Number of Passwords Value is Invalid, Defaulting to 1...")
    numofpasses = 1

for n in range(numofpasses):
    password = ''
    for char in range(length):
        password = password + random.choice(chars)
    print(f"\nPassword {n+1}: {password}")

print("\nPress Any Key to Exit...", end='')
os.system("pause > nul")