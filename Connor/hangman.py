from wonderwords import RandomWord
print("Welcome To Hangman")
print("By Connor Davis")
random = RandomWord()
word = "testtesttesttesttesttesttesttesttest"
currentword = ''
hangmanart = [
'''
Letters Wrong: 0
_________
|        |
|        |
|       
|        
|
|
|
|
|
|
|
''',
'''
Letters Wrong: 1
_________
|        |
|        |
|       (0)
|        
|
|
|
|
|
|
|
''',
'''
Letters Wrong: 2
_________
|        |
|        |
|       (0)
|      #####
|      #####
|      #####
|      #####
|
|
|
|
''',
'''
Letters Wrong: 3
_________
|        |
|        |
|       (0)
|     |#####
|     |#####
|     |#####
|      #####
|
|
|
|
''',
'''
Letters Wrong: 4
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|
|      #####
|
|
|
|
''',
'''
Letters Wrong: 5
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|
|      #####
|      |
|      |
|      |
|
''',
'''
Letters Wrong: 6
_________
|        |
|        |
|       (0)
|     |#####|
|     |#####|
|     |#####|  
|      #####
|      |   |
|      |   |
|      |   |
|
'''
]
def get_uinput():
            while True:
                try:
                    uinput = str(input("Letter: "))
                    if len(uinput) == 1:
                        break
                    else:
                        print("Please Enter 1 Letter!")
                except ValueError:
                    print("Please Enter A Letter!")
            return(uinput)

def lose(words_wrong, word_to_guess, word_length):
    global wordswrong
    global currentword
    global num
    global loops
    global letter
    print(hangmanart[words_wrong])
    print(f"Thanks For Playing!\nThe Word Was {word_to_guess}.\nThe Word Length Was {word_length}\nI Hope You Get It Next Time!")
    while True:
        playagain = input("Press P To Play Again Or Q to Exit! ")
        if playagain == "Q" or playagain == "q":
            exit()
        elif playagain == "P" or playagain == "p":
            wordswrong = 0
            currentword = ''
            num = 0
            loops = 0
            letter = ''
            mainloop()

def win(words_wrong, word_to_guess, word_length):
    global wordswrong
    global currentword
    global num
    global loops
    global letter
    print(f"Congrats! You Won!!!!!!\nThanks For Playing!\nThe Word Was {word_to_guess}.\nThe Word Length Was {word_length}\nYou Got {words_wrong} Words Wrong!")
    while True:
        playagain = input("Press P To Play Again Or Q to Exit! ")
        if playagain == "Q" or playagain == "q":
            exit()
        elif playagain == "P" or playagain == "p":
            wordswrong = 0
            currentword = ''
            num = 0
            loops = 0
            letter = ''
            mainloop()

def mainloop():
    global currentword
    global num
    global word
    try:   
        while True:
            try:
                wordlen = int(input("Length Of Word [2-15]: "))
                if wordlen < 2:
                    wordlen = 2
                elif wordlen > 15:
                    wordlen = 15
                break
            except ValueError:
                print("You Did Not Enter A Number!")

        print("Generating Word, Please Wait.")
        word = random.word(word_min_length=wordlen, word_max_length=wordlen)
        word = word.lower()

        for num in range(wordlen):
            currentword = currentword + "_"
        num = 0
        wordswrong = 0
        while True:
            print(hangmanart[wordswrong])
            print(currentword)
            workinguinput = get_uinput()
            bdcurrentword = list(currentword)
            bdword = list(word)
            loops = 0
            prevcurrentword = currentword
            for letter in bdword:
                if letter == workinguinput:
                    bdcurrentword[loops] = workinguinput
                loops += 1
            currentword = ''.join(bdcurrentword)
            if prevcurrentword == currentword:
                wordswrong += 1
            if wordswrong == 6:
                lose(6, word, wordlen)
            if word == currentword:
                win(wordswrong, word, wordlen)
                            
    except KeyboardInterrupt:
        print("\nYou Have Quited!")
        try:
            input("Press Enter To Exit!")
            exit()
        except KeyboardInterrupt:
            exit()
mainloop()
