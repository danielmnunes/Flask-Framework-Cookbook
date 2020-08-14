from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True # Object level
app.debug = True # Config leval
# app.run(debug=True) # named argument
# $ export or Set FLASK_DEBUG = 1 # Set on an environment variable


@app.route('/')
def index():
    return 'Hello World!!'