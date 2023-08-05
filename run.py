import gspread
from google.oauth2.service_account import Credentials
import random
import os
import sys
import pandas as pd
import messages

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guess-the-number')

def update_worksheet(data, worksheet):
    '''
    Updates the worksheet in Google docs with the username and score.
    '''
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


def clear():
    '''
    Clears the terminal when needed when running the game.
    '''
    os.system('cls' if os.name == 'nt'else 'clear')


def show_instructions():
    '''
    Gives to users option to either view or skip instructions before playing.
    Includes a loop with try/except that raises error and 
    an if else to confirm user correct input, and a break 
    to stop showing instructions and run next function inside main().
    '''
    print('\nYou can view instructions or just start playing !')

    while True:
        instructions = input('\nEnter 1 to view instructions and 2 to skip it : \n')
        clear()

        try:
            instructions = int(instructions)
        except ValueError:
            print('\n')
            messages.game_name_ascii()
            print('\nNumbers only !')
            continue
        if instructions == 1:
            clear()
            messages.instructions_message()
            input('Press ENTER to play :\n')
            break
        elif instructions == 2:
            break
        else:
            print('\n')
            messages.game_name_ascii()
            print('\nNumber outside the allowed range > 1 or 2')


def user_level_choice():
    '''
    Shows to users available level options - easy, medium or hard and gets
    users' option to play with.
    Contains a try/except to validate users' input raises error showing 
    instructions when input is incorrect - either number out of range or not
    numbers.
    '''
    while True:
        game_level = input('\nEnter 1 for easy, 2  medium or, if you dare, 3 for hard leveL : \n')
        clear()

        try:
            game_level = int(game_level)
        except ValueError:
            print('\n')
            messages.game_name_ascii()
            print('\nNumbers only !')
            continue
        if 1 <= game_level <= 3:
            return game_level
        else:
            print('\n')
            messages.game_name_ascii()
            print('\nNumber outside the allowed range > 1 to 3 ')


def generate_random_number(user_level):
    '''
    Generates a random number, range is based on the user_level, 
    argument passed from user_level_choice. 
    Range is 30, 60 and 120. 
    '''
    if user_level == 1:
        guess_range = 30
    elif user_level == 2:
        guess_range = 60
    elif user_level == 3:
        guess_range = 120

    number = random.randint(1, guess_range)
    return number, guess_range


def user_guessed_number(guess_range, incorrect_guesses):
    '''
    Gets user guessed number using a try/except to validate 
    input, raises errors and shows message.
    Each round it also prints the tried numbers from game_loop.
    Uses arguments guess_range from generate_random_number and 
    incorrect_guesses from game_loop to print information for 
    each round.
    '''
    while True:
        user_input = input(f'\nGuess a number between 1 and {guess_range} :\n')
        clear()
        try:
            guess = int(user_input)
        except ValueError:
            clear()
            print('\n')
            messages.game_name_ascii()
            print(f'\nTried numbers : {incorrect_guesses}')
            print('\nNumbers only !')
            continue
        if 1 <= guess <= guess_range:
            clear()
            return guess
        else:
            clear()
            print('\n')
            messages.game_name_ascii()
            print(f'\nTried numbers : {incorrect_guesses}')
            print(f'\n{user_input} is outside the allowed range > 1 - {guess_range} ')


def play_again_or_exit():
    '''
    When the game ends, gives users option to either play again triggering
    main or exiting program.
    Validates input through try/except.
    '''
    while True:
        play_again = input('Press 1, if you want to start again or 2 to exit :\n')

        try:
            play_again = int(play_again)
        except ValueError:
            clear()
            print('\n')
            messages.game_name_ascii()
            print('\nNumbers 1 or 2 only !\n')
            continue
        if play_again == 1:
            main()
            break
        elif play_again == 2:
            clear()
            print('\n')
            messages.game_name_ascii()
            sys.exit("\nYou've left the game. Thank you for playing !")
        else:
            clear()
            print('\n')
            messages.game_name_ascii()
            print('\nInvalid number, only 1 or 2 are accepted ! \n')


def calculate_score(guesses_allowed, user_level):
    '''
    Calculates user score based on remaining allowed guesses and
    user selected level.
    Uses arguments guesses_allowed from game_loop and user_level 
    from user_level_choice.
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
    Gets user name or nickname to be logged to the game history and
    combines them passing to update_results.
    Uses a loop to get names with specific length. 
    '''
    while True:
        user_name = input('Please enter your name or nickname :\n')

        if len(user_name) <= 1 or len(user_name) >= 13:
            clear()
            print('\n')
            messages.game_name_ascii()
            print('\nName should be 2 to 12 characters .\n')
        else:
            update_results(user_name, score)
            return user_name


