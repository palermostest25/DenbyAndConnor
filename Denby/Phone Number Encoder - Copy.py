import os
os.system("title Phone Number Encoder")

while True:
    letterstoencode = input("Letters: ")
    letterstoencode = letterstoencode.lower()
    output = ""

    for l in letterstoencode:
        if l.isnumeric():
            output = output + l
        elif l == "a":
            output = output + "2"
        elif l == "b":
            output = output + "2"
        elif l == "c":
            output = output + "2"
        elif l == "d":
            output = output + "3"
        elif l == "e":
            output = output + "3"
        elif l == "f":
            output = output + "3"
        elif l == "g":
            output = output + "4"
        elif l == "h":
            output = output + "4"
        elif l == "i":
            output = output + "4"
        elif l == "j":
            output = output + "5"
        elif l == "k":
            output = output + "5"
        elif l == "l":
            output = output + "5"
        elif l == "m":
            output = output + "6"
        elif l == "n":
            output = output + "6"
        elif l == "o":
            output = output + "6"
        elif l == "p":
            output = output + "7"
        elif l == "q":
            output = output + "7"
        elif l == "r":
            output = output + "7"
        elif l == "s":
            output = output + "7"
        elif l == "t":
            output = output + "8"
        elif l == "u":
            output = output + "8"
        elif l == "v":
            output = output + "8"
        elif l == "w":
            output = output + "9"
        elif l == "x":
            output = output + "9"
        elif l == "y":
            output = output + "9"
        elif l == "z":
            output = output + "9"

    print(output)
    input("Press Enter to Encode another Phone Number...")
    print("")