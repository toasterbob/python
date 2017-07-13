#the application module
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# For small applications like flaskr, it is possible to drop the configuration
# directly into the module. However, a cleaner solution is to create a separate
# .ini or .py file, load that, and import the values from there.

app = Flask(__name__) #create the application instance
app.config.from_object(__name__) # load config from this file, flaskr.py

# Load default config and overrisde config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# The silent switch just tells Flask to not complain if no such environment key is set.

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
