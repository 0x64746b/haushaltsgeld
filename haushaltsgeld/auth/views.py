# coding: utf-8
import http

from flask import abort, flash, render_template, request, url_for
from flask_login import login_user, logout_user
from is_safe_url import is_safe_url
from werkzeug.utils import redirect

from haushaltsgeld.auth.forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        next_url = request.args.get('next', '/')
        if not is_safe_url(next_url, (request.host_url,)):
            abort(http.HTTPStatus.BAD_REQUEST, 'Invalid Login Attempt')

        login_user(form.authenticated_user)  # The form validation checked the credentials
        return redirect(next_url)

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You\'ve been successfully logged out', category='success')
    return redirect(url_for('auth.login'))

