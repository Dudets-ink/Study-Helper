from .. import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.relationship('Info', backref='user', lazy=True)

    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreign_key('user.id'), 
                        nullable=False)
    
    text = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow())
    
