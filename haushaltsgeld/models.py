# coding: utf-8

from datetime import datetime
from enum import Enum

import pytz
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


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


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __init__(self, **kwargs):
        try:
            kwargs['password_hash'] = self._hash_password(kwargs.pop('password'))
        except KeyError:
            pass
        super().__init__(**kwargs)

    @staticmethod
    def _hash_password(password: str) -> str:
        return generate_password_hash(password)

    def set_password(self, password: str) -> None:
        self.password_hash = self._hash_password(password)

    def is_correct_password(self, candidate: str) -> bool:
        return check_password_hash(self.password_hash, candidate)

    def __repr__(self):
        return f'<User {self.username}>'


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

