import math
from decimal import Decimal, getcontext
import sys
import os
import time


start = time.time()


sys.setrecursionlimit(2147483647)
while True:
    try:
        decimals = int(input("How Many Decimals Would You Like?- "))
        break
    except:
        print("Input a Number of Decimals...")
while True:
    try:
        accuracy = int(input("Accuracy- "))
        break
    except:
        print("Input a Number of for Accuracy...")
num_terms = decimals
getcontext().prec = decimals

def calculate_e(n_terms):
    global e
    e = Decimal(sum(1 / Decimal(math.factorial(i)) for i in range(n_terms)))
    os.system("cls")
    print(f"E: {e}")
count = 0
try:
    while count < accuracy:
        calculate_e(num_terms)
        count += 1
except KeyboardInterrupt:
    pass
os.system("cls")
end = time.time()
timetaken = end - start
print(f"Final: {e}, Decimals: {decimals}, Accuracy: {count} Time Taken: {timetaken} Seconds")
print("Exiting...")
exit()