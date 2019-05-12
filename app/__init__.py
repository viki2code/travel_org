from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange
from flask import render_template, redirect, url_for, flash, request
from app.plan.models import Travel_plan
from app.models import db
from app.user.models import User
from app.user.views import bp as user_blueprint
from app.plan.views import bp as plan_blueprint
from app.currency_converter.views import bp as currency_converter_bp
from app.currency_converter.currency import all_currency, rate_of_exchange
from app.expenditure.views import bp as expenditure_blueprint
from flask import flash
from datetime import datetime
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

    @app.route('/', methods=['GET', 'POST', 'PUT'])
    def index():

        if not current_user.is_authenticated:
            return redirect(url_for('user.login'))
        page_title = f'Органайзер пользователя {current_user.username}'
        travel_plans_new = Travel_plan.query.filter(
            (Travel_plan.user_id == current_user.id) & (
                Travel_plan.date_start > datetime.now())).all()
        plans_new = []
        for travel_plan in travel_plans_new:
            plan = {
                'name_travel': travel_plan.country.name,
                'about': travel_plan.text,
                'id': travel_plan.id}
            plans_new.append(plan)

        travel_plans_old = Travel_plan.query.filter(
            (Travel_plan.user_id == current_user.id) & (
                Travel_plan.date_start < datetime.now())).all()
        plans_old = []
        for travel_plan in travel_plans_old:
            plan = {
                'name_travel': travel_plan.country.name,
                'about': travel_plan.text,
                'id': travel_plan.id}
            plans_old.append(plan)

        return render_template(
            'index.html',
            page_title=page_title,
            plans_new=plans_new,
            plans_old=plans_old)

    return app
