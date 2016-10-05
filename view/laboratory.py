# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from flask import render_template, request, g, redirect, jsonify

from model.laboratory import Laboratory
from lib.decorator import validate_user_login


def index_template():
    return render_template("laboratory.html")


@validate_user_login
def add_lab():
    if request.method == "GET":
        return render_template("admin/add_lab.html")
    else:
        key ,values = map(request.form.get,("key","values"))
        Laboratory.insert(g.db,key=key,json_data={"data":values})
        return render_template("laboratory.html")

def api_lib_index():
    stmt =  Laboratory.show_last(g.db)
    if stmt:
        stmt = stmt[0]
        return jsonify(data=stmt)
    else:
        return jsonify({"data":""})
