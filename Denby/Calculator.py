import os
import math
import time
import sys
import random
from statistics import *
import webbrowser
os.system("title Caluclator")
def goback():
    input("Press Enter to Go Back to The Start...")
    print()

# def clean_units(unit):
    # unit = unit.rstrip('s')  # remove plural
    # words_to_remove = ['m', 'l', 'g']  # remove type of unit
    # for word in words_to_remove:
        # unit = unit.replace(word, '')
    # return unit

def convert(val, unit_in, unit_out=''):
    SI = {'mm': 0.001, 'cm': 0.01, 'm': 1,
          'i': 0.00393701, 
          'deci': 0.1, '': 1.0, 'deka': 10,
          'hecto': 100, 'kilo': 1000, 'l': 1000, 'ml': 1,
          'mi': 1609, 'km': 1000, 'g': 1, 'kg': 1000, 'p': 453.592}
    return val*SI[unit_in]/SI[unit_out]

def simplify_fraction(numerator, denominator):
    if math.gcd(numerator, denominator) == denominator:
        return int(numerator/denominator)
    elif math.gcd(numerator, denominator) == 1:
        return str(numerator) + "/" + str(denominator)
    else:
        top = numerator / math.gcd(numerator, denominator)
        bottom = denominator / math.gcd(numerator, denominator)
        return str(top) + "/" + str(bottom)
