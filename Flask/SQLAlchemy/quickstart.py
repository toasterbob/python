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

# To create the initial database, just import the db object from an
# interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database:
#
# >>> from yourapplication import db
# >>> db.create_all()

# Boom, and there is your database. Now to create some users:
#
# >>> from yourapplication import User
# >>> admin = User('admin', 'admin@example.com')
# >>> guest = User('guest', 'guest@example.com')
# But they are not yet in the database, so let’s make sure they are:
#
# >>> db.session.add(admin)
# >>> db.session.add(guest)
# >>> db.session.commit()

# Accessing the data in database is easy as a pie:
#
# >>> users = User.query.all()
# [<User u'admin'>, <User u'guest'>]
# >>> admin = User.query.filter_by(username='admin').first()
# <User u'admin'>


# Simple Relationships
# SQLAlchemy connects to relational databases and what relational databases
# are really good at are relations. As such, we shall have an example of an
# application that uses two tables that have a relationship to each other

from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
