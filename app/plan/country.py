from app.plan.models import Country

def all_countries():

    return Country.query.order_by(Country.name)