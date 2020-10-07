from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

@app.route('/version')
def time():
    return {"version": 2}
