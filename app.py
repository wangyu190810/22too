# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import timedelta

from flask import Flask, g, current_app
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from config import Config
from view.toole import google
from view.login import logout
from view import login
from view.blog import index, edit, search, arch, blog, blog_tag, blog_classify, blog_change


app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db

app.sa_engine = create_engine(Config.db)
app.DBSession = scoped_session(sessionmaker(bind=app.sa_engine))

app.add_url_rule("/", view_func=index, methods=["GET", "POST"])
app.add_url_rule("/edit", view_func=edit, methods=["GET", "POST"])
app.add_url_rule("/change/<int:blog_id>", view_func=blog_change, methods=["GET", "POST"])
app.add_url_rule("/search", view_func=search, methods=["GET"])

app.add_url_rule("/arch", view_func=arch, methods=["GET"])
app.add_url_rule("/blog/<int:blog_id>", view_func=blog, methods=["GET", "POST"])
app.add_url_rule("/tag/<tag>", view_func=blog_tag, methods=["GET", "POST"])
app.add_url_rule("/classify/<name>", view_func=blog_classify, methods=["GET", "POST"])


app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=logout, methods=["GET", "POST"])

app.add_url_rule("/googlefad2f2add41d5dac.html", view_func=google)


@app.before_request
def _before_request():
    g.db = current_app.DBSession()


@app.teardown_request
def teardown_request(*args, **kwargs):
    current_app.DBSession.remove()
    g.db.close()