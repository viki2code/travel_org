from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class CurrencyInputForm(FlaskForm):
    currency = SelectField('Код валюты: ')
    submit = SubmitField('Курс валюты')

