# A Minimal Application

# Flask application, load the configuration of choice and then create
# the SQLAlchemy object by passing it the application.

# Once created, that object then contains all the functions and helpers
# from both sqlalchemy and sqlalchemy.orm.

# Furthermore it provides a class called Model that is a declarative
# base which can be used to declare models:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
