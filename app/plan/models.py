from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from datetime import datetime

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
    

    def __repr__(self):
        return '<TravelPlan {} {} {} {}>'.format(
            self.date_in, self.date_out, self.text,self.country_id)

