from flask import Flask
from flask import render_template
from flask import request # use this to access params
# how to use form
# files upload -> save on local storage
# db, prob wont save.

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/random')
# randomize a avt 
