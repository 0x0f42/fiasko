from app import db


class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}' with role '{}'>".format(self.username, self.role)

class Room(db.Model):
    __tablename__ == 'room_table'

    id = db.Column(db.Integer(), primary_key=True)
    room_number = db.Column(db.Integer())
    reserved = db.Column(db.Boolean())

    def __init__(self, room_number, reserved=False):
        self.room_number = room_number
        self.reserved = reserved
