# Guess the Number

**Guess the Number** is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

In this game, users will be challenged find a random generate number. In each game play users get 10 "guesses", allowing to try up to 10 numbers. The random number is generated in a range based on the difficulty level selected by users (easy, medium and hard). After each try, the game throws a hint in order to help finding the number and the already tried numbers are displayed as a guide.

The game works well as an alternative for a quick game play, adding some elements to challenge the users such as calling generated number as their "lucky number" and funny hints as the game runs.

Link to live game: [Guess the Number](https://guess-the-number-p3-31510f7a135e.herokuapp.com/)

![Responsive Mockup](/assets/images/readme-am-i-responsive.png)
View it on [Am I responsive?](https://ui.dev/amiresponsive?url=https://guess-the-number-p3-31510f7a135e.herokuapp.com/)

## TABLE OF CONTENTS

+ [FEATURES](#features "Features")
  + [Landing page](#landing-page "Landing page")
  + [Welcome & view instructions](#welcome--view-instructions "Welcome & view instructions")
  + [Instructions](#instructions "Instructions")
  + [Game level](#game-level "Game level")
  + [Guessing the number](#guessing-the-number "Guessing the number")
  + [Ending the game](#ending-the-game "Ending the game")
  + [Displaying results](#displaying-results "Displaying results")
  + [UI](#ui "UI")
  + [Features Left to Implement or Future Features](#features-left-to-implement-or-future-features "Features Left to Implement or Future Features")
+ [USER STORIES](#user-stories "USER STORIES")
+ [DATA SCHEMA](#data-schema "DATA SCHEMA")
+ [TESTING](#testing "TESTING")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Testing as a Table](#testing-as-a-table "Testing as a Table")
+ [BUGS](#bugs "BUGS")
  + [Solved bugs](#solved-bugs "Solved bugs")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [TOOLS AND TECHNOLOGIES](#tools-and-technologies "TOOLS AND TECHNOLOGIES")
  + [Languages](#languages "Languages")
  + [Python Libraries and Modules](#python-libraries-and-modules "Python Libraries and Modules")
  + [Tools](#tools "Tools")
  + [Database](#database "Database")
+ [DEVELOPMENT & DEPLOYMENT](#development--deployment "DEVELOPMENT & DEPLOYMENT")
  + [Connecting Google Sheets with Python](#connecting-google-sheets-with-python "Connecting Google Sheets with Python")
  + [Deploying on Heroku](#deploying-on-heroku "Deploying on Heroku")
+ [CREDITS](#credits "CREDITS")
  +[Content](#content "Content")
  +[Acknowledgement](#acknowledgement "Acknowledgement")
  

## FEATURES

### Landing page

+ Opens a blank page showing a python terminal following Code Institute mock terminal on Heroku. The whole game runs inside the Python terminal.
  
  ![Landing](/assets/images/readme-landing.png)

### Welcome & view instructions

+ The initial displayed screen on terminal displays the **welcome message** with **game name** and option to either view or skip **instructions**.
+ Welcome message and game name welcomes users to the game display its name using stylishly font and green color - the game name is displayed at the top of every screen except for instructions screen to reinforce game identity.
+ View or skip instructions asks users to either view or skip instructions - this option is given as returning players might not be interested in seeing the instructions again. Users need to enter a number to submit their option - 1 view instructions and 2 skip them, when entering different input an error message is displayed accordingly.
  
  ![Welcome and view instructions](/assets/images/readme-welcome-instructions.png)

### Instructions

+ If user opts to view instructions, they will be displayed on a new screen on the terminal containing instructions about the game and its hints - for the hints, they are based on the distance between tried numbers and number.
+ Upon pressing enter, users leave instructions and are led to next screen.
  
  ![Instructions](/assets/images/readme-instructions.png)

### Game level

+ After leaving instructions or just skipping them initially, users are led to game level selection screen. Here they are asked to select which level they want to play with.
+ The game offers 3 levels: easy, medium and hard level with details explained in the instructions. In order to select a level, users need to input between 1 to 3 when entering different input an error message will be displayed accordingly. The text will show a challenging message to engage with users, to play the hard level.
  
  ![Game level](/assets/images/readme-game-level.png)

### Guessing the number

+ After selecting a level, user is led to next screen where users are asked to guess a number between 1 and ending with the maximum number range based on the game level - easy 1 to 30, medium 1 to 60 and hard 1 to 120.
+ When entering a number, users are given a feedback, with a list of tried numbers and a hint based on how far tried number is from number. After second tried number and onwards, each tried number is added to the displayed list of tried numbers and a new hint is given based on previous tried number - if closer or further away from number.
+ The numbers inside the tried numbers list and number of remaining guesses are displayed in yellow for users awareness.
+ Only numbers, and inside the range for the selected level are accepted, when trying to input either a non-number or number outside range, an error message will be displayed accordingly. Also, if users try to input a number already tried, an error message is displayed and the without affecting remaining guesses.
  
  ![Guessing the number 1](/assets/images/readme-guessing-number-1.png)
  ![Guessing the number 2](/assets/images/readme-guessing-number-2.png)

### Ending the game

+ Game ends when either users guess the number within given allowed guesses - 10 in total - or when the allowed guesses run out. For scenarios users are led to the following screens.

#### Winner

+ Guessing correct number triggers winning screen, which displays correct number - which is the "lucky number" - and "WIN" message printed in the same green as game name, to associate game branding with victory. Then a prompt asking users to enter name or nickname.
+ The name/username is asked after the game is played as way to focus on the game play. Also, for privacy reasons users may input any data inside allowed range of 2 to 12 characters, even blank spaces, in order to not disclose their identity. This information is used to fill game database with user - even if not disclosed - and score. When trying to enter username outside allowed range, an error message is displayed accordingly.
  
  ![Ending the game 1](/assets/images/readme-ending-game-1.png)

#### Not winner

+ Running out of guesses before guessing correct number results in losing the game.
+ This scenario display to users which was the correct number, or the "lucky number" printed in yellow for awareness followed by a message wishing more lucky for next game play and a prompt asking users if they want to start again or exit the game.
+ Start again option restarts the game while second will end the program showing a message thanking users for playing. Users need to input 1 or 2 and when entering different input, an error message will be displayed accordingly.
  
  ![Ending the game 2](/assets/images/readme-ending-game-2.png)
  ![Ending the game 3](/assets/images/readme-ending-game-3.png)

### Displaying results

+ When users are winners, following the details above, after entering name/nickname, they are led the displaying results screen.
+ In this screen the input name/nickname will be displayed printed in the same green from game name and "WIN" statement from previous screen, along side the score points and a congratulating message.
+ Below users name/nickname and score, it is displayed an all time game ranking containing the top 5 scorers of all time, ordered by the highest to lowest - in case of same numbers of points, older result displayed first.
+ Finally, the same prompt displayed for the not winner scenario asks users if they want to start again or exit the game. Starting again restarts game while exiting exits the program throwing the same thank you for playing message. Here, users need to input 1 or 2 and when entering different input, an error message will be displayed accordingly.
  
  ![Displaying results](/assets/images/readme-displaying-results.png)
  ![Ending the game 3](/assets/images/readme-ending-game-3.png)

### UI

#### Text color

+ As describe above, the game UI uses text in different colors other than basic terminal white. **Green** is used for positive feedback, such as winner results and game and **yellow** is used for awareness, showing tried numbers, remaining guesses and "lucky number" in a not winner scenario. **Red** is the third color being used for attention, hence, only displayed in the error messages.

  ![Error message 1](/assets/images/readme-error-1.png)
  ![Error message 1](/assets/images/readme-error-2.png)

#### Dynamic terminal UI

+ To improve user experience in the game, its UI works by cleaning the terminal completely after each input to bring users the impression of new screens being displayed each time.
  
  ![Dynamic terminal](/assets/images/readme-terminal-ui.gif)

### Features Left to Implement or Future Features

+ Include additional game levels to provide more options when playing the game.
+ Update display results feature to display ranked results split by game level, eg: top 5 easy, top 5 medium and top 5 hard.

[Back to top](#guess-the-number "Back to top")

## USER STORIES

Considering this project scope and design, as for user stories we contain only **user** who is the player of the game.

+ As a **user** I want to either **view the game instructions** so I can **understand how to play the game and its rules** or to **skip and play directly, as I am returning player and know how to play**.
+ As a **user** I want to **select a game level** that best suits me, either **being easy and relaxing or hard and challenging**.
+ As a **user** I want to be able to **view hints that help me find the "lucky" number** and **view numbers I have tried already** allowing me to **get the correct number and win the game**.
+ As a **user** I want to either **add my name or nickname** to be displayed in the game score board results to **log my results to display how I performed** or **to leave without adding any info about myself**.
+ As a **user** I want to be given the option to either **continue playing** or to **leave the game**.

[Back to top](#guess-the-number "Back to top")

## DATA SCHEMA

Flowchart created on [Lucidchart](https://www.lucidchart.com/pages/) displaying main user inputs and code output (actions). Validating data not including for better visual result, all user inputs pass through data validation to avoid program crashing.
![Flowchart](/assets/images/readme-flowchart.png)
View it on [Lucidchart](https://lucid.app/lucidchart/a2deff5c-9110-4e4d-b0c0-5145f1b1c9d0/edit?viewport_loc=-235%2C-65%2C3072%2C1504%2C0_0&invitationId=inv_04534744-09ec-48c2-9c81-e9cb23670608), login required.

[Back to top](#guess-the-number "Back to top")

## TESTING

** *The game should not work on mobile as it runs inside Code Institute mock terminal on Heroku. No accessibility or responsivity testing was applied as therefore, they are not needed.* **

### Validator Testing

Python code has been tested and validated with [CI Python Linter](https://pep8ci.herokuapp.com/) and all errors have been removed from code.

+ **run.py**

  ![run.py](/assets/images/readme-validator-run-py.png)

+ **instructions.py**

  ![run.py](/assets/images/readme-validator-instructions-py.png)

### Testing as a Table

**INPUT**|**ACTION**|**EXPECTED**|**RESULT**
----------|----------|----------|----------
Enter 1 to view instructions and 2 to skip them:|User inputs integer 1 + press Enter|Moves to instructions screen|Works as expected
||User inputs integer 2 + press Enter|Skips instructions and moves to select level|Works as expected
||User inputs anything other than integer + press Enter|Displays message: "Numbers only!"|Works as expected
||User inputs any integer other than 1 or 2 + press Enter|Displays message: "Number outside the allowed range > 1-2"|Works as expected
Press ENTER to play:|User press Enter|Moves to select level|Works as expected
||User inputs anything + press Enter|Moves to select level|Works as expected
Enter 1 for easy, 2  medium or, if you dare, 3 for hard level:|User inputs integer 1 + press Enter|Starts the game with easy level selected|Works as expected
||User inputs integer 2 + press Enter|Starts the game with medium level selected|Works as expected
||User inputs integer 3 + press Enter|Starts the game with hard level selected|Works as expected
||User inputs anything other than integer + press Enter|Displays message: "Numbers only!"|Works as expected
||User inputs any integer other than 1, 2 or 3 + press Enter|Displays message: "Number outside the allowed range > 1-3"|Works as expected
Guess a number between 1 and 30:|User inputs integer between 1 and 30 + press Enter|If input = generated number:|
|||displays generated number + communicates WIN result to user + prompts user to enter a name or nickname|Works as expected
|||If input $\neq$ generated number and remaining guesses = 0:|
|||displays generated number + communicates LOSE result to user + prompts option to start again or exit|Works as expected
|||If input $\neq$ generated number and remaining guesses > 0 and not inside tried numbers: []:|
|||adds input to tried numbers: [],|
|||subtracts 1 guess from remaining guessed,|
|||displays tried numbers: [] + hint + remaining guesses|Works as expected
|||If input $\neq$ generated number and remaining guesses > 0 and inside tried numbers: []:|
|||displays "You have tried this number already! Try again.",|
|||ignores input|Works as expected
||User inputs anything other than integer + press Enter|Displays message: "Numbers only!"|Works as expected
||User inputs any integer not between 1 and game level range + press Enter|Displays message: "{integer} is outside the allowed range > 1-{game level range}"|Works as expected
Please enter your name or nickname:|User inputs anything between 2 and 12 characters length (including blank spaces) + press Enter|Moves to display results screen|Works as expected
||User inputs anything outside range between 2 and 12 characters length + press Enter|Moves to display results screen|Works as expected
Press 1, if you want to start again or 2 to exit:|User inputs integer 1 + press Enter|Restarts the game|Works as expected
||User inputs integer 2 + press Enter|Exits the game + displays message "You've left the game. Thank you for playing!"|Works as expected
||User inputs anything other than integer + press Enter|Displays message: "Numbers only!"|Works as expected
||User inputs any integer other than 1 or 2 + press Enter|Displays message: "Number outside the allowed range > 1-2"|Works as expected

Application did not break not matter inputs added and correct errors were displayed.

[Back to top](#guess-the-number "Back to top")

## BUGS

### Solved bugs

+ Display_results() function not working properly with scores >= 100 and more than 16 rows of data

  + This function reads the game data base (worksheet) and uses Pandas library to create a data frame with DataFrame() using columns and rows as parameters and then use sort.values() function to sort the results based on 'Scores' column from highest to lowest, filtering the top 5 results with top() function. After that, it  prints the data frame to the terminal as results.
  + When running tests on the game, it was noticed 2 issues: 1. when the scores where equal to 100 or higher (and integer with 3 digits or more), the row with these values were ignored by the sort.values() function; 2. when the worksheet contained 16 or more rows, the sort.values() stopped working as expected, always adding most recent result to the top 5, with higher scored being displayed after.
  + The bug was solved by adding the function to_numeric() to guarantee all results from column were converted into integers before being sorted.
  + Code example with bug:

    ```
    def display_results(user_name, score):
        data = SHEET.worksheet('results').get_all_values()
        headers = data[0]
        rows = data[1:]

        data_frame = pd.DataFrame(rows, columns=headers)
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
    ```
  + This string was added before sort.values() function to fix the bug:
    ```
    data_frame['Scores'] = pd.to_numeric(data_frame['Scores'], errors='coerce')
    ```

+ Deployment error after implementing **colorama** and **pyfiglet**

  + **colorama** and **pyfiglet** where implemented into the code in final development stage to import *Fore* and *Style* (from first one) and *Figlet* (from second one) in order to add color to the game text and styling to the game name respectively.
  + After the implementation, the command *Pip3 freeze > requirements.txt* was run to the terminal in order to update the file with requirements for Heroku deployment. After deployment, when trying to run the game, an error was returning in the terminal line 7, with **colorama** not found crashing the application. Upon the error, requirements.txt file was inspected where both **colorama** and **pyfiglet** where not found.
  + Upon some online research, a possible reason for the issue could be these libraries not installed (the project is developed using VS Code as IDE, running locally to avoid disruptions from online IDEs). Using *pip* commands in the terminal it was confirmed both libraries were installed, and, still, requirements.txt was not being updated as expected.
  + Some more research was made and the possible issue was pointed to the current installed libraries not being fully compatible with IDE with the application was running perfectly in terminals, both VS Code terminal and Mac OS terminal, however, requirements were not being updated.
  + In order to solve the bug and deploy a runnable application, the solution applied was to manually add the requirements to the requirements.txt using currently libraries version installed. Using pip commands to install libraries it was confirmed installation along side version, which were added to the requirements.txt file.
  ```
  pyfiglet==0.8.post1
  colorama==0.4.6
  ```

  ![Terminal](/assets/images/readme-terminal.png)

### Unfixed Bugs

There are no unfixed bugs.

[Back to top](#guess-the-number "Back to top")

## TOOLS AND TECHNOLOGIES

### Languages

+ [Python](https://www.python.org/) - backend programming language

### Python Libraries and Modules

+ [os](https://docs.python.org/3/library/os.html) - used to clear the terminal within clear() function
+ [sys](https://docs.python.org/3/library/sys.html) - used to exit exit the program within play_again_or_exit() function
+ [random](https://docs.python.org/3/library/random.html) - used to generate random number to be guessed in the game within generate_random_number() function
+ [colorama](https://pypi.org/project/colorama/) - used to apply color to the game running in the terminal, used across the code
+ [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - used to add font style to the game name within game_name_ascii() function
+ [pandas](https://pandas.pydata.org/) - used within display_results() function to created, sort and display a data frame with game ranked results
+ [gspread](https://docs.gspread.org/en/v5.10.0/) and [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/index.html) - used to access and manipulate worksheet inside Google Spreadsheets to store and read data frame with game results

### Tools

+ [GitHub](https://github.com/) - used store the code online and deployment
+ [Heroku](https://www.heroku.com/) - cloud platform used to deploy and run application inside Code Institute mock terminal
+ [EZGIF.COM](https://ezgif.com/) - tool used to generate gif added to the README doc to display UI functionality
+ [VS Code](https://code.visualstudio.com/) - IDE used to write, edit the code and run git via terminal
+ [git](https://git-scm.com/) - used for version control through terminal commands *git add .* to add files ready to commit, *git commit -m "description"* to commit the code to repository ready to be pushed and *git push* used to push committed code to GitHub
+ [Lucidchart](https://www.lucidchart.com/pages/) - used to create program flowchart

### Database

+ [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk) - used to access Google Drive to link with application
+ [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts) - used to read and modify spreadsheet data with the application
+ [Google Drive](https://www.google.com/drive/) - used to store the file containing the data base on the cloud
+ [Google Sheets](https://www.google.com/sheets/about/) - used to store and handle the data base

## DEVELOPMENT & DEPLOYMENT

+ Application is a terminal based game written in Python, running in the Code Institute mock terminal template from [python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template).
+ The live application is deployed using Heroku and can be accessed [here](https://guess-the-number-p3-31510f7a135e.herokuapp.com/).

### Connecting Google Sheets with Python

+ Steps to connect Python to Google Sheets - used in development stage:
  + Sign in or create a [Google Account](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AXo7B7WsDhqcpaon49aRS2jMza1LPi7mXD7Mkj33SCOGJ5qL7NMLdgrhxg12s8ZG2haHibcGP6Jv&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-83235363%3A1691449447247998);
  + Create a spreadsheet in Google Sheets and add needed data (columns "Player"and "Scores" and rows) needed in the application and name it "guess-the-number";
  + Open [Google Cloud Platform](https://console.cloud.google.com/) and make sure to select Google Account you wish to use;
  + Click "Select a project" > click "NEW PROJECT";
  + Name project "GuessTheNumber" > click "CREATE";
  + When the project is created, click "SELECT PROJECT";
  + On the left side menu, click "APIs and services" > click on "Library";
  + Search and enable APIs Google Drive, when enabled it will lead to API dashboard;
  + Click "CREATE CREDENTIALS" > in "Select an API*", Google Drive API should be pre-selected otherwise select it;
  + Toggle "Application Data" > toggle "No, I'm not using them > click "NEXT";
  + In "Service account name" add the account name > click "CREATE AND CONTINUE";
  + In the dropdown menu "Select a role" > select "Basic" and "Editor" > click "CONTINUE";
  + Leave following options in blank > click "DONE"
  + On the lef side menu, click "Credentials" > on "Service Accounts" click on the service account created;
  + On the next page, click on "KEYS" > click on dropdown menu "ADD KEY" and select "Create new key" > select "JSON" key type > click "CREATE" - this should prompt the credentials file to download to your computer;
  + Search and enable APIs Google Drive;
  + Go to the application repository and upload the downloaded credentials file - recommended to update its name to a more readable name, such as "creds.json";
  + Open the json file with the credentials, look for and copy the "client_email" value;
  + Open the created spreadsheet in Google Sheets > click "Share" button and add copied client email giving editor permission and deselecting "Notify people" option;
  + **creds.json contains sensitive information, hence, take measures to prevent it to be committed to GitHub (such as .gitignore file) in order to keep information safe**;
  + Add libraries `google-auth` and `gspread` to the project using *pip install* and import them to the Python file where the code is placed;
  + Setup the SCOPE, CREDS, SCOPED_CREDS, GSPREAD_CLIENT and SHEET following [love-sandwiches-p5-sourcecode](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/blob/master/01-getting-set-up/02-connecting-oto-our-api-with-python/run.py) and finish integration between Python and Google Sheets.

### Deploying on Heroku

+ Steps to deploy project on Heroku - valid for the Code Institute [python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template):
  + For the code to work properly in the provided template, before deployment it is necessary to add `\n` method, so the inputs can be captured;
  + Create the list of dependencies required to be installed by Heroku when deploying adding it to the "requirements.txt" file using terminal command *Pip3 freeze > requirements.txt**;
  + Go to [Heroku](https://heroku.com/) and sign in to the account or create a free an account if necessary;
  + From Heroku's dashboard > click on dropdown button "New" and select "Create new app";
  + Inside "App name" add the unique name "guess-the-number-p3" for the app and under "Choose a region" select "Europe" > click "Create app";
  + On the top menu, click "Settings" tab;
  + On the next page, scroll down to "Config Vars" > click "Reveal Config Vars";
  + Inside box, replace "KEY" with "CREDS", go to the "creds.json" file, copy the entire file and paste it inside the box replacing "VALUE" > click "Add";
  + On the second pair of boxes, replace "KEY" for "PORT" and "VALUE" for "8888";
  + Scroll down to "Buildpacks" > click "Add buildpack";
  + On the new box, first select "python" > click "Add Buildpack", repeat this action but selecting "node.js" this time;
  + Make sure the buildpacks are in the correct correct order, with python coming first at the top - if needed they can be arranged by dragging and dropping;
  + Go to "Deploy" tab through the top menu > "Deployment method" select "GitHub" > click "Connect to GitHub" to connect Heroku to [GitHub](https://github.com/) account;
  + On "Connect to GitHub" search for the repository name "guess-the-number" > click "Search" > click "Connect" to connect to the repository;
  + On first deployment, scroll down to "Manual deploy" > click "Deploy Branch" which allows to view logs when App is built;
  + After first deployment, enable "Enable Automatic Deploys" to keep App up to date after each push.

[Back to top](#guess-the-number "Back to top")

## CREDITS

### Content

+ Game code and README inspired/taken by [Hangman](https://github.com/AsiaWi/hangman/tree/main) project - game layout, structure and styling.
+ Game code inspired/taken by [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) project - how to connect with Google Sheets and use of try/except to validate data.
+ Guess the number game basic code inspired/taken by [How to Create a Number Guessing Game in Python](https://www.makeuseof.com/number-guessing-game-using-python/).
+ Create a game data base and README inspired by [Dad Jokes](https://github.com/Pelikantapeten/p3-dad-jokes/tree/main) - idea for implementing interactive data base.
+ README build with support of [readmes.md](https://github.com/CluelessBiker/mentoring/blob/main/readmes.md) provide by mentor;
+ Solution to implement dynamic hints implemented in game_loop() function taken from [answer](https://stackoverflow.com/a/57046054/21121456) on [Stack Overflow](https://stackoverflow.com/questions/57045410/python-guessing-game-with-clues).
+ Solutions applied to display_results() function - Pandas library and *__ abs __()* taken from:
  + [Methods for Ranking in Pandas](https://www.stratascratch.com/blog/methods-for-ranking-in-pandas/#:~:text=To%20summarize%2C%20rankings%20in%20Pandas,tied%20group%20is%20also%20used);
  + [Get First N Rows of Pandas DataFrame](https://sparkbyexamples.com/pandas/get-first-n-rows-of-pandas/#:~:text=If%20the%20argument%20is%20not,and%20columns%20by%20position%2Findex);
  + [How to print Dataframe in Python without Index?](https://www.geeksforgeeks.org/how-to-print-dataframe-in-python-without-index/);
  + [Python Absolute Value – Python abs Tutorial](https://www.freecodecamp.org/news/python-absolute-value-python-abs-tutorial/#:~:text=The%20abs()%20built%2Din,zero%20on%20the%20number%20line);
  + [Pandas Sort Values Tutorial](https://www.datacamp.com/tutorial/pandas-sort-values).
+ Debugging performed with support of [ChatGPT](https://chat.openai.com/).

### Acknowledgement

+ [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/) for great support throughout the development process, providing insightful ideas and feedback.

[Back to top](#guess-the-number "Back to top")