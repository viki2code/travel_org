from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange
from flask import render_template, redirect, url_for, flash, request
from app.models import db
from app.user.models import User
from app.user.views import bp as user_blueprint
from app.plan.views import bp as plan_blueprint
from app.currency_converter.views import bp as currency_converter_bp
from app.currency_converter.currency import all_currency,rate_of_exchange
from app.expenditure.views import bp as expenditure_blueprint
from flask import  flash
import requests
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(plan_blueprint)
    app.register_blueprint(currency_converter_bp)
    app.register_blueprint(expenditure_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)






    @app.route('/', methods=['GET', 'POST','PUT'])
    def index():
        
        form = CurrencyInputForm()
        '''
        form.currency.choices = all_currency()
        
        page_title = 'Курс валюты на сегодня:'
        name_of_currency = ''
        rate = ''

        try:
            currency_data = rate_of_exchange(
            'EUR')
            name_of_curency=currency_data['name_of_currency'],
            rate=currency_data['rate']
        except (requests.RequestException, TypeError,ValueError):
            flash('Отсутствие связи')
            
        
        if form.validate_on_submit():
            print(form.currency.data)
            currency_data = rate_of_exchange(
                form.currency.data)
           
            return redirect(
                url_for('index'))
        elif request.method == 'PUT':
            form.rate.data = currency_data['rate']
            print(form.rate.data)
            return redirect(
                url_for('index'))

        print(form.errors)'''
        return render_template(
            'index.html',
            page_title='Органайзер путешественника',
            name='name_of_currency',
            rate='rate',
            form=form)
    

    return app
