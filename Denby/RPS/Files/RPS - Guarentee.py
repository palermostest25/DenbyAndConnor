import random
import os
print("Welcome to Paper Scissors Rock by Denby Daily")
os.system("title RPS by Denby Daily")
print("1=Paper\n2=Scissors\n3=Rock")
usropt = input("Paper, Scissors, Rock? (1,2,3)- ")


if usropt == "1":
    rps = "Rock"
    rpsusr = "Paper"
elif usropt == "2":
    rps = "Paper"
    rpsusr = "Scissors"
elif usropt == "3":
    rps = "Scissors"
    rpsusr = "Rock"
else:
    print("Error.")
    os.system("exit")

if rps == rpsusr:
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("Draw!")
    os.system("exit")
if rps == "Paper" and rpsusr == "Scissors":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("User wins!")
    os.system("exit")
if rps == "Scissors" and rpsusr == "Rock":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("User wins!")
    os.system("exit")
if rps == "Paper" and rpsusr == "Rock":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("User wins!")
    os.system("exit")
if rps == "Rock" and rpsusr == "Scissors":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("Computer wins!")
    os.system("exit")
if rps == "Scissors" and rpsusr == "Paper":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("Computer Wins!")
    os.system("exit")
if rps == "Rock" and rpsusr == "Paper":
    print(f"You put: {rpsusr}\nComputer put: {rps}")
    print("User Wins!")
    os.system("exit")