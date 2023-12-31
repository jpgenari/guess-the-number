'''
Import section
'''
import os
import sys
import random
from colorama import Fore, Style
from pyfiglet import Figlet
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import instructions

f = Figlet(font='small')

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guess-the-number')


def game_name_ascii():
    '''
    Prints game to users when needed.
    '''
    print(Fore.GREEN + f.renderText('Guess the Number!') + Style.RESET_ALL)


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


def validate_data(values):
    '''
    Validates if all user inputs are integers using a try/except to raise
    error and show the message.
    '''
    try:
        values = int(values)
    except ValueError:
        print('\n')
        game_name_ascii()
        print(f'\n{Fore.RED}Numbers only!{Style.RESET_ALL}')
        return False
    return True


def show_instructions():
    '''
    Gives to users option to either view or skip instructions before playing.
    Loop validates input with validate_data() an if else to confirm user
    correct input, and a break to stop showing instructions and run next
    function inside main().
    '''
    print('\nView instructions or start playing!')

    while True:
        see_instructions = input(
            '\nEnter 1 to view instructions and 2 to skip them:\n'
            )
        clear()
        if validate_data(see_instructions):
            if int(see_instructions) == 1:
                clear()
                instructions.instructions_message()
                input('Press ENTER to play:\n')
                break
            elif int(see_instructions) == 2:
                break
            else:
                print('\n')
                game_name_ascii()
                print(
                    f'{Fore.RED}\nNumber outside the allowed range > 1-2'
                    f'{Style.RESET_ALL}'
                    )


def user_level_choice():
    '''
    Shows to users available level options - easy, medium or hard and gets
    users' option to play with.
    Loop validates input with validate_data() an if else to confirm user
    correct input, returning game_level passed to main().
    '''
    while True:
        game_level = input(
            '\nEnter 1 for easy, 2  medium or, if you dare, 3 for hard level:'
            '\n'
            )
        clear()
        if validate_data(game_level):
            if 1 <= int(game_level) <= 3:
                return int(game_level)
            else:
                print('\n')
                game_name_ascii()
                print(
                    f'\n{Fore.RED}Number outside the allowed range > 1-3'
                    f'{Style.RESET_ALL}'
                    )


def generate_random_number(user_level):
    '''
    Generates random number, the range is based on the user_level,
    argument passed from user_level_choice().
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
    Gets user guessed number, uses a loop to validate input with
    validate_data() and if else to confirm user correct input, returning
    guess to main().
    Each round it also prints the tried numbers from game_loop, uses
    arguments guess_range from generate_random_number() and
    incorrect_guesses from game_loop() to print information for
    each round.
    '''
    while True:
        guess = input(f'\nGuess a number between 1 and {guess_range}:\n')
        clear()
        if validate_data(guess):
            print('\n')
            game_name_ascii()
            print(
                f'\nTried numbers: {Fore.YELLOW}{incorrect_guesses}'
                f'{Style.RESET_ALL}'
                )
            if 1 <= int(guess) <= guess_range:
                clear()
                return int(guess)
            else:
                clear()
                print('\n')
                game_name_ascii()
                print(
                    f'\nTried numbers: {Fore.YELLOW}{incorrect_guesses}'
                    f'{Style.RESET_ALL}'
                    )
                print(
                    f'\n{Fore.RED}{int(guess)} is outside the allowed range >'
                    f' 1-{guess_range}{Style.RESET_ALL}'
                    )
        else:
            print(
                f'\nTried numbers: {Fore.YELLOW}{incorrect_guesses}'
                f'{Style.RESET_ALL}'
                )


def play_again_or_exit():
    '''
    When the game ends, gives users option to either play again triggering
    main or exiting program.
    Loop validates input with validate_data() an if else to confirm user
    correct input, either triggering main() or exiting program.
    '''
    while True:
        play_again = input(
            '\nPress 1, if you want to start again or 2 to exit:\n'
            )
        clear()
        if validate_data(play_again):
            print('\n')
            game_name_ascii()
            if int(play_again) == 1:
                main()
                break
            elif int(play_again) == 2:
                clear()
                print('\n')
                game_name_ascii()
                sys.exit("\nYou've left the game. Thank you for playing!")
            else:
                clear()
                print('\n')
                game_name_ascii()
                print(
                    f'{Fore.RED}\nInvalid number, only 1 or 2 are accepted!'
                    f'{Style.RESET_ALL}'
                    )


def calculate_score(guesses_allowed, user_level):
    '''
    Calculates user score based on remaining allowed_guesses and
    user_level from main() and user_level_choice().
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
    combines them passing to update_results() using a loop to get names
    with specific length.
    '''
    while True:
        user_name = input('Please enter your name or nickname:\n')

        if len(user_name) <= 1 or len(user_name) >= 13:
            clear()
            print('\n')
            game_name_ascii()
            print(
                f'{Fore.RED}\nName should be 2 to 12 characters.\n'
                f'{Style.RESET_ALL}'
                )
        else:
            update_results(user_name, score)
            return user_name


def update_results(user_name, score):
    '''
    Gets both user_name and score arguments and add them to a data list
    which is then pushed to the worksheet results through update_worksheet().
    '''
    data = [user_name, score]
    update_worksheet(data, 'results')
    display_results(user_name, score)


