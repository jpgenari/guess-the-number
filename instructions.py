def instructions_message():
    '''
    Prints the game instructions to users when starting the
    program
    '''
    print(
        'The game objective is to guess the lucky number using the minimum\n'
        'number of guesses as possible as it will impact your score.\n'
        )
    print('> Instructions:')
    print('- Pick your level between easy, medium and hard level;')
    print('- For each level you will have 10 guesses available;')
    print(
        '- Easy -> lucky number between 1 and 30 with each guess\n'
        'worth 10 points;'
        )
    print(
        '- Medium -> lucky number between 1 and 60 with each guess\n'
        'worth 20 points;'
        )
    print(
        '- Hard -> lucky number between 1 and 120 with each guess worth\n'
        '40 points (each you level up, difficulty and points double);\n'
        )
    print('>> Hints:')
    print("* if Cold you're far from your number;")
    print("* if Warm you're not so far;")
    print("* if Hot you're close;")
    print("* if Boiling you're really really close;")
    print("* if Colder you're moving away from your number;")
    print("* if Warmer you're getting close;")
    print("* if Hotter you're getting really really close.\n")
