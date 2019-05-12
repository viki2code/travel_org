from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return '{}'.format(self.id)


class Travel_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    date_start = db.Column(db.Date, index=True, nullable=False)
    date_end = db.Column(db.Date, index=True)
    text = db.Column(db.Text, nullable=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'))
    country = relationship('Country', backref='Travel_plan')

    def __repr__(self):
        return '<TravelPlan {} {} {} {}>'.format(
            self.date_start, self.date_end, self.text, self.country_id)
