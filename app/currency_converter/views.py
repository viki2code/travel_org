from app.models import db
from datetime import datetime
from flask import render_template
from app.currency_converter.forms import CurrencyInputForm
from app.currency_converter.currency import rate_of_exchange
from flask import Blueprint

bp = Blueprint('currency_converter', __name__, url_prefix='/currency_converter')

@bp.route('/currency/<code>', methods=['GET', 'POST'])
def show_currency(code):
    currency_data = rate_of_exchange(
        code)
    return render_template(
        'rate.html',
        title='Home',
        name=currency_data['name_of_currency'],
        rate=currency_data['rate'])
