#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template, redirect, url_for, request, session
from flask_login import login_user, logout_user, login_required

from app_name.models.user import User

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

from app_name.extensions import login_manager
@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@auth.route('/', methods=['GET'])
def login():
    return render_template('auth/login.html')

@auth.route('/', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None:
        print("Could not find user")
        return redirect(url_for('auth.login'))

    if user.check_password(password) == False:
        print("Wrong password")
        return redirect(url_for('auth.login'))

    # TODO: implement remember
    remember = False
    login_user(user, remember=remember)

    session.permanent = True
    session.modified  = True

    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    # Logout the user
    logout_user()

    # Redirect back to login page
    return redirect(url_for('auth.login'))