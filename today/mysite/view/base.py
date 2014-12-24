__author__ = 'wangyu'
from flask import session,wrappers,redirect
from functools import wraps

def validate_user_login(func):
    @wraps(func)
    def _validate_user_login(*args,**kwargs):
        if "username" in session:
            return func(*args,**kwargs)
        return redirect("/login")
    return _validate_user_login


