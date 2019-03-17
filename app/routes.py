from flask import render_template
import datetime
from app import app
from app.forms import LoginForm
from app.currency import rate_of_exchange

@app.route('/')
@app.route('/index')
def index():
    page_title = 'Курс валюты на сегодня:'
    currency_data = rate_of_exchange('EUR',datetime.datetime.today().strftime("%d/%m/%Y"))
    return render_template('index.html', title='Home',page_title=page_title,name = currency_data['name_of_currency'] 
                            ,rate = currency_data['rate']) 
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
@app.route('/<currency>')
def show_currency(currency):
    currency_data = rate_of_exchange(currency,datetime.datetime.today().strftime("%d/%m/%Y"))
    return render_template('rate.html', title='Home',name = currency_data['name_of_currency'] ,rate = currency_data['rate'])