from app.currency import all_currency
from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

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
    #country_field = SelectField("Страна: ", choices=all_countries(), default=1)
    country_field = StringField("Страна: ")
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Найти план')
    submitadd = SubmitField('Добавить')


class ExpendituresForm(FlaskForm):
    country_field = SelectField("Страна: ", default=1)
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Найти план')
    


class AddTravelPlan(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Добавить')

class EditTravelPlan(FlaskForm):
    name = StringField('Наименование', validators=[DataRequired()])
    #country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Изменить')
    
class AddExpanditureForm(FlaskForm):
    name = StringField('Наименование')
    sum_plan = DecimalField('Плановые затраты')
    sum_fact = DecimalField('Фактические затраты')
    submit = SubmitField('Добавить')

