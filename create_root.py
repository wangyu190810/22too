# -*-coding: utf-8-*-

__author__ = 'wangyu'

from model.user import User
from app import app


def root():
    username = raw_input("username: ")
    password = raw_input("password: ")
    repassword = raw_input("repassword: ")
    while password != repassword:
        print
        print u'# 密码不一致，请重新输入'
        print
        password = raw_input("password: ")
        repassword = raw_input("repassword: ")

        user = User(username=username)
        user.set_password(password)
        app.DBSession.add(user)
        app.DBSession.commit()


if __name__ == '__main__':
    root()