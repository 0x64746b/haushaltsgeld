# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.validators import InputRequired
from wtforms.widgets.html5 import NumberInput

from haushaltsgeld.models import Stores


class ExpenseForm(FlaskForm):
    amount = DecimalField(
        'Amount',
        widget=NumberInput(min=0.01, step=0.01),
        validators=[InputRequired()]
    )
    store = SelectField(
        'Store',
        choices=[(store, store.name.title()) for store in Stores],
        coerce=lambda value: value if isinstance(value, Stores) else Stores[value or Stores.unspecified.name]
    )
    submit = SubmitField('Record')
