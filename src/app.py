from functools import reduce
from flask import Flask, jsonify, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return {"message":'Running'}, 200


@app.route('/time')
def time():
    now = datetime.now()
    short = request.args.get('short')
    current_time = now.strftime("%d.%m.%y") if short is 'yes' or short is 'y' or short is '1' else now.strftime("%d.%m.%y %H:%M:%S")
    return {"time":current_time}, 200


@app.route('/version')
def version():
    return {"version": 3}, 200


@app.route('/users')
def users():
    from models import User

    def concat(a, b):
        a.append(b)
        return a

    return jsonify(
        reduce(
            concat,
            map(lambda e: {"username": e.username, "password": e.password}, User.query.all()),
            []
        )
    ), 203


if __name__ == '__main__':
    app.run(port=5001)
