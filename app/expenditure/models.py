from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from datetime import datetime

class Expenditures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    travel_plan_id = db.Column(
        db.Integer,
        db.ForeignKey('travel_plan.id', ondelete='CASCADE'))
    text = db.Column(db.Text, nullable=True)
    sum_plan = db.Column(db.Numeric, nullable=True)
    sum_real = db.Column(db.Numeric, nullable=True)
    expand_expenditures = db.relationship(
        'Expand_expenditures',
        backref='Expenditures',
        lazy='dynamic')
    def __repr__(self):
        return '<Expenditure {}>'.format(self.text)

class Expand_expenditures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expenditure_id = db.Column(db.Integer, db.ForeignKey('expenditures.id'))
    text = db.Column(db.Text, nullable=True)
    sum_plan = db.Column(db.Numeric, nullable=True)
    sum_real = db.Column(db.Numeric, nullable=True)

    def __repr__(self):
        return '<Expenditure {}>'.format(self.text)
