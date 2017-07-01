from flask import Flask

app = Flask(__name__)
from app import views

# The script above simply creates the application object (of class Flask)
# and then imports the views module, which we haven't written yet. Do not
# confuse app the variable (which gets assigned the Flask instance) with
# app the package (from which we import the views module).

# If you are wondering why the import statement is at the end and not at
# the beginning of the script as it is always done, the reason is to avoid
# circular references, because you are going to see that the views module
# needs to import the app variable defined in this script. Putting the
# import at the end avoids the circular import error.

# The views are the handlers that respond to requests from web browsers 
# or other clients. In Flask handlers are written as Python functions.
# Each view function is mapped to one or more request URLs.
