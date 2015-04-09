# -*-coding: utf-8-*-

__author__ = 'wangyu'

from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base()
