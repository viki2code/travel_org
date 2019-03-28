from app.currency import all_currency
from app.country import all_countries
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField


class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In', render_kw={'class': 'btn btn-primary'} )


class CurrencySelectForm(FlaskForm):
    test_field = SelectField("Валюта: ", choices=all_currency, default=2)


class CountrySelectForm(FlaskForm):
    country_field = SelectField("Страна: ", choices=all_countries(), default=1)
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Найти план')
