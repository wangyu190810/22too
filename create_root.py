# -*-coding: utf-8-*-

__author__ = 'wangyu'

from model.user import User
from application import app


def root():
    username = raw_input("username")
    password = raw_input("password")
    user = User(username=username, password=password)
    app.DBSession.add(user)
    app.DBSession.commit()

root()