__author__ = 'wangyu'
from mysite.model.blog import Blog
from mysite.model.base import Base
from mysite.application import app

Base.metadata.create_all(app.sa_engine)


