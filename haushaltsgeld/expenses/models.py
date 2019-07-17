# coding: utf-8

from datetime import datetime
from enum import Enum

import pytz

from .. import db
from ..auth.models import User


class Stores(Enum):
    unspecified = 0
    aldi = 1
    lidl = 2
    rewe = 3
    edeka = 4
    budni = 5
    other = 6

    def __str__(self):
        return self.name


class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(pytz.utc),
    )
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User, backref=db.backref('expenses'), lazy=True)
    amount = db.Column(db.Float(precision=2, asdecimal=True), nullable=False)
    store = db.Column(db.Enum(Stores), nullable=False)

    def __repr__(self):
        return f'<Expense {self.amount}>'
