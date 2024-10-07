from random import choice
from flask import Flask
app = Flask(__name__)
choices = ["first","second","third"]
@app.route("/")
def pick_work():
     return choice(choices)