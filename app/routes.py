from app import app, db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyInputForm()
    page_title = 'Курс валюты на сегодня:'
    currency_data = rate_of_exchange(
        'EUR')
    if form.validate_on_submit():

        return redirect(
            url_for(
                'currency_converter/show_currency',
                code=form.currency.data))

    return render_template(
        '/index.html',
        title='Home',
        page_title=page_title,
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'],
        form=form)
