import random as rand
from random import randint
import os
import sys
os.system("title Number Guesser")
print("Welcome to the Number Guesser!")
print("Rules:\n1. You will have to guess the number the computer is thinking of, you will have a chance to choose.\n2. You will enter the number you think the computer is thinking of and the computer will tell you if your guess is higher or lower.\n")

os.system("echo Press any key to start... && pause > nul")
randomrangemin = int(input("Enter the minimum number- "))

randomrangemax = int(input("Enter the maximum number- "))

def end():
    print(f"You won!")
    playagain = input("Would you like to play again? (Y/N)- ")
    if (playagain) == "y":
        os.startfile(sys.argv[0])
        sys.exit()
    elif (playagain) == "Y":
        os.startfile(sys.argv[0])
        sys.exit()
    elif (playagain) == 1:
        os.startfile(sys.argv[0])
        sys.exit()
    else:
        os.system("echo Press any key to exit... && pause > nul && exit")

print("Generating Number...")
count = int(0)
randomnumber = rand.randint(randomrangemin,randomrangemax)
print("Number Successfully Generated!")
while (count) < 1:
    guess = int(input(f"Guess a number between {randomrangemin} and {randomrangemax}- "))
    if (guess) == (randomnumber):
        count = int(2)
        end()
    if (guess) < (randomnumber):
        print("Higher")
    if (guess) > (randomnumber):
        print("Lower")