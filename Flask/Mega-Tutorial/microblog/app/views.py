from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mark'} # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Bob'},
            'body': 'The church of the subgenius is seeking spam recipes!'
        }
    ]
    return render_template( 'index.html',
                            title='Home',
                            user=user,
                            posts=posts)

# The only other thing that is new here is the methods argument in the
# route decorator. This tells Flask that this view function accepts GET
# and POST requests. Without this the view will only accept GET requests.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

# This view is actually pretty simple, it just returns a string, to be
# displayed on the client's web browser. The two route decorators above
# the function create the mappings from URLs / and /index to this function.

# Under the covers, the render_template function invokes the Jinja2
# templating engine that is part of the Flask framework. Jinja2
# substitutes {{...}} blocks with the corresponding values provided as
# template arguments.

# Control statements in templates

# The Jinja2 templates also support control statements, given inside
# {%...%} blocks. Let's add an if statement to our template
# (file app/templates/index.html):
  # <head>
  #   {% if title %}
  #   <title>{{ title }} - microblog</title>
  #   {% else %}
  #   <title>Welcome to microblog</title>
  #   {% endif %}
  # </head>
# Now our template is a bit smarter. If the view function forgets to
# define a page title then instead of showing an empty title the
# template will provide its own title.
