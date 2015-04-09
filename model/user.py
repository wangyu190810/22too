# -*-coding: utf-8-*-

__author__ = 'wangyu'

from sqlalchemy import Column, String, Integer

from .base import Base


class User(Base):
    __tablename__ = "bloguser"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80))
    password = Column(String(80))
    email = Column(String(80))

    @classmethod
    def addUser(cls, connection, username, password, email=None):
        user = User(username=username, password=password, email=email)
        connection.add(user)
        connection.commit()

    @classmethod
    def checkUser(cls, connection, username, password):
        q = connection.query(User).filter_by(username=username).filter_by(password=password)
        return connection.execute(q).scalar()