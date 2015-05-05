# -*-coding:utf-8-*-
__author__ = 'Administrator'
from flask import g,session,render_template

from model.blog import Blog
from lib.decorator import validate_user_login


@validate_user_login
def admin_index():
    return render_template("admin.html", blogs=Blog.admin_index(g.db))