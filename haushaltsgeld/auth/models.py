# coding: utf-8

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager
from haushaltsgeld import db


@login_manager.user_loader
def resolve_user(user_id):
    return User.query.filter_by(username=user_id).one_or_none()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False, index=True)
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

    def get_id(self):
        return self.username

    def __repr__(self):
        return f'<User {self.username}>'


