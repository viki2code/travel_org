from app import app, db
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from app.expenditure.forms import AddExpanditureForm, EditExpanditureForm
from app.models import Travel_plan, Expenditures, Country, User
from flask_login import current_user, login_user, logout_user, login_required
from app.expenditure import bp


@bp.route('/add_expenditure/<travel_plan_id>', methods=['GET', 'POST'])
def add_expenditure(travel_plan_id):
    form = AddExpanditureForm()
    travel_plan = Travel_plan.query.get(travel_plan_id)
    page_title = 'Добавить статьи затрат для путешествия в страну '
    country_name = Country.query.get(travel_plan.country_id).name
    date_start = travel_plan.date_in
    date_end = travel_plan.date_out
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
                'expenditure.add_expenditure',
                travel_plan_id=travel_plan_id))

    return render_template(
        'expenditure/add_expenditure.html',
        page_title=page_title,
        country_name=country_name,
        date_start=date_start,
        date_end=date_end,
        form=form)


@bp.route('/edit_expenditure/<expenditure_id>', methods=['GET', 'PUT', 'POST'])
def edit_expenditure(expenditure_id):
    form = EditExpanditureForm()
    expenditure = Expenditures.query.get(expenditure_id)
    print(expenditure)

    if expenditure is None:

        flash('Данных не найдено')
        return redirect(url_for('index'))

    if form.validate_on_submit():

        expenditure.text = form.name.data
        expenditure.sum_plan = form.sum_plan.data
        expenditure.sum_real = form.sum_real.data
        db.session.commit()
        flash('Изменения сохранены')
        return redirect(
            url_for(
                'expenditure.edit_expenditure',
                expenditure_id=expenditure_id))

    elif request.method == 'GET':
        form.name.data = expenditure.text
        form.sum_plan.data = expenditure.sum_plan
        form.sum_real.data = expenditure.sum_real
    elif request.method == 'PUT':

        form.name.data = expenditure.text
        form.sum_plan.data = expenditure.sum_plan
        form.sum_real.data = expenditure.sum_real
        flash('Изменения сохранены')
        return redirect(
            url_for(
                'expenditure.edit_expenditure',
                expenditure_id=expenditure_id))

    return render_template(
        'expenditure/edit_expenditure.html',
        title='Edit plan',
        form=form)


@bp.route('/delete_expenditure/<expenditure_id>')
def delete(expenditure_id):
    expenditure = Expenditures.query.get(expenditure_id)
    if expenditure is None:
        flash('expenditure is not found.')
        return redirect(url_for('index'))
    db.session.delete(expenditure)
    db.session.commit()
    flash('Пункт плана удален')
    return redirect(url_for('index'))
