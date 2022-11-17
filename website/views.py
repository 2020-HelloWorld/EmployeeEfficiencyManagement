from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Employee
from . import db
import json
from datetime import date
from .models import Note

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        new_employee = Employee(email=email, first_name=first_name)
        db.session.add(new_employee)
        db.session.commit()
        flash('New employee Added!', category='success')
        print("Employee: ",Employee)
    return render_template("home.html",user=current_user)


@views.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    today = date.today()
    return render_template("feedback.html", user=current_user,date=today)
