def game_name():
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
    print()
    print('Guess the hidden number!!')
    print()
    print('The game objective is to guess the lucky number using')
    print('the minimum number of guesses as possible as this will')
    print('determine you final score.')
    print()
    print()
    print('- You can select between an easy and a hard level;')
    print('- For each level you will have 10 guesses available;')
    print('- In the easy level the lucky number will be between 1 to 30')
    print('and each guess is worth 4 points;')
    print('- In the hard level the lucky number will be between 1 to 60')
    print('and each guess is worth 8 points, double the difficulty,')
    print('double the points.')
    print()
    print('Good look!')
    print()
