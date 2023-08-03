import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guess-the-number')

import random
import os
import sys
import pandas as pd

import messages

def update_worksheet(data, worksheet):
    """
    Updates the worksheet with the username and scores
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)

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
        clear()
        if instructions == 'y':
            clear()
            messages.instructions_message()
            back = input('                       Press ENTER to proceed: ')
            clear()
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
        clear()

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

def user_guessed_number(guess_range, incorrect_guesses):
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
            clear()
            print(f'Tried numbers: {incorrect_guesses}')
            print()
            print('Numbers only!')
            continue
        if 1 <= guess <= guess_range:
            clear()
            return guess
            break
        else:
            clear()
            print(f'Tried numbers: {incorrect_guesses}')
            print()
            print(str(user_input) +' is outside the allowed range (1 - ' + str(guess_range) + ')')

        # print(guess)

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
            sys.exit("Thank you for playing! You've left the game")
        else:
            print('Invalid number, only 1 or 2 are accepted')

def calculate_score(guesses_allowed, user_level):
    '''
    Gets user score based on remaining allowed guesses and
    user selected level
    '''
    if user_level == 1:
        score = guesses_allowed * 4
    else:
        score = guesses_allowed * 8
    return score

def user_name(score):
    '''
    Gets user name or nickname to be logged to the game history
    '''
    while True:
        print()
        user_name = input('Please enter your name or nickname\n')

        if len(user_name) <= 1 or len(user_name) >= 11:
            print('Name / username should be 2 to 10 characters')
        else:
            update_results(user_name, score)
            return user_name
        
def update_results(user_name, score):
    '''
    Gets both username and score and add to list data which 
    is then pushed to the worksheet results.
    '''
    data = [user_name, score]
    update_worksheet(data, 'results')
    display_results()

def display_results():
    '''
    Display results from previous players at the end of
    the game.
    Creates a ranking showing users based on their scores in descending order (top scored at the top).
    Displays only the top 5 scorers.
    '''
    data = SHEET.worksheet('results').get_all_values()
    headers = data[0]
    rows = data[1:]

    df = pd.DataFrame(rows, columns=headers)
    df = df[['Player', 'Points']].sort_values(by='Points', ascending=False)

    top_5 = df.head(5)

    print()
    print('Check our all time ranking!')
    print()
    print(top_5.to_string(index=False))
    print()
    play_again_or_exit()


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
        print(f'{guesses_allowed} remaining guesses')
        guess = user_guessed_number(guess_range, incorrect_guesses)
        if guess == number:
            print('Winner')
            print()
            score = (calculate_score(guesses_allowed, user_level))
            print(f'You scored {score} points, well done!')
            user_name(score)
            break
        else:
            if guess in incorrect_guesses:
                print(f'Tried numbers: {incorrect_guesses}')
                print()
                print('You have tried this number already! Try again')
                print()
                continue
            else:
                guesses_allowed -= 1
                incorrect_guesses.append(guess)
                print(f'Tried numbers: {incorrect_guesses}')
                print()
                if guesses_allowed == 0:
                    print("You lose! Wish you more luck next time.")
                    print()
                else:
                    if abs(number - guess) <= 5:
                        print("You're getting warmer!!!")
                        print()
                    elif abs(number - guess) <= 10:
                        print("You're warm!")
                        print()
                    elif abs(number - guess) <= 20:
                        print("You're cold.")
                        print()
                    else:
                        print("You're freezing.")
                        print()
    else:
        play_again_or_exit()


def main():
    '''
    Runs the program outside game loop
    '''
    clear()
    messages.welcome_message()
    show_instructions()
    messages.welcome_message()
    user_level = user_level_choice()
    clear()
    number, guess_range = generate_random_number(user_level)
    game_loop(number, guess_range, user_level)

main()
