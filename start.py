from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%d.%m.%y %H:%M:%S")
    return current_time

@app.route('/version')
def version():
    return {"version": 2}

app.run(debug=True)
