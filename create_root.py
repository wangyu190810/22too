# -*-coding: utf-8-*-

__author__ = 'wangyu'

from model.user import User
from app import app


def root():
    username = raw_input("username: ")
    password = raw_input("password: ")
    repassword = raw_input("repassword: ")
    if password == repassword:
        user = User(username=username)
        user.set_password(password)
        app.DBSession.add(user)
        app.DBSession.commit()
    else:
        return 

root()