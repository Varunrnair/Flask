from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from website.db import db   
from flask_login import login_user, login_required, logout_user, current_user

admin = Blueprint('admin', __name__)

# admin login
@admin.route('admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Admin.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("admin/login.html", user=current_user)