# Guess the Number!

Guess the Number! is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

In this game, users will be challenged find a random generate number. In each game play users get 10 "guesses", allowing to try up to 10 numbers. The random number will be generated in a range based on the difficulty level selected by users (easy, medium and hard). After each try, the game will throw a hint in order to help finding the number and the tried number will be displayed as a guide.

The game works well as an alternative for a quick game play, adding some elements to challenge the users such as calling generated number as their "lucky number" and funny hints as the game runs. 

[Guess the Number!](https://guess-the-number-p3-31510f7a135e.herokuapp.com/)

![Responsive Mockup]()

## Features

### Existing Features

- Lorem Ipsum
  - Lorem Ipsum

    ![Header]()

- Lorem Ipsum
  - Lorem Ipsum

    ![Instructions]()

    - Lorem Ipsum

      ![Start]()

## Features Left to Implement or Future Features

### Scoreboard

- 

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
