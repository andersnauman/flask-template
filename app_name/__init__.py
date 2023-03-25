#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

from app_name.extensions import db, login_manager
from app_name.config import DevConfig

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevConfig)

    login_manager.init_app(app)

    db.init_app(app)

    from app_name.models.user import User

    with app.app_context():
        db.create_all()
        session = db.session()

        # Install default users if the database is empty
        if len(session.query(User).all()) == 0:
            from app_name.models.user import setup as user_setup
            user_setup(session)
        else:
            print(session.query(User).all())     

    from app_name.auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app_name.main.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Error handling. Present a more generic page than default
    @app.errorhandler(404)
    def _404(e):
        return render_template('404.html')
    
    return app

