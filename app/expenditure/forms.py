from wtforms.validators import DataRequired,Required, InputRequired
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

   
class AddExpanditureForm(FlaskForm):
    name = StringField('Наименование',render_kw={'class': 'form-control'})
    sum_plan = DecimalField('Плановые затраты')
    sum_real = DecimalField('Фактические затраты')
    submit = SubmitField('Добавить',render_kw={'class': 'btn btn-lg btn-success btn-block'})

   
class EditExpanditureForm(FlaskForm):
    name = StringField('Наименование',render_kw={'class':'form-control'})
    sum_plan = DecimalField('Плановые затраты',render_kw={'class':'form-control'})
    sum_real = DecimalField('Фактические затраты',render_kw={'class':'form-control'})
    submit = SubmitField('Изменить',render_kw={'class': 'btn btn-lg btn-success btn-block'})
   
 
class DeleteExpanditureForm(FlaskForm):
    
    submit = SubmitField('Да',render_kw={'class': 'btn  btn-success btn-block'})
    cancel = SubmitField('Отмена',render_kw={'class': 'btn  btn-success btn-block'})
