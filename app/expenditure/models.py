from app.models import db
from sqlalchemy.orm import relationship


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
    travel_plan = relationship('Travel_plan', backref='Expenditures')

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
