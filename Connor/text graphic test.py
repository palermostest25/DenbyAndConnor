import os

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

def xycalc(x, y):
    y *= 10
    pixelxy = x + y
    return pixelxy
def sctrl(func, sx=0, sy=0):
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
        screen[xycalc(sx, sy)] = "@"
    if func == "resetscreen":
        for pixel in range(101):
            screen[pixel] = "#"

px = 1
py = 1
while True:
    sctrl("resetscreen")
    sctrl("pixelon", px, py)
    sctrl("getscreen")
    ctrl = input("?: ")
    if ctrl == "w":
        py -= 1
    elif ctrl == "s":
        py += 1
    elif ctrl == "a":
        px -= 1
    elif ctrl == "d":
        px += 1
    sctrl("clear")



# the x and y args on sctrl are optional for pixel ploting