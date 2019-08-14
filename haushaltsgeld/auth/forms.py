# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, ValidationError

from haushaltsgeld.auth.models import resolve_user


class LoginForm(FlaskForm):

    INVALID_CREDENTIALS_MSG = 'Username or password are invalid'

    username = StringField(
        'Username',
        validators=[InputRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired()]
    )
    submit = SubmitField('Sign In')
