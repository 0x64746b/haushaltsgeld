# coding: utf-8

from flask import Blueprint, redirect, render_template, request

from haushaltsgeld.forms import ExpenseForm

expenses = Blueprint('expense', __name__)


@expenses.route('/', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()

    if request.method == 'POST' and form.validate():
        return redirect(list_expenses)

    return render_template('add.html', form=form)

@expenses.route('/list')
def list_expenses():
    return render_template('list.html')
