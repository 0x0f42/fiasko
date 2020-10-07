from flask import Flask
from datetime import datetime
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def hello_world():
    return {"message":'Running'}, 200

@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%d.%m.%y %H:%M:%S")
    return {"time":current_time}, 200

@app.route('/version')
def version():
    return {"version": 2}, 203

if __name__ == '__main__':
    app.run(port=5001)
