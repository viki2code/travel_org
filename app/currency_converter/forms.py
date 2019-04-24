from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class CurrencyInputForm(FlaskForm):
    
    rate = FloatField('Рубли',render_kw={'class':'form-control'})
    currency = SelectField('Валюта страны',render_kw={'class':'form-control'})
    currency_convert = SelectField('Конвертируемая валюта',render_kw={'class':'form-control'})
    submit = SubmitField('Конвертировать',render_kw={'class': 'btn btn-lg btn-success btn-block'})
