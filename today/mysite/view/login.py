__author__ = 'wangyu'
from flask import render_template,redirect,g,session,request

from mysite.model.user import User


def login():
    if request.method == "GET":
        return render_template("login.html")

    username, password =  map(request.form.get,("username","password"))
    print username,password
    userLogin = User.checkUser(g.db,username,password)
    if userLogin:
        session["username"] = username
        print session
        return redirect("/edit")
    return redirect("/index")




def logout():
    session.pop("username")
    return redirect("/index")



