# *Code Institute Milestone Project 2*

This is Practical Python Milestone Project called Riddle Me This. It is a project as part of the syllabus on the Full Stack Web Development course.

* Description:
# *RIDDLE-ME-THIS* GUESSING GAME

Build a web application game that asks players to guess the answer to a
pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players
enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed
below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time, each in
their own browser.
Users are identified by a unique username, but note that no
authentication features such as a password are required for this project.
Create a leaderboard that ranks top scores for all (at least recent) users.

This game is based on 10 text riddles which are presented to the user one at a time.
The player must choose a username at the beginning of the game which will be unique.

The player is presented with a series of 10 text based riddles. Players enter their answer into a text box form.

If the player guesses correctly, they are directed to the next riddle and awarded 1 point. If a player guesses incorrectly,
their incorrect guess is storedand printed below the riddle.

At the end of the game, the players score will be recorded on the leaderboard using their username as a reference.

* Data (Text or Images)
* A list of option to select the correct answer.

* Structure:

(0) Initial state (Variables are initialized) ----> (1)
(1) Question state (Render the question with the list of answers)
    --- If user answer the question correctly ---> (2)
    --- If the answer is incorrectly ---> (1.2) 
(1.2) `attemptsCounter` incremented by 1
    --- If `attemptsCounter` == questionary[question_counter].attempts ---> (2)
    --- If `attemptsCounter` < questionary[question_counter].attempts ---> (1)
(2) Increment `question_counter` plus 1, reset `attemptsCounter` ---> (3)
(3) If question_counter is equal to total questions -----> (4) if not ---> (1)
(4) Shows result of the quiz

Initial state
This is the state where all variables initial values get assigned. e.g:
`question_counter = 0`

Question state
In this state the question is selected together with its list of answer where
one answer is the correct answer. The `question_counter` variable is the
variable that keeps the index of the current question in progress.



* When `question_counter` reaches the total of questions then the game is over.

* Some of the tech used includes:
* HTML and CSS
    To structure and style the web app content, Including creating the POST method form
* Python2
    To design the logic of the game
    For reading from, and writing to, the game’s text files
    For unit testing the game’s functions. These tests are found in test_game.py
    Creating a requirements.txt and Procfile to deploy the app on Heroku
    Sorting the leadboard data
* Flask
    For binding functions to URLs using routing
    To render HTML templates, including the use of a base template. These templates are in the templates directory
    To enable Python programming within HTML pages
    To trigger functions on GET or POST requests
    For getting data from, and dumping data to, JSON files
    Used for debugging
* JSON
    For storing and editing player data (players.json) and previously asked questions (used_questions.json) throughout the game
    Used to store high score data, found in /data/high_scores.json
* Bootstrap
    Used primarily for the website’s grid layout and for styling buttons, player cards, and the leaderboard table
    Heroku https: ...
    Final deployment of the app
    
* Testing:    