os.system("cls")
print("Welcome to the Calculator!")
print("==========V 1 (Python)==========")
print("PI")
print("E")
print("POW")
print("SQRT")
print("Square")
print("Round")
print("ABS")
print("AVG")
print("Conv for Conversions")
print("Guess for the Guessing Game")
print("Simp for Simplify Fractions")
while True:
    try:
        sum = input("Please enter your sum(Type ? for information)- ")
        sum = sum.lower()
        if "=" in sum:
            sum = sum.split("=")
            calc1 = sum[0]
            calc2 = sum[1]
            result = eval(calc1)
            if str(calc2) == str(result):
                print("True")
            else:
                print("False")
            goback()
            continue
        if sum == "cls" or sum == "clear":
            os.system("cls")
            continue
        if sum == "power":
            usersum = input("Enter the Number: ")
            userthepower = input("To the Power of: ")
            usersum = float(usersum)
            userthepower = float(userthepower)
            result = (pow(usersum, userthepower))
            print(f"{usersum} to the Power of {userthepower} is {result}")
            goback()
            continue
        if sum == "sqrt":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.sqrt(usersum)
            print(f"The Square Root of {usersum} is {result}")
            goback()
            continue
        if sum == "square":
            usersum = input("Enter the Number to be Squared: ")
            usersum = float(usersum)
            result = (usersum*usersum)
            print(f"The Square of {usersum} is {result}")
            goback()
            continue
        if sum == "round":
            usersum = input("Enter the Number to be Rounded: ")
            userto = int(input("Enter the amount of Decimal Places to Round to: "))
            result = round(float(usersum), userto)
            print(f"{usersum} Rounded to {userto} Decimal Places is {result}")
            goback()
            continue
        if sum == "abs":
            usersum = input("Enter the Number to Find the Absolute Value of: ")
            usersum = float(usersum)
            result = abs(usersum)
            print(f"The Absolute Value of {usersum} is {result}")
            goback()
            continue
        if sum == "avg":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = list(str1.split(','))
            total = 0
            for i in result:
                total += float(i)
            result1 = total / len(result)
            result1 = round(result1, 3)
            print(f"The Average of {str1} is {result1}")
            goback()
            continue
        if sum == "median":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = str1.split(', ')
            result1 = median(result)
            print(f"The Median of {str1} is {result1}")
            goback()
            continue
        if sum == "mode":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = str1.split(', ')
            result1 = mode(result)
            print(f"The Mode of {str1} is {result1}")
            goback()
            continue
        if sum == "floor":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.floor(usersum)
            print(f"The Floor of {usersum} is {result}")
            goback()
            continue
        if sum == "ceiling" or sum == "ceil":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.ceil(usersum)
            print(f"The Ceiling of {usersum} is {result}")
            goback()
            continue

        if sum == "simp":
            nume = int(input("Numerator: "))
            deno = int(input("Denominator: "))
            result = (simplify_fraction(nume, deno))
            print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
            print(f"{nume}/{deno} Simplified is {result}")
            goback()
            continue
        
        if sum == "conv" or sum == "convert" or sum == "converter":
            print("1 = Miles to KM")
            print("2 = Pounds to KG")
            print("3 = Celsius to Fahrenheit")
            print("4 = Fractions to Decimals")
            print("5 = Percentages to Fractions")
            print("6 = Percentages to Decimals")
            print("7 = Percent of a number")
            print("8 = Percent off")
            print("9 = Inches to CM")
            print("10 = Tax Calculator")
            print("11 = Add percent to a number")
            print("12 = Language Translation jk Google Translate")
            print("13 = Month Information")
            print("14 = What percentage of a number is in a number")
            print("15 = Celsius to Kelvin")
            print("16 = Fahrenheit to Kelvin")
            print("17 = Circle Tools")
            convopt = input("What Option Would You Like [1-17]: ")
            print()

            if convopt == "1":
                print("1 = Miles to KM")
                print("2 = KM to Miles")
                milesorkm = input("What Option Would You Like? [1,2]: ")
                if milesorkm == "1":
                    miles = input("Miles: ")
                    miles = float(miles)
                    result = convert(miles, 'mi', 'km')
                    print(f"{miles} Miles is {result} KM")
                if milesorkm == "2":
                    km = input("KM: ")
                    km = float(km)
                    result = convert(km, 'km', 'mi')
                    print(f"{km} KM is {result} Miles")

            if convopt == "2":
                print("1 = Pound to KG")
                print("2 = KG to Pound")
                poundorkg = input("What Option Would You Like? [1,2]: ")
                if poundorkg == "1":
                    pound = input("Pound: ")
                    pound = float(pound)
                    result = convert(pound, 'p', 'kg')
                    print(f"{pound} Pounds is {result} KG")
                if poundorkg == "2":
                    kg = input("KG: ")
                    kg = float(kg)
                    result = convert(kg, 'kg', 'p')
                    print(f"{kg} KG is {result} Pounds")

            if convopt == "3":
                print("1 = Celsius to Fahrenheit")
                print("2 = Fahrenheit to Celsius")
                corf = input("What Option Would You Like? [1,2]: ")
                if corf == "1":
                    celsius = input("Celsius: ")
                    celsius = float(celsius)
                    # Manual because it's a Formula
                    result = eval("(celsius*9/5)+32")
                    print(f"{celsius} Degrees Celsius is {result} Fahrenheit")
                if corf == "2":
                    fahrenheit = input("Fahrenheit: ")
                    fahrenheit = float(fahrenheit)
                    # Manual because it's a Formula
                    result = eval("(fahrenheit-32)*9/5")
                    print(f"{fahrenheit} Degrees Fahrenheit is {result} Celsius")

            if convopt == "4":
                print("1 = Fraction to Decimal")
                print("2 = Decimal to Fraction")
                dorf = input("What Option Would You Like? [1,2]: ")
                if dorf == "1":
                    numerator = input("Numerator: ")
                    denominator = input("Denominator: ")
                    numerator = float(numerator)
                    denominator = float(denominator)
                    result = eval("numerator / denominator")
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{numerator} / {denominator} Expressed as a Decimal is {result}")
                if dorf == "2":
                    d = input("Decimal: ")
                    d = float(d)
                    result = (d).as_integer_ratio()
                    result = str(result)
                    result = result.replace('(', '')
                    result = result.replace(')', '')
                    result = result.replace(', ', ' / ')
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{d} Expressed as a Fraction is {result}")
            
            if convopt == "5":
                print("1 = Percentage to Fraction")
                print("2 = Fraction to Percentage")
                porf = input("What Option Would You Like? [1,2]: ")
                if porf == "1":
                    p = input("Percentage: ")
                    d = 100
                    p = float(p)
                    d = float(d)
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{p}% Expressed as a Fraction is {p} / {d}")
                if porf == "2":
                    f = input("Fraction (eg. 1/2) (The / Is the Line in the Middle of the Fraction (Vinculum)): ")
                    f1 = eval(f)
                    d = f1 * 100
                    result = eval("(round(d,4))")
                    print(f"{f} Expressed as a Percentage is {result}%")
                
            if convopt == "6":
                print("1 = Percentages to Decimals")
                print("2 = Decimals to Percentages")
                dorp = input("What Option Would You Like? [1,2]: ")
                if dorp == "1":
                    p = input("Percentage (No Percentage Sign): ")
                    print(f"{p}% as a Decimal is 0.{p}")
                if dorp == "2":
                    d = input("Decimal: ")
                    d = float(d)
                    result = float(eval("(d*100)"))
                    print(f"{d} as a Percentage is {result}%")

            if convopt == "7":
                p = input("Percentage (No Percentage Sign): ")
                num = input("Number to Find the Percentage of: ")
                p = float(p)
                num = float(num)
                result = eval("(p/100)*num")
                print(f"{p}% of {num} is {result}")
            
            if convopt == "8":
                print("1 = Price After Sale")
                print("2 = Price Before Sale")
                porp = input("What Option Would You Like? [1,2]: ")
                if porp == "1":
                    price = input("Origional Price (No Dollar Sign): ")
                    p = input("Percent Off (No Percentage Sign): ")
                    price = float(price)
                    p = float(p)
                    result = eval("price-(p/100)*price")
                    print(f"{p}% off ${price} is ${result}")
                if porp == "2":
                    price = input("Discounted Price (No Dollar Sign): ")
                    p = input("Percent Off (No Percentage Sign): ")
                    price = float(price)
                    p = float(p)
                    result = eval("price/((100-p)/100)")
                    print(f"The Origional Price of the Discounted Price ${price} After a Discount of {p}% is ${result}")

            if convopt == "9":
                print("1 = Inches to CM")
                print("2 = CM to Inches")
                iorc = input("What Option Would You Like? [1,2]: ")
                if iorc == "1":
                    inches = input("Inches: ")
                    inches = float(inches)
                    # Flipped because Math and to Correct the Convert Function
                    result = convert(inches, 'cm', 'i')
                    print(f"{inches} Inches to CM is {result}")
                if iorc == "2":
                    cm = input("CM: ")
                    cm = float(cm)
                    result = convert(cm, 'i', 'cm')
                    print(f"{cm} CM to Inches is {result}")

            if convopt == "10":
                price = input("Origional Price (No Dollar Sign): ")
                per = input("Tax Percentage (No Percentage Sign): ")
                price = float(price)
                per = float(per)
                result = eval("price+(price*(per/100))")
                print(f"${price} With Added Tax of {per}% is ${result}")

            if convopt == "11":
                value = input("Origional Value: ")
                per = input("Percentage to Add (No Percentage Sign): ")
                value = float(value)
                per = float(per)
                result = eval("value+(value*(per/100))")
                print(f"{value} With Added Percentage of {per}% is {result}")
            
            if convopt == "12":
                webbrowser.open("translate.google.com")
            
            if convopt == "13":
                print("Month Data: ")
                print("Number - Month - Short Form - Days")
                print("1 - January - Jan - 31")
                print("2 - Feburary - Feb - 28/29")
                print("3 - March - Mar - 31")
                print("4 - April - Apr - 30")
                print("5 - May - May - 31")
                print("6 - June - Jun - 30")
                print("7 - July - Jul - 31")
                print("8 - August - Aug - 31")
                print("9 - September - Sep - 30")
                print("10 - October - Oct - 31")
                print("11 - November - Nov - 30")
                print("12 - December - Dec - 31")
            
            if convopt == "14":
                fracnum = input("Part of a Number: ")
                totnum = input("Total Number: ")
                result = eval("(float(fracnum)/float(totnum)*100)")
                print(f"{fracnum} is {result}% of {totnum}")

            if convopt == "15":
                print("1 = Celsius to Kelvin")
                print("2 = Kelvin to Celsius")
                korc = input("What Option Would You Like? [1,2]: ")
                if korc == "1":
                    c = input("Celsius: ")
                    c = float(c)
                    result = eval("c+273.15")
                    print(f"{c} Degrees Celsius is {result} Degrees Kelvin")
                if korc == "2":
                    k = input("Kelvin: ")
                    k = float(k)
                    result = eval("k-273.15")
                    print(f"{k} Degrees Kelvin is {result} Degrees Celsius")

            if convopt == "16":
                print("1 = Fahrenheit to Kelvin")
                print("2 = Kelvin to Fehrenheit")
                fork = input("What Option Would You Like? [1,2]: ")
                if fork == "1":
                    f = input("Fahrenheit: ")
                    f = float(f)
                    # Manual because it's a formula
                    result = eval("(f-32)*5/9+273.15")
                    print(f"{f} Fahrenheit is {result} Kelvin")
                if fork == "2":
                    k = input("Kelvin: ")
                    k = float(k)
                    # Manual because it's a formula
                    result = eval("(k-273.15)*9/5+32")
                    print(f"{k} Kelvin is {result} Fahrenheit")

            if convopt == "17":
                print("1 = Area to Radius")
                print("2 = Radius to Area")
                print("3 = Area to Diameter")
                print("4 = Diameter to Area")
                print("5 = Area to Circumfrence")
                print("6 = Circumfrence to Area")
                print("7 = Diameter to Radius")
                print("8 = Radius to Diameter")
                print("9 = Diameter to Circumfrance")
                print("10 = Circumfrance to Diameter")
                print("11 = Radius to Circumfrance")
                print("12 = Circumfrance to Radius")
                corc = input("What Option Would You Like? [1-12]: ")
                print()
                if corc == "1":
                    a = input("Area (No Units)- ")
                    r = math.sqrt(float(a) / 3.14159265358979)
                    print(f"The Radius of a Cirle with an Area of {a} is {r}")
                if corc == "2":
                    r = input("Radius (No Units): ")
                    a = (3.14159265358979*(float(r)*float(r)))
                    print(f"The Area of a Circle with a Radius of {r} is {a}")
                if corc == "3":
                    a = input("Area (No Units)- ")
                    d = (3.14159265358979*(float(d)/2)*(float(d)/2))
                    print(f"The Diameter of a Circle with an Area of {a} is {d}")


            
                

            goback()
            continue



        if sum == "guess":
            randomnumber = random.randint(1, 100)
            guessamnt = 0
            while True:
                guess = input("Guess the Number: ")
                guess = int(guess)
                guessamnt += 1
                if guess == randomnumber:
                    print("Great Job!")
                    print(f"You Guessed It In {guessamnt} Tries!")
                if guess > randomnumber:
                    print("Lower!")
                    continue
                if guess < randomnumber:
                    print("Higher!")
                    continue
                goback()
                break
            continue

        else:
            sum = sum.replace("pi", "3.14159265358979")
            sum = sum.replace("e", "2.71828182845905")
            result = eval(sum)
            print(f"The Answer to {sum} is {result}")
            goback()
            continue
    except:
        print("Error")
        goback()
        continue