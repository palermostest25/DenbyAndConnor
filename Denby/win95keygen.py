import sys
import random
import os
os.system("title Windows 95 KeyGen")
def divisible_random(a,b,n):
    if b-a < n:
      raise Exception('{} is too big'.format(n))
    result = random.randint(a, b)
    while result % n != 0:
      result = random.randint(a, b)
    return result
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
else:
    print("Error: Not Enough Arguments!")
    print("To Get Personal Keys, the Format is: nameoffile.py numberofkeys")
    print("To Get OEM Keys, the Format is: nameoffile.py -o numberofkeys")
    input("Press Enter to Exit...")
    exit()
if arg1 == "-o":
    generated = 0
    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
    else:
        print("Error: Not Enough Arguments!")
        print("To Get Personal Keys, the Format is: nameoffile.py numberofkeys")
        print("To Get OEM Keys, the Format is: nameoffile.py -o numberofkeys")
        input("Press Enter to Exit...")
        exit()
    def gensec1():
        global sec1
        global sec1p1
        global sec1p2
        sec1p1 = ("{:03d}".format(random.randint(1, 366)))
        sec1p2 = (random.choice(["95", "96", "97", "98", "99", "00", "01", "02", "03"]))
        sec1 = (f"{sec1p1}{sec1p2}")
    def gensec2():
        global sec2
        sec2 = (divisible_random(100000, 999999, 7))
    def gensec3():
        global sec3
        sec3 = random.randint(10000, 99999)
        
    while generated < int(arg2):
        gensec1()
        gensec2()
        gensec3()
        friendlygenerated = generated + 1
        print(f"Your Windows 95 OEM Key ({friendlygenerated}) is {sec1}-OEM-0{sec2}-{sec3}")
        generated += 1
    input("Press Enter to Exit...")
    exit()
else:
    generated = 0
    def gensec1():
        global sec1
        sec1 = random.randint(100, 999)
        if sec1 == 333 or sec1 == 444 or sec1 == 555 or sec1 == 666 or sec1 == 777 or sec1 == 888 or sec1 == 999:
            gensec1()
    def gensec2():
        global sec2
        sec2 = (divisible_random(1000000, 9999999, 7))

    while generated < int(arg1):
        gensec1()
        gensec2()
        friendlygenerated = generated + 1
        print(f"Your Windows 95 Key ({friendlygenerated}) is: {sec1}-{sec2}")
        generated += 1
    input("Press Enter to Exit...")
    exit()