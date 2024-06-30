import os
import random
import time
from pynput.keyboard import Key, Listener
import threading
import sys
if os.name == 'nt': 
    import msvcrt
    import subprocess
    def clear_windows_input_buffer():
        while msvcrt.kbhit():
            msvcrt.getch()
else:
    def clear_windows_input_buffer():
        pass

time.sleep(2)
screen = ["ctrl","#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#",
          "#","#","#","#","#","#","#","#","#","#"
          ]

def dead():
    print("\nDead!")
    while True:
        clear_windows_input_buffer()
        playagain = input("Play Again[Y,N] ").strip()
        if playagain == 'y' or playagain == 'Y':
            python = sys.executable
            if os.name == 'nt':
                subprocess.run([sys.executable] + sys.argv)
            else:
                os.execl(python, python, *sys.argv)
        elif playagain == 'n' or playagain == 'N':
            sys.exit()
        else:
            print("Please Enter Y Or N.")
def keypress(key):
    global ctrl
    try:
        ctrl = key.char
    except Exception:
        pass
def keyreslease(key):
    pass
def keylistener():
    with Listener(on_press=keypress, on_release=keyreslease) as listener:
        listener.join()
def xycalc(x, y):
    y *= 10
    pixelxy = x + y
    return pixelxy
def sctrl(func, sx=0, sy=0, pixelchar='@'):
    if func == "clear":
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
    if func == "getscreen":
        printed = 1
        xycordprinted = 1
        while not printed == 11:
            printloops = 1
            xcoltoprint = ""
            while not printloops == 11:
                if not printloops == 1:
                    xcoltoprint = xcoltoprint + " " + screen[xycordprinted]
                elif printloops == 1:
                    xcoltoprint = xcoltoprint + screen[xycordprinted]
                printloops += 1
                xycordprinted += 1
            print(xcoltoprint)
            printed += 1
    if func == "pixelon":
        screen[xycalc(sx, sy)] = pixelchar
    if func == "pixeloff":
        screen[xycalc(sx, sy)] = "#"
    if func == "resetscreen":
        for pixel in range(101):
            screen[pixel] = "#"
listenerloop = threading.Thread(target=keylistener, daemon=True)
listenerloop.start()
snakebody = [(5,5)]
ctrl = "d"
snakelen = 1
wallcordlist = [
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
    (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
    (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0),
    (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9)
]
for wallcord in wallcordlist:
    sctrl("pixelon", wallcord[0], wallcord[1])
fy = random.randint(1,8)
fx = random.randint(2,9)

while True:
    px, py = snakebody[0]
    if not (ctrl == 'w' or ctrl == 'a' or ctrl == 's' or ctrl == 'd'):
        ctrl = lastctrl
    if ctrl == "w":
        py -= 1
    elif ctrl == "s":
        py += 1
    elif ctrl == "a":
        px -= 1
    elif ctrl == "d":
        px += 1
    if (px, py) in snakebody[1:] or (px, py) in wallcordlist:
        dead()
    sctrl("clear")
    snakebody.insert(0, (px, py))
    if len(snakebody) > snakelen:
        snakebody.pop()
    for segment in snakebody:
        sctrl("pixelon", segment[0], segment[1])
    sctrl("pixelon", fx, fy, 'F')
    if (px, py) == (fx, fy):
        snakelen += 1
        fy = random.randint(1,8)
        fx = random.randint(2,9)
        print("+ snake len")
    sctrl("getscreen")
    print("Score:",len(snakebody))
    lastctrl = ctrl
    time.sleep(1)
    for cord in snakebody:
        sctrl("pixeloff", cord[0], cord[1])
    sctrl("pixeloff", fx, fy)



# the x and y args on sctrl are optional for pixel ploting
# list[1:] is everything exept the first one