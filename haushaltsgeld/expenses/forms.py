# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired
from wtforms.widgets.html5 import NumberInput

from .models import Stores


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
    date= DateField(
        'Date',
        validators=[InputRequired()],
    )
    submit = SubmitField('Record')
