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
    
def final_score(player_name, score):
    if player_name != "" and score != "":
        with open('data/scores.txt', 'a') as file:
            file.writelines(str(score) + "\n")
            file.writelines(str(player_name) + "\n")
   

def get_scores():
    player_names = []
    scores = []
    with open('data/scores.txt', 'r') as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            scores.append(text)
        else:
            player_names.append(text)
    player_names_and_scores = sorted(zip(player_names, scores), key=lambda x: x[1], reverse=True)
    return player_names_and_scores  
    
#def get_topleaders():
#    with open('data/scores.txt', 'r') as scores:
#        scores = [line for line in scores.readlines()[1:]]
#    top_playername_score = []    
#        
#   for score in scores:
#        tupe = (score.split(':')[0].strip, int(score.split(':')[1].strip()))
#        top_playername_score.append(tupe)
#
#    return sorted(top_playername_score, key=lambda x: x[1])[::-1][:10] 
    
      
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
            final_score(player_name, score) 
            player_names_and_scores = get_scores() # get_scores + 10topleaders need to add
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
    
# @app.route('/<game_over>', methods=["GET", "POST"])                                # what is our parameter refering
 #def gamer(game_over):
  # player_names_and_scores = get_scores()
   #return render_template(
    #    "game_over", player_names_and_scores=player_names_and_scores 
#   )
        
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

    