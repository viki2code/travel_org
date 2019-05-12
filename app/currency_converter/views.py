from app.models import db
from datetime import datetime
from flask import render_template
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange, all_currency, calculate_currency
from flask import render_template, redirect, url_for, flash, request
from flask import Blueprint
import requests

bp = Blueprint(
    'currency_converter',
    __name__,
    url_prefix='/currency_converter')


@bp.route('/calc_currency/<param>', methods=['GET', 'POST'])
def calc_currency(param):
    form = CurrencyInputForm()
    page_title = 'Валютный калькулятор:'
    param_list = param.split('-')
    form.currency.choices = all_currency()
    form.currency_convert.choices = all_currency(['EUR', 'USD'])

    if form.validate_on_submit():
        param = f'{form.rate.data}-{form.currency_convert.data}-{form.currency.data}'
        print(param)
        return redirect(
            url_for('currency_converter.calc_currency', param=param))

    elif request.method == 'GET':
         # если нет трех элементов в list то кидать 400 ошибку

        try:
            currency_convert = param_list[1]
            currency_convert_data = rate_of_exchange(currency_convert)
            currency = param_list[2]
            currency_data = rate_of_exchange(currency)
            rate = param_list[0]

        except (requests.RequestException, TypeError, ValueError):
            return redirect(
                url_for('index'))

        form.currency.choices = all_currency()
        form.currency.default = currency
        form.currency_convert.choices = all_currency(['EUR', 'USD'])
        form.currency_convert.default = currency_convert

        form.process()
        form.rate.data = rate
        rate_convert = calculate_currency(
            rate,
            currency_convert_data['rate'],
            currency_convert_data['nominal'])
        rate_country = calculate_currency(
            rate, currency_data['rate'], currency_data['nominal'])
        converter = f'{rate} RUB = {rate_convert} {currency_convert} = {rate_country} {currency}'
        info = f'по курсу ЦБРФ {datetime.now().strftime("%d/%m/%Y")}'
    return render_template(
        'currency_converter/rate.html',
        page_title=page_title,
        info=info,
        converter=converter,
        form=form)
