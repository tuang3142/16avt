from flask_wtf import Form
from wtforms import StringField


class AvatarForm(Form):
    url = StringField()
    # img =
