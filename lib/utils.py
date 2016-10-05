# -*-coding: utf-8-*-

__author__ = 'wangyu'

from random import choice
from string import ascii_letters
from flask import make_response
from functools import wraps
def random_string(length=8, letters=ascii_letters):
    return ''.join(choice(letters) for _ in range(length))


def allow_cross_domain(fun):
    '''接口做同源处理'''
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        rst.headers["Access-Control-Allow-Credentials"] = True

        return rst
    return wrapper_fun