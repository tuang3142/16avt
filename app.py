from flask import Flask
from flask import render_template
from flask import request

from extract_data import get_traits, get_hero_info
# how to use form
# files upload -> save on local storage
# db, prob wont save.

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    url = request.form['url']
    return get_traits(url)
    # img = request.form['img']


# @app.route('/random')
# randomize a avt 
