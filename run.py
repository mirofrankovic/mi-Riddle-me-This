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
             
             
#Attempts should we count as messages and chat_messages as incorect answers    
def get_all_messages():
    """Get all of the messages and separete them by a `br`"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = [row for row in chat_messages if len(row.strip()) > 0]
    return messages
    
def num_of_messages():
    """The number or messages/attempst made by the user on the current question"""
    messages = get_all_messages
    return len(messages);
    
def messages_rem():
    """Return the number of messages/attempts remaining"""
    rem_messages = 5 - num_of_messages()
    return rem_messages;

def add_users(username):
    """Now we added users to the `users` stored in text file"""
    write_to_file("data/users.txt", "{}\n".format(username.title()))
        
def get_all_users():
    users= []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users
    
@app.route('/users/online', methods=["GET"])
def online_users():
    online_users_file = open("data/online_users.txt")
    online_users = [row for row in online_users_file if len(row.strip()) > 0]
    online_users_file.close()
    
    return jsonify(online_users)
        
@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instruction"""
    
    # Handle POST request
    if request.method == "POST":
        
        write_to_file("data/users.txt", request.form["username"] + "\n")
        
        return redirect(request.form["username"])
    return render_template("index.html", username=user)
    
    
  #Route to show the game
@app.route('/game/<username>', methods=["GET", "POST"])
def user(username,):
    """Display chat messages"""
    
    if request.method == "POST":
        form = request.form
    
    if form.get('first-question') == 'true':
        context = init_game(username)
        return render_template('game.html', context=context)
    else:
        #Get attempts numbers from the application file
        attempts = int(request.form.get('attempts'))
        question_counter = int(request.form.get('question_counter'))
        score = int(request.form.get('current_score'))
        question = get_question_counter(question_counter)
        
        #Check if the answer is correct
        accepted_answers = request.form.get('accepted_answers').strip().lower()
        actual_answers = question['answers'].strip().lower()
        correct = accepted_answers == actual_answers
        
        #Scoring
        while question_counter < 10:
            if correct:
                question_counter += 1
                score += 1
                attempts = 5
                next_question = get_question_counter(question_counter)
            else:
                if attempts >= 5:
                    question_counter += 1
                    score += 1
                    
                    next_question = get_question_counter(question_counter)
                    
                    
                    
        
        
        
        
    
    with open("data/application.json", "r") as json_data:
        data = json.load(json_data)
        
    messages = get_all_messages()
    
    return render_template("game.html",
                            username=username, chat_messages=messages,
                        ) 
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    