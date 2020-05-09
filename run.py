import os
import json
from datetime import datetime
import logging

from flask import Flask, redirect, render_template, request, jsonify, url_for, flash

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
application_data = []
questionary = None # Special Python value. Is returned by functions that do not execute a return statement with a return argument
with open('data/application.json') as json_file:
    application_data = json.load(json_file)
    questionary = application_data['questionary']
    json_file.close()
    

def save_scores(top_ten_players):
    with open('data/scores.txt', 'w') as file:
        for player in top_ten_players:    
            file.writelines(str(player[0]) + "\n")
            file.writelines(str(player[1]) + "\n")
   
         
def load_scores():
    with open('data/scores.txt', 'r') as file:
        lines = file.read().splitlines()
        
    player_names = []
    scores = []
    for i, text in enumerate(lines):
        if i%2 == 0:
            player_names.append(text)
        else:
            scores.append(text)

    return zip(player_names, scores)

# Function to get top players on the table

def get_score_table(player_name, score):
    top_ten = load_scores()
    top_ten.append((player_name, score))
    return sorted(top_ten, key=lambda x: int(x[1]), reverse=True)
    
    
@app.route('/', methods=["GET", "POST"])
def index():                                          # index is called
    if request.method == "POST":                      # route is requested
        player_name = request.form['player_name']     #player_name is a variable
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
        answer = int(form['answer'])
        correct_answer = int(form['correct_answer'])                 
        attempts = int(form['attempts'])                             
        print("answer={}".format(answer))
        print("correct_answer={}".format(correct_answer))
    else:
        question_counter = 0
        attempts_counter = 0
        score = 0
        answer = ''
        
    """Question state"""
    total = len(questionary) #is this a new function len() and stores the retur value for variable total
    if request.method == "POST":
        if correct_answer == answer: 
            attempts_counter = 0
            question_counter += 1
            score += 1 # TODO: improve this by addeding a nice formula
            # flash('Well! Well! Well! Your guess is...!', 'correct') #go to riddle
        else:
            print("attempts_counter={} of attempts={}".format(attempts_counter, attempts))
            print("attempts_counter <= attempts={}".format(attempts_counter <= attempts))
            if attempts_counter < attempts:                                              
                attempts_counter += 1
            else:
                question_counter += 1
                attempts_counter = 0
                print("question_counter={} total={}".format(question_counter, total))
                print("question_counter <= total={}".format(question_counter == total))
        if question_counter == total:
            player_names_and_scores = get_score_table(player_name, score)
            save_scores(player_names_and_scores[:10])
            return render_template(
                "game_over.html",
                score=score,
                player_name=player_name,
                player_names_and_scores=player_names_and_scores 
            ) 
                
    # check if the answer is correct:
    
    
    question_data = questionary[question_counter]
    attempts = question_data['attempts']
    correct_answer = question_data['correctAnswerIndex']
    logger.debug("correct_answer={}".format(correct_answer))
    print("correct_answer={}".format(correct_answer))
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
        attempts=attempts,            
        correct_answer=correct_answer 
    )
    
  
  
  
    
@app.route('/top_ten')                                # what is our parameter refering
def top_ten():
   player_names_and_scores= load_scores()

   return render_template("table.html", player_names_and_scores=player_names_and_scores) 
    
    
    
    
    
         
        
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

    