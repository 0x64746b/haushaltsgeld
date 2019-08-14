# coding: utf-8

from flask import current_app, render_template
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from haushaltsgeld.auth.forms import LoginForm
from haushaltsgeld.auth.models import resolve_user
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(resolve_user(form.username.data))  # The form validation checked the credentials
        return redirect(current_app.config['INDEX_PAGE'])

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')

