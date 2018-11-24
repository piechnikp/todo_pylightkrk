from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    msg = StringField('Message', validators=[DataRequired()])
    done = BooleanField('Done', default=False)
    submit = SubmitField('Add')
