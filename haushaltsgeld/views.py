# coding: utf-8

from flask import Blueprint, redirect, render_template, request, url_for

from haushaltsgeld.forms import ExpenseForm

expenses = Blueprint('expenses', __name__)


@expenses.route('/', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()

    if request.method == 'POST' and form.validate():
        print(form.amount.data, type(form.amount.data))
        print(form.store.data, type(form.store.data))
        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)

@expenses.route('/list')
def list_expenses():
    return render_template('list.html')
