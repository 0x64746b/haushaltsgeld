# coding: utf-8

from wtforms_alchemy import ModelForm

from haushaltsgeld.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
