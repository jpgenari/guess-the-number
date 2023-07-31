import random
import os

def clear():
    '''
    Clears the terminal when needed
    '''
    os.system('cls' if os.name == 'nt'else 'clear')

def welcome_message():
    '''
    Prints the welcome message to the users when starting the 
    program
    '''
    print()
    print()
    print()
    print()
    print()
    print('                 --- Welcome to ... ----')
    print()
    print()
    print('             G U E S S   T H E   N U M B E R')
    print()
    print()
    print()
    print()

def instructions():
    '''
    Provides option to the users either view instructions before
    the game or skip it going directly to play game. It also 
    includes while loop to collect right option.
    '''
    print()
    print('You can view instructions or just start playing!')
    print()

    while True:
        instructions = input('Do you want to check the instructions? Y/N: ').lower()
        clear()
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
            print('             with 4th guess: well, you lose! The points will')
            print('         sum up through the rounds and you can log them at the end!')
            print()
            print('                              Good look!')
            print()
            print()
            print()
            back = input('                       Press ENTER to proceed: ')
            clear()
            break
        elif instructions == 'n':
            break
        else:
            welcome_message()
            print()
            print('Incorrect entry, you should either pick [Y]es or [N]o')
            print()


def user_level_choice():
    '''
    Provides to the user the game level choice and get
    user's option. 
    Try method implemented to validate data: collects int and 
    raises error if input is not a number and if number
    is not 1 or 2.
    '''
    while True:
        print()
        game_level = input('Enter 1 for easy or 2 for hard level: ')
        clear()

        try:
            game_level = int(game_level)
        except ValueError:
            welcome_message()
            print('Numbers only!')
            continue
        if 1 <= game_level <= 2:
            return game_level
            break
        else:
            welcome_message()
            print('Number outside the allowed range.')
        
def main():
    '''
    Runs the program outside game loop
    '''
    clear()
    welcome_message()
    instructions()
    welcome_message()
    user_level = user_level_choice()

main()