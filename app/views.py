from flask import request, render_template, url_for, redirect, flash
from app import models, db, app


def index():
    transactions = models.Transactions.query.all()
    return render_template('index-card.html', transactions=transactions)


def add_transaction():
    transactions = models.Transactions.query.all()
    if request.method == 'POST':
        period = request.args.get('period')
        value = request.args.get('value')
        status = request.args.get('status')
        unit = request.args.get('unit')
        subject = request.args.get('subject')
        new_transaction = models.Transactions(period=period, value=value, status=status, unit=unit, subject=subject)
        db.session.add(new_transaction)
        db.session.commit()
        return render_template('add_transaction.html', transactions=transactions)
    return redirect(url_for('index'))

