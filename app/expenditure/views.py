from app import db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.expenditure.forms import AddExpanditureForm, EditExpanditureForm, DeleteExpanditureForm
from app.expenditure.models import  Expenditures

from app.plan.models import Travel_plan, Country

from flask_login import current_user
from flask import Blueprint

bp = Blueprint('expenditure', __name__, url_prefix='/expenditure')

def get_travel_name(travel_plan):
    country_name = travel_plan.country.name
    date_start = travel_plan.date_start.strftime('%d/%m/%Y')
    date_end = travel_plan.date_end.strftime('%d/%m/%Y')
    return f'{country_name}: {date_start}-{date_end}'



@bp.route('/add_expenditure/<travel_plan_id>', methods=['GET', 'POST'])
def add_expenditure(travel_plan_id):

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    page_title = 'Добавить статью затрат'
    form = AddExpanditureForm()
    travel_plan = Travel_plan.query.get(travel_plan_id)
          
    if not travel_plan or travel_plan.user_id != current_user.id:
        flash('Путешествие не найдено')
        return redirect(url_for('index'))
    name_travel = get_travel_name(travel_plan)
   
    new_expenditure = Expenditures(
        travel_plan_id=travel_plan_id,
        text=form.name.data,
        sum_plan=form.sum_plan.data,
        sum_real=form.sum_real.data)
    if form.validate_on_submit():

        db.session.add(new_expenditure)
        db.session.commit()
        flash('Вы добавили статью затрат')
        return redirect(
            url_for(
                'plan.travel_plan_info',
                travel_plan_id=travel_plan_id))

    return render_template(
        'expenditure/add_expenditure.html',
        page_title=page_title,
        name_travel=name_travel,
        form=form)


@bp.route('/edit_expenditure/<expenditure_id>', methods=['GET', 'PUT', 'POST'])
def edit_expenditure(expenditure_id):
    
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
        
    page_title = 'Изменить статью затрат'
    form = EditExpanditureForm()
    expenditure = Expenditures.query.get(expenditure_id)
    name_travel = get_travel_name(expenditure.travel_plan)
   
    if not expenditure or expenditure.travel_plan.user_id != current_user.id:
        flash('Данных не найдено')
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        
        form.name.data = expenditure.text
        form.sum_plan.data = expenditure.sum_plan
        form.sum_real.data = expenditure.sum_real
        
    elif form.validate_on_submit():

        expenditure.text = form.name.data
        expenditure.sum_plan = form.sum_plan.data
        expenditure.sum_real = form.sum_real.data
        db.session.commit()
        flash('Изменения сохранены')
        return redirect(
            url_for(
                'plan.travel_plan_info',
                travel_plan_id=expenditure.travel_plan_id))

    

    return render_template(
        'expenditure/edit_expenditure.html',
        page_title=page_title,
        name_travel=name_travel,
        form=form)


@bp.route('/delete_expenditure/<expenditure_id>', methods=[ 'GET','POST'])
def delete_expenditure(expenditure_id):

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    page_title = 'Удалить статью затрат'
    expenditure = Expenditures.query.get(expenditure_id)
    name = expenditure.text
    form = DeleteExpanditureForm()
    if not expenditure or expenditure.travel_plan.user_id != current_user.id:
        flash('Данных не найдено')
        return redirect(url_for('index'))
    if form.validate_on_submit():
        if form.submit.data:
            db.session.delete(expenditure)
            db.session.commit()
            flash('Пункт плана удален')
            return redirect(url_for(
                    'plan.travel_plan_info',
                    travel_plan_id=expenditure.travel_plan_id))
        elif form.cancel.data:
            return redirect(url_for(
                    'plan.travel_plan_info',
                    travel_plan_id=expenditure.travel_plan_id))
       
    
    return render_template(
        'expenditure/delete_expenditure.html',
        page_title=page_title,
        name=name,
        form=form)
