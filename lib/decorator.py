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

from datetime import time, tzinfo,timedelta


def get_time(date):
    int_date = str(date).split("-")
    return int_date




class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1)

    def dst(self, dt):
        return timedelta(0)

    @classmethod
    def tzname(cls, dt):
        return "Europe/Prague"
