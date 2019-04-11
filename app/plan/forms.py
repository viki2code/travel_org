from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')

class CountrySelectForm(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
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
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Изменить')
    


