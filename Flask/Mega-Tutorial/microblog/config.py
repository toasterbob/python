import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


#The WTF_CSRF_ENABLED setting activates the cross-site request forgery
# prevention (note that this setting is enabled by default in current
# versions of Flask-WTF). In most cases you want to have this option
# enabled as it makes your app more secure.

# In practice, we will find that a lot of people don't even know that
# they already have a few OpenIDs. It isn't that well known that a number
# of major service providers on the Internet support OpenID authentication
# for their members. For example, if you have an account with Google,
# you have an OpenID with them. Likewise with Yahoo, AOL, Flickr and many
# other providers. (Update: Google is shutting down their OpenID service
# on April 15 2015).

# We will start by defining the list of OpenID providers that we want to
# present. We can do this in our config file (file config.py):
