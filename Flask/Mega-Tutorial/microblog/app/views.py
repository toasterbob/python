from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mark'} # fake user
    return '''
    <html>
      <head>
        <title>Microblog Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + user['nickname'] + '''!</h1>
      </body>
    </html>
'''

# This view is actually pretty simple, it just returns a string, to be
# displayed on the client's web browser. The two route decorators above
# the function create the mappings from URLs / and /index to this function.
