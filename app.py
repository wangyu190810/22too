# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import timedelta

from flask import Flask, g, current_app
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from config import Config
from view.toole import google,recent_feed
from view.login import login, logout
from view.blog import index, edit, search, blog, blog_classify_by_name, \
    blog_change, set_blog_status,get_blog_from_date,blog_tag_title
from view.admin import admin_index
from view.uploadimg import upload_file
from view.restful import api_index
from view import laboratory as lab

app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db

app.sa_engine = create_engine(Config.db,echo=False)
app.DBSession = scoped_session(sessionmaker(bind=app.sa_engine))

# ---- user -----
app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=logout, methods=["GET", "POST"])

# ---- blog -----
app.add_url_rule("/", view_func=index, methods=["GET", "POST"])
app.add_url_rule("/blog/<int:blog_id>", view_func=blog, methods=["GET", "POST"])
app.add_url_rule("/blog/<name>",view_func=blog_tag_title,methods=["GET"])
app.add_url_rule("/classify/<name>", view_func=blog_classify_by_name, methods=["GET", "POST"])
app.add_url_rule("/edit", view_func=edit, methods=["GET", "POST"])
app.add_url_rule("/change/<int:blog_id>", view_func=blog_change, methods=["GET", "POST"])
app.add_url_rule("/search", view_func=search, methods=["GET"])
app.add_url_rule("/status/<int:blog_id>",view_func=set_blog_status,methods=["POST"])
app.add_url_rule("/date_arch/<date>",view_func=get_blog_from_date,methods=["GET"])

# ----lab---
app.add_url_rule("/add_lab",view_func=lab.add_lab,methods=["GET","POST"])
app.add_url_rule("/index_lab",view_func=lab.index_template,methods=["GET"])
app.add_url_rule("/api/api_lib_index",view_func=lab.api_lib_index,methods=["GET"])
app.add_url_rule("/api/api_lib_data/<json_key>",view_func=lab.api_lib_data,methods=["GET"])
# app.add_url_rule("/tag/<tag>", view_func=blog_tag, methods=["GET", "POST"])

# ---- admin ----
app.add_url_rule("/admin", view_func=admin_index,methods=["GET"])
app.add_url_rule("/upload",view_func=upload_file,methods=["GET","POST"])


# ----tool----
app.add_url_rule("/googlefad2f2add41d5dac.html", view_func=google)
app.add_url_rule("/recent.atom", view_func=recent_feed)

# ----API-----
app.add_url_rule("/api/index", view_func=api_index)

@app.before_request
def _before_request():
    g.db = current_app.DBSession()


@app.teardown_request
def teardown_request(*args, **kwargs):
    current_app.DBSession.remove()
    g.db.close()