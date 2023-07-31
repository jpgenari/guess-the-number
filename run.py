import random
import os

def clear():
    '''
    Clears the terminal when needed
    '''
    os.system('cls' if os.name == 'nt'else 'clear')

def instructions():
    '''
    Provides option to the users either view instructions before
    the game or skip it going directly to play game. It also 
    includes while loop to collect right option.
    '''
    print()
    print('You can view instructions or just start playing!')
    print()
    instructions = input('Do you want to check the instructions? Y/N: ').lower()

    while instructions != 'y' and instructions != 'n':
        clear()
        print('Incorrect entry, you should either pick [Y]es or [N]o')
    else:
        if instructions == 'y':
            clear()
            print()
            print()
            print('                       Guess the hidden number!')
            print('              The aim of this game is to guess the number')
            print('             and have as few incorrect guesses as possible,')
            print('          you have 3 guesses, after each incorrect one you will')
            print('                          receive a hint!')
            print()
            print('      Be aware, the fewer incorrect guesses, the higher your score:')
            print('      1st guess: 500 pts, 2nd guess: 300 pts, 3rd guess: 100 pts and')
            print('             with 4th guess: well, you lose! The poins will')
            print('         sum up through the rounds and you can log them at the end!')
            print()
            print('                              Good look!')
            print()
            print()
            print()
            back = input('                       Press ENTER to proceed: ')

instructions()