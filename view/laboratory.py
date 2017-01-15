# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from flask import render_template, request, g, redirect, jsonify

from model.laboratory import Laboratory
from lib.decorator import validate_user_login


def index_template():
    lab_data = Laboratory.show_all(g.db)
    print(lab_data)
    return render_template("laboratory.html",json_data = lab_data)


@validate_user_login
def add_lab():
    if request.method == "GET":
        return render_template("admin/add_lab.html")
    else:
        key ,values = map(request.form.get,("key","values"))
        stmt = Laboratory.get_data(g.db, key)
        if stmt:
            return jsonify(data=stmt.content)

        Laboratory.insert(g.db,key=key,json_data={"data":values})
        return render_template("laboratory.html")
                
def api_lib_index():
    stmt =  Laboratory.show_last(g.db)
    if stmt:
        print(dir(stmt))
        key = stmt.key
        data = stmt.content
        return jsonify(data=data, key=key)
    else:
        return jsonify({"data":""})

def api_lib_data(json_key):
    stmt = Laboratory.get_data(g.db, json_key)
    if stmt:
        # stmt = stmt[0]
        return jsonify(data=stmt.content)
    else:
        return jsonify({"data":""})
    # for row in stmt:
    #     if row is None:
    #         return jsonify({"data":"false"})
    # else:
    #     return jsonify(data=row)

