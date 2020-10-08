from app import app
from models import db, User


@app.shell_context_processor 
def make_shell_context():
    return dict(app=app, db=db, User=User)
