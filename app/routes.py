from flask import render_template,redirect
import datetime
from app import app
from app.forms import LoginForm,StringForm
from app.currency import rate_of_exchange

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StringForm()
    page_title = 'Курс валюты на сегодня:'
    currency_data = rate_of_exchange('EUR',datetime.datetime.today().strftime("%d/%m/%Y"))
    if form.validate_on_submit():
        
        return redirect('/USD')
    return render_template('index.html', title='Home',page_title=page_title,name = currency_data['name_of_currency'] 
                            ,rate = currency_data['rate'], form = form) 
                        
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
@app.route('/<currency>', methods=['GET', 'POST'])
def show_currency(currency):
    currency_data = rate_of_exchange(currency,datetime.datetime.today().strftime("%d/%m/%Y"))
    return render_template('rate.html', title='Home',name = currency_data['name_of_currency'] ,rate = currency_data['rate'])