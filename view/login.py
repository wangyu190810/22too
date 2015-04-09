# -*-coding: utf-8-*-

__author__ = 'wangyu'

from flask import render_template, redirect, g, session, request

from model.user import User


def login():
    if request.method == "GET":
        return render_template("login.html")

    username, password = map(request.form.get, ("username", "password"))
    check = User.check_user(g.db, username, password)
    if check:
        session["username"] = username
        return redirect("/edit")
    return u'用户名密码错误'


def logout():
    session.pop("username")
    return redirect("/index")