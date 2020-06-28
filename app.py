import os

from flask import Flask
from flask import request
from flask import render_template

from forms import AvatarForm
from extract_data import extract_data
# files upload -> save on local storage

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AvatarForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)

    url = request.form['url']
    # img = request.form['img']
    return extract_data(url)


# @app.route('/random')
# randomize a avt
