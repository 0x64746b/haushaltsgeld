# coding: utf-8

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('haushaltsgeld.default_settings')
    app.config.from_envvar('HAUSHALTSGELD_SETTINGS', silent=True)

    from .views import expenses
    app.register_blueprint(expenses)

    from .models import db
    db.init_app(app)
    db.create_all(app=app)

    return app
