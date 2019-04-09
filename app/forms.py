from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField, DecimalField

class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')

