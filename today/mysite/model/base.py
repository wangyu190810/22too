__author__ = 'wangyu'
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine,desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.schema import MetaData
from flask import g

from config import Config
import hashlib


from datetime import date

metadata = MetaData()
Base = declarative_base()
#
#
#
# @as_declarative(metadata=metadata)
# class Base(object):
#
#     @classmethod
#     def delete_blog(cls, id):
#         try:
#             g.db.query(cls).filter_by(id=id).delete()
#             g.db.commit()
#         except Exception, e:
#             g.db.rollback()
#             raise e
#
#
#     @classmethod
#     def add_blog(cls):
#         try:
#             g.db.add(cls)
#             g.gb.commit(cls)
#         except Exception, e:
#             g.db.rollback()
#             raise e
#
#     @classmethod
#     def index_blog(cls):
#         g.db.query(cls).filter_by(desc(cls.id)).limit(1)
#


