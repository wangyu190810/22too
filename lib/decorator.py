# -*-coding: utf-8-*-

__author__ = 'wangyu'

from functools import wraps

from flask import session, redirect


def validate_user_login(func):
    @wraps(func)
    def _validate_user_login(*args, **kwargs):
        if "username" in session:
            return func(*args, **kwargs)
        return redirect("/login")
    return _validate_user_login