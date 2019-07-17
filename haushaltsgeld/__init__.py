# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from haushaltsgeld.auth import login_manager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('haushaltsgeld.default_settings')
    app.config.from_envvar('HAUSHALTSGELD_SETTINGS', silent=True)

    db.init_app(app)
    db.create_all(app=app)

    from .auth.views import auth
    app.register_blueprint(auth)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .views import expenses
    app.register_blueprint(expenses)

    return app
