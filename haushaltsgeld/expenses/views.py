# coding: utf-8

from flask import redirect, render_template, url_for
from flask_login import login_required

from . import expenses
from .forms import ExpenseForm
from .models import Expense, User, db


@expenses.route('/', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()

    if form.validate_on_submit():
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
@login_required
def list_expenses():
    return render_template('list.html', expenses=Expense.query.all())
