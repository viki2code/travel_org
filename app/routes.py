from app import app, db
import datetime
from flask import render_template, redirect, url_for
from app.forms import LoginForm, CurrencyInputForm, CountrySelectForm
from app.currency import rate_of_exchange
from app.models import Travel_plan, Expenditures, Country


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyInputForm()
    page_title = 'Курс валюты на сегодня:'
    currency_data = rate_of_exchange(
        'EUR')
    if form.validate_on_submit():

        return redirect(url_for('show_currency', code=form.currency.data))
    return render_template(
        '/index.html',
        title='Home',
        page_title=page_title,
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'],
        form=form)


@app.route('/login')
def login():
    page_title = 'Авторизация'

    login_form = LoginForm()
    return render_template('login.html', page_title=page_title,title='Sign In', form=login_form)


@app.route('/currency/<code>', methods=['GET', 'POST'])
def show_currency(code):
    currency_data = rate_of_exchange(
        code)
    return render_template(
        'rate.html',
        title='Home',
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'])


@app.route('/travel_plan', methods=['GET', 'POST'])
def travel_plan():
    form = CountrySelectForm()
    page_title = 'Органайзер для путешествий'
    country = Country.query.filter_by(id=form.country_field.data).first()
    travel_plan = Travel_plan.query.filter_by(
        country_id=form.country_field.data).first()
    expenditures = ''
    if travel_plan:
        expenditures = Expenditures.query.filter_by(
            travel_plan_id=travel_plan.id).all()
    # if form.validate_on_submit():
    return render_template(
        'travel_plan.html',
        title=page_title,
        country_name=country.name,
        expenditures=expenditures,
        form=form)
