from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
class NullableFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
           
            rate = ' '.join(valuelist).strip()
            
            if rate == '':
                self.data = None
                return
            try:
                self.data = rate
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid date value'))
class CurrencyInputForm(FlaskForm):
    
    ruble = NullableFloatField(FloatField('Рубли'))
    currency_convert = SelectField('Конвертируемая валюта: ')
    currency = SelectField('Валюта страны: ')
    rate_convert = NullableFloatField(FloatField('Конвертируемая'))
    rate = NullableFloatField(FloatField('Значение'))
    submit = SubmitField('Курс валюты')
