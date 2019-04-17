from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from datetime import datetime

class CurrencyInputForm(FlaskForm):
    currency = StringField('Код валюты: ', validators= [DataRequired()])
    submit = SubmitField('Курс валюты')

class NullableDateField(DateField):
    def process_formdata(self, valuelist):
        if valuelist:
           
            date_str = ' '.join(valuelist).strip()
            
            if date_str == '':
                self.data = None
                return
            try:
                self.data = datetime.strptime(date_str, '%d/%m/%Y').date()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid date value'))

class CountrySelectForm(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
    date_start = NullableDateField(DateField('Дата начала поездки: ', format='%d/%m/%Y'))
    date_end = NullableDateField(DateField('Дата окончания поездки: ', format='%d/%m/%Y'))
    submit = SubmitField('Найти путешествие')
   


class AddTravelPlan(FlaskForm):
    country_field = QuerySelectField("Страна: ",allow_blank=True,get_label='name')
    date_start = NullableDateField(DateField('Дата начала поездки: ', format='%d/%m/%Y'))
    date_end = NullableDateField(DateField('Дата окончания поездки: ', format='%d/%m/%Y'))
    text = StringField('Описание:')
    currency = QuerySelectField("Валюта: ",allow_blank=True,get_label='name')
    submit = SubmitField('Добавить')

class EditTravelPlan(FlaskForm):
    name = StringField('Наименование', validators=[DataRequired()])
    text = StringField('Описание:')
    date_start = NullableDateField(DateField('Дата начала поездки: ', format='%d/%m/%Y'))
    date_end = NullableDateField(DateField('Дата окончания поездки: ', format='%d/%m/%Y'))
    submit = SubmitField('Изменить')
    


