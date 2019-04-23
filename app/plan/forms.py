from wtforms.validators import DataRequired,Required, InputRequired, Optional
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from datetime import datetime

class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')

class CountrySelectForm(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name', validators=[Optional()])
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y', validators=[Optional()])
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y', validators=[Optional()])
    submit = SubmitField('Найти путешествие')
   


class AddTravelPlan(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y', validators=[Optional()])
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y', validators=[Optional()])
    text = StringField('Описание:')
    currency = QuerySelectField("Валюта: ",allow_blank=True,get_label='name')
    submit = SubmitField('Добавить')

class EditTravelPlan(FlaskForm):
    text = StringField('Описание:')
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y')
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y')
    submit = SubmitField('Изменить')

class ChangeTravelPlan(FlaskForm):
    edit_plan = SubmitField('Изменить')
    add_expanditure = SubmitField('Добавить статьи затрат')

    


