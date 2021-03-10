#app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(url_for('static', filename='main.css'))
    return render_template('index.html')
