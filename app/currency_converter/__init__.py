from flask import Blueprint

bp = Blueprint('currency_converter', __name__)

from app.currency_converter import routes