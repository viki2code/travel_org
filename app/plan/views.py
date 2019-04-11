from app.models import db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.plan.forms import CountrySelectForm, AddTravelPlan, EditTravelPlan
from app.plan.models import Travel_plan, Country
from app.plan.country import all_countries
from app.expenditure.models import Expenditures
from flask import Blueprint

bp = Blueprint('plan', __name__,url_prefix='/plan')

@bp.route('/travel_plan_info', methods=['GET', 'POST'])
def travel_plan_info():
    form = CountrySelectForm()
    page_title = 'Органайзер для путешествий'
    form.country_field.query_factory=all_countries
    
    expenditures = []
    if form.validate_on_submit():
        travel_plan = Travel_plan.query.filter(Travel_plan.country_id==form.country_field.data.id).first()
       
        
        if travel_plan:
            expenditures = Expenditures.query.filter_by(
                travel_plan_id=travel_plan.id).all()
           
   
    return render_template(
        'plan/travel_plan.html',
        expenditures=expenditures,
        title=page_title,
        form=form)




@bp.route('/add_travel_plan', methods=['GET', 'POST'])
def add_travel_plan():
    form = AddTravelPlan()
    page_title = 'Добавить план'
    form.country_field.query_factory = all_countries
    travel_plan = Travel_plan(
        country=form.country_field.data,
        date_start=form.date_start.data,
        date_end=form.date_end.data)

    if form.validate_on_submit():
        db.session.add(travel_plan)
        db.session.commit()
        flash('Вы добавили план')
        return redirect(url_for('plan.add_travel_plan'))

    return render_template(
        'plan/add_travel_plan.html',
        form=form)


@bp.route('/edit_travel_plan/<travel_plan_id>', methods=['GET', 'PUT', 'POST'])
def edit_travel_plan(travel_plan_id):
    form = EditTravelPlan()
    travel_plan = Travel_plan.query.get(travel_plan_id)
    if travel_plan is None:
        flash('План не найден')
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
    if travel_plan is None:
        flash('Данные не найдены')
        return redirect(url_for('index'))
    db.session.delete(travel_plan)
    db.session.commit()
    flash('Пункт плана удален')
    return redirect(url_for('index'))
