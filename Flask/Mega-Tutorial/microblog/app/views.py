from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# This view is actually pretty simple, it just returns a string, to be
# displayed on the client's web browser. The two route decorators above
# the function create the mappings from URLs / and /index to this function.
