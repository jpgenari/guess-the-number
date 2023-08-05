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
        instructions = input('Do you want to check the instructions? Y/N:\n').lower()
        clear()
        if instructions == 'y':
            clear()
            messages.instructions_message()
            input('Press ENTER to proceed:\n')
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
    Gets user level choice - easy, medium or hard. 
    Try method implemented to validate data: collects int and 
    raises error if input is not a number and if number
    is not between 1 to 3.
    '''
    while True:
        print()
        game_level = input('Enter 1 for easy, 2  medium or, if you dare, 3 for hard leveL: \n')
        clear()

        try:
            game_level = int(game_level)
        except ValueError:
            messages.welcome_message()
            print('Numbers only!')
            continue
        if 1 <= game_level <= 3:
            return game_level
        else:
            messages.welcome_message()
            print('Number outside the allowed range.')
    # clear()

def generate_random_number(user_level):
    '''
    Picks a random number to be guessed based on the user 
    level option, changing the number range.
    '''
    if user_level == 1:
        guess_range = 30
    elif user_level == 2:
        guess_range = 60
    elif user_level == 3:
        guess_range = 120

    number = random.randint(1, guess_range)

    print(f"Lucky number {number}")

    return number, guess_range

def user_guessed_number(guess_range, incorrect_guesses):
    '''
    Gets user guessed number and validate it, otherwise
    user will see an error message if number is out of 
    guess range and not a number
    '''
    while True:
        print()
        user_input = input(f'Guess a number between 1 and {guess_range} :\n')
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
        else:
            clear()
            print(f'Tried numbers: {incorrect_guesses}')
            print()
            print(f'{user_input} is outside the allowed range > 1 - {guess_range}')

def play_again_or_exit():
    '''
    Provides option for user to play again and
    also validate user input
    '''
    while True:
        play_again = input('Press 1, if you want to start again or 2 to exit:\n')

        try:
            play_again = int(play_again)
        except ValueError:
            clear()
            print('Incorrect input, only 1 or 2 are accepted, try again \n')
            continue
        if play_again == 1:
            main()
            break
        elif play_again == 2:
            clear()
            sys.exit("You've left the game. Thank you for playing!")
        else:
            clear()
            print('Invalid number, only 1 or 2 are accepted \n')

def calculate_score(guesses_allowed, user_level):
    '''
    Gets user score based on remaining allowed guesses and
    user selected level
    '''
    if user_level == 1:
        score = guesses_allowed * 10
    elif user_level == 2:
        score = guesses_allowed * 20
    else:
        score = guesses_allowed * 40
    return score

def pick_user_name(score):
    '''
    Gets user name or nickname to be logged to the game history
    '''
    while True:
        print()
        user_name = input('Please enter your name or nickname\n')

        if len(user_name) <= 1 or len(user_name) >= 13:
            print('Name should be 2 to 12 characters')
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
    display_results(score)

def display_results(score):
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
    df['Scores'] = pd.to_numeric(df['Scores'], errors='coerce')
    df = df[['Player', 'Scores']].sort_values(by='Scores', ascending=False)

    top_5 = df.head(5)

    print()
    print(f'You scored {score} points, well done!')
    print()
    print('Check our all time ranking!')
    print()
    print(top_5.to_string(index=False))
    print()
    play_again_or_exit()

# display_results(score)


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
    last_distance = -1

    while guesses_allowed > 0:
        # print(f'{guesses_allowed} remaining guesses')
        guess = user_guessed_number(guess_range, incorrect_guesses)
        how_close_to_number = (number - guess)
        how_close_to_number = how_close_to_number.__abs__()
        if guess == number:
            print(f"{guess} is your lucky number, you W I N!")
            score = (calculate_score(guesses_allowed, user_level))
            pick_user_name(score)
            break
        else:
            if guess in incorrect_guesses:
                print(f'Tried numbers: {incorrect_guesses} \n')
                print('You have tried this number already! Try again \n')
                continue
            else:
                guesses_allowed -= 1
                incorrect_guesses.append(guess)
                print(f'Tried numbers: {incorrect_guesses} \n')
                
                # print(f"lucky number {number}")
                
                # print(f"how close to number {how_close_to_number}")

                # print(f"last distance {last_distance}")
                
                if guesses_allowed == 0:
                    print(f"The lucky number was {number} \n")
                    print("You lose! Wish you more luck next time. \n")
                else:
                    if how_close_to_number <=3 and last_distance == -1:
                        print(f"You're BOILING!!! Remaining guesses {guesses_allowed}")
                    elif last_distance == -1:
                        if 3 < how_close_to_number <= 8:
                            print(f"You're Hot!! Remaining guesses {guesses_allowed}")
                        elif 8 < how_close_to_number <= 15:
                            print(f"You're Warm! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number > 15:
                            print(f"You're Cold. Remaining guesses {guesses_allowed}")
                    else:
                        if how_close_to_number < last_distance:
                            if how_close_to_number <= 3:
                                print(f"You're HOTTER!! Remaining guesses {guesses_allowed}")
                            else:
                                print(f"You're Warmer! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number == last_distance:
                            print(f"Argh, neither hotter neither colder! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number > last_distance:
                            print(f"You're Colder. Remaining guesses {guesses_allowed}")
                    last_distance = how_close_to_number
    else:
        play_again_or_exit()


def main():
    '''
    Runs the program outside game loop
    '''
    clear()
    print('\n Welcome to ...')
    messages.game_name()
    show_instructions()
    messages.game_name()
    user_level = user_level_choice()
    clear()
    number, guess_range = generate_random_number(user_level)
    game_loop(number, guess_range, user_level)

main()