def display_results(user_name, score):
    '''
    Displays the results from top 5 players and current player.
    Gets data from worksheet and converts it into a data frame handled
    by Pandas library that sorts players list by score and displays top 5.
    Uses arguments user_name and score from pick_user_name()
    and calculate_score() to display current game play results.
    '''
    data = SHEET.worksheet('results').get_all_values()
    headers = data[0]
    rows = data[1:]

    data_frame = pd.DataFrame(rows, columns=headers)
    data_frame['Scores'] = pd.to_numeric(data_frame['Scores'], errors='coerce')
    data_frame = data_frame[['Player', 'Scores']].sort_values(
        by='Scores', ascending=False
        )

    top_5 = data_frame.head(5)

    clear()
    print('\n')
    game_name_ascii()
    print(
        f'\n{Fore.GREEN}{user_name}{Style.RESET_ALL}, you scored {Fore.GREEN}'
        f'{score}{Style.RESET_ALL} points, well done!\n'
        )
    print('Check our all time top scorers!\n')
    print(top_5.to_string(index=False))
    play_again_or_exit()


def game_loop(number, guess_range, user_level):
    '''
    Runs the whole game.
    Gets number, guess_range, guess and user_level
    from generate_random_number(), user_guessed_number() and
    user_level_choice(). Sets guesses_allowed to run the game.
    Checks if users still have guesses remaining, if guess has been tried
    already, updates incorrect_guesses list to show guesses tried to user,
    checks if guesses match, and run conditionals to show hints to the users
    along the game.
    Triggers functions in the program workflow.
    '''
    guesses_allowed = 10
    incorrect_guesses = []
    last_distance = -1

    while guesses_allowed > 0:
        guess = user_guessed_number(guess_range, incorrect_guesses)
        how_close_to_number = number - guess
        how_close_to_number = abs(how_close_to_number)

        if guess == number:
            clear()
            print('\n')
            game_name_ascii()
            print(
                f"\n{Fore.GREEN}{guess}{Style.RESET_ALL} is your lucky number,"
                f" you {Fore.GREEN}WIN!{Style.RESET_ALL}\n"
                )
            score = calculate_score(guesses_allowed, user_level)
            pick_user_name(score)
            break
        else:
            if guess in incorrect_guesses:
                clear()
                print('\n')
                game_name_ascii()
                print(
                    f'\nTried numbers: {Fore.YELLOW}{incorrect_guesses}'
                    f'{Style.RESET_ALL}')
                print(
                    f'{Fore.RED}\nYou have tried this number already! Try '
                    f'again.{Style.RESET_ALL}'
                    )
                continue
            else:
                guesses_allowed -= 1
                incorrect_guesses.append(guess)
                print('\n')
                game_name_ascii()
                print(
                    f'\nTried numbers: {Fore.YELLOW}{incorrect_guesses}'
                    f'{Style.RESET_ALL}'
                    )
                if guesses_allowed == 0:
                    clear()
                    print('\n')
                    game_name_ascii()
                    print(
                        f"\nThe lucky number was {Fore.YELLOW}{number}"
                        f"{Style.RESET_ALL}."
                        )
                    print("\nYou lose! Wish you more luck next time.")
                else:
                    if how_close_to_number <= 3 and last_distance == -1:
                        print(
                            "\nYou're BOILING!!! Remaining guesses "
                            f"{Fore.YELLOW}{guesses_allowed}{Style.RESET_ALL}"
                            )
                    elif last_distance == -1:
                        if 3 < how_close_to_number <= 8:
                            print(
                                "\nYou're Hot!! Remaining guesses "
                                f"{Fore.YELLOW}{guesses_allowed}"
                                f"{Style.RESET_ALL}"
                                )
                        elif 8 < how_close_to_number <= 15:
                            print(
                                "\nYou're Warm! Remaining guesses "
                                f"{Fore.YELLOW}{guesses_allowed}"
                                f"{Style.RESET_ALL}"
                                )
                        elif how_close_to_number > 15:
                            print(
                                "\nYou're Cold. Remaining guesses "
                                f"{Fore.YELLOW}{guesses_allowed}"
                                f"{Style.RESET_ALL}"
                                )
                    else:
                        if how_close_to_number < last_distance:
                            if how_close_to_number <= 3:
                                print(
                                    "\nYou're HOTTER!! Remaining guesses "
                                    f"{Fore.YELLOW}{guesses_allowed}"
                                    f"{Style.RESET_ALL}"
                                    )
                            else:
                                print(
                                    "\nYou're Warmer! Remaining guesses "
                                    f"{Fore.YELLOW}{guesses_allowed}"
                                    f"{Style.RESET_ALL}"
                                    )
                        elif how_close_to_number == last_distance:
                            print(
                                "\nOops, neither hotter neither colder! "
                                f"{Fore.YELLOW}{guesses_allowed}"
                                f"{Style.RESET_ALL}"
                                )
                        elif how_close_to_number > last_distance:
                            print(
                                "\nYou're Colder. Remaining guesses "
                                f"{Fore.YELLOW}{guesses_allowed}"
                                f"{Style.RESET_ALL}"
                                )
                    last_distance = how_close_to_number
    else:
        play_again_or_exit()


def main():
    '''
    Runs the program outside game loop
    '''
    clear()
    print('\nWelcome to ...')
    game_name_ascii()
    show_instructions()
    clear()
    print('\n')
    game_name_ascii()
    user_level = user_level_choice()
    clear()
    number, guess_range = generate_random_number(user_level)
    print('\n')
    game_name_ascii()
    game_loop(number, guess_range, user_level)


main()
