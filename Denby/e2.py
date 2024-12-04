from decimal import Decimal, getcontext
import sys
sys.setrecursionlimit(2147483647)

decimals = 20

decimals = int(decimals)

getcontext().prec = decimals

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

e = 1
count = 1
try:
    while True:
        countfactorial = (factorial(count))
        e = Decimal(e+Decimal(1/factorial(count)))
        count += 1
        print(e, end='\r')
except KeyboardInterrupt:
    print("\nExiting...")
    exit()