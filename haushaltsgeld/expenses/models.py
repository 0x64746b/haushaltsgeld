# coding: utf-8

from datetime import date
from enum import Enum

from . import User, _db


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


class Expense(_db.Model):
    __tablename__ = 'expenses'

    id = _db.Column(_db.Integer, primary_key=True)
    date = _db.Column(
        _db.Date(),
        nullable=False,
        default=lambda: date.today()
    )
    user_id = _db.Column(_db.Integer, _db.ForeignKey(User.id), nullable=False)
    user = _db.relationship(User, backref=_db.backref('expenses'), lazy=True)
    amount = _db.Column(_db.Float(precision=2, asdecimal=True), nullable=False)
    store = _db.Column(_db.Enum(Stores), nullable=False)

    def __repr__(self):
        return f'<Expense {self.amount}>'
