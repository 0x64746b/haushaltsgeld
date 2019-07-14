# coding: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def add_expense():
    return render_template('add.html');

@app.route('/show')
def list_expenses():
    return render_template('list.html');
