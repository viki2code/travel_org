from app.models import Travel_plan, Expenditures, Country



def all_countries():
    countries = Country.query.all()
    all_rec = []
    i = 0
    for country in countries:
        
        new = (country.id, country.name)
        all_rec.append(new)
    return all_rec
