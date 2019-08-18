# coding: utf-8

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from . import expenses
from .forms import ExpenseForm
from .models import Expense, _db


@expenses.route('/', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()

    if form.validate_on_submit():
        _db.session.add(
            Expense(
                user=current_user,
                amount=form.amount.data,
                store=form.store.data,
                date=form.date.data,
            )
        )
        _db.session.commit()
        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)


@expenses.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get(id)
    form = ExpenseForm(obj=expense)

    if form.validate_on_submit():
        expense.amount = form.amount.data
        expense.store = form.store.data
        expense.date = form.date.data

        _db.session.add(expense)
        _db.session.commit()
        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)


@expenses.route('/list')
@login_required
def list_expenses():
    return render_template('list.html', expenses=Expense.query.all())