def update_results(user_name, score):
    '''
    Gets both user_name and score arguments and add them to a data list
    which is then pushed to the worksheet results through update_worksheet.
    '''
    data = [user_name, score]
    update_worksheet(data, 'results')
    display_results(user_name, score)


def display_results(user_name, score):
    '''
    Displays the results from top 5 players and current player.
    Gets data from worksheet and converts it into a data frame handled
    by Pandas library that sorts players list by score and displays top 5.
    Uses arguments user_name from pick_user_name and score from calculate_score
    to display current game play results.
    '''
    data = SHEET.worksheet('results').get_all_values()
    headers = data[0]
    rows = data[1:]

    df = pd.DataFrame(rows, columns=headers)
    df['Scores'] = pd.to_numeric(df['Scores'], errors='coerce')
    df = df[['Player', 'Scores']].sort_values(by='Scores', ascending=False)

    top_5 = df.head(5)

    clear()
    print('\n')
    messages.game_name_ascii()
    print(f'\n{user_name} , you scored {score} points, well done !\n')
    print('Check our all time top scorers ! \n')
    print(top_5.to_string(index=False) + '\n')
    play_again_or_exit()


def game_loop(number, guess_range, user_level):
    '''
    Runs the whole game.
    Gets random generated number and guess_range from generate_random_number,
    guess number, user_level from user_level_choice.
    Sets guesses_allowed to run the game.
    Checks if users still have guesses remaining, if guess has been tried already, 
    updates incorrect_guesses list to show guesses tried to user, checks if guesses
    match, and run conditionals to show hints to the users along the game.
    '''
    guesses_allowed = 10
    incorrect_guesses = []
    last_distance = -1

    while guesses_allowed > 0:
        guess = user_guessed_number(guess_range, incorrect_guesses)
        how_close_to_number = (number - guess)
        how_close_to_number = how_close_to_number.__abs__()

        if guess == number:
            clear()
            print('\n')
            messages.game_name_ascii()
            print(f"\n{guess} is your lucky number, you WIN ! \n")
            score = (calculate_score(guesses_allowed, user_level))
            pick_user_name(score)
            break
        else:
            if guess in incorrect_guesses:
                clear()
                print('\n')
                messages.game_name_ascii()
                print(f'\nTried numbers: {incorrect_guesses}')
                print('\nYou have tried this number already ! Try again .\n')
                continue
            else:
                guesses_allowed -= 1
                incorrect_guesses.append(guess)
                print('\n')
                messages.game_name_ascii()
                print(f'\nTried numbers: {incorrect_guesses}')
                if guesses_allowed == 0:
                    clear()
                    print('\n')
                    messages.game_name_ascii()
                    print(f"\nThe lucky number was {number} .")
                    print("\nYou lose! Wish you more luck next time .\n")
                else:
                    if how_close_to_number <=3 and last_distance == -1:
                        print(f"\nYou're BOILING !!! Remaining guesses {guesses_allowed}")
                    elif last_distance == -1:
                        if 3 < how_close_to_number <= 8:
                            print(f"\nYou're Hot !! Remaining guesses {guesses_allowed}")
                        elif 8 < how_close_to_number <= 15:
                            print(f"\nYou're Warm ! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number > 15:
                            print(f"\nYou're Cold . Remaining guesses {guesses_allowed}")
                    else:
                        if how_close_to_number < last_distance:
                            if how_close_to_number <= 3:
                                print(f"\nYou're HOTTER !! Remaining guesses {guesses_allowed}")
                            else:
                                print(f"\nYou're Warmer ! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number == last_distance:
                            print(f"\nArgh , neither hotter neither colder ! Remaining guesses {guesses_allowed}")
                        elif how_close_to_number > last_distance:
                            print(f"\nYou're Colder . Remaining guesses {guesses_allowed}")
                    last_distance = how_close_to_number
    else:
        play_again_or_exit()


def main():
    '''
    Runs the program outside game loop
    '''
    clear()
    print('\nWelcome to ...')
    messages.game_name_ascii()
    show_instructions()
    clear()
    print('\n')
    messages.game_name_ascii()
    user_level = user_level_choice()
    clear()
    number, guess_range = generate_random_number(user_level)
    print('\n')
    messages.game_name_ascii()
    game_loop(number, guess_range, user_level)

main()
