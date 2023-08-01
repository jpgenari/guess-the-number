import random
import os
import messages

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

    while True:
        instructions = input('Do you want to check the instructions? Y/N: ').lower()
        # clear()
        if instructions == 'y':
            # clear()
            messages.instructions_message()
            back = input('                       Press ENTER to proceed: ')
            # clear()
            break
        elif instructions == 'n':
            break
        else:
            messages.welcome_message()
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
        # clear()

        try:
            game_level = int(game_level)
        except ValueError:
            messages.welcome_message()
            print('Numbers only!')
            continue
        if 1 <= game_level <= 2:
            return game_level
            break
        else:
            messages.welcome_message()
            print('Number outside the allowed range.')
    
    # clear()

def get_random_number(user_level):
    '''
    Picks a random number to be guessed based on the user 
    level option
    '''
    if user_level == 1:
        guess_range = 50
        guesses_allowed = 20
    elif user_level == 2:
        guess_range = 100
        guesses_allowed = 20

    number = random.randint(1, guess_range)
    
    print(number)




        
def main():
    '''
    Runs the program outside game loop
    '''
    # clear()
    messages.welcome_message()
    instructions()
    messages.welcome_message()
    user_level = user_level_choice()
    # clear()
    number = get_random_number(user_level)

main()