# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, ValidationError

from haushaltsgeld.auth.models import resolve_user, User


class LoginForm(FlaskForm):

    authenticated_user: User = None

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
            self.authenticated_user = None
            raise ValidationError('Username or password are invalid')

        self.authenticated_user = user
