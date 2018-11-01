# *RIDDLE-ME-THIS* GUESSING GAME
Build a web application game that asks players to guess the answer to a
pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players
enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed
below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time, each in
their own browser. Users are identified by a unique username, but note that no
authentication features such as a password are required for this project.
Create a leaderboard that ranks top scores for all (at least recent) users.

* Data (Text or Images)
* A list of option to select the correct answer.

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


Build a web application game that asks players to guess the answer 
to a pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle.
Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed
below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time,
each in their own browser. Users are identified by a unique username, 
but note that no authentication features such as a password are required
for this project.
Create a leaderboard that ranks top scores for all (at least recent) users.

