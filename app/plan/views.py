from app.models import db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.plan.forms import CountrySelectForm, AddTravelPlan, EditTravelPlan, NullableDateField
from app.plan.models import Travel_plan, Country
from app.plan.country import all_countries
from app.expenditure.models import Expenditures
from flask import Blueprint
from flask_login import current_user


bp = Blueprint('plan', __name__,url_prefix='/plan')
def notNone(date_from_form):
    if date_from_form is None:
        return datetime.strptime('01/01/1900', '%d/%m/%Y').date()
    else:
        return date_from_form
@bp.route('/travel_plan_info', methods=['GET', 'POST'])
def travel_plan_info():
    form = CountrySelectForm()
    page_title = 'Органайзер для путешествий'
    form.country_field.query_factory=all_countries
    travel_plans_list =[]
   
    if form.validate_on_submit():
        if form.date_start.data and form.date_end.data and form.date_start.data > form.date_end.data:
            flash('Дата начала путешествия должна быть ранее даты окончания')
       
        travel_plans = Travel_plan.query.filter((Travel_plan.country_id==form.country_field.data.id)
        &(Travel_plan.user_id==current_user.id)&(Travel_plan.date_end >=notNone(form.date_start.data))).all()
        #&((form.date_start.data is None)| (Travel_plan.date_end >=form.date_start.data))).all()
        #&(or_(form.date_end.data is None,Travel_plan.date_start <= form.date_end.data))).all()
        
        if travel_plans:
            
            for travel_plan in travel_plans:
               # if form.date_start.data >= travel_plan.date_start:
                #    print(travel_plan.date_start)
                #new_p = (form.date_start.data >= travel_plan.date_start)
                #print(new_p)
                country = Country.query.get(travel_plan.country_id).name
                plan = [country, travel_plan.date_start,travel_plan.date_end,travel_plan.id]
                travel_plans_list.append(plan)
    
    return render_template(
        'plan/travel_plan.html',
        title=page_title,
        travel_plans_list=travel_plans_list,
        form=form)




@bp.route('/add_travel_plan', methods=['GET', 'POST'])
def add_travel_plan():
    form = AddTravelPlan()
    page_title = 'Добавить план'
    form.country_field.query_factory = all_countries
    

    if form.validate_on_submit():
        travel_plan = Travel_plan(
        country_id=form.country_field.data.id,
        date_start=form.date_start.data,
        date_end=form.date_end.data,
        user_id=current_user.id,
        text=form.text.data)

        db.session.add(travel_plan)
        db.session.commit()
        flash('Вы добавили план')
        return redirect(url_for('plan.travel_plan_info'))

    return render_template(
        'plan/add_travel_plan.html',
        form=form)


@bp.route('/edit_travel_plan/<travel_plan_id>', methods=['GET', 'PUT', 'POST'])
def edit_travel_plan(travel_plan_id):
    form = EditTravelPlan()
    travel_plan = Travel_plan.query.get(travel_plan_id)
    if not travel_plan:
        flash('Путешествие не найдено')
        return redirect(url_for('index'))
    if form.validate_on_submit():
        travel_plan.date_start = form.date_start.data
        travel_plan.date_end = form.date_end.data
        db.session.commit()
        flash('Изменения сохранены')
        return redirect(
            url_for(
                'plan.edit_travel_plan',
                travel_plan_id=travel_plan_id))
    elif request.method == 'GET':
        form.date_start.data = travel_plan.date_start
        form.date_end.data = travel_plan.date_end
        form.name.data = Country.query.get(travel_plan.country_id).name

    elif request.method == 'PUT':
        form.date_start.data = travel_plan.date_start
        form.date_end.data = travel_plan.date_en
        form.name.data = Country.query.get(travel_plan.country_id).name

        flash('Изменения сохранены')
        return redirect(
            url_for(
                'plan.edit_travel_plan',
                travel_plan_id=travel_plan_id))

    return render_template(
        'plan/edit_travel_plan.html',
        title='Редактировать путешествие',
        form=form)


@bp.route('/delete_travel_plan/<travel_plan_id>')
def delete(travel_plan_id):
    travel_plan = Travel_plan.query.get(travel_plan_id)
    if not travel_plan:
        flash('Данные не найдены')
        return redirect(url_for('index'))
    db.session.delete(travel_plan)
    db.session.commit()
    flash('План путешествия удален')
    return redirect(url_for('index'))
