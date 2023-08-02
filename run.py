
import random
import os
import sys
import messages

def clear():
    '''
    Clears the terminal when needed
    '''
    os.system('cls' if os.name == 'nt'else 'clear')

def show_instructions():
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

def generate_random_number(user_level):
    '''
    Picks a random number to be guessed based on the user 
    level option
    '''
    if user_level == 1:
        guess_range = 30
    elif user_level == 2:
        guess_range = 60

    number = random.randint(1, guess_range)

    # print(number)

    return number, guess_range

def user_guessed_number(guess_range):
    '''
    Gets user guessed number and validate it, otherwise
    user will see an error message if number is out of 
    guess range and not a number
    '''
    while True:
        print()
        user_input = input('Guess a number between 1 and ' + str(guess_range) + ': ')
        try:
            guess = int(user_input)
        except ValueError:
            print('Numbers only!')
            continue
        if 1 <= guess <= guess_range:
            return guess
            break
        else:
            print(str(user_input) +' is outside the allowed range (1 - ' + str(guess_range) + ')')

        print(guess)

def user_name():
    '''
    Gets user name or nickname to be logged to the game history
    '''
    while True:
        print()
        user_name = input('Please enter your name or nickname\n')

        if len(user_name) <= 1 or len(user_name) >= 11:
            print('Name / username should be 2 to 10 characters')
        else:
            print(f'Thank you for playing {user_name} !')
            play_again_or_exit()
            return user_name


def play_again_or_exit():
    '''
    Provide an option for user to play again and
    also validate user input
    '''
    while True:
        play_again = input('Press 1, if you want to start again or 2 to exit: ')

        try:
            play_again = int(play_again)
        except ValueError:
            print('Incorrect input, only 1 or 2 are accepted, try again')
            continue
        if play_again == 1:
            main()
            break
        elif play_again == 2:
            clear()
            sys.exit("You've left the game")
        else:
            print('Invalid number, only 1 or 2 are accepted')

def get_score(guesses_allowed, user_level):
    '''
    Gets user score based on remaining allowed guesses and
    user selected level
    '''
    if user_level == 1:
        score = guesses_allowed * 5
    else:
        score = guesses_allowed * 10
    return score

def game_loop(number, guess_range, user_level):
    '''
    Runs the whole game.
    Gets the random generated number and the users guessed number
    and checks winner condition.
    Sets the number of guesses allowed which will determine how 
    long the game will run.
    Displays to user numbers already guessed and checks if user is 
    repeating a number - not allowing repeated numbers.
    '''
    guesses_allowed = 10
    incorrect_guesses = []

    while guesses_allowed > 0:
        print(guesses_allowed)
        guess = user_guessed_number(guess_range)
        if guess == number:
            print('Winner')
            print(get_score(guesses_allowed, user_level))
            user_name()
            break
        else:
            if guess in incorrect_guesses:
                print('You have tried this number already! Try again')
                continue
            else:
                guesses_allowed -= 1
                incorrect_guesses.append(guess)
                print(f'You have tried do far: {incorrect_guesses}')
                if guesses_allowed == 0:
                    print()
                else:
                    if abs(number - guess) <= 5:
                        print("You're warm!")
                    elif abs(number - guess) <= 10:
                        print("You're getting warmer.")
                    elif abs(number - guess) <= 20:
                        print("You're cold.")
                    else:
                        print("You're freezing.")
    else:
        print("You lose")
        user_name()


def main():
    '''
    Runs the program outside game loop
    '''
    # clear()
    messages.welcome_message()
    show_instructions()
    messages.welcome_message()
    user_level = user_level_choice()
    # clear()
    number, guess_range = generate_random_number(user_level)
    # guess = user_guessed_number(guess_range)
    game_loop(number, guess_range, user_level)

main()
