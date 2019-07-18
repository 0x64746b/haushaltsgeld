# coding: utf-8

from flask import Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


auth = Blueprint(
    'auth',
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static'
)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

_db = SQLAlchemy()


def get_database():
    # Register models on DB
    from . import models
    return _db
