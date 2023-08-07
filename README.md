# Guess the Number

**Guess the Number** is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

In this game, users will be challenged find a random generate number. In each game play users get 10 "guesses", allowing to try up to 10 numbers. The random number is generated in a range based on the difficulty level selected by users (easy, medium and hard). After each try, the game throws a hint in order to help finding the number and the already tried numbers are displayed as a guide.

The game works well as an alternative for a quick game play, adding some elements to challenge the users such as calling generated number as their "lucky number" and funny hints as the game runs.

Link to live game: [Guess the Number](https://guess-the-number-p3-31510f7a135e.herokuapp.com/)

![Responsive Mockup](/assets/images/readme-am-i-responsive.png)

## FEATURES

### Landing page

- Opens a blank page showing a python terminal following Code Institute mock terminal on Heroku. The whole game runs inside the Python terminal.
  
  ![Landing](/assets/images/readme-landing.png)

### Welcome & view instructions

- The initial displayed screen on terminal displays the **welcome message** with **game name** and option to either view or skip **instructions**.
- Welcome message and game name welcomes users to the game display its name using stylishly font and green color - the game name is displayed at the top of every screen except for instructions screen to reinforce game identity.
- View or skip instructions asks users to either view or skip instructions - this option is given as returning players might not be interested in seeing the instructions again. Users need to enter a number to submit their option - 1 view instructions and 2 skip them, when entering different input an error message is displayed accordingly.
  
  ![Welcome and view instructions](/assets/images/readme-welcome-instructions.png)

### Instructions

- If user opts to view instructions, they will be displayed on a new screen on the terminal containing instructions about the game and its hints - for the hints, they are based on the distance between tried numbers and number.
- Upon pressing enter, users leave instructions and are led to next screen.
  
  ![Instructions](/assets/images/readme-instructions.png)

### Game level

- After leaving instructions or just skipping them initially, users are led to game level selection screen. Here they are asked to select which level they want to play with.
- The game offers 3 levels: easy, medium and hard level with details explained in the instructions. In order to select a level, users need to input between 1 to 3 when entering different input an error message will be displayed accordingly. The text will show a challenging message to engage with users, to play the hard level.
  
  ![Game level](/assets/images/readme-game-level.png)

### Guessing the number

- After selecting a level, user is led to next screen where users are asked to guess a number between 1 and ending with the maximum number range based on the game level - easy 1 to 30, medium 1 to 60 and hard 1 to 120.
- When entering a number, users are given a feedback, with a list of tried numbers and a hint based on how far tried number is from number. After second tried number and onwards, each tried number is added to the displayed list of tried numbers and a new hint is given based on previous tried number - if closer or further away from number.
- The numbers inside the tried numbers list and number of remaining guesses are displayed in yellow for users awareness.
- Only numbers, and inside the range for the selected level are accepted, when trying to input either a non-number or number outside range, an error message will be displayed accordingly. Also, if users try to input a number already tried, an error message is displayed and the without affecting remaining guesses.
  
  ![Guessing the number 1](/assets/images/readme-guessing-number-1.png)
  ![Guessing the number 2](/assets/images/readme-guessing-number-2.png)

### Ending the game

- Game ends when either users guess the number within given allowed guesses - 10 in total - or when the allowed guesses run out. For scenarios users are led to the following screens.

#### Winner

- Guessing correct number triggers winning screen, which displays correct number - which is the "lucky number" - and "WIN" message printed in the same green as game name, to associate game branding with victory. Then a prompt asking users to enter name or nickname.
- The name/username is asked after the game is played as way to focus on the game play. Also, for privacy reasons users may input any data inside allowed range of 2 to 12 characters, even blank spaces, in order to not disclose their identity. This information is used to fill game database with user - even if not disclosed - and score. When trying to enter username outside allowed range, an error message is displayed accordingly.
  
  ![Ending the game 1](/assets/images/readme-ending-game-1.png)

#### Not winner

- Running out of guesses before guessing correct number results in losing the game.
- This scenario display to users which was the correct number, or the "lucky number" printed in yellow for awareness followed by a message wishing more lucky for next game play and a prompt asking users if they want to start again or exit the game.
- Start again option restarts the game while second will end the program showing a message thanking users for playing. Users need to input 1 or 2 and when entering different input, an error message will be displayed accordingly.
  
  ![Ending the game 2](/assets/images/readme-ending-game-2.png)
  ![Ending the game 3](/assets/images/readme-ending-game-3.png)

### Displaying results

- When users are winners, following the details above, after entering name/nickname, they are led the displaying results screen.
- In this screen the input name/nickname will be displayed printed in the same green from game name and "WIN" statement from previous screen, along side the score points and a congratulating message.
- Below users name/nickname and score, it is displayed an all time game ranking containing the top 5 scorers of all time, ordered by the highest to lowest - in case of same numbers of points, older result displayed first.
- Finally, the same prompt displayed for the not winner scenario asks users if they want to start again or exit the game. Starting again restarts game while exiting exits the program throwing the same thank you for playing message. Here, users need to input 1 or 2 and when entering different input, an error message will be displayed accordingly.
  
  ![Displaying results](/assets/images/readme-displaying-results.png)
  ![Ending the game 3](/assets/images/readme-ending-game-3.png)

### UI

#### Text color

- As describe above, the game UI uses text in different colors other than basic terminal white. **Green** is used for positive feedback, such as winner results and game and **yellow** is used for awareness, showing tried numbers, remaining guesses and "lucky number" in a not winner scenario. **Red** is the third color being used for attention, hence, only displayed in the error messages.

  ![Error message 1](/assets/images/readme-error-1.png)
  ![Error message 1](/assets/images/readme-error-2.png)

#### Dynamic terminal UI

- To improve user experience in the game, its UI works by cleaning the terminal completely after each input to bring users the impression of new screens being displayed each time.
  
  ![Dynamic terminal](/assets/images/readme-terminal-ui.gif)

## Features Left to Implement or Future Features

- Include additional game levels to provide more options when playing the game.
- Update display results feature to display ranked results split by game level, eg: top 5 easy, top 5 medium and top 5 hard.

## USER STORIES

Considering this project scope and design, as for user stories we contain only **user** who is the player of the game.

- As a **user** I want to either **view the game instructions** so I can **understand how to play the game and its rules** or to **skip and play directly, as I am returning player and know how to play**.
- As a **user** I want to **select a game level** that best suits me, either **being easy and relaxing or hard and challenging**.
- As a **user** I want to be able to **view hints that help me find the "lucky" number** and **view numbers I have tried already** allowing me to **get the correct number and win the game**.
- As a **user** I want to either **add my name or nickname** to be displayed in the game score board results to **log my results to display how I performed** or **to leave without adding any info about myself**.
- As a **user** I want to be given the option to either **continue playing** or to **leave the game**.

## Testing

- 
  
### Workflow testing

- Lorem Ipsum
  - Lorem Ipsum

- Lorem Ipsum

  [Am I Responsive?](https://ui.dev/amiresponsive?url=https://guess-the-number-p3-31510f7a135e.herokuapp.com/) shows all available common layouts.

- Tested Browsers and Devices

  - Desktop:
    - Google Chrome
    - Mozilla Firefox
    - Apple Safari
    - DuckDuckGo
  - Tablet *tested through Google Chrome Inspector*:
    - *iPad Air*
    - *iPad Mini*
    - *Surface Pro 7*
    - *Google Nest Hub*
  - Mobile *tested through Google Chrome Inspector*:
    - iPhone 13 Pro (Google Chrome, Mozilla Firefox, Apple Safari and DuckDuckGo)
    - *iPhone SE*
    - *iPhone XR*
    - *Pixel 5*
    - *Samsung Galaxy S8+*
    - *Samsung Galaxy S20 Ultra*

### Validator Testing

- Lorem Ipsum
  - Lorem Ipsum [W3C validator]().

### Bugs

- In development stage, multiple minor bugs were noticed, most of them while creating functions and styling. However, 2 bugs stood out.

- Solved Bugs
  - Function returning same value with assign event listener to buttons
    - After implementing solution to make [If/Else statement execute with event listener inside](https://stackoverflow.com/questions/48167887/if-else-statement-not-executing-correctly-with-event-listener-inside-javascript), the functions getUserOption() and getUserNumber() were still returning the same value. The bug was taking place due to two semicolons misplaced in the code (after 'btn-evens' condition and after 'btn-5' condition). The but was solved with the help of [Stack Overflow community](https://stackoverflow.com/questions/76551168/functions-returning-same-value-even-with-assigned-event-listener-to-the-buttons).

    - Code example with bug:

      ```text

      function getUserOption(userOption) {
      let userResult;

      if (userOption === 'btn-odds') {
        userResult = 1;
      } else if (userOption === 'btn-evens'); {
        userResult = 0;
      }}

      function getUserNumber(userNumber) {

      let userNumberSelected;

      if (userNumber === 'btn-1') {
        userNumberSelected = 1;
      } else if (userNumber === 'btn-2') {
        userNumberSelected = 2;
      } else if (userNumber === 'btn-3') {
        userNumberSelected = 3;
      } else if (userNumber === 'btn-4') {
        userNumberSelected = 4;
      } else if (userNumber === 'btn-5'); {
        userNumberSelected = 5;
      }}

      ```

### Unfixed Bugs

- There are no unfixed bugs.

## Deployment

- Lorem Ipsum
  - Lorem Ipsum
  
- The live link can be found here - <https://guess-the-number-p3-31510f7a135e.herokuapp.com/>

## Credits

### Content

- Game code was inspired by [Love Maths]() project - events listener structure with 'data-type' and results functions built based in the project's.
- 
### Media

- Lorem Ipsum [Shutterstock]() with free trial plan.
