from itertools import count
import json
from flask import Flask, request, jsonify
from markupsafe import escape
app = Flask(__name__)

count = 1

@app.route("/")
def intro():
    # return default type is HTML
    return "Hello World!!!"

@app.route("/home/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route("/home/login", methods = ['POST'])
def login():
    id_info = request.json.get('id')
    pw_info = request.json.get('pw')
    return {
        'id_r': id_info,
        'pw_r' : pw_info
    }
@app.route("/count")
def count_click():
    global count
    
    count += 1
    
    return f"<div>I count it as... <b>{count}</b></div>"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')