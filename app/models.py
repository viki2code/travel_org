from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def is_admin(self):
        return self.role == 'admin'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    travel_plan = db.relationship(
        'Travel_plan',
        backref='country',
        lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.id)


class Travel_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    date_in = db.Column(db.DateTime, index=True, nullable=False)
    date_out = db.Column(db.DateTime, index=True)
    text = db.Column(db.Text, nullable=True)
    expenditures = db.relationship(
        'Expenditures',
        backref='travel_plan',
        lazy='dynamic')

    def __repr__(self):
        return '<TravelPlan {} {} {} {}>'.format(
            self.date_in, self.date_out, self.text,self.country_id)


class Expenditures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    travel_plan_id = db.Column(db.Integer, db.ForeignKey('travel_plan.id'))
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
