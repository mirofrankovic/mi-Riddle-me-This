import os
from datetime import datetime

from flask import Flask, redirect, render_template, request


app = Flask(__name__)
messages = []
data = []


def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
    

def add_messages(username, message):
    """Now we added messages to the `messages` stored in text file"""
    write_to_file("data/messages.txt", "({0}) - {1}\n".format(
             username.title(),
             message))
    
def get_all_messages():
    """Get all of the messages and separete them by a `br`"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = [row for row in chat_messages if len(row.strip()) > 0]
    return messages

def add_users(username):
    """Now we added users to the `users` stored in text file"""
    write_to_file("data/users.txt", "({0}) - {1}\n".format(
              username.title()))
        
def get_all_users():
    users= []
    with open("data/users.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users
        


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instruction"""
    
    # Handle POST request
    if request.method == "POST":
        
        write_to_file("data/users.txt", request.form["username"] + "\n")
        
        return redirect(request.form["username"])
    return render_template("index.html")
    
    
@app.route('/<username>')
def user(username):
    messages = get_all_messages()
    
    return render_template("game.html",
                            username=username, chat_messages=messages) 
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    