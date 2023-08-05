def game_name_ascii():
    '''
    Prints the welcome message to users when starting the 
    program
    '''
    game_name_art = '''
   ___                       _   _                __                 _                _ 
  / _ \\_   _  ___  ___ ___  | |_| |__   ___    /\\ \\ \\_   _ _ __ ___ | |__   ___ _ __ / \\
 / /_\\/ | | |/ _ \\/ __/ __| | __| '_ \\ / _ \\  /  \\/ / | | | '_ ` _ \\| '_ \\ / _ \\ '__/  /
/ /_\\\\| |_| |  __/\\__ \\__ \\ | |_| | | |  __/ / /\\  /| |_| | | | | | | |_) |  __/ | /\\_/ 
\\____/ \\__,_|\\___||___/___/  \\__|_| |_|\\___| \\_\\ \\/  \\__,_|_| |_| |_|_.__/ \\___|_| \\/   
'''
    print(game_name_art)


def instructions_message():
    '''
    Prints the game instructions to users when starting the 
    program
    '''
    print('\n')
    game_name_ascii()
    print('''\nThe game objective is to guess the lucky number using the minimum number of guesses
as possible as it will impact your score.\n''')
    print('> Instructions:\n')
    print('- Pick your level between easy, medium and hard level')
    print('- For each level you will have 10 guesses available')
    print('- Easy gives you a lucky number between 1 and 30 with each guess worth 10 points')
    print('- Medium gives you a lucky number between 1 and 60 with each guess worth 20 points')
    print('- Hard gives you a lucky number between 1 and 120 with each guess worth 40 points')
    print('(each time you level up, difficulty and points double)\n')
    print('>> Hints:\n')
    print("* if Cold you're far from your number")
    print("* if Warm you're not so far")
    print("* if Hot you're close")
    print("* if Boiling you're really really close")
    print("* if Colder you're moving away from your number")
    print("* if Warmer you're getting close")
    print("* if Hotter you're getting really really close\n")
    print("Good Luck!")