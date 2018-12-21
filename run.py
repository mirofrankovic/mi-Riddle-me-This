import os
import json
from datetime import datetime

from flask import Flask, redirect, render_template, request, jsonify, url_for

app = Flask(__name__)
application_data = []
questionary = None # Special Python value. Is returned by functions that do not execute a return statement with a return argument
with open('data/application.json') as json_file:
    application_data = json.load(json_file)
    questionary = application_data['questionary']
    json_file.close()

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        player_name = request.form['player_name']
        return redirect(player_name)
    return render_template("index.html")
    
@app.route('/<player_name>', methods=["GET", "POST"])
def game(player_name):
    # (0) Initial state (Variables are initialized) ----> (1)
    # (1) Question state (Render the question with the list of answers)
    #     --- If user answer the question correctly ---> (2)
    #     --- If the answer is incorrectly ---> (1.2) 
    # (1.2) `attemptsCounter` incremented by 1
    #     --- If `attemptsCounter` == questionary[question_counter].attempts ---> (2)
    #     --- If `attemptsCounter` < questionary[question_counter].attempts ---> (1)
    # (2) Increment `question_counter` plus 1, reset `attemptsCounter` ---> (3)
    # (3) If question_counter is equal to total questions -----> (4) if not ---> (1)
    # (4) Shows result of the quiz
    
    """Conditionals: Initializing variables"""
    if request.method == "POST":
        form = request.form
        question_counter = int(form['question_counter'])
        attempts_counter = int(form['attempts_counter'])
        score = int(form['score'])
        answer = form['answer']
        correct_answer = form['correct_answer'] #added from line 53 and bad request!
        attempts = form['attempts'] #added from line 58
    else:
        question_counter = 0
        attempts_counter = 0
        score = 0
        answer = ''
        
    """Question state"""
    total = len(questionary)
    if request.method == "POST":
        if correct_answer == answer:
            attempts_counter = 0
            question_counter += 1
            score += 1 # TODO: improve this by addeding a nice formula
        else:
            if attempts_counter <= attempts:
                attempts_counter += 1
            else:
                if question_counter == total:
                    return render_template(
                        'game_over.html', score=score, player_name=player_name
                        )
                attempts_counter = 0
    
    question_data = questionary[question_counter]
    attempts = question_data['attempts']
    correct_answer = question_data['correctAnswerValue']
    return render_template(
        "riddle.html",
        player_name=player_name,
        question=question_data['question'],
        answers=question_data['answers'],
        question_counter=question_counter,
        attempts_counter=attempts_counter,
        score=score,
        answer=answer,
        total=total,
        attempts=attempts, #double check attempts
        correct_anwer=correct_answer #double check correct_answer
    )
    
@app.route('/<game_over>', methods=["GET", "POST"])  
def result(game_over):
    if request.method == "POST":
        
        
        
        return render_template(
            "game_over",
            )
        
        
        

    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    