from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    collectionDate = db.Column(db.String(50))
    collectionTime = db.Column(db.String(50))
    imagePath = db.Column(db.String(50))

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Complaints(db.Model):
    cid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    message=db.Column(db.String(50))
    date=db.Column(db.String(50),nullable=False)
    image=db.Column(db.String(50))

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    message = db.Column(db.String(50))
    date = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(50))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))