from datetime import datetime
from app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    travel_plan = db.relationship(
        'Travel_plan',
        backref='country',
        lazy='dynamic')

    def __repr__(self):
        return '<Country {} {}>'.format(self.code, self.name)


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
        return '<TravelPlan {} {} {}>'.format(
            self.date_in, self.date_out, self.text)


class Expenditures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    travel_plan_id = db.Column(db.Integer, db.ForeignKey('travel_plan.id'))
    text = db.Column(db.Text, nullable=True)
    sum_plan = db.Column(db.Numeric, nullable=True)
    sum_real = db.Column(db.Numeric, nullable=True)

    def __repr__(self):
        return '<Expenditure {}>'.format(self.text)
