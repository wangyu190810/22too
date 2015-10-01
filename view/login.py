# -*-coding: utf-8-*-

__author__ = 'wangyu'

from flask import render_template, redirect, g, session, request, jsonify

from model.user import User


def login():
    if request.method == "GET":
        return render_template("admin/login.html")

    username, password = map(request.form.get, ("username", "password"))
    has_user = User.has_user(g.db, username)
    if has_user:
        check_password = User.check_password(g.db, username, password)
        if check_password:
            session["username"] = username
            return redirect("/admin")
        else:
            return jsonify(status=400, message=u'密码错误')
    return jsonify(status=400, message=u'用户名错误')


def logout():
    if session.get("username"):
        session.pop("username")
    return redirect("/")