# coding: utf-8

from flask import Blueprint

# This blueprint depends on the `auth` blueprint
# Provide coupled resources to be imported from here for internal use
from .. import auth
from ..auth.models import User


expenses = Blueprint('expenses', __name__, template_folder='templates')
_db = auth.get_database()


def get_database():
    # Register models on DB
    from . import models
    return _db
