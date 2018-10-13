import os
import json
from datetime import datetime 
from flask import Flask, redirect, render_template, request, jsonify, flash, url_for 

app = Flask(__name__)
data = []


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

def add_messages(username, message):
    """Add messages to the `messages` text file"""
    write_to_file("data/messages.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(),
            message))
    
def get_all_messages():
    """Get all of the messages and separate them by a `br`"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages
    
def add_users(username):
    write_to_file("data/users.txt", "({0}) - {1}\n".format(
        username.title()))
        
def get_all_users():
    users = []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instrutions"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")
    
@app.route('/game') 
def game():
    return render_template("game.html")
    
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")
    
    
    
@app.route('/<username>', methods=["GET", "POST"]) 
def user(username):
    """Display chat messages"""
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return "Welcome, {0} - {1}".format(username, get_all_messages())
    
    riddle_index = 0
    
    messages = get_all_messages()
    
    return render_template("game.html",
    username=username, chat_messages=messages, company_data=data, riddle_index=riddle_index)
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    