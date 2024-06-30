import os
import time
from fuzzywuzzy import fuzz
import sys
import clearterm

local_qnum = 1
qadata = {}
score = 0

print(f'Arguments provided: {sys.argv[1:]}')
print('Processing...')
time.sleep(3)
clearterm.clear_terminal()

def display_help():
    try:
        while True:
            try:
                print("You typed help!\nWhat do you need help with?\n1 for argument structure, 2 for about, 3 to exit.")
                helpuse = input()
            except KeyboardInterrupt:
                print("Quiz Stopped.")
                sys.exit()
            if helpuse == '1':
                print('The arguments should be structured:\nque1 ans1 que2 ans2, etc.')
                print("And also, instead of space put a ' so this s'p'a'c'e will look like s p a c e \nOr you can put \"s p a c e\" and it will also look like: s p a c e")
                input('Press Enter to Continue..')
                clearterm.clear_terminal()
            elif helpuse == '2':
                print("Quiz_engine v0.1\nBy Moa\nVersion made in python 3.11.2.")
                input('Press Enter to Continue')
                clearterm.clear_terminal()
            elif helpuse == '3':
                print('Exiting...')
                time.sleep(2)
                sys.exit()
            else:
                print('You did not type 1, 2, or 3')
                input('Press Enter to Continue...')
                clearterm.clear_terminal()
    except Exception as ezep:
        print(f'Oops There was an error. Error code: {ezep}')
        sys.exit()

try:
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "help":
        display_help()

    if len(sys.argv[1:]) < 2 or len(sys.argv[1:]) % 2 != 0:
        debugforlencheck2 = len(sys.argv) % 2 != 0
        debugforlencheck1 = len(sys.argv) < 2
        print(f"length of sys.argv is {len(sys.argv)}. If it is higher than 2, it should work, but if the number is odd, it won't work, and here is the bool for len(sys.argv) < 2: {debugforlencheck1}")
        print(f"Also, this is the bool for len(sys.argv) % 2 != 0: {debugforlencheck2}")
        if ValueError:
            print("You did not provide a sufficient number of arguments. It should be structured as 'q1 a1 q2 a2, etc.'")
            input('Press Enter to Continue...')
            sys.exit()

    for i in range(1, len(sys.argv), 2):
        que_key = 'q' + str(local_qnum)
        ans_key = 'a' + str(local_qnum)
        qadata[que_key] = sys.argv[i].replace("'", " ").replace('"', ' ')
        qadata[ans_key] = sys.argv[i + 1].replace("'", " ").replace('"', ' ')
        local_qnum += 1
except ValueError as e:
    print(e)
    sys.exit(1)
except IndexError as ie:
    print(f'There was an Index Error. Error Code: {ie}')

def quiz_ai_processor(A, Qnum, que_key, threshold=80):
    ans_key = 'a' + str(Qnum)
    similarity_score = fuzz.token_sort_ratio(A.lower(), qadata[ans_key].lower())
    global robotans
    robotans = similarity_score >= threshold
    if robotans:
        global score
        score += 1
        print('Correct!!! Good Job :)')
    else:
        print(f'That is Not Correct.')

local_qnum = 1
try:
    print('Hello!\nHow are you?\nWe are going to do a quiz!')
    while local_qnum <= len(sys.argv[1:]) // 2:
        que_key = 'q' + str(local_qnum)
        usea = input(qadata.get(que_key, f'No question available from q{que_key}') + ': ')
        quiz_ai_processor(usea, local_qnum, que_key, 80)
        local_qnum += 1
    print(f'The Quiz is Over, Have a Nice day!! \n Your score is {score}')
    input('Press Enter to Exit...')

except KeyboardInterrupt:
    print('\nQuiz Stopped.')
except Exception as e:
    print(f'Oops, there was an error: {str(e)}')
