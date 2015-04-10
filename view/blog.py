# -*-coding: utf-8-*-

__author__ = 'wangyu'

from flask import render_template, request, g, redirect, jsonify

from model.blog import Blog
from lib.decorator import validate_user_login


def index():
    return render_template("index.html", blogs=Blog.index(g.db))


@validate_user_login
def edit():
    if request.method == "GET":
        return render_template("edit.html")

    if request.method == "POST":
        title, classify, content_md, tag, img = map(request.form.get, ("title", "classify", "content_md", "tag", "img"))
        Blog.add_blog(g.db, title=title, content_md=content_md, classify=classify, tag=tag, img=img)
        return redirect("/")


def search():
    eq = request.form.getlist("eq")
    title = Blog.blog_list(g.db, eq)
    return jsonify(title)


def arch():
    return render_template("arch.html", blogs=Blog.blog_list(g.db))


def blog(blog_id):
    print blog_id
    return render_template("blog.html", blogs=Blog.blog(g.db, blog_id=blog_id, status=1))


def blog_tag(tag):
    return render_template("arch.html", blogs=Blog.blog_tag(g.db, tag))


def blog_classify(name):
    return render_template("arch.html", blogs=Blog.get_classify(g.db, name))


@validate_user_login
def blog_change(blog_id):
    if request.method == "GET":
        return render_template("change.html", blogs=Blog.blog(g.db, blog_id=blog_id))
    else:
        title, classify, content_md, tag, img, status = map(
            request.form.get,
            ("title", "classify", "content_md", "tag", "img", "status")
        )
        Blog.blog_change(g.db,
                         blog_id=blog_id,
                         title=title,
                         classify=classify,
                         content_md=content_md,
                         tag=tag, img=img,
                         status=status)
        return redirect("/")
