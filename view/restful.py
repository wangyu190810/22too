# -*-coding: utf-8-*-

__author__ = 'wangyu'

from flask import render_template, request, g, redirect, jsonify

from model.blog import Blog
from lib.decorator import validate_user_login
from lib.utils import allow_cross_domain

@allow_cross_domain
def api_blog(blog_id):
    return jsonify(blogs=Blog.blog(g.db, blog_id=blog_id, status=1))


@allow_cross_domain
def api_blog_tag_title(name):
    return jsonify(blogs=Blog.blog_tag_title(g.db, name))


@allow_cross_domain
def api_index():
    datas = Blog.index(g.db).all()
    resp_data = []
    for data in datas:
        resp_data.append(
            dict(
                title=data.title,
                content_md=data.content_md,
                content_html=data.content_html,
                date=str(data.date),
            )
        )

    return jsonify(blogs=resp_data)


@allow_cross_domain
def api_archs():
    dates = Blog.get_arch_dates(g.db)
    return jsonify(archs=dates)
