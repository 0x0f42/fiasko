from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer(), primary_key=True) 
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)


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
