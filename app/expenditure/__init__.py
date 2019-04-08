from flask import Blueprint

bp = Blueprint('expenditure', __name__)

from app.expenditure import routes