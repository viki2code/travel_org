from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.init_app(app)
login.login_view = 'user.login'

from app.user import bp as user_bp
app.register_blueprint(user_bp, url_prefix='/user')

from app.plan import bp as plan_bp
app.register_blueprint(plan_bp, url_prefix='/plan')

from app.currency_converter import bp as currency_converter_bp
app.register_blueprint(currency_converter_bp, url_prefix='/currency_converter')

from app.expenditure import bp as expenditure_bp
app.register_blueprint(expenditure_bp, url_prefix='/expenditure')



from app import routes,models
'''

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'user.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app) 
        
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.plan import bp as plan_bp
    app.register_blueprint(plan_bp, url_prefix='/plan')

    from app.currency_converter import bp as currency_converter_bp
    app.register_blueprint(currency_converter_bp, url_prefix='/currency_converter')

    from app.expenditure import bp as expenditure_bp
    app.register_blueprint(expenditure_bp, url_prefix='/expenditure')

    

    return app
from app import  models,routes
'''