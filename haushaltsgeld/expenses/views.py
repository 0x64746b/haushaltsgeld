# coding: utf-8

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from . import expenses
from .forms import ExpenseForm
from .models import Expense, _db


@expenses.route('/', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()

    if form.validate_on_submit():
        expense = Expense(user=current_user)
        form.populate_obj(expense)

        _db.session.add(expense)
        _db.session.commit()

        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)


@expenses.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get(id)

    if current_user != expense.user:
        flash("You can only edit entries that belong to you", category="danger")
        return redirect(url_for('expenses.list_expenses'))

    form = ExpenseForm(obj=expense)

    if form.validate_on_submit():
        form.populate_obj(expense)
        _db.session.commit()

        return redirect(url_for('expenses.list_expenses'))

    return render_template('add.html', form=form)


@expenses.route('/list')
@login_required
def list_expenses():
    return render_template('list.html', expenses=Expense.query.all())


@expenses.route('/service-worker.js')
def serve_service_worker():
    return expenses.send_static_file('dist/js/service-worker.js')
