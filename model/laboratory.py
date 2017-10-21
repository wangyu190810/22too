# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from datetime import date

from sqlalchemy import Column, Integer, TEXT,Date,VARCHAR
from sqlalchemy.types import JSON
from .base import Base


class Laboratory(Base):
    __tablename__ = "laboratory"
    key = Column(VARCHAR(30),primary_key=True)
    content = Column(JSON)
    system_time = Column(Date,default= lambda :date.today())

    @classmethod
    def insert(cls,connection,key=None,json_data=None):
        lab = Laboratory(key=key,content=json_data)
        connection.add(lab)
        connection.commit()

    @classmethod
    def get_data(cls, connection, key):
        return connection.query(Laboratory).filter(Laboratory.key==key).limit(1).first()

    @classmethod
    def show_last(cls, connection):
        return connection.query(Laboratory.key,Laboratory.content).order_by(Laboratory.system_time.desc()).limit(1).first()

    @classmethod
    def show_all(cls, connection, index=1, size=15):
        start = (index -1 ) * size
        end = index * size - 1
        return connection.query(Laboratory).order_by(Laboratory.system_time.desc()).all()
