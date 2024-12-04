import sys
import math
from decimal import Decimal, getcontext

n = 1
sys.setrecursionlimit(2147483647)
try:
    while True:
        e = Decimal((1+1/n)**n)
        n += 1
        print(f"E: {e}", end='\r')
except KeyboardInterrupt:
    print("Exiting...")