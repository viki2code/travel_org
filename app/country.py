from app.models import Travel_plan, Expenditures, Country
from sqlalchemy.orm import load_only




def all_countries():

    countries = Country.query.options(load_only('id','name')).all()
    all_rec = []
    
    for country in countries:
        
        country_tuple = (country.id, country.name)
        all_rec.append(country_tuple)
        
    return all_rec
