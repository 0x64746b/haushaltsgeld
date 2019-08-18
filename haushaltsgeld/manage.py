# coding: utf-8

from getpass import getpass

import click
from click import BadParameter
from sqlalchemy.orm.exc import NoResultFound

from haushaltsgeld import create_app
from haushaltsgeld.auth.models import User
from haushaltsgeld.expenses import get_database


application = create_app()


@application.shell_context_processor
def make_shell_context():
    return {
        'db': get_database(),
        'User': User,
    }

@application.cli.command(help="Add a user")
@click.argument('username')
def add_user(username):
    if User.query.filter_by(username=username).one_or_none():
        raise BadParameter(f"There already is a user with name '{username}'")

    password = getpass()
    new_user = User(username=username, password=password)

    db = get_database()
    db.session.add(new_user)
    db.session.commit()

@application.cli.command(help="Change the password of a user")
@click.argument('username')
def change_password(username):
    try:
        user = User.query.filter_by(username=username).one()
    except NoResultFound:
        raise BadParameter(f"There is no user with name '{username}'")

    password = getpass('New password: ')
    user.set_password(password)

    db = get_database()
    db.session.add(user)
    db.session.commit()
