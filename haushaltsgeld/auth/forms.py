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

    def validate_password(self, field):
        user = resolve_user(self.username.data)
        if not user or not user.is_correct_password(self.password.data):
            raise ValidationError(self.INVALID_CREDENTIALS_MSG)
