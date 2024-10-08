from random import choice
from os import environ
from flask import Flask
app = Flask(__name__)
option_file = environ.get(
     "OPTION_FILE","option.txt")
def load_option(file_path):
     with open(file_path, "r" , encodeing="utf-8") as f:
          file_contents = f.read()
          return file_contents.split()
options = load_options(option_file)
@app.route("/")
def pick_work():
     return choice(options)