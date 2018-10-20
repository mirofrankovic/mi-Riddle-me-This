import os

from flask import Flask, redirect, render_template, request


app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))
    
    
def get_all_messages():
    return "<br>".join(messages)



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.writelines(request.form["username"] + "\n")
            return redirect(request.form["username"])
    return render_template("index.html")
    
    
@app.route('/<username>')
def user(username):
    return "Welcome, {0} - {1}".format(username, get_all_messages())
    
    
@app.route('/<username>/<message>')  
def send_message(username, message):
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)    