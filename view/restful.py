# -*-coding: utf-8-*-

__author__ = 'wangyu'

from flask import render_template, request, g, redirect, jsonify

from model.blog import Blog
from lib.decorator import validate_user_login
from lib.utils import allow_cross_domain

@allow_cross_domain
def api_index():
    dates = Blog.get_arch_dates(g.db)
    return jsonify.dumps(blogs = Blog.index(g.db))
    
    #return render_template("index.html", blogs=Blog.index(g.db), archs=dates)

@allow_cross_domain
def api_last():
    pass
    


@validate_user_login
@allow_cross_domain
def edit():
    if request.method == "GET":
        return render_template("admin/edit.html")

    if request.method == "POST":
        title, classify, content_md, tag, img,tag_title = map(request.form.get,

                                                    ("title", "classify", "content_md", "tag", "img","tag_title"))
        Blog.add_blog(g.db, title=title, content_md=content_md,
                      classify=classify, tag=tag, img=img,
                      tag_title=tag_title)
        return redirect("/")


def set_blog_status(blog_id):
    if request.method == "POST":
        data = request.form.get("status",int)
        if Blog.set_blog_status(g.db,blog_id,status=data):
            return jsonify(status="success")
    return jsonify(status="false")


def get_blog_from_date(date):
    if request.method == "GET":
        return render_template("date_arch.html", blogs=Blog.get_blog_form_data(g.db,date))
    return render_template("date_arch.html", blogs=None)


def blog(blog_id):
    return render_template("details.html", blogs=Blog.blog(g.db, blog_id=blog_id, status=1))


def blog_tag_title(name):
    return render_template("details.html",blogs=Blog.blog_tag_title(g.db,name))


def blog_classify_by_name(name):
    return render_template("index.html", blogs=Blog.get_classify(g.db, name))


def search():
    eq = request.form.getlist("eq")
    title = Blog.blog_list(g.db, eq)
    return jsonify(title)


def blog_classify_by_tag(tag):
    return render_template("index.html", blogs=Blog.blog_tag(g.db, tag))


def blog_classify_by_date(date):
    return render_template("index.html", blogs=Blog.blog_tag(g.db, date))


@validate_user_login
def blog_change(blog_id):
    if request.method == "GET":
        return render_template("admin/change.html", blogs=Blog.blog(g.db, blog_id=blog_id))
    else:
        title, classify, content_md, tag, img, status ,tag_title= map(
            request.form.get,
            ("title", "classify", "content_md", "tag", "img", "status","tag_title")
        )
        Blog.blog_change(g.db,
                         blog_id=blog_id,
                         title=title,
                         classify=classify,
                         content_md=content_md,
                         tag=tag, img=img,
                         status=status,
                         tag_title=tag_title)
        return redirect("/")

