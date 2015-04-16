# -*-coding: utf-8-*-

__author__ = 'wangyu'

from sqlalchemy import Column, Integer, TEXT

from .base import Base


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(TEXT)
    user_name = Column()
