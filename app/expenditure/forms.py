from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

   
class AddExpanditureForm(FlaskForm):
    name = StringField('Наименование')
    sum_plan = DecimalField('Плановые затраты')
    sum_real = DecimalField('Фактические затраты')
    submit = SubmitField('Добавить')

   
class EditExpanditureForm(FlaskForm):
    name = StringField('Наименование')
    sum_plan = DecimalField('Плановые затраты')
    sum_real = DecimalField('Фактические затраты')
    submit = SubmitField('Изменить')
