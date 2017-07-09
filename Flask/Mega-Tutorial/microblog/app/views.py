from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

# Note how this function is registered with Flask-Login through the
# lm.user_loader decorator. Also remember that user ids in Flask-Login
# are always unicode strings, so a conversion to an integer is necessary
# before we can send the id to Flask-SQLAlchemy.

@app.before_request
def before_request():
    g.user = current_user

# you will remember that in the login view function we check g.user to
# determine if a user is already logged in. To implement this we will
# use the before_request event from Flask. Any functions that are decorated
# with before_request will run before the view function each time a request
# is received. So this is the right place to setup our g.user variable (file app/views.py):

# The current_user global is set by Flask-Login, so we just put a copy
# in the g object to have better access to it. With this, all requests
# will have access to the logged in user, even inside templates.



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
@oid.loginhandler
# We have added a new decorator to our view function. The oid.loginhandler
# tells Flask-OpenID that this is our login view function.
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    # we check if g.user is set to an authenticated user, and in that
    # case we redirect to the index page. The idea here is that if there
    # is a logged in user already we will not do a second login on top.
    # The g global is setup by Flask as a place to store and share data
    # during the life of a request. As I'm sure you guessed by now, we
    # will be storing the logged in user here.
    # The url_for function that we used in the redirect call is defined
    # by Flask as a clean way to obtain the URL for a given view function.
    # If you want to redirect to the index page you may very well use
    # redirect('/index'), but there are very good reasons to let Flask
    # build URLs for you.
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login requested for OpenID="%s", remember_me=%s' %
        #       (form.openid.data, str(form.remember_me.data)))
        # return redirect('/index')
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']) #Here we grab the configuration by looking it up in app.config with its key.

# The validate_on_submit method does all the form processing work. If
# you call it when the form is being presented to the user (i.e. before
# the user got a chance to enter data on it) then it will return False,
# so in that case you know that you have to render the template.

# When validate_on_submit is called as part of a form submission request,
# it will gather all the data, run all the validators attached to fields,
# and if everything is all right it will return True, indicating that the
# data is valid and can be processed. This is your indication that this
# data is safe to incorporate into the application.

# If at least one field fails validation then the function will return
# False and that will cause the form to be rendered back to the user,
# and this will give the user a chance to correct any mistakes. We will
# see later how to show an error message when validation fails.

# The flash function is a quick way to show a message on the next page
# presented to the user. The flashed messages will not appear automatically
# in our page, our templates need to display the messages in a way that
# works for the site layout. We will add these messages to the base template,
# so that all our templates inherit this functionality.

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

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
