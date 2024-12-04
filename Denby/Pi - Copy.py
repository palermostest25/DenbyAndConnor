import sys
from decimal import Decimal, getcontext
import os
count = 0

sys.setrecursionlimit(2147483647)

decimals = input("How Many Decimals Would You Like in Your Number? [1-x]: ")
accuracy = input("How Accurate Would You Like Your Number? [1-x] (x for Infinity): ")

decimals = int(decimals)

getcontext().prec = decimals

def pi_bbp():
    count = 0
    pi = Decimal(0)
    k = 0
    while count < accuracy:
        term = (Decimal(1)/(16**k)) * (
            Decimal(4)/(8*k + 1) - Decimal(2)/(8*k + 4) - Decimal(1)/(8*k + 5) - Decimal(1)/(8*k + 6))
        if term == 0:
            break
        pi += term
        k += 1
        print(pi)
        count +=1
    return pi

if accuracy.isnumeric():
    try:
        accuracy = int(accuracy)  # Convert input to integer
        pi = pi_bbp()
        print(f"Pi: {pi}, Accuracy: {accuracy}")
    except KeyboardInterrupt:
        print(f"Final: {pi}, Accuracy: {accuracy}")
        input("Press Enter to Exit...")

else:
    print("Invalid input or non-numeric value.")
    count = 0
    pi = Decimal(0)
    k = 0
    try:
        while True:
            term = (Decimal(1)/(16**k)) * (
                Decimal(4)/(8*k + 1) - Decimal(2)/(8*k + 4) - Decimal(1)/(8*k + 5) - Decimal(1)/(8*k + 6))
            if term == 0:
                break
            pi += term
            k += 1
            print(f"Pi: {pi}, Accuracy: {count}")
            count +=1
    except KeyboardInterrupt:
        os.system("cls")
        print(f"Final: {pi}, Accuracy: {accuracy}")
        input("Press Enter to Exit...")