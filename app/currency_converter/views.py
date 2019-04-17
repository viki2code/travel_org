from app.models import db
from datetime import datetime
from flask import render_template
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange,all_currency,notNone
from flask import render_template, redirect, url_for, flash, request
from flask import Blueprint

bp = Blueprint('currency_converter', __name__, url_prefix='/currency_converter')

@bp.route('/show_currency/', methods=['GET', 'POST','PUT'])
def show_currency():
    form = CurrencyInputForm()
    page_title = 'Курс валюты на сегодня:'
    code = 'EUR'
    currency_data = rate_of_exchange(code)    
    form.currency.default = code  
    form.process()
    form.currency.choices = all_currency()
    
    currency_convert_data = rate_of_exchange(code)    
    form.currency_convert.default = code  
    form.process()
    form.currency_convert.choices = all_currency(['EUR','USD'])

    form.rate.data = float(notNone(form.ruble.data,1)) * float(currency_data['rate'].replace(',','.'))
    form.rate_convert.data = float(notNone(form.ruble.data,1)) *float(currency_data['rate'].replace(',','.'))
    if form.validate_on_submit():
        #???
        return redirect(
            url_for('currency_converter.show_currency'))
    
    print(type(form.rate.data))
    print(form.errors)
    return render_template(
        'currency_converter/rate.html',
        title=page_title,
        name=currency_data['name_of_currency'],
        form=form)