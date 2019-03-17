from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import DataRequired
from app.currency import all_currency


class StringForm(FlaskForm):
    currency = StringField('Код валюты: ', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class SelectedForm(FlaskForm):
  test_field = SelectField("Валюта: ", choices=all_currency, default=2)