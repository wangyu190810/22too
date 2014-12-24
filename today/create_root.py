__author__ = 'wangyu'
from mysite.model.user import User
from mysite.application import app
from flask import g


def root():
    username = raw_input("username")
    password = raw_input("password")
    user = User(username=username,password=password)
    app.DBSession.add(user)
    app.DBSession.commit()

root()

