import os

def clear_terminal():
    if os.name == 'posix':  
        os.system('clear')
    elif os.name == 'nt':  
        os.system('cls')
    else:
        print("os not detected.")
