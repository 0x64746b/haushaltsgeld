# coding: utf-8

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('haushaltsgeld.default_settings')
    app.config.from_envvar('HAUSHALTSGELD_SETTINGS', silent=True)

    # Use the expenses blueprint to build this app.
    # It will take care of its own dependencies
    from . import expenses
    db = expenses.get_database()
    db.init_app(app)
    db.create_all(app=app)

    from .auth.views import auth
    app.register_blueprint(auth)

    from .auth import login_manager
    login_manager.init_app(app)

    from .expenses.views import expenses
    app.register_blueprint(expenses)

    return app
