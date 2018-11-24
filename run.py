import os
import json
from datetime import datetime


from flask import Flask, redirect, render_template, request, jsonify


app = Flask(__name__)


def get_question_counter(questionary):
    """Create an array of question and answer"""
    with open("data/application.json") as json_application:
        application = json.loads(json_application.read())
        return application[questionary] if questionary < 10 else None  #Return None to avoid questionary error on the last question
        
"""Initial state for the game with all variables with some initial default values get assignet"""
#riddle == question
def init_game(username):
    score = 0
    attempts = 5
    question = get_question_counter(0)
    context = {
        'question_counter': 0,
        'question': question['question'],
        'answers': question['answers'],
        'attemptsCounter': attempts,
        'current_score': score,
        'username': username,
        'correctAnswerIndex': question['correctAnswerIndex'],
        'correctAnswerValue': question['correctAnswerValue']
    }
    return context


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        
    
    
def add_messages(username, message):
    """Now we added messages to the `messages` stored in text file"""
    write_to_file("data/messages.txt", "({0}) - {1}\n".format(
             username.title(),
             message))
             
             
# Function to get all attempts should we understand as messages and chat_messages as incorect answers    
def get_all_attempts():
    """Get all of the attempts/ messages and separete them by a `br`"""
    attempts = []
    with open("data/messages.txt", "r") as incorect_answers:
        attempts = [row for row in incorect_answers if len(row.strip()) > 0]
    return attempts
    
def num_of_attempts():
    """The number or messages/attempst made by the user on the current question"""
    attempts = get_all_attempts
    return len(attempts);
    
def attempts_rem():
    """Return the number of messages/attempts remaining"""
    rem_attempts = 5 - num_of_attempts()
    return rem_attempts;

def add_users(username):
    """Now we added users to the `users` stored in text file"""
    write_to_file("data/users.txt", "{}\n".format(username.title()))

#Function to get current users        
def get_all_users():
    users= []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users
    

        
@app.route('/', methods=["GET", "POST"])
def home():
    """Main page with instruction"""
    
    # Handle POST request
    if request.method == "POST":
        
        write_to_file("data/users.txt", request.form["username"] + "\n")
        
        return redirect(request.form["username"])
    return render_template("index.html", username=user)
    
    
  #Route to show the game
@app.route('/game/<username>', methods=["GET", "POST"])
def user(username):
    """Question state - Display chat messages"""
    
    if request.method == "POST":
        form = request.form
        
    #If user answer correcly increment question_counter +1
    if form.get('first-question') == 'true':
        context = init_game(username)
        return render_template('game.html', context=context, username=username)
        
    else:
        #Get attempts numbers from the application.json file
        #int() argument must be a string or a number(5 or attemptsCounter)?
        attempts = int(request.form.get('attempts'))
        question_counter = int(request.form.get('question_counter'))
        score = int(request.form.get('current_score'))
        question = get_question_counter(question_counter)
        
        #Check if the answer is correct
        accepted_answers = request.form.get('accepted_answers').strip().lower()
        actual_answers = question['answers'].strip().lower()
        correct = accepted_answers == actual_answers
        
        #Scoring correctly question_counter incremented +1
        while question_counter < 10:
            if correct:
                question_counter += 1
                score += 1
                attempts = 5
                next_question = get_question_counter(question_counter)
            else:
                #If answers are incorrect and the number of attempts user have more then 5, take the user to the next question
                #`attemptsCounter` incremented by 1
                #questionary[question_counter].attempts
                if attempts >= 5:
                    question_counter += 1
                    score += 1
                    
                    next_question = get_question_counter(question_counter)
                    
    with open("data/application.json", "r") as json_data:
        data = json.load(json_data)
        
    attempts = get_all_attempts()
    
    return render_template(
        "game.html", username=username, attempts=attempts,
    ) 
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    