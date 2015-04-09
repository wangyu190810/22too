# -*-coding: utf-8-*-

__author__ = 'wangyu'

from ..model.base import Base
from ..application import app


Base.metadata.create_all(app.sa_engine)