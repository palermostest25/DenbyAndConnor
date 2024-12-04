import os

os.system("title Phone Number Decoder")
while True:
    numtodecode = input("Input Number: ")

    for loop1 in numtodecode:
        if loop1.isalpha():
            print(loop1, end='')
        if loop1 == '1':
            print('  ', end='')
        if loop1 == '2':
            print('A ', end='')
        if loop1 == '3':
            print('D ', end='')
        if loop1 == '4':
            print('G ', end='')
        if loop1 == '5':
            print('J ', end='')
        if loop1 == '6':
            print('M ', end='')
        if loop1 == '7':
            print('P ', end='')
        if loop1 == '8':
            print('T ', end='')
        if loop1 == '9':
            print('W ', end='')
        else:
            print(' ', end='')

    print(' ')
    for loop2 in numtodecode:
        if loop2.isalpha():
            print(loop2, end='')
        if loop2 == '1':
            print('  ', end='')
        if loop2 == '2':
            print('B ', end='')
        if loop2 == '3':
            print('E ', end='')
        if loop2 == '4':
            print('H ', end='')
        if loop2 == '5':
            print('K ', end='')
        if loop2 == '6':
            print('N ', end='')
        if loop2 == '7':
            print('Q ', end='')
        if loop2 == '8':
            print('U ', end='')
        if loop2 == '9':
            print('X ', end='')
        else:
            print(' ', end='')

    print(' ')
    for loop3 in numtodecode:
        if loop3.isalpha():
            print(loop3, end='')
        if loop3 == '1':
            print('  ', end='')
        if loop3 == '2':
            print('C ', end='')
        if loop3 == '3':
            print('F ', end='')
        if loop3 == '4':
            print('I ', end='')
        if loop3 == '5':
            print('L ', end='')
        if loop3 == '6':
            print('O ', end='')
        if loop3 == '7':
            print('R ', end='')
        if loop3 == '8':
            print('V ', end='')
        if loop3 == '9':
            print('Y ', end='')
        else:
            print(' ', end='')

    print(' ')
    for loop4 in numtodecode:
        if loop4.isalpha():
            print(loop4, end='')
        if loop4 == '1':
            print('  ', end='')
        if loop4 == '2':
            print('  ', end='')
        if loop4 == '3':
            print('  ', end='')
        if loop4 == '4':
            print('  ', end='')
        if loop4 == '5':
            print('  ', end='')
        if loop4 == '6':
            print('  ', end='')
        if loop4 == '7':
            print('S ', end='')
        if loop4 == '8':
            print('  ', end='')
        if loop4 == '9':
            print('Z ', end='')
        else:
            print(' ', end='')

    print('\n')