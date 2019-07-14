# coding: utf-8

from os import environ

"""Set Flask configuration vars from .env file."""

# Database
SQLALCHEMY_DATABASE_URI = environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'sqlite:///../haushaltsgeld.sqlite',
)
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS',
    False,
)
