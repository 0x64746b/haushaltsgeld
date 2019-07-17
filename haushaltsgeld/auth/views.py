# coding: utf-8

from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'Welcome'


@auth.route('/logout')
def logout():
    return 'Goodbye'

