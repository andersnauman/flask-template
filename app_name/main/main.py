#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template
from flask_login import login_required

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')

@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('main/index.html')