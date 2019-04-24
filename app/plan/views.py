from app.models import db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.plan.forms import CountrySelectForm, AddTravelPlan, EditTravelPlan, ChangeTravelPlan
from app.plan.models import Travel_plan, Country
from app.plan.country import all_countries
from app.expenditure.models import Expenditures
from flask import Blueprint
from flask_login import current_user, UserMixin
from sqlalchemy import or_, and_

bp = Blueprint('plan', __name__,url_prefix='/plan')

def notNone(date_from_form,date_min_max):
    if date_from_form is None:
        return datetime.strptime(date_min_max, '%d/%m/%Y').date()
    else:
        return date_from_form

def DateFormat(date):
    return date.strftime('%d/%m/%Y')


@bp.route('/search_travel_plan', methods=['GET', 'POST'])
def search_travel_plan():

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = CountrySelectForm()
    page_title = 'Найти путешествие'
    form.country_field.query_factory=all_countries
    travel_plans_list =[]
   
    if form.validate_on_submit():
        if form.date_start.data and form.date_end.data and form.date_start.data > form.date_end.data:
            flash('Дата начала путешествия должна быть ранее даты окончания')
       
        travel_plans = Travel_plan.query.filter((Travel_plan.country_id==form.country_field.data.id)
        &(Travel_plan.user_id==current_user.id)
        &(Travel_plan.date_end >=notNone(form.date_start.data,'01/01/1900'))
        &(Travel_plan.date_start <=notNone(form.date_start.data,'01/01/2100'))
        ).all()
         
        if travel_plans:
            
            for travel_plan in travel_plans:
             
                country = travel_plan.country.name
                plan = [country, DateFormat(travel_plan.date_start),DateFormat(travel_plan.date_end),travel_plan.id]
                travel_plans_list.append(plan)
    
    return render_template(
        'plan/travel_plan.html',
        page_title=page_title,
        travel_plans_list=travel_plans_list,
        form=form)



        
@bp.route('/travel_plan_info/<travel_plan_id>', methods=['GET', 'POST'])
def travel_plan_info(travel_plan_id):

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
   
   
    travel_plan = Travel_plan.query.get(travel_plan_id)

    if not travel_plan or travel_plan.user_id != current_user.id:
        flash('Данных не найдено')
        return redirect(url_for('index'))

    form = ChangeTravelPlan()
    
    if request.method == 'GET': 
     
        date_start =  DateFormat(travel_plan.date_start)
        date_end = DateFormat(travel_plan.date_end)
        info = f' {travel_plan.text}'
        country_name = travel_plan.country.name
        page_title = f'{country_name}  c {date_start} по {date_end}' 

        if travel_plan:
            expenditures = Expenditures.query.filter_by(
                travel_plan_id=travel_plan.id).all()   

    elif form.validate_on_submit() and travel_plan and travel_plan.user_id == current_user.id:
        if form.edit_plan.data:
            
            return redirect(url_for(
                    'plan.edit_travel_plan',
                    travel_plan_id=travel_plan.id))
        elif form.add_expanditure.data:
            return redirect(url_for(
                    'expenditure.add_expenditure',
                    travel_plan_id=travel_plan.id))
    
    return render_template(
        'plan/travel_plan_info.html',
        page_title=page_title,
        
        info=info,
       
        expenditures=expenditures,
        travel_plan_id=travel_plan_id,
        form=form)



@bp.route('/add_travel_plan', methods=['GET', 'POST'])
def add_travel_plan():
    
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
   
    form = AddTravelPlan()
    page_title = 'Добавить путешествие'
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
        return redirect(url_for('plan.travel_plan_info',travel_plan_id = travel_plan.id))

    return render_template(
        'plan/add_travel_plan.html',
        page_title=page_title,
        form=form)


@bp.route('/edit_travel_plan/<travel_plan_id>', methods=['GET', 'POST'])
def edit_travel_plan(travel_plan_id):

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
   
    page_title = 'Изменить'
    form = EditTravelPlan()
    travel_plan = Travel_plan.query.get(travel_plan_id)
    country_name = travel_plan.country.name

    if not travel_plan or travel_plan.user_id != current_user.id:
        flash('Путешествие не найдено')
        return redirect(url_for('index'))

    if request.method == 'GET':
       
        form.date_start.data = travel_plan.date_start
        form.date_end.data = travel_plan.date_end
        form.text.data = travel_plan.text
    
    elif form.validate_on_submit():

        travel_plan.date_start = form.date_start.data
        travel_plan.date_end = form.date_end.data
        travel_plan.text = form.text.data
        db.session.commit()
        return redirect(
            url_for(
                'plan.travel_plan_info',
                travel_plan_id=travel_plan_id))
   
    
   
    return render_template(
        'plan/edit_travel_plan.html',
        page_title=page_title,
        country_name=country_name,
        form=form)


@bp.route('/delete_travel_plan/<travel_plan_id>')
def delete(travel_plan_id):

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
   

    travel_plan = Travel_plan.query.get(travel_plan_id)
    if not travel_plan or travel_plan.user_id != current_user.id:
        flash('Данные не найдены')
        return redirect(url_for('index'))
    db.session.delete(travel_plan)
    db.session.commit()
    flash('План путешествия удален')
    return redirect(url_for('index'))
