#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app_name.extensions import db

from flask_login import UserMixin

from sqlalchemy_utils import PasswordType
from sqlalchemy_utils import force_auto_coercion

force_auto_coercion()

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
        ],
    ))

    def check_password(self, password):
        return self.password == password

    def __repr__(self):
        return f'<Name "{self.name}", Username "{self.username}", Password: "{self.password}">, Cubicle "{self.cubicles}"'

def setup(session):
    users = [
        {
            "name": "Bob Bobsson",
            "username": "user1",
            "password": "test",
        },   
    ]
    try:
        for user in users:
            u = User()
            u.name = user["name"]
            u.username = user["username"]
            u.password = user["password"]
            session.add(u)
            session.commit()

    except Exception as e:
        print(e)
