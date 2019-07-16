# coding: utf-8

from flask import Blueprint, redirect, render_template, request, url_for

from haushaltsgeld.forms import ExpenseForm
from haushaltsgeld.models import Expense, User, db

expenses = Blueprint('expenses', __name__)


@expenses.route('/', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()

    if request.method == 'POST' and form.validate():
        db.session.add(
            Expense(
                user=User.query.first(),  # TODO: Use user from session
                amount=form.amount.data,
                store=form.store.data
            )
        )
        db.session.commit()
        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)

@expenses.route('/list')
def list_expenses():
    return render_template('list.html', expenses=Expense.query.all())
