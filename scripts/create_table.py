# -*-coding: utf-8-*-

__author__ = 'wangyu'

from blog.model.base import Base
from blog.application import app


Base.metadata.create_all(app.sa_engine)