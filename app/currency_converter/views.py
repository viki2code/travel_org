from app.models import db
from datetime import datetime
from flask import render_template
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange,all_currency,notNone
from flask import render_template, redirect, url_for, flash, request
from flask import Blueprint

bp = Blueprint('currency_converter', __name__, url_prefix='/currency_converter')


@bp.route('/calc_currency/<param>', methods=['GET', 'POST'])
def calc_currency(param):
    form = CurrencyInputForm()
    page_title = 'Валютный калькулятор:'
    param_list = param.split('-')
    form.currency.choices = all_currency()
    form.currency_convert.choices = all_currency(['EUR','USD'])
    
    if form.validate_on_submit():
        param = f'{form.rate.data}-{form.currency_convert.data}-{form.currency.data}'
        print(param)
        return redirect(
            url_for('currency_converter.calc_currency', param=param))

    elif request.method == 'GET':
         #если нет трех элементов в list то кидать 400 ошибку
        currency_convert = param_list[1]
        currency_convert_data = rate_of_exchange(currency_convert)    
        currency = param_list[2]
        currency_data = rate_of_exchange(currency)    
        rate = param_list[0]  
        form.currency.choices = all_currency()
        form.currency.default = currency
        form.currency_convert.choices = all_currency(['EUR','USD'])
        form.currency_convert.default = currency_convert
        
        form.process()
        form.rate.data = rate
        rate_convert = round(float(notNone(rate,1))/float(currency_convert_data['rate'].replace(',','.')),2)
        rate_country = round(float(notNone(rate,1)) /float(currency_data['rate'].replace(',','.')),2)
        converter = f'{rate} RUB = {rate_convert} {currency_convert} = {rate_country} {currency}'

    return render_template(
        'currency_converter/rate.html',
        page_title=page_title,
        converter=converter,
        form=form)
