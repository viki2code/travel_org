from wtforms.validators import DataRequired,Required, InputRequired, Optional
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from datetime import datetime

class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')

class CountrySelectForm(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name', validators=[Optional()],render_kw={'class':'form-control'})
    date_start = DateField('Дата начала поездки: ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    date_end = DateField('Дата окончания поездки: ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    submit = SubmitField('Найти путешествие',render_kw={'class': 'btn btn-lg btn-success btn-block'})
   


class AddTravelPlan(FlaskForm):
    country_field = QuerySelectField("Страна ",allow_blank=True,get_label='name',render_kw={'class':'form-control'})
    date_start = DateField('Дата начала поездки ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    date_end = DateField('Дата окончания поездки ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    text = StringField('Описание',render_kw={'class':'form-control'})
    currency = QuerySelectField("Валюта ",allow_blank=True,get_label='name')
    submit = SubmitField('Добавить',render_kw={'class': 'btn btn-lg btn-success btn-block'})

class EditTravelPlan(FlaskForm):
    text = StringField('Описание',render_kw={'class':'form-control'})
    date_start = DateField('Дата начала поездки ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    date_end = DateField('Дата окончания поездки ', format='%d/%m/%Y', validators=[Optional()],render_kw={'class':'form-control'})
    submit = SubmitField('Сохранить',render_kw={'class': 'btn btn-lg btn-success btn-block'})

class ChangeTravelPlan(FlaskForm):
    edit_plan = SubmitField('Изменить',render_kw={'class': 'btn btn-lg btn-success btn-block'})
    add_expanditure = SubmitField('Добавить статьи затрат',render_kw={'class': 'btn btn-lg btn-success btn-block'})

    


