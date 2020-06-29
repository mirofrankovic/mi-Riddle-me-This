# **Code Institute Milestone Project 2**

This is Practical Python Milestone Project 2 called Riddle Me This is a project as part of the syllabus on the Full Stack Web Development course.

* DESCRIPTION:

# **RIDDLE-ME-THIS** GUESSING GAME

Build a web application game that asks players to guess the answer to a text-based riddle.
The player is presented with atext that contains the riddle. Players
enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed
below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time, each in
their own browser.
Users are identified by a unique username, but note that no
authentication features such as a password are required for this project.
At the end of the game, the players score will be recorded on the leaderboard using their username as a reference.


This game is based on 10 text riddles which are presented to the user one at a time.
The player must choose a username at the beginning of the game which will be unique.

The player is presented with a series of 10 text based riddles. Players enter their answer into a text box form.

If the player guesses correctly, they are directed to the next riddle and awarded 1 point. If a player guesses incorrectly,
their incorrect guess is storedand printed below the riddle.

* STRUCTURE:

(0) **Initial state** (Variables are initialized) ----> (1)
(1) **Question state** (Render the question with the list of answers)
    --- If user answer the question correctly ---> (2)
    --- If the answer is incorrectly ---> (1.2) 
(1.2) `attemptsCounter` incremented by 1
    --- If `attemptsCounter` == questionary[question_counter].attempts ---> (2)
    --- If `attemptsCounter` < questionary[question_counter].attempts ---> (1)
(2) **Increment** `question_counter` plus 1, reset `attemptsCounter` ---> (3)
(3) If question_counter is equal to total questions -----> (4) if not ---> (1)
(4) Shows **result** of the quiz

**Initial state**

This is the state where all variables initial values get assigned. e.g:
`question_counter = 0`

**Question state**

In this state the question is selected together with its list of answer where
one answer is the correct answer. The `question_counter` variable is the
variable that keeps the index of the current question in progress.
When `question_counter` reaches the total of questions then the game is over.

* FEATURES:

The app features a game which requires a unique username so that results can be recorded on a leaderboard. 
The Top 10 results are displayed o nthe leaderboard. 
The app consists of a welcome page, an instruction page, 10 riddles and then a leaderboard page.

# * Some of the tech used includes:


* HTML and CSS

    > to structure and style the web app content, Including creating the POST method form
    
* Python2

    > to design the logic of the game
    > for reading from, and writing to, the game’s text files
    > for unit testing the game’s functions. These tests are found in test_game.py
    > creating a requirements.txt and Procfile to deploy the app on Heroku
    > sorting the leadboard data
    
* Flask

    > for binding functions to URLs using routing
    > to render HTML templates, including the use of a base template. These templates are in the templates directory
    > to enable Python programming within HTML pages
    > to trigger functions on GET or POST requests
    > for getting data from, and dumping data to, JSON files
    > used for debugging
    
* JSON

    > for storing and editing player data (players.json) and previously asked questions (used_questions.json) throughout the game
    > used to store high score data, found in /data/high_scores.json
    
* Bootstrap

    > used primarily for the website’s grid layout and for styling buttons, player cards, and the leaderboard table
    > Heroku https: ...
    > final deployment of the app
    
# * Testing:  

**Manual Testing**

**Responsive Testing** The app was tested on Samsung S8, Apple iPhone 6, 
Apple iPad Air 2 and also using the Google Chrome inspect feature to tes for repsonsiveness and any errors that occurred.
The main issue which was found was the sidevar/ navbar not resizing.

# * Deployment:

The GitHub Repository is hosted *[here](https://mirofrankovic.github.io/mi-Riddle-me-This/)*.

# * Credits:

**Extra Resources**

Stackoverflow.com

Slack

GitHub

Flexbox














