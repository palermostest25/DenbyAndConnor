import re
import os
try:
    from pint import UnitRegistry
except ModuleNotFoundError:
    os.system("pip install pint")
    print("Open This File Again Please!")
    input("Press Enter To Exit!")
    exit()

ureg = UnitRegistry()
pi = 3.141592653589793
unit = 0

try:
    while True:
        try:
            print("Welcome To Calculator\n=====================\nV0.1 (Production Test)\n=====================\nBy Connor Davis\n=====================\nBug Reporting: https://github.com/palermostest25/ConnorAndDenby/issues\n=====================")
            print("<num>Sqrt For Square Root\n<num>Pi or just Pi for Pi\n<num>Powof<num> For to The Power Of")
            print("<num>round For Round\n<num>square For Number Squared\n<num>cube For Number Cubed")
            print("<num>tri For Triangle Numbers\n<num>numline For Number Line\n<num, num, num, etc, etc>average For Average\n<num>abs For Absolute")
            print("dataunits For Data Unit Conversion")
            uinput = input("Sum: ")
            numbers = re.findall(r'(?:\-)?\d+(?:\.\d+)?', uinput)
            try:
                if numbers:
                    num1 = numbers[0]
                    num2 = numbers[1]
                elif not numbers:
                    num1 = None
                    num2 = None
            except IndexError:
                pass
            uinput = uinput.lower()
            try:
                print(eval(uinput))
            except ValueError:
                pass
            except SyntaxError:
                pass
            except NameError:
                pass
            if re.findall(r'sqrt', uinput):
                prev = 0
                guess = int(num1) / 2
                rnum = 0
                while not prev == guess:
                    prev = guess
                    guess = (guess + (int(num1) / guess)) / 2
                    rnum += 1
                print(guess)
            if re.findall(r'pi', uinput):
                try: 
                    if not num1 == None:
                        print(int(num1) * pi)
                except ValueError:
                    print("Error")
            if re.findall(r'powof', uinput):
                try:
                    print(pow(int(num1), int(num2)))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'round', uinput):
                try:
                    print(num1)
                    print(round(float(num1)))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'square', uinput):
                try:
                    print(pow(int(num1), 2))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'cube', uinput):
                try:
                    print(eval(int(num1) ** 3))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'tri', uinput):
                try:
                    plus1 = int(num1) + 1
                    print(int(num1) * plus1 / 2)
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'numline', uinput):
                try:
                    loops = 0
                    num1len = len(num1)
                    while not loops == int(num1) + 1:
                        currentnumlinepeacetoshow = str(loops)
                        while not len(currentnumlinepeacetoshow) == num1len:
                            currentnumlinepeacetoshow = currentnumlinepeacetoshow + " "
                        currentnumlinepeacetoshow = currentnumlinepeacetoshow + '|'
                        print(currentnumlinepeacetoshow)
                        loops += 1
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'average', uinput):
                try:
                    numberslen = len(numbers)
                    numofloops = 0
                    while not numberslen == numofloops:
                        numbers[numofloops] = int(numbers[numofloops])
                        numofloops += 1
                    print(sum(numbers) / int(len(numbers)))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'abs', uinput):
                try:
                    print(abs(int(num1)))
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")
            if re.findall(r'dataunits', uinput):
                try:
                    print("From:\nB\nKB\nMB\nGB\nTB\nPB")
                    dufrom = input("? [Type B or KB or etc or etc]: ")
                    duinput = input("How Meany?: ")
                    print("To:\nB\nKB\nMB\nGB\nTB\nPB")
                    duto = input("? [Type B or KB or etc or etc]: ")
                    dufrom = dufrom.lower()
                    duto = duto.lower()
                    if not (dufrom == "b" or dufrom == "kb" or dufrom == "mb" or dufrom == "gb" or dufrom == "tb" or dufrom == "pb"):
                        raise ValueError
                    if not (duto == "b" or duto == "kb" or duto == "mb" or duto == "gb" or duto == "tb" or duto == "pb"):
                        raise ValueError
                    if dufrom == "b":
                        unit = int(duinput) * ureg.byte
                    elif dufrom == "kb":
                        unit = int(duinput) * ureg.kilobyte
                    elif dufrom == "mb":
                        unit = int(duinput) * ureg.megabyte
                    elif dufrom == "gb":
                        unit = int(duinput) * ureg.gigabyte
                    elif dufrom == "tb":
                        unit = int(duinput) * ureg.terabyte
                    elif dufrom == "pb":
                        unit = int(duinput) * ureg.petabyte
                    if duto == "b":
                        print(unit.to(ureg.byte))
                    elif duto == "kb":
                        print(unit.to(ureg.kilobyte))
                    elif duto == "mb":
                        print(unit.to(ureg.megabyte))
                    elif duto == "gb":
                        print(unit.to(ureg.gigabyte))
                    elif duto == "tb":
                        print(unit.to(ureg.terabyte))
                    elif duto == "pb":
                        print(unit.to(ureg.petabyte))
                except ValueError:
                    print("valError")
                except SyntaxError:
                    print("synError") 
            if re.findall(r'nice', uinput):
                try:
                    print(69, 420)
                except ValueError:
                    print("Error")
                except SyntaxError:
                    print("Error")   
            input("Press Enter To do another sum!")
        except ValueError:
            print("value error")
            input("Press Enter To do another sum!")
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        num1 = ''
        num2 = ''
except KeyboardInterrupt:
    print("\nYou Have Exited!")
    print("Leaving Calculator...")
    exit()

# - minus
# + plus
# * times
# / divide
# ** powerof
# not only applies to first condition in if, not all. so if mulible conditions put in brackets so it will do all at once
# r"[\-\+\*]" will check for + - or *
