from app.models import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app.user.forms import LoginForm, RegistrationForm
from app.user.models import User
from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
def login():
    page_title = 'Вход в органайзер путешественника'

    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template(
        'user/login.html',
        page_title=page_title,
        title=page_title,
        form=login_form)


@bp.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@bp.route('/logout')
def logout():
    flash('Вы вышли')
    logout_user()
    return redirect(url_for('index'))


@bp.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template(
        'user/registration.html',
        page_title=title,
        form=form)


@bp.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        flash('Пожалуйста, исправьте ошибки в форме')
        return redirect(url_for('user.register'))
