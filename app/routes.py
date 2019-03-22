from app import app,db
import datetime
from flask import render_template, redirect, url_for
from app.forms import LoginForm, CurrencyInputForm
from app.currency import rate_of_exchange


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyInputForm()
    page_title = 'Курс валюты на сегодня:'
    currency_data = rate_of_exchange(
        'EUR')
    if form.validate_on_submit():

        return redirect( url_for('show_currency', code=form.currency.data))
    return render_template(
        '/index.html',
        title='Home',
        page_title=page_title,
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'],
        form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/currency/<code>', methods=['GET', 'POST'])
def show_currency(code):
    currency_data = rate_of_exchange(
        code)
    return render_template(
        'rate.html',
        title='Home',
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'])
