import os
import json
from datetime import datetime 
from flask import Flask, redirect, render_template, request, jsonify

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

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instrutions"""
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")
    
    
    
@app.route('/<username>', methods=["GET", "POST"]) 
def user(username):
    """Display chat messages"""
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return "Welcome, {0} - {1}".format(username, get_all_messages())
    
    riddle_index = 0
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    